# Fresh mathematical referee report

## Frozen scope and reconstruction

I reviewed the claim at snapshot
`aa9d4e9c69acafe43ae93b50277cef413ba72d54831c6cc9c8fd13695634b5bf`.
All listed file hashes agree with `audit/snapshot.json`, and I independently
recomputed the snapshot digest from its canonical file map. The claim concerns
only ordered positive-integer solutions of the four displayed coefficient
equations, through the first nonempty common-sum layer. It does not claim a
minimum over all distance-cospectral graph pairs or a classification above that
layer.

Define the two four-component signatures exactly as in `problem.md`. Equality
of component 1 is the common-sum equation, while equality of components 2, 3,
and 4 is respectively the remaining quadratic, cubic, and quartic equation.
Thus an exact signature join is equivalent to the full frozen system; it is not
a relaxation or merely a necessary test.

For each fixed sum (s\geq 4), every ordered positive quadruple is uniquely
represented by three cut points (1\leq i<j<k\leq s-1), giving
((i,j-i,k-j,s-k)). Hence there are exactly
(\binom{s-1}{3}) tuples on each side and

\[
\sum_{s=4}^{61}\binom{s-1}{3}=\binom{61}{4}=521855
\]

on each side through 61. I performed a fresh, read-only exact-integer join using
this cut-point enumeration, independently of the nested-loop generator in the
submitted program. It visited 521855 tuples on each side, found no match on any
layer (4\leq s\leq 60), and found exactly these four ordered matches at 61:

1. (b=(1,16,8,36)), (a=(4,9,16,32));
2. (b=(1,16,8,36)), (a=(4,16,9,32));
3. (b=(36,8,16,1)), (a=(4,9,16,32));
4. (b=(36,8,16,1)), (a=(4,16,9,32)).

Direct exact substitution gives the common signature
((61,1116,6912,18432)) in every case.

## Submitted certificate checks

The exhaustive Python program uses arbitrary-precision integer arithmetic and
enumerates each positive composition exactly once, without pruning. Its frozen
report contains all 58 layers from 4 through 61, the correct per-layer counts,
aggregate count 521855 on each side, zero matches below 61, exactly the four
matches above at 61, and no anomaly.

I also checked the independent bit-vector encoding against the frozen equations.
Positivity together with common sum at most 61 makes the coordinate cap 58
lossless. All coordinates are zero-extended before 32-bit arithmetic. For the
four equalities, absolute bounds for the corresponding integer differences are
respectively below 465, 87464, 4292464, and 56582480, all strictly below
(2^{32}). Therefore equality modulo (2^{32}) is equivalent to integer
equality throughout the encoded domain, including the subtractions. Each model
blocking clause excludes exactly one ordered eight-tuple. I freshly ran Z3
4.15.3 on the frozen sub-61 SMT-LIB instance and obtained `unsat`; I also ran it
on the frozen instance with all four reported models blocked and obtained
`unsat`. These checks confirm absence below 61 and exhaustion after precisely
the four models.

The two stated involutions preserve every signature component. They exchange
the two distinct (b)-tuples and the two distinct (a)-tuples, respectively.
Their commuting action on any one reported pair therefore produces all four
distinct ordered pairs, so the complete layer is exactly one permitted orbit.

## Source comparison and contribution

The archived primary-source PDF was checked directly. Its equations (3.1) and
(3.2) yield exactly system (3.3); Theorem 3.1 supplies the sum-61 representative
but no lower-bound or equality-layer classification. Its conclusion asks for a
minimum-order determination and classification of positive solutions. The
candidate honestly restricts its delta to the first positive layer of this fixed
(P_4\)/paw coefficient system. This is a sharp minimum plus a complete ordered
equality classification, and is a coherent, nontrivial resolution of the frozen
problem even though the proof is finite and computational.

The dated literature record reports a targeted primary-literature search finding
no equivalent result and explicitly disclaims proof of priority. I found no
mathematical claim here that depends on a stronger novelty assertion. The broader
minimum graph-order problem and all layers above 61 remain unresolved, as the
candidate states.

## Verdict

**Accept.** The exact frozen claim is proved in its full stated scope; coverage,
arithmetic soundness, all four witnesses, completeness, and the permitted orbit
classification survive fresh reconstruction and independent recomputation. No
unresolved mathematical gap requires revision.
