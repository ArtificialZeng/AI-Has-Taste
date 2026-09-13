# v7 independent final manuscript and archive audit

Date: 2026-08-24 (Asia/Shanghai).

Verdict: **PASS at the independent technical release gate, with scientific
status restricted to two exact computer-assisted partial theorems.**  The
audit found 0 fatal, 0 major, and 0 minor technical defects.  The unrestricted
complex Hermitian gate, the full compact-ball quartic, a common metric for
arbitrary separators, the arbitrary-node bridge, and the optimal constant of
a fixed crossing lens all remain open.  No journal peer review is implied.

This is not an unconditional authorization to submit.  The author must still
confirm the displayed name, affiliation, and email, choose a venue, and check
that venue's AI-disclosure, acknowledgment, funding, bibliography-style, and
source-format rules.  Those are nontechnical submission gates, not defects in
the audited mathematical package.

## 1. Independent scope and transcription audit

The complete 1,080-line `main.tex` was read against the frozen theorem notes,
the source verifiers, and the genuinely separate referee verifiers.  The
abstract, introduction, theorem statements, appendices, scope section, and
disclosure agree on the following restricted claims.

### Complex-scale island

The scale result fixes the displayed local shape chart and proves positivity
on the complete legal positive scale half-line only for

```text
3626/919 <= t <= 3726/919,
equivalently |t-4| <= 50/919.
```

The independently replayed finite-ratio ceiling is

```text
22832956414652720419288572875925058067205119308096 /
419658897924777012091564281675537127592865447699025 > 50/919,
```

with positive cross product
`542048826999460747984389198271984118232259188974`.  All fourteen
cell/sign reserves are strictly positive.  The separate 96-corner diagnostic
contains 48 `g>0` and 48 `g<=0` cases and has minimum direct `T=1` gate

```text
40614857500397194448289907112063 /
17267773417544622036100000000 > 0.
```

The corner grid is correctly labeled a falsification diagnostic; it is not
substituted for the exact continuum certificate.  No larger half-width or
general complex Hermitian theorem is claimed.

### Compact moving-sheet island

The moving-sheet theorem is stated only for

```text
0 <= X <= 1/17,
```

with the genuinely new terminal cell

```text
1/18 <= X <= 1/17,   S=X*sigma,   0<sigma<=9/5000.
```

The independently reconstructed terminal-cell reserve is exactly

```text
56825922845924911137909427477635861991459577165298164167361883470142517 /
28264468561920000000000000000000000000000000000000000000000 > 0.
```

The source legality envelope gives
`Z<=50071149309/289289000000` and danger reserve
`4220971659943/9444435000000`; the independent referee uses the deliberately
different envelope `Z<=50070128289/289289000000` and danger reserve
`4221004993243/9444435000000`.  Both are legal and both give the same strict
gate conclusion.

At the terminal right-end base, `Z` crosses the historical locator `Z=1/6` by
the exact excess `11/1734`.  The manuscript correctly explains that this is
not a proof dependency: the lossless reduction requires only
`0<S<=1`, `lambda>0`, `Z>0`, and `x^2+y^2+Z<1`.  It does not require
`Z<1/6`.  The 72 exact nodes and printed endpoint values are correctly
described as falsification checks, not as the continuum proof.  No full
positive-`Z` collar or full compact-ball result is claimed.

### Excluded overclaims and rejected routes

The manuscript does **not** claim the full compact ball, the general complex
Hermitian gate, a global common metric, a fixed-lens solution, or an all-node
theorem.  It does not present any new endpoint as Lean-checked.  The disclosure
accurately says that no proof assistant formalizes either complex endpoint.

CE-046, CE-048, CE-059, and CE-060 were searched in the manuscript,
certificate notes, and audit notes.  None is reused as a valid route.  In
particular the scale proof does not invoke real-part monotonicity, automatic
absorption, or a fixed allocation, and the moving-sheet proof does not revive
a locator-only argument.

## 2. Exact replay, fail-closed behavior, and attacks

All decisive commands were run independently from the packaged
`certificate_workspace/` with caches disabled.  These four normal executions
returned exit code 0:

```sh
python -B tmp/research/verify_common_metric_tilted_rankone_complex_scale_t50over919_enlargement.py
python -B audit/verify_common_metric_tilted_rankone_complex_scale_t50over919_referee.py
python -B tmp/research/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x17_extension.py
python -B tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x17_extension_independent_referee.py
```

