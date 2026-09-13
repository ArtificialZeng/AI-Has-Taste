#!/bin/sh
set -eu

project_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
bash "$project_dir/tests/run_fc_lift_certificate.sh"
bash "$project_dir/tests/run_weighting_no_go.sh"
