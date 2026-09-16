"""Bounded intake test of a proposed S22 prefix decoder, not an all-N proof."""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from importlib.util import spec_from_file_location, module_from_spec
from math import isqrt
from pathlib import Path
import json
import platform
import time

BASE = Path(__file__).with_name("check-p10-p11-small.py")
spec = spec_from_file_location("p10_prescreen", BASE)
old = module_from_spec(spec)
spec.loader.exec_module(old)


def decode(values, length, a, b):
    prefix = [a, b]
    while True:
        used = old.schur22_monomials(prefix)
        if any(v > values.get(k, 0) for k, v in used.items()):
            return None, "negative_remaining_multiplicity"
        residual = values - used
        if len(prefix) == length:
            return (tuple(prefix), "exact") if not residual else (None, "residual_at_full_length")
        if not residual:
            return None, "premature_empty"
        x, remainder = divmod(max(residual), a*a*b)
        if remainder or x <= 0 or x > prefix[-1]:
            return None, "nonintegral_or_out_of_order_next_part"
        prefix.append(x)


def main():
    start = time.monotonic()
    count = attempts = 0
    reasons = Counter()
    first_pair_ambiguity = None
    seen_frontiers = {}
    collisions = []
    for n in range(2, 25):
        for p in old.partitions(n):
            if len(p) < 2:
                continue
            count += 1
            values = old.schur22_monomials(p)
            product = isqrt(max(values))
            assert product*product == max(values) == (p[0]*p[1])**2
            decoded, reason = decode(values, len(p), p[0], p[1])
            assert decoded == p, (p, decoded, reason)
            key = (n, len(p), product)
            if key in seen_frontiers and seen_frontiers[key][:2] != p[:2] and first_pair_ambiguity is None:
                other = seen_frontiers[key]
                first_pair_ambiguity = dict(N=n, length=len(p), pair_product=product,
                    a=other, b=p, full_multisets_equal=old.schur22_monomials(other)==values)
            seen_frontiers.setdefault(key, p)
            candidates = []
            for b in range(1, isqrt(product)+1):
                if product % b:
                    continue
                a = product//b
                if a+b+len(p)-2 > n or a+ (len(p)-1)*b < n:
                    continue
                attempts += 1
                candidate, why = decode(values, len(p), a, b)
                reasons[why] += 1
                if candidate is not None and sum(candidate) == n:
                    candidates.append(candidate)
            assert p in candidates
            for q in candidates:
                if p != q:
                    collisions.append([p,q])
    result = dict(schema=1, observed_at_utc=datetime.now(timezone.utc).isoformat(),
        python=platform.python_version(), domain="All positive integer partitions N=2..24, length>=2",
        arithmetic="exact integers and multiplicity Counters", randomness="none",
        partitions=count, true_first_pair_decodes=count, first_pair_attempts=attempts,
        outcomes=dict(reasons), same_N_collisions=collisions,
        first_frontier_ambiguity=first_pair_ambiguity,
        algorithm="Enumerate divisor pairs for sqrt(max S22); remove the complete known-prefix S22 multiset; the proposed next part is max residual divided by a1^2*a2.",
        limitations="Finite decoder validation only. Universal recovery after the true first pair and uniqueness of a surviving first pair at fixed N require proofs. Shared N,length,largest monomial alone need not fix the first pair.",
        script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        imported_script_sha256=sha256(BASE.read_bytes()).hexdigest(),
        elapsed_seconds=time.monotonic()-start)
    target=Path(__file__).with_name("p10-prefix-check.json")
    target.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2))


if __name__ == "__main__":
    main()
