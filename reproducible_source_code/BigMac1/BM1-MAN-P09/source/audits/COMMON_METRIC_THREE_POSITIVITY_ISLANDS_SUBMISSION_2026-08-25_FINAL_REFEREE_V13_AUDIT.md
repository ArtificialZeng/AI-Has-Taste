# FINAL_REFEREE_V13 independent final audit

Date: 2026-08-25  
Role: independent final referee; no builder conclusion was trusted  
Workspace root: derived from this report's repository, never from a packaged
absolute path

## Verdict

**PASS** under the required rule that a pass requires zero fatal and zero
major findings.

| Severity | Count |
|---|---:|
| Fatal | 0 |
| Major | 0 |
| Minor | 1 |

The one minor finding is a local documentation defect in the integrity
command; it does not affect the archive bytes, the complete JSON release
manifest, the exact mathematical certificates, the deterministic build, or
the delivered PDF.  The frozen candidate was not modified.

This is a technical submission-package pass for the **partial scalar-gate
theorems actually stated**.  It is not a proof of the full compact-ball
quartic, the general common-metric problem, the optimal constant of a fixed
crossing lens, an arbitrary-node bridge, or arbitrary dimension.  Those
problems remain open.  Author identity and venue-specific AI, funding,
acknowledgment, source-format, and style declarations remain external
pre-submission responsibilities, as the package itself says.

## Frozen objects

The following frozen delivery hashes were independently recomputed before
any audit action and agree with the assigned values:

| Object | SHA-256 | Size/page count |
|---|---|---:|
| `output/pdf/common_metric_three_positivity_islands_submission_2026-08-25-v13.pdf` | `2fff9cad48f3f80281b202ce5f62d8fb72feea57ea50c27570f0c2873ca917f3` | 528,661 bytes; 29 pages |
| `output/source_packages/common_metric_three_positivity_islands_submission_2026-08-25-v13.zip` | `c5b8db2fd9ddb9c5be9fe5d2fc3e10979f274d9a25cd919e743e3efc33b586ad` | frozen ZIP |

All audit extraction and compilation occurred in freshly randomized
`mktemp` directories.  Nothing was compiled in the release directory.

## 1. Archive integrity, manifest, and hygiene

- `unzip -t`: 0 bad entries.
- ZIP topology: **613 entries total**, exactly **586 regular files** and
  **27 directory entries**, under one archive root.  After excluding that
  root, the tree has 26 directories.
- No duplicate member names, traversal paths, absolute member names,
  symlinks, or other special files were found.
- `RELEASE_MANIFEST.sha256` SHA-256:
  `457e75fd445ebcd084b2cfb8e1617d2202c6868d2481d1d6b7d105a6138ad13b`.
- Despite its suffix, this file is a JSON object.  Its `files` map contains
  exactly **585 records**, one for every regular file except the manifest
  itself.  Independent recomputation found:
  **missing 0, extra 0, bad sizes 0, bad hashes 0, duplicate paths 0**.
- No `.venv`, `.lake`, `.git`, `__pycache__`, `.pyc`, Python/TeX caches,
  `.aux`, `.log`, `.fls`, `.fdb_latexmk`, `.synctex.gz`, `.DS_Store`, or
  generated build rubbish is present.
- A byte scan found no `/Users/`, `/home/`, Windows-drive absolute path, or
  `file://` host binding.
- The package's `main.pdf` is byte-for-byte the delivered PDF.

### MINOR-001: documented manifest command is incompatible with the manifest format

`README.md` lines 304--306 correctly say the manifest binds every other
distributed file, but instruct the reader to run
`shasum -a 256 -c RELEASE_MANIFEST.sha256`.  That command expects
line-oriented checksum syntax, whereas the file is JSON.  Reproduction gave
exit status 1 and:

```text
shasum: RELEASE_MANIFEST.sha256: no properly formatted SHA checksum lines found
```

Classification: **minor**.  The manifest itself is complete and correct and
was independently verified record by record; the defect is only the stated
one-line verification command.  A future revision should either ship a
standard checksum file or document a JSON-aware verifier.  The frozen v13
candidate was deliberately not repaired.

## 2. Mathematical scope and claim audit

