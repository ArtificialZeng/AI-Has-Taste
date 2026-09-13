# Exact closure of the ordered `star1` chamber

## 1. Scope and result

This note independently closes the full ordered closure of the (Q_5)
high-pair chamber

\[
N=\{(0,1)\},\qquad a_0\ge a_1\ge a_2\ge a_3\ge a_4>0.
\]

The normalization is (a_4=1).  All computations below are over
\(\mathbb Q\), except for the final explicitly isolated quadratic root.  The
result is:

\[
\boxed{
\text{The ordered `star1` closure has exactly one critical orbit: }
(\alpha,\alpha,1,1,1),\quad
\alpha={24+\sqrt {69}\over13}.}
\]

It lies in the strict pair chamber (although on coordinate-order walls caused
by repeated coordinates), and its tangent Hessian has signature
\((-,-,-,+)\).  Hence it is a saddle, and this chamber contains no local
extremum: its sole critical point is non-diagonal and indefinite.

No floating-point root or discovery output is used in the certificate or its
verifier.

## 2. Exact chamber chart and all walls

Use ordered gaps

\[
x=a_0-a_1,quad y=a_1-a_2,quad z=a_2-a_3,quad w=a_3-a_4,quad a_4=1.
\]

Thus

\[
(a_0,a_1,a_2,a_3,a_4)
=(1+w+z+y+x,\ 1+w+z+y,\ 1+w+z,\ 1+w,\ 1).
\]

Put

\[
y={1-x-z\over2}+u.
\]

Writing a positive margin for the high pair (01), and positive margins for
all the other low pairs, gives exactly

\[
\begin{array}{c|c@{\qquad}c|c}
01&2u&02&1-x-z\\
03&1-x+z&04&1+2w-x+z\\
12&1+x-z&13&1+x+z\\
14&1+2w+x+z&23&2(u+1)\\
24&2(u+w+1)&34&2(u+w+z+1).
\end{array}
\]

Consequently the entire ordered closure is precisely

\[
\boxed{x,z,w,u\ge0,\qquad x+z\le1.}\tag{2.1}
\]

Indeed, the first two displayed margins give (u\ge0) and (x+z\le1),
and every remaining margin is nonnegative on that simplex.  Conversely these
conditions imply (y=(1-x-z)/2+u\ge0), hence ordering.  The balance margins
are automatically strict; for example

\[
\sum_i a_i-2a_0=3+2w-x+z\ge2.
\]

Thus there is no hidden dominant-coordinate stratum.  The subset-sum wall
(01) is (u=0); the first low-pair wall is (x+z=1), with further low-pair
equalities only at its endpoints and their compatible intersections.  The
chart also retains all coordinate-order walls (x=0,z=0,w=0) (and the
possible (y=0) intersection).

## 3. Critical equations from the subset-sum formula

Let

\[
T={1\over2}\sum_i a_i,qquad S=\sum_i a_i^2,qquad D=\prod_i a_i.
\]

The paired truncated-power numerator in this chamber is reconstructed as

\[
P=T^4-\sum_i(T-a_i)^4
  +\sum_{i<j}(T-a_i-a_j)^4-2(T-a_0-a_1)^4,\tag{3.1}
\]

and the section volume is (F=\sqrt S,P/(24D)).  For any gap variable
(q\in\{x,y,z,w\}), direct differentiation gives

\[
\partial_qF={H_q\over48\sqrt S D^2},\qquad
H_q=S_qPD+2SP_qD-2SPD_q.\tag{3.2}
\]

There is no division by (P) in (3.2).  Since (S,D>0), criticality is
equivalent to the four polynomial equations (H_q=0).

On a subset-sum wall an adjacent chamber changes (3.1) by a multiple of
(L^4), where (L=0) on the wall.  Its first three derivatives vanish there.
Thus (3.2) is the correct common first-derivative system throughout the
closure (2.1), not only in its strict interior.

## 4. Bernstein certificate forcing (x=z=0)

After substituting (y=(1-x-z)/2+u), form the exact combination

\[
K=-6H_x+7H_y-8H_z+4H_w.\tag{4.1}
\]

Its degree in (x,z) is nine.  In the degree-nine simplex Bernstein basis,

