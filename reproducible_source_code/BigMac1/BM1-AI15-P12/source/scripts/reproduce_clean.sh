#!/usr/bin/env bash
set -euo pipefail

REPRO_ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPRO_PYTHON_BIN="${REPRO_PYTHON_BIN:-python3.13}"
REPRO_EXPECTED_PYTHON="3.13.5"
REPRO_ACTUAL_PYTHON="$($REPRO_PYTHON_BIN -c 'import platform; print(platform.python_version())')"

if [[ "$REPRO_ACTUAL_PYTHON" != "$REPRO_EXPECTED_PYTHON" ]]; then
  echo "FAIL: expected CPython $REPRO_EXPECTED_PYTHON, got $REPRO_ACTUAL_PYTHON" >&2
  exit 2
fi

REPRO_TMP_DIR="$(mktemp -d "${TMPDIR:-/tmp}/rank2-marcus-repro.XXXXXX")"
cleanup_repro() {
  if [[ -n "${REPRO_TMP_DIR:-}" && -d "$REPRO_TMP_DIR" ]]; then
    find "$REPRO_TMP_DIR" -depth -delete
  fi
}
trap cleanup_repro EXIT

"$REPRO_PYTHON_BIN" -m venv "$REPRO_TMP_DIR/venv"
REPRO_VENV_PYTHON="$REPRO_TMP_DIR/venv/bin/python"
"$REPRO_VENV_PYTHON" -m pip install \
  --disable-pip-version-check --no-cache-dir --require-hashes \
  -r "$REPRO_ROOT_DIR/requirements-repro.txt"

"$REPRO_VENV_PYTHON" -c \
  'import platform, sympy; assert platform.python_version() == "3.13.5"; assert sympy.__version__ == "1.13.3"; print("PINNED", platform.python_version(), sympy.__version__)'

cd "$REPRO_ROOT_DIR"
"$REPRO_VENV_PYTHON" certificates/verify_n3_sos_stdlib.py
"$REPRO_VENV_PYTHON" certificates/verify_n3_sos.py
"$REPRO_VENV_PYTHON" certificates/test_fail_closed.py
"$REPRO_VENV_PYTHON" certificates/builder_verify_n3_equality.py
"$REPRO_VENV_PYTHON" experiments/builder_verify_n3.py
"$REPRO_VENV_PYTHON" experiments/referee_verify_n3.py
"$REPRO_VENV_PYTHON" experiments/referee_verify_pgl2_equality.py
"$REPRO_VENV_PYTHON" experiments/breaker_verify.py \
  experiments/breaker_random_n3_uv.json \
  experiments/breaker_random_n3_canonical.json \
  experiments/breaker_random_n4_uv.json \
  experiments/breaker_random_n4_canonical.json \
  experiments/breaker_zero_n3.json \
  experiments/breaker_zero_n4.json \
  experiments/breaker_sparse_n3.json \
  experiments/breaker_sparse_n4.json > "$REPRO_TMP_DIR/breaker-verification.json"

if command -v latexmk >/dev/null 2>&1; then
  mkdir -p "$REPRO_TMP_DIR/paper"
  cp paper/main.tex paper/references.bib "$REPRO_TMP_DIR/paper/"
  (
    cd "$REPRO_TMP_DIR/paper"
    latexmk -pdf -interaction=nonstopmode -halt-on-error -silent main.tex
  )
  echo "CLEAN LATEX PASS"
else
  echo "FAIL: latexmk is required for full clean reproduction" >&2
  exit 3
fi

echo "ALL CLEAN REPRODUCTION CHECKS PASSED"
