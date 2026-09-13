#!/bin/sh
set -eu

target=verification/third_party/drat-trim
(cd "$target" && shasum -a 256 -c ../drat-trim.SHA256)
cc "$target/lrat-check.c" -std=c99 -DLONGTYPE -O2 \
  -o "$target/lrat-check"
"$target/lrat-check" 2>&1 | sed -n '1p'
printf '%s\n' "BUILT_PINNED_LRAT_CHECK"
