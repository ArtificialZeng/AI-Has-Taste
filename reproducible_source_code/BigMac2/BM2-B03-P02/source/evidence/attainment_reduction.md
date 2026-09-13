# Exact finite reduction for three-point attainment

This note isolates the attainment issue in Assertion 1.  It is a theorem about
the frozen formulation; it does **not** prove the numerical bound
\(5E/8\).

Write \(\langle x,y\rangle_{\mathbb R}=\operatorname{Re}(x^*y)\) on
\(\mathbb C^2\), and, for a valid pair, write
\[
 X_{ij}=B_{ij},\qquad d_{ij}=|t_i-t_j|^2.
\]
For a valid set \(S\), let
\(K_S=\operatorname{conv}\{X_{ij}:i,j\in S,\ t_i\ne t_j\}\) and
\(\rho_S=\operatorname{dist}^2(0,K_S)\).

## Proposition (ten-triple attainment audit)

Fix a five-label moment system and a threshold \(R\ge0\).  There is an
admissible \(q\), supported on at most three labels, with \(C(q)\le R\) if
and only if at least one valid set \(S\), \(2\le |S|\le3\), satisfies one of
the following conditions.

1. \(\rho_S<R\).
2. \(\rho_S=R\), and the Euclidean projection of \(0\) onto \(K_S\) is
   realized: it is a vertex, is in the relative interior of a triangle from
   three distinct directions, or lies anywhere on the segment arising when
   two labels of \(S\) have the same direction.

Consequently, after the ten triples are inspected, failure of the literal
existential assertion has exactly two possible forms:

* the ordinary obstruction \(\min_S\rho_S>R\), which also violates the
  corresponding infimum inequality; or
* the attainment-only obstruction \(\min_S\rho_S=R\), with every minimizing
  triple having its unique projection in the relative interior of a
  nondegenerate edge and three pairwise distinct directions.

In particular, any proof of the closure inequality with a **strict** bound
\(\min_S\rho_S<R\) automatically proves the literal existential statement.
An attainment-only counterexample must solve exact equality conditions; a
floating-point value merely close to \(R\) cannot certify one.

## Exact face tests

For three distinct directions put
\(X=X_{ij},Y=X_{ik},Z=X_{jk}\).  Either all three coefficients coincide
(then the singleton is a realized pair coefficient), or they are pairwise
distinct and noncollinear over \(\mathbb R\).

For the edge \([X,Y]\), put
\[
 h=\|Y-X\|^2,\qquad
 \theta=-\frac{\langle X,Y-X\rangle_{\mathbb R}}{h},\qquad
 \delta=X+\theta(Y-X).
\]
It is the projection onto an open edge precisely when
\[
 0<\theta<1,qquad
 \langle\delta,Z-\delta\rangle_{\mathbb R}\ge0.
\]
Such a \(\delta\) is not attained by a selection on these three distinct
directions.  The other two edge tests are obtained cyclically.

For an interior projection, let \(D_1=Y-X,D_2=Z-X\), form the real Gram
matrix \(G=(\langle D_r,D_s\rangle_{\mathbb R})_{r,s=1}^2\), and solve
\[
 G\binom uv=-\binom{\langle X,D_1\rangle_{\mathbb R}}
                         {\langle X,D_2\rangle_{\mathbb R}}.
\]
The affine-plane projection is in the triangle interior exactly when
\(u>0,v>0,1-u-v>0\).  Its barycentric edge weights are
\((\alpha_{ij},\alpha_{ik},\alpha_{jk})=(1-u-v,u,v)\), and it is realized
by positive selection weights with
\[
 q_i:q_j:q_k=
 \alpha_{ij}\alpha_{ik}d_{jk}:
 \alpha_{ij}\alpha_{jk}d_{ik}:
 \alpha_{ik}\alpha_{jk}d_{ij}.
\]
A vertex \(X_{ij}\) is realized by any positive selection on \(\{i,j\}\).
If, for example, \(t_i=t_j\ne t_k\), every convex combination of
\(X_{ik}\) and \(X_{jk}\) is realized: choose \(q_k\in(0,1)\) and split
\(1-q_k\) between \(i,j\) in the desired edge-weight ratio.

## Proof

Lemma 7.2 identifies the regression coefficient \((a,b)\) with the convex
combination of pair coefficients having weights proportional to
\(q_iq_jd_{ij}\).  For three distinct directions, positive barycentric edge
weights are inverted by the displayed formula for \(q\); vertices come from
two-point supports.  No point in an open edge is realized, because two
positive incident edge weights and a zero third edge weight would require the
common label to have positive weight while both other labels have positive
weight, making the third product positive.  Conversely, approaching weight
one on the common label realizes every open-edge point as a limit.  When two
directions coincide, the omitted same-direction product permits the whole
remaining segment to be realized exactly.

The squared norm is strictly convex, so its projection onto each compact
\(K_S\) is unique.  If \(\rho_S<R\), realized interior points can approach a
nonattained boundary projection and remain below \(R\).  At equality, an
open-edge projection is the only point of \(K_S\) with norm at most
\(\sqrt R\), so equality is available exactly in the realized-face cases.
The projection formulas and inequalities are the standard real Gram/KKT
conditions.  This proves the audit and the two-way classification.

## Reproducible reconnaissance (not proof)

`evidence/explore_five.py` implements the Gram tests for five pairwise
distinct sampled directions.  With seed `20260906`, it accepted 199,953 of
200,000 generated balanced systems.  Its largest sampled closure optimum was
`0.26883261950789661 E`, attained at an interior triangle.  This narrow random
family is discovery-only and neither establishes exhaustive coverage nor a
universal bound.  Separate spot checks found global open-edge projections as
well, confirming that the second audit branch is genuinely needed even though
those sampled values were far below `5E/8`.
