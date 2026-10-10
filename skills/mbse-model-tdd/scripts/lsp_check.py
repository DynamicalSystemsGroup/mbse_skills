"""Exercise stdio LSP diagnostics with one outstanding document version at a time."""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import queue
import signal
import subprocess
import tempfile
import selectors
import threading
import time

try:
    from .engine_check import file_hash, load_profile, tool_environment
except ImportError:
    from engine_check import file_hash, load_profile, tool_environment

MAX_FRAME = 2 * 1024 * 1024


def encode_message(message):
    body = json.dumps(message, ensure_ascii=False).encode('utf-8')
    return f'Content-Length: {len(body)}\r\n\r\n'.encode() + body


def read_message(stream):
    headers = {}
    length = 0
    while True:
        line = stream.readline(8193)
        if not line:
            raise EOFError('LSP stream closed')
        length += len(line)
        if length > 8192:
            raise ValueError('LSP header too large')
        if line in (b'\r\n', b'\n'):
            break
        key, value = line.decode('ascii').split(':', 1)
        headers[key.lower()] = value.strip()
    size = int(headers['content-length'])
    if size < 0 or size > MAX_FRAME:
        raise ValueError('invalid LSP frame length')
    body = bytearray()
    while len(body) < size:
        block = stream.read(size - len(body))
        if not block:
            raise EOFError('incomplete LSP body')
        body.extend(block)
    value = json.loads(body)
    if not isinstance(value, dict):
        raise ValueError('LSP message must be an object')
    return value


