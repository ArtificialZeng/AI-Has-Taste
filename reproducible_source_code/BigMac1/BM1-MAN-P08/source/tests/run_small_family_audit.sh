#!/bin/sh
set -eu

project_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
python3 "$project_dir/src/enumerate_small_union_closed.py" \
  "$project_dir/results/small_family_weighting_audit.json"
python3 "$project_dir/src/verify_small_union_closed.py" \
  "$project_dir/results/small_family_weighting_audit.json" --full-recount
