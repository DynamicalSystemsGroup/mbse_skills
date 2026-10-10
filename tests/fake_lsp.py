"""Regression fixture; invoked as a local stdio server, not an engine."""
import json
import sys


def send(message):
    raw = json.dumps(message).encode()
    sys.stdout.buffer.write(f'Content-Length: {len(raw)}\r\n\r\n'.encode() + raw)
    sys.stdout.buffer.flush()

while True:
    headers = {}
    while True:
        line = sys.stdin.buffer.readline()
        if not line:
            sys.exit(0)
        if line == b'\r\n':
            break
        key, value = line.decode().split(':', 1)
        headers[key.lower()] = value.strip()
    message = json.loads(sys.stdin.buffer.read(int(headers['content-length'])))
    method = message.get('method')
    if method == 'initialize':
        send({'jsonrpc': '2.0', 'id': message['id'], 'result': {'capabilities': {'textDocumentSync': 1}}})
    elif method == 'textDocument/didOpen':
        document = message['params']['textDocument']
        for errors in [False, True, False]:
            # All three publications belong to didOpen. This server ignores changes.
            send({'jsonrpc': '2.0', 'method': 'textDocument/publishDiagnostics', 'params': {
                'uri': document['uri'], 'diagnostics': [{'severity': 1, 'message': 'stale',
                'range': {'start': {'line': 0, 'character': 0}, 'end': {'line': 0, 'character': 1}}}] if errors else []}})
    elif method == 'shutdown':
        send({'jsonrpc': '2.0', 'id': message['id'], 'result': None})
    elif method == 'exit':
        sys.exit(0)
