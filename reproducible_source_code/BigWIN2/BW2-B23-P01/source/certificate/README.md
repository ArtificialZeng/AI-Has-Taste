# Exact certificate

Run:

```bash
python3 code/derive_identity.py
python3 code/verify_certificate.py 2000
```

The first command verifies the generating-function identities symbolically by
polynomial expansion.  The second uses only Python integer arithmetic, builds
the nonlinear and linear sequences independently, checks their agreement,
checks the positive defect recurrence, and checks the exact coefficient
inequality used in the infinite induction.  The finite term scan is a
cross-check, not the proof of the universal claim.
