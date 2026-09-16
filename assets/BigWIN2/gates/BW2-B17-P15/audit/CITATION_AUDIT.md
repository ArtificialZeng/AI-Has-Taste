# Citation audit

Audit date: 2026-09-01. Each citation was checked independently against its
primary publisher or official live record.

- `MV2010`: Elsevier DOI `10.1016/j.jmaa.2010.07.030`, the author-hosted
  journal manuscript, and the author's publication list agree on the authors,
  title, journal, volume 372, issue 2, and year 2010. Equation (1) gives
  `1.2748 <= S <= 1.5098`; Section 4 and equation (13) give the uniform-step
  reduction. The incorrect locator “Theorem 1.1” was repaired. Crossref's
  complete electronic page span is 439--447.e2. Confidence: 0.995.
- `ArenaSOTA`: the fixed GitHub commit `ee1495c1babb` contains the
  `first-autocorrelation` data, README, and analysis notebook. The notebook
  recomputes `1.502862858705311`, displayed as `1.50286286`. This is a public
  floating-point repository, not a peer-reviewed or exact certificate.
  Confidence: high.
- `ArenaLive`: the official problem page and public APIs show a mutable
  floating-point leaderboard. The API records `1.5027436492326165` with a
  submission time of 2026-08-14T23:27:35.795Z. Exact integer comparison shows
  that the rational value proved in this manuscript is about
  `1.50274364923263`, approximately `1.37e-14` higher. The introduction now
  states explicitly that no numerical improvement over that API entry is
  claimed. Confidence: high.
- Mechanical audit after correction: cited=3, BibTeX entries=3, missing=0,
  unused=0. None of the live computational records is used as a theorem
  premise.

Verdict: PASS for citation accuracy. Publication priority is limited to exact
certification below the eight-decimal target, not a new live numerical record.
