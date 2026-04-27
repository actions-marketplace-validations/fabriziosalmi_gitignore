# SPDX-License-Identifier: MIT
"""Snapshot tests: lock canonical generator output.

If a snapshot fails, inspect the diff. To intentionally update, regenerate via:
    python -m occam_gitignore_core._snapshot_helper  (dev-only)
or manually replace the file contents and the matching hash.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from occam_gitignore_core import (
    DefaultFingerprinter,
    FileSystemTemplateRepository,
    GenerateOptions,
    JsonRulesTable,
    generate,
)

_DATA = Path(__file__).resolve().parents[3] / "data"
_SNAP = Path(__file__).resolve().parent / "snapshots"

_CASES = (
    (
        "python",
        ("pyproject.toml",),
        "sha256:d3934387f931f965ab2a14bfde2afa8eed08bc045c0f095bb6be47c5cb9c6666",
    ),
    (
        "node-ts",
        ("package.json", "tsconfig.json"),
        "sha256:196b986b4d693e71502ea7b59eb3d486ac33313c7dcf1628f534fb7b6126c210",
    ),
    (
        "python-docker",
        ("pyproject.toml", "Dockerfile", "docker-compose.yml"),
        "sha256:b50097ea7d57f800a92e35a2539fdd97280abd604db41cf661788e0dc9d5e350",
    ),
    (
        "java",
        ("pom.xml", "src/main/java/A.java"),
        "sha256:c8497eda93d560d5825e220ec8b7b25227b40f34eaae60240d704ff7bcc00fad",
    ),
    (
        "rust",
        ("Cargo.toml", "src/main.rs"),
        "sha256:741f37a8a7a0df298a27ba23fb5675724ec81400f84787adf6bff6b1fbbda5f3",
    ),
)


@pytest.fixture(scope="module")
def deps() -> tuple[FileSystemTemplateRepository, JsonRulesTable]:
    return (
        FileSystemTemplateRepository(_DATA / "templates"),
        JsonRulesTable.from_file(_DATA / "rules_table.json"),
    )


@pytest.mark.parametrize(("label", "tree", "expected_hash"), _CASES)
def test_snapshot_matches(
    deps: tuple[FileSystemTemplateRepository, JsonRulesTable],
    label: str,
    tree: tuple[str, ...],
    expected_hash: str,
) -> None:
    templates, rules = deps
    fp = DefaultFingerprinter().fingerprint(tree)
    out = generate(
        fp,
        GenerateOptions(include_comments=True),
        templates=templates,
        rules_table=rules,
    )
    snapshot_file = _SNAP / f"{label}.gitignore"
    assert snapshot_file.exists(), f"missing snapshot {snapshot_file}"
    assert out.content == snapshot_file.read_text("utf-8"), (
        f"snapshot drift for {label}: regenerate intentionally"
    )
    digest = "sha256:" + hashlib.sha256(out.content.encode("utf-8")).hexdigest()
    assert digest == expected_hash
    assert out.output_hash == expected_hash
