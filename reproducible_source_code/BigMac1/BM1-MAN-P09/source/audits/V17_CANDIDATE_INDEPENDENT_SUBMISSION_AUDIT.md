# v17 candidate independent submission audit

Date: 2026-08-26  
Candidate: `tmp/pdfs/v17_candidate/`  
Mode: independent, read-only submission audit  
Verdict: **FAIL — repair, rebuild, refreeze, and reaudit**  
Classification: **fatal 0 / major 2 / minor 0**

The candidate is not submission-ready.  The frozen exact certificate chains,
scope of the mathematical results, bibliography, deterministic build, fonts,
and release manifest all passed.  Two independently reproducible manuscript
defects nevertheless block promotion.  Neither finding refutes the underlying
exact local positivity certificates; both are defects in the candidate being
submitted.

## Major findings

### M1 — malformed LaTeX is visibly printed in equation (78)

`main.tex:1197` contains

```tex
S=\frac{13}{30000}\tau X,qquad 0\le u,\tau\le1.
```

The missing backslash before `qquad` is not harmless source style.  It appears
in the frozen PDF on page 20 as the literal token `qquad0` between the formula
for `S` and `0 <= u,tau <= 1`; `pdftotext -layout` reproduces it at extracted
text line 878.  Original-resolution inspection of rendered page 20 confirms
the same defect.  An exact scan found no second bare `qquad` token in
`main.tex`, `README.md`, or the v17 builder report.

This also falsifies the builder report's statement that visual/text QA found
no unreadable glyph or transcription defect.  Repair the command, rebuild the
PDF twice, rerun text and visual QA, and regenerate the release manifest.

### M2 — constant-Z second-cell legality is placed in the wrong theorem proof

`main.tex:1404-1420` proves the legality bounds for the adjacent constant-Z
cell `99/100 <= X <= 497/500`, including the labels
`eq:constant-second-Z`, `eq:constant-second-T`, and
`eq:constant-second-legality`.  That paragraph is currently inside the proof
of `thm:recentered-sheet`, whose asserted interval stops at
`X_rec^*=1019767/1040000`.  Worse, it uses `Z_const` before `Z_const` is
defined at `main.tex:1466-1469`.

The proof of `thm:constant-sheet` begins at `main.tex:1494`, announces
"legality on the two closed cells," but locally establishes legality only on
`X_rec^* <= X <= 99/100`; it relies silently on the paragraph misplaced in the
preceding theorem.  The exact bounds themselves agree with the frozen
constant-Z source/referee artifacts, so this is not a numerical or theorem
counterexample.  It is a material proof-order and attribution defect.  Move
the complete second-cell legality paragraph into the constant-Z proof after
the definition of `Z_const`, then rebuild and refreeze.

## Gates that passed

### Candidate integrity and fail-closed behavior

- `RELEASE_MANIFEST.sha256` has SHA-256
  `07fdec43169469a2bc054f66d7620e37343db668f7ec971c99c44aefd59fdaaa`.
- Independent JSON parsing found exactly 1174 records and exactly 1174 other
  files: missing 0, extra 0, changed hash 0, wrong size 0.
- The package-local verifier independently returned `PASS JSON release
  manifest: 1174/1174 records`.
- In a separate temporary copy, changing one byte in `README.md` made the
  verifier exit 1 with `FAIL: record mismatch README.md`.  Restoring that byte
  and adding an unlisted sentinel made it exit 1 with a file-set mismatch.
  The top-level integrity gate therefore fails closed for both changed and
  extra files.

Frozen candidate hashes were:

| artifact | SHA-256 |
|---|---|
| `main.tex` | `b85d51f4586791da0ed9b6b0b411853ea9e6d3fef91c334b8e71b69685ad7674` |
| `main.pdf` | `5f2fd38573ac786205f6ecaaba6d6b4ab6acbc0351d71987edc33a995cb841ac` |
| `main.bbl` | `3d8e3ac2c999b50e84b126e5f04e108d3e74f0e971aa2ca9f91eaa4742d04f1b` |
| `references.bib` | `989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600` |
| `README.md` | `322467ee06092b9eabe4d2af9114626e19e1edec8cee40cfe743ca033224ccfd` |

### Exact-certificate transcription and scope

The six primary post-v16 manifest chains passed independently from
`certificate_workspace/`:

| chain | records | manifest SHA-256 |
|---|---:|---|
| constant-Z source | 8 | `e7220043d9ac01c91e72ebf4029a8c248bff77bb2225b2884b5c372c60df108d` |
| constant-Z referee | 35 | `50c451f84eabfdb7832e3610c37bd347dc1419c109f64b7c7cece41e8e60eb06` |
| cap source | 8 | `8d68e2cbeb9e56e86b818dfcdfb1e4ebc1ac5cc5a678ab4c3857a55cde0d2cc5` |
| cap referee | 40 | `3cdbb03409be176c7d557056e3fcbd426e14563f35d81edc18b03dbd43064a9c` |
| local-box source | 21 | `9655e59e124f8a8dd2aaf661a052f70c9d489c058e638c2d8212c7c6b794422d` |
| local-box referee | 64 | `dcd4d091a8b2b9fc714c1e79571a3f251b747777ff91721fe1f5a1f7ab9a67cd` |

The three final referee reports are frozen at:

- constant-Z: `ed2cb48240fa5a17eef9e9e76c4e547942642de1cc3997f2c23ae95818b61c45`;
- cap shear: `b8db0fa9bf450312c8921ca9ace147c09b451060647a9b90cb1267992144e71d`;
- local box: `d5560cb01f08bae6634f2b48710dacfda1e03bdd5f8752c651dc3c728586cb0a`.

Apart from M2's placement, the candidate accurately transcribes the exact
claims:

- constant-Z second cell `99/100 <= X <= 497/500`: `32/32/1581`, bidegree
  `(7,4)`, `40/40` strict controls, unique weakest `(7,0)`, the complete exact
  reserve, three-level seam, full-cell `Z`/danger/`det C`/both-sign/rank-two
  legality, and 72 nodes described only as diagnostics;
- cap shear `497/500 <= X <= 1`: `48/48/2263`, bidegree `(7,8)`, `72/72`
  strict controls, unique weakest `(7,8)`, exact reserve, three-level seam,
  endpoint legality, both signs and rank two, with 72 nodes only diagnostic;
- local box `Z=1/8`, `|x-5/8|<=1/1000`, `|y|<=1/100`: control groups
  `1+9+50+147+324=531`, all strict, unique global minimum in the lambda-cubed
  group at `(0,0,6)`, danger `30189/62500`, `det C/S=5/72`, both signs and all
  positive scales.  The coefficient and control-table hashes printed in the
  appendix agree with the referee.

No sampled node is presented as a proof.  CE-046/048/059/060 are not reused.
The manuscript repeatedly distinguishes chart illegality from a negative raw
gate and from maximality.  It does not claim the full compact ball, a general
common metric, arbitrary nodes or dimension, the fixed-lens optimum, or an
unrestricted solution.

### Build and PDF

Two independent copies were cleaned and rebuilt with

```text
latexmk -C main.tex
SOURCE_DATE_EPOCH=1787673600 FORCE_SOURCE_DATE=1 \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Both exits were zero.  Both full console logs have SHA-256
`d16b7f23363bc671d4bfd3cb6f80931ff5cf134ce0eb21e7f48bcb0ce99912f6`,
and both rebuilt PDFs are byte-identical to the candidate PDF.

The archived `V17_CANDIDATE_CLEAN_BUILD_1.log` and `_2.log` are complete
multi-pass `latexmk` console transcripts, not final TeX logs.  They retain 157
matches from first-pass undefined citations/references, then run BibTeX and
additional TeX passes and end with all targets up-to-date.  The converged
`main.log` and `main.blg` contain zero undefined reference/citation warnings,
zero package/LaTeX warnings, and zero overfull/underfull boxes.  Thus the
initial warnings are not a build-gate failure; they must not be described as
warnings in the final `main.log`.

The PDF is 41 letter-size pages, PDF 1.7, unencrypted, with all fonts embedded.
Title, five-author metadata, fixed timestamp, page count, and extracted text
otherwise agree.  All 41 pages were rendered at 150 dpi and inspected in six
contact sheets.  Pages 1, 20, 25-30, 32-33, and 40-41 were also inspected at
original resolution.  No clipping, overlap, black square, broken table,
header/footer defect, or page-numbering defect was found.  M1 is the sole
visible transcription defect found by this pass.

### Authors and disclosures

The title page and source preserve all five authors.  `Yonghua Xiong*`, the
corresponding-author footnote, affiliation, and email are present; PDF author
metadata lists all five authors.  The AI-assistance disclosure limits the
role to transcription, typesetting, build assistance, and exact symbolic
computation.  The manuscript explicitly says no Lean formalization is claimed
for the complex positivity theorems.

### Bibliography

The mechanical key checker returned five cited keys, five BibTeX keys, five
AUX keys, no missing key and no unused entry.  The current contexts and the
official publication records agree:

- `MR2223270`: Beckermann--Crouzeix, *A lenticular version of a von Neumann
  inequality*, Archiv der Mathematik 86 (2006), 352-355,
  [DOI](https://doi.org/10.1007/s00013-005-1533-5).
- `Crouzeix_2003`: Crouzeix--Delyon, *Some estimates for analytic functions of
  strip or sectorial operators*, Archiv der Mathematik 81 (2003), 559-566,
  [DOI](https://doi.org/10.1007/s00013-003-0569-7).
- `MR2449098`: Badea--Beckermann--Crouzeix, *Intersections of several disks of
  the Riemann sphere as K-spectral sets*, CPAA 8 (2009), 37-54,
  [official journal record](https://www.aimsciences.org/article/doi/10.3934/cpaa.2009.8.37).
- `MR2047592`: Crouzeix, *Bounds for Analytical Functions of Matrices*, IEOT
  48 (2004), 461-477,
  [DOI](https://doi.org/10.1007/s00020-002-1188-6).
- `Crouzeix_2016`: Crouzeix, *Some Constants Related to Numerical Ranges*,
  SIAM J. Matrix Anal. Appl. 37 (2016), 420-442,
  [official journal record](https://epubs.siam.org/doi/10.1137/15M1020411).

No BibTeX key or bibliographic field needs changing, and no unsupported or
new citation was found.

## Required repair gate

Do not promote this tree or produce a submission ZIP.  Correct M1, relocate M2
without changing its mathematics, rerun two clean builds, verify the final
logs rather than only the complete console transcript, re-render all pages,
recheck page 20 and the constant-Z proof pages at original resolution, rerun
the six nested manifests and top-level tamper gates, regenerate the top-level
manifest, and submit the newly frozen bytes to a fresh independent audit.