The scale source and referee each reconstructed 40,595 exact controls per
cell, fourteen strict reserves, and the 96-corner split above.  The X17 source
and referee independently reconstructed 20 quotient terms, 16 higher terms,
947 centered monomials, the exact terminal reserve, and 72 legal nodes.

The same four programs under `python -O -B` each returned nonzero at their
explicit fail-closed guard.  Optimization therefore cannot silently turn a
certificate failure into success.

Eight mutation attacks were run independently and all returned nonzero at the
intended gate:

```text
T50OVER919_TEST_BAD_DEPENDENCY=1
T50OVER919_TEST_DROP_SIGN=1
T50OVER919_REFEREE_TEST_BAD_DEPENDENCY=1
T50OVER919_REFEREE_TEST_DROP_SIGN=1
X17_TEST_BAD_DEPENDENCY=1
X17_TEST_DROP_TERM=1
X17_REFEREE_BAD_DEPENDENCY=1
X17_REFEREE_DROP_TERM=1
```

All four verifier files also passed `py_compile` with
`PYTHONPYCACHEPREFIX` directed outside the candidate tree.  No byte-code cache
was written into the release.

The four direct dependency manifests passed `shasum -a 256 -c`.  Their entry
counts and manifest-file SHA-256 values are:

```text
11  aefe32dc96a5b3d903ad487a441ee557a87c53de159887e1f56464485337037c
 9  08a36c384431d8d8f69930c069db3125d52ca8d87df6697c339521fbc6f7e507
 4  322d75bee07e6844b0fb4780aea6cafef69a273d472cbd199a7c861e5cb78c2b
14  33641e40d8cb421fa027ef94bcf6b5abfa86a20a7926c769a1d5d085abc6cb76
```

The decisive verifier hashes are:

```text
6e9be003ceb0e89e50e9156ede7d54d6a79888bb7768ac854dd4318792d9e415  scale source
a8cb4c4a99f644fbdd97191bf53504bf90a28f85227d3c1c8dfc907febdcf350  scale referee
9273ffe9cc6fee174d151f1581d3cf971f8c16d782bdcf076c219bb89d23ccf3  X17 source
7213b61c7f8e10a25954db1c17bc5f583e1aa506143214e0e3620af9c5024b30  X17 referee
```

The frozen independent X17 audit has SHA-256
`928899fbe1e794734367172e7ad4af71c99e53a2c273f7b9f6334577c62c6dca`.

## 3. Bibliography authenticity and claim support

The paper cites exactly five keys, and `references.bib` contains exactly those
five entries.  Each was checked against a publisher DOI page and, when useful,
an author-hosted official manuscript.  No title, author, venue, year, volume,
page, or DOI repair was required.

| key | authoritative record checked | result and support for the manuscript |
|---|---|---|
| `MR2223270` | Springer DOI `10.1007/s00013-005-1533-5`; Beckermann's University of Lille manuscript | Beckermann--Crouzeix, *A lenticular version of a von Neumann inequality*, Arch. Math. 86 (2006), 352--355; directly treats convex lens-shaped domains and supports the cited classical lens reduction/bound. |
| `Crouzeix_2003` | Springer DOI `10.1007/s00013-003-0569-7` and DOI-indexed metadata | Crouzeix--Delyon, *Some estimates for analytic functions of strip or sector operators*, Arch. Math. 81 (2003), 559--566; directly supports the strip/sector numerical-range estimate statement.  A page-range typo in isolated secondary citations was resolved in favor of the DOI record and multiple consistent bibliographic records. |
| `MR2449098` | AIMS/CPAA DOI `10.3934/cpaa.2009.8.37` | Badea--Beckermann--Crouzeix, *Intersections of several disks of the Riemann sphere as K-spectral sets*, CPAA 8 (2009), 37--54; directly supports the cited intersection-of-disks uniform spectral-set result. |
| `MR2047592` | Springer DOI `10.1007/s00020-002-1188-6` | Crouzeix, *Bounds for analytical functions of matrices*, IEOT 48 (2004), 461--477; its abstract and metadata support the paper's general numerical-range estimate context. |
| `Crouzeix_2016` | SIAM DOI `10.1137/15M1020411` and the author's official manuscript | Crouzeix, *Some constants related to numerical ranges*, SIAM J. Matrix Anal. Appl. 37 (2016), 420--442; directly supports the cited numerical-range constants and open-problem perspective. |

The per-reference checks were performed sequentially because the independent
agent pool was already at its project concurrency limit; the required
primary-source checks were not omitted.  No bibliography file or citation key
was edited.

## 4. Clean LaTeX/BibTeX build and log gate

