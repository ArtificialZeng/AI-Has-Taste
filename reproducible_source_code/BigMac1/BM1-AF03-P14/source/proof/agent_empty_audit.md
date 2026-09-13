# Independent exact audit: empty high-pair chamber

## Audited endpoint

The only real full-support critical direction of the central-section volume of
\(Q_5\) in the positive ordered closure of the empty high-pair chamber is the
diagonal direction.  Explicitly, if

\[
 a_0\ge a_1\ge a_2\ge a_3\ge a_4>0,
 \qquad a_i+a_j\le T:=\frac12\sum_{i=0}^4a_i
 \quad(0\le i<j\le4),
\]

and the direction is critical, then

\[
 a_0=a_1=a_2=a_3=a_4.
\]

The exact serialized certificate is
`results/empty_highpair_classification_certificate.json`.  It covers weak pair
inequalities, hence every full-support pair wall and intersection incident to
this chamber.  It does not cover a zero-coordinate support boundary or a
chamber containing a strictly high pair.

## Independent symmetric reconstruction

No numerical roots or discovery output enter the verifier.  Put

\[
 p_j=\sum_{i=0}^4a_i^j,\qquad S=p_2.
\]

The empty-chamber box-spline numerator expands exactly as

\[
 P=\frac38p_1^4-3p_1^2p_2+3p_2^2+4p_1p_3-4p_4. \tag{1}
\]

The no-import verifier reconstructs both sides: its first side is the original
formula

\[
 T^4-\sum_i(T-a_i)^4+\sum_{i<j}(T-a_i-a_j)^4,
 \qquad T=p_1/2,
\]

in five independent variables.  Singular verifies its identity with (1), so
the power-sum form is not trusted as input.

For a placeholder \(X\), define

\[
\begin{aligned}
 C_0&=\frac32p_1^3-6p_1p_2+4p_3,\\
 C_1&=-6p_1^2+12p_2,\\
 q(X)&=-16SX^4+12p_1SX^3+(C_1S+P)X^2+C_0SX-SP.
\end{aligned} \tag{2}
\]

Direct differentiation of (1) gives

\[
 P_i=C_0+C_1a_i+12p_1a_i^2-16a_i^3.
\]

Consequently the full-support critical polynomial

\[
 G_i=a_iSP_i+(a_i^2-S)P
\]

is exactly \(q(a_i)\).  The verifier checks all five identities in the
independent-variable ring.  Since \(S>0\), (2) has degree four.  Hence every
coordinate of a critical point is a positive root of one common nonzero
quartic, and a critical direction has at most four distinct coordinate
values.  This is the symmetry decomposition used below.

For the rest of the proof scale by \(p_1=2\).  Pair walls are then
\(a_i+a_j=1\).  The empty ordered cone reduces to the single largest-pair
condition \(a_0+a_1\le1\).

## One and two distinct values

The one-value direction is diagonal.  It is critical by permutation symmetry
and homogeneity; the verifier also substitutes an equal-coordinate point into
(2) and obtains zero.

For two values, let \(r>1\) be the larger value after scaling the smaller to
one, and let its multiplicity be \(m\).  The empty-pair condition gives

\[
\begin{array}{c|c}
m&\text{allowed range}\\ \hline
1&1<r\le2\\
2&1<r\le3/2\\
3&1<r\le2\\
4&1<r<\infty.
\end{array}
\]

Because both values are roots of \(q\), the exact divided difference
\((q(r)-q(1))/(r-1)\) must vanish.  Reconstruction from (1)--(2) gives

\[
\begin{array}{c|c}
m& (q(r)-q(1))/(r-1)\\ \hline
1&\frac{15}{8}r^4(r-3)\\
2&\frac58(16r^5-48r^4+40r^3-8r^2-9r+3)\\
3&\frac58(3r^5-9r^4-8r^3+40r^2-48r+16)\\
4&\frac{15}{8}(1-3r).
\end{array} \tag{3}
\]

The first and fourth rows are visibly nonzero.  A rational Sturm computation
gives zero roots on \([1,3/2]\) for the second-row quintic and zero roots on
\([1,2]\) for the third-row quintic.  The verifier rebuilds the Sturm chains
using only `fractions.Fraction`; it imports neither SymPy nor a project module.
Thus no non-diagonal two-value point occurs in this chamber closure.

## Three distinct values

