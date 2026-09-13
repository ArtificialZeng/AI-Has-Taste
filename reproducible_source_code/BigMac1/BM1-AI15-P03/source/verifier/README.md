# Independent zero-set verifier

Run from the project root:

```bash
python3 verifier/verify_zero_set.py verifier/certificate.json
```

The input is exact JSON.  The verifier fails closed on missing or unexpected
fields and uses only integer arithmetic and the Python standard library.

It performs three logically distinct checks:

1. enumerates every cyclic `+/-` difference word for `6 <= n <= 20` and
   recovers the exact counts in the certificate;
2. reconstructs the graph edge sets and independently exhausts proper
   three-colour assignments for every `6 <= n <= 20`, reproducing the same
   exact counts (fixing vertex 0 to colour 0 only by colour relabelling
   symmetry);
3. checks the finite algebraic and local invariants behind the three infinite
   constructive families.  Concrete instances are additionally converted to
   colours and checked directly against reconstructed graph edges.

The script prints SHA-256 digests of both itself and its serialized input.
No SAT solver, CAS, floating-point arithmetic, or proof assistant is used.
