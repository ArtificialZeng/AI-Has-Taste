# Degree and local-dimension jumps in the partition graph

Primary source: Fedor B. Lyudogovskiy, *Jump and Gradient Invariants in the Partition Graph*, arXiv:2605.28981v1, Section 8.6, Problems 8.1 and 8.2; definitions in Sections 2.1–2.2 and 3.1.
https://arxiv.org/html/2605.28981v1

For each integer n >= 2, let G_n have the integer partitions of n as vertices. A legal move transfers one unit from a donor part p >= 1 to a different recipient part q >= 1, or to a new part represented by q=0, discards a zero donor part, then reorders. Equal donor and recipient sizes require two distinct rows. Identity moves are excluded. Adjacency means one such legal move.

Write d(lambda)=deg_Gn(lambda), and delta(lambda) for the largest clique containing lambda minus one (equivalently, the local dimension in the clique complex). Define
D_d(n) = max_{lambda~mu in G_n} |d(mu)-d(lambda)|,
D_delta(n) = max_{lambda~mu in G_n} |delta(mu)-delta(lambda)|.

Problem 8.1 asks for the growth of D_d(n), and Problem 8.2 asks for the growth of D_delta(n). These are two related extremal functions, not an asserted formula. The source additionally asks about location of large dimension jumps; that qualitative question is not silently resolved by a numerical growth bound.

This is the outer supervisor's precise paraphrase of the two numbered source questions, not a purported verbatim downloaded batch. Original source questions and definitions are accessible at the link above. The n>=2 convention avoids an empty edge maximum; setting both functions to zero at n=1 is only a stated extension.

Relevant known input:
- arXiv:2605.28981v1 Proposition 3.1: support-size jump at most 2.
- arXiv:2603.27248v1 Theorem 2.2: for support size r, d=r(r-1)+A+B, where A counts consecutive distinct-size gaps >1 (including the gap to zero), and B counts multiplicities >1.
- arXiv:2606.20773v1 Background Proposition 3.1 and Proposition 3.3 recall the exact local transfer and clique-dimension formulas.
https://arxiv.org/html/2603.27248v1
https://arxiv.org/html/2606.20773v1

Provenance: authorized primary-literature fallback, screened 2026-09-14 +08. Not generated in Chrome, no browser batch number. A bounded current literature search found no inspected resolution of these two edgewise targets; this is not a worldwide open-status guarantee.
