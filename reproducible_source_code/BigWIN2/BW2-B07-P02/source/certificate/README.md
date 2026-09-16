# Exact and rigorous certificates

All programs use only the Python 3 standard library.

## Fast core verification

```bash
bash code/run_certificates.sh --fast
```

This performs:

- the independent outward-rounded fixed-point prefix check through 5000 at
  two precisions;
- exact rational verification of every finite constant in the analytic tail;
- exact low-degree reconstruction of the factorization from both sides.

## Full verification

```bash
bash code/run_certificates.sh --full
```

This additionally runs the exact \(5000!\)-denominator product expansion.
On the recorded WSL2/Python 3.10.12 environment that extra run took about
101 seconds.

The fixed-point checker represents each endpoint as an integer multiple of
\(10^{-p}\).  Division by a cycle length is rounded down for lower endpoints
and up for upper endpoints.  Descending coefficient updates ensure that both
endpoints enclose the same partial product coefficient.  A comparison is
accepted only when the upper interval for \(q_m\) is strictly below the lower
interval for \(q_{m-1}\).

No proof assistant was used.
