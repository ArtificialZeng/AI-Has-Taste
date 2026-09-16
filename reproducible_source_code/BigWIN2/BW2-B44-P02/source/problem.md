# Precise problem statement

## Frozen claim, interpreted

All graphs are finite, simple, and undirected.  For a graph \(G\), write
\(n=|V(G)|\),
\[
\delta(G)=\min_{v\in V(G)} d_G(v),\qquad
\operatorname{diam}(G)=\max_{u,v\in V(G)}d_G(u,v).
\]
Here distance is the number of edges in a shortest path.  “\(K_7\)-free”
means that \(G\) contains no copy of \(K_7\) as a (not necessarily induced)
subgraph, equivalently \(\omega(G)\le 6\).

The precise assertion is
\[
\forall\delta\in\mathbb Z,\ \delta\ge8,\quad
\exists C_\delta\in\mathbb R\quad
\forall\text{ finite simple connected }G,
\]
\[
\delta(G)\ge\delta\ \Longrightarrow\
\operatorname{diam}(G)\le {8|V(G)|\over3\delta}+C_\delta.
\]
The parameter \(\delta\) in the denominator is the fixed threshold, not
necessarily the actual minimum degree \(\delta(G)\).  The constant may depend
on that threshold but on neither \(G\) nor \(n\).  Equivalently, for each fixed
\(\delta\ge8\), the supremum of
\(\operatorname{diam}(G)-8|V(G)|/(3\delta)\) over the indicated graphs must be
finite.

A disproof therefore requires one fixed admissible \(\delta\) and a sequence
of such graphs, necessarily of unbounded order, whose excess tends to
infinity.  A single finite graph cannot disprove the assertion.  Every
6-colorable graph is \(K_7\)-free, so a 6-colorable counterexample suffices;
an upper bound proved only for 6-colorable graphs does not prove the frozen
claim.

There are no admissible graphs with \(n\le\delta\).  This vacuity does not
affect the quantifiers.

## Boundary case already settled

The case \(\delta=8\) follows from the standard unrestricted diameter bound.
If \(d=\delta(G)\) and a diametral path has length \(D\), the closed
neighborhoods of path vertices at indices \(0,3,6,\ldots\) are disjoint.
Thus
\((\lfloor D/3\rfloor+1)(d+1)\le n\), whence
\[
D\le {3n\over d+1}-1\le {n\over3}-1.
\]
Consequently the frozen inequality holds at \(\delta=8\), for example with
\(C_8=-1\).  This does not settle any \(\delta>8\).

## Literature position and proposed delta

The statement is the \(k=6\) specialization of Conjecture 2 of Czabarka,
Singgih, and Sz\'ekely, *J. Combin. Theory Ser. B* 151 (2021), 38--45,
doi:10.1016/j.jctb.2021.06.001 (printed p.40).  For even \(k=2r\), that paper
identifies it with part (ii) of the Erd\H{o}s--Pach--Pollack--Tuza conjecture;
at \(r=3\), the older formulation covers minimum degrees divisible by 8.

Chen and Chen, arXiv:2609.03346v1 (submitted 2026-09-03), restate the general
claim as Conjecture 1.3 (PDF p.2) and disprove it for odd \(k\ge7\) and even
\(k=2r\ge8\).  Their Theorem 2.7 (PDF pp.6--7) explicitly assumes \(r\ge4\),
so it does not settle \(k=6\).  Exact-assertion searches on 2026-09-06 found
no primary source resolving the \(k=6\) case; this is evidence of current open
status, not a proof of priority or exhaustiveness.

The proposed contribution is to test an unrestricted \(K_7\)-free extension
of the even-case layered blow-up at \(r=3\): nearest prior result = Theorem
2.7 for \(r\ge4\); proposed delta = alter its exceptional junction so that it
is \(K_7\)-free without requiring 6-colorability; verification route = an
exact finite weighted-degree/clique calculation followed by the periodic
blow-up formulas.  A successful construction for one fixed \(\delta\) would
disprove the frozen claim.

