# Independent exact breaker/certifier route

## Result

The characteristic-zero verifier certifies that Lentfer's candidate set
`B_n^(1,2)` is a basis for `R_n^(1,2)` for `n=3,4,5`.  In particular, at the
first previously unverified case `n=5`, all 396 trigraded blocks pass and

```text
ambient dimension after Artin reduction = 122880
positive-invariant ideal dimension      = 120960
quotient dimension                      =   1920
candidate count                         =   1920
```

No exact dependency, missing quotient class, or graded-dimension discrepancy
was found.  This is a finite `n=5` result, not a proof for general `n`.

## Trust boundary and method

`verify_exact.py` is standalone: it does not import `core.py`,
`discover_modular.py`, root discovery code, or discovery output.  Starting
from the serialized `certificate/certificate.json`, it reconstructs:

1. the Artin quotient by the elementary symmetric polynomials using the
   Groebner basis `h_i(x_i,...,x_n)`;
2. the two mutually anticommuting exterior alphabets and their signs;
3. the diagonal `S_n` action and every Reynolds invariant;
4. the positive-invariant ideal, block by block, by multiplication with all
   `x_i`, `theta_i`, and `xi_i`; and
5. the Definition 3.1 candidate monomials.

Sparse modular elimination is used only to select literal integer ideal
columns.  Every decisive rank is then recomputed by Singular over `Q`.  In a
block containing candidates, the verifier checks

```text
rank_Q(all ideal-generator columns) = N - number_of_candidates
rank_Q(selected ideal columns | candidate columns) = N.
```

When a block has no candidates, `N` selected columns are themselves literal
integer elements of the ideal, and Singular verifies that their `Q`-rank is
`N`.  No finite-field rank is accepted as the endpoint.

The paper source is pinned by SHA-256.  The parser rejects unknown keys,
unknown schemas, invalid case counts, invalid primes, malformed hashes, and
out-of-range cases.  The main verifier also fails closed on a missing or
hash-mismatched source PDF and on unparseable/failed Singular output.

## Reproduction

From the project root:

```bash
python independent/tests/test_fail_closed.py
python independent/verify_exact.py independent/certificate/certificate.json \
  --case 3 --output independent/certificate/exact_n3.json
python independent/verify_exact.py independent/certificate/certificate.json \
  --case 4 --output independent/certificate/exact_n4.json
python independent/verify_exact.py independent/certificate/certificate.json \
  --case 5 --output independent/certificate/exact_n5.json
```

The recorded final `n=5` run used Python 3.13.5 and Singular 4.4.1 over `Q`,
checked 396 blocks, and took 7637.68 seconds.  See `proof/breaker_notes.md` for
the mathematical reduction, hashes, test results, limitations, and the reason
earlier exploratory runs were restarted.

## Artifact roles

- `source/Lentfer_2025_ALCO424.pdf`: pinned published source.
- `certificate/certificate.json`: small serialized input and expected finite
  cases.
- `verify_exact.py`: standalone exact verifier.
- `certificate/exact_n{3,4,5}.json`: exact per-block rank records.
- `logs/exact_n{3,4,5}.log`: complete console logs.
- `tests/test_fail_closed.py`, `logs/fail_closed.log`: negative tests.
- `discover_modular.py` and `logs/screen_*`: scouting only; never endpoint
  evidence.  The `n=5` scouting log is intentionally incomplete because that
  run was stopped after the exact verifier superseded it.

No Lean, Coq, Isabelle, or other proof assistant was used.
