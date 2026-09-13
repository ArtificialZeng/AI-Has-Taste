#!/usr/bin/env python3
"""No-project-import mutation checks for the independent referee JSON loader."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
VERIFIER = HERE / "independent_verifier.py"


def load_module():
    spec = importlib.util.spec_from_file_location("q5_independent_referee", VERIFIER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load independent verifier")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def expect_failure(label: str, action) -> None:
    try:
        action()
    except Exception:
        return
    raise RuntimeError(f"{label}: malformed JSON was accepted")


def main() -> int:
    module = load_module()
    expect_failure(
        "duplicate top-level key",
        lambda: module.load_json_strict('{"schema":"bad","schema":"good"}'),
    )
    expect_failure(
        "duplicate nested key",
        lambda: module.load_json_strict('{"outer":{"value":0,"value":1}}'),
    )
    expect_failure(
        "boolean in integer slot",
        lambda: module.reject_noncanonical_booleans({"dimension": False}),
    )
    module.reject_noncanonical_booleans(
        {"classification": {"radical": True}},
        frozenset({("classification", "radical")}),
    )
    expect_failure(
        "boolean outside sole allowed star3 path",
        lambda: module.reject_noncanonical_booleans(
            {"classification": {"radical": True}, "schema_version": True},
            frozenset({("classification", "radical")}),
        ),
    )
    print("PASS: independent referee rejected 4 parser attacks and accepted only the canonical star3 boolean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
