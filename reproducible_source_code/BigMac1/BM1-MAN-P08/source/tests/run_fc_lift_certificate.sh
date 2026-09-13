#!/usr/bin/env bash
set -euo pipefail

TESTS_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$TESTS_DIR/.." && pwd)"
PYTHON_BIN="${PYTHON_BIN:-$(command -v python3)}"

if [ -z "$PYTHON_BIN" ]; then
  echo "FAIL: python3 is unavailable" >&2
  exit 1
fi

WORK_DIR="$(mktemp -d)"
trap 'rm -rf "$WORK_DIR"' EXIT
REBUILT="$WORK_DIR/fc_deletion_lift_bounds.json"

echo "[1/3] Rebuilding the exact recurrence certificate"
"$PYTHON_BIN" "$PROJECT_ROOT/src/fc_deletion_lift.py" "$REBUILT" --stop 50

echo "[2/3] Comparing with the frozen certificate"
cmp "$REBUILT" "$PROJECT_ROOT/results/fc_deletion_lift_bounds.json"
echo "FROZEN COMPARISON: PASS"

echo "[3/3] Running the independent verifier"
"$PYTHON_BIN" "$PROJECT_ROOT/src/verify_fc_deletion_lift.py" "$REBUILT"

echo "FULL FC DELETION-LIFT CERTIFICATE: PASS"
