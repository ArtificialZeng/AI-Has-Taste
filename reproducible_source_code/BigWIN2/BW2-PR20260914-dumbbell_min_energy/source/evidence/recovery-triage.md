# Recovery triage verification

Job: `primary-20260914-dumbbell-min-energy-triage-cf68286d5ba6`.
Date: 2026-09-14. Decision: advance; candidate_kind=none;
original_status=unresolved. This is a triage check, not referee acceptance.

## Source and recovery leads

Read both enumerated handoffs: `literature/outer-intake-handoff.md` and
`literature/triage-recovery-handoff-20260914T1704.md`. The prior phase was
terminated without an accepted worker result. Its evidence remains intact;
this job does not change runner state, counters, or that outcome.

Live primary sources retrieved on 2026-09-14:

- [Version record](https://arxiv.org/abs/2604.27785): latest listed version
  is v2, 26 May 2026.
- [Primary v2 text](https://arxiv.org/html/2604.27785v2): Introduction
  retains the all-odd minimum problem; Definition 2.3 and Theorem 2.10
  agree with the graph and matching formula in `problem.md`.
- In that text, Theorem 4.7, equation (117), quantifies over every interior
  minimizer, with no nonsingularity assumption. Its proof differentiates
  the improper integral using polynomial parameter dependence.
- Proposition 4.9 already supplies the half-diagonal energy and strict
  improvement over the origin. The paragraph before Figure 2 already notes
  nondifferentiability at that point. A uniform correction must add more
  than rediscovering that observation.

These passages also agree with the supplied PDF text: Section 4.1 and
Lemma 4.2, printed pp.9-10; Theorem 4.7, pp.13-14; Proposition 4.9 and
the Figure 2 discussion, pp.16-17. Local inspected spans were lines
463-532, 756-808, and 916-978 of `literature/2604.27785v2.txt`.

Fresh queries were `"2604.27785" correction stationarity` and
`"complex unit gain dumbbell" "minimum" energy`. They returned the
source and derivative listings; no later correction or resolution was
identified. Search snippets were not theorem evidence. Reused the same-day
bounded screen in `literature/triage-screen.md`; this is qualified
open-supported status, not an exhaustive priority claim.

## Exact replay and mathematical review

Command: `python3 evidence/recovery_checks.py`, exit 0, SymPy 1.14.0.
The wrapper replays every mathematical assertion in the preserved verifier
with only the result destination and job provenance changed. It excludes
the old registry scan. Old code, results, and argument files are preserved.
Output: `evidence/recovery-checks.json`; it records the original verifier
hash. Four rational Hermitian characteristic-polynomial comparisons, 27
constant-term identities, root isolation, cubic factorization, stationarity
numerator and derivative jump all passed. Three kernel comparison identities
and the zero-root derivative were additionally checked exactly.

The complete small-case argument in `evidence/triage-math.md` was reviewed
directly, not inferred from the success flag. Details resolving possible gaps:

1. For ab<=0, expansion of K-Z^2 has nonnegative terms
   X^2(a^2+b^2)-2ab(ZW-X^2)+a^2b^2W^2, with ZW-X^2>0.
   It is strict away from the origin. For ab>0 the comparison with the
   same-product diagonal is exactly X^2(a-b)^2. Together with simultaneous
   negation, this reduces the full closed square, including its boundary,
   to c in [0,1].
2. For c<1/2, F_+ has negative root product and trace 1, so real-rootedness
   forces one negative root and two positive roots. F_- has positive root
   product and trace -1, hence two negative roots and one positive root.
   Thus the energy expression 2+2(U+v) is valid. With
   h(z)=z^3+z^2-3z, h(U)=1-2c and h(v)=1+2c, one has v>U>1;
   increasing h' on this interval makes the energy derivative negative
   for 0<c<1/2.
3. For c>1/2, both root products are positive. F_+ cannot have three
   positive roots because its pairwise-root sum is -3; F_- cannot because
   its trace is -1. Hence the energy equals twice the two positive roots,
   each strictly increasing with c. Continuity handles c=1/2. The only
   minimizing real-part pairs are therefore (+1/2,+1/2) and (-1/2,-1/2).
4. At the positive minimizer both equation (117) numerators equal
   2t^6(1+5t^2+7t^4)>0. The denominators are positive; the integrands are
   O(t^4) at zero and O(t^-2) at infinity, so the integrals converge and
   cannot equal zero. This contradicts the equations in their stated scope.
   The simple zero root has diagonal derivative -2/3 and causes a 4/3
   jump in the energy derivative. It does not invalidate the diagonal
   conclusion, already established without differentiation.

The determinant-permutation argument for the full characteristic formula
and the unique-perfect-matching argument for
P(0)=(-1)^(N/2)(1-4 alpha beta) were also checked directly. Finite replay
does not establish a uniform optimality theorem or its novelty.

## Deduplication, scope, and next test

Read `literature/dedup.json` and `evidence/triage-registry.json` as prior
receipts, not a new corpus scan. The supplied neighboring original statements
concern thrackle embeddings, signed theta edge flips, or positive/negative
squared energy of unicyclic graphs. Their graph classes, gain domains or
functionals differ from the frozen task. No fresh whole-corpus, Windows, or
conversation comparison is claimed.

Advance is justified by a precise possible delta and exact verifier: a uniform
nonsmooth replacement for Theorem 4.7 with explicit structural information.
Original all-odd minimum/equality classification remains unresolved. The
known half-diagonal value and the already acknowledged cusp are not novelty.
No manuscript, candidate acceptance, or publishability claim is made.

One next test: on alpha beta=1/4 in the interior square for arbitrary odd
r,s>=3 and odd ell>=1, establish zero-root simplicity, isolate its
absolute-value contribution, and derive explicit necessary directional
optimality conditions; require exact recovery of the D_(3,3,1) cusp.
This test is left to research, as the recovery handoff requests.
