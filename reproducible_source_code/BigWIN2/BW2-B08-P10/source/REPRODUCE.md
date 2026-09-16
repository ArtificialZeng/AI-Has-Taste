# Reproducing the exact order-nine census

Run from the project root on the recorded Linux/WSL environment.

```bash
NAUTY_LIBS="$PWD/tools/nauty-bin/usr/lib:$PWD/tools/nauty-bin/usr/lib/x86_64-linux-gnu"
env LD_LIBRARY_PATH="$NAUTY_LIBS" \
  tools/nauty-bin/usr/bin/nauty-geng -c 9 \
  > experiments/data/connected_n9_all.g6 \
  2> experiments/logs/geng_n9_all.log

python3 experiments/exact_census.py \
  --input experiments/data/connected_n9_all.g6 \
  --expected-n 9 --output results/census_n9_all.json

python3 certificates/verify_census_flint.py \
  --input experiments/data/connected_n9_all.g6 \
  --census results/census_n9_all.json \
  --log certificates/verify_n9_flint.json
```

Expected generator count: 261080. Expected census totals: 261074 strict,
6 equality, 0 violations. The first computation uses exact rational
congruence; the independent verifier uses FLINT integer characteristic
polynomials, square-free factorization, and rational Sturm sequences.

The separate breaker implementation and direct equality verifier are under
`experiments/breaker/`. No random seeds or floating-point sign decisions are
used.
