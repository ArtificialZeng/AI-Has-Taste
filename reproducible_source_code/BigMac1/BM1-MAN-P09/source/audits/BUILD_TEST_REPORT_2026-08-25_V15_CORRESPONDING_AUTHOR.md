# V15 corresponding-author revision audit

Date: 2026-08-25 (Asia/Shanghai)

## Verdict

**PASS.**  V15 changes only the displayed corresponding-author metadata and
release documentation.  The mathematical statements, exact certificates,
references, and supplied affiliations and email addresses are unchanged from
the audited V14 source.

## Requested title-page change

- The author line displays `Yonghua Xiong*`.
- The title-page note displays `* Corresponding Author: Yonghua Xiong.`
- The PDF metadata retains the plain bibliographic author name `Yonghua
  Xiong`, without a decorative star.

## Build and layout gates

- Two clean builds in distinct directories are byte-identical.
- PDF SHA-256:
  `7e67a93526a892dcfa4221b5dc621cbcb61b48bffaa9d40f691bf24df672a417`.
- The PDF has 31 Letter pages and is 541,464 bytes.
- The final LaTeX log has no overfull or underfull boxes, undefined
  citations or references, warnings, or fatal errors.
- All fonts are embedded, subset, and Unicode mapped.
- The title page was rendered at 150 dpi and inspected at original render
  resolution.  Both stars are visible, correctly placed, and unclipped.
- Text extraction independently contains `YONGHUA XIONG*` and
  `Corresponding Author: Yonghua Xiong.`

## Scope

This remains a partial-results preprint about five exact local positivity
families and their certificates.  It does not solve the unrestricted fixed
crossing-lens constant, the full compact-ball quartic, the general complex
common-metric problem, or the arbitrary-node bridge.

Fatal findings: 0.  Major findings: 0.  Minor findings: 0.