\[
K=\sum_{i,j\ge0,\ i+j\le9}
b_{ij}(u,w){9!\over i!j!(9-i-j)!}
x^iz^j(1-x-z)^{9-i-j}.\tag{4.2}
\]

Exact rational conversion proves:

* (b_{00}=0);
* every monomial coefficient of every other (b_{ij}(u,w)) is strictly
  positive;
* in particular all 54 nonzero (b_{ij}) have a strictly positive constant
  coefficient.

The serialized table has 55 rows and 1620 positive parameter monomials (plus
the canonical zero entry for (b_{00})).  Its canonical row digest is

```text
d47de13461dbd9d8d06ff8a896b0986ede3410a448f1da3722a74250610015b3
```

The independent verifier reconstructs (4.1) from (3.1)--(3.2), reconstructs
the right side of (4.2) from all serialized rational coefficients, and checks
the polynomial identity exactly.

On (2.1), every Bernstein basis function is nonnegative and every parameter
coefficient above is positive.  If (x>0), the term with ((i,j)=(9,0)) is
strictly positive; if (z>0), the term ((0,9)) is strictly positive.
Therefore

\[
K=0\quad\Longleftrightarrow\quad x=z=0.
\]

Since a critical point makes every (H_q), and hence (K), zero, every
critical point in the whole closure satisfies

\[
\boxed{x=z=0.}\tag{4.3}
\]

## 5. Radical decomposition on the remaining face

At (x=z=0), two necessary critical equations factor as

\[
H_x={(w+1)^2(2u+2w+3)\over16}A,qquad
H_z=-{(w+1)(2u+2w+3)\over16}B,
\]

where the displayed prefactors are strictly positive for (u,w\ge0), and

\[
\begin{aligned}
A={}&128u^2w^3+384u^2w^2+416u^2w+156u^2\\
&-128uw^4-384uw^3-512uw^2-360uw-108u\\
&-64w^4-192w^3-268w^2-180w-45,
\end{aligned}\tag{5.1}
\]

\[
\begin{aligned}
B={}&128u^3w^3+384u^3w^2+352u^3w+104u^3\\
&-256u^2w^4-832u^2w^3-1120u^2w^2-784u^2w-228u^2\\
&+128uw^5+384uw^4+576uw^3+588uw^2+336uw+78u\\
&+64w^5+224w^4+420w^3+458w^2+240w+45.
\end{aligned}\tag{5.2}
\]

The lexicographic Gröbner basis of (langle A,B\rangle\subset\mathbb Q[w,u])
is a graph over a square-free degree-15 polynomial in (u).  Factoring that
polynomial and reducing the graph relation modulo each factor gives the exact
radical decomposition

\[
\begin{aligned}
\langle A,B\rangle={}&
\langle4u^2+4u+3,\ 2w+2u+3\rangle\\
&\cap\langle52u^2-36u-15,\ w\rangle\\
&\cap\langle84u^2-52u+1,\ 3w+2\rangle\\
&\cap\langle32u^3+48u^2+32u+9,\ 2w+2u+3\rangle\\
&\cap\langle
1280u^6+3840u^5+6720u^4+7072u^3+5056u^2+2160u+525,\\
&\hspace{21mm}40w+640u^5+1920u^4+2960u^3+2736u^2+1488u+465
\rangle.
\end{aligned}\tag{5.3}
\]

All five (u)-polynomials in (5.3) are irreducible over (mathbb Q), their
degrees sum to 15, and their product is the square-free univariate Gröbner
basis element.  Hence (5.3) is an equality of radical ideals, not merely a
list of sampled solutions.

For comparison, eliminating (u) gives the independently checked identity

\[
\begin{aligned}
\operatorname{Res}_u(A,B)={}&1024w^2(3w+2)^2(2w^2+4w+3)
(32w^3+96w^2+104w+39)\\
&\cdot(10240w^6+61440w^5+158720w^4+225216w^3\\
&\hspace{33mm}+184192w^2+81840w+15345).
\end{aligned}\tag{5.4}
\]

The decomposition gives a particularly transparent exact real/order audit:

