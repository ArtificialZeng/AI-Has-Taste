# Gap ledger

| ID | Proposition/location | Missing step | Severity | Test/repair | Status |
|---|---|---|---|---|---|
| G01 | General Conjecture 7.6 / proposed local cover lemma | No general K-jdt or insertion construction is known that fills a prescribed addable interior box while preserving the class. | fatal for a general proof; irrelevant to the finite n=8 theorem | Derive from a common K-jdt ancestor or seek an exact n=9 refutation. | open |
| G02 | Novelty claim for a publishable finite result | Gate 1 is necessarily bounded; two current search passes and a line-by-line citation audit are required. | major for manuscript release; irrelevant to certificate validity | Preserve bounded wording in all release artifacts. | resolved by `literature/search_log.md` and `audit/CITATION_AUDIT.md` |
| G03 | Finite proof exposition | The human-readable dependency proof and endpoint limitations must agree with the verifier. | local | Reaudit after any theorem or verifier change. | resolved by `proof/finite_result.md` and `audit/PROOF_AUDIT.md` |
| G04 | Discovery independence | A shared encoding or imported state file could make two computations repeat one bug. | fatal | Independent verifier uses shape-first enumeration, 80-bit cell encoding, explicit grids, and bitset closure; it imports no discovery output. | resolved by `src/verifier.cpp` and clean run |
| G05 | Malformed-certificate acceptance | Duplicate keys, extra trusted fields, type confusion, missing fields, or changed counts might bypass verification. | fatal | Strict schema/type validation plus six rejection/acceptance tests. | resolved by `tests/test_fail_closed.py` |
