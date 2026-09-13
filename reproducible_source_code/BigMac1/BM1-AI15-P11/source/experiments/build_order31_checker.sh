#!/bin/sh
set -eu

project_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
nauty_dir="$project_dir/literature/external/nauty-src"
output="$project_dir/experiments/gentreeg_order31_checker"

if [ ! -f "$nauty_dir/makefile" ]; then
    (cd "$nauty_dir" && ./configure)
fi
make -C "$nauty_dir" gtools.o

cc -O3 -DNDEBUG -I"$nauty_dir" \
  -include "$project_dir/experiments/order31_plugin_decl.h" \
  -DOUTPROC=research_check_tree \
  -DSUMMARY=research_check_summary \
  -DPLUGIN_INIT='{ research_check_init(); }' \
  -o "$output" \
  "$nauty_dir/gentreeg.c" \
  "$project_dir/experiments/order31_checker.c" \
  "$nauty_dir/gtools.o"

shasum -a 256 "$output" "$project_dir/experiments/order31_checker.c"
