# Contributing

Thanks for considering a contribution. This project ships a deterministic
tool, so the bar for changes that affect output is intentionally high — but
the process is short.

## Development setup

Requirements: Python ≥ 3.11 and [`uv`](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/fabriziosalmi/gitignore
cd gitignore/occam-gitignore
uv sync
uv run pytest -q
uv run ruff check .
uv run mypy .
```

The repo is a uv workspace with 6 packages under `packages/`. See
[occam-gitignore/README.md](occam-gitignore/README.md) for the architecture.

## Workflow

1. Open an issue describing the change, especially for anything that affects
   the deterministic output.
2. Branch from `main`. Keep PRs focused.
3. Make your change with tests. Snapshot/conformance hash drift is **not**
   accidental — if you intentionally change output, regenerate locally and
   commit the new hashes (CI will reject silent drift).
4. Run the full local QA: `pytest`, `ruff`, `mypy`. All must pass.
5. Open a PR. CI must be green before review.

## Adding a new ecosystem (template + fingerprint rule)

1. Add `data/templates/<feature>.gitignore`.
2. Add fingerprint evidence in `occam_gitignore_core/_fingerprint.py`.
3. Regenerate the conformance corpus:
   `uv run python conformance/generate_cases.py`.
4. Add a snapshot case in
   `packages/occam-gitignore-core/tests/test_snapshots.py`.
5. Bump versions if appropriate (see "Versioning" below).

## Versioning

The project uses [SemVer](https://semver.org/). Reminder:

- **Patch** (0.1.x): bug fixes, no output change.
- **Minor** (0.x.0): new features, output changes that strictly add lines.
- **Major** (x.0.0): output changes that remove or reorder lines.

Output hash changes for the same input ⇒ at least a minor bump and a
CHANGELOG entry. The frozen rules table + templates versions ensure such
changes are visible.

## Code style

- Strict typing, `mypy --strict` clean.
- `ruff check .` clean (config in `ruff.toml`).
- Public symbols should have a one-line docstring; internal helpers don't
  need one.
- All Python sources start with `# SPDX-License-Identifier: MIT`.

## License

By contributing, you agree your contributions will be licensed under the
[MIT License](LICENSE).
