# Precise reading: inverse-weight LLY flow on \(C_3\)

## Frozen source and notation

The immutable statement is `source.md`.  Label the vertices of the triangle
\(1,2,3\), and put
\[
 a=w_{23},\qquad b=w_{31},\qquad c=w_{12}.
\]
The open and closed normalized simplices are
\[
 \Delta^\circ=\{(a,b,c)\in\mathbb R_{>0}^3:a+b+c=1\},\qquad
 \overline\Delta=\{(a,b,c)\in\mathbb R_{\ge0}^3:a+b+c=1\}.
\]
Every raw strictly positive initial triple is identified with its normalization
in \(\Delta^\circ\); common rescaling does not change the metric ratios,
transition probabilities, or curvature.

## Metric, transition kernel, and curvature

For \(w=(a,b,c)\in\mathbb R_{>0}^3\), the path metric is
\[
 d_w(2,3)=\min\{a,b+c\},\quad d_w(3,1)=\min\{b,c+a\},\quad
 d_w(1,2)=\min\{c,a+b\}.
\]
At a vertex \(x\), set \(D_x(w)=\sum_{z\sim x}w_{xz}^{-1}\).  For
\(0\leq\alpha<1\), the inverse-weight lazy measure is
\[
 m_x^\alpha(x)=\alpha,\qquad
 m_x^\alpha(z)=(1-\alpha)\frac{w_{xz}^{-1}}{D_x(w)}\quad(z\sim x),
\]
and is zero elsewhere.  For probability measures \(\mu,\nu\) on the three
vertices, \(W_{1,w}(\mu,\nu)\) is the minimum transport cost with cost metric
\(d_w\).  For an edge \(e=xy\), define
\[
 \kappa_e(w)=\lim_{\alpha\uparrow1}
 \frac{1-W_{1,w}(m_x^\alpha,m_y^\alpha)/d_w(x,y)}{1-\alpha}.
\]
Thus the denominator is the endpoint distance \(d_w(x,y)\), as in the
general weighted-graph LLY definition.  The tree paper writes \(w_e\) there
because every tree edge is geodesic.  Reading that denominator literally as
\(w_e\) on all positive triples of \(C_3\) would make the displayed limit
diverge whenever \(w_e>d_w(x,y)\), so it is incompatible with the source's
quantifier over every positive triple.

## Normalized flow and requested quantifiers

Put
\[
 K(w)=\sum_{e\in\{a,b,c\}}w_e\kappa_e(w),\qquad
 \dot w_e=-w_e\bigl(\kappa_e(w)-K(w)\bigr).                 \tag{RF}
\]
The problem asks for the following statements, with no genericity assumption:

1. For every \(w^0\in\Delta^\circ\), first prove that (RF) has a unique
   solution \(w(t;w^0)\in\Delta^\circ\) for every \(t\ge0\), including through
   the walls \(a=b+c\), \(b=c+a\), and \(c=a+b\).
2. Determine exactly
   \[
   \omega(w^0)=\{q\in\overline\Delta:\exists\ t_n\to\infty,
   \ w(t_n;w^0)\to q\}
   \]
   for every \(w^0\in\Delta^\circ\).
3. In particular, prove or disprove the universal assertion
   \(\lim_{t\to\infty}w(t;w^0)=(1/3,1/3,1/3)\).
4. Classify all interior fixed points, equivalently all
   \(w\in\Delta^\circ\) satisfying
   \(\kappa_a(w)=\kappa_b(w)=\kappa_c(w)\).  Symmetry immediately makes the
   uniform point an interior fixed point, but does not prove uniqueness or
   attraction.
5. Classify every possible boundary degeneration of an interior trajectory:
   its limiting support, limiting ratios when defined, rates needed to
   distinguish different approaches to the same face, and whether the omega
   set is a point or a larger connected set.

## Boundary-scope caveat

The inverse-weight measures and LLY quotient are defined only for positive
weights; at a zero edge the transition rule is singular and the path distance
may be a pseudometric.  Consequently, the phrase "invariant faces" does not by
itself define a boundary ODE.  The source-intrinsic, well-defined request is to
classify faces reached by omega limits of interior solutions.  A literal face
may be called invariant only after proving that the interior vector field in
(RF) has a unique continuous (or explicitly specified stratified/blow-up)
extension to its relative interior.  If the limit depends on approach ratios,
that dependence is part of the boundary-degeneration classification and no
canonical invariant-face claim is to be made.

## Nearest primary results and status (checked 2026-09-07)

- Bai--Hua, arXiv:2609.04671v1, Sections 1--2 and Theorems 1.1--1.3,
  <https://arxiv.org/abs/2609.04671>, defines the inverse-weight tree model,
  normalized flow, and omega limits, and explicitly says behavior on graphs
  with cycles remains open.  The inspected local PDF has SHA-256
  `95a760c9bb4a955fd669ff14a95d140bf7d3e3b19b779055707ae57cec750fa5`.
- Bai--Lin--Lu--Wang--Yau, *Ollivier Ricci-flow on weighted graphs*,
  arXiv:2010.01802v9, Definition 3 and equation (4),
  <https://arxiv.org/abs/2010.01802>, supplies the general-graph
  \(d_w(x,y)\)-denominator and normalized-flow convention.  Its stated
  long-time theorem assumes every edge remains a shortest route, so it does
  not settle the present all-positive-triples problem.
- Bai, arXiv:2607.14748v1, Section 6,
  <https://arxiv.org/abs/2607.14748>, computes static \(C_3\) curvature for the
  **uniform-neighbor** kernel.  That adjacent model is not the inverse-weight
  flow except at the uniform metric and does not settle this question.

Source status is open-supported at the family level (cycles), while priority
for this exact \(C_3\) phase portrait remains unverified: the bounded exact and
equivalent-language searches found no primary treatment, which is not a claim
of novelty.

## Triage target

Nearest prior result X: the tree convergence/diffusion results above, together
with the general weighted-graph definition.  Proposed delta Y: a complete
piecewise-exact phase portrait of (RF) on \(\Delta^\circ\), including global
existence, all fixed points, every omega limit, and approach-sensitive boundary
behavior.  Verification route Z: derive the three curvatures by exact
Kantorovich primal/dual certificates in each shortest-path chamber, verify the
formulas and wall matching symbolically, and then prove the planar ODE phase
portrait with exact sign or Lyapunov arguments.  Floating trajectories may
guide but cannot certify the result.
