#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 7 ]]; then
    echo "usage: $0 ROLE N TARGET MODULUS WORKERS EXPECT_TOTAL RUN_TAG" >&2
    exit 2
fi

role=$1
n=$2
target=$3
modulus=$4
workers=$5
expect_total=$6
run_tag=$7

case "$role" in
    builder) scanner="code/builder_scan" ;;
    certifier) scanner="code/certifier_scan" ;;
    *) echo "ROLE must be builder or certifier" >&2; exit 2 ;;
esac

if [[ ! -x "$scanner" ]]; then
    echo "missing executable: $scanner" >&2
    exit 2
fi

run_dir="logs/runs/$run_tag"
mkdir -p "$run_dir" certificates

scanner_hash=$(shasum -a 256 "$scanner" | awk '{print $1}')
config="$role n=$n target=$target modulus=$modulus expect_total=$expect_total scanner_sha256=$scanner_hash"
config_file="$run_dir/config.txt"
if [[ -e "$config_file" ]]; then
    if [[ "$(<"$config_file")" != "$config" ]]; then
        echo "existing run configuration mismatch: $config_file" >&2
        exit 2
    fi
else
    printf '%s\n' "$config" > "$config_file"
fi

export n target modulus scanner run_dir role
seq 0 $((modulus - 1)) | xargs -n 1 -P "$workers" bash -c '
    set -o pipefail
    residue=$1
    stem=$(printf "slice_%04d_of_%04d" "$residue" "$modulus")
    log="$run_dir/$stem.log"
    status="$run_dir/$stem.status"
    if [[ -f "$status" && "$(<"$status")" == 0 ]] && grep -Eq "^(BUILDER_OK|CERTIFIER_OK) n=$n target=$target " "$log"; then
        exit 0
    fi
    set +e
    gentourng -q "$n" "$residue/$modulus" | "$scanner" "$n" "$target" > "$log" 2>&1
    result=$?
    set -e
    printf "%s\n" "$result" > "$status"
    exit "$result"
' _

python3 code/aggregate_sweep.py \
    --run-dir "$run_dir" \
    --role "$role" \
    --n "$n" \
    --target "$target" \
    --modulus "$modulus" \
    --expect-total "$expect_total" \
    --scanner "$scanner" \
    --output "certificates/${run_tag}.json"
