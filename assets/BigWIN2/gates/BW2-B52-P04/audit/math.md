# Fresh mathematical referee report

## Frozen claim and verdict

I reviewed the frozen resolution claim

\[
c_{1,\infty}(C_4\mathbin{\square}C_4)=4
\]

under exactly the placement, simultaneous unit-speed cop move, immediate-capture,
and post-move cop-deleted-component robber convention in `problem.md`.  The
mathematical verdict is **accept**.  The upper and lower bounds cover the full
original scope, and I found no unresolved mathematical gap.

This report is bound to snapshot
`d14ab990f79b5f12f1bd0c3acec401cd45a8700c8ca6f05339f39a6fa73ec9f7`.
The reviewed frozen source, problem, claim, certificate, programs, reports, and
provided source PDF had the SHA-256 values recorded in the snapshot.  In
particular, the certificate hash was
`a544375352b451c4f703477b9ea88c3dfad6096573cb3c1b4e2cc80dbb8bc779`.
Per the referee-job restriction, I did not use `checkpoint.md` in reaching the
decision.

## Reconstruction of the decisive argument

For a sorted (k)-cop multiset (C) and a robber vertex (r\notin C), let
((C,r)) denote the state at the start of a cop turn.  A successor multiset
(D) is legal precisely when the entries of (C) can be matched to those of
(D) so that every matched cop either stays or crosses one graph edge.  If
(r\in D), the move captures.  Otherwise the robber's possible endpoints are
exactly the component (R_D(r)) of (r) in (G-\operatorname{supp}(D)).

Define (W_0=\varnothing), and recursively put ((C,r)) in (W_{t+1}) when
it is already in (W_t), or there is a legal successor (D) such that either
(r\in D), or every state ((D,r')) with (r'\in R_D(r)) is in (W_t).
This is the standard least reachability attractor, derived directly from the
move quantifiers: the cops choose (D), and then every legal robber response
must remain winning.  Membership first acquired at step (t) gives a
rank-decreasing strategy that captures in at most (t) cop moves, so the
argument is not circular.

For four cops, all 48,960 legal sorted-multiset states enter this attractor by
step 4.  The rank counts are 32,944, 9,344, 6,496, and 176 at ranks 1 through
4.  Thus every one of the 3,876 possible initial four-cop multisets wins against
every legal robber placement.  The frozen certificate supplies a legal selected
successor for every such state, and the checked strict rank decrease makes the
winning policy replayable.

For three cops, the fixed attractor contains 6,304 of the 10,880 legal states;
its complement (L) contains 4,576 states.  Negating the fixed-point condition
shows that, for every ((C,r)\in L) and every legal cop successor (D), capture
does not occur and some (r'\in R_D(r)) has ((D,r')\in L).  Moreover, every
one of the 816 three-cop initial multisets has a nonempty (L)-mask.  The robber
therefore chooses an initial safe vertex and, after each cop move, the certified
response that remains in (L).  Induction over the rounds gives evasion for
arbitrarily many rounds, hence forever in this finite perfect-information game.
Consequently three cops are insufficient while four suffice, proving the exact
value 4.

## Checks actually performed

I inspected the exporter and the separately implemented labelled checker, then
ran the labelled checker afresh.  It verified all 48,960 canonical four-cop
policy entries, their expansion to 810,000 legal ordered four-cop states, and
2,662,000 ordered three-cop moves from the 21,296 labelled states corresponding
to (L).  It also verified that every chosen four-cop multiset move lifts to a
legal labelled simultaneous move and that every three-cop response is reachable
in the appropriate deleted graph.  The run reproduced the frozen report byte
for byte; the report and certificate hashes remained unchanged.

As a separate derivation, I wrote and ran `audit/referee_recompute.py`.  It
imports none of the proposer programs, constructs adjacency independently from
modular coordinate differences, computes deleted-graph components by a fresh
depth-first search, and recomputes the least fixed point for (k=3,4).  Its
report `audit/referee_recompute_report.json` returns status `pass`, exact value
4, the counts above, and the same four-cop rank histogram.

The following boundary issues were checked explicitly:

- the graph has 16 vertices, 32 undirected edges, degree four, and graph digest
  `dc5ff1ba83c901714eae763d51d3c87d763524cff2a1b8c4a57929254d106d5e`;
- repeated cop positions, cop collisions, swaps, stays, and all ordered
  simultaneous cop moves are covered;
- only permutations of cop labels are quotiented, with no unrecorded graph
  automorphism quotient;
- capture on the cop move is tested before robber reachability, and a
  noncaptured robber moves only inside the component containing his current
  vertex after deleting the new occupied set;
- illegal states with a robber on a cop are excluded, while all legal initial
  robber placements are quantified; and
- the three-cop certificate handles every cop successor, not merely one
  adversarially selected move.

## Source comparison and contribution scope

The provided Biswas PDF states in Section 5.2 the product bound
(c_{1,\infty}(C_m^{\square k})\le 2m^{k-1}) for (m\ge4), and quotes the
Kinnersley--Townsend two-dimensional estimate
(2m-24\le c_{1,\infty}(C_m\square C_m)\le2m) only for (m\ge18).  Neither
statement gives the exact (m=4) value.  The candidate is appropriately limited
to the single (4\times4) torus cell and makes no claim about larger tori or
priority.  Exact resolution of the frozen cell, with independently checkable
upper- and lower-bound certificates, is a coherent contribution matching the
declared `resolution-paper` scope.

One bibliographic detail should be corrected during writing: although the local
filename and frozen prose identify arXiv v1, the embedded metadata of the
provided PDF identifies arXiv v2 dated 3 September 2026.  This does not affect
the mathematical verdict or the quoted Section 5.2 scope, but the manuscript
should cite the version actually used.

