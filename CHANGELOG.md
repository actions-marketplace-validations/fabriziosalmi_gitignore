# Changelog

All notable changes to `occam-gitignore` are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/) and the project adheres to
[Semantic Versioning](https://semver.org/).

## [0.1.3] — 2026-04-27

### Fixed
- `occam-gitignore serve api` and `occam-gitignore serve mcp` now auto-resolve
  the bundled data directory and pass it through to the adapter, so a fresh
  `pip install occam-gitignore` works out-of-the-box for both servers (no more
  manual `OCCAM_GITIGNORE_DATA_DIR=...`).

### Changed
- All Python sources now carry an `SPDX-License-Identifier: MIT` header.

## [0.1.2] — 2026-04-27

### Fixed
- Published CLI wheel now bundles `data/templates/` and `data/rules_table.json`
  (previous wheels were broken: `occam-gitignore generate .` raised
  `FileNotFoundError`). A hatch build hook copies the data into the package
  source tree at build time; runtime resolution falls back to the bundled
  `_data/` directory before walking the monorepo layout.

## [0.1.0] — 2026-04-27

### Added
- Initial public release.
- `occam-gitignore-core`: deterministic generator (frozen merkle of
  rules table + templates + core version).
- `occam-gitignore` CLI (`generate`, `fingerprint`, `diff`, `version`,
  `serve api|mcp`).
- `occam-gitignore-api`: FastAPI HTTP adapter, hash-in-header.
- `occam-gitignore-mcp`: Model Context Protocol server (FastMCP).
- `occam-gitignore-bench`: corpus benchmark with quality + latency gates.
- `occam-gitignore-training`: offline pipeline to mine rules from JSONL.
- 32-case conformance suite with locked output hashes.
- 5 snapshot tests + property-based tests (Hypothesis).
- PyPI publishing via OIDC trusted publisher.
- SBOM (SPDX) + SLSA build provenance attestations on every release.
- Composite GitHub Action (`uses: fabriziosalmi/gitignore@v0.1.x`) for
  drift check / auto-fix in CI.

[0.1.3]: https://github.com/fabriziosalmi/gitignore/releases/tag/v0.1.3
[0.1.2]: https://github.com/fabriziosalmi/gitignore/releases/tag/v0.1.2
[0.1.0]: https://github.com/fabriziosalmi/gitignore/releases/tag/v0.1.0
