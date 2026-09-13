#!/bin/sh
set -eu
c++ -std=c++20 -O3 -Wall -Wextra -Wpedantic src/discovery.cpp -o experiments/discovery
result=$(experiments/discovery --n 7 --count-only)
case "$result" in
  "n=7 all_tableaux=343210 initial_tableaux=238405 enumeration_seconds="*) ;;
  *) echo "unexpected n=7 discovery baseline: $result" >&2; exit 1 ;;
esac
printf '%s\n' "$result"
