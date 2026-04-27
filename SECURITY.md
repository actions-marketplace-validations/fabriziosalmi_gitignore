# Security policy

## Supported versions

Only the latest minor of `occam-gitignore` on PyPI is supported. Older
versions receive no security backports.

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |
| < 0.1   | :x:                |

## Reporting a vulnerability

**Do not** open a public GitHub issue.

Please use **GitHub Security Advisories** for this repository:
<https://github.com/fabriziosalmi/gitignore/security/advisories/new>

Or email the maintainer (preferred contact in repo profile).

We aim to acknowledge reports within **72 hours** and to publish a fix or a
mitigation within **14 days** for high-severity issues.

## Threat model

`occam-gitignore` is a local-first deterministic generator. Concretely:

- The CLI does **not** read network resources at runtime.
- The HTTP API is something operators run themselves; it has no
  authentication and is intended for trusted networks. If you expose it,
  put it behind an authenticated proxy.
- The MCP server runs as a child process of an MCP host (Claude Desktop,
  Cursor, etc.); it has no privileges beyond reading the bundled data
  directory and accepting structured input on stdio/HTTP.

In-scope issues:

- Path traversal or arbitrary read in the CLI / API / MCP server.
- Crashes or DoS on malformed input.
- Determinism breakage (output depends on environment in a way not
  documented by the determinism contract).
- Supply-chain integrity (compromised wheels, mismatched SBOM/SLSA).

Out of scope:

- DoS via expensive but documented input sizes.
- Issues in third-party MCP hosts or HTTP clients.
- Vulnerabilities in node_modules / VitePress used to build documentation.
