# Proof dossier: all restricted 2-by-4-by-3 counts

Research job `newwin-00001-p12-research-79bff11d6956`, 2026-09-12.
This is a proposed complete computational proof for fresh mathematical review.
It is not an acceptance report or a publication manuscript.

## Exact theorem

Let q be any prime power. Let lambda and mu be weakly decreasing triples
of nonnegative integers, with mu_j <= lambda_j, lambda_j <= 4-j, and
mu_j <= 3-j for j=1,2,3. The number of ordered pairs (A,B) of 4-by-3
matrices over F_q satisfying

\[
A_{rj}=0\quad(r>4-\lambda_j),\qquad
B_{rj}=0\quad(r>4-\mu_j)
\]

and having nonzero boundary-format hyperdeterminant is

\[
q^9(q-1)^6\prod_{j=1}^3[5-j-\lambda_j]_q
                 \prod_{j=1}^3[4-j-\mu_j]_q.                 \tag{T}
\]

Here [n]_q=1+q+...+q^(n-1). This is precisely the statement frozen in
`source.md` and `problem.md`. In particular, nondegeneracy concerns the
algebraic closure, all allowable entries may be zero, and arrays are not
identified under group actions. The general conjecture for k>3 is outside
this theorem.

## Established dependency and normalization

Write E_0 and E_1 for the 4-by-3 matrices with respectively
(E_0)_{tj}=1 iff t=j and (E_1)_{tj}=1 iff t=j+1.
For sigma in S_4 and pi in S_3, define matrices over Z[X,Y] by

\[
L_{\sigma(a),a}=1,\quad
L_{\sigma(a),b}=x_{ab}\quad(a<b,\ \sigma(a)>\sigma(b)),
\]
\[
R_{\pi(i),i}=1,\quad
R_{\pi(j),i}=y_{ij}\quad(i<j,\ \pi(i)>\pi(j)),
\]

with all other entries zero. Variables are distinct for distinct indicated
inversions, and X and Y are disjoint. Put H=(LE_0R, LE_1R) and
n=inv(sigma)+inv(pi). These are the SE and NW conventions of
Koprowski--Lewis, journal Definitions 4.5--4.7 (arXiv Definitions 4.12,
4.16, 4.23). R is the matrix multiplying on the right; in their group
action notation the second acting matrix is R-transpose. This removes a
potential inverse/transpose ambiguity.

Let C_(sigma,pi)(P,q) count assignments of these n variables for which H
respects P=(lambda,mu). The established orbit reduction is

\[
N_P(q)=q^9(q-1)^6\sum_{\sigma\in S_4,\pi\in S_3}
C_{\sigma,\pi}(P,q).                                      \tag{1}
\]