The paper title, abstract, introduction, theorem statements, Section 10,
conclusion/reproducibility discussion, README, certificate scripts, and audit
notes were compared rather than sampled.

- Exact title: *Three exact local positivity islands and a high-Z
  complex-phase tube for a Hermitian rank-two scalar gate*.
- There are exactly **six theorem environments of interest**:
  one exact scale-cubic criterion and **five positivity theorems** (all-scale,
  centered moving sheet, affine-omega tilted sheet, inward-Z sheet, and
  high-Z tube).
- “Three islands” is expressly defined as three classes of local region:
  (1) the all-scale Schur-boundary island; (2) the seam-stitched but
  formula-distinct centered, affine, and inward compact-ball family; and
  (3) the high-Z tube.  The terminology does not assert three global sheets.
- The abstract and main text consistently describe a finite-dimensional,
  rank-two scalar-gate sufficient condition and exact local families.
- The manuscript explicitly leaves open the arbitrary complex Hermitian
  gate outside the displayed families, the full compact unit ball, a common
  metric for all separators/data, the arbitrary-node bridge, arbitrary
  dimension, and the optimal fixed crossing-lens constant.
- The 72/72 exact rational node values are explicitly and repeatedly called
  **falsification diagnostics only**.  The continuum theorem is instead
  based on exact Bernstein positivity.  No numerical minimum, floating-point
  SDP, or plotted evidence is promoted to a theorem.
- The statement that the v13 builder candidate awaited a separate final
  audit is faithful freeze provenance: the independent audit is this
  external report.  It is not a mathematical overclaim.
- The disclosure says no Lean or other proof assistant formalizes these
  complex theorems.  That agrees with the evidence; no proof-assistant claim
  was inferred.

The manuscript uses `Gate=4*gate` globally and the compact certificate uses
`36*Gate`; the normalizations, inequalities, and reserves were checked with
those factors and are consistent.

## 3. New inward-Z theorem: independent exact audit

The package-local source verifier, independent referee, theorem statement,
source note, test report, and both manifests were read and compared.  The
source and referee do not share the asserted polynomial/control table: the
referee reconstructs the signed Gram data in a different column/vector order
and performs an independently ordered Bernstein transform.

### Parameters and seam

The audited family is exactly

```text
0 < S <= 1/10000,      3/13 <= X <= 1/4,
|M| <= 1/1000,         |omega|, |nu| <= 1/100,
A = 1+M,               lambda = A/S,
y0 = 12/(25A)+nu,
omega_phys = omega-(10636/275)(X-1/5),
b = (45M+18)/(25A)-(3/5)X+omega_phys,
x = -1/5+X,            y = 3/5+S*y0,
Z = 9/13-X^2+S*b-S^2*y0^2.
```

The identity `Z_in-Z_tilt=-3(X-3/13)` proves the exact, parameter-by-parameter
seam at `X=3/13`; away from the seam these are different sheets.

### Legality and rank

Independent rational reconstruction verified

- `lambda>0`;
- `46999/100100 <= y0 <= 16333/33300`;
- `-69948/50875 <= b <= -299011/500500 < 0`;
- `9984760329129934873/15857127000000000000 <= Z < 108/169 < 1`;
- strict danger
  `D=(2/5)(X-3/13)-S*T >= (2/5)(X-3/13)+S/100 > 0`;
- `det(C)=(5/9)SZ>0`, hence the support compression has rank two;
- the construction depends on `z` only through `Z=z^2`, so both signs of
  `z` are covered.

The original fully conjugated gate, its `Q^2` terms, the danger term, and the
positive clearing factors were reconstructed rather than accepted from a
cached discovery polynomial.

### Exact continuum certificate

Both programs independently returned all of the following:

- definition-level direct `(S,X)` terms: **32**;
- core `(S,X)` coefficients: **32**;
- centered parameter monomials: **1,581**;
- quotient bidegree: **(7,4)**;
- first nonzero scale layer: `S^3`;
- Bernstein degree on the rectangle: **(7,9)**;
- controls: **80 total**, exactly **3 closure zeros** at
  `(0,0)`, `(0,1)`, `(1,0)`, and **77 strict positive controls**;
- least strict control, at `(2,0)`:
  `10071067674014002577317165966399410637259618083 /
  128416777961472000000000000000000000000000000`;
