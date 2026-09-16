# Precise problem reading

## Frozen target

Determine the single integer
\[
c_{1,\infty}(C_4\mathbin{\square}C_4).
\]
The original wording and frozen lead remain verbatim in `source.md`; this file only makes its mathematical reading explicit.

## Graph

Let \(\mathbb Z_4=\mathbb Z/4\mathbb Z\).  The finite, undirected, simple graph
\(G=C_4\square C_4\) has vertex set \(V(G)=\mathbb Z_4^2\).  Distinct vertices
\((x,y)\) and \((x',y')\) are adjacent exactly when either

- \(x'=x\pm1\pmod 4\) and \(y'=y\), or
- \(x'=x\) and \(y'=y\pm1\pmod 4\).

Thus \(|V(G)|=16\), every vertex has four distinct neighbors, and both coordinates wrap around.  In the computational encoding, \((x,y)\) is vertex \(4x+y\), for \(x,y\in\{0,1,2,3\}\).

## Game convention and quantifiers

For an integer \(k\ge 0\), the game with \(k\) cops is a perfect-information game with these rules.

1. The cops first choose an ordered \(k\)-tuple of vertices.  Repeated positions are allowed.  The robber then chooses a vertex not occupied by a cop.  (Cop labels do not affect the game, so a sorted multiset is an equivalent state representation.)
2. Each round consists of a simultaneous cop move followed, if capture has not occurred, by a robber move.  On a cop move, each cop independently stays put or moves across one edge.  Cop collisions and swaps are allowed.
3. If a cop's new vertex is the robber's current vertex, capture is immediate and there is no robber move that round.
4. Otherwise, writing \(S\) for the set of vertices occupied after the simultaneous cop move, the robber may end at any vertex in the connected component of \(G-S\) containing his current vertex.  Equivalently, he may stay or traverse an arbitrary finite path all of whose vertices, including both endpoints, avoid \(S\).  Vacated cop vertices may be used; only the cops' positions after their move block this robber move.
5. The cops have a winning strategy if they force capture after finitely many cop moves, for every legal initial robber choice and every sequence of legal robber moves.  Otherwise the robber wins by evading forever.

Then \(c_{1,\infty}(G)\) is the least \(k\) for which the cops have a winning strategy.  The required result must therefore prove both: a winning strategy for some \(k\), and a robber strategy against \(k-1\) cops.

## Scope and boundary checks

- The target is only the \(4\times4\) torus, not an assertion for all even \(m\), an asymptotic claim, or a claim about the planar grid \(P_4\square P_4\).
- “Path” is used only through reachability in \(G-S\), so allowing a finite walk instead gives the same legal endpoints.
- Capture during the cops' turn is evaluated before the robber obtains his unbounded-speed move.
- The convention agrees with Kinnersley--Townsend's placement and round order and with their definition of an infinite-speed cop-free path.

## Prior results and source status

The nearest inspected primary result is William B. Kinnersley and Nikolas Townsend, “Catching an infinitely fast robber on a grid,” *Discrete Applied Mathematics* 320 (2022), 446--461, [arXiv:2107.14193v2](https://arxiv.org/abs/2107.14193), DOI 10.1016/j.dam.2022.06.022.  The rules appear on PDF pp. 1--2, and Theorem 2.7 on PDF p. 8 proves
\[
2n-24\le c_\infty(C_n\square C_n)\le 2n\qquad(n\ge18).
\]
It does not cover \(n=4\).

Arindam Biswas, “Fast robbers on abelian Cayley graphs and digraphs,” [arXiv:2608.30474v1](https://arxiv.org/abs/2608.30474v1), Section 5.2 (PDF p. 15), restates this torus result and gives the product-sweeping upper bound \(c_{1,\infty}(C_m^{\square k})\le2m^{k-1}\) for \(m\ge4\); for the present cell it yields the non-exact bound \(c_{1,\infty}(C_4\square C_4)\le8\).

Exact-assertion and equivalent-language web searches performed on 2026-09-07 found no primary paper stating the \(C_4\square C_4\) value.  This is not proof of novelty or open status.  The source status is therefore **status-uncertain** (a newly isolated finite atlas question), while its suitability for exact research is high.

## Triage target

- **Nearest prior result:** the bounds above, with no inspected exact \(n=4\) value.
- **Proposed delta:** determine the exact \(C_4\square C_4\) value under the frozen convention.
- **Verification route:** a complete finite reachability-game attractor, together with a replayable four-cop policy and a closed robber-response certificate for three cops, checked by an implementation independent of the search code.

The preliminary exact attractor in `evidence/triage_attractor.py` reports that no configuration of one, two, or three cops wins initially, while every four-cop configuration wins, with all legal four-cop states entering the attractor within four iterations.  This is a computational observation for admission, not yet an independently audited resolution.
