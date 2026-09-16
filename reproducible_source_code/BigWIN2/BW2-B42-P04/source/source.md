# Frozen source — win-00042-p04

## Immutable original claim

For every prime `p>=37` satisfying `p congruent 1 (mod 12)`, there exists `a in F_p\{0,1}` such that the integral quandle ring of the Alexander quandle `Alex(F_p,f_a)` contains a nontrivial idempotent. Equivalently within the source's character criterion, prove that for some nontrivial multiplicative character `chi` one has

`chi(-1)=1` and `{chi(a),chi(1-a)}={zeta_6,zeta_6^{-1}}`.

This asks whether `p=13` is the unique prime congruent to 1 modulo 12 for which no such parameter a exists.

## Source and claimed delta to verify

- Primary source: arXiv:2609.03799, Lemma 6.2, Theorem 6.3, Corollary 6.4 (PDF pp.10--12).
- Local immutable source PDF: `batches/inbox/bigWin-42-materials/2609.03799.pdf`, SHA-256 `173a741c72a01f5a890897613279db100c41cef21d72617d01461f8d9e5230bb`.
- The source gives a fixed-`(p,a)` character criterion and the necessary congruence. The universal existence assertion above is a new lead inferred from that criterion, not a theorem or an explicitly attributed conjecture of the source. Triage must check later character-sum and quandle literature before any novelty claim.

## Required resolution standard

A proof should give an explicit positive lower bound for the exact count `N_p` above a rigorously stated threshold and an exact, independently replayable verification for every remaining prime. A disproof must give a prime and a complete character/discrete-log certificate that `N_p=0`. Numerical sampling or an unchecked asymptotic is insufficient.

