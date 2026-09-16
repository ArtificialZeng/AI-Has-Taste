# Exact least-layer theorem and proof certificate

## Theorem

For ordered positive-integer quadruples (b=(b_0,b_1,b_2,b_3)) and
(a=(a_0,a_1,a_2,a_3)) satisfying the four equations frozen in `source.md`,
the least common sum is (61). At sum (61), the complete ordered solution
set consists of the following four pairs:

1. (b=(1,16,8,36)), (a=(4,9,16,32));
2. (b=(1,16,8,36)), (a=(4,16,9,32));
3. (b=(36,8,16,1)), (a=(4,9,16,32));
4. (b=(36,8,16,1)), (a=(4,16,9,32)).

Every pair has common signature ((61,1116,6912,18432)). The four pairs
form one orbit under the two and only two allowed involutions, with
representative (b=(1,16,8,36)), (a=(4,9,16,32)).

## Why the finite test is the stated system

Define (sigma_b) and (sigma_a) by the four integer expressions displayed
in `problem.md`. Equality of their first coordinates is the common-sum
equation, and equality of coordinates two through four gives, term for term,
the other three frozen equations. Thus
(sigma_b(b)=sigma_a(a)) is equivalent to the full system, rather than merely
a necessary filter. The source paper independently derives the same equivalence
by coefficientwise comparison of its reduced quartics (3.1) and (3.2).

## Exhaustive signature join

`enumerate_signatures.py` makes separate passes over the two ordered domains.
On a layer of sum (s), it chooses arbitrary positive first three coordinates
whose partial sum is at most (s-1), then assigns the unique positive residual
to the fourth coordinate. This is a bijection with the positive ordered
compositions of (s) into four parts, so it visits every tuple exactly once.
The observed count on each layer is (inom{s-1}{3}); the aggregate count on
each side through 61 is


\[
  \sum_{s=4}^{61}\binom{s-1}{3}=\binom{61}{4}=521855.
\]

It computes both signatures with arbitrary-precision integers and joins exact
equal keys. `signature_join_61.json` records zero matches on every layer
(4\le s\le60), and exactly the four displayed matches on layer 61.

## Structurally independent bounded-SMT verification

`verify_z3_bv.py` neither imports nor calls the enumeration program. It asserts
the eight coordinates and the four equations directly in quantifier-free
bit-vector logic. Each coordinate is a six-bit unsigned value in `[1,58]`;
the upper bound loses nothing because four positive coordinates with total at
most 61 have each coordinate at most 58. Every coordinate is zero-extended to
32 bits before any arithmetic.

The bit-vector equations are exact integer equations on this domain. Indeed,
using only (1\le x_i\le58), crude bounds for the absolute difference of the
two sides are at most (87464), (4292464), and (56582480) for the
quadratic, cubic, and quartic equations, respectively; the sum difference is
also below (2^{32}). Each bound is strictly below the modulus (2^{32}).
Therefore congruence modulo (2^{32}) is equality over the integers for every
asserted equation in this bounded domain, including expressions containing a
subtraction.

Z3 4.15.3 returned `unsat` for the direct query with common sum at most 60.
For common sum at most 61 it returned the four displayed models. After each
model, the verifier added a clause excluding that exact ordered 8-tuple; after
the fourth clause it returned `unsat`. The initial, sub-61, and terminal
model-blocked SMT-LIB instances are retained beside the JSON report. Thus the
SMT model list is complete for the represented domain, not a sampled search.

`independent_verifier_comparison.json` fail-closed compares the two reports. It
confirms their coverage statements, the absence below 61, terminal SMT
exhaustion, and equality of their complete ordered hit sets.

## Conclusion and orbit classification

The sub-61 UNSAT decision and the zero joins exclude every positive solution
of smaller sum. Each of the four recorded pairs verifies the equations exactly,
so sum 61 is attained and hence is minimal. Applying the reversal involution to
the displayed (b) exchanges the two recorded (b)-tuples, and applying the
middle-coordinate involution to (a) exchanges the two recorded (a)-tuples.
Their commuting actions generate all four Cartesian combinations, so there is
exactly one permitted orbit.

This theorem resolves only the least positive layer of equation (3.3) for the
fixed P4/Paw ansatz. It does not determine the least order over all connected
distance-cospectral graph pairs of opposite bipartiteness, nor classify
solutions of (3.3) above sum 61.
