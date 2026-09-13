# Exact computation record

Date: 2026-09-04  
Platform: Darwin 25.5.0 arm64  
Interpreter: Python 3.14.7, Clang 21.0.0

Witness input SHA-256:
`b2172bf0cd04116f17d9317af42cb420ba7428fbe02554c1ce1050ef8fe965f6`.

## LCM-sum verifier

Command:

```text
python3 verification/verify_lcm_sum.py evidence/witness-31862.json
```

Result:

```json
{"algorithm":"lcm-sum-then-reduce","code_sha256":"fae116dc83e4587ef84654ae9fc0318c51c22f3e8963324d387d31a245690c30","computed_h":179,"denominator_bits":45866,"denominator_mod_179":165,"denominator_sha256_decimal":"3be745715b54a298fd4a9e9cd127fedebbd4714a538b9ec7ec6da984b089b361","input_sha256":"b2172bf0cd04116f17d9317af42cb420ba7428fbe02554c1ce1050ef8fe965f6","n":31862,"numerator_bits":45869,"numerator_mod_179_squared":15036,"numerator_sha256_decimal":"b284af4f4b5da4ff75e3762fec00118e630b846c53d23858089c84a69b51b523","status":"PASS"}
```

## Reduced-recurrence verifier

Command:

```text
python3 verification/verify_recurrence.py evidence/witness-31862.json
```

Result:

```json
{"algorithm":"stepwise-reduced-recurrence","code_sha256":"a04ec2a5a3a60baaac35cd1846964da04c2d49b9e6fc2745a3dea5ef55c9cc3a","computed_h":179,"denominator_bits":45866,"denominator_mod_179":165,"denominator_sha256_decimal":"3be745715b54a298fd4a9e9cd127fedebbd4714a538b9ec7ec6da984b089b361","input_sha256":"b2172bf0cd04116f17d9317af42cb420ba7428fbe02554c1ce1050ef8fe965f6","n":31862,"numerator_bits":45869,"numerator_mod_179_squared":15036,"numerator_sha256_decimal":"b284af4f4b5da4ff75e3762fec00118e630b846c53d23858089c84a69b51b523","status":"PASS"}
```

Both programs recompute the rational harmonic number rather than trusting any
stored numerator or denominator.  They fail closed on malformed or
wrong-endpoint witness fields.  The second method is slower because it performs
31862 exact reductions, but it shares neither the LCM construction nor the
single final reduction used by the first.

## Block 2 verifier repair and exact rerun

After independent audit 01 rejected the submitted certificate package, both
candidate verifiers were repaired to reject duplicate JSON member names before
dictionary construction and to require the exact frozen claim text.  The full
attack suite was expanded to include a duplicate `claim` key and a trailing
space in an otherwise correct claim.

Command:

```text
python3 audit/test_fail_closed.py
```

At 2026-09-04T06:51:50Z, all three baselines passed and every one of the 15
malformed or wrong-endpoint inputs was rejected by every verifier.  The two
repaired candidate verifiers and the prior independent no-import verifier again
returned the common exact result

```text
n = 31862
computed_h = 179
numerator_bits = 45869
denominator_bits = 45866
numerator_mod_179_squared = 15036
denominator_mod_179 = 165
numerator_sha256_decimal = b284af4f4b5da4ff75e3762fec00118e630b846c53d23858089c84a69b51b523
denominator_sha256_decimal = 3be745715b54a298fd4a9e9cd127fedebbd4714a538b9ec7ec6da984b089b361
```

The repaired code hashes are

```text
verify_lcm_sum.py       ad45ae40ad5a641bff7bb67a321d9cb345a734e35ea086904cc046f03f5f1369
verify_recurrence.py    de8baaf2590022323642a5e55e2561aa7782bb150696308dd2a52f6ab021f4a3
test_fail_closed.py     cc912577c030290202e97c6b4ffc6f2952abba8fcd7319d56541c23c981b0cf5
```

The machine-readable regression record is
`evidence/fail-closed-repair-02.json`.  This owner-context rerun repairs the
submitted package but does not replace the required second fresh independent
audit.
