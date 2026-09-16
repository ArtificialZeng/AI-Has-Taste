# Precise problem — the 4 x 4 transversal achievement game

## Frozen question and scope

The immutable statement is `source.md`. This file fixes its mathematical reading; it does not alter the source claim. Only the ordinary finite two-player game on one \(4\times4\) board and its exact forced-win time are in scope. No assertion for general \(n\) is sought.

Let

\[
B=[4]\times[4],\qquad
\mathcal T=\bigl\{\{(i,\pi(i)):i\in[4]\}:\pi\in S_4\bigr\}.
\]

Thus \(B\) has 16 cells and \(\mathcal T\) consists of its 24 transversals (equivalently, the perfect matchings of \(K_{4,4}\)). X and O alternately claim one previously unclaimed cell, X at odd plies and O at even plies. If after a move the mover's claimed set contains a member of \(\mathcal T\), that mover wins immediately and the history terminates. If all cells are claimed without a win, the result is a draw.

A (pure, deterministic) strategy for a player is a function from every legal, nonterminal finite history at which that player is to move to a free cell. Since this is a finite perfect-information game without chance, randomization is irrelevant to a force guarantee. For strategies \(\sigma_X,\sigma_O\), let \(\tau_X(\sigma_X,\sigma_O)\) be X's winning ply, with value \(\infty\) if the induced history instead ends in an O win or a draw. Define

\[
T_4=\min_{\sigma_X}\ \max_{\sigma_O}\tau_X(\sigma_X,\sigma_O),
\]

where the order on possible values is the usual order extended by \(t<\infty\). Equivalently, \(T_4\le t\) means

\[
\exists\sigma_X\ \forall\sigma_O:\quad
X\text{ wins by ply }t.
\]

Because X moves only on odd plies and a published strategy gives \(T_4\le11\), the claim \(T_4=11\) is equivalent to the missing statement

\[
\forall\sigma_X\ \exists\sigma_O:\quad
X\text{ has not won by the end of ply }9.
\]

Here the chosen O response may depend on the full preceding history. An earlier O win is a valid way to prevent an X win on that branch. A defense against only one prescribed X strategy does not establish this quantifier.

## Boundary checks

- X cannot win before ply 7 because a transversal requires four X cells.
- The only candidate forced-win plies at or below 11 are therefore 7, 9, and 11.
- Row permutations, column permutations, and transposition preserve legal play and winning sets. In particular all 16 opening cells are equivalent, but any symmetry-reduced certificate must retain enough group-action data for moves to be replayed in the original coordinates.
- The number of labelled occupancy states through ply 9 before removing terminal positions is
  \(\sum_{p=0}^{9}\binom{16}{\lceil p/2\rceil}\binom{16-\lceil p/2\rceil}{\lfloor p/2\rfloor}=2{,}959{,}437\). This makes a complete exact horizon-9 state search plausible; it is not itself evidence of the game's value.

## Prior-result and status screen

Retrieved 2026-09-06.

1. Kevin Guan, *The transversal achievement game on a square grid*, arXiv:2608.13501v1, <https://arxiv.org/abs/2608.13501>. The local PDF has SHA-256 `fedcf61bc6c79f4abbffcd2794e89f9aed6a831d394efbde9c729af464c129dd`. Section 2 defines the same first-to-own-a-transversal game and Theorem A states X wins for every \(n\ge4\). Sections 4--5 prove that Guan's particular strategy wins by ply \(2n+3\), hence \(T_4\le11\). Section 6/Table 1 exhaustively checks O's replies only against that fixed strategy. Printed p.14, Conjecture 14, conjectures optimality and explicitly says this computation does not rule out a faster X strategy. The arXiv record lists only v1, submitted 2026-08-13.
2. Zarko Randjelovic, *The transversal game*, arXiv:2401.16768v2, <https://arxiv.org/abs/2401.16768>. Its abstract and theorem establish that X has a winning strategy for \(n\ge4\), but do not supply the fixed \(n=4\) optimal-length lower bound.
3. Niranjan Krishna, *Transversal achievement game on a square grid*, arXiv:2101.00770v2, <https://arxiv.org/abs/2101.00770>, is withdrawn; the arXiv record says the proof has an error. It is not valid prior evidence for this claim.

Exact-assertion and equivalent-language searches on arXiv found no source, as of the retrieval date, proving or disproving the universal \(4\times4\) horizon-9 defense. This is a limited literature screen, not a priority proof. The source status is **open-supported**: the nearest primary source poses a stronger conjecture whose \(n=4\) case is exactly the missing lower bound.

## Proposed contribution and decisive verification route

Nearest prior result X: Guan proves \(T_4\le11\) and checks only a fixed X strategy. Proposed delta Y: determine the complete minimax value for the fixed \(4\times4\) instance, in particular the universal horizon-9 defense (or exhibit a faster X strategy). Verification route Z: exact retrograde/AND--OR search on pairs of disjoint 16-bit masks, with terminal checks against all 24 transversal masks.

At an X node, a horizon-9 defense certificate must validate every legal X successor; at an O node it may select one legal O successor. Leaves are successful for the defense if O has already won or ply 9 is reached without an X transversal, and unsuccessful if X has won. The research artifact must export a replayable strategy/counterstrategy DAG, not merely a root value or node count. A separate small verifier should check mask disjointness, turn and ply, move legality, immediate termination, all AND children, each OR choice, acyclicity/reachability, and the root conclusion without trusting solver caches or pruning. A horizon-11 solve can independently certify the matching upper strategy and distinguish values 7, 9, and 11.
