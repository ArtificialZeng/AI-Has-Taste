# Log-concavity of the lower-mode forcing polynomial

Proposed subsidiary theorem for review. The full original Conjecture 3.3
and its j=2 restriction remain unresolved here. This is a research argument
and certificate dossier, not an accepted manuscript.

Use the definitions of A and B in `problem.md`. All Newton expansions use
binom(x,r), with coefficients extended by zero outside r>=0.
For every integer k>=4 define

\[
\begin{aligned}
R_k(x)={}&(x-k+2)A_{k-1,1}(x)
 +\tfrac12(x-k+3)(x-k+2)A_{k-2,0}(x)\\
 &+(x+1)(x-k+3)A_{k-2,1}(x)\\
 &+\tfrac12(x+1)(x-k+4)(x-k+3)A_{k-3,0}(x),
\qquad R_k(x)=\sum_{r\ge0}\rho_{k,r}\binom xr.
\end{aligned}
\]

**Theorem submitted for review.** For every k>=4, rho_{k,r} is positive
exactly when k-2<=r<=2k-1, vanishes otherwise, and satisfies

\[
\rho_{k,r}^2\ge \rho_{k,r-1}\rho_{k,r+1}\qquad(r\ge0).
\]

The family is the four lower-mode terms in equation (5.2) of Bérczi–Fehér,
[arXiv:2605.25271v1](https://arxiv.org/html/2605.25271v1). That equation is

\[
\Delta A_{k,2}(x)=(x+1)A_{k-1,2}(x)+R_k(x).
\tag{1}
\]

It follows by comparing coefficients in
E_d(T,u)=(T+d)E_{d-1}(T+u,u), where
E_d(T,u)=prod_{i=0}^d(T+i+(d-i)u), and then extracting [u^2](1-u).
For k=4 the term A_{3,2}, interpreted by coefficient extraction, is zero
by palindromicity. The definition of R_k above uses only admissible modes.
The exact primary HTML is frozen in `evidence/external/2605.25271v1.html`.

## Permutation basis and support

Let D(N,K) count permutations of N letters with no fixed points and N-K
cycles, and let D(0,0)=1. It is zero outside the natural range. Deleting
a distinguished letter from a cycle of length at least three, or deleting
its transposition, gives

\[
D(N,K)=(N-1)(D(N-1,K-1)+D(N-2,K-1)). \tag{2}
\]

For K>=1 its positive support is exactly [K+1,2K]: a permutation with
c=N-K cycles needs N>=2c and c>=1; conversely take c-1 transpositions
and one cycle of length 2K-N+2.

Put S_h(x)=A_{h,0}(x). Expanding a permutation by its nonfixed support
and applying Pascal's identity yields

\[
S_h(x)=\sum_r(D(r,h)+D(r+1,h))\binom xr. \tag{3}
\]

The product's rising-factorial expansion, or equation (3.3) of the
primary source, gives

\[
A_{n,1}(x)=x(x+2-n)S_{n-1}(x)-(n+1)S_n(x). \tag{4}
\]

For completeness, the rising-factorial identity is
E_d(T,u)=(1-u)^{d+1}((T+du)/(1-u))^{overline{d+1}}.
Expand in powers of T and extract [u](1-u) to obtain (4) for all integer
d>=0 and hence as a polynomial identity.

Equations (2)--(4) also give the source's explicit j=1 formula

\[
\begin{aligned}
B_{n,1,r}={}&r(r+2-n)D(r+1,n-1)+r(3r+2-3n)D(r,n-1)\\
&+(3r^2-3nr-2r+n+1)D(r-1,n-1)\\
&+(r-1)(r-n-1)D(r-2,n-1).
\end{aligned}\tag{5}
\]

Each coefficient is nonnegative whenever its D factor is nonzero.
For the third one write r=n+1+t: it becomes
2n+2+(3n+4)t+3t^2. The others are immediate from r>=n-1,n,n+2,
respectively. Formula (5) proves strict support [n-1,2n] for n>=2:
the first term covers n-1<=r<=2n-3; the second, third and fourth cover
r=2n-2, 2n-1 and 2n, respectively. At those last three indices their
coefficients are (2n-2)(3n-4), 6(n-1)^2 and (2n-1)(n-1), all positive.
Equation (3) gives strict support [h,2h] for S_h, h>=1.

Multiplication by x-c sends Newton coefficients a_r to
(r-c)a_r+r a_{r-1}. If a_r>0 exactly on [I,M] and c<=I, it produces
strict support [I,M+1] for c<I and [I+1,M+1] for c=I.
Applying this observation to the four summands defining R_k gives,
in their displayed order, the strict supports

\[
[k-1,2k-1],\quad[k-1,2k-2],\quad[k-2,2k-2],\quad[k-2,2k-3].
\]

All four summands have nonnegative Newton coefficients. Their union is
[k-2,2k-1], proving the stated positivity and no-internal-zero property.

## A finite polynomial certificate valid for all k

Fix K=k-3>=1 and write D_i=D(r+i,K). Equations (2)--(4), together with
the Newton multiplication rule, express the residual as

\[
2\rho_{k,r}=\sum_{i=-5}^{1}p_i(k,r)D_i. \tag{6}
\]

All seven explicit degree-four polynomials p_i are serialized under
`twice_residual_expansion` in `evidence/j2-residual-symbolic.json`.
Here is a compact reproducible specification independent of that list.
Let F_t(c_1,...,c_m;r) be the formal Newton coefficient at r of
prod(x+c_i) S_{K+t}(x), reduced by (2) to the basis D(N,K).
For m=0 start from D(r,K+t)+D(r+1,K+t) and reduce t times.
For m>0 use

\[
F_t(c_1,...,c_m;r)=(r+c_m)F_t(c_1,...,c_{m-1};r)
 +rF_t(c_1,...,c_{m-1};r-1).
\]

Then the formal expression on the right of (6) is exactly

\[
\begin{aligned}
&2F_1(2-k,0,3-k;r)-2kF_2(2-k;r)+F_1(3-k,2-k;r)\\
&\quad+2F_0(1,3-k,0,4-k;r)-2(k-1)F_1(1,3-k;r)
 +F_0(1,4-k,3-k;r).
\end{aligned}\tag{7}
\]

This follows by substituting (4) directly into the four defining terms.
It proves degree(p_i)<=4: each reduction or linear multiplication adds
at most one to total degree, and the scalar k factors are included.
The generator separately derives (6) from (1) and the j=2 Stirling
formula, and checks equality with (7).

Let L=rho_{k,r}^2-rho_{k,r-1}rho_{k,r+1}. Expanding (6) gives
4L=sum q_{a,b}(k,r)D_aD_b, with unordered pairs a<=b in

\[
\mathcal P=\{\operatorname{sort}(a,b):-5\le a,b\le1\}
\cup\{\operatorname{sort}(a-1,b+1):-5\le a,b\le1\}.
\]

There are exactly 41 pairs. This definition includes every term from
both products, with no support-dependent deletion of coefficients.
For each trace S=a+b, order its pairs from the center outward. If
U_i=D_{a_i}D_{b_i} and U_{t+1}=0, put

\[
W_i(k,r)=\tfrac14\sum_{j\le i}q_{a_j,b_j}(k,r).
\]

We have U_i>=U_{i+1}. Indeed P_K(t)=sum_N D(N,K)t^N satisfies
P_K=t^2((1+t)P_{K-1})', P_0=1. Induction and Rolle's theorem give only
real nonpositive roots. Newton's inequalities and the interval support
then give D(p,K)D(q,K)>=D(p-1,K)D(q+1,K) for p<=q, and iteration proves
the required comparison. These are also Lemma 5.3 and its proof in the
primary source.

Abel summation now gives the exact identity

\[
L=\sum_S\sum_i W_i(k,r)(U_i-U_{i+1}). \tag{8}
\]

Whenever U_i-U_{i+1}>0, both factors of U_i are positive. Thus
X=r+a_i-(k-2)>=0 and Y=2k-6-(r+b_i)>=0. Solving gives

\[
k=X+Y+b_i-a_i+4,\qquad r=2X+Y+b_i-2a_i+2. \tag{9}
\]

The certificate lists all 41 polynomials W_i after (9), by full
monomial/coefficient arrays. They have 1,506 strictly positive
coefficients in total, no negative coefficients, and no zero prefix
polynomials. Therefore each W_i is nonnegative on every active support
point. Equation (8) proves L>=0 for all k>=4 and all integer r>=0.
This includes k=4 (K=1); no large-k assumption or finite-range inference
is made.

### Exact verification of the finite algebra

`evidence/j2_residual_symbolic.py` generates (6)--(9) in SymPy over exact
rational polynomials. `evidence/verify_residual_certificate.py` uses only
the standard library and imports none of the generator's functions.
It regenerates (7) numerically using integer arithmetic and verifies
every serialized prefix on the 9-by-9 tensor grid 0<=X,Y<=8.

This is an identity certificate, not extrapolation: the degree bound
above makes both actual and reported W separately degree<=8 in X,Y.
A polynomial with those bounds vanishing at all 81 grid points is
identically zero, by two applications of univariate interpolation.
The verifier checks the degree bounds on every reported monomial,
the completeness and uniqueness of all 41 pairs, and nonnegativity of
every coefficient. There are 3,321 exact identity comparisons.

As an additional implementation check, it compares the residual
expansion, support, and quadratic values with 1,073 Newton entries
formed from the defining-product data for 4<=k<=32, 0<=r<=2k.
The report is `evidence/residual-certificate-verification.json`.
These finite checks supplement the polynomial proof; they are not its
infinite-range justification. Both implementations were run in the
same research context, and this is not a fresh referee acceptance.

## Precise remaining induction kernel

Let a_r=B_{k-1,2,r} and g_r=(r+1)a_r+r a_{r-1}. Equation (1) says
B_{k,2,r+1}=g_r+rho_{k,r}. If a is nonnegative and log-concave with
interval support, then g is too. To see this for r>=1, expand its minor
and group it as

\[
\begin{aligned}
g_r^2-g_{r-1}g_{r+1}={}&
(r+1)^2a_r^2-r(r+2)a_{r-1}a_{r+1}\\
&+r(r+1)a_{r-1}a_r-(r-1)(r+2)a_{r-2}a_{r+1}\\
&+r^2a_{r-1}^2-(r^2-1)a_{r-2}a_r.
\end{aligned}
\]

The three lines are at least a_r^2, 2a_{r-1}a_r, and a_{r-1}^2,
respectively, by strong log-concavity of a. At r=0 the assertion is
immediate. The multiplication rule gives interval support.

Consequently the following single sufficient assertion, still unproved,
would complete the j=2 induction:

\[
2g_r\rho_{k,r}-g_{r-1}\rho_{k,r+1}-g_{r+1}\rho_{k,r-1}\ge0
\quad(k\ge5,r\ge0). \tag{10}
\]

The k=4 case follows from R_4=Delta A_{4,2} and A_{3,2}=0.
Adding the two individual minors and (10) gives the desired next minor.
We assert only sufficiency, not equivalence of (10) to the original.

The former direct expansion of the entire B minor at common defect k-3
cannot be certified by requiring each trace to be nonnegative: at k=8,
r=10 the trace -7 equals -1196776183680, whereas the full minor is
23405794555448176. Its separate exact product/cycle-type verification is
`evidence/j2-defect3-witness-verification.json`. The associated probe
tests all requested 5<=k<=32 and finds 348 negative active prefixes.
This is a counterexample only to the specified intermediate assertion.

**Gap list for the submitted residual theorem:** none known; the finite
symbolic algebra and the contribution's value still require fresh review.
**Gap for the j=2 conjecture:** inequality (10), or a different proof.
**Gap for the frozen original:** all j>=2 remain unsettled by this result.
No manuscript or PDF is proposed before mathematical acceptance.
