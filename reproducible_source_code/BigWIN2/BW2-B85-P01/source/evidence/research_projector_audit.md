# Independent exact projector certificate

Job: `win-00085-p01-research-fce2de65d535`  
Date: 2026-09-10 (Asia/Shanghai)  
Checker: `evidence/research_projector_audit.py`

This is an independent reconstruction of the proposed certificate.  The
checker does not import or call `evidence/triage_exact_check.py`.  It uses the
ordinary dense matrices for (I,X,Y,Z) over exact Gaussian integers, obtains
the eight group elements by dense matrix multiplication, constructs every
code projector, performs each partial trace entry by entry, and computes each
rank by Gaussian elimination over ℚ(i).  A clean run ends in `AUDIT_OK`.

## Projector and marginal identities

For each of the four commuting independent generator triples, dense matrix
multiplication gives eight distinct Hermitian elements and verifies

\[
 R_S=\sum_{g\in S}g,\qquad R_S^2=8R_S,\qquad
 \operatorname{Tr}R_S=2^n,\qquad
 \operatorname{rank}R_S=2^{n-3}.
\]

Thus the code projector is (P_S=R_S/8), and its trace-one normalization is

\[
 \rho_S=\frac{P_S}{2^{n-3}}=2^{-n}\sum_{g\in S}g.
\]

For (A\subseteq[n]), direct entrywise partial trace agrees in every one of
the (2^n) cases with

\[
 \operatorname{Tr}_{A^c}\rho_S
 =2^{-|A|}\sum_{\substack{g\in S\\\operatorname{supp}(g)\subseteq A}}g|_A.
\]

The summation set is a subgroup of order (2^{d_S(A)}).  Dividing its sum by
that order gives its joint (+1)-eigenspace projector, of rank
(2^{|A|-d_S(A)}).  Hence

\[
 \operatorname{rank}(\operatorname{Tr}_{A^c}\rho_S)
 =2^{|A|-d_S(A)}.
\]

The checker verifies this equality independently for all 192 pairs
`(code, A)` (32 for each five-qubit code and 64 for each six-qubit code).

## Full signed Pauli and support tables

The selector bits, from right to left, select the displayed generators in
their listed order.

| code | selector | signed Pauli | support |
|:---|---:|:---|:---|
| (S_A) | `000` | `+IIIII` | ∅ |
| | `001` | `+ZZZZI` | 1234 |
| | `010` | `+XXIIX` | 125 |
| | `011` | `-YYZZX` | 12345 |
| | `100` | `+IIXXX` | 345 |
| | `101` | `-ZZYYX` | 12345 |
| | `110` | `+XXXXI` | 1234 |
| | `111` | `+YYYYI` | 1234 |
| (S_B) | `000` | `+IIIII` | ∅ |
| | `001` | `+ZZIZX` | 1245 |
| | `010` | `+XIZXI` | 134 |
| | `011` | `-YZZYX` | 12345 |
| | `100` | `+IXXYI` | 234 |
| | `101` | `+ZYXXX` | 12345 |
| | `110` | `-XXYZI` | 1234 |
| | `111` | `+YYYIX` | 1235 |
| (S_+) | `000` | `+IIIIII` | ∅ |
| | `001` | `+XXIIXX` | 1256 |
| | `010` | `+IIXXXX` | 3456 |
| | `011` | `+XXXXII` | 1234 |
| | `100` | `+ZZZZIX` | 12346 |
| | `101` | `-YYZZXI` | 12345 |
| | `110` | `-ZZYYXI` | 12345 |
| | `111` | `+YYYYIX` | 12346 |
| (S_-) | `000` | `+IIIIII` | ∅ |
| | `001` | `+XXZXII` | 1234 |
| | `010` | `+ZZXYII` | 1234 |
| | `011` | `+YYYZII` | 1234 |
| | `100` | `+IZZZXX` | 23456 |
| | `101` | `-XYIYXX` | 12456 |
| | `110` | `+ZIYXXX` | 13456 |
| | `111` | `-YXXIXX` | 12356 |

Equivalently, the four exact signed Pauli sums are the eight rows of each
block above multiplied respectively by (2^{-5},2^{-5},2^{-6},2^{-6}).

## Complete marginal-rank profiles

These compact rules list every subsystem.  An unlisted subsystem of a listed
cardinality has the stated default rank.

- (S_A): for ∣A∣ ≤ 2 the rank is (2^{|A|}).  For triples it is 4
  exactly at 125 and 345, and 8 otherwise.  For four-subsets it is 4 at
  1234 and 8 at the other four.  The full-system rank is 4.
- (S_B): for ∣A∣ ≤ 2 the rank is (2^{|A|}).  For triples it is 4
  exactly at 134 and 234, and 8 otherwise.  For four-subsets it is 4 at
  1234 and 8 at the other four.  The full-system rank is 4.
- (S_+): for ∣A∣ ≤ 3 the rank is (2^{|A|}).  For four-subsets it
  is 8 exactly at 1234, 1256, and 3456, and 16 otherwise.  For five-subsets
  it is 8 at 12345 and 12346, and 16 at the other four.  The full-system
  rank is 8.
- (S_-): for ∣A∣ ≤ 3 the rank is (2^{|A|}).  For four-subsets it
  is 4 exactly at 1234, and 16 otherwise.  For five-subsets it is 8 at
  12345 and 12346, and 16 at the other four.  The full-system rank is 8.

The empty-subsystem rank is 1 in all four cases, as included by the first
rule in each block.

## Separating certificates and proof

If normalized code projectors are related by a product unitary, then tracing
out (A^c) cancels the unitary factors on (A^c) and conjugates the reduced
operator by the product unitary on (A).  Its rank is therefore unchanged.
A qubit permutation merely relabels (A).  Consequently, LU-plus-permutation
equivalence requires the two indexed marginal-rank profiles to be related by
one coordinate permutation.

For (S_A), the rank-4 triples are 125 and 345, whose intersection has size
1.  For (S_B), they are 134 and 234, whose intersection has size 2.  A
permutation preserves intersection size, so no permutation can coordinate
the profiles.  Hence (E_5) is false.

For (S_+), the rank histogram over the fifteen four-subsets is
({8:3,16:12}).  For (S_-), it is ({4:1,16:14}).  A permutation
preserves this histogram, so no permutation can coordinate the profiles.
Hence (E_6) is false.

This resolves only the two concrete assertions frozen in `source.md`.  The
general marginal/support invariant is prior art; the contribution is its
explicit exact application and the two small incidence certificates here.

