# Fail-closed verifier and tamper audit

Audit date: 2026-08-29 (Asia/Shanghai)

Outcome: **PASS.**

## Trust and schema model

`verification/verify_stagnation.py` uses no host floating point. It requires:

- an explicit SHA-256 trust anchor, defaulting to the audited certificate hash;
- exact top-level, `arithmetic`, `unit_roundoff`, `inputs`, `exact_system`, and
  `expected_trace` key sets;
- exact JSON types, with `bool` rejected where `int` is required;
- global duplicate-key rejection through `object_pairs_hook`;
- rejection of `NaN`, `Infinity`, malformed UTF-8, malformed JSON, unknown
  nested keys, missing keys, and unsupported arithmetic declarations;
- exact comparison with the fixed audited input instance;
- independent recomputation of `B`, both condition numbers, unit roundoff,
  every trajectory value, the midpoint parity decision, `T(0)=0`, and both
  backward errors.

The verified digest from the initially read byte string is retained for success
output, eliminating a second-read TOCTOU ambiguity.

## Root negative suite

Command:

```bash
python3 verification/test_tamper_fail_closed.py
```

Observed results:

| Case | Expected | Result |
|---|---:|---:|
| baseline | 0 | 0 |
| badhash | nonzero | 1 |
| extra | nonzero | 1 |
| drop | nonzero | 1 |
| change-input | nonzero | 1 |
| change-trace | nonzero | 1 |
| change-arithmetic | nonzero | 1 |
| duplicate-key | nonzero | 1 |
| bool-as-int | nonzero | 1 |
| float-as-int | nonzero | 1 |
| nested-extra | nonzero | 1 |
| nan | nonzero | 1 |
| change-exact-system | nonzero | 1 |

Except for `badhash`, every mutant was passed with its own correct SHA-256.
Therefore these failures exercise schema, type, fixed-instance, and exact
mathematical recomputation rather than merely the hash gate.

## Independent breaker attack

An independent adversarial process reproduced baseline success and the six
required nonzero exits against the final verifier. It additionally rejected:

- top-level, nested, and Unicode-escaped duplicate keys;
- `bool`/`int` confusion, floats, numeric strings, `NaN`, `Infinity`, and
  `1e9999`;
- short or uppercase SHA strings;
- coordinated changes of the input, exact system, and trace with the mutant's
  own correct SHA;
- 132 automatically generated drop/extra/type mutations, all 132 nonzero.

Semantic-preserving JSON reordering with an explicitly replaced external trust
anchor remains accepted, as expected: the schema is semantic while the caller
has deliberately chosen a new byte-level trust anchor.

Final audited hashes at this milestone:

- scalar certificate:
  `28c6865ee1d22bf1def7565758fc3ddb254563be31ef69d3e1578a8180366eea`;
- scalar verifier:
  `49c359401a23ca036108667e1ea22802c6266641498330b9daa88c7102467385`;
- 2-by-2 certificate:
  `662374272407d01b56fd18c86153d7fdfc69508a1cbbab0a51026524948c6e9a`;
- 2-by-2 verifier:
  `0969a71fb3e8f6579557b565f648ddf94f03d818cf7545c25cd22d6b1d9be2dd`.
