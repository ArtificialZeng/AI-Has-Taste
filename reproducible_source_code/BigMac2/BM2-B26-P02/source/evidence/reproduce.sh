#!/bin/zsh
set -euo pipefail

PROJECT_DIR=/Users/mac/4prove-or-disprove-math/projects/bigMac-00026-p02
RESEARCH_PYTHON=/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
GENG=/opt/homebrew/bin/geng
LABELG=/opt/homebrew/bin/labelg
CXX=/usr/bin/clang++
AUDIT_DIR=$(mktemp -d /private/tmp/bigMac-00026-p02-reproduce.XXXXXX)

cd "$PROJECT_DIR"

"$GENG" -cq 8 8:28 "$AUDIT_DIR/inventory.g6"
cmp evidence/order8-connected-nontrees.g6 "$AUDIT_DIR/inventory.g6"

"$RESEARCH_PYTHON" evidence/build_rooted_streams.py \
  "$AUDIT_DIR/inventory.g6" \
  "$AUDIT_DIR/base-precanonical.g6" \
  "$AUDIT_DIR/augmented-precanonical.g6" \
  "$AUDIT_DIR/rooted-metadata.json" >/dev/null
"$LABELG" -q -g -fazzzzzzz \
  "$AUDIT_DIR/base-precanonical.g6" "$AUDIT_DIR/base-canonical.g6"
"$LABELG" -q -g -fazzzzzzz \
  "$AUDIT_DIR/augmented-precanonical.g6" "$AUDIT_DIR/augmented-canonical.g6"
cmp evidence/base-rooted-canonical.g6 "$AUDIT_DIR/base-canonical.g6"
cmp evidence/augmented-rooted-canonical.g6 "$AUDIT_DIR/augmented-canonical.g6"

"$CXX" -std=c++20 -O3 -DNDEBUG -Wall -Wextra -pedantic \
  evidence/census_modular.cpp -o "$AUDIT_DIR/census_modular"
"$AUDIT_DIR/census_modular" \
  "$AUDIT_DIR/inventory.g6" \
  "$AUDIT_DIR/base-canonical.g6" \
  "$AUDIT_DIR/augmented-canonical.g6" > "$AUDIT_DIR/census-result.json"

"$RESEARCH_PYTHON" evidence/exact_regression.py > "$AUDIT_DIR/exact-regression.json"

"$RESEARCH_PYTHON" - "$AUDIT_DIR" <<'PY'
import hashlib
import json
import sys
from pathlib import Path

audit = Path(sys.argv[1])
project = Path.cwd()

def load(path):
    return json.loads(path.read_text())

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

expected_census = load(project / "evidence/census-modular-result.json")
actual_census = load(audit / "census-result.json")
expected_census.pop("elapsed_seconds")
actual_census.pop("elapsed_seconds")
assert expected_census == actual_census

expected_regression = load(project / "evidence/exact-regression.json")
actual_regression = load(audit / "exact-regression.json")
assert expected_regression == actual_regression

print(json.dumps({
    "status": "pass",
    "inventory_byte_identity": True,
    "base_rooted_stream_byte_identity": True,
    "augmented_rooted_stream_byte_identity": True,
    "all_non_timing_census_fields_identical": True,
    "exact_regression_byte_semantics_identical": True,
    "inventory_sha256": digest(audit / "inventory.g6"),
    "base_rooted_canonical_sha256": digest(audit / "base-canonical.g6"),
    "augmented_rooted_canonical_sha256": digest(audit / "augmented-canonical.g6"),
    "census_source_sha256": digest(project / "evidence/census_modular.cpp"),
    "exact_regression_source_sha256": digest(project / "evidence/exact_regression.py"),
    "geng_sha256": digest(Path("/opt/homebrew/bin/geng")),
    "labelg_sha256": digest(Path("/opt/homebrew/bin/labelg")),
}, indent=2, sort_keys=True))
PY
