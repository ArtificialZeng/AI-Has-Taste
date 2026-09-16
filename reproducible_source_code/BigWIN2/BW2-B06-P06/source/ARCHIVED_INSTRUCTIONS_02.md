# Exact certificate for the finite result on P_11

## Result certified

The certificate proves the upper bound
\[
\operatorname{Var}M_{P_{11}}f\le\frac{10}{11}\operatorname{Var}f.
\]
The endpoint point mass supplies the matching lower bound.

## Files

- `p11_radius_certificate.json`: format, exact target, counts, and payload
  bindings.
- `p11_radius_certificate.bin`: one comparison radius byte per adjacent
  nonzero sign-coefficient pair, in canonical chamber order.
- `p11_fractional_exceptions.json`: exact rational negative-ball mixtures for
  the 10 chambers not covered by the pure-radius search.
- `../code/verify_radius_certificate.py`: independent fail-closed verifier.
- `../code/generate_radius_certificate.py`: discovery/generation program; it
  is not trusted by the verifier.

## Verification

From the project root, using Python 3.10 or newer and no third-party package:

```bash
python3 code/verify_radius_certificate.py \
  certificates/p11_radius_certificate.json \
  certificates/p11_radius_certificate.bin
```

Expected summary:

```text
status: VERIFIED
n: 11
target: 10/11
chambers: 5874849
slots: 45011088
fractional_exceptions: 10
```

The verifier independently enumerates sign patterns and positive active
radii. It builds signed rational uniform measures on vertices and checks that
their total mass is zero and that every cumulative edge flux has magnitude at
most \(10/11\). It rejects malformed structure, invalid radii, wrong rational
masses, truncation, trailing data, and binding mismatches.

## Discovery environment

The generator used Python 3.10.12, NumPy 2.2.6, and SciPy 1.15.3 under WSL2.
Floating linear programming was used only to locate supports for 10 rational
exceptions; both generator and independent verifier subsequently checked the
serialized rational weights exactly. The decisive verifier itself uses only
the Python standard library.
