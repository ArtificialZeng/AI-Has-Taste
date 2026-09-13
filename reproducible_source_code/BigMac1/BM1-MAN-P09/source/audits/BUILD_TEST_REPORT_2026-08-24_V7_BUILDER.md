# v7 builder report: conservative endpoint integration and archive gate

Date: 2026-08-24 (Asia/Shanghai).

Status: **builder-complete local partial-theorem candidate awaiting a separate
independent v7 final manuscript/archive referee**.  This report records
transcription, exact-certificate replay, build, bibliography, and visual gates;
it is not that independent final referee report.  The general complex Hermitian
gate, the full compact-ball quartic, a common metric for arbitrary separators,
the arbitrary-node bridge, and the optimal constant of a fixed crossing lens
remain open.  Unconditional submission-ready status also requires confirmation
of author metadata and the selected venue's AI-disclosure, acknowledgment,
funding, bibliography, and style requirements.

## Frozen baseline and exact v6-to-v7 delta

The source was copied from the frozen, independently audited v6 release.  No
global claim ledger, counterexample database, portfolio, or dispatch file was
edited, and no new mathematical search was performed.  Only the following two
already frozen endpoint advances and their reproducibility materials were
integrated.

1. The scale island changes from `|t-4|<=13/239` to
   `|t-4|<=50/919`, equivalently `3626/919<=t<=3726/919`.  All seven
   derivative majorants were recomputed on the wider interval, and all
   fourteen cell/sign reserves are strictly positive.  The exact finite-ratio
   witness is

   ```text
   22832956414652720419288572875925058067205119308096 /
   419658897924777012091564281675537127592865447699025 > 50/919,
   ```

   with positive cross product
   `542048826999460747984389198271984118232259188974`.
   The independent 96-corner falsification diagnostic has minimum direct
   `T=1` gate

   ```text
   40614857500397194448289907112063 /
   17267773417544622036100000000 > 0.
   ```

   The theorem still quantifies over the complete legal positive scale
   half-line but only on the displayed local shape chart; no larger half-width
   is claimed.

2. The moving sheet changes from `0<=X<=1/19` to `0<=X<=1/17` by
   adjoining the exact cells `1/19<=X<=1/18` and
   `1/18<=X<=1/17`.  The last cell has continuum reserve

   ```text
   56825922845924911137909427477635861991459577165298164167361883470142517 /
   28264468561920000000000000000000000000000000000000000000000 > 0.
   ```

   The source legality reconstruction gives
   `Z<=50071149309/289289000000<1` and danger reserve
   `4220971659943/9444435000000`; the independent referee gives
   `Z<=50070128289/289289000000` and danger reserve
   `4221004993243/9444435000000`.  The last cell crosses the historical
   locator `Z=1/6` by the exact excess `11/1734` at its right-end base.
   This is legal because the lossless reduction uses only
   `0<S<=1`, `lambda>0`, `Z>0`, and `x^2+y^2+Z<1`; no proof identity
   requires `Z<1/6`.  The 72-node grid and displayed endpoint values are
   falsification checks only.  No full positive-`Z` collar or full-ball result
   is claimed.

No Lean or other proof assistant formalizes either new endpoint.  Existing Lean
files elsewhere in the project concern narrower real algebraic cores and are
not cited as support for either complex theorem.

## Exact certificate replay and fail-closed tests

The distributed `certificate_workspace/` contains the complete
repository-relative dependencies used by the verifiers.  The four new normal
replays, run from that directory, all exited 0:

```sh
python -B tmp/research/verify_common_metric_tilted_rankone_complex_scale_t50over919_enlargement.py
python -B audit/verify_common_metric_tilted_rankone_complex_scale_t50over919_referee.py
python -B tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x17_extension.py
python -B tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x17_extension_independent_referee.py
```

The same four commands under `python -O -B` each failed closed with the
intended nonzero exit code.  Eight independent mutation attacks (changed exact
constants and dropped sign/term checks across source and referee paths) also
failed as intended.  All four verifier files passed Python byte-code
compilation; compiled caches were removed before archive closure.

The new direct manifests passed `shasum -a 256 -c`.  Their entry counts and
manifest-file SHA-256 values are:

```text
11  aefe32dc96a5b3d903ad487a441ee557a87c53de159887e1f56464485337037c
 9  08a36c384431d8d8f69930c069db3125d52ca8d87df6697c339521fbc6f7e507
 4  322d75bee07e6844b0fb4780aea6cafef69a273d472cbd199a7c861e5cb78c2b
14  33641e40d8cb421fa027ef94bcf6b5abfa86a20a7926c769a1d5d085abc6cb76
```

The four decisive verifier hashes are:

```text
scale source:   6e9be003ceb0e89e50e9156ede7d54d6a79888bb7768ac854dd4318792d9e415
scale referee:  a8cb4c4a99f644fbdd97191bf53504bf90a28f85227d3c1c8dfc907febdcf350
X17 source:     9273ffe9cc6fee174d151f1581d3cf971f8c16d782bdcf076c219bb89d23ccf3
X17 referee:    7213b61c7f8e10a25954db1c17bc5f583e1aa506143214e0e3620af9c5024b30
```

The frozen independent X17 audit has SHA-256
`928899fbe1e794734367172e7ad4af71c99e53a2c273f7b9f6334577c62c6dca`.
The immediate predecessor `50/919`-dependency (`21/386`) and X18 source and
referee programs and all four of their direct manifests were replayed again
from the distributed workspace and passed.  Earlier exact certificate lineage
is retained from the frozen independently audited v6 package.

## Clean build, bibliography, log, and PDF QA

Environment used for replay and build:

```text
Python 3.13.5
SymPy 1.13.3
latexmk 4.88
Poppler pdftoppm 26.04.0
```

The source was built from a clean LaTeX state:

```sh
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Both exited 0.  The mathematics-workflow auditor reported
`cited=5 bib=5 missing=0 unused=0`; the bibliography checker independently
reported the same five cited and five database keys, no missing or unused
entry, and exact agreement with `main.aux`.  Citation commands, citation
contexts, and BibTeX entries are unchanged from the frozen primary-source
audit; `references.bib` retains SHA-256
`989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600`.

The converged log contains no undefined citation/reference, missing database
entry, repeated entry, LaTeX/package warning, fatal error, undefined control
sequence, runaway argument, overfull box, or underfull box.  The PDF is US
letter size and 18 pages.  All 18 pages were rendered at 150 dpi with Poppler
and inspected: there is no clipping, overlap, missing glyph, black box, broken
equation, or malformed reference.  Headers, footers, links, section
transitions, both exact-data appendices, the bibliography, and final-page
whitespace were checked.

Frozen manuscript hashes before release-manifest generation:

```text
84e9487e7765e73a0356b6368d99ac820529e259a3eebe40eb7a35ce110c4913  main.tex
eccc150b8486fd18e3aa37bdbc6a1b61282d2df7ad10583445521bec10716a27  main.pdf
3d8e3ac2c999b50e84b126e5f04e108d3e74f0e971aa2ca9f91eaa4742d04f1b  main.bbl
989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600  references.bib
```

## Archive closure and remaining gate

`RELEASE_MANIFEST.sha256` is generated only after the release tree is frozen
and binds every distributed file other than itself.  The archive is then
freshly extracted; its manifest, clean build, citation/log checks, packaged
PDF byte identity, and rendered-page identity are rechecked before handoff.
The authoritative ZIP hash is written in the external `.zip.sha256` sidecar;
it cannot be embedded inside the same ZIP without changing the archive.

The historical workspace checkpoint manifest reports the four expected live
checkpoint mismatches in `APPROACH_REGISTRY.md`, `CLAIM_LEDGER.md`,
`COUNTEREXAMPLE_DB.md`, and `research_state.json`; this bounded builder did not
modify them.  The v7 release manifest is the authoritative integrity record
for this candidate.

The remaining technical release gate is an independent v7 final
manuscript/archive referee.  The remaining nontechnical gate is confirmation
of author metadata and the selected venue's AI-disclosure, acknowledgment,
funding, bibliography, and style requirements.

## Post-builder independent result

After this builder report was frozen, the separate referee recorded a PASS
with zero fatal, major, or minor technical defects in
`audits/V7_INDEPENDENT_FINAL_AUDIT.md`.  Root release finalization adds that
report to a regenerated manifest and archive without changing `main.tex`,
`references.bib`, any certificate, or the delivered PDF.  The nontechnical
author and venue checks above remain outstanding.
