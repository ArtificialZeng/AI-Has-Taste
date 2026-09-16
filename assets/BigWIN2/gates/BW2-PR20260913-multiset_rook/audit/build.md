# Build review

Release job: `primary-20260913-multiset-rook-release-f279096f79ec`. Review date: 2026-09-13 UTC. Manuscript digest: `74fbbb0c497af6bd1255b7f61e16c5253f52d7ae3d006fdd771b7086b395a280`. PDF digest: `217ceb7dd07098a9789777a0485f3c16c7107bfa23d6399cfdac0351f6b8dee1`.

Verdict: **accept**. A final clean build was executed after all source edits, using `latexmk -C -outdir=build main.tex`, followed by `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex` from `manuscript`. Both commands exited zero. The full transcript is `release-clean-build-transcript.log`; `release-build.log` is byte-identical to the final engine log.

The final engine and BibTeX logs contain no warnings, undefined citations/references, missing entries, repeated entries, overfull/underfull boxes, or fatal/error diagnostics. The first clean pass generates normal auxiliary state; only the converged final log is audited. `bib-key-check.txt` reports five matching source, bibliography and auxiliary keys.

The PDF has five unencrypted letter-size pages and nonempty text extraction. Title and author metadata match the article. All 21 listed font instances are embedded, subsetted and have Unicode mappings. FLS dependency review is recorded separately. The standalone published code, all 30 bases, 60 ascent entries, 60 legal words and exact signs were independently replayed in `release-verify.py`. All 16 protected inputs, including the 12 frozen snapshot files, remain unchanged.
