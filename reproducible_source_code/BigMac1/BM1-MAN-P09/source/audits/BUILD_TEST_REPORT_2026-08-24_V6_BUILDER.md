# v6 builder report: exact endpoint integration, build, and archive gate

Date: 2026-08-24 (Asia/Shanghai).

Status: **builder-complete local partial-theorem candidate; subsequent
independent final technical audit passed**.  The two new endpoint certificates
have independent exact referee programs, and the v6 manuscript and archive
subsequently passed the separate root-task referee recorded in
`V6_INDEPENDENT_FINAL_AUDIT.md`.  The unrestricted complex Hermitian gate, the full
compact-ball quartic, the common-metric theorem, the arbitrary-node bridge,
and the optimal fixed crossing-lens constant remain open.  Unconditional
submission-ready status also requires confirmation of author metadata and the
target venue's AI disclosure, acknowledgments, funding, bibliography, and
style requirements.

## Frozen baseline and exact v5-to-v6 delta

The source was copied from the frozen, independently audited
`common_metric_two_positivity_islands_submission_2026-08-24-v5` release, not
from a moving development manuscript.  Only the following mathematical
endpoints and their direct reproducibility materials were added:

1. The complete legal-scale island changes from `|t-4|<=5/92` to
   `|t-4|<=13/239`, equivalently `943/239<=t<=969/239`.  All seven derivative
   majorants were recomputed on the new interval; all fourteen cell/sign
   reserves are strictly positive.  The fresh finite ratio bottleneck is

   ```text
   27162772450885609710321172264010161955258866496 /
   499232790087220155922502903379517386791638099025 > 13/239.
   ```

   The independent 96-corner diagnostic has minimum direct `T=1` gate
   `3791537219332938219668993327/1612003174500796900000000>0`.  The theorem
   still quantifies over the entire legal `T` half-line and remains only a
   seven-real-parameter local island.

2. The five-real-parameter moving sheet changes from `0<=X<=1/20` to
   `0<=X<=1/19` by adding the closed cell `1/20<=X<=1/19`.  The exact
   projective order is `S=X sigma`, `sigma<=1/500`; legality includes
   `59/400<Z<1/6`, strict danger, rank two, both signs of `z`, the exact seam,
   and the right endpoint.  The continuum reserve is

   ```text
   26756976522448207008651434175031131058236664369690137089162898293759 /
   13308465593548800000000000000000000000000000000000000000 > 0.
   ```

   The 72-node grid is falsification only.  No maximal endpoint, full
   positive-`Z` collar, arbitrary normalized scale, or full-ball result is
   claimed.

No global claim ledger, counterexample database, portfolio, or dispatch file
was edited by this bounded builder task.  No new mathematical search was
performed, and no Lean or other proof assistant covers either complex theorem.

## Exact certificate replay and fail-closed tests

All commands below were run from the packaged `certificate_workspace/`.
Normal execution produced exit code 0 for each command:

```sh
python -B tmp/research/verify_common_metric_tilted_rankone_complex_scale_t13over239_enlargement.py
python -B audit/verify_common_metric_tilted_rankone_complex_scale_t13over239_referee.py
python -B tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x19_extension.py
python -B tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x19_extension_independent_referee.py
```

The corresponding optimized-Python commands, with `python -O -B`, each
produced the intended nonzero exit code 1 and the message that optimized
Python disables verification.  Thus all four programs fail closed when
assertion checks would be removed.

The four direct dependency manifests all exited 0 under
`shasum -a 256 -c`:

```text
tmp/research/common_metric_tilted_rankone_complex_scale_t13over239_enlargement_manifest.sha256
audit/common_metric_tilted_rankone_complex_scale_t13over239_referee_manifest.sha256
tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x19_extension_manifest.sha256
tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x19_extension_independent_referee_manifest.sha256
```

The grouped scale-cubic manifest binds 60 files and the grouped moving-sheet
manifest binds 63 files; both passed from `certificate_workspace/`.  The
final release manifest binds 273 distributed files other than itself and is
verified after generation.

The decisive new verifier hashes are:

```text
scale source:   3e2cb11a74a7e77993f3464ccdd888f2dd5d495903b137444adf05344e68bf09
scale referee:  c29f5c864a66c369c439976fb9873d8a22a4a935c3286e7656e16638371c71a8
X19 source:     1287290731cb2b5dd24789116f4f1dadc23dd213d45c90ae302f65101326fc34
X19 referee:    35e9d90c6ac1fcb8ba2d304e60ddd98d5a56f2e8347a174cfed9af009ba2a01c
```

## Clean build, bibliography, log, and PDF QA

Environment used for the packaged replay and build:

```text
Python 3.13.5
SymPy 1.13.3
latexmk 4.88
Poppler pdftoppm 26.04.0
```

The final source was built from a clean LaTeX state:

```sh
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Both exited 0.  The mathematics-workflow LaTeX auditor reported
`cited=5 bib=5 missing=0 unused=0`.  The bibliography skill checker likewise
reported five cited keys, five BibTeX keys, no missing bibliography, no
missing or unused entry, and exact agreement with `main.aux`.  Because v6
changes no citation command, citation context, or BibTeX entry, the frozen
primary-source audit remains applicable; the v5 and v6 `references.bib`
files are byte-identical with SHA-256
`989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600`.

The converged `main.log` and `main.blg` contain no undefined citation or
reference, missing database entry, repeated entry, LaTeX/package warning,
fatal error, undefined control sequence, runaway argument, overfull box, or
underfull box.

The final PDF is letter size, 17 pages, and 482,426 bytes.  Its metadata title
and author are the manuscript title and Zijian Zeng.  All 17 pages were
rendered at 150 dpi with Poppler and inspected: there is no clipping, overlap,
missing glyph, black box, broken table/equation, or malformed reference.
Headers, footers, page numbers, links, section transitions, the exact-data
appendix, bibliography, and final-page whitespace were checked.  A final
clean rebuild changed only PDF metadata bytes: the complete final render set
was pixel-identical to the inspected 17-page set.

Frozen manuscript hashes before release-manifest generation:

```text
019bf0ce092ac17eaa3b171cc2fea9fb4e74a34abaf800581e5465f890d8badb  main.tex
108df96cbe20e438db0e7dbcb6534a2d65339431f210627a2caf691a865558d2  main.pdf
3d8e3ac2c999b50e84b126e5f04e108d3e74f0e971aa2ca9f91eaa4742d04f1b  main.bbl
989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600  references.bib
```

## Archive hash and remaining release gate

The authoritative final ZIP SHA-256 is written beside the archive in
`common_metric_two_positivity_islands_submission_2026-08-24-v6.zip.sha256`
after archive closure.  It cannot be embedded as a literal value inside the
same ZIP without changing the ZIP and invalidating that value; the external
sidecar and the root-task handoff therefore carry the final archive hash.
The ZIP is freshly extracted and its release manifest, clean build, and PDF
byte identity are rechecked before handoff.

The historical workspace-wide `CHECKPOINT_MANIFEST.sha256` reports four
expected live-checkpoint mismatches in `APPROACH_REGISTRY.md`,
`CLAIM_LEDGER.md`, `COUNTEREXAMPLE_DB.md`, and `research_state.json`; this
bounded task does not modify those files.  The v6 release manifest is the
authoritative integrity record for this candidate.

The separate independent v6 manuscript/archive referee subsequently passed;
its report is `V6_INDEPENDENT_FINAL_AUDIT.md`.  The remaining nontechnical
submission gate is confirmation of author metadata and the selected venue's
AI disclosure, acknowledgments, funding, bibliography, and style requirements.
