#!/usr/bin/env bash
set -euo pipefail
python3 code/test_small_cases.py
python3 code/verify_counterexample.py
python3 code/verify_branch_formula.py
python3 code/verify_sturm.py
