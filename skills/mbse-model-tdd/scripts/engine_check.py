"""Bounded local CLI checks. Native results remain the evidence of record."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import selectors
import time


def file_hash(path):
    digest = hashlib.sha256()
    with open(path, 'rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def library_hash(path):
    root = Path(path)
    files = sorted(p for p in root.rglob('*') if p.suffix in {'.sysml', '.kerml'})
    if not files:
        raise ValueError('library contains no SysML/KerML files')
    inventory = [(p.relative_to(root).as_posix(), file_hash(p)) for p in files]
    return hashlib.sha256(json.dumps(inventory, separators=(',', ':')).encode()).hexdigest()


def load_profile(path):
    profile = json.loads(Path(path).read_text())
    for name, entry in profile['engines'].items():
        if name not in {'opensysml', 'toolkit', 'opensysml-lsp'}:
            raise ValueError(f'unknown engine: {name}')
        executable = Path(entry['executable']).expanduser().resolve()
        if file_hash(executable) != entry['sha256']:
            raise ValueError(f'{name} executable hash mismatch')
        entry['executable'] = str(executable)
    library = Path(profile['library']).expanduser().resolve()
    if not library.is_dir():
        raise ValueError('library directory missing')
    if 'library_sha256' in profile and library_hash(library) != profile['library_sha256']:
        raise ValueError('library hash mismatch')
    profile['library'] = str(library)
    return profile


def tool_environment():
    # Explicit inputs; ambient model/library variables and credentials are excluded.
    cache = Path('.local/cache').resolve()
    cache.mkdir(parents=True, exist_ok=True)
    return {'PATH': os.defpath, 'LANG': 'C.UTF-8', 'TMPDIR': '/tmp',
            'XDG_CACHE_HOME': str(cache), 'SYSMLV2_LIB_CACHE': 'off',
            'OPENSYSML_RECORD_CACHE': '0'}


def execute(argv, timeout=30, max_bytes=262144):
    started = time.monotonic()
    try:
        proc = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                env=tool_environment(), start_new_session=True)
    except OSError as error:
        return {'argv': argv, 'state': 'launch-failed', 'exit_code': None,
                'stdout': '', 'stderr': str(error)}
    buffers = [bytearray(), bytearray()]
    selector = selectors.DefaultSelector()
    for stream, buffer in zip((proc.stdout, proc.stderr), buffers):
        os.set_blocking(stream.fileno(), False)
        selector.register(stream, selectors.EVENT_READ, buffer)
    state = 'completed'
    deadline = started + timeout
    def stop():
        try:
            os.killpg(proc.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
    try:
        while selector.get_map():
            left = deadline - time.monotonic()
            if left <= 0:
                state = 'timeout'
                stop()
                break
            for key, _ in selector.select(timeout=left):
                try:
                    block = os.read(key.fileobj.fileno(), 4096)
                except BlockingIOError:
                    continue
                if not block:
                    selector.unregister(key.fileobj)
                    continue
                remaining = max_bytes - len(key.data)
                key.data.extend(block[:remaining])
                if len(block) > remaining:
                    state = 'output-limit'
                    stop()
                    break
            if state == 'output-limit':
                break
        if state == 'completed':
            try:
                proc.wait(timeout=max(0.001, deadline - time.monotonic()))
            except subprocess.TimeoutExpired:
                state = 'timeout'
                stop()
        proc.wait(timeout=5)
    finally:
        # Kill descendants even if the immediate parent has already exited.
        stop()
        selector.close()
        proc.stdout.close()
        proc.stderr.close()
    return {'argv': argv, 'state': state, 'exit_code': proc.returncode,
            'stdout': buffers[0].decode('utf-8', errors='replace'),
            'stderr': buffers[1].decode('utf-8', errors='replace'),
            'elapsed_seconds': round(time.monotonic() - started, 4)}


def classify(engine, operation, code, stdout):
    """Interpret only pinned native contracts; exit zero alone cannot prove a check."""
    if engine == 'toolkit' and operation == 'verify':
        match = re.search(r'(\d+) satisfied, (\d+) violated, (\d+) undecided', stdout)
        if not match:
            return 'unavailable'
        held, failed, unknown = map(int, match.groups())
        if failed and code == 1:
            return 'violated'
        if unknown and code == 0:
            return 'undecided'
        return 'holds' if held and not failed and code == 0 else 'unavailable'
    try:
        payload = json.loads(stdout)
        if engine == 'opensysml' and operation == 'validate':
            diagnostics = payload['diagnostics'] or []
            if not isinstance(diagnostics, list):
                return 'unavailable'
            if code == 2 and any(d.get('severity') == 'error' for d in diagnostics if isinstance(d, dict)):
                return 'invalid'
            if code == 0 and payload['status'] == 'holds' and payload['exit'] == 0 and not payload['errors']:
                return 'valid'
            return 'unavailable'
        if engine == 'toolkit' and operation == 'validate':
            errors = payload['summary']['errors']
            if not isinstance(errors, int) or errors < 0 or not isinstance(payload['findings'], list):
                return 'unavailable'
            return 'invalid' if errors or code == 1 else ('valid' if code == 0 else 'unavailable')
        if engine == 'opensysml' and operation == 'verify':
            if code == 2:
                return 'unavailable'
            checks = payload['checks']
            if not isinstance(checks, list) or not checks:
                return 'unavailable'
            statuses = [check['status'] for check in checks]
            if code == 1 and 'fails' in statuses:
                return 'violated'
            if code == 0 and payload['status'] == 'holds' and all(s == 'holds' for s in statuses):
                return 'holds'
    except (ValueError, KeyError, TypeError):
        pass
    return 'unavailable'


def invocation(profile, engine, operation, model, subject):
    executable = profile['engines'][engine]['executable']
    if engine == 'opensysml':
        return ([executable, '-strict', '-no-record-cache', '-json', '-validate', str(model)]
                if operation == 'validate' else
                [executable, '-strict', '-no-record-cache', '-json', '-constraint', subject, str(model)])
    return [executable, 'check' if operation == 'validate' else 'verify',
            *(['--format', 'json'] if operation == 'validate' else []),
            '--lib', profile['library'], str(model)]


def run_suite(profile_path, manifest_path, output):
    profile = load_profile(profile_path)
    manifest_path = Path(manifest_path).resolve()
    manifest = json.loads(manifest_path.read_text())
    report = {'captured_at_utc': datetime.now(timezone.utc).isoformat(),
              'helper_sha256': file_hash(__file__), 'profile_sha256': file_hash(profile_path), 'manifest_sha256': file_hash(manifest_path),
              'engines': profile, 'runs': [], 'versions': {}}
    for engine in ('opensysml', 'toolkit'):
        flag = '-version' if engine == 'opensysml' else '--version'
        report['versions'][engine] = execute([profile['engines'][engine]['executable'], flag])
        for case in manifest['cases']:
            model = (manifest_path.parent / case['model']).resolve()
            before = file_hash(model)
            validation = execute(invocation(profile, engine, 'validate', model, manifest['subject']))
            validation['outcome'] = (classify(engine, 'validate', validation['exit_code'], validation['stdout'])
                                     if validation['state'] == 'completed' else 'unavailable')
            row = {'engine': engine, 'case': case['id'], 'model_sha256': before, 'validation': validation}
            wanted = case['expected_validation']
            if isinstance(wanted, dict):
                wanted = wanted[engine]
            row['expectation_met'] = validation['outcome'] == wanted
            if wanted == 'valid' and validation['outcome'] == 'valid':
                verdict = execute(invocation(profile, engine, 'verify', model, manifest['subject']))
                verdict['outcome'] = (classify(engine, 'verify', verdict['exit_code'], verdict['stdout'])
                                      if verdict['state'] == 'completed' else 'unavailable')
                row['verification'] = verdict
                expected_verdict = case['expected_verification']
                if isinstance(expected_verdict, dict):
                    expected_verdict = expected_verdict[engine]
                row['expectation_met'] &= verdict['outcome'] == expected_verdict
            if file_hash(model) != before:
                raise ValueError('model changed during capture')
            report['runs'].append(row)
        if file_hash(profile['engines'][engine]['executable']) != profile['engines'][engine]['sha256']:
            raise ValueError('engine changed during capture')
    if library_hash(profile['library']) != profile['library_sha256']:
        raise ValueError('library changed during capture')
    report['expectations_met'] = all(row['expectation_met'] for row in report['runs'])
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    Path(output).write_text(json.dumps(report, indent=2) + '\n')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile', required=True)
    parser.add_argument('--manifest', default='examples/rover/cases.json')
    parser.add_argument('--output', default='.local/rover-cli.json')
    args = parser.parse_args()
    try:
        report = run_suite(args.profile, args.manifest, args.output)
    except (OSError, ValueError, KeyError) as error:
        parser.exit(2, f'{error}\n')
    print(json.dumps({'expectations_met': report['expectations_met'], 'runs': len(report['runs']), 'output': args.output}))
    return 0 if report['expectations_met'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
