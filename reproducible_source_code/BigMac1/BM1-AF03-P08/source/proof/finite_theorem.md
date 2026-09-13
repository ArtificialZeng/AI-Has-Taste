# Certified finite theorem for n=10

## Result

Let $v_{10}=[3,4,5,6,7,8,9,10,1,2]$.  For every comparable pair

\[
e\le u\le v\le v_{10},
\]

there are integers $k\ge0$ and $h_1,\ldots,h_k\ge2$ such that

\[
\widetilde R_{u,v}(q)
=q^{\ell(v)-\ell(u)}\prod_{i=1}^kF_{h_i}(q^{-2}).
\]

The empty product covers (u=v).  This is a computer-assisted exact finite
theorem for $n=10$; it is not a proof for arbitrary $n$.

## Proof certificate argument

The standalone verifier in `certificates/verify_n10.cpp`, launched by
`certificates/verify_certificate.py`, proves the finite statement as follows.

1. **Universe completeness.**  It visits all $10!$ permutations and retains
   exactly those passing the rank-matrix criterion $w\le v_{10}$.  It then
   independently constructs the products of all (2^{16}) subwords of
   \(Omega_{10}=s_2s_1\cdots s_9s_8\), deduplicates them, and requires exact
   set equality.  Both methods give 12,866 elements.
2. **Pair completeness.**  It applies the rank-matrix criterion to every
   ordered pair of retained elements.  Exactly 6,229,297 pairs are comparable.
   The pair universe is regenerated; no discovery-supplied pair list or hash
   is accepted as evidence.
3. **First exact evaluator.**  Write
   $\widetilde R_{u,v}(q)=q^dB_{u,v}(q^{-2})$, where
   $d=\ell(v)-\ell(u)$.  Dyer's recurrence becomes
   \[
   B_{u,v}=B_{us,vs}\quad(s\in D_R(u)),
   \qquad
   B_{u,v}=B_{u,vs}+xB_{us,vs}\quad(s\notin D_R(u)),
   \]
   with an incomparable second term interpreted as zero.  Processing upper
   endpoints by increasing length makes this an exact induction from
   $B_{u,u}=1$.  All operations use guarded integers.
4. **Complete monoid decision.**  Since
   \(\deg F_h=\lfloor h/2\rfloor\), any factor in a product of degree at most
   eight has (2\le h\le17).  The verifier recursively enumerates every
   nondecreasing multiset of indices in this finite range whose total degree
   is at most eight, multiplying coefficient vectors in \(\mathbb Z[x]\).
   This yields 434 distinct allowed product polynomials, including the unit.
   Each newly reconstructed $B_{u,v}$ must equal one catalogued product;
   otherwise the verifier stops with the exact pair and polynomial.
5. **Second exact evaluator.**  Independently of the normalized Dyer
   recurrence, the same complete pair universe is processed using the
   ordinary $R$-polynomial recurrence
   \[
   R_{u,v}(Q)=Q R_{us,vs}(Q)+(Q-1)R_{u,vs}(Q)
   \]
   in the non-descent branch.  For each gap $d$, allowed normalized
   polynomials are mapped exactly through
   \[
   R_{u,v}(z^2)=z^d\widetilde R_{u,v}(z-z^{-1}).
   \]
   The ordinary recurrence result must land in the same unique class as the
   normalized recurrence result for every pair.
6. **Pattern, baseline, and fail-closed checks.**  The verifier independently
   enumerates every nondecreasing index multiset with $h_i\ge2$ and
   $\sum_i h_i\le n-2$ and requires its class set to equal the set observed
   among all pairs.  The identical verifier also reconstructs the complete
   cases $2\le n\le9$, reproducing the source's last claimed
   baseline.  It rejects missing/duplicate/unknown fields, a wrong endpoint,
   an overflowing endpoint, a changed reduced word or Fibonacci recurrence,
   and a false complete-pair count.  The eight-case destructive-input suite
   passes.

The verifier returns success only after all six steps.  Its exact $n=10$
summary is

```text
interval=12866
pairs=6229297
distinct_B=22
max_coefficient=15
index_sum_patterns=true
fingerprint=0x78cf5914f6aaeb37
all_pairs_factor=TRUE
dual_recurrence=TRUE
```

The displayed 64-bit fingerprint is only a deterministic change detector.
The certificate and source are bound cryptographically by SHA-256 in the
release manifest.

## Independent breaker route

The discovery program `experiments/breaker/exhaustive_rtilde.cpp` is not
imported by the verifier.  It uses subwords of retained reduced words to
enumerate each lower interval, cross-checks the top interval by downward
Bruhat-cover BFS, and separately catalogs exact normalized products.  Two
deterministic full runs and an AddressSanitizer/UndefinedBehaviorSanitizer run
agree on zero rejected pairs and the exact counts above.  A separate Python
implementation enumerates all of $S_n$, uses rank-matrix comparability,
stores uncompressed polynomials in $q$, and decides membership by exact
integer polynomial division through $n=8$.

## Limitation and structural signal

The full all-$n$ conjecture is not proved.  The finite verifier certifies that the 22
factor patterns occurring at $n=10$ are exactly the products indexed by
partitions with parts $h_i\ge2$ and $\sum_i h_i\le8=n-2$.  The analogous
statement is exactly checked in every computed dimension $2\le n\le10$.
Until a heap or
interval decomposition proves this bound and realizes the factors as
independent blocks, it remains a discovery observation rather than a general
theorem.
