# win-00067-p04 — Three-move subtraction games of shape (2,5)

## Frozen source statement

For every integer `c>5` with `c!=7`, let `S={2,5,c}` and define the Sprague–Grundy word by `g(0)=0` and

`g(n)=mex({g(n-s): s in S, n>=s})`.

Prove or disprove Conjecture 50 of arXiv:2609.05358v1 for this entire `(a,b)=(2,5)` shape. Source-known residue zones must be checked but not reproved unless needed; the new core is to decide the two remaining classes

`c congruent to 0 or 4 (mod 7)`.

In particular, determine whether each has positive minimal preperiod and, if feasible, prove exact parameterized preperiod/period words. The following patterns are provisional computational leads, not facts:

- Set `A=0011021`. For `c=7K+4`, `K>=1`, the word appears to be `A^K 0011223 (021021 A^K)^infinity`, suggesting `(q,p)=(c+3,c+2)`.
- For `c=7K`, `K>=2`, it appears to be `A^K 32203103 (1 A^(K-1) 02102102)^infinity`, suggesting `(q,p)=(c+8,c+2)`.

First recompute all boundary cases and exact mex values. A universal proof must give a finite, parameter-independent block/seam verification and prove minimality of any claimed preperiod and period. A single mismatch with its index and mex predecessors is an exact disproof of a provisional formula. Sampling many K values is not a proof.

## Source and contribution boundary

Primary source: *Three-move subtraction games*, arXiv:2609.05358v1. Table 1 and Theorem 32 are on PDF p.21; Conjectures 50, 54, and 55 are on pp.32–35. For the regime `b>2a` and `a` not dividing `b`, the source leaves admissible residue classes with conjectured positive preperiod. For `(2,5)`, the unresolved residues are `{0,4}`.

This is distinct from Batch 65's `(4,6,c)` work: it freezes an entire smallest shape in a different structural regime, not a new name for one residue. Triage must verify the residue extraction and later literature before a novelty claim.

Primary evidence: `batches/inbox/bigWin-67-materials/2609.05358.pdf` (SHA-256 `39457676064479f1ff52fded8697695c1ddd598f63665996b2eb889ec6fa66ca`).