This is journal Corollary 4.2 (arXiv Corollary 4.19).
Its hypotheses are exactly nested partition zero patterns over any finite
field; there is no restriction on the characteristic. The source texts
are retained in `evidence/external/koprowski-lewis-eca2027-web.txt` and
`evidence/external/koprowski-lewis-2602.22129v1-web.txt`.
[Journal primary paper](https://ecajournal.haifa.ac.il/Volume2027/ECA2027_S2A3.pdf),
[arXiv version](https://arxiv.org/html/2602.22129v1).

For completeness, the reduction uses the free transitive action of
(GL_4 x GL_3)/{(cI_4,c^(-1)I_3)} on nondegenerate tensors, quoted from
Aitken in journal Theorem 3.1 (arXiv Theorem 3.3), and Bruhat decomposition,
journal Theorem 4.3 (arXiv Theorem 4.13). Bruhat factors the two acting
matrices into an upper triangular 4-by-4 matrix times L, and a lower
triangular 3-by-3 matrix times R-transpose. The product of triangular
group orders is q^(6+3)(q-1)^(4+3); the scalar stabilizer has q-1 elements.
Triangular multiplication and its inverse preserve the two bottom-left
zero patterns: left upper triangular operations mix a row with lower rows,
and right upper triangular operations mix a column with earlier columns,
whose permitted heights are no larger. This yields the factor in (1).
The normalized pivots in L and R also ensure that distinct assignments
within an augmented cell give distinct tensors: equality of the tensors
forces a scalar relation by the stabilizer theorem, and a pivot equal to 1
forces that scalar to be 1.

## Characteristic-free counting of an augmented cell

Every H has entries exactly 1 at

\[
(0,\sigma(\pi(c)),c),\qquad(1,\sigma(\pi(c)+1),c),
\quad 1\le c\le3.                                       \tag{2}
\]

These are its only entries with a constant term. For example, in the first
entry the left factor is zero before the intermediate index pi(c), and
the right factor is zero after it. The shifted argument proves the second
identity. A forbidden position from (2) therefore makes the cell empty
over every field. If no such pivot is forbidden, the zero assignment of
all variables is permitted.

Suppose the pivots respect P. We now count all assignments, including
nonzero ones. Let h be the number of forbidden entries whose generic
polynomial is nonzero. Each of these equations has a distinct variable
with coefficient 1 which can be solved in an explicit order.

To see this directly for a forbidden front entry (r,c), put
a=sigma^(-1)(r) and v=pi(c). Products contributing to that entry have
intermediate index a<=t<=v. If a>v the entry is zero, and a=v would be
the forbidden pivot, already excluded. If a<v, then r>sigma(v), because
the pivot in column c is allowed whereas r is forbidden. Thus x_(a,v)
exists. Set b=pi^(-1)(a). Necessarily b>c: if b<c, the allowed front
pivot in column b has row r, so monotonicity of lambda gives
r<=4-lambda_b<=4-lambda_c, a contradiction. The entry is consequently

\[
y_{cb}+x_{av}+\sum_t x_{at}y_{c,\pi^{-1}(t)},              \tag{3}
\]

where the sum runs over a<t<v for which both variables exist. We solve
this equation for y_(c,b). It occurs only as the displayed linear term.

For a forbidden back entry (r,c), again set a=sigma^(-1)(r), v=pi(c),
and d=v+1. The contributing left column indices range from a to d.
The entry is zero if a>d; a=d would be a forbidden pivot. If a<d,
then r>sigma(d), so the term x_(a,d), from the right pivot, exists with
coefficient 1. All remaining terms involve only x_(a,t+1) with t<v,
or y_(c,j), or products of such variables. We solve for x_(a,d).

Order all variables lexicographically by the keys

\[
K(x_{ab})=(b,0,0,a),\qquad
K(y_{ij})=(\pi(i),1,-\pi(j),0).                            \tag{4}
\]

In (3), x_(a,v) precedes y_(c,b) at the second key coordinate; all
intermediate x_(a,t) precede it at the first coordinate. An intermediate
y_(c,pi^(-1)(t)) precedes it at the third coordinate because t>a.
In a back equation the target's first key coordinate is v+1, while all
other variables have first coordinate at most v. Thus every equation is
z+f(earlier variables)=0. Front targets are distinct since (c,b) determines
the row sigma(pi(b)) and column c. Back targets are distinct since (a,d)
determines the row sigma(a) and column pi^(-1)(d-1). Front and back targets
lie in disjoint variable sets.

There are exactly h targets. Assign all other n-h variables freely and
then solve successively in order (4). Each step is unique and uses only
addition and multiplication and a sign; no division by a characteristic-
dependent quantity occurs. Conversely every solution arises this way.
This proves a polynomial parametrization over Z with inverse projection
to the free variables, and hence

\[
C_{\sigma,\pi}(P,q)=q^{n-h}                               \tag{5}
\]

for every prime power q whenever the pivots respect P. This counting
principle is the existing one behind journal Theorem 4.4 and Section 5.1;
no novelty is claimed for it. Formula (4) makes its use in the finite
certificate explicit.

## Complete finite polynomial verification

All admissible shapes are enumerated without any symmetry quotient by

\[
0\le l_1\le3,\quad0\le l_2\le\min(l_1,2),\quad
0\le l_3\le\min(l_2,1),
\]
\[
0\le m_1\le\min(l_1,2),\quad
0\le m_2\le\min(m_1,l_2,1),\quad m_3=0.
\]

These ranges are equivalent in both directions to the theorem's
inequalities. They give 55 pairs. Each pair is tested against all
4!3!=144 permutation pairs; none are discarded by an unproved symmetry.

`evidence/verify_sparse.py` constructs the actual matrices entry by entry
over Z and multiplies them using sparse polynomial addition and
multiplication. It records every augmented matrix, all 7,920 cases,
the forbidden constant witness in every empty case, and every equation,
free variable, order, and solved polynomial in every nonempty case.
It verifies all target uniqueness and ordering conditions, and substitutes
the solved polynomials into every original forbidden entry, obtaining
zero identically in Z[free variables]. In addition to (4), an independent
topological sort checks acyclicity. No interpolation or finite-field
assumption enters this part.

For each shape, let c_d count surviving pairs with n-h=d. The exact
coefficient vector (c_0,c_1,...) is in `evidence/shape_table.md`.
The complete certificate is `evidence/sparse_certificates.json`.
For each row of that table the program directly counts the sums of
exponents chosen from the six ranges 0,...,r_j-1, where

\[
(r_1,\ldots,r_6)=(4-l_1,3-l_2,2-l_3,3-m_1,2-m_2,1-m_3),
\]

and verifies equality with c_d for every coefficient. Thus each row proves
the polynomial identity in Z[q]

\[
\sum_d c_dq^d=\prod_{j=1}^6(1+q+\cdots+q^{r_j-1}).        \tag{6}
\]

The run gives 6,759 empty and 1,161 nonempty cases, with 997 unit-pivot
equations in total. The maximum degree of a serialized solution polynomial
is 3. All 55 identities (6) hold. A separately implemented earlier Boolean
support calculation also agrees term by term, including every n,h,d.
That comparison is an extra check, not an input to the sparse derivation.
Combining (1), (5), and the complete list of identities (6) proves (T).

## Adversarial check and scope limitations

The separate program `evidence/exhaust_f2.py` tests the full binary tensor
domain of 2^24 inputs. It first discards rank-deficient A or B (a necessary
condition), leaving 2,520^2=6,350,400 pairs. It then takes the gcd in F_2[t]
of the four 3-by-3 minors of A+tB. Gcd 1 excludes a rank drop at every
finite point of the algebraic closure; full rank of B excludes infinity.
Therefore this is an exact exhaustive test of the original definition
at q=2. It uses no augmented cells or permutation-sum code. Every one
of the 55 counts agrees, with 3,386,880 nondegenerate tensors in the
unrestricted case. `evidence/exhaust_f2.json` records all counts.

This test also finds 403,200 additional tensors that pass just the three
F_2-rational pencil tests, including an exact witness whose nonzero minor
is 1+t^2+t^3. This is a diagnostic against weakening the rank criterion;
it is not a novel subsidiary contribution. The binary enumeration supports
the proof but does not establish other q; the Z-polynomial argument does.

The candidate resolves the specified k=3 problem only. Fourteen shapes
with mu=0 and the maximal shape were already proved in the primary paper;
the contribution is the complete product evaluation covering its other
40 shapes, with reproducible small certificates. The prior orbit method,
cell-counting principle, and general positivity theorem are credited to
the primary authors. The current source comparison is in
`literature/research-screen.md`; it does not establish global priority.

Known mathematical gaps in the proposed proof: none. The finite
calculation is part of the proof and remains subject to fresh review of
its implementation, coverage, source dependency, and contribution value.
There is no formal proof-assistant certificate, independent model audit,
or peer review at this stage.

Reproduction from the project root:

```
python3 evidence/verify_sparse.py
python3 evidence/exhaust_f2.py
```

The first uses Python's standard library; the second uses NumPy for exact
integer array operations. Their JSON reports are evidence summaries,
not replacements for the argument and inspectable computations above.
