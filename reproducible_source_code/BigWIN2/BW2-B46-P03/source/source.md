# Immutable source statement: win-00046-p03

## Title

Complete tight-set classification for deletion speed `r=12`

## Statement

For every integer `n >= 13` and every integer `w > n-1`, put
\[
V_{n,w}=([n-1]\setminus\{12\})\cup\{w\},\qquad
LR(V)=\max_{t\in[0,1)}\min_{v\in V}\|vt\|.
\]
Classify all pairs `(n,w)` for which `LR(V_{n,w})=1/n`.

The candidate conclusion to attack symmetrically is that the unique pair is `(14,24)`. This conclusion is not frozen as fact.

## Scope and provenance

- Primary source: T. Zhang, arXiv:2608.13599v1. Use Theorem 1.1 and Proposition 1.3 for `2r>n-1`, Theorem 1.6 for the effective middle-range bound, Theorem 1.8 and Table 1 for the published census, Lemma 2.2 for exact breakpoints, and Question 5.1 for the remaining classification problem.
- Frozen PDF: `batches/inbox/bigWin-46-materials/2608.13599.pdf`, SHA-256 `c661b2edcda1b6d11225c5c94e8a4289ed223da6cba82702336910c38bd73d44`.
- Outer scouting combined the published bounds into 20 claimed residual pairs: `(46,46..50)`, `(47,47..48)`, `(48,48..50)`, `(50,50..56)`, `(51,51..53)`, and reported an unreviewed exact enumeration finding none tight. Both the reduction and enumeration must be independently reconstructed; they are leads, not evidence accepted in advance.

## Accepted contribution boundary

A full resolution must prove coverage of every admissible `(n,w)`, reproduce the known positive pair `(14,24)`, and certify the exact value of `LR` on every residual pair. Finite checking without the theorem-based range reduction is not a universal classification.

## Cheapest decisive route

Derive the finite range from the cited theorems, enumerate the Lemma 2.2 breakpoint set in exact rational arithmetic, save an argmax and exact value per residual pair, and repeat with an independently implemented checker.
