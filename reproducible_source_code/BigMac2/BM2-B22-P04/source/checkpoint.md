# Checkpoint

Release job `bigMac-00022-p04-release-7b9c803e490d` completed fresh citation,
clean-build, and rendered-page audits for the accepted `result-note`.  The
original cograph torsion-existence problem remains unresolved; the accepted
contribution proves the all-finite-graph singleton-anchor homology formula and
the necessary conditions `|K|>=2`, `n>=|K|+2` for a torsion witness.

During visual/text comparison, four stray literal commas in exponents in
`manuscript/main.tex` were found and removed.  This was a publication-only
typographical repair: neither the frozen mathematical statement nor its evidence
changed.  A clean `latexmk -gg` rebuild succeeded, the manuscript was refrozen,
and the current bindings are:

```text
evidence snapshot  2023a3cd86fb4345f524bacaa1ef9971821af45d2177e3e94da7ab0ef3501440
manuscript digest  f8f9f022aa6c2f81823d6da598a8908957bce2e572ec0477bbe5e47cca7a4294
PDF digest         1f489da613d6e5feff47269d96da58cecb2fc62390b87efcc9f1792493fec928
build-log digest   f02891e55978295f8dddf8c0067724188925a21bbab1d411c15fcb36a92887e5
```

The requested citation-check skill was applied as an advisory two-pass review.
Both bibliography records and their nearby claims were verified from primary
sources: Kozlov's publisher/arXiv record and Mamun--Nalikka--Ramos arXiv v1.
All keys resolve, and `publication.json` lists the complete authored dependency
scope.  `literature/user_bibliography_check.md` is absent from this project, so
there was no user-designated workbook record to inspect; no unrelated citation
was inserted.  This is recorded in `audit/citations.md` and does not leave an
unverified citation.

The final compiler and BibTeX logs contain no unresolved citations/references,
fatal errors, layout warnings, or BibTeX warnings.  All three PDF pages were
rendered at 160 dpi and inspected; equations, references, fonts, and margins are
legible with no clipping or overlap.  Fresh audit records are in
`audit/citations.*`, `audit/build.*`, and `audit/visual.*`.

`release_gate.py check` succeeds for the current state.  The immutable
`source.md` remains SHA-256
`301b65eb092ad49afb7e0dd80a9c0a82344af7288a3c86a41f2aedf048159a2f`.

Next test: the supervisor should run `release_gate.py publish` on this project
and verify that `release/manifest.json` and `release/main.pdf` match the checked
digests.
