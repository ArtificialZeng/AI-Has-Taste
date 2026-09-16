# Immutable source statement: win-00046-p04

## Title

Zero-free columns of the symmetric-group character table at `n=44`

## Statement

For partitions `lambda, mu` of 44, let `chi^lambda(mu)` be the irreducible character value of `S_44`. Determine exactly
\[
ZF(44)=\{\mu\vdash44: \chi^\lambda(\mu)\ne0\text{ for every }\lambda\vdash44\}
\]
and `D(44)=|ZF(44)|`.

## Scope and provenance

- Primary source: C. Defant, S. Hariharan, K. Lau and K. Ono, *Zero-free columns in the character tables of symmetric groups*, arXiv:2608.27718v1. Definition (3), p.2; data through `D(43)`, pp.3 and 14; Duro exact problem and the type-III obstruction discussion, pp.12–13; computational method, pp.13–14.
- Frozen PDF: `batches/inbox/bigWin-46-materials/2608.27718.pdf`, SHA-256 `b814224c8e648114d804380f6b218aab98f69ddb87127d282392bcee83e33223`.
- The source reduces possible zero-free columns to cycle types `(3^a,2^b,1^c)` with even `b`, further bounded by the 2-core and 3-core distances. It publishes the complete table only through 43. This project computes the adjacent finite layer; it does not claim progress on the asymptotic conjecture.

## Accepted contribution boundary

A complete result must list every survivor and prove that no candidate column was skipped. Each rejected candidate needs a partition `lambda` giving an exact zero, while each survivor needs all character values checked nonzero. Code output alone must be accompanied by a small independent verifier or an independent standard-system comparison, plus reproduction of the published values through 43.

## Cheapest decisive route

Implement the beta-number Murnaghan–Nakayama recurrence described in the appendix, stop at the first zero for rejected columns, compute full columns only for survivors, and compare a sample or the full reduced set with GAP/Sage if available.