- 72/72 diagnostic nodes legal and positive, with minimum exact `36*Gate`
  at `(S,X,M,omega,nu)=(1/10000,3/13,-1/1000,1/100,-1/100)` equal to
  `182249907370437372958214245586018359494715888079 /
  16726464040000000000000000000000000000000000`;
- least nodal danger: `1/100000000`.

The three zero controls occur only at the artificial `S=0` closure.  On the
physical domain, the normalized scale parameter `tau` is positive and

```text
W(tau)=sum_{i=2}^7 binom(7,i) tau^i (1-tau)^(7-i)
      =1-(1-tau)^7-7*tau*(1-tau)^6 > 0.
```

All controls in rows `i>=2` are at least the stated strict reserve; the
Bernstein basis sums to one.  Therefore the core is strictly positive for
`tau>0`, and division only by the independently positive clearing factors
proves the original gate sign.  This closes the continuum logically; the
diagnostic nodes are unnecessary to the proof.

### Independent executions and fail-closed attacks

The cold package was run with Python 3.11.15 and SymPy 1.14.0 reconstructed
from the project manifest.  No system environment or copied cache was used.

- source verifier, normal execution: **PASS**;
- independent referee, normal execution: **PASS**;
- both direct checksum manifests: **PASS**, eight checked dependencies in
  each relevant chain;
- external `py_compile` with cache redirected to `mktemp`: **PASS**;
- source under `python -O`: **FAIL CLOSED**;
- referee under `python -O`: **FAIL CLOSED**;
- referee with bad dependency-hash injection: **FAIL CLOSED** before proof;
- referee with a deleted core gate term: **FAIL CLOSED** at the reconstructed
  32-coefficient gate.

The certificate does not reuse the absorption, real-part, or universal
allocation routes rejected by CE-046, CE-048, CE-059, or CE-060.  Those
counterexamples remain respected.

## 4. Cold deterministic LaTeX builds

Two independent clean builds were performed from two fresh extractions:

```text
SOURCE_DATE_EPOCH=1787625600 FORCE_SOURCE_DATE=1 latexmk -C main.tex
SOURCE_DATE_EPOCH=1787625600 FORCE_SOURCE_DATE=1 \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Results for both builds:

- PDF SHA-256:
  `2fff9cad48f3f80281b202ce5f62d8fb72feea57ea50c27570f0c2873ca917f3`;
- 528,661 bytes, 29 pages;
- build 1 = build 2 = packaged PDF = delivered PDF, byte for byte;
- `main.tex` SHA-256:
  `bab35874250bb9d64096a0de6c4a4ca25842caa4b76e4642939b52af2bba360a`;
- `references.bib` SHA-256:
  `989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600`;
- converged `main.bbl` SHA-256:
  `3d8e3ac2c999b50e84b126e5f04e108d3e74f0e971aa2ca9f91eaa4742d04f1b`;
- final converged logs: undefined citations 0, undefined references 0,
  missing/repeated BibTeX entries 0, LaTeX/BibTeX warnings 0, overfull boxes
  0, underfull boxes 0, font/missing-character warnings 0, fatal errors 0.

Transient first-pass reference notices in `latexmk` output disappeared in
the converged logs and are not final-build warnings.

## 5. Bibliography and citation context

Mechanical closure is exact: **5 cited keys, 5 BibTeX entries, 5 generated
`thebibliography` items, all 5 used, 0 missing, 0 unused, 0 duplicate**.
The key sets in `main.tex`, `main.aux`, `references.bib`, and `main.bbl`
agree.

The five records and their use were checked against the authoritative pages,
not merely for BibTeX syntax:

| Key | Authoritative evidence | Manuscript context | Result |
|---|---|---|---|
| `MR2223270` | Springer, DOI `10.1007/s00013-005-1533-5` | classical lenticular reduction/bounds | supported |
| `Crouzeix_2003` | Springer, DOI `10.1007/s00013-003-0569-7` | strip/sector operator estimates | supported |
| `MR2449098` | AIMS, DOI `10.3934/cpaa.2009.8.37` | intersections of spherical disks and uniform spectral-set bounds | supported |
| `MR2047592` | Springer, DOI `10.1007/s00020-002-1188-6` | matrix/numerical-range bounds and low-dimensional perspective | supported |
| `Crouzeix_2016` | SIAM, DOI `10.1137/15M1020411` | later constants and numerical-range perspective | supported |

Result: **5/5 official records verified, 5/5 citation contexts supported,
0 replacements, 0 key changes, 0 blockers**.  The SIAM direct BibTeX endpoint
is access-restricted, but the official article page and DOI metadata agree;
this is not a bibliographic uncertainty.

## 6. PDF structure, extraction, and 29/29 visual audit

Poppler rendered all **29/29 pages** at 110 DPI to 935-by-1210 PNGs.  Every
page was inspected, including title/abstract, each theorem and proof, the
inward-Z theorem on pages 17--19, the high-Z table, the scope/disclosure
section, long exact-rational appendices, references, and contact block.

- clipped/cropped content: 0 pages;
- overlapping text/formulas/tables: 0 pages;
- visible margin overflow: 0 pages;
- unreadable formulas, tables, appendix numbers, or references: 0 pages;
- blank or failed render: 0 pages.

The rendered ink boxes stay inside the page with substantial margins (all
pages had nonempty text; observed x range 192--745 and y range 146--1084 in
the 935-by-1210 renders).  Page 29's large lower whitespace is normal after
the bibliography/contact block, not missing content.

PDF structural checks:

- title, author, subject, keywords, dates, producer, and 29-page metadata are
  present and consistent;
- letter size, rotation 0, PDF 1.7;
- encrypted: no; JavaScript: no; forms: none; embedded files: 0;
- Poppler `Suspects: no`;
- **30/30 fonts embedded, 30/30 subset, 30/30 Unicode mappings**;
- layout-preserving text extraction succeeded for all 29 pages (75,239
  bytes; 29 page separators), including title, equations, references, and
  final contact text.

## 7. Frozen v11/v12 nonmutation baseline

The prior final-referee records were used only to obtain the baselines; all
four current artifact hashes were then recomputed independently:

| Frozen artifact | Recomputed SHA-256 | Result |
|---|---|---|
| v11 PDF | `91794e054228d51cabbe5afb735bb52a0aec890e7633c582c25e7176695db641` | unchanged |
| v11 ZIP | `250a51826c798a7334feee9da6ed9ea19c8ed41ddb2319cbce6d981f9dfaef91` | unchanged |
| v12 PDF | `1359a72329ef81a8c9e1c23eac680d157439c7f1ba8bbd06f04f19a4d643c70a` | unchanged |
| v12 ZIP | `ac6a27fb92163d7099108092dadc9ef184f9eb79ea1420503d4cb8b9427931c8` | unchanged |

The historical checkpoint checksum file was also exercised.  Its only four
reported differences are the intentionally live project state files
`CLAIM_LEDGER.md`, `APPROACH_REGISTRY.md`, `COUNTEREXAMPLE_DB.md`, and
`research_state.json`; all other historical checkpoint entries verified.
That old checkpoint snapshot is not the v13 release manifest and does not
alter this verdict.

## 8. Independent release verifier

The read-only standard-library verifier
`audit/VERIFY_COMMON_METRIC_THREE_POSITIVITY_ISLANDS_SUBMISSION_2026_08_25_FINAL_REFEREE_V13.py`
checks the six frozen v11/v12/v13 artifact hashes, ZIP CRC/topology/path
safety, all 585 JSON manifest records, package hygiene, packaged/delivered
PDF identity, exact theorem/citation sets, and required scope markers.

Normal result:

```text
FINAL_REFEREE_V13 INTEGRITY VERIFIER: PASS
frozen_artifact_hashes=6/6
archive_entries=613 files=586 manifest_records=585 manifest_bad=0
theorems=6 positivity_theorems=5 scale_cubic=1 citations=5 bibliography=5
packaged_pdf_equals_delivered_pdf=yes
```

It compiles externally and fails closed under `python -O`.

## Final disposition

Fatal 0; major 0; minor 1.  **PASS.**  The frozen PDF and ZIP may be treated
as independently audited technical delivery artifacts for the five local
positivity theorems and the scale-cubic criterion stated in the manuscript.
No new PDF or ZIP was created, and no candidate, ledger, builder report,
manuscript/release directory, or prior frozen artifact was modified.
