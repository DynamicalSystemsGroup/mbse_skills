"""Normalize calibrated CLI captures without discarding native evidence."""
import argparse
import hashlib
import json
from pathlib import Path
import re

from engine_check import classify

HASH = re.compile('[0-9a-f]{64}')
VALIDATE = {'accepted', 'rejected', 'unsupported', 'unavailable', 'not_run'}
VERIFY = {'satisfied', 'violated', 'undecided', 'unsupported', 'unavailable', 'not_run'}
MEASUREMENTS = {'completed', 'timeout', 'output-limit', 'launch-failed', 'not-run'}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def validate_report(report):
    if report.get('schema_version') != 1 or not isinstance(report.get('records'), list) or not report['records']:
        raise ValueError('invalid report schema or empty records')
    source = report.get('source', {})
    if not isinstance(source.get('path'), str) or not source['path'] or Path(source['path']).is_absolute() or '..' in Path(source['path']).parts:
        raise ValueError('source must be project-relative')
    for value in (source.get('sha256'), report.get('adapter_sha256')):
        if not isinstance(value, str) or not HASH.fullmatch(value):
            raise ValueError('invalid source/adapter hash')
    seen = set()
    for row in report['records']:
        for key in ('id', 'engine', 'case', 'reason', 'native_pointer', 'diagnostics_pointer'):
            if not isinstance(row.get(key), str) or not row[key].strip():
                raise ValueError('missing report identity/reason/pointer')
        if row['id'] in seen:
            raise ValueError('duplicate report record')
        seen.add(row['id'])
        operation = row.get('operation')
        allowed = VALIDATE if operation == 'validate' else VERIFY if operation == 'verify' else set()
        outcome, measurement = row.get('outcome'), row.get('measurement')
        if outcome not in allowed or measurement not in MEASUREMENTS:
            raise ValueError('invalid operation/outcome/measurement')
        if outcome == 'not_run' and measurement != 'not-run':
            raise ValueError('not_run outcome requires not-run measurement')
        if measurement == 'not-run' and outcome not in {'not_run', 'unsupported'}:
            raise ValueError('not-run measurement requires a skipped or explicitly unsupported operation')
        if measurement not in {'completed', 'not-run'} and outcome != 'unavailable':
            raise ValueError('incomplete measurement cannot establish a verdict')
        if outcome == 'unsupported':
            capability = row.get('capability_evidence')
            if not isinstance(capability, dict) or not isinstance(capability.get('statement'), str) or not capability['statement'].strip():
                raise ValueError('unsupported requires explicit capability evidence')
        for key in ('engine_sha256', 'model_sha256', 'profile_sha256', 'manifest_sha256', 'library_sha256'):
            value = row.get(key)
            if not isinstance(value, str) or not HASH.fullmatch(value):
                raise ValueError(f'invalid {key}')
        scope = row.get('subject_scope', {})
        if scope.get('kind') not in {'model-validation', 'named-checks', 'file-eligible-checks'}:
            raise ValueError('invalid subject scope')
        if (operation == 'validate') != (scope['kind'] == 'model-validation'):
            raise ValueError('subject scope differs from operation')
        if scope['kind'] == 'named-checks' and (not isinstance(scope.get('subjects'), list) or not scope['subjects'] or any(not isinstance(s, str) or not s for s in scope['subjects'])):
            raise ValueError('named check scope requires native subjects')
    return report


def normalize(capture, source_path, source_sha256):
    rows = []
    engines = capture['engines']
    mapping = {'valid': 'accepted', 'invalid': 'rejected', 'holds': 'satisfied', 'violated': 'violated', 'undecided': 'undecided', 'unavailable': 'unavailable'}
    for index, raw in enumerate(capture['runs']):
        engine = raw['engine']
        if engine not in {'opensysml', 'toolkit'}:
            raise ValueError('uncalibrated engine')
        for operation in ('validate', 'verify'):
            key = 'validation' if operation == 'validate' else 'verification'
            observation = raw.get(key)
            pointer = f'/runs/{index}/{key}'
            scope = {'kind': 'model-validation' if operation == 'validate' else 'file-eligible-checks'}
            if observation is None:
                if operation == 'validate' or raw['validation'].get('outcome') == 'valid':
                    raise ValueError('missing executed operation')
                outcome, measurement = 'not_run', 'not-run'
                reason = 'Verification not executed after validation did not establish acceptance.'
                pointer = f'/runs/{index}/validation'
            else:
                measurement = observation['state']
                if measurement not in MEASUREMENTS - {'not-run'}:
                    raise ValueError('unknown native measurement state')
                interpreted = classify(engine, operation, observation['exit_code'], observation['stdout']) if measurement == 'completed' else 'unavailable'
                if observation.get('outcome') != interpreted:
                    raise ValueError('stored interpretation disagrees with native capture')
                outcome = mapping[interpreted]
                reason = f'Calibrated {engine} {operation} interpretation: {interpreted}; measurement {measurement}.'
                if operation == 'verify' and engine == 'opensysml' and measurement == 'completed':
                    try:
                        subjects = [c['subject'] for c in json.loads(observation['stdout']).get('checks') or []]
                    except (ValueError, KeyError, TypeError):
                        subjects = []
                    if subjects:
                        scope = {'kind': 'named-checks', 'subjects': subjects}
            rows.append({'id': f'{engine}:{raw["case"]}:{operation}', 'engine': engine,
                         'engine_sha256': engines['engines'][engine]['sha256'], 'case': raw['case'],
                         'model_sha256': raw['model_sha256'], 'operation': operation, 'outcome': outcome,
                         'measurement': measurement, 'reason': reason, 'native_pointer': pointer,
                         'diagnostics_pointer': f'/runs/{index}/validation/stdout', 'subject_scope': scope,
                         'profile_sha256': capture['profile_sha256'], 'manifest_sha256': capture['manifest_sha256'],
                         'library_sha256': engines['library_sha256']})
    return validate_report({'schema_version': 1, 'source': {'path': source_path, 'sha256': source_sha256},
                            'adapter_sha256': digest(__file__), 'records': rows,
                            'limits': ['native evidence is authoritative', 'no current engine/model byte check',
                                       'Toolkit scope is all eligible file checks', 'no physical/stakeholder validation']})


def convert(source, output, root):
    root, source, output = Path(root).resolve(), Path(source).resolve(), Path(output).resolve()
    if not source.is_relative_to(root) or not output.is_relative_to(root):
        raise ValueError('source and output must lie inside project root')
    report = normalize(json.loads(source.read_text()), source.relative_to(root).as_posix(), digest(source))
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('x') as stream:
        stream.write(json.dumps(report, indent=2) + '\n')
    return report


def verify_retained(report, root):
    """Verify native identity and replay this adapter's calibrated interpretation."""
    validate_report(report)
    root = Path(root).resolve()
    source = (root / report['source']['path']).resolve()
    if not source.is_relative_to(root) or not source.is_file() or digest(source) != report['source']['sha256']:
        raise ValueError('retained native source identity differs')
    replay = normalize(json.loads(source.read_text()), report['source']['path'], digest(source))
    if replay['records'] != report['records']:
        raise ValueError('report records differ from calibrated native interpretation')
    return {'native_source_verified': True, 'records_replayed': len(replay['records'])}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source')
    parser.add_argument('output')
    parser.add_argument('--root', required=True)
    args = parser.parse_args()
    try:
        result = convert(args.source, args.output, args.root)
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(2, str(error) + '\n')
    print(json.dumps({'records': len(result['records']), 'output': args.output}))
