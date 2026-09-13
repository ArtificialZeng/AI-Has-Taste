# v18 repaired-candidate build, portability, and visual-QA report

Date: 2026-08-26  
Status: repaired builder gates passed; new independent submission audit still required.  
Candidate root: `common_metric_three_positivity_islands_submission_2026-08-26-v18/`

This report concerns only the v18 candidate tree under `tmp/research/`.
Nothing was promoted to the formal `output/` directory.  The frozen v17 PDF,
ZIP, and release manifest were checked before this build at, respectively,

- `41f816165950f9d5369f0cc4583b33f396fb7bb3d3b937d8a62f8b1177611939`;
- `86e337dc5408db8aa226cbcf6b65c8ee81a0785cab1cdaa1cebf80e028e2a1ba`;
- `b372a05ca9c10aac7acde5a33fbc8dda03b683301613617fa1e4d74d81de03bd`.

## Portability repair history

The first v18 candidate failed the first stage of independent submission
audit with one major portability defect: 277 historical generated `.log` or
`.txt` files under `certificate_workspace/` contained a machine-specific
user-home path.  Its ZIP SHA-256 was
`0e549206bb0d2a809fe650fe818d0023868f407322d7c50da10dcf2b7a91763e`.
That archive is identified here only as failed audit history and is not
represented as a pass.

The repaired candidate was copied into a new tree.  Exactly those 277
generated transcript/diagnostic files were omitted; no retained file was
string-rewritten.  No source code, source/referee note or report, historical
manifest, or one of the 32 principal post-v17 files was omitted or changed.
The policy and fresh direct replay commands are recorded in
`certificates/PORTABILITY_NOTE.md`.  Because some historical manifests name
an omitted generated transcript, this repaired report does not claim a
complete line-oriented replay of those old transcript manifests.

A later independent audit failed that repaired candidate with two major
portability findings: retained generated files still exposed absolute
temporary-directory paths, and the eight historical post-v17 manifests named
113 unique omitted members.  This portable-chain repair does not rewrite or
silently repoint those historical manifests.  It omits the 15 generated or
old-audit files containing 16 absolute temporary-path occurrences and adds a
parallel `certificates/xy_box_post_v17_portable/` layer built from fresh
relative-path runs.  The old manifests remain provenance anchors only.

## Mathematical scope checked in the candidate

The existing local-box theorem is upgraded to the strict stitched partial
theorem

```text
Z=1/8,  313/500 <= x <= 7/10,  |y| <= 1/100,
both signed-z lifts, every 0<h<=1, and every lambda>0.
```

It is explicitly the union of the four independently certified cells
`313/500..627/1000`, `627/1000..63/100`, `63/100..16/25`, and
`16/25..7/10`.  The text states `531/531` exact strict controls on each
cell and the exact left-seam checks.  The latest cell records
`D>=3849/10000`, `det(C)/S=5/72`, `71/71`, and unique weakest control
`C1(0,2,2)=517/1000`.  The paper continues to state that the full compact
ball, the general complex common-metric problem, arbitrary nodes/dimension,
and the fixed-lens optimum remain open.

## Deterministic clean builds

Both builds ran from the candidate root with
`SOURCE_DATE_EPOCH=1787673600` and `TZ=UTC`:

