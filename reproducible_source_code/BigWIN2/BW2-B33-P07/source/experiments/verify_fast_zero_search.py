#!/usr/bin/env python3
"""Fail-closed checker for a fast_zero_search JSON record."""

import json
import sys

from fast_zero_search import INT64_MAX, normalize, search_direct, search_via_and


path = sys.argv[1] if len(sys.argv) > 1 else "experiments/fast-zero-evidence.json"
# Read only the run dimensions before invoking compiled code, then reload the
# complete claim after both computations.  This keeps the verifier independent
# of Python-boxing behavior around long-running JIT calls.
with open(path, encoding="utf-8") as handle:
    dimensions = json.load(handle)
limit = dimensions["limit_inclusive"]
stride = dimensions["checkpoint_stride"]
del dimensions

assert isinstance(limit, int) and 2 <= limit < 1 << 63
assert isinstance(stride, int) and 1 <= stride <= limit
search_direct(2, 1)
search_via_and(2, 1)
direct_raw = search_direct(limit, stride)
via_and_raw = search_via_and(limit, stride)
direct = normalize(direct_raw)
via_and = normalize(via_and_raw)

with open(path, encoding="utf-8") as handle:
    claimed = json.load(handle)

assert claimed["schema_version"] == 1
assert isinstance(limit, int) and 2 <= limit < 1 << 63
assert isinstance(stride, int) and 1 <= stride <= limit
assert claimed["known_zero_indices"] == [0, 6, 11, 23, 36, 42, 48, 54]
assert direct == via_and
assert direct == claimed["direct_xor"] == claimed["and_identity"]
assert claimed["implementations_agree"] is True
assert direct["zero_count"] == 8 and direct["last_zero"] == 54
assert direct["steps_completed"] == limit and direct["overflow_detected"] is False
assert direct["maximum_conservative_step_bound"] <= INT64_MAX
assert claimed["no_signed_overflow"] is True
assert claimed["int64_max"] == INT64_MAX
print(json.dumps({
    "status": "PASS",
    "limit_inclusive": limit,
    "zero_count": direct["zero_count"],
    "last_zero": direct["last_zero"],
    "maximum_conservative_step_bound": direct["maximum_conservative_step_bound"],
}, separators=(",", ":")))
