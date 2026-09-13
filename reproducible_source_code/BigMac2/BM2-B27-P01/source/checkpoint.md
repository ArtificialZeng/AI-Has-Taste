# Checkpoint

- Phase/job: packaging-only writing recovery,
  `bigMac-00027-p01-write-8ff6977c206a` (2026-09-09).
- Mathematical gate: `release_gate.py check-math` passed for accepted snapshot
  `59e03e68ab8779d31d40334c841de1fae8b4fd0f247cdcff6f179d4f3391dfc4`.
- Accepted scope: a `resolution-paper` proving entropy concavity on `[0,1]`
  for every positive-integer pair `(u,v)` in the frozen three-bit problem.
  No result for four or more bits and no priority claim is being added.
- Decisive evidence: `audit/math.md` accepts the exhaustive five-profile
  collision classification and the uniform strict interior second-derivative
  argument in `evidence/proof.md`.
- Source integrity: `source.md` remains immutable with SHA-256
  `0af528efdf37ddabccc405621c5e04c5afca4ee0c7cd2939aaf2dd00de9133ab`.
- Manuscript: `manuscript/main.tex` and `manuscript/references.bib` form a
  concise self-contained three-page article; `manuscript/main.pdf` is the clean
  compiled draft. `publication.json` records all TeX/BibTeX inputs and the
  reproducible `latexmk` build command.
- Build/visual evidence: final `latexmk` build exited 0 with no undefined
  references, overfull/underfull boxes, or package warnings. `pdfinfo` reports
  three letter-size pages with title/author metadata; extracted text was
  complete, and all three rendered pages were visually inspected with no
  clipping, overlap, or malformed formula/table.
- Bibliography: the requested project-local check was absent at intake. The
  user-designated workbook was inspected read-only and recorded in
  `literature/user_bibliography_check.md`; rows 21 and 40 are cited only for
  narrow methodological comparisons. No external metadata refresh was
  attempted. The directly relevant Neunh\u00e4userer preprint was checked against
  its local PDF, including Conjecture 3.1 and Proposition 3.1.
- Reproducibility: both accepted exact programs were rerun with the required
  interpreter; all symbolic identities vanished exactly and the partition
  audit again matched representatives plus all 10,000 pairs in
  `1<=u,v<=100`. The manuscript labels this finite work corroboration only.
- Recovery verification: the recorded source, accepted-snapshot, manuscript,
  and PDF digests all matched. `release_gate.py check-math` passed, and
  `freeze-manuscript` passed idempotently with `changed=false`.
- Freeze: manuscript digest is
  `875b64e5a9863dc34e0013cbeeb8d47b2beaec98d1f0f3587362c260d0448dda`;
  PDF digest is
  `df103e23862493e261d1af3536a6b5fc0ae662b8337a248ec2dff452a7d35ed5`.
- Obstacles: none. Citation refresh limitation is disclosed and does not affect
  the accepted mathematics or clean local PDF.

Next test: run the separate fresh citation, clean-build, and visual release
audits against `audit/manuscript-snapshot.json` without modifying the frozen
manuscript or PDF.
