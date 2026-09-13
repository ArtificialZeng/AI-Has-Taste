#!/bin/sh
# Isolated rebuild and small exact functional comparison for the order-31 checker.
set -eu

project_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
rebuild_dir=$(mktemp -d /tmp/erdos993-order31-rebuild.XXXXXX)
trap 'rm -rf -- "$rebuild_dir"' EXIT HUP INT TERM

tarball="$project_dir/literature/external/nauty2_9_3.tar.gz"
source_file="$project_dir/experiments/order31_checker.c"
declarations="$project_dir/experiments/order31_plugin_decl.h"
frozen_binary="$project_dir/experiments/gentreeg_order31_checker"
candidate="$rebuild_dir/gentreeg_order31_checker.rebuilt"
candidate_debug="$rebuild_dir/gentreeg_order31_checker_debug.rebuilt"

tar -xzf "$tarball" -C "$rebuild_dir"
nauty_dir="$rebuild_dir/nauty2_9_3"
(cd "$nauty_dir" && ./configure >/dev/null)
make -C "$nauty_dir" gtools.o >/dev/null

build_one()
{
    output=$1
    shift
    cc -O3 -DNDEBUG "$@" -I"$nauty_dir" \
      -include "$declarations" \
      -DOUTPROC=research_check_tree \
      -DSUMMARY=research_check_summary \
      -DPLUGIN_INIT='{ research_check_init(); }' \
      -o "$output" \
      "$nauty_dir/gentreeg.c" "$source_file" "$nauty_dir/gtools.o"
}

build_one "$candidate"
build_one "$candidate_debug" -DPRINT_ALL_SEQUENCES

"$frozen_binary" -q 23 0/24 \
  >"$rebuild_dir/frozen.exceptions" 2>"$rebuild_dir/frozen.summary"
"$candidate" -q 23 0/24 \
  >"$rebuild_dir/rebuilt.exceptions" 2>"$rebuild_dir/rebuilt.summary"
cmp "$rebuild_dir/frozen.exceptions" "$rebuild_dir/rebuilt.exceptions"

frozen_fields=$(sed 's/ cpu=[0-9.]*$//' "$rebuild_dir/frozen.summary")
rebuilt_fields=$(sed 's/ cpu=[0-9.]*$//' "$rebuild_dir/rebuilt.summary")
if [ "$frozen_fields" != "$rebuilt_fields" ]; then
    echo "FAIL: rebuilt and frozen order-23 chunk summaries differ" >&2
    exit 3
fi

python3 "$project_dir/experiments/crosscheck_c_checker.py" \
  "$candidate_debug" --max-n 11
printf 'REBUILD_BINARY_SHA256 '
shasum -a 256 "$candidate" | awk '{print $1}'
printf 'FROZEN_BINARY_SHA256 '
shasum -a 256 "$frozen_binary" | awk '{print $1}'
printf 'ORDER23_CHUNK0_FIELDS %s\n' "$rebuilt_fields"
printf 'REBUILD_AUDIT PASS\n'
