# Gap ledger

| ID | Proposition/location | Missing step | Severity | Test/repair | Status |
|---|---|---|---|---|---|
| G01 | `main_proof.md`, exterior triple identity | Must exclude all extensions inside \(X\). | fatal if absent | Such a four-set is disjoint from the fixed \(E\in\mathcal F\). | closed |
| G02 | `main_proof.md`, injectivity | Multiset repetition might survive the triple condition. | fatal if false | Complement-pair multiplicity proof; independently checked by \(31^4\) forcing-set enumeration. | closed |
| G03 | `main_proof.md`, mixed triple \(Q_a\) | Need at most one \(X\)-extension, including the cases \(x_0=x_a\) or \(x_j=x_a\). | fatal if false | Injectivity and the unused definition exclude both equalities; intersection with (2) forces the fourth point to be \(x_a\). | closed |
| G04 | `main_proof.md`, final contradiction | The triple \(S\) must remain fixed while \(a\) varies. | fatal if false | Fix \(j\) first; \(S=X\setminus\{x_0,x_j\}\) is independent of \(a\). | closed |
| G05 | Full parameter family | Dependence on Huang--Zhang for \(n\ge11\) could hide a citation gap. | major | The new \(n\ge10\) argument is self-contained; external theorem removed from the proof DAG. | closed |
| G06 | Equality | Full classification of all equality families is not supplied. | expository/limitation | State only sharpness via full stars and explicitly disclaim uniqueness/classification. | closed with stated limitation |
| G07 | Computational endpoint claim | Solver self-check is not an independent certificate. | fatal if used alone | Freshly compiled pinned external `lrat-check` accepts both LRATs; the wrapper snapshots all audited inputs and rejects eight bad traces. | closed |