1. (4u^2+4u+3) has negative discriminant.
2. The third component forces (w=-2/3<0).
3. The fourth forces (2w+2u+3=0), impossible for (u,w\ge0).
4. Every coefficient of the sixth-degree polynomial in the fifth component
   is positive, so it cannot vanish for (u\ge0).
5. The remaining component is
   \(w=0, 52u^2-36u-15=0\).  This quadratic has exactly one positive root,
   \[
   u={9+2\sqrt{69}\over26}.
   \]

Substitution into all four original (H_q), followed by reduction modulo
(52u^2-36u-15), gives zero.  Thus no sufficiency was inferred merely from
the two necessary equations (5.1)--(5.2).

Since (x=z=w=0), the coordinates are

\[
(3/2+u,3/2+u,1,1,1)=(\alpha,\alpha,1,1,1),qquad
13\alpha^2-48\alpha+39=0.
\]

The selected root is isolated exactly by

\[
{12\over5}<\alpha<{5\over2}.
\]

Here the high margin is (2u>0) and the first low margin is (1), so the
point is on no subset-sum wall.  Equation (5.3) also proves there are no
critical points on the subset-sum boundary portions (u=0) or (x+z=1).

## 6. Exact Hessian audit

At a critical point, the tangent Hessian has the sign of the restriction of

\[
M_{ij}={\delta_{ij}\over S}-{2a_ia_j\over S^2}
+{P_{ij}\over P}-{P_iP_j\over P^2}+{\delta_{ij}\over a_i^2},\tag{6.1}
\]

because the omitted scalar factor (F) is positive.  The verifier rebuilds
(P,P_i,P_{ij}) from (3.1), not from serialized Hessian output.

Use the tangent vectors

\[
L=(1,-1,0,0,0),\quad
S_0=(0,0,1,-1,0),\quad
B_0=(3,3,-2\alpha,-2\alpha,-2\alpha).
\]

Reduction of the three quadratic forms modulo
(13\alpha^2-48\alpha+39) gives

\[
\begin{aligned}
L^TML&=-{4(17784\alpha+13597)\over864435}<0,\\
S_0^TMS_0&={4(416\alpha-1367)\over66495}<0,\\
B_0^TMB_0&={12(104\alpha-215)\over169}>0.
\end{aligned}\tag{6.2}
\]

The signs follow rationally from (12/5<\alpha<5/2).  The small-block
difference representation has dimension two under (S_2\times S_3); the
large-block and block-contrast representations each have dimension one.
Therefore the tangent signature is exactly

\[
\boxed{(-,-,-,+)},
\]

and the point is a saddle.

## 7. Certificate, independent verifier, and rejection tests

Artifacts:

* `certificates/star1_exact_certificate.json`: all 55 rational Bernstein
  rows, chamber margins, exact (A,B), resultant factors, radical components,
  survivor, and Hessian claims;
* `src/builder_build_star1_certificate.py`: exact certificate constructor;
* `src/builder_verify_star1.py`: fail-closed independent reconstruction and
  verifier; it imports no constructor or discovery file;
* `src/builder_test_star1_mutations.py`: nine rejection tests covering
  semantic chamber metadata, critical equations, Bernstein hash, a Bernstein
  coefficient with a refreshed hash, a radical component, the resultant, the
  survivor interval, a Hessian form, and deletion of a wall margin.

Reproduction (using an isolated SymPy environment) is:

```bash
uv run --with sympy python src/builder_build_star1_certificate.py \
  certificates/star1_exact_certificate.json
uv run --with sympy python src/builder_verify_star1.py \
  certificates/star1_exact_certificate.json
uv run --with sympy python src/builder_test_star1_mutations.py \
  src/builder_verify_star1.py certificates/star1_exact_certificate.json
```

The expected terminal lines are

```text
PASS: exact star1 closure has one critical orbit, ((24+sqrt(69))/13)^2,1^3, and its tangent Hessian is indefinite
PASS: all 9 mutations rejected
```

At the time of this report, the certificate SHA-256 is

```text
70cf7f980c89ff36e6b07ccecde268bcde6d8cf5f9da171759b5d8ba5c0e3fa7
```

This report closes only the ordered `star1` chamber (including its full
closure).  It makes no completeness claim about the other ordered chambers.
