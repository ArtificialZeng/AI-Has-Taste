# Gap ledger

| ID | Proposition/location | Missing step | Severity | Test/repair | Status |
|---|---|---|---|---|---|
| G01 | Component identity (*) | Possible transpose error between \(a_{ij}\) and the direct-sum supports \((j,i)\). | fatal | Derive each of the three commutators separately; check by a second pairwise-expansion program. | closed: `proof/main_proof.md`; `logs/verify_symbolic_expansion.log` |
| G02 | Repeated indices in (*) | Embeddings with \(i=j\), \(j=k\), or \(i=k\) might have been treated as disjoint components. | major | State the maps into the three separate tensor factors and avoid any independence argument. | closed: final paragraph of proof |
| G03 | Match to transitive CYBE | The middle color must be exactly the entry constrained by transitivity. | fatal | Apply the array axiom to the ordered triple \((k,i,j)\), giving \(a_{kj}\in\{a_{ki},a_{ij}\}\). | closed: D4 and 571,625 exact checks at n=5 |
| G04 | Completeness of finite baseline | A generated list may omit color-equality patterns. | major for finite certificate; not used by universal proof | Independently reconstruct Proposition 3.14's classification and compare sets. | closed: `logs/verify_certificate.log` |
| G05 | Degenerate cases | Zero family, constant arrays, repeated colors, infinite \(C\), and \(C=\varnothing\). | local | State them in the formal endpoint; proof uses no division or genericity. | closed: `problem/formal_statement.md` |
| G06 | Novelty | A later public proof may exist outside searched databases. | expository/publication | Repeat exact-title, citing-work, author-page, DOI, and code searches before release; bound novelty wording. | closed as a search gate: second pass S14--S20 complete; manuscript makes no universal priority claim |
