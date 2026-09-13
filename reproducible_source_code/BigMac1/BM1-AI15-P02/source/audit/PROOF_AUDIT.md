# Proof audit

Status: **PASS** (2026-08-29).

## Audited theorem

For the fixed four-element rectangle subgroup
\(G=\{1,h,v,hv\}\), including on the exceptional square board at
\(n=2\), the A321614 orbit sequence has the reduced generating function

\[
\frac{1-8x+29x^2-52x^3+34x^4+11x^5-8x^6-15x^7+6x^8}
{1-12x+54x^2-98x^3-17x^4+346x^5-505x^6+210x^7+120x^8-126x^9+27x^{10}}.
\]

Consequently Barker's order-ten recurrence holds for every \(n\ge10\),
and order ten is minimal for the scalar sequence.

## Exact proof gates

1. `code/verify_certificate.py` reconstructs the twelve block states from
   the king attack rule, reconstructs the adjacency and symmetry maps, and
   rejects any mismatch with the serialized certificate.
2. It embeds the four Burnside branches into a 68-dimensional integer
   linear representation.  All 68 exact observable moments of the claimed
   denominator applied to that representation vanish.  Cayley--Hamilton
   therefore proves the annihilation for all subsequent moments.
3. It verifies the exact rational Bezout identity for the displayed
   numerator and denominator, so no cancellation is possible.
4. The structurally different builder certificate verifies the polynomial
   resolvent identity
   \(Z(y)(I-yT)=D_0(y){\bf1}^{T}\) coefficient by coefficient over the
   integers, then derives all four branch generating functions.
5. The breaker implementation independently enumerates state words through
   \(n=80\), raw placements through \(n=6\), and verifies the recurrence
   throughout its audited range.  These checks are corroboration, not the
   all-\(n\) inference.
6. The referee independently reconstructed the 12-state isomorphism and all
   144 adjacency entries; its second-round report records no fatal or major
   mathematical gap for the repaired theorem.
7. A third, no-import verifier independently reconstructs the root
   certificate using only the Python standard library.  It verifies the
   68-dimensional representation, 68 observable zero moments, final
   numerator/denominator, and Bezout identity without importing discovery or
   verifier code.

## Reproduction and fail-closed results

Command `make verify` exited 0 and reported:

- root certificate: `PASS`, 12 states, global dimension 68, 68 zero
  moments, denominator degree 10, 22/22 OEIS prefix terms;
- builder certificate: `VERIFIED`, denominator degree 10, gcd 1;
- breaker certificate: `VERIFIED rows=0..80`, recurrence `n=10..80`, and
  exact convention counts `D2=23`, `D4=14` at `n=2`;
- clean LaTeX target and citation audit: 4 cited, 4 bibliography records,
  0 missing, 0 unused.

All three verifiers were tested with genuine, bad-matrix, and drop-key inputs
under Python 3.9.6 and 3.14.7, in both normal and `-O -I` modes.  The 12
genuine runs passed and all 24 tampered runs failed.  The reusable command is
`python3 code/test_fail_closed.py --python /usr/bin/python3 --python
/opt/homebrew/bin/python3`.

## Frozen SHA-256 values

| Artifact | SHA-256 |
|---|---|
| `certificate/a321614_certificate.json` | `af61e215342a301910f4684ea124f34f99135a1a50a4ff3105e637af7c33de65` |
| `code/verify_certificate.py` | `afef4c0886194f1d01f65a606fbc8ae3065e6fd6ea31ed81564f6e78656d3e65` |
| `agents/builder/certificate.json` | `7cbf65615520b672fed1530157ad510a41b7bb49170b23c4ee1c507d36bef128` |
| `agents/builder/verify_certificate.py` | `c75d00e45f89c3d7f3ae82abab9e0fa7baaec38ff0e2eea3ad3e01d9f9b11a6a` |
| `agents/referee/verify_no_import.py` | `44f15b093e431f96095a02d7c010c51c8836b005f5f679474154c2b5a77a8ddc` |
| `agents/breaker/audit_output.json` | `b9974cf701c0598e8edc2fc26ccb4ccc77e15a8898d4de7b173723b6fe17c4f6` |
| `agents/breaker/verify_audit.py` | `a272e74bd6773fddc8971588670fd0dbc773c3ba8a5351d53c88263051f9963e` |
| `paper/main.pdf` | `bfcd1dcfab157ad1f7b7fefdc021e4275726d93053d32b32630e2d78695c5587` |

## Scope limitation

The phrase “all symmetries” cannot literally mean the full eight-element
square group at \(n=2\): that convention gives 14 rather than 23 orbits and
changes the recurrence residuals at \(n=10,11,12\).  The proved theorem
uses the convention encoded by A321614's values: the same four rectangle
operations for every \(n\).

No proof assistant was used.  Every decisive check is exact integer or
rational arithmetic in the supplied independent verifiers.
