# Precise problem statement

## Frozen claim and domain

Let \(G=(V,E)\) be an arbitrary finite, simple, undirected, connected graph with
\(|V|\ge 2\). The question is whether
\[
  2b(G)-2\le \gamma_R(G)                                      \tag{1}
\]
holds for every such \(G\). Equivalently, because both parameters are integers,
\[
  b(G)\le \left\lfloor\frac{\gamma_R(G)}2\right\rfloor+1.     \tag{2}
\]
The universal quantifier ranges over all graph orders, not merely the finite
datasets described by the machine source.

## Definitions and convention

Write \(d_G(u,v)\) for graph distance and
\(N_r[x]=\{v\in V:d_G(v,x)\le r\}\). Under the standard simultaneous-spread
burning convention, one new, previously unburned source is selected in each
round and fire already present spreads one edge per subsequent round. The
burning number \(b(G)\) is the least positive integer \(k\) for which there are
vertices \(x_1,\ldots,x_k\) satisfying
\[
 V=\bigcup_{i=1}^k N_{k-i}[x_i],\qquad
 d_G(x_i,x_j)\ge j-i\quad(1\le i<j\le k).                    \tag{3}
\]
The distance condition encodes that the source chosen in round \(j\) has not
burned earlier. This is the convention required by the frozen source.

A Roman dominating function (RDF) is a function
\(f:V\to\{0,1,2\}\) such that every vertex assigned \(0\) has a neighbor
assigned \(2\). Its weight is \(w(f)=\sum_{v\in V}f(v)\), and
\[
 \gamma_R(G)=\min\{w(f):f\text{ is an RDF on }G\}.             \tag{4}
\]

Disconnected graphs, the one-vertex graph, directed/weighted graphs, burning
variants, and weak, perfect, total, double, or other Roman-domination variants
are outside scope. A counterexample must include an exact graph6 string or edge
list and independently justified upper and lower bounds for both optima; a
finite search with no counterexample is not a proof.

## Intake status and nearest prior material

The source is a machine-generated survivor, not a verified open problem.
AutoGraphForge (arXiv:2609.03478v1, retrieved 2026-09-07) states in Section
3.4.1 that its static data include every connected graph of orders \(2\) through
\(9\), and explicitly warns in Sections 3.4 and 4.2 that survival of finite
refutation is not a universal theorem. The exact survivor is located by the
frozen source at repository commit
`2bbf36e92328295976b1cd62b2a5e15f9a628e41`; the cited local source assets are
not present in this project checkout.

Direct searches on 2026-09-07 for the exact inequality and for papers jointly
mentioning graph burning and Roman domination found no primary publication of
(1). This establishes only `status-uncertain`, not openness or novelty. The
closest inspected foundations were Bessy--Bonato--Janssen--Rautenbach,
*Bounds on the Burning Number* (arXiv:1511.06023, definition in the abstract),
and Cockayne--Dreyer--Hedetniemi--Hedetniemi, *Roman domination in graphs*,
Discrete Mathematics 278 (2004), 11--22,
doi:10.1016/j.disc.2003.06.004 (RDF definition and minimum weight).

## Proposed contribution and verification route

Nearest prior result: the standard metric characterization (3) and the
standard RDF formulation (4). Proposed delta: resolve their machine-generated
cross-parameter inequality (1), with equality cases if a proof naturally gives
them. Verification route: exact enumeration can decisively find and certify a
counterexample, while a proof should convert the parts
\(V_i=f^{-1}(i)\) of a minimum RDF into a burning sequence of length at most
\(|V_2|+\lfloor |V_1|/2\rfloor+1\), or identify precisely why this natural
stronger construction fails.

As a cheap boundary check, \(K_2\) has \(b=2\) and \(\gamma_R=2\), so (1) is
tight. The exhaustive triage script in `evidence/triage_atlas_check.py` found
no counterexample among the 995 connected unlabeled graphs of orders 2 through
7; this is exact finite evidence only.
