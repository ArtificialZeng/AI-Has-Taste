# Gap ledger

| ID | Proposition/location | Missing step | Severity | Test/repair | Status |
|---|---|---|---|---|---|
| G01 | Matrix-specific theorem | Could a factor have rank below two despite the row relations? | local | Exhibit a nonzero \(2\times2\) minor in each factor and independently enumerate minors. | resolved by `certificates/builder_verify_counterexample.py` |
| G02 | Three-parameter family | Formulas divide by \(x,y,z,x-y,x-z,y-z\). | local | State pairwise-distinct nonzero hypotheses and verify every denominator. | resolved in `proof/exact_disproof.md` |
| G03 | Source identification | The displayed matrix might have been mistranscribed from the paper. | fatal | Compare entrywise with arXiv v1 Example 5. | resolved; exact match, source PDF hash in `literature/search_log.md` |
| G04 | Novelty statement | Database non-detection cannot prove priority. | expository | Use explicitly bounded “not found in audited searches” language. | resolved by `literature/NOVELTY_LOCK.md` |
| G05 | Broader universal question | The witness does not decide statement \((U)\). | out-of-scope limitation | Separate \((C_M)\) and \((U)\) in every theorem, abstract, and final status. | monitored |
| G06 | Rivin Theorem 6 attribution | The printed sign-enumeration proof does not on its face explain zero-position assignments and arbitrary integer entries. | major for that borrowed theorem; irrelevant to T1 | Do not rely on Theorem 6; attribute it only as an author claim unless independently reproduced. | quarantined from proof |
| G07 | Release portability | The first source ZIP recursively included `certificates/__pycache__/builder_verify_counterexample.cpython-313.pyc`. | major for release; irrelevant to theorem | Remove workspace cache, rebuild from `release/SOURCE_FILELIST.txt`, scan ZIP entries, then verify certificates and LaTeX from a clean extraction. | resolved by `audit/RELEASE_PORTABILITY_AUDIT.md` and clean-extraction logs |
