#!/usr/bin/env python3
"""Exact order-72 orbit census and singleton/pair test for K_3,3.

All decisive arithmetic is on small integers.  Numba changes execution speed,
not the enumerated domain or predicates.  The certificate is checked separately
by verify_extremal.py, which does not import NumPy or Numba.
"""

from itertools import combinations, permutations, product
import hashlib
import platform
from pathlib import Path

import numba
import numpy as np
from numba import njit


PROFILE_COUNT = 13 ** 6


def weak_orders():
    return [r for r in product(range(3), repeat=3)
            if set(r) == set(range(max(r) + 1))]


def inverse(p):
    ans = [0] * 3
    for i, x in enumerate(p):
        ans[x] = i
    return tuple(ans)


def build_actions(orders):
    """Return output-agent -> input-agent maps and induced order maps."""
    order_id = {o: i for i, o in enumerate(orders)}
    perms = list(permutations(range(3)))
    inputs, maps, labels = [], [], []
    for swapped in range(2):
        for pi, p in enumerate(perms):
            for qi, q in enumerate(perms):
                ip, iq = inverse(p), inverse(q)
                input_agent = [0] * 6
                coordinate_map = [None] * 6
                if not swapped:
                    # Old m_i -> new m_p(i); old w_j -> new w_q(j).
                    for k in range(3):
                        input_agent[k], coordinate_map[k] = ip[k], iq
                    for l in range(3):
                        input_agent[3 + l], coordinate_map[3 + l] = 3 + iq[l], ip
                else:
                    # Old m_i -> new w_p(i); old w_j -> new m_q(j).
                    for k in range(3):
                        input_agent[k], coordinate_map[k] = 3 + iq[k], ip
                    for l in range(3):
                        input_agent[3 + l], coordinate_map[3 + l] = ip[l], iq
                order_map = []
                for a in range(6):
                    c = coordinate_map[a]
                    order_map.append([order_id[tuple(o[c[x]] for x in range(3))]
                                      for o in orders])
                inputs.append(input_agent)
                maps.append(order_map)
                labels.append(f"{'swap' if swapped else 'preserve'}:{pi},{qi}")
    return (np.array(inputs, dtype=np.int8), np.array(maps, dtype=np.int8),
            labels)


def fixed_profiles(input_agent, order_map):
    """Count fixed profiles from cycles of the six agent/order variables."""
    inverse_map = [[0] * 13 for _ in range(6)]
    for a in range(6):
        for old in range(13):
            inverse_map[a][order_map[a][old]] = old
    visited = [False] * 6
    answer = 1
    for start in range(6):
        if visited[start]:
            continue
        choices = 0
        for initial in range(13):
            a, value = start, initial
            while True:
                visited[a] = True
                value = inverse_map[a][value]
                a = input_agent[a]
                if a == start:
                    break
            choices += value == initial
        answer *= choices
    return answer


def all_matchings():
    result = []
    for size in range(4):
        for men in combinations(range(3), size):
            for women in combinations(range(3), size):
                for image in permutations(women):
                    partners = [3] * 6
                    for man, woman in zip(men, image):
                        partners[man] = woman
                        partners[3 + woman] = man
                    result.append(tuple(partners))
    return result


@njit(cache=True)
def decode_profile(code):
    p = np.empty(6, dtype=np.int8)
    for a in range(5, -1, -1):
        p[a] = code % 13
        code //= 13
    return p


@njit(cache=True)
def rank_code_from_row(row):
    code = 0
    for a in range(6):
        code = 4 * code + row[a]
    return code


@njit(cache=True)
def is_popular(qcode, ranks, cache_seen, cache_value, generation):
    if cache_seen[qcode] == generation:
        return cache_value[qcode]
    q = np.empty(6, dtype=np.int8)
    x = qcode
    for a in range(5, -1, -1):
        q[a] = x % 4
        x //= 4
    result = 1
    for y in range(34):
        margin = 0
        for a in range(6):
            if q[a] < ranks[y, a]:
                margin += 1
            elif q[a] > ranks[y, a]:
                margin -= 1
        if margin < 0:
            result = 0
            break
    cache_seen[qcode] = generation
    cache_value[qcode] = result
    return result


@njit(cache=True)
def profile_dimension(p, orders, matchings, cache_seen, cache_value, generation):
    ranks = np.empty((34, 6), dtype=np.int8)
    codes = np.empty(34, dtype=np.int16)
    for mi in range(34):
        for a in range(6):
            partner = matchings[mi, a]
            ranks[mi, a] = 3 if partner == 3 else orders[p[a], partner]
        codes[mi] = rank_code_from_row(ranks[mi])
    for i in range(34):
        if is_popular(codes[i], ranks, cache_seen, cache_value, generation):
            return 1
    best = np.empty(6, dtype=np.int8)
    for i in range(34):
        for j in range(i + 1, 34):
            for a in range(6):
                best[a] = min(ranks[i, a], ranks[j, a])
            if is_popular(rank_code_from_row(best), ranks, cache_seen,
                          cache_value, generation):
                return 2
    return 3


