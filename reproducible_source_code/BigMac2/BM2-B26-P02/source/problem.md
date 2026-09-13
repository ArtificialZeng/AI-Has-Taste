# Precise problem reading

## Objects and conventions

Let \(G=(V,E)\) be a finite, undirected, unweighted, loopless simple graph.
The quantified graphs satisfy

\[
|V|=8,\qquad G\text{ connected},\qquad G\text{ not a tree}.
\]

Because \(G\) is connected, “not a tree” is equivalent to containing a cycle,
or to \(|E|\ge 8\). A **genuine nonedge** is an unordered pair
\(\{u,v\}\subset V\) with \(u\ne v\) and \(\{u,v\}\notin E\). Write

\[
G+uv=(V,E\cup\{\{u,v\}\}).
\]

For a starting vertex \(s\in V\), let \((X_t)_{t\ge0}\) be discrete-time
simple random walk on the graph in question, with \(X_0=s\) and each next
vertex chosen uniformly from the current vertex's neighbours. Define

\[
\tau_{\rm cov}=\min\{t\ge0:\{X_0,\ldots,X_t\}=V\},\qquad
t_{\rm cov}(G,s)=\mathbb E_s[\tau_{\rm cov}].
\]

Thus the start is visited at time zero and time is counted in edge
transitions. The walks on \(G\) and \(G+uv\) use their respective degree
distributions. The start \(s\) may equal \(u\) or \(v\).

An exact computational definition is obtained by letting \(C_G(x,A)\) be the
expected additional time to visit all vertices when the current vertex is
\(x\in A\) and the already visited set is \(A\). Then

\[
C_G(x,V)=0,\qquad
C_G(x,A)=1+\frac1{d_G(x)}\sum_{y\sim_G x}C_G(y,A\cup\{y\}),
\]

and \(t_{\rm cov}(G,s)=C_G(s,\{s\})\). Solving the same-layer linear systems
over \(\mathbb Q\) makes all values and comparisons exact.

## Frozen quantified claim

The statement to decide is

\[
\forall G\;\forall\{u,v\}\;\forall s\in V(G),\qquad
\Delta_s(G;uv):=t_{\rm cov}(G+uv,s)-t_{\rm cov}(G,s)\ne0,
\]

where \(G\) ranges over the connected non-tree simple graphs on exactly eight
vertices and \(\{u,v\}\) ranges over its genuine nonedges. Its exact negation
is one marked instance \((G,u,v,s)\) with \(\Delta_s(G;uv)=0\).

It is enough to process one representative of every unlabelled graph
isomorphism class only if every nonedge and every start is processed, or if
any orbit reduction is itself certified. Nauty/Traces 2.9301 `geng` gives
11,117 connected order-eight classes: 23 have seven edges (and hence are
trees), leaving 11,094 connected non-tree classes. The complete graph is in
the latter inventory but contributes no marked instances because it has no
nonedge.

## Scope and success conditions

This is only the order-eight, fixed-start, unit-edge layer. It does not ask
about the maximum over starting vertices, variable edge conductance, trees,
other orders, the sign of \(\Delta_s\), or the unrestricted conjecture.

Disproof requires an explicit graph (for example, a labelled edge list), a
genuine nonedge \(uv\), a start \(s\), and independently checkable exact
rational values for both cover times. Proof requires exhaustive coverage of
all 11,094 graph classes, all relevant nonedges and starts, exact arithmetic,
a complete and hashed inventory, run metadata, and a structurally independent
verification route.

## Nearest prior result and triage status

Ian Meng Si, *Nonlocality of Cover-Time Changes Under Edge Addition*,
arXiv:2608.27474v1 (19 August 2026), was inspected at
https://arxiv.org/abs/2608.27474 on 2026-09-09. Conjecture 6.2 (PDF p. 24)
states fixed-start strict nonequality for every finite connected simple graph.
Recurrence (6.4) and Theorem 6.4 (PDF p. 25) report an exact census with no
fixed-start or worst-start equality through order seven, and no equality among
trees of orders eight and nine. Consequently, the present target is precisely
the connected non-tree order-eight layer omitted by that census.

The source supports the unrestricted problem as open, but this finite layer
was not separately certified as uncomputed. A bounded exact-phrase and
equivalent-language search on 2026-09-09 found no other source settling this
layer; that is a search limitation, not a priority or novelty proof.

**Target contribution:** nearest prior result = Si's order-at-most-seven and
order-eight/nine tree census; proposed delta = decide all connected non-tree
graphs of order eight for fixed starts; verification route = exhaustive
unlabelled inventory plus exact rational visited-set computation and an
independent exact verifier.
