# A quadratic product-weight theorem for the Pieri–RSK family

Proposed partial result for fresh review. The original Problem 29 remains
unresolved. This file is mathematical evidence, not a manuscript or acceptance.

## Statement and exact scope

Let n,a be admissible as in problem.md, with a>=2 and k=(n-a)/2>=2; hence
n>=6. Work over Q or C. Write y_ij for the image of x_ij, i<j, and E for
the two-element subsets of [n]. Put L=sum_(e in E) y_e. Let H_n be the set
of all two-edge matching monomials. Use ij as an abbreviation for {i,j}.
Define the following disjoint set of quadratic monomials:

T_n = {y_12 y_ij : 3<=i<j<=n}
    union {y_13 y_2j : 4<=j<=n}
    union {y_1j y_23 : 4<=j<=n}
    union {y_15 y_24, y_15 y_34, y_25 y_34}.

Theorem. The source's literal Pieri–RSK candidate in degree 2 is exactly
H_n minus T_n, and its residue classes form a basis of R(M_(n,a))_2.
Moreover, give each y_ij the positive weight n^2-ij. Every t in T_n has a
unique homogeneous straightening

    t = sum_(h in H_n minus T_n) c_(t,h) h

in the quotient, and c_(t,h)!=0 implies score(t)<score(h), where
score(y_ij y_rs)=ij+rs. Thus the straightening strictly decreases weight.
The degree-2 standard monomials are H_n minus T_n for every monomial order
refining this weight on Q[y_ij]. This statement concerns the presentation
using off-diagonal variables, not an unspecified order on all n^2 variables.

The degree-0 and degree-1 candidates in this range are {1} and all y_e except
y_12. Consequently, for every n>=6 the union of these three sets is a full
monomial basis, and a standard monomial basis for the same weight orders,
of R(M_(n,n-4)). This is the class with exactly two transpositions.
It has Hilbert series

    1 + (C(n,2)-1)q + (3 C(n,4)-C(n,2))q^2.

No assertion of a basis in arbitrary higher degree is part of the theorem.

## Dependency: the already known ideal presentation

Zhu, EJC 33(2) (2026), P2.54, Section 2.5, printed p.6, states generators
of gr I(M_(n,a)). The complete primary PDF and extracted text are copied to
evidence/external/. Its printed p.21 defines the candidate; Proposition 17
and Corollary 24 give its count and remove the first-row restriction when
d<=a. These are prior results, not contributions of this note.

The incidence interpretation and its rank criterion are also prior mathematics:
Dao--Nair, *On the Lefschetz property for quotients by monomial ideals
containing squares of variables*, Communications in Algebra 52(3) (2024),
1260--1270, arXiv:2112.09434v4, Proposition 3.1, Lemma 3.2 and Theorem 3.3.
Those passages were checked in the primary full text. The argument below
reproves the needed elementary facts; it claims no new Lefschetz criterion.
The proposed delta is the explicit identification of the source's excluded
Pieri--RSK monomials with T_n and the uniform product-weight comparison.

Here is the needed consequence, including the elimination check. Set
B=Q[y_e:e in E]/(y_e^2, y_e y_f for e and f sharing a vertex).
The symmetry and homogeneous row sums eliminate x_ji and x_ii, with
x_ii=-sum_(j!=i)y_ij. All row/column quadratic products then vanish already
in B: an off-diagonal product has a repeated endpoint, a diagonal times
an entry in its row has only such terms, and the diagonal square is a sum
of such terms. The diagonal sum is -2L. The remaining source generators
have degrees a+1 and >k, both at least 3 under the hypotheses. Therefore

    R(M_(n,a))_1 = B_1 / Q L,
    R(M_(n,a))_2 = B_2 / L B_1.                         (1)

There are no hidden lower-degree consequences: all the source generators
are homogeneous, and a polynomial multiple cannot lower their degrees.
Conversely, substitution defines inverse maps for the linear elimination.

## The incidence matrix and the basis

The graph G=KG(n,2) has vertex set E and joins disjoint pairs. Its edges
are precisely the basis monomials H_n of B_2. Let D be its signless
vertex-edge incidence matrix. For a vertex e,

    y_e L = sum_(f disjoint e) y_e y_f,

so the row space of D is exactly L B_1 in the H_n coordinates.

Regard T_n as a spanning subgraph of G. It consists of three disjoint stars:
center 12 with leaves ij, 3<=i<j<=n; center 13 with leaves 2j, j>=4;
and center 23 with leaves 1j, j>=4; together with the last three edges in
the displayed definition of T_n. Those three edges connect the stars.
There are C(n,2) vertices and C(n,2) edges. The graph is connected and its
unique cycle is

    13 -- 24 -- 15 -- 34 -- 25 -- 13,

of length five. If a row vector z satisfies z^t D_T=0, adjacent vertices
have opposite z-values. The odd cycle forces zero there, and connectedness
forces zero at every vertex. Thus the square matrix D_T is invertible
over Q (indeed its determinant has absolute value 2, by leaf elimination).

Writing H=H_n minus T_n, the relations give

    D_T (t)_(t in T_n) + D_H (h)_(h in H) = 0.

They solve uniquely as t=-D_T^(-1)D_H h. The rows are independent, and
(1) now proves that H is a basis, with dimension 3 C(n,4)-C(n,2).

## Strict weight comparison

For a vertex ij of G write p(ij)=ij, so a graph edge uv has score p(u)+p(v).
For each edge h=uv outside T_n we show its incidence column lies in the
span of T_n columns having score strictly smaller than score(h). Since
D_T is invertible, this proves that every nonzero entry in column h of
D_T^(-1)D_H occurs at a smaller-score row t, as required.

