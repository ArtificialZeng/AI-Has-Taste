# Source statement — win-00047-p03

## Exact frozen question

On a (4\times4) board, players X and O alternately occupy previously empty cells, with X moving first. A player wins upon occupying four cells in pairwise distinct rows and pairwise distinct columns (a transversal). Let (T_4) denote the least ply by which X can force a win, with O choosing play to delay or prevent that win; if O can prevent X forever then (T_4=\infty).

Determine whether

\[
T_4=11.
\]

The upper bound (T_4\le11) follows from the source's explicit strategy for all (n\ge4). The missing assertion is the universal lower bound: for every X strategy, O has a defense preventing X from completing a transversal on ply (9) or earlier.

An exact solution may use symmetry-reduced minimax, but must export a replayable strategy/counterstrategy DAG and an independent verifier covering every legal branch. A run that checks only the source's particular X strategy does not prove optimality.

## Primary source and known boundary

Kevin Guan, *The transversal achievement game on a square grid*, arXiv:2608.13501v1. See the rules and Theorem A on p.3, the exhaustive verification of the displayed strategy in Table 1 on p.14, and Conjecture 14 on p.14. The author explicitly states that the computation for the displayed strategy does not rule out a faster X strategy.

Local primary-source copy: `batches/inbox/bigWin-47-materials/2608.13501.pdf` (SHA-256 `fedcf61bc6c79f4abbffcd2794e89f9aed6a831d394efbde9c729af464c129dd`).

## Proposed contribution boundary

Only the fixed (4\times4) game length is in scope. A defense that delays one particular X strategy is insufficient; the lower bound must quantify over all X strategies.
