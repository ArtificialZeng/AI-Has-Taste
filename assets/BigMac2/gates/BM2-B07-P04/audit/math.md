# Fresh mathematical audit: exact Kasami verification at \(n=14\)

## Frozen scope and verdict

I reviewed the exact `resolution-paper` claim bound to snapshot digest
`7cbf2de6cf5efb98a779aaa9f3d99eddcd4a2cf57949737fbb9efb0193c66a72`.
The claim is the full assertion in `source.md`, not a weakened or sampled form:
for each \(k\in\{3,5\}\), the image set \(\Delta_k\) has size \(8192\), and
the stated triple count is \(2^{25}\) for every one of the \(16382\) elements
\(\rho\in\mathbb F_{2^{14}}\setminus\{0,1\}\). The two cases are separate,
the triples are ordered, and `Delta` is treated as a set rather than a
multiset.

**Verdict: accept.** The field construction, image sizes, character identity,
and every quantified count have exact reproducible certificates. The scope
resolves the frozen finite assertion and is explicitly confined to the
\(n=14\) layer.

## Reconstruction of the decisive argument

Let \(q=2^{14}\) and realize

\[
K=\mathbb F_2[\alpha]/(\alpha^{14}+\alpha^5+1)
\]

in the polynomial basis \((1,\alpha,\ldots,\alpha^{13})\), with the bits of an
integer encoding the corresponding coefficients. The certificate gives the
Rabin remainders

\[
X^{2^2}=\mathtt{0x0010},\qquad
X^{2^7}=\mathtt{0x08c5},\qquad
X^{2^{14}}=X
\]

modulo \(X^{14}+X^5+1\), and the first two remainders minus \(X\) have gcd one
with the modulus. These are exactly the tests for the prime divisors \(7\) and
\(2\) of degree \(14\), so the quotient is a field of order \(q\). The
separate checker establishes the same fact without Rabin remainders: it tries
all \(1+2+\cdots+64=127\) monic, constant-one polynomials of degrees at most
seven and finds no divisor. A reducible degree-fourteen polynomial with
constant term one would have such a factor.

The exponents are \(2^6-2^3+1=57\) and
\(2^{10}-2^5+1=993\). Exact enumeration of all \(16384\) inputs to

\[
\delta_k(t)=t^{d_k}+(t+1)^{d_k}+1
\]

shows, for each exponent, precisely \(8192\) image values, each with exactly
two preimages. Thus both required image-size statements hold, and subsequent
membership arrays represent sets.

For the indicator \(1_{\Delta_k}\), put

\[
S_k(a)=\sum_{x\in\Delta_k}(-1)^{\operatorname{Tr}(ax)}.
\]

Additive-character orthogonality gives, with no limiting or probabilistic
step,

\[
\begin{aligned}
N_k(\rho)
&=\sum_{x,y,z\in\Delta_k}
  \frac1q\sum_{a\in K}
  (-1)^{\operatorname{Tr}(a(x+\rho y+(1+\rho)z))}\\
&=\frac1q\sum_{a\in K}
  S_k(a)S_k(a\rho)S_k(a(1+\rho)).
\end{aligned}
\]

Here \(\rho\ne0,1\), so neither multiplication parameter is accidentally
zero. The saved certificate contains all \(16384\) values of \(S_k\) for each
\(k\) and a row for every encoded \(\rho=2,\ldots,16383\). For every one of
the \(32764\) count rows, the sum over \(a\ne0\) is exactly zero. Since
\(S_k(0)=|\Delta_k|=8192\), the full sum is

\[
8192^3=2^{39}=549755813888,
\]

and division by \(q=2^{14}\) gives \(N_k(\rho)=2^{25}=33554432\).
This establishes every quantifier in the claim.

## Checks actually performed

- I checked the producer and checker source line by line, including the field
  arithmetic, trace pairing, transform indexing, certificate coverage, and
  integer types. The Walsh transform is reindexed by the explicit dual mask
  \(a\mapsto(\operatorname{Tr}(a\alpha^i))_i\), so it computes the character
  sums in the displayed formula rather than an unrelated bit-dot transform.
- I compiled both programs afresh with C11, optimization, and
  `-Wall -Wextra -Wpedantic`; compilation was warning-free. Running the
  producer recreated a certificate byte-for-byte identical to
  `evidence/n14_certificate.tsv`, with SHA-256
  `7f8d716a216aab3da464a26cbcb027060adcba50718762059ccd636ce7ae3d69`.
- I ran the separate checker against the frozen certificate. It reconstructed
  the two image sets using carryless multiplication plus polynomial long
  division, recomputed all \(32768\) Walsh coefficients by direct character
  sums, and recomputed all \(32764\) full correlations through polynomial-basis
  linear multiplication maps. Every comparison passed.
- That checker also directly enumerated \(8192^2\) pairs at the held-out
  encodings \(\rho=\mathtt{0x1555}\) and
  \(\rho=\mathtt{0x3ffe}\) for each \(k\); all four counts were
  \(33554432\). The producer's disjoint direct checks at
  \(\mathtt{0x0002}\) and \(\mathtt{0x2000}\) also passed for both cases.
- I repeated both runs under AddressSanitizer and UndefinedBehaviorSanitizer.
  There were no sanitizer findings, and the sanitized producer again emitted
  a byte-identical certificate.
- All decisive arithmetic is integral. The only floating-point value in the
  producer is an informational elapsed-time calculation after the certificate
  has been closed; it cannot affect any mathematical output. The largest
  possible accumulated character sum is below \(2^{53}\), safely within the
  signed 64-bit accumulators used.
- The hashes of `source.md`, `problem.md`, `claim.json`, and every decisive
  local evidence file inspected agree with the snapshot mapping. I did not use
  owner confidence, prior verdicts, progress summaries, or `checkpoint.md` in
  reaching this decision.

## Source comparison and contribution

I checked the cited primary source, Nagy--Vajda,
[*On a conjecture on the Kasami APN function*](https://arxiv.org/pdf/2608.18584),
arXiv:2608.18584v2. Its Conjecture 1.1 is the same ordered-triple assertion;
Proposition 4.1 gives the same normalization by
\(\rho=v_2/v_1\) and nonzero-character correlation; Lemma 3.5 gives the
\(k\leftrightarrow n-k\) Frobenius symmetry. Section 12 and Theorem 13.1 state
exhaustive verification only through \(n\le13\), proofs for residue classes
\(\pm1,\pm2\), and that the other residue classes remain open.

At \(n=14\), the admissible residues are \(1,3,5,9,11,13\); the established
\(\pm1\) cases cover \(1,13\), while symmetry pairs \(3\) with \(11\) and
\(5\) with \(9\). Thus the two cases certified here are exactly the two new
representatives needed for the next complete finite layer. This is a concrete,
non-toy extension of the source's exhaustive range. A limited exact-phrase
arXiv search on 2026-09-07 found no separate report of this \(n=14\) layer;
that observation is a bounded literature check, not a claim of priority.

## Limits and unresolved matters

There is no unresolved mathematical gap in the frozen finite claim. The
computation does not prove the conjecture for arbitrary \(n\), does not supply
a uniform theoretical mechanism, and does not establish publication novelty
by itself. Those limits are already stated honestly in the candidate scope and
do not weaken the resolution of `source.md`.
