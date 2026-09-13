# Fresh mathematical referee report

## Frozen scope

I reviewed the claim at snapshot
`ba716a810c205d214da52cc5b993cc6650f9d7be715542223f01b7730d054ed1`.
The submitted scope is exactly the frozen original problem: the
Jones--Kinnersley partial-feedback game on `Q_3`, with three simultaneous
ordered probes, a separately adversarial legal directional reply to each
probe, localization before movement, and a stay-or-one-edge move after an
unresolved round.  The claim is the full resolution
\(\zeta_d(Q_3)=3\), not a restricted or subsidiary statement.

All nine snapshot hashes, including the hashes of `source.md`, `problem.md`,
the proof, both programs, the certificate, and both reports, were recomputed
and matched.  Recomputing the canonical snapshot digest also gave the digest
above.

## Reconstruction of the decisive argument

Write the cube as \(\mathbb F_2^3\), with basis
\(e_1,e_2,e_3\) and \(\mathbf 1=e_1+e_2+e_3\).  The first-round action is
\((0,0,\mathbf 1)\).

For a robber at \(r\ne0\), either zero probe may return precisely an
\(e_i\) whose coordinate lies in \(\operatorname{supp}(r)\).  For
\(r\ne\mathbf1\), the last probe may return precisely
\(\mathbf1+e_k\) for an absent coordinate \(k\).  Replies `0` and
\(\mathbf1\) themselves are possible only at the corresponding hit and hence
identify the position.

If the two zero-probe replies are distinct, say \(e_i,e_j\), and the last
reply is \(\mathbf1+e_k\), then \(i,j\) are present and \(k\) is absent;
the position is uniquely \(e_i+e_j\).  If the first two replies agree at
\(e_i\), the last reply names an absent \(k\ne i\), and, writing \(j\) for
the remaining coordinate, the fiber is exactly
\[
F_{ij}=\{e_i,e_i+e_j\}.
\]
Thus the only unresolved histories are the six ordered choices of distinct
\(i,j\).  A fresh enumeration from the distance definition found exactly 24
nonempty public-answer fibers: 18 singleton fibers and these six two-point
fibers.

After a legal robber move, the belief arising from \(F_{ij}\) is, with
\(a=e_i,b=e_j,c=e_k\),
\[
B=N[F_{ij}]=\{0,a,b,a+b,a+c,a+b+c\}.
\]
The prescribed second-round action is \((0,a+b,a+c)\).  Re-deriving legal
responses directly from distance gives

| current vertex | from `0` | from \(a+b\) | from \(a+c\) |
| --- | --- | --- | --- |
| \(0\) | \(\{0\}\) | \(\{a,b\}\) | \(\{a,c\}\) |
| \(a\) | \(\{a\}\) | \(\{a\}\) | \(\{a\}\) |
| \(b\) | \(\{b\}\) | \(\{b\}\) | \(\{a,c,a+b+c\}\) |
| \(a+b\) | \(\{a,b\}\) | \(\{a+b\}\) | \(\{a,a+b+c\}\) |
| \(a+c\) | \(\{a,c\}\) | \(\{a,a+b+c\}\) | \(\{a+c\}\) |
| \(a+b+c\) | \(\{a,b,c\}\) | \(\{a+b+c\}\) | \(\{a+b+c\}\) |

Every pair of rows has a disjoint entry in at least one probe component, so
their Cartesian sets of public reply triples are disjoint.  Hence every legal
second-round reply identifies the current vertex before movement.  This
handles all answer choices independently for the repeated first-round probes,
all six ambiguous histories, staying, and each one-edge move.  It supplies a
uniform bound of two rounds and proves \(\zeta_d(Q_3)\le3\).

The frozen source and interpretation record Jones--Kinnersley Corollary 3.9 as
giving \(\zeta_d(Q_n)\in\{n,n+1\}\), hence the needed lower bound
\(\zeta_d(Q_3)\ge3\).  As an additional nondecisive check, I independently
computed the two-probe attractor from the graph-distance definition: among all
255 nonempty beliefs, 194 are winning and 61 form the complementary safety
trap containing the full belief.  For every one of the 61 beliefs and all 64
ordered two-probe actions, an unresolved answer returning to that trap was
verified (3,904 belief-action pairs).  Thus the lower bound is also consistent
with an exhaustive direct game calculation.

Combining the two bounds proves the exact submitted statement.

## Certificate and implementation checks

The solver's update is the required belief update: it intersects the current
belief with a full-cube answer support, treats a singleton fiber as immediate
localization, and otherwise takes the closed neighborhood, including staying.
Its fixed-point loop uses only beliefs from strictly earlier rank levels.  It
enumerates all 255 nonempty beliefs and all \(8^3=512\) ordered actions, so it
does not assume distinct probes.

The replay checker does not import the solver.  It represents vertices by
coordinate triples, constructs neighbors explicitly, and accepts a reply only
when it reduces graph distance to the robber by one.  It then reconstructs
every public-answer fiber and every closed-neighborhood successor.  Inspection
found no mismatch between its encoded statement and the frozen game.

I ran the solver to temporary outputs.  It reproduced the frozen certificate
byte for byte, with SHA-256
`c34439f7e1c9422540d7e6b6626e532f89394f6b1755d4714ac58cf576255dc3`.
I separately ran the replay checker on the frozen certificate.  It checked all
255 strategy beliefs and 3,472 answer fibers; the only six nonsingleton
transitions are the rank-2 initial branches, and each goes to rank 1.  The
certificate has the eight singleton beliefs at rank 0, all 246 proper
nonsingleton beliefs at rank 1, and the full belief at rank 2.  These results
agree with, but are not needed in place of, the explicit two-round proof.

## Prior-result comparison and gaps

Within the frozen source comparison, the nearest prior result supplies only
the bracket \(\{3,4\}\) for `Q_3` and explicitly leaves the exact hypercube
value as a question.  The submitted strategy selects the value 3 in the full
game and is a concrete nonroutine delta, while making no claim for higher
dimensions or an unsupported priority assertion.  The cited external PDF is
not part of this snapshot's evidence list, so I did not perform a new
bibliographic or present-day novelty audit in this pass; that limitation does
not leave a mathematical gap because the frozen bracket is explicit and the
two-cop lower bound was also checked directly.

No unresolved mathematical gap was found in the exact frozen candidate scope.

## Verdict

**ACCEPT.**  Scope, correctness/evidence, and contribution all pass for a
`resolution-paper` with original status `proved`.
