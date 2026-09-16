# Quadratic finite-field q-hit residue

## Frozen interpretation

The original statement is `source.md`, preserved byte-for-byte. For every integer
n >= 1, every board B subset [n] x [n], every d in {0,...,n}, and every prime power
q = p^a (p prime, a >= 1), let F_q be the field of q elements. Define

- supp(A) = {(r,c): A[r,c] != 0} for A in Mat_n(F_q).
- m_i(B,q) = #{A: supp(A) subset B and rank_Fq(A) = i}.
- M_i(B,q) = m_i(B,q)/(q-1)^i, with M_0 = 1.
- [k]!_q = product_{j=1}^k (1+q+...+q^(j-1)), including [0]!_q = 1.

The hit numbers are defined by the exact finite identity

    sum_{d=0}^n H_d(B,q) t^d
      = q^(n(n-1)/2) sum_{i=0}^n M_i(B,q) [n-i]!_q
          product_{j=0}^{i-1} (t q^(-j)-1).

Empty products equal 1. These are the finite-field matrix q-hit numbers for
arbitrary square boards. The leading power of q cancels all possible negative
powers in the expanded summands, so H_d is integer-valued on prime powers.

Let S = {p^a-1: p prime, a >= 1}. For each fixed (n,B,d), the premise gives a
polynomial P_B,d(x) = c_0+c_1 x+c_2 x^2 in Z[x], of degree at most two, such that

    H_d(B,x+1) - P_B,d(x) belongs to x^3 Z for every x in S.

This is integer congruence on an unbounded domain, not a claim that H_d is a
polynomial function. Existence follows from the published residue theorem below.
Uniqueness follows because the difference of two such polynomials has degree at
most two: divided by x^3 it is an integer tending to zero along S, so the
difference vanishes at infinitely many x and is identically zero.

The original target is: c_2(B,d) >= 0 for all the above n,B,d. A disproof requires
one fully specified board, index d, and an exact negative quadratic residue.
Testing only finite q values without a justified reconstruction theorem is
insufficient. Empty/full boards and d=0,n are included. Neither positivity for
Ferrers boards nor positivity of numerical H_d values replaces this target.
No correction or weakening of the source statement is proposed.

## Nearest prior result and proposed contribution

Chen and Selover, *Positivity properties of q-hit numbers in the finite general
linear group*, ECA 6:3 (2026), S2R22, DOI 10.54550/ECA2026V6S3R22:
[primary journal PDF](https://ecajournal.haifa.ac.il/Volume2026/ECA2026_S2A22.pdf).
The definition is on p. 2; Corollary 3.13 (p. 7) supplies integer polynomial
residues modulo x^6; Theorem 4.10 (p. 14) proves c_1 >= 0. Conjecture 4.1 (p. 8)
includes the present degree-two question; Section 5 (p. 15) discusses its
alternating expansion. The cached journal PDF and corresponding text were
re-inspected, and live arXiv history still lists only v1. Source status:
**open-supported within the inspected literature**, without a priority guarantee.

Nearest result X: universal linear positivity and existence of the quadratic
residue. Proposed delta Y: universal quadratic positivity. The research pass
produced a candidate proof using balanced row/column restriction convolution:
the quadratic hit family has a kernel supported on board sizes at most four,
and every coefficient of each of those finite kernels is nonnegative.
The locality argument and all-board certificates are in
`evidence/quadratic_locality_proof.md`. This is a full-scope resolution candidate;
fresh mathematical review is pending and no acceptance is asserted.

## Research pass 1 candidate and precise scope

The proposed theorem is exactly c_2(B,d)>=0 for every n>=1, every board
B subset [n]^2 and every d in {0,...,n}, with the prime-power residue definition
above. The proposed proof does not assume H_d is a polynomial for arbitrary B.
It also gives the identity C_2=h*K_2 for the balanced restriction convolution,
where K_2 is zero above size four and is coefficientwise nonnegative in the
remaining sizes. No higher-order positivity claim is submitted.

The assigned all-board n=4 test is complete: 327,680 board/index pairs, with
no negative quadratic coefficient. The subsequent locality certificate covers
all 329,780 pairs at sizes 1--4, with a second complete computation using a
different algorithm. Orbit counts were checked using determinant ranks over
F_2,F_3,F_4,F_5,F_7,F_8 and reconstructed again. Larger structured and deterministic
test cases through n=8, including the Fano board, agree with the proposed
identity. These checks support the proof and do not replace its locality lemma.

The new literature comparison is `literature/research-screen.md`. The decisive
local primary journal PDF/text are copied to `evidence/external/` and will be
bound in `claim.json`. No handoff files were present. The earlier bounded
historical comparison and its limitations remain in `literature/triage-screen.md`.

One next test: a fresh referee should audit the universal locality identity,
especially the dummy-permutation decomposition, and reproduce the finite
nonnegative kernel certificate. The candidate is not yet accepted.
