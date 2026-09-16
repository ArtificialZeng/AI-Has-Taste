#!/usr/bin/env python3
"""Exact triage check: a fixed K_3,3 profile has no popular matching."""

from itertools import combinations, permutations, product
import platform


def weak_orders():
    result = []
    for ranks in product(range(3), repeat=3):
        used = set(ranks)
        if min(used) == 0 and used == set(range(max(used) + 1)):
            result.append(ranks)
    return result


def all_matchings():
    result = []
    for size in range(4):
        for men in combinations(range(3), size):
            for women in combinations(range(3), size):
                for image in permutations(women):
                    partners = [3] * 6  # 3 denotes unmatched on either side.
                    for man, woman in zip(men, image):
                        partners[man] = woman
                        partners[3 + woman] = man
                    result.append(tuple(partners))
    return result


def edge_string(matching):
    edges = [f"m{man}-w{matching[man]}" for man in range(3)
             if matching[man] != 3]
    return "{" + ",".join(edges) + "}"


def votes(profile, candidate, alternative):
    for_candidate = 0
    for_alternative = 0
    for agent in range(6):
        candidate_rank = (3 if candidate[agent] == 3
                          else profile[agent][candidate[agent]])
        alternative_rank = (3 if alternative[agent] == 3
                            else profile[agent][alternative[agent]])
        for_candidate += candidate_rank < alternative_rank
        for_alternative += alternative_rank < candidate_rank
    return for_candidate, for_alternative


def main():
    orders = weak_orders()
    matchings = all_matchings()
    assert len(orders) == 13 and len(set(orders)) == 13
    assert len(matchings) == 34 and len(set(matchings)) == 34

    # Agent order m0,m1,m2,w0,w1,w2; coordinate conventions are in problem.md.
    profile = (
        (0, 0, 0),
        (0, 1, 2),
        (0, 2, 1),
        (0, 2, 1),
        (1, 2, 0),
        (1, 0, 0),
    )
    assert all(order in orders for order in profile)

    witnesses = []
    for candidate_index, candidate in enumerate(matchings):
        for alternative_index, alternative in enumerate(matchings):
            support, oppose = votes(profile, candidate, alternative)
            if support < oppose:
                witnesses.append((candidate_index, alternative_index,
                                  support, oppose))
                break
        else:
            raise AssertionError(
                f"matching {candidate_index} unexpectedly is popular")

    assert len(witnesses) == 34
    print(f"python={platform.python_version()}")
    print(f"weak_orders={len(orders)} matchings={len(matchings)}")
    print(f"profile={profile}")
    for ci, ai, support, oppose in witnesses:
        print(f"M{ci}={edge_string(matchings[ci])} defeated_by "
              f"M{ai}={edge_string(matchings[ai])} votes={support}:{oppose}")
    print("VERIFIED: no singleton is popular winning for this profile")


if __name__ == "__main__":
    main()
