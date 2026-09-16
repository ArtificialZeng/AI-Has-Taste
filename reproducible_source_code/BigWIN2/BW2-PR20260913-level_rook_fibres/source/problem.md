# Precise problem and triage scope

The immutable original statement is in source.md, SHA256
`0d9344b0f088a0d374302c97799c3d24e842950554cba9a17bc1af1702f2c20f`.
This file interprets it; it does not replace the original arbitrary-m scope.

## Definitions and quantifiers

For each integer m>=1, let a Ferrers shape be a finite weakly increasing
sequence B=(b_1,...,b_n) of positive integer column heights; n=0 is allowed.
Leading zero columns are identified as padding, not counted as distinct
shapes. This convention is explicitly supported by Barrese 1812.00533v2,
Section 3. Width n is not fixed. A translation of a padded representation
does not create another shape under this normalization.

For every positive integer p, level p consists of rows (p-1)m+1,...,pm,
counted from the bottom. Its number of cells is

    L_p(B) = sum_(i=1)^n min(m,max(0,b_i-(p-1)m)).

If B is nonempty, t=ceil(b_n/m) is its number of nonempty levels, and

    l_m(B)=(L_t(B),L_(t-1)(B),...,L_1(B)).

Set l_m(empty)=empty. A Ferrers shape is m-singleton if, for every p>=1,
there is at most one column i with (p-1)m<b_i<pm. Full columns ending at
pm are unrestricted. This is a condition on column multiplicity as well as
heights. BLRS 1508.05944v1, Definition 4 and the paragraph before Lemma 5,
state that l_m maps all Ferrers shapes onto m-singleton shapes and restricts
to an involution on singleton shapes. The same-level singleton B_S is a
different construction; l_m(B)=l_m(B_S), not generally B_S.

The original target is: for every m>=1 and every m-singleton Ferrers shape
C=(c_1,...,c_t), determine

    F_m(C) = #{Ferrers shapes B : l_m(B)=C}.

The fibre includes nonsingleton B and varying widths. Its members all have
area N=sum_i c_i, so the fibre is finite. The empty shape has F_m(empty)=1.
For m=1, l_1 is ordinary conjugation and F_1(C)=1. A non-singleton target
has no preimage, but is outside the requested input domain.

## Source status, nearest result, and contribution standard

Source status: open-supported by the authors' explicit question in BLRS,
Section 6.2, printed p.21, and no resolution found in the primary passages
inspected during this bounded 2026-09-13 search. This is not a guarantee of
current worldwide open status. See literature/triage-screen.md for URLs,
positions, and search limits. No prior resolution was established here.

Nearest enumeration theorem: BLRS 1308.4081 Theorem 5.2, printed p.15,
counts singleton boards in an m-level rook-equivalence class. It does not
count arbitrary boards in one fibre. Weighted-file enumeration is also a
different problem. Solving this fibre question would not by itself be
claimed as solving the source's broader full-class enumeration problem.

An answer must provide an informative uniform formula, structural
classification, or algorithm with a demonstrated nontrivial benefit.
Generic enumeration of all partitions of N, a tautological coefficient
product, or another small census alone does not meet that threshold.

## Proposed partial theorem: m=2, all singleton inputs

This is a natural parameter-wide partial target, not a correction of the
original. The new reduction in evidence/m2-path-reduction.md encodes the
fibre by integer points in an inhomogeneous path polytope. For
s_i=c_(t+1-i), s_(t+1)=0, and

    a_i=floor(s_i/2)-ceil(s_(i+1)/2),

the coordinates satisfy d_i>=0, d_i+d_(i+1)<=a_i (i<t), and d_t<=a_t.
Direct column enumeration and inverse reconstruction agree for all 2,714
boards of area 0..20, grouped into 797 fibres. This finite test is distinct
from the derivation and is not an unrestricted proof audit.

Nearest adjacent method: Jiang–Wen–Zhong 2607.14887v1, Section 2.1,
uses finite transfer matrices for alternating-capacity path polytopes.
Earlier uniform weighted-graph sources are recorded as further leads.
Thus the ordinary transfer recurrence alone is not the proposed novelty.

Research pass 1 gives a complete proposed proof of that stronger delta in
evidence/m2-compressed-proof.md. For arbitrary nonnegative path capacities
a_1,...,a_t and A=max a_i, exact counting takes O(t^4) integer operations
on O(t log(A+t+2))-bit integers and O(t^2) stored integers. A conservative
schoolbook bit bound is O(t^6 log^2(A+t+2)). This implies polynomial time
for F_2(C) in log(t+1)+sum_i log(c_i+1). The algorithm stores at most i
integer intervals of degree at most i-1 at layer i. Normalizing each
piece by forward differences taken only inside its interval yields
|c_k|<=2^(i-1)(A+1)^(i-1), where c_k here denotes a polynomial coefficient,
not a column height. Every nonnegative capacity vector occurs for a
positive singleton target, as shown in the proof.

evidence/m2-compressed.py implements the method with exact integers. Its
verifier compares 35,915 exhaustive capacity vectors, including 3,906
direct Cartesian-product counts, all 797 direct Ferrers fibres of area
0..20, and 160 longer heterogeneous numeric-DP cases. Large two-variable
closed forms and uniform-capacity rational Lagrange interpolation provide
additional oracles. Four 80-coordinate cases with capacities reaching
100 digits are labelled stress runs without independent oracles.
The JSON records these scopes separately. No finite test is the proof.

literature/research-comparison.md checks the precise claim against primary
weighted-path, alternating-sequence, marked-order-polytope, flagged
P-partition, and symbolic-inference sources. Uniform cases, qualitative
piecewise polynomiality, and piecewise polynomial message passing are
known. No equivalent binary-input F_2 theorem was found in the inspected
statements; broader priority is not certified. All local primary sources
decisive for the original statement, normalization, and nearest theorem
have exact copies under evidence/external/.

This is a proposed result-note, requiring fresh mathematical and
contribution review. It is not a proof of the full original problem.
One next test: independently audit the frozen m=2 theorem, especially
short-interval normalization and the bit bound, and attempt to identify
an equivalent binary-input fibre result in the bounded-poset literature.