class Session:
    def __init__(self, argv, timeout=30):
        self.timeout = timeout
        self.messages = []
        self.queue = queue.Queue()
        self.total = 0
        self.stderr_bytes = bytearray()
        self.output_limit = threading.Event()
        self.stderr_truncated = False
        self.proc = subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE, env=tool_environment(), start_new_session=True)
        self.worker = threading.Thread(target=self._read, daemon=True)
        self.worker.start()
        self.stderr_worker = threading.Thread(target=self._read_stderr, daemon=True)
        self.stderr_worker.start()
        os.set_blocking(self.proc.stdin.fileno(), False)

    def stop(self):
        try:
            os.killpg(self.proc.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass

    def _read_stderr(self):
        while block := self.proc.stderr.read(4096):
            remaining = 262144 - len(self.stderr_bytes)
            self.stderr_bytes.extend(block[:remaining])
            if len(block) > remaining:
                self.stderr_truncated = True
                self.output_limit.set()
                self.stop()
                break

    def _read(self):
        try:
            while True:
                message = read_message(self.proc.stdout)
                self.total += len(json.dumps(message).encode())
                if self.total > 8 * MAX_FRAME:
                    self.output_limit.set()
                    self.stop()
                    raise ValueError('LSP session output limit')
                self.queue.put(message)
        except Exception as error:
            self.queue.put(error)

    def send(self, message):
        self.messages.append({'direction': 'client', 'message': message})
        body = encode_message(message)
        if len(body) > MAX_FRAME:
            raise ValueError('client LSP frame too large')
        deadline = time.monotonic() + self.timeout
        with selectors.DefaultSelector() as selector:
            selector.register(self.proc.stdin, selectors.EVENT_WRITE)
            while body:
                left = deadline - time.monotonic()
                if left <= 0 or not selector.select(left):
                    self.stop()
                    raise TimeoutError('LSP write deadline exceeded')
                try:
                    count = os.write(self.proc.stdin.fileno(), body)
                except BlockingIOError:
                    continue
                body = body[count:]

    def wait(self, predicate):
        deadline = time.monotonic() + self.timeout
        while True:
            left = deadline - time.monotonic()
            if left <= 0:
                raise TimeoutError('LSP response deadline exceeded')
            try:
                message = self.queue.get(timeout=left)
            except queue.Empty as error:
                raise TimeoutError('LSP response deadline exceeded') from error
            if isinstance(message, Exception):
                raise message
            self.messages.append({'direction': 'server', 'message': message})
            if 'method' in message and 'id' in message:
                response = {'jsonrpc': '2.0', 'id': message['id']}
                if message['method'] == 'workspace/configuration':
                    response['result'] = [{} for _ in message.get('params', {}).get('items', [])]
                elif message['method'] in {'client/registerCapability', 'window/workDoneProgress/create'}:
                    response['result'] = None
                else:
                    response['error'] = {'code': -32601, 'message': 'method not supported by this test client'}
                self.send(response)
            if predicate(message):
                if 'error' in message:
                    raise ValueError(f'LSP error: {message["error"]}')
                return message

    def request(self, identifier, method, params=None):
        self.send({'jsonrpc': '2.0', 'id': identifier, 'method': method, 'params': params})
        return self.wait(lambda message: message.get('id') == identifier and 'method' not in message)

    def close(self):
        self.stop()
        self.proc.wait(timeout=5)
        self.worker.join(timeout=2)
        self.stderr_worker.join(timeout=2)
        self.proc.stdin.close()
        self.proc.stdout.close()
        self.proc.stderr.close()
        return self.stderr_bytes.decode(errors='replace')


def probe(argv, workspace, texts, timeout=30):
    session = Session(argv, timeout)
    uri = (Path(workspace) / 'rover.sysml').resolve().as_uri()
    report = {'argv': argv, 'state': 'unavailable', 'documents': []}
    try:
        initialized = session.request(1, 'initialize', {
            'processId': os.getpid(), 'rootUri': Path(workspace).resolve().as_uri(),
            'capabilities': {'textDocument': {'publishDiagnostics': {'versionSupport': True}},
                             'general': {'positionEncodings': ['utf-16']}},
            'initializationOptions': {'strictConformance': True}})
        report['capabilities'] = initialized['result']['capabilities']
        session.send({'jsonrpc': '2.0', 'method': 'initialized', 'params': {}})
        for version, text in enumerate(texts, 1):
            if version == 1:
                session.send({'jsonrpc': '2.0', 'method': 'textDocument/didOpen', 'params': {
                    'textDocument': {'uri': uri, 'languageId': 'sysml', 'version': version, 'text': text}}})
            else:
                session.send({'jsonrpc': '2.0', 'method': 'textDocument/didChange', 'params': {
                    'textDocument': {'uri': uri, 'version': version}, 'contentChanges': [{'text': text}]}})
            def matches(message):
                params = message.get('params', {})
                return (message.get('method') == 'textDocument/publishDiagnostics' and
                        params.get('uri') == uri and params.get('version', version) == version)
            params = session.wait(matches)['params']
            diagnostics = params['diagnostics']
            if not isinstance(diagnostics, list):
                raise ValueError('malformed diagnostic list')
            if any(not isinstance(d, dict) or 'range' not in d or 'message' not in d for d in diagnostics):
                raise ValueError('malformed diagnostic')
            report['documents'].append({
                'version': version, 'text_sha256': __import__('hashlib').sha256(text.encode()).hexdigest(),
                'version_basis': 'server-version' if 'version' in params else 'unversioned-publication',
                'diagnostics': diagnostics, 'has_errors': any(d.get('severity', 1) == 1 for d in diagnostics)})
        session.send({'jsonrpc': '2.0', 'method': 'textDocument/didClose', 'params': {'textDocument': {'uri': uri}}})
        session.request(2, 'shutdown')
        session.send({'jsonrpc': '2.0', 'method': 'exit'})
        session.proc.wait(timeout=5)
        report['state'] = 'completed' if session.proc.returncode == 0 else 'unavailable'
        report['version_correlated'] = all(d['version_basis'] == 'server-version' for d in report['documents'])
        report['exit_code'] = session.proc.returncode
    except (TimeoutError, EOFError, OSError, ValueError, KeyError, TypeError, subprocess.TimeoutExpired) as error:
        report['error'] = str(error)
    finally:
        report['stderr'] = session.close()
        report['transcript'] = session.messages
        report['stderr_truncated'] = session.stderr_truncated
        report['output_limit'] = session.output_limit.is_set()
        if session.output_limit.is_set():
            report['state'] = 'output-limit'
    return report


def run(profile_path, output, model):
    profile = load_profile(profile_path)
    valid = Path(model).read_text()
    invalid = 'package Rover { attribute broken : ; }'
    results = []
    with tempfile.TemporaryDirectory(prefix='mbse-lsp-') as directory:
        for engine in ('opensysml', 'toolkit'):
            argv = ([profile['engines']['opensysml-lsp']['executable'], '-strict', '-no-record-cache']
                    if engine == 'opensysml' else
                    [profile['engines']['toolkit']['executable'], 'lsp', '--lib', profile['library']])
            result = probe(argv, directory, [valid, invalid, valid])
            result['engine'] = engine
            # A same-session unversioned publication cannot prove edit correlation.
            # Corroborate each text in a fresh session containing only one document version.
            if result['state'] == 'completed' and not result.get('version_correlated'):
                isolated = []
                for text in [valid, invalid, valid]:
                    single = probe(argv, directory, [text])
                    isolated.append(single)
                result['isolated_text_checks'] = isolated
                evidence_ok = (all(r['state'] == 'completed' for r in isolated) and
                    [r['documents'][0]['has_errors'] if len(r['documents']) == 1 else None
                     for r in isolated] == [False, True, False])
                result['correlation_basis'] = 'fresh-session-per-text; edit publications remain unversioned'
            else:
                evidence_ok = result.get('version_correlated', False)
                result['correlation_basis'] = 'server-version'
            result['expectations_met'] = (result['state'] == 'completed' and evidence_ok and
                [d['has_errors'] for d in result['documents']] == [False, True, False])
            results.append(result)
    load_profile(profile_path)  # Verify executable and library bytes after the exchanges.
    report = {'captured_at_utc': datetime.now(timezone.utc).isoformat(),
              'helper_sha256': file_hash(__file__), 'profile_sha256': file_hash(profile_path), 'results': results,
              'expectations_met': all(r['expectations_met'] for r in results)}
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    Path(output).write_text(json.dumps(report, indent=2) + '\n')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile', required=True)
    parser.add_argument('--output', default='.local/rover-lsp.json')
    parser.add_argument('--model', required=True)
    args = parser.parse_args()
    try:
        result = run(args.profile, args.output, args.model)
    except (OSError, ValueError, KeyError) as error:
        parser.exit(2, f'{error}\n')
    print(json.dumps({'expectations_met': result['expectations_met'], 'output': args.output}))
    return 0 if result['expectations_met'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
