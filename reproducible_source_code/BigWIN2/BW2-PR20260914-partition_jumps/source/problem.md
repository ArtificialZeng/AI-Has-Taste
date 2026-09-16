# Precise problem and proposed research scope

Provenance: `primary-20260914-partition-jumps-triage-4d4ff86831cc`.
Frozen input: `source.md`, SHA-256
`f7b5d436d50606d2679b25bc5f17c2a79e098c16343a41802e06cae98cb393c1`.

For every integer n >= 2, P(n) is the set of finite nonincreasing sequences
of positive integers summing to n. The simple undirected graph G_n has
vertex set P(n). Select one donor row of size p >= 1 and either a different
existing row of size q >= 1 or a new row (q = 0); replace their sizes by
p-1 and q+1, discard zeros, and sort. Distinct resulting partitions are
adjacent. In particular p=q requires two rows and identity moves are omitted.
Repeated descriptions of an edge do not give multiple edges.

Let N(lambda) be its set of neighbors, d(lambda)=|N(lambda)|, and
delta(lambda)=max{|C|-1: C is a clique of G_n containing lambda}.
Thus delta(lambda) is also the clique number of G_n[N(lambda)]. Define

    D_d(n) = max{|d(mu)-d(lambda)|: {lambda,mu} in E(G_n)},
    D_delta(n) = max{|delta(mu)-delta(lambda)|: {lambda,mu} in E(G_n)}.

The original task is to determine their growth as n tends to infinity.
It asserts no candidate formula. Bounds asserted for all sufficiently large
n require constants independent of n and witnesses for every such n,
unless explicitly limited to a subsequence. Exact formulas for all n would
be a stronger possible contribution. At n=2 the unique edge has both jumps
zero. The optional convention D_d(1)=D_delta(1)=0 is outside the frozen domain.
The qualitative localization question in source Problem 8.2 is separate;
a growth bound alone does not answer it.

## Inspected nearest literature

Retrieved 2026-09-14. Lyudogovskiy, arXiv:2605.28981v1,
Sections 2.1-2.2 and 3.1 match these definitions; Section 8.6, Problems
8.1-8.2 explicitly asks these growth questions. Proposition 3.1 gives
|r(mu)-r(lambda)| <= 2 for r(lambda)=number of distinct positive sizes.
https://arxiv.org/html/2605.28981v1

Lyudogovskiy, arXiv:2603.27248v1, Theorem 2.2, states
d(lambda)=r(r-1)+A+B. Write the distinct sizes as
s_1>...>s_r>0, put s_{r+1}=0, let m_i be their multiplicities,
A=#{i:s_i-s_{i+1}>1}, and B=#{i:m_i>1}.
https://arxiv.org/html/2603.27248v1

Lyudogovskiy, arXiv:2606.20773v1, Section 2.1 and Background
Proposition 3.1, states

    delta(lambda) = max(max_i(r+1-a_i-b_i),
                        max_j(r-a_j-b_{j-1})),

where a_i=1[m_i=1], b_i=1[s_i-s_{i+1}=1], i=1,...,r,
j=1,...,r+1, a_{r+1}=b_0=0. These indicators differ from the
degree paper's notation; the definitions above remove that ambiguity.
https://arxiv.org/html/2606.20773v1

The original formula source is arXiv:2603.18696v1, Theorem 7.1:
https://arxiv.org/html/2603.18696v1. An earlier equivalent boundedness
question is Problem 6.4(iii) in arXiv:2603.23228v1:
https://arxiv.org/html/2603.23228v1.

Direct exact graph computation agrees with both formulas on every partition
for 2<=n<=20. Source status is open-supported by the numbered questions;
this does not establish that no later resolution exists. Coarse boundedness
D_delta<=4 already follows from the published formulas. The admitted
research target is sharper: prove or refute D_delta<=2 and its proposed
attainment set {11} union {n>=14}, and verify the proposed asymptotic
D_d(n)=4sqrt(2n)+O(1). These are proposed conclusions, not assumptions or
changes to the frozen original. See evidence/triage-math.md and
literature/triage-screen.md for evidence and limitations.

## Research pass 1: precise candidate and residual scope

Proposer: `primary-20260914-partition-jumps-research-abca685cda7d`.
The research proof is in `evidence/research-proof.md`. For every n>=2 it
gives D_delta(n)=0 at n=2,3; D_delta(n)=1 at n=4,...,10,12,13; and
D_delta(n)=2 at n=11 and all n>=14. For every n>=10 it gives
4s-8<=D_d(n)<=4s+2, with T_s<=n<T_{s+1}, hence
D_d(n)=4sqrt(2n)+O(1). All infinite witness families are proved symbolically.
The exceptional finite dimension maxima are recomputed directly from
graphs and exhaustive clique-subset searches in evidence/research_check.py
and evidence/research_check.json, without assuming the dimension formula.

For an edge oriented toward nondecreasing support, let k be the support
increase. Call an endpoint H when some size x>=2 is repeated and x-1 is
absent. The same proof shows that a dimension jump of magnitude two occurs
exactly when either k=1, the lower endpoint is neither a staircase nor H,
and the upper endpoint is H; or k=2 and both endpoints are H. This local
classification makes no claim about spatial/statistical concentration.

Both quantitative growth questions are answered by the proposed theorem.
The separate qualitative localization question in the source remains
unresolved; the candidate is therefore conservatively a result-note with
workflow original_status=unresolved. This label does not suggest that the
two proved growth estimates themselves remain conjectural. Fresh review
has not yet occurred, and worldwide novelty is not certified.

The decisive primary texts have been copied inside the project as
evidence/external/2605.28981v1.html (original questions and definitions),
evidence/external/2603.27248v1.html (Theorem 2.2), and
evidence/external/2606.20773v1.html (Background Proposition 3.1).
They are full primary HTML captures, verified against live relevant
sections, and must remain in the frozen evidence. Their hashes and origins
are in evidence/external/source-manifest.json. Source.md is unchanged.
