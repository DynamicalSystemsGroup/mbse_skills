import json
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skills/mbse-model-tdd/scripts"))
from engine_check import classify, execute, file_hash, load_profile
from lsp_check import read_message, encode_message
import io
import time
from unittest.mock import patch
import lsp_check

class ToolsTests(unittest.TestCase):
    def test_opensysml_false_is_not_unavailable(self):
        self.assertEqual(classify('opensysml', 'verify', 1, json.dumps({'status':'fails','checks':[{'status':'fails'}]})), 'violated')
        self.assertEqual(classify('opensysml', 'verify', 2, '{}'), 'unavailable')
    def test_opensysml_exit_zero_needs_actual_check(self):
        for output in ['{}', 'broken', '{"status":"holds","checks":[]}']:
            self.assertEqual(classify('opensysml', 'verify', 0, output), 'unavailable')
    def test_toolkit_undecided_does_not_pass(self):
        self.assertEqual(classify('toolkit', 'verify', 0, '0 satisfied, 0 violated, 1 undecided'), 'undecided')
        self.assertEqual(classify('toolkit', 'verify', 0, '0 satisfied, 0 violated, 0 undecided'), 'unavailable')
        self.assertEqual(classify('toolkit', 'verify', 1, '0 satisfied, 1 violated, 0 undecided'), 'violated')
    def test_opensysml_validation_requires_native_evidence(self):
        self.assertEqual(classify('opensysml','validate',0,''),'unavailable')
        self.assertEqual(classify('opensysml','validate',2,'{}'),'unavailable')
        self.assertEqual(classify('opensysml','validate',2,'{"diagnostics":[{"severity":"error"}]}'),'invalid')
        self.assertEqual(classify('opensysml','validate',0,'{"status":"holds","exit":0,"diagnostics":null,"errors":null}'),'valid')

    def test_toolkit_diagnostics_count_errors(self):
        self.assertEqual(classify('toolkit', 'validate', 0, '{"summary":{"errors":2},"findings":[]}'), 'invalid')
        self.assertEqual(classify('toolkit', 'validate', 0, '{}'), 'unavailable')
    def test_timeout_and_missing_executable(self):
        self.assertEqual(execute([sys.executable,'-c','import time; time.sleep(2)'], timeout=.05)['state'], 'timeout')
        self.assertEqual(execute(['/no/such/engine'])['state'], 'launch-failed')
    def test_output_cap(self):
        result=execute([sys.executable,'-c','print("x"*10000)'], max_bytes=100)
        self.assertEqual(result['state'], 'output-limit')
        self.assertLessEqual(len(result['stdout'].encode()),100)
    def test_profile_hash_mismatch(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'profile.json'
            p.write_text(json.dumps({'engines':{'toolkit':{'executable':sys.executable,'sha256':'0'*64}},'library':d}))
            with self.assertRaisesRegex(ValueError,'hash'):
                load_profile(p)
    def test_cli_deadline_includes_descendant_held_pipes(self):
        started = time.monotonic()
        code = 'import subprocess,sys; subprocess.Popen([sys.executable,"-c","import time;time.sleep(20)"])'
        result = execute([sys.executable, '-c', code], timeout=.1)
        self.assertEqual(result['state'], 'timeout')
        self.assertLess(time.monotonic() - started, 2)

    def test_lsp_write_deadline(self):
        session = lsp_check.Session([sys.executable, '-c', 'import time;time.sleep(20)'], timeout=.1)
        try:
            with self.assertRaises(TimeoutError):
                session.send({'jsonrpc':'2.0','method':'textDocument/didOpen','params':{'text':'x'*100000}})
        finally:
            session.close()

    def test_lsp_stderr_limit_is_explicit(self):
        with tempfile.TemporaryDirectory() as directory:
            result = lsp_check.probe([sys.executable, '-c', 'import sys,time;sys.stderr.write("x"*1000000);sys.stderr.flush();time.sleep(20)'], directory, ['package P {}'], timeout=1)
        self.assertEqual(result['state'], 'output-limit')
        self.assertTrue(result['stderr_truncated'])
        self.assertEqual(len(result['stderr']),262144)

    def test_stale_unversioned_publications_do_not_prove_edits(self):
        with tempfile.TemporaryDirectory() as directory:
            fake = Path(directory)/'language-server'
            fake.write_text('#!/usr/bin/python3\n'+Path('tests/fake_lsp.py').read_text())
            fake.chmod(0o755)
            model = Path(directory)/'model.sysml'
            model.write_text('package P {}')
            profile={'engines':{'opensysml-lsp':{'executable':str(fake)},'toolkit':{'executable':str(fake)}},'library':directory}
            profile_path=Path(directory)/'profile.json'
            profile_path.write_text('{}')
            with patch('lsp_check.load_profile',return_value=profile):
                result=lsp_check.run(profile_path,Path(directory)/'output.json',model)
            self.assertFalse(result['expectations_met'])
            for row in result['results']:
                self.assertEqual([d['has_errors'] for d in row['documents']],[False,True,False])
                self.assertFalse(row['version_correlated'])
                self.assertFalse(row['expectations_met'])

    def test_lsp_framing_and_invalid_length(self):
        message={'jsonrpc':'2.0','id':1,'result':'µ'}
        self.assertEqual(read_message(io.BytesIO(encode_message(message))),message)
        for raw in [b'Content-Length: -1\r\n\r\n',b'Content-Length: 99999999\r\n\r\n',b'Content-Length: 5\r\n\r\nx']:
            with self.assertRaises((ValueError,EOFError)):
                read_message(io.BytesIO(raw))

if __name__=='__main__': unittest.main()
