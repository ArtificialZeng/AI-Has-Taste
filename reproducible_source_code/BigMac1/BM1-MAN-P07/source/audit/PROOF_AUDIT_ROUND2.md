# Proof audit, editorial round 2

Status: **accepted as a certified finite result** on 2026-08-22.

## Certified claims

1. If a composite integer \(n\) satisfies \(\varphi(n)\mid n-1\), then
   \(P^+(n)\ge349\).
2. The 38 cap-347 sets surviving the complete 2-adic filter all contain 3
   and have \(2<n/\varphi(n)<3\).  A Lehmer solution among them would have
   index \(k=2\), while the local equation at 3 forces
   \(k\equiv1\pmod3\); hence one congruence rejects all 38.
3. The CRT--Dirichlet theorem in Section 4 is sound: infinitely many
   compatible prime sets can satisfy the strict ratio and full 2-adic
   conditions while failing a prescribed fresh odd Korselt component.

## Computational audit

`tests/run_full_certificate.sh` completed successfully.  It rebuilt the
cap-347 record, matched every frozen deterministic count, and completed the
independent tuple/trial-division replay.  The exact endpoint counts remain
27,179,711 selection attempts, 17,803,010 ratio-eligible sets, 38 two-adic
survivors, and zero Korselt or Lehmer survivors.  The obstruction unit tests
and the exact CRT verifier also passed.

The experimental pseudo-Boolean implication is mathematically sound, and
strict proofs close the indices 3, 4, and 5.  The index-2 run ended UNKNOWN,
without an UNSAT conclusion.  Therefore the partial solver artifacts are
excluded from the theorem's certificate and from all manuscript claims.

## Scope

The global Lehmer problem remains open.  No claim is made about a candidate
containing a prime greater than 347, and no absolute priority claim is made
for the numerical endpoint.  The independent adversarial details are in
`audit/ROUND2_REFEREE.md`.