Write the three values as \(x>y>z>0\), with multiplicities
\((m,n,k)\), where \(m+n+k=5\).  There are exactly six ordered compositions:

\[
 (1,1,3),(1,2,2),(1,3,1),(2,1,2),(2,2,1),(3,1,1).
\]

Set

\[
 z=\frac{2-mx-ny}{k},
\]

substitute the corresponding moments in (1)--(2), and form

\[
 R(u,v)=\frac{q(u)-q(v)}{u-v}.
\]

No actual division is used in the certificate: \(R\) is rebuilt from

\[
\begin{aligned}
R(u,v)={}&-16S(u^3+u^2v+uv^2+v^3)
 +24S(u^2+uv+v^2)\\
& +(C_1S+P)(u+v)+C_0S.
\end{aligned} \tag{4}
\]

The necessary equations are \(f=R(x,y)=0\) and \(g=R(y,z)=0\), up to the
positive rational primitive scales recorded in the certificate.  The verifier
recomputes each resultant \(\operatorname{Res}_y(f,g)\) exactly.  With factor
names expanded below, the six factorizations are

\[
\begin{array}{c|l}
(m,n,k)&\operatorname{Res}_y(f,g)/\text{nonzero constant}\\ \hline
(1,1,3)&x^4(2x-1)^8(7x-2)A_4A_8\\
(1,2,2)&x^4B_4^2C_4^2B_5\\
(1,3,1)&x^4(2x-1)^4A_4A_5A_8\\
(2,1,2)&(2x-1)^8(7x-2)D_8E_8\\
(2,2,1)&(2x-1)^4B_5D_8E_8\\
(3,1,1)&(2x-1)^{12}(7x-2)F_2^2F_4^2.
\end{array} \tag{5}
\]

All ten named integer polynomials, their exponents, primitive scales, and the
six resultant constants are serialized.  Singular checks (5) as polynomial
identities, rather than comparing textual CAS output.

The order and chamber inequalities sharply constrain the largest value.  Its
mean is \(2/5\), so \(x>2/5\).  If \(m\ge2\), the largest pair gives
\(x\le1/2\).  If \(m=1\), then \(x+y\le1\), while

\[
2=x+ny+kz<x+4y
\]

gives \(y>(2-x)/4\), hence \(x<2/3\).  Therefore

\[
 \frac25<x<\frac23\quad(m=1),
 \qquad
 \frac25<x\le\frac12\quad(m\ge2). \tag{6}
\]

Exact Sturm counts applied to the factors in (5) leave only these branches:

\[
\begin{array}{c|c}
(1,1,3)&x=1/2\\
(1,2,2)&B_4=0\text{ or }B_5=0\\
(1,3,1)&x=1/2\text{ or }A_5=0\\
(2,1,2),(2,2,1),(3,1,1)&x=1/2.
\end{array} \tag{7}
\]

The verifier then recomputes the branch ideals and proves mutual containment
with the following Gröbner bases:

\[
\begin{array}{c|l}
(1,1,3),\ x=1/2& y^2,\ 2x-1\\
(1,3,1),\ x=1/2&2y-1,\ 2x-1\\
(2,1,2),\ x=1/2&y^2,\ 2x-1\\
(2,2,1),\ x=1/2&2y-1,\ 2x-1\\
(3,1,1),\ x=1/2&y^2(2y-1),\ 2x-1.
\end{array}
\]

These force \(y=0\) or \(y=x\), contradicting positivity or three
distinct ordered values.  In the \((1,2,2)\), \(B_5\) branch the basis contains
\(3x+2y-2\), which together with \(z=1-x/2-y\) gives \(z=x\).  In the
\((1,3,1)\), \(A_5\) branch it contains \(2x+3y-2\), which together with
\(z=2-x-3y\) again gives \(z=x\).

It remains to exclude the \((1,2,2)\), \(B_4\) branch.  The exact branch
basis is

\[
 B_4(x),\qquad
 \mathcal R(x,y)=88y^2+(44x-88)y-3x^3+26x^2-40x+24. \tag{8}
\]

Sturm's theorem gives exactly one root of \(B_4\) in \((2/5,2/3)\), and
exactly one root in the smaller interval

\[
 \frac{59}{100}<x<\frac35. \tag{9}
\]

