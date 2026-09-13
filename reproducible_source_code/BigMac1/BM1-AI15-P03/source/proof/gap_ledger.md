# Gap ledger

| ID | Proposition/location | Missing step | Severity | Test/repair | Status |
|---|---|---|---|---|---|
| G1 | Formal statement / graph definition | Source paper excludes its generic boundary \(k=n/2\), but OEIS separately defines and computes \(n=6\) | major | OEIS executable definition and endpoint example checked; discrepancy recorded in formal statement | resolved |
| G2 | L2 / infinite construction | Needed residue-complete family | fatal | explicit colour blocks \(A=01,B=21202\), plus an independent sign-word construction | resolved |
| G3 | L3 / four nonexistence cases | Computed zeros were not a proof certificate | fatal | exact run bound and sliding half-window argument; two exhaustive sign-word verifiers | resolved |
| G4 | Gate 1 novelty | Needed a current-dated secondary search pass after the theorem statement and blocks were fixed | major | second search pass S08 found no prior all-order proof in the recorded scope | resolved |
| G5 | Gate 5 independent referee | Candidate proof required definition-first reconstruction and adversarial boundary checks | major | independent audit, remediation, and recheck; final verdict PASS with no unresolved items | resolved |
| G6 | Gate 6 release audit | Citation, LaTeX, clean-build, and page audit were required | major | citation audit PASS; clean five-page build PASS; every rendered page inspected; submission audit PASS | resolved |
| G7 | `verification/primary_verify.py` fail-closed behavior | Correctness-critical language `assert` statements disappeared under `python -O`, allowing a bad extension block and missing key to print PASS | fatal | replaced every correctness assertion with explicit `require`/`fail`, added strict schema checks, and passed a 12-cell normal/`-O`/`-O -I` adversarial matrix | resolved |
| G8 | even transfer-matrix equivalence | Ordinary closure forgets the half-cycle track swap | fatal | derived the 54-state paired-window automaton with twisted closure (s_m=\tau(s_0)); independent referee proved the colouring/walk bijection in both directions | resolved |
| G9 | automaton eventual positivity | A long finite prefix or modular recurrence would not prove positivity | major | exact integer certificate proves (O^{10}>0) and (E^{13}>0), with no zero columns; cone propagation gives all later powers | resolved |
| G10 | static-whitelist release freeze | The prior ZIP included two build logs, while the manifest also signed ten rendered temporary pages | major | rebuilt from explicit source/manifest whitelists; zero junk entries; four verifiers in normal/optimized modes, fail-closed harness, LaTeX audit, ZIP integrity, and two manifest verifiers pass from a clean extraction | resolved |

No open mathematical or release gap remains.  The literature conclusion is
deliberately bounded to the sources and searches recorded in
`literature/search_log.md`; it is not a claim of absolute global priority.
