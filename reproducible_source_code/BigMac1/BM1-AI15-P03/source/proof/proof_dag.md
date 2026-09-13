# Proof dependency graph

- T0 (target zero-set theorem)
  - L1: exact difference-word characterization for proper colourings of the
    offset-\(1,3\) cycle, including the even diameter condition.
  - L2: explicit admissible difference words for every nonexceptional order.
  - L3: exact nonexistence for \(n=7,8,12,16\), preferably a short structural
    argument and independently an exhaustive finite certificate.
  - L4: endpoint and simple-graph collision audit for \(n=6\).
  - A1: independent verifier reconstructs L2/L3 from serialized exact input.
  - N1: novelty/source audit confirms the graph definition and prior frontier.
  - R2: independent seam-correct transfer automata are bijective with graph
    colourings; exact positive powers imply eventual positivity.

Completion evidence:

- L1: `proof/builder_notes.md`, Section 1 (independently rederived in
  `proof/main_proof.md`, Section 1).
- L2: `proof/builder_notes.md`, Section 2, with exact colour blocks
  serialized in `certificates/builder_construction_spec.json`; an independent
  sign-word construction appears in `proof/main_proof.md`, Sections 2--3.
- L3: `proof/builder_notes.md`, Section 3, plus exhaustive diagnostics in two
  separately written verifiers.
- L4: the alternating word \((01)^3\) directly covers \(n=6\).
- A1: `certificates/verify_builder_construction.py`,
  `verification/primary_verify.py`, and the independently written
  `verifier/verify_zero_set.py` all report PASS.  The definition-first
  referee report `audit/PROOF_AUDIT.md` ends in a clean remediation PASS
  with no unresolved item.
- N1: the pre-result lock and the post-result search pass are recorded in
  `literature/claim_ledger.md` and `literature/search_log.md`; no prior
  all-order proof was found in that explicitly bounded scope.
- R2: `proof/transfer_automaton.md` proves
  \(a(n)=\operatorname{tr}(O^n)\) for odd orders and
  \(a(2m)=\operatorname{tr}(E^mP)\) for even orders.  The exact certificate
  reconstructs 12/54 states, proves \(O^{10}>0\) and \(E^{13}>0\), and closes
  \(6\le n\le25\) by an independent direct-graph recursion.  The
  definition-first report `audit/AUTOMATON_EQUIVALENCE_AUDIT.md` independently
  proves both implications and identifies the ordinary-trace seam failure.

All dependencies of T0 are discharged.  The exact theorem is therefore
proved without reliance on the finite diagnostics.  Route R2 is an additional
exact proof route, while `paper/main.tex` deliberately keeps only the shorter
colour-block proof as its main argument.
