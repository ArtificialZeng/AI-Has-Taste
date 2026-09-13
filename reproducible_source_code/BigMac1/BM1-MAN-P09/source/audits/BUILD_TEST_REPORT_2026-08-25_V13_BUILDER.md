# v13 inward-Z builder test report

Date: 2026-08-25 (Asia/Shanghai)  
Status: **technical builder candidate only; pending a separate independent
v13 final manuscript/archive referee.**  This report is builder evidence,
not peer review and not an unconditional declaration that the archive is
ready for journal upload.

## 1. Honest mathematical scope

Version 13 preserves the frozen v12 partial results and adds one separately
frozen compact-ball partial theorem.  The new inward-`Z` chart uses

```text
0<S<=1/10000, 3/13<=X<=1/4,
|M|<=1/1000, |omega|,|nu|<=1/100,
mu=1+M, lambda=mu/S,
y0=12/(25mu)+nu,
omega_phys=omega-(10636/275)(X-1/5),
b=(45M+18)/(25mu)-(3/5)X+omega_phys,
Z=9/13-X^2+S*b-S^2*y0^2.
```

Its full parameter tuple agrees with the affine-`omega` chart at the exact
seam `X=3/13`, where `Z_in=Z_tilt`.  Away from that seam it is a different
sheet.  Exact legality proves `lambda>0`, `0<Z<1`, rank two for both signs of
`z`, and strict danger.  The normalized gate certificate has 32 nonzero
`(S,X)` coefficients; after removing one explicitly nonnegative layer its
core again has 32 coefficients and 1,581 centered monomials.  The map

```text
X=3/13+u/52,   S=(13/30000)*tau*X
```

gives Bernstein degree `(7,9)` and 80 exact controls.  Exactly three controls,
`(0,0)`, `(0,1)`, and `(1,0)`, vanish on the artificial `S=0` closure; the
other 77 are strictly positive.  The exact reserve is

```text
10071067674014002577317165966399410637259618083
--------------------------------------------------- .
128416777961472000000000000000000000000000000
```

The apparent boundary zeros are discharged analytically by

```text
W(tau)=1-(1-tau)^7-7*tau*(1-tau)^6
      =sum_{i=2}^7 binom(7,i) tau^i (1-tau)^(7-i)>0
```

for `tau>0`.  The 72 exact rational nodes are falsification diagnostics only;
they are not used as a continuum proof.  No Lean theorem covers this result.

The centered, affine, and inward charts form a stitched family through two
exact seams but are not a single global parameter sheet.  The other two
positivity families are the all-scale Schur-boundary island and the high-`Z`
phase tube.  The paper contains five positivity theorems and one scale-cubic
reduction; the title's “three islands” names those three local result classes,
not three theorems and not global coverage.

The full compact ball, unrestricted common-metric gate, arbitrary-node bridge,
and optimal constant for a fixed crossing lens all remain open.

## 2. Frozen evidence and release-local replay

The new theorem consumes only the following frozen root artifacts:

| artifact | SHA-256 |
|---|---|
| source program | `6ee91b88c1835f44183a8da833239c817cdd6d079d73cd5b9e9c42428661f6ca` |
| source note | `7b78d77ef418de755f41d8fcbd7b8aaa15eae1b1052276fe1a90274c1989e563` |
| source freeze manifest | `dddb1e18ed0e0972d75d7099ccc75409f7ac609db9bead51a61046ff3f05d614` |
| independent no-import referee | `e6cb94c9ecd322190e959ede9ce19131e57a6964dfb29ccd88f76c076abff3c0` |
| independent referee audit | `bde3d29e63f8e9672494a824da34f9081ca0349b37f1cdcaa317d5b7c874c2d5` |
| independent referee manifest | `db05941b343bbd680c81c075f89d0aaa46e750e2e27a9f40577c58644528390e` |
| referee test record | `048870c69da355441f16c98956f374b53dec97f100169056373e3e66175b660b` |

Normal release-local source and referee replays both exited `0`, independently
recovering the signed-`z` gate, legality, seam, `32/32/1581`, all 80 controls,
the three closure zeros, 77 strict controls, the same reserve, and all 72
diagnostic nodes.  The source manifest passed `2/2`; the referee manifest
passed `8/8`.  The referee rejected optimized Python, a corrupted dependency,
and a deleted raw-gate term, while an external-cache `py_compile` succeeded.

