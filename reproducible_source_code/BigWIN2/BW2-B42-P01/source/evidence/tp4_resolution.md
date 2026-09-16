# Exact computer-assisted proof that the Eulerian triangle is TP4

This dossier proves the frozen claim in `source.md`, subject to fresh
mathematical audit.  All computations used as proof are exact integer
computations and their complete outputs are stored in the accompanying JSON
certificates.  The source paper's TP3 theorem and its lower-triangular reduction
criterion are used as stated in `problem.md`.

## 1. Reduction to consecutive order-four minors

Write

`A_n(x)=sum_k A(n,k)x^k`.

Frobenius real-rootedness gives

`A_n(x)=product_(i=1)^n(1+r_i x)`, with every `r_i>0`.

For `I subset [n]` put

`f_I=product_(i notin I)(1+r_i x)`, `g_I=product_(i in I)(1+r_i x)`,
`c_I=product_(i in I)(1+r_i)`, and
`G_j=sum_(|I|=j)c_I f_I`.

The source identity

`(1-x)G'_j=(j+1)G_(j+1)-(n-j)G_j`

and the Eulerian recurrence show that one Eulerian step, when applied to a
formal term `x^a G_j` while constructing row `n+t+1` from row `n+t`, is

`x^aG_j -> (a+1)x^aG_j+(t+1-a+j)x^(a+1)G_j+(j+1)x^(a+1)G_(j+1)`.

Iterating for `t=0,1,2`, followed by determinant-preserving row operations,
gives, for `K={k,k+1,k+2,k+3}`,

`D(n,k):=D_K(A_n,A_(n+1),A_(n+2),A_(n+3))`

`=D_K(G0,xQ1,xG0+x^2Q2,x^2H2+x^3Q3)`,

where

`Q1=G0+G1`, `Q2=G0+3G1+2G2`,
`H2=7G0+10G1+4G2`, and `Q3=G0+7G1+12G2+6G3`.

The exact formal-basis check is `verify_row_reduction()` in
`reconstruct_126.py`.  Expanding the last two rows produces four determinants,
with subset-size caps and shifts as follows.

| term | subset caps in rows 2--4 | shifts | maximum union size | maximum local row degrees |
|---|---|---|---:|---|
| 1 | `(1,0,2)` | `(0,1,1,2)` | 3 | `(3,3,4,3)` |
| 2 | `(1,0,3)` | `(0,1,1,3)` | 4 | `(4,4,5,4)` |
| 3 | `(1,2,2)` | `(0,1,2,2)` | 5 | `(5,5,5,5)` |
| 4 | `(1,2,3)` | `(0,1,2,3)` | 6 | `(6,6,6,6)` |

For any selected subset tuple, let `U` be its union and `m=|U|`.  Factoring
the common `f_U` from the four rows and applying the source's
Toeplitz--Cauchy--Binet identity yields

`D(n,k)=sum_(U subset [n], |U|<=6) sum_(L subset {0,...,6}, |L|=4)`

`          Psi_U(L) det T_(f_U)(L,K).`                                             (1)

Every `f_U` is a product of factors `1+r_i x`, so its upper coefficient
Toeplitz matrix is totally nonnegative.  Hence every Toeplitz determinant in
(1) is nonnegative.  Relabelling `U` permutes the `r_i` and proves that
`Psi_U(L)` is a symmetric polynomial depending only on the canonical template
`(m,L)`.

Exact support enumeration leaves respectively

`1,3,9,19,25,34,35`

nonzero templates for `m=0,...,6`, a total of 126.  Of the other 119 slots,
118 have no support-perfect-matching and `(5,{3,4,5,6})` cancels identically.
The exhaustive map and the exceptional symbolic identity are in
`template_manifest.json` and `reconstruct_126.py`; the full derivation is in
`coverage_126.md`.

## 2. Universal signs of all 126 templates

The script `audit_template_coefficients.py` implements (1) independently as a
sparse polynomial calculation.  The condition that the selected subsets have
union exactly `U` is enforced by

`sum_(V subset U)(-1)^(m-|V|) [all selected subsets lie in V]`.

