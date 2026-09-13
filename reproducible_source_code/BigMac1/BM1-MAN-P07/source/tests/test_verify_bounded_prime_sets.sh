#!/bin/sh
set -eu

cxx=${CXX:-c++}
root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
bin="$root/results/verify_bounded_prime_sets"

"$cxx" -std=c++17 -O3 -Wall -Wextra -Wpedantic \
  -Wno-deprecated-literal-operator \
  -I/opt/homebrew/include "$root/src/verify_bounded_prime_sets.cpp" \
  -L/opt/homebrew/lib -lgmpxx -lgmp -o "$bin"

output=$($bin 3)
printf '%s\n' "$output" | grep -q '^odd_primes=1$'
printf '%s\n' "$output" | grep -q '^solutions=0$'

output=$($bin 11)
printf '%s\n' "$output" | grep -q '^odd_primes=4$'
printf '%s\n' "$output" | grep -q '^solutions=0$'

if "$bin" 1 >/dev/null 2>&1; then
  echo "invalid bound was accepted" >&2
  exit 1
fi

echo "test_verify_bounded_prime_sets: PASS"
