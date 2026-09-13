#!/bin/bash
set -u

if [ "$#" -ne 4 ]; then
    echo "usage: $0 ORDER MODULUS WORKERS OUTPUT_DIR" >&2
    exit 2
fi

order=$1
modulus=$2
workers=$3
output_dir=$4
project_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
mkdir -p "$output_dir"

pids=()
for ((worker=0; worker<workers; worker++)); do
    sh "$project_dir/experiments/run_tree_sweep_worker.sh" \
        "$order" "$modulus" "$worker" "$workers" "$output_dir" \
        >"$output_dir/worker_${worker}.log" 2>&1 &
    pids+=("$!")
done

status=0
for pid in "${pids[@]}"; do
    if ! wait "$pid"; then
        status=1
    fi
done
exit "$status"
