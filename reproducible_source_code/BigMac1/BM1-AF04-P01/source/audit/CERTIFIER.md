# Certifier record

Date: 2026-08-30 CST.  Role executed after Breaker.

Certificate: `certificates/annihilator_certificate.json`.

Independent verifier: `certificates/verify_certificate.py`.  It uses only the
Python standard library, imports no discovery module, parses exact integer
polynomial data, rebuilds rational-function arithmetic, and fails closed on
unknown fields, missing fields, wrong types, zero denominators, or failed
identities.

Successful checks:

- reconstructed state system to (L_3);
- noncommutative Ore left product to (L_5);
- (L_5) to the five recurrence coefficients;
- formal square-root/exponential Taylor coefficients through (a_8);
- recurrence residuals for every available boundary (4\le n\le8).

Recorded success hashes from the first certified run:

- certificate SHA-256:
  `8d31bebf230f3a3eda53d881f5094573d6fcee8406619e27878fbffa95b3a1ba`;
- verifier SHA-256:
  `86232f3821c5d37b6c7c6b40729b34faf98418d24eaa69829ceadf440e958982`.

Mutation suite result: one changed (L_5) coefficient, one missing definition,
one unknown top-level field, and one string-valued coefficient were all
rejected.  The finite matching enumerator is a separate implementation and is
not part of the decisive universal proof.