Within the bracket, determinant multilinearity separates the three subset
sums.  Every resulting local row is multiaffine in `r_1,...,r_m`; therefore
every ordinary monomial exponent in a four-row determinant is at most four.
Sparse monomials are stored as base-five exponent vectors and all arithmetic is
over the integers.  Symmetry follows before computation by relabelling `U`.
The script collapses labelled monomials into permutation orbits only after a
complete determinant, verifies exact divisibility by each orbit size, and
cross-checks every reconstructed polynomial at a fixed positive integer vector
against the direct subset evaluator in `reconstruct_126.py`.

The complete 126-polynomial coefficient output is
`template_coefficients.json`.  It finds 120 coefficientwise-nonnegative
templates.  The remaining six contain exactly 18 negative symmetric-monomial
orbits; these are also nonnegative by the following exact Muirhead certificate.

For a length-`m` partition `lambda`, let `m_lambda` be the sum of the distinct
labelled monomials in its orbit, let `N_lambda` be the orbit size, and set
`M_lambda=m_lambda/N_lambda`.  Muirhead's inequality says
`M_lambda>=M_mu` on nonnegative variables whenever `lambda` majorizes `mu`.
An ordinary orbit coefficient `c_lambda` supplies
`c_lambda N_lambda M_lambda`.  Each row below transfers the displayed amount
from a positive supply to cover a negative demand.  Equal total degrees and all
majorization partial sums are checked in `verify_muirhead_certificate.py`.

| template | positive `lambda` | negative `mu` | normalized amount |
|---|---|---|---:|
| `m4-L1234` | 2110 | 1111 | 984 |
| `m4-L2345` | 3320 | 3311 | 72 |
|  | 4320 | 4311 | 144 |
|  | 4420 | 4411 | 72 |
|  | 4430 | 4421 | 72 |
|  | 4431 | 4422 | 72 |
| `m5-L1234` | 21100 | 11110 | 1440 |
|  | 21110 | 11111 | 1200 |
| `m5-L1235` | 21110 | 11111 | 720 |
| `m5-L1345` | 32110 | 31111 | 240 |
|  | 42110 | 41111 | 240 |
|  | 43221 | 42222 | 240 |
| `m5-L2345` | 32210 | 32111 | 600 |
|  | 42210 | 42111 | 600 |
|  | 33210 | 33111 | 600 |
|  | 43210 | 43111 | 600 |
|  | 43221 | 42222 | 600 |
|  | 43321 | 43222 | 600 |

For every negative orbit the transferred amount equals its entire normalized
demand, and no positive orbit's available supply is exceeded.  The exact
amounts, orbit sizes, unused supplies, and majorization partial sums are stored
in `muirhead_certificate.json`.  It follows that every `Psi_m(L)` is
nonnegative whenever all `r_i>=0`, in particular for the positive Eulerian
roots.

## 3. Strictness and conclusion

Equation (1) now gives `D(n,k)>=0`.  In fact it is strictly positive for every
`n>=k>=0`: retain only the template `m=0`, `L={0,1,2,3}`, whose coefficient is
one.  Its Toeplitz factor is

`det[e_(k+j-i)(r_1,...,r_n)]_(1<=i,j<=4)`

(`e_q=0` outside its natural range).  By the dual Jacobi--Trudi identity this
is the Schur polynomial `s_(4^k)(r_1,...,r_n)`.  It is positive for positive
`r_i` when `0<=k<=n`; for `n=k=0` it is `s_empty=1`.  All other summands in
(1) are nonnegative.

Thus every admissible consecutive order-four minor is strictly positive.
Orders at most three are strictly positive by the source's Theorem 1.1.
Applying its Theorem 2.5 to each finite leading principal truncation proves
that every admissible minor of order at most four is strictly positive.
Every nonadmissible minor of a lower triangular matrix is zero.  Consequently
every minor of the infinite Eulerian triangle of order at most four is
nonnegative, exactly as required in `source.md`.

## Reproduction

From the project root:

`python3 evidence/reconstruct_126.py --output evidence/template_manifest.json`

`python3 evidence/audit_template_coefficients.py --output evidence/template_coefficients.json`

`python3 evidence/verify_muirhead_certificate.py --output evidence/muirhead_certificate.json`

The first command reconstructs coverage, the second audits every ordinary
monomial coefficient, and the third checks the exact inequality transfers.
