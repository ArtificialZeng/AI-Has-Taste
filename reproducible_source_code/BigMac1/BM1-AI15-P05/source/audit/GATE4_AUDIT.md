# Gate 4 optimization and isolation audit

Audit completed: 2026-08-29 03:41 UTC.

## Defect and repair

The prior `verification/test_verifier.py` used optimization-sensitive Python
`assert` statements and imported `verify_extension` through the ambient module
search path.  Consequently `python3 -O` could erase test predicates and
`python3 -O -I test_verifier.py` could fail before the tests ran.

The repaired harness now:

- loads `verify_extension.py` from its absolute `__file__`-derived path with
  `importlib.util.spec_from_file_location`;
- uses explicit `require(...)` exceptions for every positive and negative
  predicate;
- parses both Python files with `ast` and fails if either contains an
  `Assert` node;
- validates required input/output fields explicitly;
- validates every serialized hard factor, product, divisor count, killing
  inequality, canonical ordering, and bound-artifact hash;
- rejects a hard record unless `(r,s,u)` reconstructs its claimed `n`.

Final AST result: `0` `Assert` nodes in each of `test_verifier.py` and
`verify_extension.py`.

## Fast adversarial matrix

The suite was run normally and with optimization/isolation.  The two isolated
runs were launched from `/tmp`, not from the project or `verification/`
directory.

```text
python3 verification/test_verifier.py
python3 -O verification/test_verifier.py
(cd /tmp && python3 -I /ABS/verification/test_verifier.py)
(cd /tmp && python3 -O -I /ABS/verification/test_verifier.py)
```

All four logs are byte-identical, SHA-256
`81a9874cabe68f939aaae4d9521b70937afa08d4e0c1b781f756bfa35b2dc19d`:

- `verification/logs/test_normal.out`
- `verification/logs/test_optimize.out`
- `verification/logs/test_isolated.out`
- `verification/logs/test_optimize_isolated.out`

Each mode accepted the authentic pair table and 21 exact hard records, and
explicitly rejected all of the following mutations:

1. inconsistent HARD `(r,s,u,n)` coordinates;
2. corrupted pair-table hash;
3. duplicated pair with a recomputed hash;
4. changed right endpoint;
5. signed-64 endpoint overflow;
6. deleted `sieve_definition` field;
7. changed exponent in a serialized hard factorization.

## Decisive full-replay matrix

The full 50,784-progression replay was then run in the same four interpreter
modes; the isolated modes again ran from `/tmp`.

```text
python3 verification/verify_extension.py --threads 12
python3 -O verification/verify_extension.py --threads 12
(cd /tmp && python3 -I /ABS/verification/verify_extension.py --threads 12)
(cd /tmp && python3 -O -I /ABS/verification/verify_extension.py --threads 12)
```

All four decisive stdout files are byte-identical, SHA-256
`19f8f31a1d037ddae404448ba13863f10607a23f24414b57628bf13b6ecc83c3`.
All four stderr files are byte-identical, SHA-256
`1a7e52d4c37623cdeddf7cb194195a929e65c138f9bc9876c54c779ec52ab300`.
Every mode reports:

```text
status = PASS
cells = 5,078,450,784
cheap exact lower-bound kills = 5,078,450,763
independently factored hard cells = 21
unresolved cells = 0
```

The canonical decisive output was copied byte-for-byte to
`certificates/finite_extension_certificate.json`.

## Frozen hashes after repair

| Artifact | SHA-256 |
|---|---|
| `verification/test_verifier.py` | `c32a72da127f7bc52bc3258b07b42b3ad000e59ea831687ce59fe961f5406cb2` |
| `verification/verify_extension.py` | `b75c881a95a8e0bf304f0117a3ae9c4804a0d330c456ea3440bb0ab4e4c7b43c` |
| `verification/replay_open_subaps.c` | `340e44cb5ed1e60339280740d9390acf497f4facd77177c582be4e7d2a44930a` |
| `certificates/finite_extension_input.json` | `f989257da9c9fe568be4eaea8df59d20891e94572ec62e78b483767acc36e2ce` |
| `certificates/sieve96_subaps.tsv` | `05693f57f61cfbc61af1a983a6080e9768c60f1bebc250aa87bde686d14abb59` |
| `certificates/finite_extension_certificate.json` | `19f8f31a1d037ddae404448ba13863f10607a23f24414b57628bf13b6ecc83c3` |

## Gate decision

PASS.  The specific optimization and isolated-import defect is closed.  Gate 5
and release packaging remain paused; the existing manuscript still contains a
pre-repair certificate digest and must not be treated as a release artifact.
