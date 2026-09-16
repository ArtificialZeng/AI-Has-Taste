# Exact coefficient audit through q^3025

Two separate exact generators compute all coefficients modulo 16 from degree
0 through 3025.

1. `constant_term_mod16.py` uses the colored Frobenius Laurent product
   directly.  The z-range truncation is exhaustive: a term contributing to a
   constant term has the same final number r of top and bottom selections.  At
   degree at most 3025, the minimum degree is 3017 for r=233 and 3042 for
   r=234.  Therefore every contributing partial monomial has |z-degree| <=233.
   Factors of q-weight greater than 3025 cannot contribute in the requested
   degree range.  Arithmetic wraps modulo 256 in uint8 and then reduces modulo
   16; this is exact because reduction from Z/256Z to Z/16Z is a ring map.

2. `source_formula_mod16.py` independently implements formula (3.15) from the
   official v1 paper.  It expands every f_d by Euler's pentagonal theorem,
   every reciprocal f_d by the partition recurrence, and the Borwein cubic
   theta function by direct enumeration of m^2+mn+n^2.  Polynomial products
   use int64 convolution; before reduction every convolution entry is below
   `(3026)*15^2`, so there is no overflow.

The complete 3026-byte residue vectors are identical and have SHA-256
`25284b4daebdf702db14e284ae6d4d633597f412cec399c409b5cbd70d64745b`.
The target CSV files are likewise byte-identical, with SHA-256
`349401db1679bb608f4ca2be0c979b68744b2852db12eeb27cc32a9bdfc37384`.
All 202 values in the two progressions, for 0 <= n <= 100, are 0 modulo 16.

Replay from the project root:

```sh
python3 evidence/computation/constant_term_mod16.py
python3 evidence/computation/source_formula_mod16.py
cmp evidence/computation/constant_term_coefficients_mod16.bin \
    evidence/computation/source_formula_coefficients_mod16.bin
```

This exhaustive finite statement does not prove either all-n congruence.

## Stronger 6-section test from research pass 2

`h_identity_mod16.py` tests the explicitly conjectural identity

```text
sum_m cphi_18(6m+1) q^m == 4*f_2*f_3^2/(f_1*f_6) (mod 16).
```

It compares both independent coefficient vectors with an eta-product
recurrence and generalized-pentagonal enumeration. The discovery range is
`0 <= m <= 99`; the held-out range is `100 <= m <= 504`.
`projection_term_audit.py` expands the fourteen formula-(3.15) summands and
records the smaller grouped 6-section kernel. Mathematical scope and limits
are in `../h_identity_dossier.md`.

```sh
python3 evidence/computation/h_identity_mod16.py
python3 evidence/computation/projection_term_audit.py
```