@njit(cache=True)
def census(orders, matchings, inputs, maps):
    visited = np.zeros(PROFILE_COUNT, dtype=np.uint8)
    cache_seen = np.zeros(4096, dtype=np.int32)
    cache_value = np.zeros(4096, dtype=np.int8)
    orbit_dimensions = np.zeros(4, dtype=np.int64)
    labelled_dimensions = np.zeros(4, dtype=np.int64)
    images = np.empty(72, dtype=np.int32)
    orbit_count = 0
    covered = 0
    first_extremal_code = -1
    generation = 0
    for code in range(PROFILE_COUNT):
        if visited[code]:
            continue
        p = decode_profile(code)
        minimum = PROFILE_COUNT
        for gi in range(72):
            image = 0
            for a in range(6):
                image = 13 * image + maps[gi, a, p[inputs[gi, a]]]
            images[gi] = image
            if image < minimum:
                minimum = image
        assert minimum == code
        orbit_size = 0
        for gi in range(72):
            image = images[gi]
            if not visited[image]:
                visited[image] = 1
                orbit_size += 1
        orbit_count += 1
        covered += orbit_size
        generation += 1
        d = profile_dimension(p, orders, matchings, cache_seen, cache_value,
                              generation)
        orbit_dimensions[d] += 1
        labelled_dimensions[d] += orbit_size
        if d == 3 and first_extremal_code < 0:
            first_extremal_code = code
    return (orbit_count, covered, orbit_dimensions, labelled_dimensions,
            first_extremal_code)


def edge_string(matching):
    return "{" + ",".join(f"m{i}-w{matching[i]}" for i in range(3)
                            if matching[i] != 3) + "}"


def votes(best, alternative_ranks):
    support = sum(x < y for x, y in zip(best, alternative_ranks))
    oppose = sum(y < x for x, y in zip(best, alternative_ranks))
    return support, oppose


def certificate(profile, orders, matchings):
    ranks = [[3 if matching[a] == 3 else orders[profile[a]][matching[a]]
              for a in range(6)] for matching in matchings]
    failures = []
    for size in (1, 2):
        for candidate in combinations(range(34), size):
            best = [min(ranks[i][a] for i in candidate) for a in range(6)]
            for y in range(34):
                support, oppose = votes(best, ranks[y])
                if support < oppose:
                    failures.append((candidate, y, support, oppose))
                    break
            else:
                raise AssertionError(f"unexpected winning candidate {candidate}")
    assert len(failures) == 34 + 561
    triple = None
    triple_margins = None
    for candidate in combinations(range(34), 3):
        best = [min(ranks[i][a] for i in candidate) for a in range(6)]
        margins = []
        for y in range(34):
            support, oppose = votes(best, ranks[y])
            margins.append(support - oppose)
        if min(margins) >= 0:
            triple, triple_margins = candidate, margins
            break
    assert triple is not None
    return failures, triple, triple_margins


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    orders = weak_orders()
    matchings = all_matchings()
    inputs, maps, labels = build_actions(orders)
    assert len(orders) == 13 and len(matchings) == 34 and len(labels) == 72
    fixed = [fixed_profiles(inputs[g].tolist(), maps[g].tolist())
             for g in range(72)]
    burnside_sum = sum(fixed)
    assert burnside_sum % 72 == 0
    burnside_orbits = burnside_sum // 72
    result = census(np.array(orders, dtype=np.int8),
                    np.array(matchings, dtype=np.int8), inputs, maps)
    orbit_count, covered, orbit_dims, labelled_dims, extremal_code = result
    assert orbit_count == burnside_orbits and covered == PROFILE_COUNT
    assert sum(labelled_dims[1:]) == PROFILE_COUNT

    print(f"python={platform.python_version()} numpy={np.__version__} "
          f"numba={numba.__version__} platform={platform.platform()}")
    print(f"script_sha256={sha256(__file__)}")
    print(f"weak_orders={len(orders)} matchings={len(matchings)} "
          f"labelled_profiles={PROFILE_COUNT} group_order={len(labels)}")
    for g, (label, count) in enumerate(zip(labels, fixed)):
        print(f"BURNSIDE g={g} label={label} fixed={count}")
    print(f"burnside_sum={burnside_sum} burnside_orbits={burnside_orbits}")
    print(f"orbit_enumeration_orbits={orbit_count} covered={covered}")
    print("orbit_dimensions=" + ",".join(f"d{i}:{int(orbit_dims[i])}"
                                               for i in range(1, 4)))
    print("labelled_dimensions=" + ",".join(f"d{i}:{int(labelled_dims[i])}"
                                                  for i in range(1, 4)))
    if extremal_code < 0:
        print("NO_DIMENSION_3_PROFILE")
    else:
        profile = tuple(int(x) for x in decode_profile(extremal_code))
        images = []
        for g in range(72):
            image = 0
            for a in range(6):
                image = 13 * image + int(maps[g, a, profile[int(inputs[g, a])]])
            images.append(image)
        assert min(images) == extremal_code
        failures, triple, margins = certificate(profile, orders, matchings)
        print(f"first_dimension_3_code={extremal_code}")
        print("extremal_profile_ids=" + ",".join(map(str, profile)))
        print("extremal_profile_ranks=" + ";".join(
            "".join(map(str, orders[x])) for x in profile))
        print(f"extremal_orbit_size={len(set(images))}")
        print("PAIR_FAILURE_WITNESSES_BEGIN")
        for candidate, y, support, oppose in failures:
            c = ",".join(map(str, candidate))
            print(f"C={c} W={y} votes={support}:{oppose}")
        print("PAIR_FAILURE_WITNESSES_END")
        print("winning_triple=" + ",".join(map(str, triple)))
        print("winning_triple_matchings=" + ";".join(
            edge_string(matchings[i]) for i in triple))
        print("winning_triple_margins=" + ",".join(map(str, margins)))
    print("VERIFIED_COMPLETE_CENSUS")


if __name__ == "__main__":
    main()