The vertex of the quadratic in (8) is \((2-x)/4\).  Since
\(z=1-x/2-y\), order \(y>z\) selects the upper root of (8).  At the empty
boundary \(y=1-x\),

\[
 \mathcal R(x,1-x)=-3x^3+70x^2-84x+24=:W(x). \tag{10}
\]

On (9), \(W''(x)=140-18x>0\), while

\[
 W'(3/5)=-81/25<0,
 \qquad W(59/100)=-1809137/10^6<0.
\]

Thus \(W'<0\) and \(W<0\) throughout (9).  The point \(1-x\) lies strictly
between the two roots of the upward quadratic (8), so its upper root satisfies
\(y>1-x\).  This contradicts the empty-pair inequality \(x+y\le1\).  Every
three-value branch is excluded.

## Four distinct values

Four distinct coordinate values are the four distinct positive roots of the
quartic (2).  Exactly one of them is duplicated among the five coordinates.
Vieta gives the sum of the four roots as

\[
 -\frac{12p_1S}{-16S}=\frac34p_1=\frac32.
\]

Since the five coordinates sum to two, the duplicated value is \(1/2\).
Write the other three values as \(x,y,z>0\), so \(x+y+z=1\), and set

\[
 u=xy+xz+yz,\qquad w=xyz.
\]

The verifier reconstructs the moments of
\((1/2,1/2,x,y,z)\) and checks the exact identities

\[
 \frac{P}{16}-\frac w2=\frac{(4u-1)^2}{64}, \tag{11}
\]

\[
 \frac{C_0}{16}-\left(w+\frac u2\right)
 =\frac{4u-4w-1}{16}. \tag{12}
\]

The constant and linear coefficients of the monic form of (2) say that the
left sides of (11) and (12) vanish.  Equation (11) yields \(u=1/4\), and then
(12) yields \(w=0\), contradicting \(xyz>0\).  Thus four distinct coordinate
values are impossible.

Together with the degree-four bound, the one-, two-, three-, and four-value
arguments exhaust every full-support critical point.  The unique orbit is the
diagonal orbit.

## Closure and wall coverage

The proof uses weak order and weak low-pair inequalities, so it includes:

- positive coordinate-equality faces;
- any pair wall incident to the empty chamber;
- all full-support intersections of these walls.

There is no positive singleton/polygon wall in this closure: from
\(a_0+a_1\le T\) and \(a_1>0\), one gets \(a_0<T\).

Across a pair wall the neighboring polynomial numerators differ by
\(2L^4\), where \(L=T-a_i-a_j\).  Values and first derivatives agree at
\(L=0\) (indeed the global formula is \(C^3\)).  Hence a full-support local
extremum on such a wall must satisfy the same critical equations, and the
empty-side reconstruction is a valid necessary condition there.

Not covered are \(a_4=0\), any lower-support stratum, or a sign chamber with a
strictly high pair.

## Certificate and independent verifier

Files:

- `results/empty_highpair_classification_certificate.json`
- `src/verify_empty_highpair_classification.py`
- `tests/test_empty_highpair_verifier.py`

Reproduction:

```bash
python src/verify_empty_highpair_classification.py \
  results/empty_highpair_classification_certificate.json
python tests/test_empty_highpair_verifier.py
```

Observed output:

```text
PASS: empty-chamber classification, exact resultants, branches, and Sturm counts verified
PASS: valid certificate accepted; 8 corruptions rejected
```

The verifier uses only the Python standard library and a fresh Singular
process.  It imports no discovery output or project source.  It rejects unknown
or missing fields, changed chamber endpoints, factor coefficients, resultants,
multiplicities, branch bases, Sturm counts, expression-injection attempts,
missing Singular, CAS errors, timeouts, and missing or duplicate success
sentinels.

No Lean, Coq, Isabelle, or other proof assistant was used.  The formal endpoint
is exactly the full-support positive ordered closure of the empty high-pair
chamber described above.

SHA-256 at this audit milestone:

```text
3d5c97a23ad36956387e4ddbdaca0f74720953f34a59af422ed15944b23e1e6a  results/empty_highpair_classification_certificate.json
c9cf895a80dee3e64b67e8c7d370928c7767f5235245be2b2b949f828d249ea0  src/verify_empty_highpair_classification.py
15bfa3bbb663ea76f6f708f7b942cd26e2761a8e5ed43b76f5397ea35d0a27f0  tests/test_empty_highpair_verifier.py
```
