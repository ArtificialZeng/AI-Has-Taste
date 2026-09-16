#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.." && pwd)
cd "$root"
export LD_LIBRARY_PATH="$root/experiments/breaker_nauty/usr/lib:$root/experiments/breaker_nauty/usr/lib/x86_64-linux-gnu"
geng="$root/experiments/breaker_nauty/usr/bin/nauty-geng"
"$geng" -q 8 > experiments/breaker_graphs8.g6
wc -l experiments/breaker_graphs8.g6
for r in 0 1 2 3 4 5 6 7; do
  python3 experiments/breaker_certify_alpha3.py --input experiments/breaker_graphs8.g6 --output "certificates/breaker_n8_shard_${r}.jsonl" --residue "$r" --modulus 8 > "experiments/breaker_n8_shard_${r}.log" 2>&1 &
done
wait
python3 experiments/breaker_merge_shards.py --graphs experiments/breaker_graphs8.g6 --output certificates/breaker_n8_alpha3_kernels.jsonl certificates/breaker_n8_shard_*.jsonl | tee experiments/breaker_merge.log
python3 experiments/breaker_verify_certificates.py certificates/breaker_n8_alpha3_kernels.jsonl | tee experiments/breaker_verify.log
sha256sum experiments/breaker_graphs8.g6 certificates/breaker_n8_alpha3_kernels.jsonl experiments/breaker_*.py > certificates/breaker_n8_sha256.txt
