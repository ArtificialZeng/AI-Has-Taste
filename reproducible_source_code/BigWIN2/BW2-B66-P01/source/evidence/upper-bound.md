# Structural upper-bound certificate

Let \(H=K_{1,3}\sqcup K_2\), and let \(G\) be a simple maximal planar
graph whose edges are coloured red and blue.  Write \(F_R,F_B\) for the
two spanning colour graphs.  This note proves the following exact-scope
partial result:

> If both \(F_R\) and \(F_B\) are \(H\)-free, then \(|V(G)|\le 20\).
> Consequently every such \(G\) on at least 21 vertices has a
> monochromatic copy of \(H\), so \(r_{\mathrm{MP}}(H,H)\le 21\).

This does not determine the least threshold.

## One-colour lemma

Recall that if an \(H\)-free graph \(F\) contains a claw \(C\), then
\(V(C)\) covers every edge of \(F\): an edge disjoint from the claw would
complete a copy of \(H\).

Let \(v\) have maximum degree \(d\ge3\) in an \(H\)-free graph \(F\).

1. If \(d=3\), the set \(S=\{v\}\cup N_F(v)\) has size four and covers
   every edge of \(F\), while \(\Delta(F)=3\).
2. If \(d=4\), every edge not incident with \(v\) has both endpoints in
   \(N_F(v)\).  Indeed, if such an edge has at most one endpoint in the
   four-element set \(N_F(v)\), three neighbours of \(v\) avoid both its
   endpoints and give a disjoint claw.  Thus every nonisolated vertex of
   \(F\) lies in the five-element set \(\{v\}\cup N_F(v)\).
3. If \(d\ge5\), every edge of \(F\) is incident with \(v\).  Otherwise
   at least three neighbours of \(v\) avoid the two endpoints of a
   nonincident edge, again producing \(H\).

## The four colour cases

A colour is type L if its maximum degree is at most two and type C
otherwise.

In case LL, each colour has at most \(n\) edges, whereas a maximal planar
graph has \(3n-6\) edges.  Hence LL is impossible for \(n\ge7\).

Consider the mixed case, say red is L and blue is C.  Apply the
one-colour lemma at a maximum-degree blue vertex \(v\).

- If \(d_B(v)=3\), the four-set \(S=\{v\}\cup N_B(v)\) covers all blue
  edges.  Every vertex outside \(S\) has degree at least three in \(G\)
  and red degree at most two, so it is incident with a blue edge meeting
  \(S\).  As every vertex of \(S\) has blue degree at most three, there
  are at most \(12\) such outside vertices.  Thus \(n\le4+12=16\).
- If \(d_B(v)=4\), every vertex outside the five-set
  \(\{v\}\cup N_B(v)\) is blue-isolated.  Such a vertex would have red
  degree at least three in \(G\), contrary to red being L.  Hence
  \(n\le5\).
- If \(d_B(v)\ge5\), every blue edge is incident with \(v\).  Therefore
  all edges of \(G-v\) are red.  Since
  \[
  e(G-v)=3n-6-d_G(v)\ge 2n-5,
  \]
  but a graph on \(n-1\) vertices of maximum degree at most two has at
  most \(n-1\) edges, this is impossible for \(n\ge5\).

The symmetric CL case has the same bound.

Finally suppose both colours are C.  Choose one claw in each colour and
let their four-vertex sets be \(S_R,S_B\); each is a vertex cover of its
colour graph.  Put \(S=S_R\cup S_B\), so \(|S|\le8\), and
\(T=V(G)\setminus S\).  There is no edge of \(G[T]\): a red edge there
would miss \(S_R\), and a blue edge would miss \(S_B\).  Thus every
vertex of \(T\) sends all of its at least three host edges to \(S\).
The simple planar bipartite graph consisting of the \(S\)-\(T\) edges
therefore satisfies
\[
3|T|\le e_G(S,T)\le2(|S|+|T|)-4.
\]
Consequently \(|T|\le2|S|-4\le12\) and
\(n=|S|+|T|\le20\).  All four cases are now covered, uniformly at every
order, proving the stated upper bound.

## Check of the paper's explicit MP constructions

The source PDF copied at `evidence/external/2609.05268.pdf` has SHA-256
`d2c05952bb165545210571a572678338e7766162141549adbf62411e3cf881b2`.
Its two Section 4.1 families do not avoid this \(H\):

- In Figure 7, \(B_p^{(1)}\) has rim-path vertices
  \(v_1,\ldots,v_{4p}\), all \(uv_i\) blue and all \(wv_i\) red.  For
  \(p\ge2\), take any path edge \(v_iv_{i+1}\).  If it is blue, use a
  blue claw centred at \(u\) with any three rim vertices outside its
  endpoints; if red, do the same at \(w\).  The chosen path edge is
  disjoint from that claw, so it gives a monochromatic \(H\).
- In Figure 8, \(B_p^{(2)}\) has all \(uv_i\) and \(wv_i\) blue.  For
  \(p\ge4\), the blue claw with centre \(u\) and leaves
  \(v_1,v_2,v_3\), together with the disjoint blue edge \(wv_4\), is an
  explicit \(H\).

The PDF's Definition 1 confirms the at-least-\(N\) convention.  Corollary
2 makes \(K_{1,3}\) alone unavoidable, not its disjoint union with an
edge.  Proposition 4 gives necessary forest/component/diameter conditions
that the present \(H\) satisfies.  Theorem 11 and Remark 5 concern
subgraphs of \(P_5\sqcup tK_2\); they do not contain \(H\), whose maximum
degree is three.  Section 5, Problem 2 asks for the complete disconnected
diagonal classification and does not state this singleton separately.

A limited arXiv title/formula search on 2026-09-07 found no separate
primary source resolving this exact singleton.  This is a search record,
not a priority claim.
