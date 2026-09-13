# Exact resolution of the frozen `Q_3` problem

## Theorem

For the partial-feedback directional localization game specified in `source.md`
and `problem.md`,
\[
\zeta_d(Q_3)=3.
\]
In fact, three cops can force localization in at most two probing rounds.

## Explicit two-round strategy

Write the vertices of `Q_3` as the vector space \(\mathbb F_2^3\), let
\(e_1,e_2,e_3\) be its standard basis, and put
\(\mathbf 1=e_1+e_2+e_3\). All sums below are in \(\mathbb F_2^3\).

In round 1, probe
\[
(0,0,\mathbf 1).
\]
For a robber at \(r\), the legal replies to a probe at zero are
\[
D(0,r)=
\begin{cases}
\{0\},&r=0,\\
\{e_i:i\in\operatorname{supp}(r)\},&r\ne0,
\end{cases}
\]
and those to a probe at \(\mathbf1\) are
\[
D(\mathbf1,r)=
\begin{cases}
\{\mathbf1\},&r=\mathbf1,\\
\{\mathbf1+e_k:k\notin\operatorname{supp}(r)\},&r\ne\mathbf1.
\end{cases}
\]
It follows directly that every possible round-1 answer triple has a singleton
fiber except the following six answers. For distinct \(i,j\), let \(k\) be
the remaining coordinate. The answer
\[
(e_i,e_i,\mathbf1+e_k)
\]
has exactly the two-point fiber
\[
F_{ij}=\{e_i,e_i+e_j\}.
\]
Indeed, if the first two answers are distinct basis vectors, their two
coordinates must both lie in the support of \(r\), while the third answer
specifies an absent coordinate, so the support is unique. If the first two
answers both equal \(e_i\), and the third specifies the absent coordinate
\(k\ne i\), the support is either \(\{i\}\) or \(\{i,j\}\), giving precisely
the displayed fiber. Answers involving `0` or \(\mathbf1\) identify those
vertices immediately.

Suppose one of these six ambiguous answers occurs. After the robber's
stay-or-neighbor move, the belief is
\[
B_{ij}=N[F_{ij}]
=\{0,e_i,e_j,e_i+e_j,e_i+e_k,\mathbf1\}.
\]
In round 2, probe
\[
(0,e_i+e_j,e_i+e_k).
\]
To check that this localizes in one round, abbreviate
\(a=e_i,b=e_j,c=e_k\). The three sets of legal component replies for every
vertex in \(B_{ij}\) are:

| robber `r` | `D(0,r)` | `D(a+b,r)` | `D(a+c,r)` |
|---|---|---|---|
| `0` | `{0}` | `{a,b}` | `{a,c}` |
| `a` | `{a}` | `{a}` | `{a}` |
| `b` | `{b}` | `{b}` | `{a,c,a+b+c}` |
| `a+b` | `{a,b}` | `{a+b}` | `{a,a+b+c}` |
| `a+c` | `{a,c}` | `{a,a+b+c}` | `{a+c}` |
| `a+b+c` | `{a,b,c}` | `{a+b+c}` | `{a+b+c}` |

For every two distinct rows, at least one of the three entries is disjoint.
Consequently their Cartesian products of possible public answer triples are
disjoint. Thus every possible round-2 answer determines the current robber
vertex uniquely, before any further movement. This proves
\(\zeta_d(Q_3)\le3\).

Jones--Kinnersley Corollary 3.9 gives
\(\zeta_d(Q_n)\in\{n,n+1\}\) for every positive integer \(n\), hence
\(\zeta_d(Q_3)\ge3\). Combining the bounds proves the theorem.

## Exact computational certificate and independent replay

`solve_q3.py` represents each nonempty belief by an 8-bit integer. It
enumerates all 255 such beliefs, all \(8^3=512\) ordered three-probe tuples,
and every legal public answer fiber. Retrograde synthesis assigns rank 0 to
the eight singleton beliefs, rank 1 to all 246 non-singleton proper beliefs,
and rank 2 to the full belief. The selected initial action is `(0,0,7)` in
binary vertex encoding; its only non-singleton answer fibers are exactly the
six fibers proved above.

The emitted `q3_certificate.json` contains a probe action and decreasing rank
for every nonempty belief. `check_q3_certificate.py` is a separate
implementation: it does not import the solver, represents vertices as
coordinate triples, derives replies by the shortest-path distance condition,
and exhaustively replays every legal answer to every certified action. Its
report records `PASS`, 255 certified beliefs, 3,472 answer fibers, and the six
non-singleton transitions, all of which go from rank 2 to rank 1. These
computations are corroborating finite evidence; the explicit argument above
is the proof.

Reproduction from the project directory:

```sh
python3 evidence/solve_q3.py
python3 evidence/check_q3_certificate.py
```

