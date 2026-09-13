# Fail-closed rejection audit

Date: 2026-08-29 (Asia/Shanghai)

Status: **PASS, 4/4 corruptions rejected with nonzero exit**.

The root-level driver `audit/fail_closed_rejection_tests.py` creates a fresh
temporary certificate tree for each case, copies the independent verifier and
every artifact bound by the preflight, applies exactly one corruption, and
runs the verifier as a subprocess.  A case passes only when the subprocess
has a nonzero exit status and its rejection message contains the expected
reason.

Command:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 audit/fail_closed_rejection_tests.py \
  --output results/fail_closed_rejection_tests.json
```

| Corruption | Exit | Required rejection | Result |
|---|---:|---|:---:|
| remove `order31_chunk119_of_120.summary.done` | 1 | `missing paired completed files for residue 119` | PASS |
| increment residue-000 `trees` while leaving `generated` unchanged | 1 | `checker/generator count mismatch at residue 0` | PASS |
| increment the final coefficient of the first serialized exceptional sequence | 1 | `rebuilt coefficients disagree` | PASS |
| change one hexadecimal digit of a preflight artifact SHA-256 | 1 | `artifact hash drift` | PASS |

The serialized result is
`results/fail_closed_rejection_tests.json`, SHA-256
`f6d02ebac35e8cff0f150a21750c9330c4c9cb0480a1e66f48783caea9fd116b`.
The driver SHA-256 is
`1e9132151f6031c4e88675d1573d29cc829253fc125f8f30fc86d1bc572fefe7`.

These are negative controls for the independent verifier.  They do not alter
the frozen production `.done` files or the positive order-31 aggregate.
