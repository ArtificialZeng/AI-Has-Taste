# Gap ledger

| ID | Proposition/location | Missing step | Severity | Test/repair | Status |
|---|---|---|---|---|---|
| G01 | Gate 1 source boundary | Could a later proof already exist? | major | Primary-source, citation-index, exact-formula, and code searches; repeat after result fixed. | closed; two bounded passes logged |
| G02 | Rational differential system | State derivative and row-elimination identities are not yet independently certified. | fatal | Serialize exact rational data; reconstruct with a no-import verifier. | closed by certificate verifier |
| G03 | Order-3 to order-5 operator | Ore multiplication is noncommutative and product-rule terms could be missed. | fatal | Independent operator-composition implementation and direct state-system evaluation. | closed by verifier and direct differentiation |
| G04 | ODE to recurrence | Factorial and index shifts could be wrong. | fatal | Derive a contribution table using falling factorials and compare symbolic polynomials. | closed by proof table and verifier |
| G05 | Initial/boundary values | OEIS begins at 1 but (n=4) uses (a_0). | major | Compute (F(0)), exact Taylor coefficients, and state both indexing conventions. | closed; a0=0 certified |
| G06 | Combinatorial baseline | EGF coefficients should match direct small enumeration, not only the paper table. | local | Exhaustively enumerate perfect matchings for small (n) with an independent definition checker. | closed for n=1..7 |
| G07 | Release audit | Citation pass 2, clean build, LaTeX audit, manifest, and PDF inspection not yet run. | major | Complete Gate 5--6 release checklist. | closed; final manifest verification recorded |
