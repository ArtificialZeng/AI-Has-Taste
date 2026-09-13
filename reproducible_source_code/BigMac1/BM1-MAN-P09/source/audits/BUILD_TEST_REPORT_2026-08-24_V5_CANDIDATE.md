# v5 candidate build and test report

Date: 2026-08-24 (Asia/Shanghai).

Status: **independently audited partial-theorem submission candidate**.  The
independent v5 mathematical transcription and release audit has now passed.
Unconditional submission-ready status still requires confirmation of author
metadata and the selected venue's disclosure, acknowledgments, funding, and
style requirements.

## Bounded change set

The frozen v4 source/release layout was copied before editing.  The v5
candidate changes only the two newly certified endpoints:

- the local all-scale chart now has `|t-4|<=5/92`, equivalently
  `363/92<=t<=373/92`, for every legal coupling scale `T`;
- the five-real-parameter moving sheet now has `0<=X<=1/20`, using the two
  closed adjacent cells X21 and X20.

The manuscript continues to state that the unrestricted complex Hermitian
gate, full compact-ball quartic, common-metric theorem, arbitrary-node bridge,
and optimal fixed crossing-lens constant remain open.  The scale result is
only a local seven-real-parameter chart (six bounded shape coordinates plus
the legal scale), and the moving-sheet result remains five-real-parameter
with normalized scale near one.  No Lean or other proof assistant covers
either complex theorem.

No new mathematical search was performed.  The protected project ledgers and
dispatch/portfolio files were not edited.

## Exact endpoint replay

The following six commands passed first in the project workspace and then
again from `certificate_workspace/` in this candidate:

```sh
python tmp/research/verify_common_metric_tilted_rankone_complex_scale_t5over92_enlargement.py
python audit/verify_common_metric_tilted_rankone_complex_scale_t5over92_referee.py
python tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x21_extension.py
python tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x21_extension_independent_referee.py
python tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x20_extension.py
python tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x20_extension_independent_referee.py
```

All six exited zero.  The decisive reported source/referee verifier hashes
were:

```text
t5/92 source:   d357bbfaac1fd054c4bab671e488243f75bfc709acff2dde29e42c7e827043a7
t5/92 referee:  0df222da6d9b4a1f4bb58f2a7d1e842219ee3952dce022ce984cded57f9b3f7d
X21 source:     4bb3fa86601d845c682884dc1fe934e493f2588143897497ac37f1e5d7dfbe6e
X21 referee:    415d90562062eab38f7f3041576aafba8ded8456a716fc9dc6e7310cd11424e4
X20 source:     c914974b1f43c86a3bcc67851a64cc7fed0b83dd8fcade023af4ccb15ecd7386
X20 referee:    b61bd069a9bcc2da63d7ca3d6e103f2b07b723b0a722660b04ce952c6f82cba8
```

The five new endpoint manifest checks passed from
`certificate_workspace/`.  The regenerated grouped manifests also passed:
53 bound files in `certificates/scale_cubic/ORIGINAL_MANIFEST.sha256` and 56
bound files in `certificates/moving_sheet/ORIGINAL_MANIFEST.sha256`.  The
frozen v4 `RELEASE_MANIFEST.sha256` was independently checked before copying
and exited zero.

## Build, bibliography, and PDF QA

Environment used:

```text
Python 3.11.15
SymPy 1.14.0
latexmk 4.88
Poppler pdftoppm 26.04.0
```

A clean build passed with:

```sh
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The workflow-provided `audit_latex.py` was run against `main.tex`,
`references.bib`, and `main.log`.  Its result was
`cited=5 bib=5 missing=0 unused=0`.  The final log scan found
no undefined references or citations, multiply defined labels, LaTeX/package
warnings, overfull boxes, underfull boxes, fatal errors, or emergency stops.

The final PDF has 16 letter-size pages.  All 16 pages were rendered with
Poppler and inspected: no clipping, overlap, missing glyph, black box, broken
table/equation, or malformed reference was found.  Page numbering, running
heads, title/author metadata, section transitions, and final-page references
were checked.  The large final-page whitespace is the natural end of the
bibliography and author address, not a rendering defect.

Frozen manuscript artifacts before release-manifest generation:

```text
635bb73504e22eae67321ecac54f1e8294c903f8823aa5ff16998da1b463d297  main.tex
a5001f7fcd7d14e59d1d48923a8eae757a776836f9e5ea1ff0d5a7d8b86d58bb  main.pdf
3d8e3ac2c999b50e84b126e5f04e108d3e74f0e971aa2ca9f91eaa4742d04f1b  main.bbl
989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600  references.bib
```

## Warnings and remaining gate

- The historical workspace-wide `CHECKPOINT_MANIFEST.sha256` check reports
  four pre-existing mismatches in `APPROACH_REGISTRY.md`, `CLAIM_LEDGER.md`,
  `COUNTEREXAMPLE_DB.md`, and `research_state.json`; the checkpoint's own
  executable verification ended `verify_checkpoint.sh: OK`.  None of the four
  mismatched files was edited in this bounded task.
- The historical v4 mathematical/bibliographic audits are retained as
  baseline evidence only.  They do not audit the two new v5 endpoints.
- Root and an independent manuscript referee subsequently rechecked the v5
  transcription, all six new verifiers, all relevant manifests, a fresh ZIP
  extraction and clean build, five citations, final logs, hashes, and all 16
  rendered pages.  No mathematical, certificate, build, or archive blocker
  was found; see `V5_INDEPENDENT_FINAL_AUDIT.md`.
