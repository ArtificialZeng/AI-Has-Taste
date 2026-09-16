# Precise reading and triage of the weighted-triangle problem

This file interprets the immutable statement in `source.md`; it does not replace
or correct that statement. Write

\[
a=w_{12},\qquad b=w_{23},\qquad c=w_{31},\qquad
\Delta_3=\{(a,b,c)\in\mathbb R_{>0}^3:a+b+c=1\}.
\]

## Definitions and conventions

The graph is the simple labelled triangle with vertex set
\(\{v_1,v_2,v_3\}\). The cost between vertices is the shortest-path metric,
so, for example,

\[
d_w(v_1,v_2)=\min\{a,b+c\}=\min\{a,1-a\},
\]

with the other two formulas obtained cyclically. At the endpoints of
\(e_{12}\),

\[
D_{v_1}=a^{-1}+c^{-1},\qquad D_{v_2}=a^{-1}+b^{-1},
\]

and cyclic analogues hold. For every \(w\in\Delta_3\) and
\(\alpha\in[0,1)\), the masses displayed in `source.md` are probability
measures on the three vertices.

For probability measures \(\mu,\nu\) on the vertices, the intended transport
quantity is the primal linear program

\[
W_1(\mu,\nu)=\min_{\pi_{ij}\geq0}
\sum_{i,j=1}^3 d_w(v_i,v_j)\pi_{ij},\quad
\sum_j\pi_{ij}=\mu(v_i),\quad \sum_i\pi_{ij}=\nu(v_j).
\]

For an edge \(e=xy\), the frozen problem literally defines

\[
\kappa^{\mathrm{lit}}_e(w)=\lim_{\varepsilon\downarrow0}
\frac{1-W_1(m_x^{1-\varepsilon},m_y^{1-\varepsilon})/w_e}{\varepsilon},
\]

provided this limit is a finite real number. No extended-real value is called
a curvature. This denominator is part of the frozen question.

The standard weighted-graph Ollivier/LLY normalization instead divides by
\(d_w(x,y)\). Hence \(\kappa^{\mathrm{lit}}_e\) agrees with that curvature only
when \(w_e=d_w(x,y)\). Conclusions about the literal quotient outside that
region must be labelled a project-defined no-surgery extension and not
attributed to the primary paper.

## Domain split forced by the constant term

Let

\[
\mathcal G=\{w\in\Delta_3:a\leq\tfrac12,
b\leq\tfrac12,c\leq\tfrac12\},\qquad
\mathcal G^\circ=\{w\in\Delta_3:\max(a,b,c)<\tfrac12\}.
\]

Thus \(\mathcal G\) is exactly the region where all three edges are geodesic;
its three equality walls have one coordinate equal to \(1/2\). The connected
open set \(\mathcal G^\circ\) is the strict-triangle region. If, for example,
\(a>1/2\), then weak convergence of the lazy measures and continuity of
finite-space \(W_1\) give

\[
W_1(m_{v_1}^{1-\varepsilon},m_{v_2}^{1-\varepsilon})
\longrightarrow d_w(v_1,v_2)=1-a<a.
\]

Consequently the numerator has positive constant term \((2a-1)/a\), and the
literal quotient tends to \(+\infty\). Cyclically, every curvature can be
finite only on \(\mathcal G\). On a geodesic edge the constant term vanishes;
finiteness there still has to be established from the exact parametric
transport LP, including at ties. This is the first research task, not an
assumption.

Whenever all three curvatures are finite, set

\[
K(w)=a\kappa_{12}(w)+b\kappa_{23}(w)+c\kappa_{31}(w),\qquad
F_e(w)=-w_e(\kappa_e(w)-K(w)).
\]

A classical forward solution from \(w^0\) means a \(C^1\) map
\(w:[0,T)\to\Delta_3\) with \(w(0)=w^0\), all three curvatures finite at every
time, and \(\dot w(t)=F(w(t))\) for every \(t<T\). It is maximal if it has no
extension with these properties. Existence and uniqueness at transport-cell
walls, and whether equality-wall data admit a classical forward solution, are
claims to prove rather than conventions. The identity \(\sum_eF_e=0\), when
\(F\) exists, must be checked explicitly.

## Quantified target and scope

Using exact primal or dual certificates, partition \(\mathcal G\) into all
shortest-path and optimal-transport cells (including every equality wall) and
give the formula and validity inequalities for each \(\kappa_e\) and \(F_e\).
Determine exactly the initial set \(\mathcal W\subseteq\Delta_3\) for which a
unique classical forward solution exists. For every \(w^0\in\mathcal W\),
determine its maximal interval, whether it can meet a transport
nondifferentiability wall or \(\Delta_3\setminus\mathcal G\) in finite time,
and whether the appropriate well-posed component is forward invariant.

Then either (i) for every such initial datum classify the maximal trajectory,
all equilibria and invariant strata, all approaches to the closed-simplex
boundary, and--only for solutions defined on \([0,\infty)\)--the omega-limit set
defined in `source.md`; or (ii) provide one exact initial datum and proof that
refutes a specifically stated universal classification or convergence claim.
No general cyclic-graph theorem is requested. Tree curvature, Gauss--Bonnet,
heat-equation, and convergence results are unavailable unless rederived here.

## Nearest prior results and proposed contribution

Literature was checked on 2026-09-07. Bai and Hua,
*Curvature Diffusion of Inverse-weight Lin--Lu--Yau Ricci Flow on Finite Trees*,
[arXiv:2609.04671v1](https://arxiv.org/abs/2609.04671), restrict Section 2 and
its formulas to finite trees (definitions (2.1), (2.2), (2.5)--(2.8), PDF
pp. 3--4) and state in the introduction (PDF p. 1) that behavior of this
inverse-weight flow on graphs with cycles remains open. Bai--Lin--Lu--Wang--Yau,
*Ollivier Ricci-flow on weighted graphs*,
[arXiv:2010.01802](https://arxiv.org/abs/2010.01802) (published in *American
Journal of Mathematics* 146 (2024), 1723--1747), is the nearest general-graph
result: its Definition 3 normalizes curvature by the induced distance
\(d_w(x,y)\), and its Section 3 proves existence/uniqueness for that flow. It
does not settle the frozen literal \(/w_e\) model on non-geodesic triangle
edges or give the requested exact triangle dynamics.

Searches for the exact title language, “inverse-weight Lin--Lu--Yau Ricci flow”
with “triangle” or “C3”, and the literal assertion located no primary paper
giving this classification. This is a limited search finding, not proof of
novelty or open status. Source status is therefore **open-supported for cyclic
inverse-weight behavior, but status-uncertain for this exact triangle
specialization**.

Triage target: nearest prior result = the general distance-normalized flow and
the tree inverse-weight formulas above; proposed delta = a complete exact
three-vertex transport-cell and maximal-dynamics classification for the frozen
model (or an exact counterexample to a named universal subclaim); verification
route = three symbolic parametric transport LPs, cyclic symmetry, exact cell
inequalities, and direct ODE/invariance arguments. The cheapest decisive next
test is to solve the \(e_{12}\) LP with \(\varepsilon=1-\alpha\) on
\(a<1/2\) and \(a=1/2\), obtain dual certificates for every basis change, and
cycle the result before analyzing the ODE.
