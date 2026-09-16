# Triage evidence: quotient reduction and slice obstruction

Provenance: `win-00082-p01-triage-2a3e4d3c3cc7`  
Date: 2026-09-09

This is triage evidence, not an accepted proof.  It records a prospective direct
nonexistence argument for independent checking.

## Derivation from the source lemma

Assume an ordering exists and let
\(S=\{s_v:v\in[8]\}\subseteq\mathbb Z_{70}\).  The shifts are distinct.  Direct
counts give
\[
 |S|=8,\qquad |D|=35,\qquad
 1_S*1_D=4\,1_{\mathbb Z_{70}},
\]
and, for distinct \(b,c\in S\),
\[
 |(D+b)\cap(D+c)|=\binom62=15.
\]
Lemma 2.2 of arXiv:2609.06724v1 therefore gives
\(15(T-8b)=0\) in \(\mathbb Z_{70}\) for every \(b\in S\), where
\(T=\sum_{c\in S}c\).  Subtracting the equations for \(b,b'\) gives
\[
 120(b-b')=0\pmod {70}.
\]
The kernel of multiplication by \(120\) on \(\mathbb Z_{70}\) is
\(7\mathbb Z_{70}\), of order \(\gcd(120,70)=10\).  After translating all
shifts, write \(S=7A\), where \(A\subseteq\mathbb Z_{10}\) and \(|A|=8\).
This derives the ten-element quotient; it is not imposed as a symmetry ansatz.

For \(j\in\{0,\ldots,6\}\), set
\[
 D_j=\{x\in\mathbb Z_{10}:j+7x\in D\}.
\]
At time \(j+7x\), the reconstructed attendee set is
\[
 C_{j,x}=A\cap(x-D_j).
\]
Consequently each slice obeys
\[
 1_A*1_{D_j}=4\,1_{\mathbb Z_{10}},\qquad |D_j|=5.
\]

## Elementary classification of every reduced slice

Put \(B=\mathbb Z_{10}\setminus A\), so \(|B|=2\).  Since
\(1_{\mathbb Z_{10}}*1_{D_j}=5\), the slice equation is equivalent to
\[
 1_B*1_{D_j}=1_{\mathbb Z_{10}}.
\]
Thus \(B+D_j\) is a unique factorization of \(\mathbb Z_{10}\).  Translate
\(B\) to \(\{0,d\}\).  Its equation says that the binary indicator of
\(D_j\) alternates around every orbit of translation by \(d\).  Hence
\(\operatorname{ord}(d)\) must be even, so \(d\) is odd.

If \(d\ne5\), translation by \(d\) is a ten-cycle, and the only two templates
are the even and odd residue classes.  Then every \(C_{j,x}\) is one of only
two four-sets (the four available vertices of one parity), contradicting the
fact that the ten times on even one slice must have distinct values under the
bijection \(e\).

If \(d=5\), then \(B\) is one coset of \(H=\{0,5\}\) and every \(D_j\) is a
transversal of the five \(H\)-cosets.  Every translate/reflection \(x-D_j\) is
also a transversal.  Since \(A\) is the union of the other four \(H\)-cosets,
each reconstructed column contains exactly one point from each of those four
cosets.  Across all slices this permits at most \(2^4=16\) different four-sets,
whereas bijectivity requires all \(\binom84=70\).  This is again a
contradiction.

## Independent finite check

`evidence/triage_enumerate.py` loops over all
\(\binom{10}{8}\binom{10}{5}=11{,}340\) pairs \((A,D_j)\), tests the ten
convolution equations directly, and reconstructs all ten columns for every
valid pair.  Its asserted/run output is:

```
A_count=45 D_per_A=252 tested_pairs=11340 valid_pairs=200
valid_A_count=25 target_columns_per_A=70 exact_cover_possible=no
```

For the twenty valid complements with odd difference other than five there
are two templates and only two accessible columns.  For the five antipodal
complements there are 32 templates and only 16 accessible columns.  The script
prints the complete 45-complement table and, for all 200 valid pairs, the
template bitmask and all ten reconstructed column bitmasks.  It exited zero on
2026-09-09 under Python 3.

## Literature boundary checked at triage

- Zhou, arXiv:2609.06724v1, Definition 1.1, Lemma 2.2, and pp. 8--9, inspected
  at <https://arxiv.org/pdf/2609.06724> on 2026-09-09: higher uniformities are
  explicitly left open and Conjecture 7.1 predicts nonexistence here.
- Gregor--Merino--Mütze, arXiv:2205.08126, Theorems 4.5--4.8, inspected at
  <https://arxiv.org/pdf/2205.08126> on 2026-09-09: their one-track Hamilton
  construction covers the coprime case; their noncoprime Johnson-graph results
  do not assert the relaxed eight-column single-track property here.
- Schwartz--Etzion, *IEEE Trans. Inform. Theory* 45 (1999), Definition 4,
  inspected at <https://etzion.net.technion.ac.il/files/2016/02/P54.pdf> on
  2026-09-09: a single-track Gray code also requires Gray adjacency, so its
  claims do not directly settle this adjacency-free full-layer instance.

Exact-assertion searches found no resolution beyond the September 2026 source.
That limited search is not evidence of novelty or priority; a full cited-chain
screen remains required before any release claim.