Two elementary facts will be used. The alternating sum of the incidence
columns along any odd walk from u to v equals the column vector e_u+e_v.
Repeated vertices or edges are allowed. Also the signless incidence columns
of a connected graph with an odd cycle span all its vertex coordinate space;
the same alternating-value argument as above proves full row rank.

The following cases exhaust h outside T_n.

1. h=(1r)(2s). Necessarily r,s>=3 and r!=s. If either is 3, h is in T_n,
so assume r,s>=4. Use the odd walk

    1r -- 23 -- 15 -- 24 -- 13 -- 2s.

Its edge scores are r+6, 11, 13, 11, 2s+3. All are less than r+2s:
the first and last comparisons use s,r>=4; the minimum r+2s is 13,
attained only at (r,s)=(5,4), which is the excluded edge 15--24 in T_n.
Every h under consideration therefore has score at least 14.

2. h=(1r)(st), with 3<=s<t and 2 absent, so r>=3.
For r>=4 use

    1r -- 23 -- 15 -- 34 -- 12 -- st.

Its scores are r+6, 11, 17, 14, st+2. The endpoint comparisons are
strict since st>=12 and r>=4. Disjointness gives r+st>=19 when r=4;
when r=5, its minimum 17 occurs only for h=15--34 in T_n; and when
r>=6, r+st>=18. Thus all five comparisons are strict. The remaining
case r=3 has score at least 3+4*5=23 and is covered below.

3. All cases not covered above either have h=(2r)(st), with s,t>=3,
or contain neither 1 nor 2 (or are the r=3 exception in case 2).
In the first type the minimum is 26 for r=3, 23 for r=4, and 22 for
r=5, the last occurring only at 25--34 in T_n; for r>=6 it is at least
24. In the second type the minimum is 3*6+4*5=38, already greater than
22. Hence every remaining h has score greater than 22.

The subgraph T_5 on the ten vertices ij contained in [5] is connected with
the five-cycle above, and all its edge scores are at most 22. Each endpoint
v of h not in that core attaches to it by one T_n edge: 1r to 23, 2r to
13, or ij (i,j>=3) to 12. The chosen neighbor has the smallest possible
product among vertices disjoint from v. Since h itself is not that T_n
edge, the attachment's score is strictly smaller than score(h). (Integer
products 6, 3, and 2 respectively are uniquely minimal.) Thus the smaller-
score subgraph contains the nonbipartite core and both endpoints of h.
Its incidence columns span e_u+e_v, finishing this case and the proof.

For each t in T_n the resulting relation has leading monomial t in every
order refining n^2-ij. Nonmatching quadratic monomials vanish individually.
These leading monomials already leave exactly dim R_2 monomials. No
additional degree-2 initial monomial can occur, by the dimension of a
homogeneous quotient and its initial quotient. This proves the stated
standard-monomial assertion. In degree 1, L has unique largest-weight
term y_12. In the k=2 corollary, all higher degrees vanish by the source
presentation, so these low-degree conclusions describe the whole basis.

## Identification with the source's tableaux

The Pieri bijection can be run forwards: for a matching on support
s1<s2<s3<s4, apply RSK, transpose the common tableau, and insert every
unused label in increasing order. This is inverse to the source's reverse
procedure. There are three pairings; direct four-letter row insertion gives
the following starting tableaux Q:

    (s1 s2)(s3 s4): Q = [s1 s2; s3 s4],
    (s1 s3)(s2 s4): Q = [s1 s3; s2 s4],
    (s1 s4)(s2 s3): Q = [s1 s2 s3 s4].

The first two have shape (2,2). PHS holds exactly when the strip meets
column 1, equivalently when insertion creates a third row. Indeed the
only possibly negative prefix is then the first step; after at most two
steps all remaining columns are strip columns. In the first tableau a
third row is created exactly when the smallest unused label is below s2;
in the second it is created exactly when that label is below s3. Such a
label immediately bumps a first-row entry smaller than some second-row
entry; if no such unused label exists, all insertions append in the first
row. The failures are respectively s2=2 and s3=3, giving exactly
12--ij and 13--2j in T_n.

For the nested pairing Q is one row of length 4. Inserting the unused
labels increasingly bumps only original support entries, in increasing
order, and appends them in row 2. The final second-row length t is the
maximum number of pairs (unused label, larger support label), using each
label once; the leftmost-greater greedy insertion realizes this maximum.
PHS holds exactly when t>=2: in the first four columns the strip occupies
the first t columns in row 2, followed by 4-t downward steps.

There are two such pairs precisely when s3>=4 and s4>=6. Necessity follows
by comparing the two chosen support labels with the two largest support
labels. For sufficiency pair the smallest unused label with s3 and the
second smallest with s4; the inequalities ensure both are available and
smaller than their targets. Hence PHS fails exactly when s3=3 or s4<=5.
The former gives 1j--23. The latter gives just the three additional edges
15--24, 15--34, 25--34 after removing overlaps. This is exactly T_n.

The extra first-row restriction in the source is automatic here by its
Corollary 24, since d=2<=a. In degree 1 the same argument starts with the
row tableau of the two matched labels. PHS fails only for matching 12;
this identifies the claimed degree-1 candidate as well.

## Audit boundaries

The proof is uniform in the stated range and uses no empirical inference.
Finite tests in verify_quadratic.py check the tableau description, incidence
inverse and all coefficient signs/weights independently of locus evaluation.
The earlier filtered ranks test actual point evaluations by different code.
Known graph-incidence linear algebra and the known ideal presentation are
explicit dependencies; novelty is proposed only for their application to the
literal Pieri–RSK family and its specific weight order. The contribution's
significance and literature coverage remain matters for the fresh referee.
Mathematical gap list for this partial theorem: none currently identified.
The uniform higher-degree product-weight hypothesis remains unproved.
