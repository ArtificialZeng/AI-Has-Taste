# Gap ledger

| ID | Proposition/location | Missing step | Severity | Test/repair | Status |
|---|---|---|---|---|---|
| G01 | Full conjecture for all finite trees | No global argument currently bridges rooted-tree products to coefficient unimodality. | fatal | Develop closure-preserving invariant or find exact counterexample. | open |
| G02 | New finite computational lower bound | None: all 120 chunks total exactly A000055(31), both aggregators agree, and the isolated rebuild audit passed. | major | Evidence: `results/order31_aggregate.json`, `results/order31_independent_aggregate.json`, `results/order31_rebuild_audit.txt`. | resolved |
| G03 | Any novelty claim | No order-31 or stronger result was located in the post-result search; this remains a cutoff-bounded negative literature conclusion. | major | Evidence: `literature/search_log.md`, NOVELTY_LOCK pass 3, and claims C11--C13. | resolved |
| G04 | Triple-valley equivalence | None: independently reconstructed from a global maximum without positivity. | local | Evidence: `notes/referee_report.md`, Section 2, plus 21,844 exact sequence tests. | resolved |
| G05 | Common-mode rooted induction | False: root states need not share a weak mode. | fatal-to-route | Exact witness: \(K_{1,3}\) rooted at a leaf, with A modes {1}, B modes {2}. | refuted |
| G06 | Naive rooted ratio-minor induction | False: adjacent cross minors can change sign and B has a forced zero denominator. | fatal-to-route | Exact witness: \(K_{1,2}\) rooted at its centre, minors \((1,-1)\). | refuted |
| G07 | Gamma-balanced gluing as a new infinite subclass | The local proof is sound, but double-private-leaf gamma positivity is already in Hibi–Kara–Vien (2026), Remark 1.5, and the broader bridge route overlaps the 2026 bridge framework. | major | Retain only as background/invariant; do not claim novelty. | novelty-refuted |
| G08 | Submission release | None: the two-pass citation audit, isolated LaTeX build, five-page visual PDF audit, exact 552-file source manifest, and fresh-root release reconstruction all passed. | major | Evidence: `audit/CITATION_AUDIT.md`, `audit/PDF_AUDIT.md`, `audit/RELEASE_AUDIT.md`. | resolved |
