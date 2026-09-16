# Citation audit

Search date: 2026-08-29.

- PASS: original source metadata and v1 status checked on arXiv and DataCite.
- PASS: exact conjecture, definition, run theorem, and reported finite range
  checked in the source TeX rather than a summary.
- PASS: later author paper `2604.10822v4` checked at source level.
- PASS WITH BOUNDED WORDING: no prior resolution located in the recorded
  searches; OpenAlex and DataCite report zero citations at query time.
- LIMITATION: Semantic Scholar API returned HTTP 429, and Crossref title
  search is not exhaustive. The manuscript must say "not found in the
  recorded searches through 2026-08-29", never "certainly first".
- PASS: the Golomb run endpoint fact is derived directly from the defining
  multiplicity property, so no unverified external theorem is needed.
- PASS: publication-stage arXiv/web recheck on 2026-08-29 again found no
  explicit prior proof; the only relevant primary records were the original
  conjecture paper and the separate Beatty-solution paper.
- PASS: journal-neutral `amsplain` output visibly includes
  `arXiv:2604.02404v1` and `arXiv:2604.10822v4`.
