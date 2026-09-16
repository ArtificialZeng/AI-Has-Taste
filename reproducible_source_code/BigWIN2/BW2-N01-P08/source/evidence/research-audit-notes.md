# Researcher checks and limits

Job: newwin-00001-p08-research-23519ac79811. Date: 2026-09-12.
This file records owner-side checks, not an independent mathematical audit.

The initial proof/disproof split was between an all-parameter first-return
derivation and exact enumeration capable of refuting its coefficients.
The derivation survived the boundary audit. The new script uses a separate
run-block representation, and imports no project counting implementation.

Running `python3 evidence/check-research.py` succeeded and created
evidence/research-check.json. It verifies 66 polynomials, all k=1,...,n,
at (m,n)=(2,9),(2,14),(3,10),(4,10),(5,8),(7,7),(17,5),(100,3).
Every one of these pairs lies outside the inherited coefficient table.
It compares exact counts with the formula, verifies the total and fixed-peak
counts, proves by rational Sturm arithmetic that W/t has degree-many
negative roots, and checks squarefreeness. It additionally verifies the
Jacobi expression against a Rodrigues derivative and the rational change
of variable after clearing denominators, and checks the ordinary scalar.

The independent whole-word enumeration checks every admissible word at
(m,n)=(2,5),(2,6),(3,5),(5,4): respectively 273,1428,969,506 words,
for a total of 3176. Their last-departure components are valid excursions,
the reconstruction matches each word, and the boundary statistics agree.
The three cases (extra NE,extra NNE) have counts (0,0):1308,
(1,0):920, and (1,1):948. The word-generated coefficients also agree.
There are no floating-point or random tests in this evidence.

These ranges were selected after the triage formula was fixed, but the
tests were designed and executed by this same research job. They are
additional exact corroboration, not a fresh model review or a proof of an
infinite assertion. The complete general argument is research-proof.md.

Boundary analysis includes k=1 (W=t), n=1, the minimal m=2, k=n, the
simple forced zero at t=0, and the nonroot t=1 in the Jacobi substitution.
At m=2,k=n, the expression reduces to the classical Narayana polynomial;
the Jacobi parameter beta=mn-2k+1 attains its minimum 1. All parameters
used by the Rodrigues argument remain in its positive-weight range.

Implementation issue, resolved: the first new script run stopped because
SymPy distinguishes Poly(1,domain=ZZ) from Poly(1,domain=QQ) in equality
comparisons. A diagnostic at k=1,2,3 showed zero polynomial differences.
The final script compares all symbolic polynomial identities over QQ;
its successful output above was generated only after that correction.
This was an exact-domain comparison error, not a mathematical counterexample.

The m=1 substitution is explicitly outside the claimed generating-function
scope: component starts can then be NE and create crossing NNE factors.
No obstruction to all proofs, and no disproof of the frozen problem, is
inferred from this limitation. No unresolved mathematical gap is known to
the researcher; independent scrutiny and contribution assessment remain.
