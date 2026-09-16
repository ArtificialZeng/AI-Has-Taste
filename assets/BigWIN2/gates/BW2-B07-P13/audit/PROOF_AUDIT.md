# Proof audit

Audit date: 2026-08-31 (Asia/Shanghai)  
Scientific status: **Proved**

## Referee reconstruction

1. Strict monotonicity of positive squares turns the adjacent-prime
   objective into the minimum of \(|p^3-q^2|\) over primes \(p,q\) with the
   stated bound on \(p\).
2. The difference cannot vanish by unique factorization.
3. Any improvement on 49,600 gives an integral solution
   \((X,Y,k)=(p,q,q^2-p^3)\) with \(0<|k|<49600\).
4. Bennett--Ghadermarzi's published classification covers all integral
   points for the larger range \(0<|k|\le10^7\) and supplies complete output.
5. The exact filter of that output has 98 sign-quotiented points in the
   required \(X\)-range.  Only four have prime \(X\); three have even
   \(|Y|>2\), and the fourth is the incumbent at absolute difference 49,600.
6. Complete \(n-1\) factorizations and Pocklington witnesses prove the two
   incumbent integers prime.  Exact integer square root proves that its
   square base is the adjacent prime below \(p^{3/2}\).

Therefore the lower and upper bounds coincide at 49,600.

## Mandatory mathematical checks

- [x] Formal theorem matches the source range and both inclusive endpoints.
- [x] The zero-difference case is excluded exactly.
- [x] Positive and negative differences are both covered.
- [x] Both signs of the Mordell coordinate \(Y\) are handled by \(|Y|\).
- [x] No floating-point value enters the proof.
- [x] The attaining pair is checked by exact arithmetic and exact primality
      certificates.
- [x] Every fatal or major gap in `proof/gap_ledger.md` is resolved.
- [x] Discovery and certification are separate implementations.
- [x] The published-completeness dependency is stated rather than hidden.

## Dependency boundary

The proof imports the complete integral-point classification of Bennett and
Ghadermarzi (2015).  The local checker independently verifies the posted
tables and this paper's filtering deduction, but does not rerun the authors'
month-long enumeration of binary cubic forms and Thue equations.  This
boundary is explicit in both the proof and manuscript.

No proof assistant was used.
