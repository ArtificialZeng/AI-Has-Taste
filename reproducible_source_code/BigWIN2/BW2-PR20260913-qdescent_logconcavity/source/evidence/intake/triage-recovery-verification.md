# Recovery verification and admission

Job: primary-20260913-qdescent-logconcavity-triage-88d4196c29cf.
Date: 2026-09-13. Decision: advance; candidate kind none; original unresolved.

Enumerated and read the sole current literature/*handoff*.md,
literature/operational-recovery-handoff.md. Its mathematical lead was checked
against original evidence; its account of the earlier timeout is supplied
operational history, not a mathematical conclusion or an imported decision.
Original prior problem/checkpoint snapshots are preserved as
triage-178cb0fc6742-problem.md and triage-178cb0fc6742-checkpoint.md in this
directory. The previous scripts, results and frozen Target K remain unchanged.

## Inspected primary evidence

Read cached Sections 1.1, 1.2 and all of Section 2 of
[Gaetz–Gao v2](https://arxiv.org/html/1912.04933v2), including Theorems 5/6,
Conjecture 7, the last-value recurrence and the following Remark. Local input:
evidence/external/gaetz-gao-1912.04933v2.html. Its SHA256 matches source.md's
frozen reference. Opened the live version page on 2026-09-13; its version
record identifies v2 as 8 January 2020, distinct from its dynamic rendered
Date. The literal strict-pair definition and separately conventional diagonal
reading have been retained. Theorem 2 in Section 1.1 attributes the q=1
result to Bencs. The source's arbitrary-b counterexample is prior work and is
not a descent-derived counterexample. No broad source-discovery repeat was
needed for this short recovery. Earlier same-date literature searches remain
qualified by their recorded access limits, particularly Liu–Xiao full text.

## Algebraic verification

For each size-m prefix permutation with last standardized value r, adjoining
last value h and unstandardizing creates m+1-h inversions. The last position
is a descent exactly when r>=h. Hence

    b_h=q^(m+1-h) sum_{r=h}^m x_r.

Substitution into the inspected source Remark yields

    K(m;k,r)=sum_{h=1}^{min(r,m-k+1)}
                  q^(k(k-1)+m+1-h) [m-h choose k-1]_q.

The identity G(t+1,k)-G(t,k)=q^(t+1-k)G(t,k-1) telescopes this sum to
q^(k^2)(G(m,k)-G(m-r,k)); the exponent and both endpoints agree.
The h=1 term is nonzero for every 1<=k,r<=m. A permutation realizing any
prescribed ascent/descent pattern T exists by labeling a linear extension
of its oriented path. Consequently some x_r is nonzero, and every a_k is
nonzero. This settles the support requirement, not the determinant target.

Expansion in independent formal variables x_r gives exactly Target K's
single and mixed coefficients, with no missing factor of two when r=s.
Thus Target K is a sound sufficient strengthening. Its failure need not be
realizable by a descent pattern; the original has not been disproved.

## Small independent calculation

Command: python3 evidence/intake/triage-recovery-check.py.
The new script uses only Python's standard library, independent sparse
integer polynomial operations and subset enumeration for Gaussians. It does
not import the earlier calibration arithmetic. It passed all 17 direct
definition cases for max S<=3, all 30 positive-suffix identities for m<=4,
and all 81 strict plus 65 diagonal Target K expressions for m<=4.
Results and SHA256 bindings: evidence/intake/triage-recovery-check.json.
These are finite recomputations of already tested ranges, not expanded
coverage, a proof, or a fresh referee pass. The earlier checker's imported
arithmetic dependency is evidence/intake/qdescent-calibration.py; its hash
and all handoff hashes were verified. Its larger observations were read but
not rerun in recovery.

## Admission and next test

Advance is warranted by the exact reduction, a uniform sufficient lemma,
existing exact falsification code and a concrete proof route. No target has
been accepted mathematically. The next bounded research test is to prove or
falsify the frozen mixed Target K inequalities by a weight-preserving
injection or positive q-Pascal decomposition, treating strict and diagonal
cases separately. A negative kernel coefficient invalidates only this
sufficient route until actual descent-vector realizability is established.
