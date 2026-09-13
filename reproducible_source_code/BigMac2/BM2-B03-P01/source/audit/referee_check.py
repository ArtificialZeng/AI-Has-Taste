"""Independent finite sanity checks for the frozen periodic-pattern claim.

These checks are supplementary: the acceptance decision rests on the
symbolic argument reconstructed in audit/math.md.
"""

from math import gcd


def modular_count(q: int, residues: set[int]) -> int:
    return sum(
        u in residues
        and (u + v) % q in residues
        and (u + 3 * v) % q in residues
        for u in range(q)
        for v in range(q)
    )


def is_additive_coset(q: int, residues: set[int]) -> bool:
    c = next(iter(residues))
    translated = {(x - c) % q for x in residues}
    return all((x + y) % q in translated for x in translated for y in translated)


def direct_count(q: int, residues: set[int], n_max: int) -> tuple[int, int]:
    values = {n for n in range(1, n_max + 1) if n % q in residues}
    count = 0
    for x in values:
        for d in range(-n_max, n_max + 1):
            if d and x + d in values and x + 3 * d in values:
                count += 1
    return len(values), count


checked = 0
for q in range(2, 16):
    if gcd(q, 6) != 1:
        continue
    equality_cases = 0
    for mask in range(1, 1 << q):
        residues = {a for a in range(q) if (mask >> a) & 1}
        t_value = modular_count(q, residues)
        size = len(residues)
        assert t_value <= size * size
        assert (t_value == size * size) == is_additive_coset(q, residues)
        equality_cases += int(t_value == size * size)
        checked += 1
    print(
        f"q={q}: checked={(1 << q) - 1}; "
        f"equality_cases={equality_cases}"
    )

print(f"total_nonempty_subsets_checked={checked}")

for q, residues in (
    (5, {0, 1}),
    (5, {2}),
    (7, {0, 1, 3}),
    (7, set(range(7))),
):
    t_value = modular_count(q, residues)
    predicted = t_value / (3 * len(residues) ** 2)
    size, count = direct_count(q, residues, 200)
    print(
        f"sample q={q}, R={sorted(residues)}, T={t_value}, "
        f"predicted={predicted:.12f}, N=200 ratio={count / size**2:.12f}"
    )
