# Proof audit

Date: 2026-08-29 (Asia/Shanghai)  
Endpoint: `problem/formal_statement.md` (T3)  
Status: **FULL MATHEMATICAL PROOF AND RELEASE AUDIT PASS**

`audit/REFEREE_TROPICAL.md` independently passes exactly the two targeted
fatal lemmas G01 and G04.  It is not a full proof-DAG audit.  Its four minors
have now been incorporated into `paper/main.tex` and
`proof/tropical_route.md`:

1. the maximal-diagonal families now contain the full transient-term and
   forced-common-value inequalities corresponding to referee I.3--I.11;
2. the restriction is stated literally as erasing every letter greater than
   3;
3. the empty witness is peeled off before the finite-entry tropical matrix
   lemma is applied;
4. complete-column centrality is proved directly by RSK as in referee II.1.

G02 is now closed at the targeted-lemma level.  The complete non-circular
human proof in `proof/g02_six_coordinate_product.md` gives the unique feasible
sextuple parametrization, proves the row word directly from the empty tableau,
and inserts its six batches while recording all five minima and six output
coordinates.  `audit/G02_REFEREE.md` independently reconstructed that proof
and returned PASS.  Its expository minors were incorporated.  A separate
stdlib-only literal row-insertion implementation then checked 913,936
exhaustive ordered products and 30,000 fixed-seed boundary products with no
mismatch; `audit/G02_DIAGNOSTIC.md` binds this rerun to the revised proof hash.
These computations are diagnostics, not proof premises.

`audit/FULL_DAG_REFEREE.md` independently reconstructed the entire proof from
the formal endpoint through the published inputs, the interval-LIS cone,
tropical powers, adjacent commutation, all thirteen weak diagonal orders,
faithfulness, tail isolation, G02, both final inclusions, and every empty or
boundary endpoint.  Its frozen-snapshot verdict was PASS with fatal count 0
and major count 0.  The three listed minors and the G02 status inconsistency
were repaired.  The same referee then appended a written post-repair PASS
bound to the new hashes of the formal statement, proof DAG, tropical route,
G02 proof, and manuscript source.  It confirmed that the repairs introduced
no collateral theorem, hypothesis, endpoint, or quantifier change.

This is a full mathematical-proof PASS.  The separate post-DAG release gates
also passed: dated second novelty search, two-reference independent citation
audit, static LaTeX audit, clean converged build, all-page PDF inspection,
independent build from the source ZIP, and fail-closed release-manifest
verification.  The scientifically honest terminal category is therefore
`PROVED`.

No Lean, Coq, Isabelle, or other proof assistant has been used.  Z3 and
bounded RSK computations are discovery/diagnostic tools only and are not
proof premises.
