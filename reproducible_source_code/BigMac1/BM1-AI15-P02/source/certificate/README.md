# Exact certificate and independent verification

The main serialized input is `a321614_certificate.json`. It contains:

- the complete twelve local states and their `0/1` adjacency matrix;
- the three state involutions and center-edge/center-state vectors;
- a 68-dimensional integer linear representation of the four Burnside
  branches;
- Barker's numerator and denominator;
- the vector `w=D^rev(B)b` and the 68 exact observable moments
  `ell*B^k*w=0` for `0 <= k < 68`;
- an exact rational Bezout identity proving `gcd(N,D)=1`.

The verifier does not import the generator. It reconstructs the states,
matrix, group action and global representation from the board rules, checks
the serialized objects and hashes, recomputes all 68 zeros, invokes only the
standard Cayley–Hamilton implication, checks all 22 OEIS terms, and verifies
the Bezout identity.

Run:

```bash
python3 code/build_certificate.py
python3 code/verify_certificate.py certificate/a321614_certificate.json
python3 agents/builder/verify_certificate.py
python3 agents/breaker/verify_audit.py agents/breaker/audit_output.json
```

The builder certificate supplies the smaller polynomial matrix identity
`Z(y)(I-yT)=D0(y)1^T`; the root certificate supplies a structurally separate
Cayley–Hamilton proof. The breaker certificate is definition-level finite
enumeration used to falsify boundary and group interpretations, not to infer
the all-`n` theorem.