```sh
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The two build exit records are both zero:

- `audits/V18_CANDIDATE_CLEAN_BUILD_1.exit`;
- `audits/V18_CANDIDATE_CLEAN_BUILD_2.exit`.

Both final PDFs have SHA-256
`2f04f9b65c6c31cc9b4f806bc9e264aec4ac951dcc525d2519206ecb3c1a89fc`.
The final PDF is 42 letter-size pages and 609424 bytes.  Its creation and
modification dates are both the fixed 2026-08-26 epoch.  The final
`main.log` and `main.blg` contain no warning, undefined reference/citation,
multiply defined label, overfull/underfull box, fatal error, or emergency
stop.  The retained aggregate latexmk logs contain the ordinary transient
undefined-reference messages from the first TeX pass after each clean; the
last latexmk pass and the final logs are clean.  The exact empty final-log
gate is retained as `audits/V18_CANDIDATE_FINAL_COMPILE_GATE.log`.
The path-dependent/time-dependent latexmk transients `main.fdb_latexmk`,
`main.fls`, and `main.log` are intentionally excluded from the archive so a
fresh clean build does not create false byte drift; the two complete build
logs, exits, empty final-warning gate, and all deterministic products remain
manifest-bound.

All five cited keys are present in `references.bib`; v18 introduces no new
reference.  The frozen bibliography audits therefore remain the applicable
record audit.  The fresh key-closure result is in
`audits/V18_CANDIDATE_CITATION_GATE.log`.

## PDF metadata, text, and fonts

`pdfinfo`, `pdffonts`, and `pdftotext -layout` were run on the final candidate
PDF.  The title and five-author metadata are present; every listed font is
embedded.  The rendered title page displays `Yonghua Xiong*` and the footnote
`* Corresponding Author: Yonghua Xiong.`  The PDF text contains all four
cell endpoints, `531/531`, the limitation language, and no `qqquad`, `TODO`,
or `FIXME`.  The supporting records are
`audits/V18_CANDIDATE_PDFINFO.log`,
`audits/V18_CANDIDATE_PDFFONTS.log`, and
`audits/V18_CANDIDATE_PDF_TEXT_GATE.log`.

## Page-by-page visual QA

The first candidate's Poppler run rendered all 42 pages at 144 dpi and seven
contact sheets covered pages 1--42 without omission.  Every page was
inspected.  Original-resolution inspection was repeated for page 1 (authors
and corresponding-author mark), pages 27--29 (stitched theorem, four-cell
table, and adjacent theorem transition), page 41 (exact table, hash appendix,
references, and affiliations), and page 42 (remaining affiliations).  The
repaired candidate changes packaging documentation and archive membership
only: its twice-clean-built PDF remains byte-identical at SHA-256
`2f04f9b65c6c31cc9b4f806bc9e264aec4ac951dcc525d2519206ecb3c1a89fc`.
Accordingly the complete page-level visual result is inherited without
rerendering; the independent repaired-candidate audit will render afresh.

Result: no crop, overlap, unexpected blank page, table or formula escape,
broken footnote, or unreadable hash line was found.  Page 28's cell and
degree/control tables fit within the text block.  Page 42 is intentionally
sparse because it contains the continuation of the author affiliations, not
an accidental blank.  The original raster dimensions and SHA-256 values for
all 42 pages and seven contact sheets are recorded in
`audits/V18_CANDIDATE_VISUAL_QA_FILES.log`.

## Certificate packaging and fresh direct replay

`certificates/xy_box_post_v17/INDEX.md` lists 32 principal files, eight for
each of the four cells.  A fresh replay matched all 32 path/SHA pairs and
confirmed all 32 files plus the index are package-local; see
`audits/V18_CANDIDATE_INDEX_REPLAY.log`.

The original historical manifests remain present as provenance.  They are
not used to conceal or recreate an omitted machine-path transcript.  In a
fresh isolated extraction, the four native source programs and four native
literal-free independent referees were instead run in normal mode.  All
eight direct mathematical gates passed.  The source gates reconstructed the
fully conjugated Hermitian `Q,Q^2` gate and all 531 exact controls per cell;
the referees independently reconstructed the coefficient/control/seam data
without importing a source coefficient table.  Fresh logs and exit records
are retained as `audits/V18_PORTABLE_DIRECT_SOURCE_*.log/.exit` and
`audits/V18_PORTABLE_DIRECT_REFEREE_*.log/.exit`; all eight exits are zero.

The new parallel layer additionally freezes complete portable source and
referee manifests for all four cells.  Every normal run exits zero; every
mathematical, dependency, optimized-mode, missing-record, and bad-member-hash
attack exits nonzero.  All twelve source/referee/cell manifests replay from
package-relative paths.  The historical principal bytes and the manuscript
PDF are not altered by this additional chain.

A recursive binary-safe scan of the final extracted archive finds zero
machine-specific user-home path matches.  The final release manifest covers
every intended archive member, and the archive contains one safe v18 root,
no absolute or parent-traversal member, no symbolic link, and no environment
cache.

## Portable-chain rebuild gate

After adding the parallel chain, two further clean builds with fixed source
epoch both exited zero.  Both reproduced the frozen 42-page PDF byte-for-byte
at SHA-256
`2f04f9b65c6c31cc9b4f806bc9e264aec4ac951dcc525d2519206ecb3c1a89fc`.
The final `main.log` and `main.blg` contain no undefined reference/citation,
multiply-defined label, overfull/underfull box, package warning, or fatal
error.  The portable top manifest has 24 records and SHA-256
`df89279bc36a5c37e9b3a2ce5b7e5d3bd83c37566fe141e674c5be8de9ce5397`;
its normal verifier exits zero and both injected attacks exit nonzero.

The twelve child source/referee/cell manifests pass at counts
`38/50/16`, `37/56/16`, `41/60/16`, and `45/60/16`.  A binary-safe full-tree
scan after transient cleanup finds no builder-home, workspace-root, or
absolute temporary-directory path.

## Builder conclusion

The deterministic build, final-log, bibliography-key, PDF-text/font,
42-page byte-identical visual inheritance, grouped-index, eight fresh direct
mathematical replays, portability scan, and archive-integrity gates pass with
no remaining builder warning or layout minor.  This is a frozen **repaired
candidate for independent submission audit**, not a formal v18
release and not a claim that any of the explicitly open global problems has
been solved.
