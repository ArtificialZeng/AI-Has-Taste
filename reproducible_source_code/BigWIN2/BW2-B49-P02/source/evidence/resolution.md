# Exact resolution for two-color Permutation Wordle at n=3

## Theorem submitted for review

In the frozen 48-secret, 48-guess game of `source.md` and `problem.md`, the
maximum numbers of secrets that a deterministic adaptive strategy can solve
within horizons \(r=1,\ldots,6\) are
\[
  (N_1,N_2,N_3,N_4,N_5,N_6)=(1,8,24,40,47,48).
\]
Consequently \(N_r=48\) for every \(r\geq6\).  The intended multicolor
CircularShift algorithm of Kutin--Smithline attains all these values
simultaneously, with exact-round counts
\((1,7,16,16,7,1)\).

Here “intended” is material: it is the circuit-completion algorithm specified
by the prose before Definition 4.3, Figure 6, and the proof of Lemma 4.4 in
arXiv:2408.00903v3.  The displayed color-update cases in Definition 4.3
conflict with those three parts of the primary source.  The discrepancy and
the exact operational reading are documented in
`evidence/circular-shift-interpretation.md`; no literal-formula equivalence is
claimed.

## Finite Bellman proof

For a viable-secret set \(A\), a legal guess \(g\), and feedback
\(u\subseteq[3]\), let \(A_{g,u}\) be the corresponding feedback cell.  The
induction in `problem.md` gives the exact recurrence
\[
 V_0(A)=0,\qquad
 V_r(A)=\max_{g\in\Omega}\left(
 |A_{g,[3]}|+\sum_{u\subsetneq[3]}V_{r-1}(A_{g,u})
 \right).
\]
It is exact because the nonterminal feedback cells are disjoint and, after
observing the feedback, their continuation strategies may be chosen
independently.  Conversely every deterministic adaptive strategy chooses one
of the 48 guesses at the root and restricts to a strategy on each such cell,
so the same expression is an upper bound.  Induction on \(r\) proves equality.
Therefore \(N_r=V_r(\Omega)\).

`evidence/bellman_exact.py` evaluates this recurrence with exact 48-bit masks.
It evaluates all 48 guesses at every reached nonempty state and uses no
symmetry quotient, dominance rule, pruning cutoff, or floating point.  Its
certificate serializes all 48 canonical items, all 2,304 feedback entries,
and 98,898 state rows.  The counts of rows at horizons 1 through 6 are
\((48645,37125,10743,2143,241,1)\), and all 4,747,104 state-action scores are
represented by certificate dependencies.

`evidence/verify_bellman_certificate.py` does not import the solver.  It
reconstructs the universe and feedback table, verifies every serialized
response, checks every dependency, and recomputes all 48 action scores at all
98,898 state rows.  Its report
`evidence/bellman-output/verification.json` records status `verified`, no
missing dependencies, and root values
\((1,8,24,40,47,48)\).  Because the verifier checks the maximum over every
legal action rather than only the retained action, these rows certify both
attainment and the upper bounds.

## CircularShift attainment

Under the operational circuit rule fixed above,
`evidence/circular_shift_sim.py` first reproduces the six-row primary example
in Figure 6 and then simulates every one of the 48 canonical two-color
secrets.  Every submitted guess remains in the legal 48-element alphabet.
All 48 completion times agree with Lemma 4.4:
\[
 T(\sigma,\kappa)=1+\operatorname{exc}(\sigma)+\sum_{i=1}^3\kappa(i).
\]
Thus their generating polynomial is
\[
 (1+4z+z^2)(1+z)^3
 =1+7z+16z^2+16z^3+7z^4+z^5,
\]
which gives exact-round counts \((1,7,16,16,7,1)\) and cumulative counts
\((1,8,24,40,47,48)\).

`evidence/verify_circular_shift_transcripts.py` independently parses all
serialized rows without importing the simulator.  It recomputes 168 feedback
sets and 120 successor transitions, verifies legality and the formula secret
by secret, and reproduces both distributions in
`evidence/circular-shift-output/verification.json`.

Comparing the two independently reconstructed cumulative sequences proves
simultaneous strong optimality at every horizon through saturation, and hence
at every integer horizon \(r\geq1\).

## Scope and literature limit

This resolves only \((n,s)=(3,2)\) for the exact feedback and legal-guess model
frozen in `source.md`.  It makes no assertion for larger \(n\), more colors,
or repeated-rank guesses.  The copied primary sources record the general
multicolor claim as conjectural/open, but the 2026 paper also cites multicolor
work “in preparation.”  Hence this dossier establishes the finite theorem,
not priority over inaccessible work or the general conjecture.
