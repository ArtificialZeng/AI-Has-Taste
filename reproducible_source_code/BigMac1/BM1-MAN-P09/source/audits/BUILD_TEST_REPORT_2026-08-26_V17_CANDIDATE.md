# v17 candidate repair-build report

Date: 2026-08-26.  Status: **repair-builder PASS; fresh independent
submission audit still required**.  This report applies only to the isolated
`tmp/pdfs/v17_candidate` tree.  No v16 or earlier PDF, ZIP, source package,
mathematical certificate, author entry, citation, or formal result was
modified, and no formal v17 output ZIP was created.

## Frozen failed audit and bounded repairs

The first independent v17 submission audit is frozen outside this candidate
at workspace-relative path
`audit/V17_CANDIDATE_INDEPENDENT_SUBMISSION_AUDIT.md`, SHA-256
`607197b7da4cb02d876ddcc93a0cc60cbb1ec832d7e2a1546c43ab55f9c8066d`.
Its verdict was **FAIL (fatal 0 / major 2 / minor 0)**.  It remains historical
external evidence and is not described here as a pass for the repaired bytes.

The repair changes exactly the two manuscript defects identified there:

1. equation (78) now uses the correct `\qquad` command, so no literal
   missing-backslash spacing token is printed;
2. the unchanged exact legality derivation for the constant-$Z$ cell
   `99/100 <= X <= 497/500` has been removed from the proof of the recentered
   sheet and placed inside the proof of the constant-$Z$ theorem, after
   `Z_const` is defined and after the first-cell legality calculation but
   before the gate-sign calculation.

The recentered proof now discusses only its eight asserted cells.  The
constant-$Z$ theorem is locally self-contained for both of its asserted
cells.  No formula, bound, quantifier, label, certificate, author, or
bibliographic record was otherwise changed.

## Integrated mathematical delta

The candidate transcribes three post-v16 results that had already passed
independent definition-level referees:

1. the constant-`Z` sheet is extended by the cell
   `99/100 <= X <= 497/500`, with `40/40` strict controls;
2. the seam-preserving cap chart
   `x=x_old-(3/2)(X-497/500)`, `y=y_old`,
   `Z=Z_const+2(X-497/500)` covers `497/500 <= X <= 1`, with a three-level
   seam and `72/72` strict controls;
3. the independent all-scale box `Z=1/8`,
   `|x-5/8|<=1/1000`, `|y|<=1/100`, both signed lifts,
   `0<h<=1`, `lambda>0`, has `531/531` strict trivariate controls.

The fixed ray and `x=5/8` y-strip are described only as nested predecessors.
The manuscript explicitly leaves the full compact ball, unrestricted complex
common-metric theorem, arbitrary nodes and dimension, and the fixed-lens
optimal constant open.

## Author and bibliography gates

The complete author block from Zijian Zeng through `\date` remains identical
to frozen v16.  In particular, `Yonghua Xiong*` and
`* Corresponding Author: Yonghua Xiong` remain unchanged.  PDF metadata lists
the same five authors.

No citation was added or changed.  `check_bib_keys.py main.tex` reports five
cited keys, five BibTeX keys, and zero missing or unused keys; `main.aux`
contains the same five keys.  Final `main.log` and `main.blg` contain zero
LaTeX/package warnings, undefined references, undefined citations,
multiply-defined labels, Overfull boxes, or Underfull boxes.

## Deterministic clean builds

Two serial, fully clean runs used

```text
latexmk -C main.tex
SOURCE_DATE_EPOCH=1787673600 FORCE_SOURCE_DATE=1 \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Both exits are zero.  Their complete console logs are byte-identical with
SHA-256
`7549de2fbffbac59930589f461336c1bc08eedc8584f1efa4044f66d7060b783`.
Both builds produce the same 41-page PDF:

```text
main.pdf  41f816165950f9d5369f0cc4583b33f396fb7bb3d3b937d8a62f8b1177611939
```

Key repaired artifacts before the candidate package manifest are:

```text
main.tex       cfd1be699b3fba93b16288d846552ce883f2b75883a930ea527c1de87b67e6ff
main.bbl       3d8e3ac2c999b50e84b126e5f04e108d3e74f0e971aa2ca9f91eaa4742d04f1b
references.bib 989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600
README.md      c0fc9523b19569feb40c9d72cb8b6937a2ad84968c39f536338b436f084d2aea
make_release.py a87655ccb1e5a5fdcc786f41728c862ad5b72b91fdab8b0e09210064167cf22b
```

`pdfinfo` gives 41 letter pages, no encryption, PDF 1.7,
creation/modification time `2026-08-26 00:00:00` under the fixed epoch, and
the unchanged paper title.  `pdffonts` shows every font embedded.

## Certificate-package gate

Frozen files remain unedited in their native relative paths under
`certificate_workspace/`.  The six primary post-v16 source/referee manifests
pass package-local `shasum -a 256 -c` verification:

```text
constant source  8/8   e7220043d9ac01c91e72ebf4029a8c248bff77bb2225b2884b5c372c60df108d
constant referee 35/35 50c451f84eabfdb7832e3610c37bd347dc1419c109f64b7c7cece41e8e60eb06
cap source       8/8   8d68e2cbeb9e56e86b818dfcdfb1e4ebc1ac5cc5a678ab4c3857a55cde0d2cc5
cap referee      40/40 3cdbb03409be176c7d557056e3fcbd426e14563f35d81edc18b03dbd43064a9c
local-box source 21/21 9655e59e124f8a8dd2aaf661a052f70c9d489c058e638c2d8212c7c6b794422d
local-box referee 64/64 dcd4d091a8b2b9fc714c1e79571a3f251b747777ff91721fe1f5a1f7ab9a67cd
```

The three independent reports in `audits/` retain their frozen hashes:
`ed2cb482...b61c45`, `b8db0fa9...4e71d`, and
`d5560cb0...6cb0a` for the constant extension, cap shear, and local box.

## Top-level package and fail-closed gate

The regenerated JSON release manifest contains exactly 1174 records.  The
package-local verifier reports `PASS JSON release manifest: 1174/1174
records`.  In separate temporary copies, appending one byte to `README.md`
makes the verifier exit 1 with `record mismatch README.md`; restoring the
tree and adding an unlisted sentinel makes it exit 1 with a file-set mismatch
that names the extra file.  Thus the repaired candidate fails closed for both
changed bytes and extra files.

## Text and visual QA

Poppler rendered all 41 pages at 150 dpi.  Six contact sheets covering every
page were inspected.  Pages 1, 20, 24--26, and 40--41 were additionally
rendered at 300 dpi and inspected at original detail.  Page 20 now displays
proper mathematical spacing in equation (78), with no literal artifact.
Pages 24--25 now show the second constant-$Z$ cell derivation inside the
constant-$Z$ proof, after the definition and first-cell legality argument and
before its gate-sign argument.  No clipping, overlap, broken table, black
square, unreadable glyph, header/footer defect, or page-numbering defect was
found.

Extracted PDF text has no missing-backslash spacing token, repeated variant,
or unresolved placeholder marker.  It retains the three exact domains and control counts, the
corresponding-author line, and the explicit unresolved-scope statements.

The repair builder therefore passes the bounded manuscript repair,
deterministic clean-build, bibliography, metadata, package-local certificate,
text-scope, and visual gates.  Promotion to submission-ready status remains
withheld pending a fresh independent audit of the newly frozen candidate
manifest and bytes.
