# Reproducing the normalized 17-point certificate

This certificate re-establishes the known geometric bound `ES(6) <= 17`.
It is not a certificate for `ES(7)` and it is not presented as a new theorem.

## 1. Generate the direct base formula

From the project root:

```sh
python3 code/direct_six_sat.py \
  --n 17 --fix-extreme --prime-signotope \
  --out tmp/sat/es_17_6_direct_relations_prime_extreme.cnf
```

The base has 680 variables, 217,176 clauses, and 849,304 literal
occurrences.  The 120 extreme-point units are sound without loss of generality
for realizable planar configurations; they are not asserted to preserve all
abstract signotopes.

## 2. Generate the exhaustive first-window partition

```sh
python3 code/generate_es17_first_window_cubes.py \
  tmp/sat/es_17_6_direct_relations_prime_extreme.cnf \
  --out-dir tmp/cubes/es17_first_window_prime_extreme
```

The generator enumerates all 1,024 assignments to the ten non-extreme triple
orientations on the first six labels.  Exactly 963 falsify a local base clause;
the remaining 61 cubes are pairwise disjoint and cover every base model.

## 3. Re-run the solver leaves

```sh
python3 code/run_cube_batch.py \
  --solver literature/external/kissat/build/kissat \
  --cube-dir tmp/cubes/es17_first_window_prime_extreme \
  --log-dir tmp/certification/es17_61cubes_120s/logs \
  --proof-dir tmp/certification/es17_61cubes_120s/proofs \
  --seconds 120 --jobs 10 \
  --summary tmp/certification/es17_61cubes_120s/summary.json
```

All 61 retained leaves must return UNSAT.

## 4. Convert to LRAT and check both proof families

```sh
python3 code/convert_and_check_es17_lrat.py --jobs 8
python3 code/verify_es17_cube_certificate.py
```

The first command converts every DRAT leaf to LRAT and invokes the LRAT
checker.  The second independently rebuilds the 1,024-case coverage, compares
every leaf against the exact base-plus-ten-units construction, reruns
DRAT-trim on all DRAT files, and reruns the LRAT checker on all converted
proofs.

The retained proof totals are 288,562,058 bytes of binary DRAT and
871,234,978 bytes of LRAT.  Human-readable paths and byte counts, rather than
content hashes, identify the release artifacts.
