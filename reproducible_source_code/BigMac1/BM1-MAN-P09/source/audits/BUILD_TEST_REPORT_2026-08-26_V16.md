# v16 builder, certificate, and submission-gate report

Date: 2026-08-26

## Scope

This report covers the consolidated v16 partial-results manuscript and source
package.  The paper proves seven strict local positivity theorems and one
scale-cubic reduction.  It does not prove the full compact ball, the
unrestricted common-metric assertion, arbitrary-node or arbitrary-dimension
extensions, or the optimal fixed crossing-lens spectral constant.

## New exact result

The v16-only constant-`Z` sheet is

```text
Z_const = Z_rec - 2(X-1019767/1040000),
1019767/1040000 <= X <= 99/100.
```

Package-local source and independent no-import referee replays both passed.
They reconstruct the original Hermitian `Q,Q^2` gate and prove:

- degree four in `Z` and positive reversible clearing;
- exact three-level seam at `X=1019767/1040000`;
- cleared/core structure `32/32/1581`, bidegree `(7,4)`;
- `40/40` strict rational Bernstein controls, uniquely weakest at `(7,0)`;
- the literal-free reserve printed in Appendix B.2;
- complete `Z`, danger, `det(C)`, both-sign and rank-two legality;
- `72/72` exact nodes used only as diagnostics;
- rejection of all eight fail-closed attacks.

The source manifest verified `8/8` files and the referee manifest verified
`41/41` files.  Across the eight recentered cells and the constant-`Z` cell,
all eighteen new source/referee manifest chains passed; the independent final
referee additionally checked all `295/295` files bound by those nested chains.

No Lean theorem or other proof-assistant result is claimed for these complex
local theorems.

## LaTeX, bibliography, and PDF gates

Two clean builds were run with

```sh
SOURCE_DATE_EPOCH=1787673600 FORCE_SOURCE_DATE=1 \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

one in the package and one in a fresh temporary copy.  Both produced the
same 36-page PDF byte for byte, SHA-256

```text
a3be35defe20fea1917cb3c9c91a2e86901d1c62a3ea9fcae9f1d2686f8a77be
```

with no undefined citations or references, no LaTeX warnings, and no
overfull or underfull boxes.  The bibliography audit found 5 cited keys,
5 database keys, and 5 generated `bibcite` keys, with no missing or unused
entry.  All 32 PDF fonts are embedded.  PDF metadata reports 36 US-letter
pages and 23 bookmarks.  Text extraction confirms `Yonghua Xiong*` and
`* Corresponding Author: Yonghua Xiong`, together with the supplied author
affiliations and email addresses.

The independent referee visually reviewed all 36 pages and found no clipping,
overlap, unreadable formula, blank content page, or broken bookmark.

## Independent final audit and manifest repair

The first independent final submission audit passed every mathematical,
certificate, build, bibliography, font, bookmark, author, and visual gate but
returned `FAIL (fatal 1 / major 0 / minor 0)` because the top-level JSON
`RELEASE_MANIFEST.sha256` still described the older 629-file package.  That
failure is preserved in `V16_INDEPENDENT_FINAL_SUBMISSION_AUDIT.md`.

The builder then regenerated the JSON manifest with the package's checked-in
`make_release.py`.  The package-local verifier passed the complete current
file set.  Because this report itself is a distributed file, the manifest is
regenerated once more after this report is added and is then subjected to a
fresh independent repair audit before release.

## Release gate

No PDF or ZIP is a final release until all of the following pass after the
last manifest regeneration:

1. package-local JSON manifest verification;
2. independent manifest-repair submission audit with fatal/major equal to 0;
3. deterministic ZIP creation without overwriting an older release;
4. fresh-extraction manifest verification and clean rebuild;
5. final all-page visual inspection of the distributed PDF.

