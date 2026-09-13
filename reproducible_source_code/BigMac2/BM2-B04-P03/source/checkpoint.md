# Checkpoint

- Job: `bigMac-00004-p03-release-2a3eeff553ed`; phase: release audit.
- Candidate: accepted full-scope `resolution-paper`; original status `proved`.
  Mathematical snapshot digest:
  `d1cd38b08aad32076bab5102c4b96643aca988b3dda4cacf13323d7b7e6dff25`.
- `source.md` remains byte-identical, SHA-256
  `fbffc6b3d9b3b2db7bac8945473758846ca4cf5d4db8d9fb17073f50d47cfe43`.
- Release review corrected two publication-only defects: a missing backslash in
  one displayed `\leq`, and Cordella's bibliography primary class (`math.NT`,
  verified from arXiv v1). Explicit PDF title/author metadata was added. No
  mathematical statement or accepted proof scope changed.
- Final manuscript snapshot digest:
  `0690123fb53072c8473609a5d0bee51a86df7d13487976a7536b07985324f011`;
  PDF digest:
  `5aead51bf0b591101dcdfb3cdda94bbb019a25707e7a4af093ff766de5f420e4`.
- Citation-check skill used in two passes. All six extracted claims passed.
  Cordella v1 supports Lemma 2.2, Theorem 6.1, the speed-110 search, both Table 2
  examples, and the base value. Preprints.org verifies the Zeng v1 metadata and
  the narrowly cited exact phase-arc methodology. Direct DOI safe-open was
  unavailable, but the authoritative host record supplied the needed evidence.
- A clean `latexmk` build passed. Final log
  `manuscript/main.log` has SHA-256
  `0c808ee28cf88f794c3f70acc797d1d2c6426463274da5575d88c5e02515e7be`
  and no persistent warnings, undefined citations/references, or box overflows.
- Exact `Fraction` verification passed for all stated finite ranges. Every page
  of the five-page final PDF was rendered at 170 dpi and individually inspected;
  no clipping, overlap, malformed symbol, or illegibility remains.
- Fresh digest-bound reports and records are in `audit/citations.*`,
  `audit/build.*`, and `audit/visual.*`.
- Final `release_gate.py check` passed with `ok=true`, five pages, and the exact
  snapshot/manuscript/PDF/build-log bindings recorded above.

Obstacles: none remaining. The DOI resolver's optional direct endpoint was
inaccessible, but authoritative source verification was complete through the
Preprints.org record.

Next test: the supervisor runs `release_gate.py publish` and verifies the active
`release/manifest.json` and `release/main.pdf` digests match this checked state.
