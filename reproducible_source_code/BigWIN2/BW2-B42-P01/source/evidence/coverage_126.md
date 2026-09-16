# Exact reconstruction of the 126 TP4 templates

This note records an independently reproducible coverage calculation for the
consecutive order-four minors required by Theorem 2.5 of the source paper.  It
does **not** prove the missing universal signs, and hence does not prove TP4.

## Consecutive family

Every admissible consecutive `4 x 4` minor is uniquely

`D(n,k) = det[A(n+i,k+j)]_(0<=i,j<=3)`, with integers `n>=0`, `0<=k<=n`.

Indeed consecutive rows and columns have the displayed form, and admissibility
is equivalent to `k+i<=n+i`, i.e. `k<=n`.  Put
`K={k,k+1,k+2,k+3}` and let `D_K(P0,P1,P2,P3)` denote the determinant of the
four coefficient rows of the polynomials `P0,...,P3` at the columns in `K`.

For `A_n(x)=product_(i=1)^n (1+r_i x)`, where all `r_i>0`, use the source
paper's polynomials

`G_j = sum_(|I|=j) c_I f_I`,
`c_I=product_(i in I)(1+r_i)`, and
`f_I=A_n/product_(i in I)(1+r_i x)`.

The identity `(1-x)G'_j=(j+1)G_(j+1)-(n-j)G_j` shows that the Eulerian
step from row `n+t` acts on the formal basis by

`x^a G_j -> (a+1)x^a G_j + (t+1-a+j)x^(a+1)G_j + (j+1)x^(a+1)G_(j+1)`.

Iterating this identity three times and applying determinant-preserving row
operations gives

`D(n,k) = D_K(G0, x Q1, x G0 + x^2 Q2, x^2 H2 + x^3 Q3)`,

where

- `Q1=G0+G1`,
- `Q2=G0+3G1+2G2`,
- `H2=7G0+10G1+4G2`,
- `Q3=G0+7G1+12G2+6G3`.

Thus `D(n,k)=T1+T2+T3+T4`, where the four terms select respectively

1. `(G0,xQ1,xG0,x^2H2)`,
2. `(G0,xQ1,xG0,x^3Q3)`,
3. `(G0,xQ1,x^2Q2,x^2H2)`,
4. `(G0,xQ1,x^2Q2,x^3Q3)`.

The script checks the formal row expansions and these row operations exactly.

## Exhaustive grouping and the count 126

Expand each `G_j` as the subset sum above.  In any summand let `U` be the union
of the two or three selected subsets.  Factor the common polynomial `f_U` from
all four local rows and apply coefficient-matrix multiplication and
Cauchy--Binet.  This yields the exact identity

`D(n,k) = sum_(U subset [n], |U|<=6) sum_(L subset {0,...,6}, |L|=4)`
`          Psi_U(L) det T_(f_U)(L,K)`.

Here `Psi_U(L)` is the sum of the four local determinant expansions listed
above.  For example the fourth contribution is

`sum w1_|I| w2_|J| w3_|H| c_I c_J c_H`
`    det coeff_L(g_U, x g_(U\I), x^2 g_(U\J), x^3 g_(U\H))`,

over `|I|<=1`, `|J|<=2`, `|H|<=3`, `I union J union H=U`, with
`(w1_0,w1_1)=(1,1)`, `(w2_0,w2_1,w2_2)=(1,3,2)`, and
`(w3_0,w3_1,w3_2,w3_3)=(1,7,12,6)`.  The other three contributions use the
weights and shifts encoded in `reconstruct_126.py`.

The bound `L subset {0,...,6}` is exhaustive.  In the largest term, for
example, the four local degrees are `m`, `1+m-|I|`, `2+m-|J|`, and
`3+m-|H|`; the union condition and the size caps bound each by 6.  The other
three terms have smaller unions.  Relabelling the elements of `U` leaves the
sum invariant, so `Psi_U(L)` depends only on the template `(m,L)`, where
`m=|U|`.

Exact enumeration leaves the following numbers of nonzero templates:

| `m` | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| nonzero `(m,L)` | 1 | 3 | 9 | 19 | 25 | 34 | 35 |

Their sum is exactly `126`.  Of the `7*binom(7,4)=245` possible slots, 118
are identically absent because no local coefficient matrix has a
support-perfect-matching.  The remaining excluded slot,
`(m,L)=(5,{3,4,5,6})`, is structurally possible but cancels identically; the
script verifies that multivariate polynomial identity exactly using SymPy.
Every one of the 126 retained slots has a stored nonzero exact integer
evaluation, proving that it is not an identically zero template.  This gives
an exhaustive canonical 126-template map for every `D(n,k)` and exactly
explains the count reported in Remark 1.2.  Since Remark 1.2 publishes no
template list, literal item-by-item comparison with the authors' hidden list
is impossible from the available source; the identification rests on the
same stated method and the exact matching count.

## What is and is not certified

`template_manifest.json` lists all 126 template IDs `(m,L)`, their exact
nonzero witnesses, all 119 excluded slots and their reasons.  The script also
evaluates every retained template at 25 fixed positive integer root vectors
(3,150 exact evaluations) and finds no negative value.  This is finite exact
evidence only.  It does not show that every coefficient polynomial
`Psi_m(L)` is nonnegative for all positive real roots.  Establishing those 126
universal inequalities (or finding a negative one) is the remaining decisive
test for this route.

Reproduce from the project root with:

`python3 evidence/reconstruct_126.py --output evidence/template_manifest.json`

At this checkpoint the manifest SHA-256 is
`927f4bc2b877ef7cec7e4ce4c62582523368e5e6a102642ab7eec860ac7ae3e3`.
