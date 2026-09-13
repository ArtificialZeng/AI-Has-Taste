# Primary-source integrity audit

Audit date: 2026-08-29 (Asia/Shanghai)

Outcome: **PASS.** The source bytes used for theorem and operation-order audit
match the hashes frozen at the first novelty lock.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `sources/2510.01696.pdf` | 717412 | `711c793c7b3ad604e8fb15ba845710b61feb2568142596a51a16c915c7f1723c` |
| `sources/2510.01696.tar` | 200444 | `0bf7fa5c4badfdace95e61d18df57e288f510f9b372d0fe177e6de19de04ae37` |
| `literature/arxiv_api_2510.01696.xml` | recorded in release manifest | `ae35b4296357ef1e03017b63ac8fa2faa2c2ad87412be59dd78f7db776867f7e` |
| `literature/datacite_2510.01696.json` | recorded in release manifest | `fbc07ffefe7d68dd5da0bb4e46a7411fa94b9fd3c8ce129162712a09a1eb6a6d` |

The arXiv source archive was extracted to `sources/2510.01696_src/`; the
independent referee cited `manuscript.tex` lines from this extraction. The
release manifest separately binds every extracted file, the original archive,
the PDF, and the machine-readable metadata.
