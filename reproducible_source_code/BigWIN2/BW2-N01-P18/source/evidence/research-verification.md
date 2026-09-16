# Research verification and attacks

Job: newwin-00001-p18-research-8635786e3d2c; 2026-09-12.
This is the proposer's verification record, not a separate referee report.

## Decisive test from the checkpoint

The prescribed test was to challenge the translated-finite-sums argument,
the digit-block contradiction for every offset, and their composition with
the residue/module reduction. All have explicit proofs in research-proof.md.
The following possible failure points were checked against those proofs:

| Possible failure | Verification |
| --- | --- |
| Ordinary recurrence is replaced by bounded-gap recurrence | The prefix return is chosen beyond a finite cutoff; no gap bound is used. |
| Infinite induction only copies individual ones | A return copies the whole prefix through the largest constructed subset sum, so it simultaneously copies every old subset sum. |
| Block sums reuse a generator | Each block is taken in the unused tail after the preceding block. Gaps between selected blocks are allowed. |
| High block digits carry into another block | Divisibility gives the lower endpoint; the strict next-power inequality gives the upper endpoint. Their occupied digit positions are disjoint. |
| One offset survives | The same low bound exceeds (p-1)a+D, so the no-carry identity holds for every integer offset 0<=r<=D at once. |
| p=2 or D=0 breaks a strict inequality | Positivity gives (p-1)b_i>=p^K_i for every p>=2; hence K_(i+1)>K_i, including p=2. One block suffices when D=0. |
| Division by n is hidden in the series identity | Residue substitution is justified by lifting an integral identity. No division in F_p by n is made. |
| Laurent exponents are excluded | The quotient ring is explicitly isomorphic to the Laurent ring; both homomorphisms are supplied. |
| Phi is mistakenly taken multiplicative | Only its linearity and its shift under multiplication by P are used. |
| Module spanning is mistaken for independence | The monic quotient gives a free module, and both inverse maps are checked. |
| Cancellations generate new support indices | A nonzero sum coefficient has at least one nonzero summand coefficient. Cancellations remove indices. |
| A sparse support is treated as sufficient | The proof uses the digit-sum constraint and the finite-sums exclusion, not a density estimate. |

No counterexample or hypothesis gap was found in these attacks. This statement
does not replace the requested fresh referee.

## Exact independent implementation

Run from the project directory:

    python3 evidence/check-research.py

The script imports no triage code. For negative monomials it computes

    Phi(x^(-m))=L(Phi(x^(1-m)))-Phi(x^(p-m)),

using P*x^(1-m)=x^(p-m)+x^(-m). This recurrence terminates because both
negative exponents on the right have smaller magnitude. Coefficients on the
other side come from Lucas digit products of the binomial expansion, with
integer-binomial crosschecks. It therefore avoids the triage module-normal-form
implementation.

The saved output evidence/research-check.json records:

- 236,775 exact coefficient comparisons: p=2,3,5,7,11,13,17,
  exponents -16..16, and n=0..1024.
- 29,799 additional direct integer-binomial checks through n=128.
- 112 finite kernel matrices: each p above and each radius R=1..16,
  with rows n=0..R(p-1). Their nullity is floor(R/(p-1)).
  Literal Laurent multiplication constructs P^k, 1<=k<=floor(R/(p-1));
  direct matrix annihilation and row rank verify that those vectors are a
  basis of that **finite-prefix** kernel.
- 207 exact digit-block certificates in evidence/digit-block-certificates.json.
  They include positive constant, linear, periodic, and geometric generators;
  D=0..3, p=2,3,5,7, a=0,1,p^2-1; plus D=4,8,16 with geometric generators
  for p=2,3,5,7,11 and a=p^4-1. Every allowed offset is checked.

All assertions passed. Every range is finite. The written proof, not these
computations, establishes the infinite statement and the all-prime scope.

## Two safeguards against overgeneralization

**Exact counterexample to an insufficient intermediate inference.**
Density-zero support does not imply nonrecurrence. Define W_0=1 and

    W_(m+1)=W_m 0^(4*|W_m|) W_m.

The nested prefixes define an infinite word w. It is recurrent: every finite
word occurs inside some W_m, and the second W_k inside W_(k+1), for all
k>=m, copies this occurrence at positions tending to infinity. Since
|W_m|=6^m and W_m has 2^m ones, for 6^m<=N<6^(m+1) the number of ones in
the first N positions is at most 2^(m+1), so its density tends to zero.
This familiar elementary construction is used only to check the logic of the
approach; no novelty is claimed for it.

**Exact boundary checks.** Q=1 gives (1,0,0,...), hence is not recurrent;
Q=P gives the zero word. For Q=x, (4) gives support {a_j:j>=1}, and the
consecutive gaps are p,p^2,p^3,... . Thus the word consisting of 1, then
p-1 zeros, then 1 occurs only at a_1=1. For p=2, Q=x has n=7 in its support
even though s_2(7)=3>deg(y); the shift in s_p((p-1)n+r) is essential.

## Operational limits

No agent, second Codex process, background worker, or proof assistant was used.
Live primary sources were read with the browser tool. Direct shell downloads
were rejected by network restrictions; this does not impair the mathematical
argument or the existing primary-source copy. No manuscript, publication PDF,
acceptance record, or release flag has been created.
