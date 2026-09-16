#!/usr/bin/env bash
set -euo pipefail

python3 -m py_compile \
  code/lg_exact.py \
  code/lg_v1_sympy.py \
  certificate/double_twist_certificate.py \
  certificate/verify_double_twist_sympy.py

python3 code/lg_exact.py --self-test
python3 code/lg_v1_sympy.py --self-test

for parameters in "1 1" "2 3" "5 7"; do
  python3 certificate/double_twist_certificate.py ${parameters} >/dev/null
  python3 certificate/verify_double_twist_sympy.py \
    ${parameters} --max-identity-n 20
done

echo ALL_EXACT_CHECKS_OK
