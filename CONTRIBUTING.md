# Contributing

Scope: resources for iOS and macOS on-device and Apple AI (Foundation Models, Core AI, Core ML, MLX, speech, runtimes).

## Adding an entry

Add an object to `data/resources.json`, then run `python3 scripts/update_status.py`. It validates the schema, fetches GitHub metadata, and regenerates `README.md`.

## Schema

| Field | Type | Meaning |
|---|---|---|
| `name` | string | `owner/repo` |
| `url` | string | GitHub URL |
| `section` | one of: Core AI, Foundation Models, Core ML, MLX, Runtimes, Speech, Evals and benchmarks, Curated lists | Table the entry appears in |
| `what` | string | One line: what it does and who should use it |
| `min_ios` | number or null | Minimum iOS version the project targets |
| `build` | object | `result`: `passed`, `failed`, `not_tested`, or `n/a` (curated lists). `xcode` and `date` are required for `passed` or `failed`. `note` is optional. |
| `added` | date | When the entry was added |
| `last_checked` | date | Set by the script |
| `status`, `license`, `stars` | | Set by the script |

## Build results

Builds use Xcode 27.1 for iOS (generic device or iOS Simulator, as noted). Record `passed` or `failed` with the Xcode version and date. Use `not_tested` when no build was run. Projects that need Apple Intelligence hardware or external services are recorded as `not_tested`, with a `note` on the requirement.

## Standards

- Public repository, open license.
- Active within the last 180 days, or clearly marked as a reference.
- `what` describes the project; it doesn't rank it.
- One maintainer review before merge.