The release initially lacked the referee audit at the exact canonical
relative path named by the frozen manifest.  That packaging defect was caught
before archive creation, the byte-identical frozen audit was added at that
path, and the manifest was rerun successfully.  No theorem statement or
certificate was changed.

The frozen v12 deliverables were not edited or rebuilt:

| frozen artifact | SHA-256 |
|---|---|
| v12 PDF | `1359a72329ef81a8c9e1c23eac680d157439c7f1ba8bbd06f04f19a4d643c70a` |
| v12 ZIP | `ac6a27fb92163d7099108092dadc9ef184f9eb79ea1420503d4cb8b9427931c8` |

## 3. Bibliography gate

The bibliography remains the same five-entry surface.  Independent online
verification found `5/5` real records and `5/5` valid citation contexts, with
zero replacement, zero key change, and zero blocker.  The authoritative
records were checked at the Springer pages for `MR2223270`, `Crouzeix_2003`,
and `MR2047592`, the AIMS page for `MR2449098`, and the SIAM page plus Crossref
metadata for `Crouzeix_2016`.  The malformed raw AIMS BibTeX and the SIAM
BibTeX endpoint's HTTP 403 were not used to replace already-correct entries.

The final key audit reports `cited=5`, `bib=5`, `missing=0`, and `unused=0`.
The converged LaTeX/BibTeX log has no undefined citation, undefined reference,
or rerun warning.

## 4. Deterministic LaTeX and PDF gates

Two clean builds with `SOURCE_DATE_EPOCH=1787625600` and
`FORCE_SOURCE_DATE=1` produced byte-identical PDFs:

- build A SHA-256: `2fff9cad48f3f80281b202ce5f62d8fb72feea57ea50c27570f0c2873ca917f3`;
- build B SHA-256: `2fff9cad48f3f80281b202ce5f62d8fb72feea57ea50c27570f0c2873ca917f3`;
- `main.tex`: `bab35874250bb9d64096a0de6c4a4ca25842caa4b76e4642939b52af2bba360a`;
- `main.bbl`: `3d8e3ac2c999b50e84b126e5f04e108d3e74f0e971aa2ca9f91eaa4742d04f1b`;
- `references.bib`: `989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600`.

The converged log contains no citation, cross-reference, box, font, or other
warning.  The PDF has 29 US-letter pages, deterministic title/author/date
metadata, no encryption, JavaScript, or form, 57,527 bytes of extracted text,
and every font is embedded, subset, and Unicode-mapped.  Poppler rendered all
29 pages; every page was inspected at full-page scale, including the dense
new theorem and exact-data pages.  No clipping, overlap, overflow, blank page,
missing glyph, or illegible formula was found.

## 5. Archive acceptance

Fresh-ZIP acceptance: **PASS.**  A random-directory extraction verified all
585 release-manifest entries, contained no forbidden host path or binary cache,
and completed a clean deterministic LaTeX build.  The packaged, delivered,
and freshly rebuilt PDF files were byte-identical, all with SHA-256
`2fff9cad48f3f80281b202ce5f62d8fb72feea57ea50c27570f0c2873ca917f3`.
The extracted no-import referee then passed its full exact reconstruction and
rejected optimized Python, a corrupted dependency, and a deleted raw-gate
term; external-cache `py_compile` passed without writing into the release.
After this status line was frozen, the manifest and archive were regenerated
after each release-description correction; the final ZIP was freshly
extracted again for a last manifest, host-path, clean-build, and PDF-identity
check.

## 6. Deliberately unresolved nontechnical metadata

The author name, affiliation, and email are inherited from the frozen v12
source but still require author confirmation.  The target journal and exact
venue style are not selected.  Venue-specific AI-disclosure language,
funding, acknowledgments, conflicts, and any data/code availability statement
must be confirmed before submission.  No value is invented for these fields.

Even after all technical gates pass, this remains a builder candidate until a
different independent final referee audits the v13 manuscript and archive.
