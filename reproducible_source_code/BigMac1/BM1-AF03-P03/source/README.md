# Lentfer Conjecture 3.2 at (n=5)

Terminal state: **CERTIFIED_FINITE_RESULT**.

Over every characteristic-zero field, the 1920 residue classes in
(B_5^{(1,2)}) form a basis of (R_5^{(1,2)}).  The result is supported by a
uniform proof that the Hilbert ideal has (4n) polarized-power-sum generators,
an exact supercommutative standard-basis/rank certificate over (mathbb Q),
and two independent exact Artin--exterior all-block reconstructions.

The result proves only the finite (n=5) endpoint.  It does not prove the
conjecture for arbitrary (n), and it does not claim that the candidate is
the standard-monomial set for the implementation's degree-product order.

## Fast reproduction

```sh
sh experiments/run_exact.sh
python3 tests/builder_test_coinvariant.py
python3 independent/tests/test_fail_closed.py
```

The complete frozen no-import (n=5) reconstruction is intentionally slower:

```sh
python independent/verify_exact.py independent/certificate/certificate.json \
  --case 5 --output independent/certificate/exact_n5.json
```

The recorded run checked 396/396 tridegrees in 7637.68 seconds.  See
`FINAL_STATUS.md`, `audit/PROOF_AUDIT.md`, and
`independent/README.md` for hashes, trust boundaries, limitations, and the
full audit trail.

## Release artifacts

- Paper PDF: `output/pdf/lentfer_n5_basis_case.pdf`
- Source/certificate archive:
  `output/source/lentfer_n5_certified_finite_result.zip`
- Hash manifest:
  `output/release/lentfer_n5_certified_finite_result/MANIFEST.json`

No Lean, Coq, Isabelle, or other proof assistant was used.
