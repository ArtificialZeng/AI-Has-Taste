# Research proof dossier: the four-edge zero-free disk

Proposer: `primary-20260914-matching-mgf-zero-free-research-551b3f76b932`.
Status: complete proposed argument, submitted for a fresh mathematical audit.
This is research evidence, not a publication manuscript or an acceptance report.

## Exact scope

For integers m,n >= 4, let C_{4,m,n} be the minimum cost of a four-edge
matching in K_{m,n}, with independent rate-one exponential edge costs.
The proposed theorem is that

\[
F_{4,m,n}(t)=\mathbb E e^{tC_{4,m,n}}\ne0\qquad (|t|<mn/4).
\]

More precisely, the sextic P below has no root in |t| <= mn/4 for every
real m,n >= 4. Consequently the reduced numerator of the rational continuation
of F_{4,m,n} has no root in that closed disk. A pole is not asserted to be
a finite nonzero value. In particular, t=mn/4 remains a pole.

This proves the k=4 restriction of the frozen original if accepted. It does
not prove the all-k conjecture or a Gaussian limit as the matching size grows.

## Dependencies and the rational identity

The probabilistic dependency is Wästlund, arXiv:2602.07563v1, Sections 2.1–2.3
and Theorem 8, equation (9) with its separate d=0 rule; see the copied primary
PDF `external/2602.07563v1.pdf`, printed pages 7–8 and 23. The stability
dependency is the classical real Routh–Hurwitz criterion: a real degree-d
polynomial with positive leading coefficient is strictly stable (all roots
have negative real part) if its d leading Hurwitz determinants are positive.
An inspected primary proof is [Olga Holtz, *Hermite-Biehler, Routh-Hurwitz,
and total positivity*, Theorem 3 and its proof, page 3](https://arxiv.org/pdf/math/0512591).
The convention reconciliation for that source is given below.

Define

\[
A=mn(m-1)(m-2)(m-3)(n-1)(n-2)(n-3),
\quad
Q(t)=\prod_{\substack{i,j\ge0\\i+j<4}}
       ((m-i)(n-j)-(4-i-j)t).
\]

Put s=m+n and r=mn. The numerator is P(t)=sum_{a=0}^6 p_a t^a, with

\[
\begin{aligned}
p_0={}&r^3(r-s+1)^2(r-2s+4),\\
p_1={}&-r^2(r-s+1)(12s^2-25sr-28s+10r^2+37r+12),\\
p_2={}&r(40r^3-117sr^2+97s^2r-22s^3+129r^2-179sr
          +44s^2+75r-16s-8),\\
p_3={}&12s^3-107s^2r+187sr^2+117sr+4s-82r^3-145r^2-58r-8,\\
p_4={}&42s^2-143sr-2s+91r^2+47r+8,\\
p_5={}&42s-52r+10,\qquad p_6=12.
\end{aligned}
\]

The exact rational identity obtained from the source recurrence is

\[
F_{4,m,n}(t)=\frac{A P(t)}{Q(t)}.\tag{1}
\]

Here is a finite algebraic construction of (1), specifying all recursion
indices and boundary conditions. Set L_{i,j}=F^{(i-j)}_{i,m,n-4+i},
0 <= j <= i <= 4, and L_{0,0}=1. Let N_i=n-4+i. For j<i,

\[
L_{i,j}=\frac{N_i L_{i-1,j}
 +(m-j)(i-j+1)t L_{i,j-1}
 +(m-j)N_i L_{i-1,j-1}}
 {(m-j)N_i-(i-j)t},\tag{2}
\]

where terms with out-of-range indices are zero. On the diagonal use

\[
L_{i,i}=\frac{t}{N_i}L_{i,i-1}+L_{i-1,i-1}.\tag{3}
\]

Computing in increasing i and then increasing j gives L_{4,4}=AP/Q.
Thus there are 15 cells including the base case. In this parameter domain
N_i>=1, and m-j>=1 whenever j<i, including at m=4. In particular (3)
does not divide by m-i at the possibly exceptional diagonal i=m=4.

Both implementations listed below verify this identity exactly. The second
uses a polynomial numerator for each cell with denominator equal to the
product of factors D_{a,b}=(m-b)(n-4+a)-(a-b)t over
1<=a<=i and 0<=b<=min(j,a-1). Ratios between these denominators are literal
products of missing factors. It clears (2) and uses exact division by N_i
in (3), requiring zero remainders, then divides the final numerator by the
eight linear factors of A, again requiring zero remainders. This yields the
displayed P. This calculation is in Z[m,n,t], not at sampled parameter values.
The coefficient list in `research-k4-certificate.json` gives the same P in
expanded m,n coordinates. The degree is exactly six since p_6=12.

## An explicit positivity certificate

Let R=mn/4 and define a polynomial by clearing the substitution denominator:

\[
H(z)=\frac{4^6}{(mn)^3}(1+z)^6
 P\left(R\frac{1-z}{1+z}\right)
 =h_0 z^6+h_1 z^5+\cdots+h_6.\tag{4}
\]

Set x=m-4, y=n-4, and v(u)=(1,u,u^2,u^3)^T. All seven coefficients have
the form h_a=v(x)^T B_a v(y). The matrices B_a, in increasing a, are:

```text
B0 = [[20519424,21197056,7200000,806400],
      [21197056,21858816,7416032,829920],
      [7200000,7416032,2514760,281400],
      [806400,829920,281400,31500]]
B1 = [[33546240,38182912,14102784,1701120],
      [38182912,43108608,15818560,1897792],
      [14102784,15818560,5775296,690080],
      [1701120,1897792,690080,82200]]
B2 = [[22417920,27708672,11058688,1434368],
      [27708672,34036992,13489952,1737504],
      [11058688,13489952,5309384,679384],
      [1434368,1737504,679384,86420]]
B3 = [[7274496,10035200,4387328,616960],
      [10035200,13540864,5832576,810880],
      [4387328,5832576,2482112,341504],
      [616960,810880,341504,46544]]
B4 = [[1101312,1815296,907520,142336],
      [1815296,2783232,1329440,202272],
      [907520,1329440,616280,91752],
      [142336,202272,91752,13428]]
B5 = [[73728,147456,89344,16640],
      [147456,268544,147776,25408],
      [89344,147776,75904,12384],
      [16640,25408,12384,1944]]
B6 = [[1536,3840,3072,768],
      [3840,8448,5856,1248],
      [3072,5856,3480,648],
      [768,1248,648,108]]
```

Form the Hurwitz matrix

\[
\mathcal H=\begin{pmatrix}
h_1&h_3&h_5&0&0&0\\
h_0&h_2&h_4&h_6&0&0\\
0&h_1&h_3&h_5&0&0\\
0&h_0&h_2&h_4&h_6&0\\
0&0&h_1&h_3&h_5&0\\
0&0&h_0&h_2&h_4&h_6
\end{pmatrix}
\]

and let Delta_j be its leading j by j determinant. Direct exact expansion
gives the following certificate. In each row the support is the **entire**
rectangle 0<=a,b<=3j of monomials x^a y^b, with no missing entries.

| j | Degree in each variable | Coefficient count | Least coefficient |
|---|---|---|---|
| 1 | 3 | 16 | 82200 |
| 2 | 6 | 49 | 5637588000 |
| 3 | 9 | 100 | 176698647552000 |
| 4 | 12 | 169 | 1539481522876416000 |
| 5 | 15 | 256 | 2195347272420556800000 |
| 6 | 18 | 361 | 237097505421420134400000 |

The complete integer coefficient lists, rather than only these summary
statistics, are in `research-k4-certificate.json`. Each entry [a,b,c] encodes
c*x^a*y^b, with c an exact decimal integer string. They are obtained by the
determinant formula sum over permutations of sign(sigma) times the product
of the selected matrix entries. The separate checker uses recursive Laplace
expansion, compares every coefficient, and verifies the full support rectangles.
The last-column expansion also gives Delta_6=h_6 Delta_5, independently
checked in both implementations.

For all x,y>=0, these expansions imply h_0>0 and Delta_j>0 for j=1,...,6.
The constant terms are included and strictly positive, so the inference also
holds on x=0 or y=0 and at their intersection. The real Routh–Hurwitz criterion
therefore shows that H has all six roots in Re(z)<0.

For direct alignment with Holtz's ascending-coefficient convention, apply her
criterion to f(w)=w^6 H(1/w)=h_0+h_1 w+...+h_6 w^6. The first seven
leading minors of her infinite Hurwitz matrix are h_0, h_0 Delta_1, ...,
h_0 Delta_6, which are positive. Thus f is stable. Since h_0,h_6>0,
inversion bijects its roots with those of H and preserves the sign of the
real part. This supplies precisely the stability statement used here.

## From stability to the zero-free disk

For |t|<=R, t != -R, set z=(R-t)/(R+t). Then

\[
\operatorname{Re}z=\frac{R^2-|t|^2}{|R+t|^2}\ge0,
\qquad 1+z=\frac{2R}{R+t}\ne0.
\]

Equation (4) and strict stability give P(t) != 0. At the omitted point,
the leading coefficient in (4) is

\[
h_0=\frac{4^6}{(mn)^3}P(-R)>0,
\]

so P(-R) != 0 as well. This proves the asserted closed-disk statement for
P for every real m,n>=4.

For completeness, all the zeros of Q are positive real numbers
rho_{ij}=(m-i)(n-j)/(4-i-j). Since m,n>=4 and i+j<4,

\[
\frac{(m-i)(n-j)}{mn}
 =\left(1-\frac{i}{m}\right)\left(1-\frac{j}{n}\right)
 \ge\left(1-\frac{i}{4}\right)\left(1-\frac{j}{4}\right)
 \ge1-\frac{i+j}{4}.
\]

Thus rho_{ij}>=mn/4 and Q has no root in the open disk. Also A>0.
Equation (1) therefore gives F_{4,m,n}(t) != 0 throughout that disk.
At any parameter specialization, cancelling a common factor of P and Q
can only remove roots from P; it cannot create new roots. Since P has no
roots on the closed disk, this proves the reduced-numerator assertion too.
The (i,j)=(0,0) factor of Q vanishes at t=R and P(R)>0, so t=R is a pole.

The expectation itself is analytic in |t|<R. One direct justification for the
required exponential moments is as follows. A k-edge matching can be sampled
uniformly from all such matchings, independently of the costs, and each edge
belongs to it with probability k/(mn). For every fixed cost array, the minimum
matching cost is at most that average matching cost, namely k/(mn) times the
sum of all mn costs. Hence E exp(a C_{4,m,n}) is finite for 0<=a<R, using
the exponential moment formula for the sum of independent Exp(1) variables.
Domination by exp(a C) on compact subsets proves analyticity there. The
source rational identity agrees with this expectation, rather than merely
with a formal expression. This completes the proposed proof.

## Reproduction, limitations, and gap list

Run from the project root:

```sh
python3 evidence/research_k4_certificate.py
python3 evidence/verify_k4_certificate.py
```

The first program reconstructs (1) in a rational function field using SymPy
1.14.0, checks normalization, transpose symmetry and equation (10) of the
primary source, and saves all coefficient arrays. It compares with the
triage reconstruction as a calibration. The second program imports only the
Python standard library and independently reconstructs (1), (4), and the six
determinants with sparse integer polynomial arithmetic. Its result is
`research-k4-verification.json`. No floating-point computation is decisive.
The proof covers an infinite parameter domain because positivity is proved
coefficient by coefficient for a fixed finite collection of polynomials.

Known mathematical gaps in the stated k=4 argument: **none identified by the
proposer**. Its algebraic certificates, invocation of the primary recursion,
and contribution remain subject to a fresh referee audit. The two arithmetic
implementations were prepared in the same research context; they are not a
substitute for that audit. No all-k claim or unconditional novelty claim is
made. Current primary-source comparison and its limits are recorded in
`../literature/research-validation.md`.
