#!/bin/sh
set -eu

if [ "$#" -ne 5 ]; then
    echo "usage: $0 ORDER MODULUS WORKER WORKERS OUTPUT_DIR" >&2
    exit 2
fi

order=$1
modulus=$2
worker=$3
workers=$4
output_dir=$5
project_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
checker="$project_dir/experiments/gentreeg_order31_checker"

case "$order:$modulus:$worker:$workers" in
    *[!0-9:]*|:*|*:) echo "numeric arguments must be nonnegative integers" >&2; exit 2 ;;
esac
if [ "$modulus" -le 0 ] || [ "$workers" -le 0 ] || [ "$worker" -ge "$workers" ]; then
    echo "invalid modulus/worker assignment" >&2
    exit 2
fi
if [ ! -x "$checker" ]; then
    echo "checker binary missing; run experiments/build_order31_checker.sh" >&2
    exit 2
fi

mkdir -p "$output_dir"
residue=$worker
while [ "$residue" -lt "$modulus" ]; do
    stem=$(printf 'order%02d_chunk%03d_of_%03d' "$order" "$residue" "$modulus")
    exceptions_done="$output_dir/$stem.exceptions.done"
    summary_done="$output_dir/$stem.summary.done"
    if [ -f "$exceptions_done" ] && [ -f "$summary_done" ]; then
        echo "SKIP $stem"
        residue=$((residue + workers))
        continue
    fi

    exceptions_tmp="$output_dir/$stem.exceptions.tmp.$$"
    summary_tmp="$output_dir/$stem.summary.tmp.$$"
    trap 'rm -f "$exceptions_tmp" "$summary_tmp"' EXIT HUP INT TERM
    echo "START $stem"
    "$checker" -q "$order" "$residue/$modulus" \
        >"$exceptions_tmp" 2>"$summary_tmp"
    if ! grep -q '^RESEARCH_CHECK ' "$summary_tmp"; then
        echo "missing checker summary for $stem" >&2
        exit 3
    fi
    mv "$exceptions_tmp" "$exceptions_done"
    mv "$summary_tmp" "$summary_done"
    trap - EXIT HUP INT TERM
    echo "DONE $stem"
    residue=$((residue + workers))
done
