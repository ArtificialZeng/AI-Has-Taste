# win-00068-p04 — Normalized inverse-weight LLY Ricci flow on the weighted triangle

## Frozen source statement

Let `C3` have vertices `v_1,v_2,v_3` and edges `e_12,e_23,e_31`. Give the edges positive lengths

`w=(w_12,w_23,w_31) in Delta_3 := {w_e>0 : w_12+w_23+w_31=1}`,

and let `d_w` be the induced shortest-path metric on the vertices. For a vertex `x`, set

`D_x(w) = sum_(e incident to x) 1/w_e`.

For `alpha in [0,1)`, define the inverse-weight lazy measure

`m_x^alpha(x)=alpha`,

`m_x^alpha(z)=(1-alpha) w_xz^(-1)/D_x(w)` for `z adjacent to x`,

and zero elsewhere. Let `W_1` be the 1-Wasserstein distance for the cost metric `d_w`. For an edge `e=xy`, define its Lin–Lu–Yau curvature, whenever the finite limit exists, by

`kappa_e(w) = lim_(alpha -> 1-) [1-W_1(m_x^alpha,m_y^alpha)/w_e]/(1-alpha)`.

Define

`K(w)=sum_(f in E(C3)) w_f kappa_f(w)`

and specialize the normalized inverse-weight flow of arXiv:2609.04671 to `C3`:

`dot w_e = -w_e (kappa_e(w)-K(w)),     w(0)=w^0 in Delta_3`.

Determine the exact maximal dynamics produced by these definitions. First determine the full subset of `Delta_3` on which every `kappa_e` is finite and the displayed vector field defines a classical flow, including what happens when an edge is tied with or longer than the alternate two-edge path. Prove whether the well-posed region is forward invariant and whether a trajectory can reach a nondifferentiability or non-finiteness locus in finite time.

On every well-posed component, derive the exact (possibly piecewise-defined) curvature vector and vector field, and then do one of the following:

1. classify every maximal trajectory, all equilibria and invariant strata, all boundary-degeneration regimes, and every omega-limit set; or
2. give a rigorous exact counterexample to a proposed universal classification or convergence assertion, specifying the initial weights and proving the claimed behavior.

For a global forward trajectory `w(t)`, its omega-limit set is

`omega(w)={w* in closed(Delta_3) : w(t_j)->w* for some sequence t_j->infinity}`.

No target limit is built into the problem. In particular, do not assume that all trajectories exist globally, that the equal-weight point is the unique equilibrium, or that every trajectory converges to it.

## Exactness and audit requirements

Compute the three Wasserstein problems from their primal transport LPs or Kantorovich duals and justify every change of optimal basis. Partition the normalized weight simplex into all required shortest-path and transport cells, including equality walls. Symbolic rational formulas, exact inequalities, interval-certified arguments, or equivalent proof objects are required for decisive claims. Floating-point phase portraits and sampled trajectories are exploratory evidence only.

Do not import Proposition 2.1's tree curvature formula, the edge-Laplacian heat equation, the tree Gauss–Bonnet identity, or the tree convergence theorems into `C3` without a new derivation: those statements are proved in the source for finite trees, whereas `C3` has a cycle. Any claimed ODE solution must be checked against the original Wasserstein definition on its entire asserted cell. A counterexample based only on numerical integration is not accepted.

The audit package must state the domain of each formula, verify preservation of `sum_e w_e=1`, distinguish an actual boundary limit from finite-time loss of well-posedness, and supply a replayable exact script or compact certificate for every computationally obtained cell or example.

## Source and contribution boundary

Primary source: Shuliang Bai and Bobo Hua, *Curvature Diffusion of Inverse-weight Lin–Lu–Yau Ricci Flow on Finite Trees*, arXiv:2609.04671v1: <https://arxiv.org/abs/2609.04671>. The inverse-weight measures, LLY curvature, normalized simplex, normalized flow, and omega-limit notation are given in Section 2, equations (2.1), (2.2), (2.5)–(2.8). The introduction states that the behavior of this inverse-weight flow on graphs with cycles remains open.

The source's proved formulas and convergence results concern trees. This project takes only the definitions and specializes them to the smallest simple cycle, `C3`. It asks for a complete exact triangle analysis or a rigorous counterexample; it does not claim a theorem for arbitrary cyclic graphs and does not presuppose equal-weight convergence.
