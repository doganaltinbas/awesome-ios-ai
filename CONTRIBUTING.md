# Contributing

Scope: resources for iOS/macOS on-device and Apple AI (Foundation Models, Core AI, Core ML, MLX, App Intents for AI).

## Adding an entry

1. Add an object to `data/resources.json` with `name`, `url`, `category`, `why` (one line), `added`, `last_verified`, `status`.
2. The repo must be public and target a current iOS/Xcode version. Note the OS version in `why` if it matters.
3. Run `python3 scripts/update_status.py` to refresh status and regenerate `README.md`.
4. Open a PR using the template.

## Rules

- No promotional or closed-source-only projects.
- Abandoned repos are marked `stale` automatically, then removed after 6 months stale.
- One maintainer review is required before merge.
