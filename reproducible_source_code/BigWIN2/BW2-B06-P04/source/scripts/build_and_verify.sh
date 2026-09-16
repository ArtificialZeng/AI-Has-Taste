#!/usr/bin/env bash
set -euo pipefail

project_dir=$(cd "$(dirname "$0")/.." && pwd)
cd "$project_dir"

compiler=${CC:-cc}
mkdir -p build

"$compiler" -std=c11 -O3 -march=native -Wall -Wextra -Werror \
  -o build/discover_n11 src/discover_n11.c
"$compiler" -std=c11 -O3 -march=native -Wall -Wextra -Werror \
  -o build/verify_n11 src/verify_n11.c

dataset=${LAMAN11_DATASET:-experiments/upstream/LamanGraphs11.txt}
certificate=${NAC11_CERTIFICATE:-certificates/nac11_four_way.cert}

build/verify_n11 "$dataset" "$certificate"
tests/adversarial_verifier.sh build/verify_n11 "$dataset" "$certificate"

if [[ ${RUN_DISCOVERY:-0} == 1 ]]; then
  build/discover_n11 "$dataset" build/recomputed.cert
  cmp "$certificate" build/recomputed.cert
  echo "DISCOVERY_REPRODUCED byte_identical=1"
fi
