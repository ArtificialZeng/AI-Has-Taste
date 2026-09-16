# Fresh mathematical referee report

## Frozen scope and verdict

I reviewed the exact `resolution-paper` claim frozen at snapshot digest
`fcab4d382c1acedc64577e63722cff758f72912479bb142dd3736e23d4942e33`:
for the ordinary first-to-own-a-transversal game on a labelled (4\times4)
board, the forced X-win time is (T_4=11).  The scope is the complete fixed
(4\times4) game, not Guan's particular X strategy and not a claim for general
(n).

**Verdict: accept.**  The submitted policy certifies the missing universal
horizon-9 defense, and the already recorded upper bound by ply 11 then gives
the exact value.  The certificate covers every legal X branch and does not use
symmetry reduction.  A fresh checker and a separate exact minimax calculation
both confirmed the decisive result.

## Reconstruction of the decisive argument

There are exactly 24 winning masks: for each permutation \(\pi\in S_4\), the
mask contains cells \((i,\pi(i))\).  The submitted JSON maps each reachable,
nonterminal O-to-move state \((X,O)\) to one free cell.  Starting at the empty
state, form the directed graph by taking every free-cell successor at each
X-to-move state and the one recorded successor at each O-to-move state.  Each
edge claims one new cell, so ply strictly increases and the graph is acyclic.

The universal/existential directions are correct.  At an X node the verifier
checks all legal X moves; at an O node it needs one legal certified reply.  It
checks wins before accepting a horizon leaf.  Thus an X transversal completed
on ply 9 would be rejected, while an earlier O transversal is correctly treated
as a terminal branch on which X has been prevented from winning.  Every
nonterminal reachable O node has a policy record, and every submitted record is
reachable and used.

The exhaustive closure contains 28,604 distinct reachable states.  It has
4,911 X nodes with 41,768 checked legal X edges, 6,861 O nodes with 6,861
checked policy edges, 111 terminal O wins, and 16,721 non-X-winning ply-9
leaves.  There are zero reachable X-winning leaves.  Finite induction over this
DAG therefore gives a single O strategy that prevents X from winning through
ply 9 against every X strategy.  Hence (T_4>9).  Since X moves only on odd
plies and the frozen source boundary records (T_4\leq11), it follows that
(T_4=11).

## Checks performed

I wrote `audit/referee_recheck.py` without importing either submitted Python
program.  It reconstructs the winning masks using four explicit column loops,
checks the one-cell-per-row and one-cell-per-column conditions, and traverses
the submitted policy breadth first.  Its result is recorded in
`audit/referee_recheck.json`.  It reproduced all graph counts above and the
policy SHA-256
`0fa7169bbccb23fb540c1138227447648375d4cc5dd8da4f9e35fc15b904509f`.

The same fresh program also solved the labelled game directly with a separate
memoized terminal/AND-OR recurrence.  X nodes use an existential move and O
nodes a universal move, with immediate X and O wins tested before the horizon.
It evaluated 5,969 states at horizon 7, 148,787 states at horizon 9, and 738,608
states at horizon 11.  The respective root values for “X forces a win by the
horizon” were false, false, and true.  This independently confirms both sides
of the claimed exact value; the submitted replayable O policy remains the
decisive exported certificate for the previously missing lower bound.

I additionally checked the following failure modes:

- masks are nonnegative 16-bit masks, disjoint, and have the alternating X/O
  ownership counts required at their ply;
- all 24 transversal masks are distinct and use one cell in every row and
  column;
- duplicate, missing, unreachable, out-of-board, occupied-cell, and wrong-turn
  policy records are rejected;
- terminal wins are checked before horizon stopping, so the ply-9 boundary has
  no off-by-one error;
- merging histories at an occupancy state is sound because legal moves,
  terminal status, and all future winning conditions depend only on the two
  ownership masks; and
- no symmetry quotient or unrecorded group action is used, so replay is in the
  original labelled coordinates.

The canonical digest recomputed from the snapshot's stored file-hash mapping
equals the frozen snapshot digest.  The current hashes of the inspected
decisive source, claim, policy, programs, and submitted reports agree with that
mapping.

## Source comparison and contribution

Within the frozen literature screen, Guan supplies (T_4\leq11) but explicitly
leaves open whether another X strategy wins sooner; the exhaustive calculation
there concerns only Guan's displayed strategy.  Randjelovic establishes a win
for (n\geq4) without the fixed-(n=4) optimal-time lower bound, and the cited
Krishna preprint is withdrawn because of an error.  The new delta is exactly
the missing universal quantifier over all X strategies at horizon 9, certified
by a replayable full labelled policy graph.  This settles the frozen original
question rather than a toy restriction or a subsidiary claim.  The literature
assessment here is limited to the sources and retrieval record frozen in
`problem.md`; acceptance is not a claim of absolute priority beyond that
screen.

## Remaining gaps

There is no mathematical or certificate gap at the frozen scope.  The result
does not settle Guan's general-(n) optimality conjecture, and no such broader
claim is made.
