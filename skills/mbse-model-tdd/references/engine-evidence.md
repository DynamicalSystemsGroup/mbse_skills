# Engine evidence and helper interfaces

| Result | Supported claim |
| --- | --- |
| Valid | The configured validation operation accepted this input under its diagnostics policy. |
| Invalid | The validation operation reported an error/failing diagnostic policy. |
| Holds / violated | An actual constraint check reported true / false for its modeled inputs. |
| Undecided | A completed check could not resolve the condition. |
| Unavailable | The operation, output contract or capture could not establish a result. |

Treat timeout, malformed output, launch failure and truncated output as measurement problems. A zero exit with no actual check, absent diagnostics, or a missing property does not establish a constraint result. Keep every native diagnostic, including warnings. Different engines' “strict” flags are different policies.

The bundled scripts use Python 3.11+ standard library and explicit local paths. They do not install anything. Run from a writable working directory for ignored caches/output:

```bash
python scripts/engine_check.py --profile engines.json --manifest cases.json --output capture.json
python scripts/lsp_check.py --profile engines.json --model valid.sysml --output lsp.json
```

Paths here are relative to the skill directory; resolve the installed skill directory before executing. Use the active project's Python runner (`uv run` in this collection).

Profile JSON:

```json
{
  "engines": {
    "opensysml": {"executable": "/absolute/path/sysml", "sha256": "ACTUAL_SHA256"},
    "toolkit": {"executable": "/absolute/path/sysmlv2", "sha256": "ACTUAL_SHA256"},
    "opensysml-lsp": {"executable": "/absolute/path/sysml-lsp", "sha256": "ACTUAL_SHA256"}
  },
  "library": "/absolute/path/sysml.library",
  "library_sha256": "ACTUAL_INVENTORY_SHA256"
}
```

The library identity hashes sorted relative `.sysml`/`.kerml` paths and their byte hashes, encoded as compact JSON. This external library applies to Toolkit. OpenSysML uses the library bundled into its pinned executable. Record this configuration difference in comparisons.

Case manifest: a `subject` naming the OpenSysML constraint, plus `cases` with `id`, model path relative to the manifest, `expected_validation` (`valid`/`invalid`, or a map by engine name), and for valid cases `expected_verification` (`holds`/`violated`/`undecided`/`unavailable`, or a map by engine name). Toolkit verifies all eligible bodies in the file; isolate the intended condition. The scripts support these specific CLI contracts; inspect the engine help and add calibration cases before adapting them to another release.

CLI captures include input, manifest/profile hashes, versions, commands, streams, exit state and interpreted outcomes. Each stream is capped at 256 KiB; runs have a 30-second deadline and terminate their process group. No shell interpolation is used. Ambient model/library variables and credentials are excluded.

LSP captures retain capabilities and the client/server messages for valid → invalid → restored text. Accept server versions when provided; otherwise keep edit publications as unversioned observations and corroborate each text in a fresh session. Those fresh-session results do not establish server-asserted correlation for the edit session. Fresh sessions corroborate each text independently; they do not establish same-session edit restoration for unversioned servers. The helper is a diagnostic smoke check, not an editor implementation or constraint execution API. It has response deadlines and frame/session bounds. Transcripts include model text: use an appropriate local output destination for confidential models.
