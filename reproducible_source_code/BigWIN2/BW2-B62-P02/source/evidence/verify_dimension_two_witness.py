#!/usr/bin/env python3
"""Pure-Python exact certificate that the displayed profile has dimension 2."""

from itertools import combinations, permutations
import hashlib
import platform
from pathlib import Path


PROFILE = (
    (0, 0, 0),
    (0, 1, 2),
    (0, 2, 1),
    (0, 2, 1),
    (1, 2, 0),
    (1, 0, 0),
)


def all_matchings():
    ans = []
    for size in range(4):
        for men in combinations(range(3), size):
            for women in combinations(range(3), size):
                for image in permutations(women):
                    p = [None] * 6
                    for man, woman in zip(men, image):
                        p[man], p[3 + woman] = woman, man
                    ans.append(tuple(p))
    assert len(ans) == 34 and len(set(ans)) == 34
    return ans


def rank(agent, partner):
    return 3 if partner is None else PROFILE[agent][partner]


def best_ranks(candidate, matchings):
    return tuple(min(rank(a, matchings[i][a]) for i in candidate)
                 for a in range(6))


def tally(best, alternative):
    alternative_ranks = tuple(rank(a, alternative[a]) for a in range(6))
    support = sum(x < y for x, y in zip(best, alternative_ranks))
    oppose = sum(y < x for x, y in zip(best, alternative_ranks))
    return support, oppose


def edges(matching):
    return "{" + ",".join(f"m{i}-w{matching[i]}" for i in range(3)
                            if matching[i] is not None) + "}"


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    matchings = all_matchings()
    print(f"python={platform.python_version()} script_sha256={sha256(__file__)}")
    print(f"profile={PROFILE}")
    print("SINGLETON_FAILURES_BEGIN")
    for i in range(34):
        best = best_ranks((i,), matchings)
        for y in range(34):
            support, oppose = tally(best, matchings[y])
            if support < oppose:
                print(f"C={i}:{edges(matchings[i])} W={y}:{edges(matchings[y])} "
                      f"votes={support}:{oppose}")
                break
        else:
            raise AssertionError(f"singleton {i} is popular")
    print("SINGLETON_FAILURES_END")

    # Under this generator: index 7 is {m2-w0}; index 28 is the identity perfect matching.
    pair = (7, 28)
    assert edges(matchings[pair[0]]) == "{m2-w0}"
    assert edges(matchings[pair[1]]) == "{m0-w0,m1-w1,m2-w2}"
    best = best_ranks(pair, matchings)
    margins = []
    print("WINNING_PAIR_CHECK_BEGIN")
    for y in range(34):
        support, oppose = tally(best, matchings[y])
        assert support >= oppose
        margins.append(support - oppose)
        print(f"Y={y}:{edges(matchings[y])} votes={support}:{oppose} "
              f"margin={support - oppose}")
    print("WINNING_PAIR_CHECK_END")
    print(f"winning_pair={edges(matchings[pair[0]])};{edges(matchings[pair[1]])}")
    print("margins=" + ",".join(map(str, margins)))
    print("VERIFIED_PROFILE_DIMENSION_EXACTLY_TWO")


if __name__ == "__main__":
    main()
