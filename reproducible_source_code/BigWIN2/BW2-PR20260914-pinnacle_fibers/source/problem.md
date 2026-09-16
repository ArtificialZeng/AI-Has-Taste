# Fixed pinnacle-order fibers: precise statement and research scope

The verbatim input remains in `source.md`, unchanged. Its SHA256 is
`1df3a7b5d04986a7f3a816b6fd50b53b6a27d5b95b005273f1d100fe5f5bcba7`.
Recovery triage: `primary-20260914-pinnacle-fibers-triage-e0fe653b2140`,
2026-09-14. The hash was rechecked before and after certificate validation.

## Definitions and quantifiers

Let n be a nonnegative integer, [n]={1,...,n}, and S_n the permutations
of [n]; S_0 contains the empty permutation. For pi in S_n, its ordered
pinnacle list is the sequence of pi_i with 2<=i<=n-1 and
pi_(i-1)<pi_i>pi_(i+1), read by increasing i. Endpoints are not peaks.
For every finite sequence sigma of distinct positive integers, let
P_n(sigma) be the permutations with complete ordered pinnacle list sigma.
The sequence records actual values, not their relative order pattern.

For v in [n], define iota_v(pi) to count values u<v lying to the right
of v in pi. Define pi <=_M rho iff iota_v(pi)<=iota_v(rho) for every
v in [n]. This is the value-indexed middle order, not the positional
inversion order or weak order. The full order on S_n is isomorphic to
the product of chains product_(v=1)^n {0,...,v-1}.

The literal source question asks whether, for all n and sigma, the
restriction of <=_M to P_n(sigma) is a distributive lattice. With the
nonempty convention for lattices, impossible sigma gives an empty-fiber
boundary defect (for example n=1 and sigma=(1)). The source's displayed
pairwise lattice axioms do not explicitly impose nonemptiness, so this
is convention dependent, not a substantive counterexample.

The openly qualified target is: for every n>=0 and every sigma such that
P_n(sigma) is nonempty, is (P_n(sigma),<=_M) a distributive lattice?
For every pair a,b in a fiber, a meet is its greatest common lower bound
IN THAT FIBER, and a join its least common upper bound IN THAT FIBER.
Distributivity means a meet (b join c)=(a meet b) join (a meet c) for all
triples in the fiber (equivalently the dual identity).
Ambient coordinatewise min/max need not be the internal meet/join.

The empty sigma is included. For n=0,1 it gives a singleton; for n=2
it gives S_2, a two-element chain. For n>=3 it means permutations
without interior peaks. Nonempty sigma is impossible at n<=2.

## Primary baseline and proposed contribution

Liang--Sagan, *Log-Concavity and Log-Convexity via Distributive Lattices*,
Order 43 (2026), article 21, Section 6 (printed pp.15--16) defines this
middle order; Section 8.2, Question 8.6(a) (printed p.30) asks this
fiber question. The arXiv v1 number is Question 8.7(a).
Published source: https://users.math.msu.edu/users/bsagan/Papers/Old/lclc%20-%20pub.pdf

Rusu--Tenner, *Admissible pinnacle orderings*, Theorems 3.4 and 3.6,
characterizes which ordered pinnacle lists occur. For a nonempty set S,
write S_x=S intersect [x]. Set admissibility requires |S_x|<x/2 for
all x in S. An ordering of an admissible set is realizable iff S_x has
at most x-2|S_x|-1 interruptions in that ordering for every x in S.
An interruption separates maximal consecutive blocks of entries of S_x.
Also require max(S)<=n for realization in S_n. This criterion does not
assert that the realizing permutations form a lattice.
Source: https://arxiv.org/html/2001.08185v3 (Sections 2--3).

Nearest prior result X: ambient middle-order distributivity and the
admissibility criterion. Proposed delta Y: the explicit five-permutation
pentagon obstruction in the nonempty fiber P_5((5)), giving a negative
answer to the selected distributive-lattice question if accepted on review.
Verification route Z: the four-table internal-meet argument and explicit
joins, supported by complete exact enumeration of the 56-element fiber,
then research freezing and fresh mathematical and novelty review.

Question 8.6(b), the counting/log-concavity question, is excluded.
No finite positive table is a proof of the universally quantified target.
Triage is not mathematical acceptance, and no manuscript is authorized by it.

The bounded test found a five-element pentagon obstruction in P_5((5));
see `evidence/n5_obstruction.md` for the internal-bound argument and
`literature/triage_verified.md` for the dated source screening. The next
research target is this exact n=5 obstruction, not further positive
extrapolation or the empty-fiber convention issue.

The recovery check `evidence/recovery_check.json` revalidated the complete
fiber, all 25 saved bound records for the five named elements, the four
possible ambient lower tables for a,c, and the distributive-law failure.
It also directly checked every distributive triple in every nonempty
fiber for n=0,...,4. This is exact finite evidence and an explicit local
argument, not a fresh referee verdict. Source status is open-supported
by the inspected primary question as prior provenance; no prior resolution
was found in the bounded screening, and no global novelty claim is made.
See `literature/recovery_verified.md` for current live checks and limits.

## Research submission scope (2026-09-14)

Research proposer: `primary-20260914-pinnacle-fibers-research-1f8e260fcbca`.
The proposed resolution is the negative answer witnessed by the NONEMPTY
fiber P_5((5)), with the exact internal operations on e,b,a,c,d proved in
`evidence/research_proof.md`. A failure at this admissible input refutes
both the literal universal assertion and the disclosed nonempty-fiber
qualification; no empty-fiber convention is used. The complete disproof
does not depend on a computer proving that the rest of the fiber is a
lattice. The independent audit has not yet occurred.

The current-job exact recomputation is `evidence/research_certificate.py`,
with output `evidence/research_certificate.json`. It covers only n=5 and
the full fiber with sigma=(5). Neither minimality in n nor any larger-n
classification is part of the submitted statement. All preceding references
to n<=4 evidence are historical finite observations, not additional claims
being submitted for acceptance. Source part (b) remains excluded.

Decisive retained primary text: `evidence/external/2408.02782v1.html`,
a byte-for-byte copy of `literature/2408.02782v1.html`, with Section 6 and
Question 8.7(a), element `S8.Thmthm7`. The live published definitions and
Question 8.6(a) agree. The contextual admissibility source was also copied
as `evidence/external/2001.08185v3.html`. Exact hashes, inspected portions,
current literature comparisons and source-access limits are in
`literature/research_verified.md`. These actual primary texts, along with
source.md and this precise interpretation, are to be bound to claim.json.
