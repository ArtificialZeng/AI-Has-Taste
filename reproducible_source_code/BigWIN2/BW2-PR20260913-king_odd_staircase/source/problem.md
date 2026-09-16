# Precise problem: King on equal odd-block staircases

Triage provenance: primary-20260913-king-odd-staircase-triage-76eec04b3033.
The exact task is frozen in `source.md`; its SHA256 is
`e4dc12773dcaea452c4710f74f8cea0715f792af5af8f043d8d73d5b30913ae8`.
No correction or weakening is proposed.

## Definitions and quantified assertion

A nonempty partition is a finite tuple of positive integers
\(\lambda=(\lambda_1\ge\cdots\ge\lambda_\ell>0)\).
For integers \(i,j\ge0\), define \(\lambda[i,j]\) by taking
\((\lambda_{i+1}-j,\ldots,\lambda_\ell-j)\) and omitting nonpositive entries.
It is empty if no entries remain. In normal play a legal move has
\((i,j)\in K=\{(0,1),(1,0),(1,1)\}\) and a nonempty destination.
Define
\[
G(\lambda)=\operatorname{mex}\{G(\lambda[i,j]):(i,j)\in K,
                                      \lambda[i,j]\ne\varnothing\},
\]
where mex is the least nonnegative integer outside a finite set and
\(\operatorname{mex}\varnothing=0\). The empty partition is not a game
position or a successor. Each move decreases size; thus this defines a finite
game. There are at most three options, so \(0\le G\le3\).

For positive integers \(r,c,k\), let
\[
D^k_{r,c}=((kc)^r,((k-1)c)^r,\ldots,c^r),
\]
where powers denote repetition of parts, not exponentiation.
The original assertion quantifies over **every odd positive integer \(r\)**
and **every positive integer \(k\)**. With \(q\) the unique residue
\(0\le q<r+2\) congruent to \(k\) modulo \(r+2\), it asserts
\[
G(D^k_{r,r})=
\begin{cases}
0,&q\text{ odd},\\
1,&q\text{ even and nonzero},\\
2,&q=0.
\end{cases}
\]
Resolving finitely many block sizes, only winning/losing positions, or the
unequal even-block Conjecture 5.2 does not resolve this assertion. The parameter
\(k=0\) is excluded; treating an empty destination as a zero option changes
the game.

## Primary statement and nearest results

Eric Gottlieb, Matjaž Krnc, Peter Muršič, *Impartial Chess on Integer
Partitions*, arXiv:2501.14640v1, 24 January 2025:
[Definitions 2.1 and 3.1, Section 3.4, Conjecture 5.1](https://arxiv.org/html/2501.14640v1).
The preserved HTML and `evidence/triage/source-extract.txt` were inspected.
Theorem 3.8 classifies rectangles, so all \(k=1\) cases here have value zero.
Lemma 3.13 gives \(G(D^k_{1,1})=(k-1)\bmod3\) for positive \(k\),
which is exactly the present \(r=1\) case. Its displayed \(k\ge0\) does not
extend the frozen task to empty boards. Lemma 3.14 treats even \(r\): value
two at \(k=1\), and one at \(k\ge2\). Neither settles arbitrary odd \(r\).

Source status on 13 September 2026: **status-uncertain**. The primary v1
explicitly states the conjecture, and the live arXiv history lists only v1.
The later [SSRN record](https://ssrn.com/abstract=5649443) could not be obtained
as full text in this triage; its content remains uncompared. No current-open
or priority certification follows. See `literature/triage-screen.md`.

## Triage route (historical)

Nearest prior result: the equal even-block classification and ordinary
staircase formula above. Proposed delta: prove or disprove the exact uniform
classification for every odd block size. Verification route: derive and check
a closed boundary-word family under the exact square mex transfer, then prove
its closure uniformly in \(r\); alternatively produce an exact failing board.

For \(D_k=D^k_{r,r}\), set
\(B_k(j)=G(D_k[0,j])\) for \(0\le j<r\). The square transfer and base
conditions are derived in `evidence/triage/transfer.md`. Finite tests validate
the transfer but disprove the naive strengthening \(B_{k+r+2}=B_k\).
Already \(r=3\) gives \(B_1=(0,3,0)\ne B_6=(0,2,0)\), while their
root values agree. A phase of length \(2(r+2)\) is the corrected route.
An explicit formula is frozen in `evidence/triage/transfer.md` and
`evidence/triage/phase-holdout.py`; it passes all 752 new boundary cases
recorded in `evidence/triage/phase-holdout.json`. Its uniform transfer closure
was unproved at triage and assigned as the first research test.

## Research pass 1: full-scope proof candidate

Proposer: primary-20260913-king-odd-staircase-research-fd17b876b830.
`evidence/research/proof.md` gives a complete proposer-side argument for the
same frozen original statement, with no known mathematical gap. It proves
the stronger boundary formula above by an explicit interior array: three
parity tables separated at L=r+2-t, with a special value 2 at (L,L).
An exhaustive local case table proves the mex identity for this array for
every nonnegative L. The square-transfer induction covers k=1 via the
rectangle calculation, k=2 with the corner absent, and both phase
wraparounds, including r=1. Taking the root yields the original formula.

Exact corroboration in `evidence/research/verify.py` and `.json` reports
4,313,608 transfer-interior comparisons, 1,309 boundary words, 114 direct
full boards, 210 recursive subpartition comparisons, and every displayed
local seam case, with no mismatch. The finite calculations are checks of
the written proof, not its universal premise. No fresh referee has accepted
this candidate; no manuscript exists.

The source-status qualification remains unchanged. The live primary v1 was
rechecked and the later SSRN full text remains inaccessible and uncompared;
see `literature/research-screen.md`. The claimed contribution is a complete
proof of the exact frozen conjecture, with priority and current openness
unverified. `source.md` has not been changed.
