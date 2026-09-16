#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 3 ]]; then
  echo "usage: $0 VERIFY_BINARY DATASET CERTIFICATE" >&2
  exit 2
fi

verifier=$1
dataset=$2
certificate=$3

read -r _ first_graph first_witness _ < <(sed -n '2p' "$certificate")
read -r _ second_graph _ _ < <(sed -n '3p' "$certificate")
swap_witness=$((first_graph ^ first_witness))

expect_fail() {
  local label=$1
  shift
  local output
  if output=$("$@" 2>&1); then
    echo "ADVERSARIAL_FAIL accepted=$label" >&2
    exit 1
  fi
  if [[ "$output" != *"VERIFY_FAIL"* ]]; then
    echo "ADVERSARIAL_FAIL non_fail_closed_error=$label" >&2
    echo "$output" >&2
    exit 1
  fi
  echo "REJECTED $label: ${output##*$'\n'}"
}

expect_fail zero_witness "$verifier" "$dataset" \
  <(awk 'NR==2 {$3="0"} {print}' "$certificate")

expect_fail outside_graph_witness "$verifier" "$dataset" \
  <(awk 'NR==2 {$3="1"} {print}' "$certificate")

expect_fail colour_swap_equivalent_witnesses "$verifier" "$dataset" \
  <(awk -v w="$swap_witness" 'NR==2 {$4=w} {print}' "$certificate")

expect_fail graph_mismatch "$verifier" "$dataset" \
  <(awk 'NR==2 {$2=$2+1} {print}' "$certificate")

expect_fail duplicated_graph "$verifier" \
  <(sed "0,/$second_graph/s//$first_graph/" "$dataset") \
  <(awk -v g="$first_graph" 'NR==3 {$2=g} {print}' "$certificate")

expect_fail unknown_tag "$verifier" "$dataset" \
  <(awk 'NR==2 {$1="X"} {print}' "$certificate")

expect_fail wrong_header "$verifier" "$dataset" \
  <(awk 'NR==1 {$2="99"} {print}' "$certificate")

expect_fail truncated_certificate "$verifier" "$dataset" \
  <(head -n 100 "$certificate")

echo "ADVERSARIAL_TESTS_PASSED cases=8"
