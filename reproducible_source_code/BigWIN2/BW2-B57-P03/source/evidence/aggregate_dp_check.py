#!/usr/bin/env python3
"""Exact comparison of an aggregate-prefix DP with a labeled scheduler.

The twelve types are (route, demand), with routes A, B, AB, BA, ABA, BAB
and demands 0, 1.  Both solvers use integer unit-time slots.  The aggregate
solver records counts at every prefix; the labeled solver records the
completed-prefix length of every individually labeled job.  The solvers have
separate transition implementations.
"""

from functools import lru_cache
from itertools import combinations_with_replacement
from math import comb
import argparse
import hashlib
import json
import time

ROUTES = ((0,), (1,), (0, 1), (1, 0), (0, 1, 0), (1, 0, 1))
TYPES = tuple((route, demand) for route in ROUTES for demand in (0, 1))


def aggregate_optimum(counts):
    """Minimum slots using only numbers of type-t jobs at each prefix."""
    offsets = []
    total = 0
    for route, _ in TYPES:
        offsets.append(total)
        total += len(route) + 1
    initial = [0] * total
    for t, count in enumerate(counts):
        initial[offsets[t]] = count
    initial = tuple(initial)

    @lru_cache(maxsize=None)
    def opt(state):
        if all(state[offsets[t] + len(TYPES[t][0])] == counts[t]
               for t in range(len(TYPES))):
            return 0

        ready = []
        for t, (route, demand) in enumerate(TYPES):
            base = offsets[t]
            for prefix, machine in enumerate(route):
                if state[base + prefix]:
                    ready.append((t, prefix, machine, demand))

        actions = [(op,) for op in ready]
        for i, left in enumerate(ready):
            for right in ready[i + 1:]:
                if left[2] == right[2] or left[3] + right[3] > 1:
                    continue
                # Different prefix populations are disjoint.  Equal ones need
                # two jobs, though equal categories cannot in fact use two
                # machines under the present route model.
                if left[:2] == right[:2]:
                    base = offsets[left[0]]
                    if state[base + left[1]] < 2:
                        continue
                actions.append((left, right))

        best = sum(counts[t] * len(TYPES[t][0]) for t in range(len(TYPES)))
        for action in actions:
            nxt = list(state)
            for t, prefix, _, _ in action:
                p = offsets[t] + prefix
                nxt[p] -= 1
                nxt[p + 1] += 1
            best = min(best, 1 + opt(tuple(nxt)))
        return best

    answer = opt(initial)
    return answer, opt.cache_info().currsize


def labeled_optimum(counts):
    """Independent exact scheduler retaining a label for every job."""
    jobs = []
    for type_index, multiplicity in enumerate(counts):
        route, demand = TYPES[type_index]
        for serial in range(multiplicity):
            jobs.append((type_index, serial, route, demand))
    initial = tuple(0 for _ in jobs)

    @lru_cache(maxsize=None)
    def finish_time(progress):
        if all(progress[j] == len(jobs[j][2]) for j in range(len(jobs))):
            return 0

        available = [j for j in range(len(jobs))
                     if progress[j] < len(jobs[j][2])]
        slot_choices = [(j,) for j in available]
        for j in available:
            machine_j = jobs[j][2][progress[j]]
            demand_j = jobs[j][3]
            for k in available:
                if k <= j:
                    continue
                machine_k = jobs[k][2][progress[k]]
                demand_k = jobs[k][3]
                if machine_j != machine_k and not (demand_j and demand_k):
                    slot_choices.append((j, k))

        upper = sum(len(jobs[j][2]) - progress[j] for j in available)
        for chosen in slot_choices:
            successor = list(progress)
            for j in chosen:
                successor[j] += 1
            upper = min(upper, 1 + finish_time(tuple(successor)))
        return upper

    answer = finish_time(initial)
    return answer, finish_time.cache_info().currsize


def weak_compositions(total, parts):
    """Yield all tuples of nonnegative integers summing to total."""
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in weak_compositions(total - first, parts - 1):
            yield (first,) + rest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-jobs", type=int, default=6)
    args = parser.parse_args()
    started = time.time()
    tested = mismatches = aggregate_states = labeled_states = 0
    digest = hashlib.sha256()
    by_size = []

    for n in range(args.max_jobs + 1):
        size_cases = 0
        for counts in weak_compositions(n, len(TYPES)):
            a, a_states = aggregate_optimum(counts)
            b, b_states = labeled_optimum(counts)
            record = json.dumps([counts, a, b], separators=(",", ":"))
            digest.update(record.encode("ascii"))
            digest.update(b"\n")
            tested += 1
            size_cases += 1
            aggregate_states += a_states
            labeled_states += b_states
            if a != b:
                mismatches += 1
                print(json.dumps({"mismatch": counts,
                                  "aggregate": a, "labeled": b}))
                raise SystemExit(1)
        expected = comb(n + len(TYPES) - 1, len(TYPES) - 1)
        assert size_cases == expected
        by_size.append(size_cases)

    expected_total = comb(args.max_jobs + len(TYPES), len(TYPES))
    assert tested == expected_total
    result = {
        "type_order": [
            {"route": "".join("AB"[m] for m in route), "demand": demand}
            for route, demand in TYPES
        ],
        "max_jobs": args.max_jobs,
        "vectors_by_total_jobs": by_size,
        "vectors_tested": tested,
        "expected_vectors": expected_total,
        "mismatches": mismatches,
        "aggregate_states_visited_sum": aggregate_states,
        "labeled_states_visited_sum": labeled_states,
        "record_sha256": digest.hexdigest(),
        "elapsed_seconds": round(time.time() - started, 6),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
