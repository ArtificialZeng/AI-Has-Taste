#!/usr/bin/env python3
"""Independent exhaustive autocorrelation check for the frozen SDS case."""

from itertools import product


GROUP = tuple(product(range(3), repeat=2))


def subtract(x, y):
    return ((x[0] - y[0]) % 3, (x[1] - y[1]) % 3)


def main():
    tested = 0
    solutions = []
    for zero in GROUP:
        support = tuple(x for x in GROUP if x != zero)
        for signs in product((-1, 1), repeat=8):
            coefficient = dict(zip(support, signs))
            coefficient[zero] = 0
            tested += 1
            correlations = tuple(
                sum(
                    coefficient[x] * coefficient[subtract(x, shift)]
                    for x in GROUP
                )
                for shift in GROUP
            )
            if correlations[0] == 8 and all(value == 1 for value in correlations[1:]):
                solutions.append((zero, signs))

    print(f"full_assignments_tested={tested}")
    print(f"solutions={len(solutions)}")
    assert tested == 9 * 2**8
    assert not solutions
    print("RESULT=PASS: exhaustive exact search found no SDS(9,8,1,C3^2)")


if __name__ == "__main__":
    main()