Only `main.tex` and `references.bib` were copied into a fresh temporary build
directory.  From there the following returned exit code 0 and converged under
`latexmk` 4.88:

```sh
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The build produced an 18-page US-letter PDF.  The packaged bibliography
checker and the independent LaTeX auditor both reported:

```text
cited keys: 5
BibTeX keys: 5
cited keys missing from bibliography: 0
unused entries: 0
auxiliary-file disagreements: 0
```

The converged `main.log` and `main.blg` have zero matches for undefined
citations or references, missing database entries, repeated entries, LaTeX or
package warnings, fatal errors, undefined control sequences, runaway
arguments, overfull boxes, or underfull boxes.

Relevant SHA-256 values are:

```text
84e9487e7765e73a0356b6368d99ac820529e259a3eebe40eb7a35ce110c4913  main.tex
989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600  references.bib
3d8e3ac2c999b50e84b126e5f04e108d3e74f0e971aa2ca9f91eaa4742d04f1b  main.bbl
70985fae0c3dc01a0666143a5505b3391df9923ef3c76cc8b290291ac90547aa  clean rebuild PDF
```

The clean PDF container hash differs from the delivered PDF because pdfTeX
regenerated metadata.  Their rendered page content is identical, as checked
below.

## 5. Release manifest, archive, and fresh extraction

Before this referee report was added, the candidate release contained 335
files including `RELEASE_MANIFEST.sha256`.  The manifest listed 334 bound
files, and all 334 checks passed.  Its SHA-256 was

```text
5a4849fd36b13ed14e8aaf2fd4fcc037c4cc055f95dc3f8a05f4cfdf7fc24690.
```

The pre-audit candidate ZIP had SHA-256

```text
beb59464903af984f8addd5518775d8a6c0002d2673d33b096e4d20f228ab204,
```

and its external `.zip.sha256` sidecar agreed.  A fresh extraction contained
exactly one top-level directory, 335 files, and the same 334-entry manifest;
all 334 checks passed.  The extracted packaged `main.pdf` was byte-identical
to the separately delivered output PDF.  The extracted `main.tex`,
`references.bib`, `main.bbl`, and release manifest matched the candidate tree.

The delivered and packaged PDF SHA-256 is

```text
eccc150b8486fd18e3aa37bdbc6a1b61282d2df7ad10583445521bec10716a27.
```

The historical workspace checkpoint replay has four expected post-checkpoint
live-state differences in `APPROACH_REGISTRY.md`, `CLAIM_LEDGER.md`,
`COUNTEREXAMPLE_DB.md`, and `research_state.json`.  They are outside the
candidate release manifest and are not a v7 archive defect.

Because this report is the only new release-tree file created by the
independent referee, the root release task must now add it to a regenerated
release manifest, rebuild the ZIP and external sidecar, and rerun the final
manifest/archive/PDF-identity checks.  That mechanical post-audit closure will
necessarily change the manifest and ZIP hashes quoted above; it does not
change this mathematical verdict.

## 6. PDF visual and pixel-identity audit

The delivered PDF and the clean rebuild were independently rendered with
Poppler at 150 dpi.  Each produced exactly 18 PNG pages, and every
corresponding rendered page was byte-identical.  All 18 pages were inspected,
including the title and abstract, both theorem statements, the notation table,
long aligned formulas, exact-integer appendices, verbatim reproducibility
blocks, disclosure, bibliography, headers, footers, page numbers, and the
final author-address page.

No clipping, overlap, missing glyph, black box, broken equation, malformed
table/reference, or inconsistent page geometry was found.  The large white
space on page 18 is the intentional `amsart` end-matter layout, not a rendering
failure.

## 7. Status language and final classification

`README.md` and `audits/BUILD_TEST_REPORT_2026-08-24_V7_BUILDER.md` correctly
describe the package as a builder-complete partial-theorem candidate awaiting
this independent audit.  They do not claim submission, publication, general
common-metric resolution, fixed-lens resolution, all-node completion, or Lean
formalization.

Final classification:

```text
fatal technical defects: 0
major technical defects: 0
minor technical defects: 0
scientific terminal status: exact computer-assisted partial theorem
proof-assistant status for the two new endpoints: none
independent technical gate: PASS
```

No repair to `main.tex`, `references.bib`, any certificate, the delivered PDF,
or the pre-audit ZIP is recommended.  Only the mechanical post-audit
manifest/README/archive closure described above remains for the release
builder, together with the author's nontechnical metadata and venue checks.
