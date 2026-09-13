#!/bin/sh
set -eu

project_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
python3 "$project_dir/src/verify_power_chain_no_go.py"
