#!/bin/sh
set -eu

commit=2e3b2dc0ecf938addbd779d42877b6ed69d9a985
target=verification/third_party/drat-trim
mkdir -p "$target"

for file in LICENSE Makefile README.md lrat-check.c; do
  curl -fsSL --connect-timeout 30 \
    "https://raw.githubusercontent.com/marijnheule/drat-trim/$commit/$file" \
    -o "$target/$file"
done

(cd "$target" && shasum -a 256 -c ../drat-trim.SHA256)
printf '%s\n' "FETCHED_PINNED_DRAT_TRIM $commit"
