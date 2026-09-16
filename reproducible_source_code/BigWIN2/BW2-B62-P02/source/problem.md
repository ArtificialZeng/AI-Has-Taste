# Precise problem reading

## Objects and encodings

Let

\[
M=\{m_0,m_1,m_2\},\qquad W=\{w_0,w_1,w_2\},\qquad V=M\cup W,
\]

and let the acceptable graph be the complete bipartite graph with edge set
`M x W`.  Every vertex is an unweighted voter.  Write `bot` for being
unmatched; every acceptable neighbour is strictly preferred to `bot`.

A weak order on the three labelled neighbours is encoded by a rank triple
`(r0,r1,r2)`, in neighbour-index order, where lower rank is better and the
set of used ranks is exactly `{0,...,max(ri)}`.  Thus ranks describe ordered
nonempty indifference blocks.  There are

\[
1+(2^3-2)+3!=1+6+6=13
\]

such triples.  A preference profile is an ordered sextuple of these triples,
in agent order `(m0,m1,m2,w0,w1,w2)`; a man's coordinates are ordered
`(w0,w1,w2)` and a woman's coordinates are ordered `(m0,m1,m2)`.  Hence the
quantified profile domain has exactly `13^6 = 4,826,809` labelled profiles.

A matching is a set of vertex-disjoint edges.  Equivalently, it is a partial
bijection between subsets of `M` and `W`.  Its partner map `p_X(v)` is the
matched neighbour of `v`, or `bot`.  Matchings of every cardinality from zero
through three are included, so the alternative domain is

\[
\mathcal X=\{X:X\text{ is a matching of }K_{3,3}\},\qquad
|\mathcal X|=\sum_{k=0}^3 {3\choose k}^2k!=34.
\]

## Popular-winning condition

For a nonempty set `C` of **distinct** matchings and an agent `v`, let
`b_C(v)` be any most-preferred element of
`{p_X(v): X in C}`.  This is unambiguous at the level of the agent's weak
order; in particular it is `bot` exactly when `v` is unmatched in every
member of `C`.  For each alternative `Y in X`, define the two integer vote
counts

\[
A_P(C,Y)=|\{v\in V:b_C(v)\succ_v p_Y(v)\}|,
\quad
B_P(C,Y)=|\{v\in V:p_Y(v)\succ_v b_C(v)\}|.
\]

An indifferent agent contributes to neither count.  The set `C` is popular
winning for profile `P` precisely when

\[
A_P(C,Y)\ge B_P(C,Y)\qquad\text{for every }Y\in\mathcal X.
\]

The instance dimension is

\[
d(P)=\min\{|C|:\varnothing\ne C\subseteq\mathcal X,
 C\text{ is popular winning for }P\},
\]

and the frozen target is the single integer

\[
D_{3,3}=\max_{P\in\mathcal W^6}d(P),
\]

where `W` is the above 13-element weak-order set.

The task requires an exact proof that `D_3,3` is 2 or 3.  If it is 3, the
certificate must give an extremal profile, verify every singleton and every
two-element subset of the 34 matchings fails against at least one of the 34
alternatives, and verify a three-element popular-winning set.  If it is 2,
the certificate must verify that every one of the 4,826,809 profiles has a
popular-winning singleton or pair, and give a profile without a popular
singleton.  Quantification over nonperfect alternatives, including the empty
matching, is mandatory in both branches.

For reproducible reporting, "canonical profile" will mean the
lexicographically least rank-sextuple in its orbit under
`(S3 x S3) semidirect C2`: independent relabelling of men and women and an
optional exchange of the two sides.  If more than one extremal orbit exists,
report the globally lexicographically least such representative.  This is a
reporting convention only and does not alter the frozen target.

## Statement validation and nearest prior result

The local primary-source PDF has SHA-256
`1707cb5423c732793ebc688f84b5663dee15ad7ae330ccb6b10cdd210a76bfd2`,
matching `source.md`.  In arXiv:2509.25150v3, the popular-winning definition
is in Section 1.2 (PDF p. 4), Table 1 states that the unweighted marriage
problem with ties has class dimension in `{2,3}` (PDF p. 4), and Theorem 3.3
gives the general upper bound 3 (PDF p. 10).  The paper does not state this
fixed `K_3,3` census.

The exact check in `evidence/triage_singleton_check.py` gives a labelled
`K_3,3` profile with no popular singleton, while including all 34 partial
matching alternatives.  Together with Theorem 3.3 this validates
`2 <= D_3,3 <= 3`; it does not decide between the two values.

On 2026-09-07, arXiv searches for the exact phrase "popular dimension" with
`K_3,3`, the paper title, and "popular winning set" with ties located the v3
source and related popular-matching literature, but no separate primary paper
reporting this finite census.  Accordingly the source status is
`new-question/status-uncertain`, not a claim of novelty or priority.

The target contribution is: nearest prior result = Theorem 3.3's universal
upper bound 3; proposed delta = determine the sharp maximum on the complete
three-by-three unweighted tied domain; verification route = exhaustive exact
enumeration modulo an explicitly checked graph-automorphism action, followed
by an independently implemented verifier over the unreduced labelled domain
or a complete orbit-lifting certificate.
