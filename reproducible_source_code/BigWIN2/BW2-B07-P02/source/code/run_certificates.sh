#!/usr/bin/env bash
set -euo pipefail

mode="${1:---fast}"
if [[ "$mode" != "--fast" && "$mode" != "--full" ]]; then
  echo "usage: $0 [--fast|--full]" >&2
  exit 2
fi

python3 code/verify_structural_identities.py --limit 80
python3 code/verify_tail_constants.py
python3 code/verify_prefix_interval.py --limit 5000 --decimal-digits 30
python3 code/verify_prefix_interval.py --limit 5000 --decimal-digits 40

if [[ "$mode" == "--full" ]]; then
  python3 code/exact_prefix_factorial.py --limit 5000
fi
