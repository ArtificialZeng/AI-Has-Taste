#!/usr/bin/env bash
set -euo pipefail

TESTS_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$TESTS_DIR/.." && pwd)"
PYTHON_BIN="$(command -v python3)"

if [ -z "$PYTHON_BIN" ]; then
  echo "FAIL: python3 is unavailable" >&2
  exit 1
fi

HUNTER_TMP_DIR="$(mktemp -d)"
cleanup() {
  if [ -n "$HUNTER_TMP_DIR" ] && [ -d "$HUNTER_TMP_DIR" ]; then
    case "$HUNTER_TMP_DIR" in
      /tmp/*|/private/tmp/*|/var/*) rm -rf -- "$HUNTER_TMP_DIR" ;;
      *) echo "REFUSING TO REMOVE UNEXPECTED TEMP PATH: $HUNTER_TMP_DIR" >&2 ;;
    esac
  fi
}
trap cleanup EXIT HUP INT TERM

export PYTHONDONTWRITEBYTECODE=1

echo "[1/4] Running unit and small exhaustive tests"
"$PYTHON_BIN" "$PROJECT_ROOT/src/agent_hunter_test.py"

echo "[2/4] Rebuilding the cap=347 search result in a temporary directory"
"$PYTHON_BIN" "$PROJECT_ROOT/src/agent_hunter_search.py" \
  --cap 347 > "$HUNTER_TMP_DIR/rebuilt_cap347.json"

echo "[3/4] Comparing every frozen deterministic field"
"$PYTHON_BIN" "$PROJECT_ROOT/src/agent_hunter_compare.py" \
  "$PROJECT_ROOT/results/agent_hunter_cap347.json" \
  "$HUNTER_TMP_DIR/rebuilt_cap347.json"

echo "[4/4] Replaying with the independent tuple/trial-division verifier"
"$PYTHON_BIN" "$PROJECT_ROOT/src/agent_hunter_verify.py" \
  "$HUNTER_TMP_DIR/rebuilt_cap347.json" \
  > "$HUNTER_TMP_DIR/independent_verification.json"

"$PYTHON_BIN" -c '
import json
import sys
from pathlib import Path

record = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
if record.get("status") != "PASS":
    raise SystemExit("FAIL: independent verifier did not report PASS")
if record.get("cap") != 347:
    raise SystemExit("FAIL: independent verifier used the wrong cap")
if record.get("exact_divisibility_pass") != 0:
    raise SystemExit("FAIL: a Lehmer candidate was reported")
print("INDEPENDENT REPLAY: PASS")
print("cap:", record["cap"])
print("exact_divisibility_pass:", record["exact_divisibility_pass"])
print("candidate_stream_sha256:", record["candidate_stream_sha256"])
' "$HUNTER_TMP_DIR/independent_verification.json"

echo "FULL CAP=347 CERTIFICATE: PASS"
