# Exact certificate

`annihilator_certificate.json` stores only exact integer polynomial data.  The
independent verifier `verify_certificate.py` uses Python's standard library and
does not import the SymPy discovery script.  It reconstructs:

1. the rational state system for (X=(E,E/s,G)^T) from (s^2=1-2t),
   (E=\exp(-1-t+s)), and (G=(2-t)e^{-t});
2. the scalar third-order annihilator;
3. the noncommutative product of the rational second-order multiplier and that
   annihilator;
4. the fifth-order polynomial ODE and its EGF coefficient recurrence;
5. the exact Taylor coefficients through (a_8).

Run:

```bash
python3 certificates/verify_certificate.py certificates/annihilator_certificate.json
python3 tests/test_certificate.py
```

The second command also requires four malformed or mathematically corrupted
certificates to be rejected.
