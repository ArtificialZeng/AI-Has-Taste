#!/bin/sh
set -eu

PROJECT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$PROJECT_DIR"

mkdir -p certificates results
python3 --version
/opt/homebrew/bin/Singular -v | sed -n '1p'

for n in 3 4 5; do
  python3 src/candidate_basis.py "$n" --json "certificates/n${n}_input.json"
  python3 certificates/verify_certificate.py "certificates/n${n}_input.json"
done

python3 -m unittest -v tests/test_verifier.py
sha256sum \
  certificates/n3_input.json \
  certificates/n4_input.json \
  certificates/n5_input.json \
  certificates/verify_certificate.py \
  src/candidate_basis.py \
  src/polarized_power_sum_test.sing
