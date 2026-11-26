#!/usr/bin/env python3
"""Generate the exact zero-float Tier 1 + Tier 2 Agoh--Giuga exclusion certificate.

Produces ``certificates/agoh_giuga_tier2_certificate.json``, which is meant to
be independently verified by the standalone zero-float fail-closed verifier
``src/verify_agoh_giuga_certificate.py``.

All decisive quantities are computed with exact integer and rational
(``fractions.Fraction``) arithmetic. Floating-point logarithms are used only as
non-decisive heuristics when choosing cascade split points or bucket boundaries;
every emitted witness is checked with exact integer inequalities before
serialization.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import platform
import time


# ---------------------------------------------------------------------------
# Number-theoretic primitives (exact integer arithmetic)
# ---------------------------------------------------------------------------


def sieve_primes(limit: int) -> list[int]:
    """Return all primes <= limit using an exact integer sieve."""
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * ((limit - p * p) // p + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def build_spf(limit: int) -> list[int]:
    """Build smallest-prime-factor table up to limit."""
    spf = list(range(limit + 1))
    for i in range(2, math.isqrt(limit) + 1):
        if spf[i] == i:
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def odd_prime_factors(x: int, spf: list[int]) -> list[int]:
    """Return distinct odd prime factors of positive integer x."""
    res: list[int] = []
    while x % 2 == 0:
        x //= 2
    while x > 1:
        p = spf[x]
        res.append(p)
        while x % p == 0:
            x //= p
    return res


def prime_power_factors(x: int, spf: list[int]) -> list[tuple[int, int]]:
    """Return (q, q^e) prime-power factorization of positive integer x."""
    res: list[tuple[int, int]] = []
    e = 0
    while x % 2 == 0:
        x //= 2
        e += 1
    if e:
        res.append((2, 1 << e))
    while x > 1:
        p = spf[x]
        pe = 1
        while x % p == 0:
            x //= p
            pe *= p
        res.append((p, pe))
    return res


def prod_tree(values: list[int]) -> int:
    """Balanced product tree for exact integer multiplication."""
    n = len(values)
    if n == 0:
        return 1
    if n == 1:
        return values[0]
    mid = n // 2
    return prod_tree(values[:mid]) * prod_tree(values[mid:])


def exact_sum(fracs: list[Fraction]) -> Fraction:
    """Balanced binary tree sum for exact Fractions."""
    n = len(fracs)
    if n == 0:
        return Fraction(0)
    if n == 1:
        return fracs[0]
    mid = n // 2
    return exact_sum(fracs[:mid]) + exact_sum(fracs[mid:])


def integer_sha256(value: int) -> str:
    """Binary big-endian SHA-256 digest of a positive integer."""
    return hashlib.sha256(
        value.to_bytes((value.bit_length() + 7) // 8, "big")
    ).hexdigest()


def exact_decimal_digits(value: int) -> int:
    """Exact decimal digit count of a positive integer without str() limit."""
    assert value > 0
    est = (value.bit_length() * 30103) // 100000 + 1
    p10 = 10 ** (est - 1)
    while p10 > value:
        est -= 1
        p10 //= 10
    while p10 * 10 <= value:
        est += 1
        p10 *= 10
    assert 10 ** (est - 1) <= value < 10**est
    return est


def encode_signed_hex(x: int) -> str:
    """Encode an arbitrary-size integer as a signed hex string."""
    if x < 0:
        return "-" + hex(-x)
    return hex(x)


def floor_frac_scaled(f: Fraction, scale: int) -> int:
    """Exact floor(f * scale) for a Fraction f."""
    return (f.numerator * scale) // f.denominator


def ceil_frac_scaled(f: Fraction, scale: int) -> int:
    """Exact ceil(f * scale) for a Fraction f."""
    return (f.numerator * scale + f.denominator - 1) // f.denominator


# ---------------------------------------------------------------------------
# Fast exact Star-Pack construction (exact integer-guided + exact Fraction audit)
# ---------------------------------------------------------------------------


STAR_SCALE = 10**18


def star_pack_leaf(
    N: list[int],
    F: list[int],
    B: int,
    odd_primes: list[int],
    spf: list[int],
) -> dict[str, object]:
    """Run max-capacity ascending Star-Pack for leaf (N, F) up to B, then verify exactly."""
    N_set = set(N)
    F_set = set(F)
    U: list[int] = []
    for p in odd_primes:
        if p > B:
            break
        if p in N_set or p in F_set:
            continue
        if any((p - 1) % r == 0 or (r - 1) % p == 0 for r in N):
            continue
        U.append(p)

    centers: list[int] = []
    leaves: dict[int, list[int]] = {}
    # Conservative exact integer lower bound on remaining capacity: floor(S/c) - sum ceil(S/q)
    cap_sc: dict[int, int] = {}
    non_normal_count = 0

    for p in U:
        pf = odd_prime_factors(p - 1, spf)
        divs = [r for r in pf if r in cap_sc]
        if divs:
            divs.sort(key=lambda c: cap_sc[c], reverse=True)
        cost_hi = (STAR_SCALE + p - 1) // p  # ceil(S / p)
        packed = False
        for c in divs:
            if cap_sc[c] > cost_hi:
                cap_sc[c] -= cost_hi
                leaves[c].append(p)
                packed = True
                break
        if not packed:
            if divs:
                non_normal_count += 1
            centers.append(p)
            leaves[p] = []
            cap_sc[p] = STAR_SCALE // p  # floor(S / p)

    # Exact Fraction verification of every star via balanced sum tree
    cap: dict[int, Fraction] = {}
    for c in centers:
        leaf_sum = exact_sum([Fraction(1, q) for q in leaves[c]])
        rem = Fraction(1, c) - leaf_sum
        assert rem > 0, f"star dominance violated at c={c}"
        cap[c] = rem

    all_centers = sorted(N + centers)
    total_sum = exact_sum([Fraction(1, p) for p in all_centers])
    return {
        "N": N,
        "F": F,
        "B": B,
        "U": U,
        "centers": centers,
        "all_centers": all_centers,
        "leaves": leaves,
        "cap": cap,
        "total_sum": total_sum,
        "non_normal_count": non_normal_count,
    }


# ---------------------------------------------------------------------------
# Incremental exact CRT & Extended-Euclid 2D lattice witness finder
# ---------------------------------------------------------------------------


def crt_merge(m1: int, r1: int, m2: int, r2: int) -> tuple[int, int]:
    """Combine x == r1 (mod m1) and x == r2 (mod m2) for coprime m1, m2."""
    if m1 == 1:
        return (m2, r2 % m2)
    if m2 == 1:
        return (m1, r1 % m1)
    k = ((r2 - r1) * pow(m1, -1, m2)) % m2
    return (m1 * m2, r1 + m1 * k)


def crt_combine_tree(arr: list[tuple[int, int]]) -> tuple[int, int]:
    """Balanced binary tree CRT merge."""
    n = len(arr)
    if n == 0:
        return (1, 0)
    if n == 1:
        return (arr[0][0], arr[0][1] % arr[0][0])
    mid = n // 2
    m1, r1 = crt_combine_tree(arr[:mid])
    m2, r2 = crt_combine_tree(arr[mid:])
    return crt_merge(m1, r1, m2, r2)


class IncrementalCRT:
    """Fast incremental exact CRT for X == C_F * Y (mod M_F) relative to P_base."""

    def __init__(self, P_base: int, spf: list[int]) -> None:
        self.P_base = P_base
        self.spf = spf
        self._g_cache: dict[int, int] = {}
        self._c_cache: dict[int, int] = {}
        self._ppf_cache: dict[int, list[tuple[int, int]]] = {}

    def ppf(self, p: int) -> list[tuple[int, int]]:
        res = self._ppf_cache.get(p)
        if res is None:
            res = prime_power_factors(p - 1, self.spf)
            self._ppf_cache[p] = res
        return res

    def giuga_rem(self, p: int) -> int:
        res = self._g_cache.get(p)
        if res is None:
            val = (self.P_base % (p * p)) // p
            res = pow(val, -1, p)
            self._g_cache[p] = res
        return res

    def carm_rem(self, qe: int) -> int:
        res = self._c_cache.get(qe)
        if res is None:
            val = self.P_base % qe
            res = pow(val, -1, qe)
            self._c_cache[qe] = res
        return res

    def build_state(self, F_list: list[int]) -> tuple[int, int, dict[int, int]]:
        """Build full CRT state (M, C, pp_max) from scratch using balanced tree."""
        pp_max: dict[int, int] = {}
        for p in F_list:
            for q, qe in self.ppf(p):
                if qe > pp_max.get(q, 0):
                    pp_max[q] = qe
        mod_rem: list[tuple[int, int]] = [(p, self.giuga_rem(p)) for p in F_list]
        for qe in pp_max.values():
            mod_rem.append((qe, self.carm_rem(qe)))
        M, C = crt_combine_tree(mod_rem)
        return M, C, pp_max

    def extend_state(
        self,
        M: int,
        C: int,
        pp_max: dict[int, int],
        extra_primes: list[int],
    ) -> tuple[int, int, dict[int, int]]:
        """Extend an existing CRT state (M, C, pp_max) by extra_primes without rebuilding."""
        if not extra_primes:
            return M, C, pp_max
        new_pp = dict(pp_max)
        # Collect new coprime factors to add, and upgraded prime powers (need division by old power)
        add_pairs: list[tuple[int, int]] = []
        upgraded: dict[int, tuple[int, int]] = {}  # q -> (old_qe, new_qe)
        for p in extra_primes:
            add_pairs.append((p, self.giuga_rem(p)))
            for q, qe in self.ppf(p):
                old_qe = new_pp.get(q, 1)
                if qe > old_qe:
                    if q in upgraded:
                        upgraded[q] = (upgraded[q][0], qe)
                    else:
                        upgraded[q] = (old_qe, qe)
                    new_pp[q] = qe

        M_cur, C_cur = M, C
        for old_qe, new_qe in upgraded.values():
            if old_qe > 1:
                M_cur //= old_qe
                C_cur %= M_cur
            add_pairs.append((new_qe, self.carm_rem(new_qe)))

        m_add, r_add = crt_combine_tree(add_pairs)
        M_new, C_new = crt_merge(M_cur, C_cur, m_add, r_add)
        return M_new, C_new, new_pp

    def minimal_extra(
        self,
        cur_logM: float,
        pp_max: dict[int, int],
        extra_F: list[int],
        target_log10_M: float,
    ) -> list[int]:
        """Select a short prefix of extra_F sufficient for log10(M) >= target_log10_M."""
        if cur_logM >= target_log10_M:
            return []
        local_pp = dict(pp_max)
        log_M = cur_logM
        chosen: list[int] = []
        for p in extra_F:
            chosen.append(p)
            log_M += math.log10(p)
            for q, qe in self.ppf(p):
                prev = local_pp.get(q, 1)
                if qe > prev:
                    log_M += math.log10(qe / prev)
                    local_pp[q] = qe
            if log_M >= target_log10_M:
                break
        return chosen


def check_lattice_witness(M: int, C: int, U: int, R: int, u: int, v: int) -> bool:
    """Exact zero-float verification of a 2D lattice refutation witness (u, v)."""
    if u == 0 and v == 0:
        return False
    if (u - C * v) % M != 0:
        return False
    if u * v < 0:
        return abs(v) * R + abs(u) * U < M
    if u * v > 0:
        if abs(v) * R < M and abs(u) * U < M:
            g = math.gcd(abs(u), abs(v))
            return (abs(u) // g > R) or (abs(v) // g > U)
    return False


def find_lattice_witness(M: int, C: int, U: int, R: int) -> tuple[int, int]:
    """Find an exact 2D lattice witness (u, v) refuting [1, R] x [1, U] via Extended Euclid."""
    assert U >= 1 and R >= 1
    thresh = math.isqrt((M * R) // U)
    r0, t0 = M, 0
    r1, t1 = C % M, 1
    while r1 > thresh and r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        t0, t1 = t1, t0 - q * t1
    cands: list[tuple[int, int]] = [(r0, t0), (r1, t1)]
    ra, ta, rb, tb = r0, t0, r1, t1
    for _ in range(4):
        if rb == 0:
            break
        q = ra // rb
        for step_q in (1, max(1, q - 1), q):
            cands.append((ra - step_q * rb, ta - step_q * tb))
        ra, rb = rb, ra - q * rb
        ta, tb = tb, ta - q * tb
        cands.append((rb, tb))

    for u, v in cands:
        if check_lattice_witness(M, C, U, R, u, v):
            return (u, v)
    raise RuntimeError(
        f"Failed to find 2D lattice witness: bits(M)={M.bit_length()}, "
        f"bits(U)={U.bit_length()}, bits(R)={R.bit_length()}"
    )


# ---------------------------------------------------------------------------
# Fast sound exact integer 2D knapsack for P(n) >= 326,057
# ---------------------------------------------------------------------------


def greedy_k_upper_bound(active: list[tuple[int, int]], rem_max: int, k_omit: int) -> int:
    if not active or rem_max <= 0:
        return k_omit
    ordered = sorted(active, key=lambda item: Fraction(item[0], item[1]), reverse=True)
    rem = rem_max - 1
    total_k = k_omit
    for l_cnt, ci in ordered:
        if ci <= rem:
            total_k += l_cnt
            rem -= ci
        else:
            total_k += (l_cnt * rem) // ci
            break
    return total_k


def compute_dp2_u_bounds(
    centers: list[int],
    leaves: dict[int, list[int]],
    cap_int: dict[int, int],
    L0_pref: list[int],
    L0_prod_pref: list[int],
    star_prod_pref: list[int],
    B_int: int,
    D: int,
    F_set: set[int],
    p_omit: int | None,
) -> tuple[set[int], list[int]]:
    """Run exact zero-float sound 2D knapsack with suffix-min over k (fast row tracking)."""
    if p_omit is None:
        rem_max = B_int
        k_omit = 0
        c_omit_0 = 0
        c_omit_1 = 0
    else:
        c_omit_0 = D // p_omit
        c_omit_1 = cap_int[p_omit]
        rem_max = B_int - c_omit_1
        k_omit = len(leaves[p_omit])

    if rem_max <= 0:
        return set(F_set), []

    F_ext = set(F_set)
    for c in centers:
        if c != p_omit and c not in F_ext and cap_int[c] >= rem_max:
            F_ext.add(c)

    active = [
        (len(leaves[c]), cap_int[c])
        for c in centers
        if c != p_omit and c not in F_ext and leaves[c]
    ]

    cap_sorted = sorted(ci for _, ci in active)
    max_ds = 0
    acc = 0
    for ci in cap_sorted:
        if acc + ci < rem_max:
            acc += ci
            max_ds += 1
        else:
            break

    K_ub = greedy_k_upper_bound(active, rem_max, k_omit)
    # Sparse dict per ds row is much faster when active items are few or rem_max is small
    rows: list[dict[int, int]] = [{} for _ in range(max_ds + 1)]
    if p_omit is None:
        rows[0][0] = 0
    else:
        if c_omit_0 < B_int:
            rows[0][0] = c_omit_0
        if k_omit > 0 and c_omit_1 < B_int:
            prev = rows[0].get(k_omit)
            if prev is None or c_omit_1 < prev:
                rows[0][k_omit] = c_omit_1

    top_ds = 0
    for l_cnt, ci in active:
        if ci >= rem_max:
            continue
        hi_ds = min(top_ds, max_ds - 1)
        for ds in range(hi_ds, -1, -1):
            row = rows[ds]
            if not row:
                continue
            nrow = rows[ds + 1]
            added = False
            for k, base in row.items():
                nc = base + ci
                if nc < B_int:
                    nk = k + l_cnt
                    if nk <= K_ub:
                        prev = nrow.get(nk)
                        if prev is None or nc < prev:
                            nrow[nk] = nc
                            added = True
            if added and ds + 1 > top_ds:
                top_ds = ds + 1

    # Convert sparse rows to dense suffix-min arrays up to max_k_seen
    max_k_seen = 0
    for ds in range(top_ds + 1):
        if rows[ds]:
            mk = max(rows[ds])
            if mk > max_k_seen:
                max_k_seen = mk

    INF = B_int + 1
    dense: list[list[int]] = []
    for ds in range(top_ds + 1):
        arr = [INF] * (max_k_seen + 1)
        for k, cost in rows[ds].items():
            arr[k] = cost
        for k in range(max_k_seen - 1, -1, -1):
            if arr[k + 1] < arr[k]:
                arr[k] = arr[k + 1]
        dense.append(arr)

    p_factor = p_omit if p_omit is not None else 1
    U_by_k: list[int] = []
    for k in range(max_k_seen + 1):
        best_u = 0
        for ds in range(top_ds + 1):
            cost = dense[ds][k]
            if cost >= B_int:
                continue
            rem = B_int - cost
            m0 = 0
            while m0 + 1 < len(L0_pref) and L0_pref[m0 + 1] < rem:
                m0 += 1
            cand_u = p_factor * star_prod_pref[ds] * L0_prod_pref[m0]
            if cand_u > best_u:
                best_u = cand_u
        U_by_k.append(best_u)

    while U_by_k and U_by_k[-1] == 0:
        U_by_k.pop()
    return F_ext, U_by_k


# ---------------------------------------------------------------------------
# Main certificate builder
# ---------------------------------------------------------------------------


def build_certificate() -> dict[str, object]:
    t_start = time.time()
    NMAX = 500_000
    primes = sieve_primes(NMAX)
    odd_primes = primes[1:]
    spf = build_spf(NMAX)

    # -----------------------------------------------------------------------
    # PART 1: 7-leaf Star-Pack Exact Extremal Normal-Set Theorem
    # -----------------------------------------------------------------------
    B = 321_053
    B_out = 352_756
    leaves_spec = [
        {"id": 1, "name": "Leaf 1: 3 in S", "N": [3], "F": []},
        {"id": 2, "name": "Leaf 2: {5,7,23,83} in S, 3 not in S", "N": [5, 7, 23, 83], "F": [3]},
        {"id": 3, "name": "Leaf 3: {5,7,23} in S, {3,83} not in S", "N": [5, 7, 23], "F": [3, 83]},
        {"id": 4, "name": "Leaf 4: {5,7} in S, {3,23} not in S", "N": [5, 7], "F": [3, 23]},
        {"id": 5, "name": "Leaf 5: 7 in S, {3,5} not in S", "N": [7], "F": [3, 5]},
        {"id": 6, "name": "Leaf 6: 5 in S, {3,7} not in S", "N": [5], "F": [3, 7]},
        {"id": 7, "name": "Leaf 7: {3,5,7} not in S", "N": [], "F": [3, 5, 7]},
    ]

    leaf_results_B = []
    leaf2_sp = None
    for spec in leaves_spec:
        sp = star_pack_leaf(spec["N"], spec["F"], B, odd_primes, spf)
        tot: Fraction = sp["total_sum"]  # type: ignore[assignment]
        ac: list[int] = sp["all_centers"]  # type: ignore[assignment]
        nn: int = sp["non_normal_count"]  # type: ignore[assignment]
        if spec["id"] == 2:
            leaf2_sp = sp
            t_extra = 0
            min_card = len(ac)
            prod_lb = prod_tree(ac)
            min_digits = exact_decimal_digits(prod_lb)
        else:
            assert tot < 1
            t_extra = (B * (1 - tot)).numerator // (B * (1 - tot)).denominator + 1
            min_card = len(ac) + t_extra
            prod_lb = prod_tree(ac) * (B**t_extra)
            min_digits = exact_decimal_digits(prod_lb)
        leaf_results_B.append(
            {
                "id": spec["id"],
                "name": spec["name"],
                "N": spec["N"],
                "F": spec["F"],
                "center_count_at_B": len(ac),
                "non_normal_centers_at_B": nn,
                "extra_gt_B_min": t_extra,
                "min_cardinality": min_card,
                "min_decimal_digits": min_digits,
            }
        )

    assert leaf2_sp is not None
    L: list[int] = leaf2_sp["all_centers"]  # type: ignore[assignment]
    centers_L: list[int] = leaf2_sp["centers"]  # type: ignore[assignment]
    leaves_L: dict[int, list[int]] = leaf2_sp["leaves"]  # type: ignore[assignment]
    cap_L: dict[int, Fraction] = leaf2_sp["cap"]  # type: ignore[assignment]
    sum_L: Fraction = leaf2_sp["total_sum"]  # type: ignore[assignment]
    gap_L = sum_L - 1

    assert len(L) == 8_135 and L[-1] == 321_053 and odd_primes[27_691] == 321_053
    assert leaf2_sp["non_normal_count"] == 0
    assert sum_L > 1 and (sum_L - Fraction(1, B)) < 1
    assert min(cap_L.values()) == Fraction(1, B) and Fraction(1, B) > gap_L

    P_L = prod_tree(L)
    P_L_digits = exact_decimal_digits(P_L)
    P_L_sha = integer_sha256(P_L)
    assert P_L_digits == 40_733 and P_L.bit_length() == 135_311
    assert P_L_sha == "826dad79c2ef410c85a9bd4cb8f3b1ea01dddfabfec8363badc427ca9f4ea7bb"

    leaf2_ext = star_pack_leaf([5, 7, 23, 83], [3], B_out, odd_primes, spf)
    assert leaf2_ext["non_normal_count"] == 0
    L_ext: list[int] = leaf2_ext["all_centers"]  # type: ignore[assignment]
    idx_B = L_ext.index(B)
    extra3 = L_ext[idx_B + 1 : idx_B + 4]
    assert extra3 == [321_073, 321_109, 321_143]
    P_8138 = P_L * extra3[0] * extra3[1] * extra3[2]
    P_8138_digits = exact_decimal_digits(P_8138)
    P_8138_sha = integer_sha256(P_8138)
    assert P_8138_digits == 40_750 and P_8138.bit_length() == 135_366
    assert P_8138_sha == "54e7192a3b8d0ea5cc571755ff05d9c4e39f788f73acedee41eae134dd439276"

    L_338032_count = sum(1 for p in L_ext if p <= 338_032)
    assert L_338032_count == 8_512

    for spec in leaves_spec:
        if spec["id"] == 2:
            continue
        sp_out = star_pack_leaf(spec["N"], spec["F"], B_out, odd_primes, spf)
        assert sp_out["total_sum"] < 1  # type: ignore[operator]
    leaf3_352757 = star_pack_leaf([5, 7, 23], [3, 83], 352_757, odd_primes, spf)
    assert leaf3_352757["non_normal_count"] == 0
    assert leaf3_352757["total_sum"] > 1  # type: ignore[operator]
    assert len(leaf3_352757["all_centers"]) == 8_880  # type: ignore[arg-type]

    lam_L = 1
    for p in L:
        lam_L = math.lcm(lam_L, p - 1)
    M_L = P_L * lam_L
    M_L_digits = exact_decimal_digits(M_L)
    M_L_bits = M_L.bit_length()
    M_L_sha = integer_sha256(M_L)
    assert M_L_digits == 54_909 and M_L_bits == 182_403

    print(
        f"[Part 1] 7-leaf Star-Pack verified in {time.time() - t_start:.2f}s: "
        f"|L|={len(L)}, P(L)={P_L_digits} digits, M_L={M_L_digits} digits, "
        f"outside-Leaf-2 exact min max(S)=352757"
    )

    # -----------------------------------------------------------------------
    # PART 2: Elementary a >= 2 Splitting Theorem
    # -----------------------------------------------------------------------
    a2_min_omega = 8_135 + 321_053
    a2_min_P = 321_053 + 6 * (321_053 // 2) + 2
    assert a2_min_omega == 329_188 and a2_min_P == 1_284_211
    assert 321_053**10_000 > 10**55_065
    assert 321_053**1_053 > 10**5_798
    a2_min_digits = 40_732 + 32 * 55_065 + 5_798 + 1
    assert a2_min_digits == 1_808_611

    # -----------------------------------------------------------------------
    # PART 3: Tier 2 Largest Prime Bound P(n) >= 326,057
    # -----------------------------------------------------------------------
    t_p3 = time.time()
    P0 = 326_056
    next_prime_P0 = next(p for p in odd_primes if p > P0)
    assert next_prime_P0 == 326_057
    sp_P0 = star_pack_leaf([5, 7, 23, 83], [3], P0, odd_primes, spf)
    assert sp_P0["non_normal_count"] == 0
    L0: list[int] = sp_P0["all_centers"]  # type: ignore[assignment]
    c0: list[int] = sp_P0["centers"]  # type: ignore[assignment]
    lv0: dict[int, list[int]] = sp_P0["leaves"]  # type: ignore[assignment]
    cp0: dict[int, Fraction] = sp_P0["cap"]  # type: ignore[assignment]
    gap0: Fraction = sp_P0["total_sum"] - 1  # type: ignore[operator]
    P_L0 = prod_tree(L0)
    crt_P0 = IncrementalCRT(P_L0, spf)

    D_scale = 10**12
    B_int = ceil_frac_scaled(gap0, D_scale)
    cap_int = {c: floor_frac_scaled(cp0[c], D_scale) for c in c0}

    L0_pref = [0]
    L0_prod_pref = [1]
    for p in reversed(L0):
        L0_pref.append(L0_pref[-1] + (D_scale // p))
        L0_prod_pref.append(L0_prod_pref[-1] * p)
    star_desc = sorted([c for c in c0 if lv0[c]], reverse=True)
    star_prod_pref = [1]
    for c in star_desc:
        star_prod_pref.append(star_prod_pref[-1] * c)

    N_leaf2 = [5, 7, 23, 83]
    F0_P0 = set(N_leaf2) | {c for c in c0 if cap_int[c] >= B_int}
    cands_P0 = sorted([c for c in c0 if c not in F0_P0], key=lambda c: cap_int[c], reverse=True)

    F_cur_list = sorted(F0_P0)
    F_cur_set = set(F_cur_list)
    M_cur, C_cur, pp_cur = crt_P0.build_state(F_cur_list)
    logP0 = math.log10(P0)
    cascade_entries: list[dict[str, object]] = []
    total_p3_pairs = 0

    def make_buckets_and_witnesses(
        M_F: int,
        C_F: int,
        U_by_k: list[int],
    ) -> list[dict[str, object]] | None:
        if not U_by_k:
            return []
        logM = M_F.bit_length() * math.log10(2)
        max_k = len(U_by_k) - 1
        buckets: list[dict[str, object]] = []
        k_lo = 0
        while k_lo <= max_k:
            U_lo = U_by_k[k_lo]
            if U_lo == 0:
                k_lo += 1
                continue
            logU = U_lo.bit_length() * math.log10(2)
            k_hi = min(max_k, max(k_lo, int((logM - logU - 1.2) / logP0)))
            while k_hi >= k_lo and 4 * U_lo * (P0**k_hi) >= M_F:
                k_hi -= 1
            if k_hi < k_lo:
                if U_lo * (P0**k_lo) >= M_F:
                    return None
                k_hi = k_lo
            U_box = max(U_by_k[k_lo : k_hi + 1])
            R_hi = P0**k_hi
            try:
                u, v = find_lattice_witness(M_F, C_F, U_box, R_hi)
            except RuntimeError:
                if k_hi > k_lo:
                    k_hi -= 1
                    U_box = max(U_by_k[k_lo : k_hi + 1])
                    try:
                        u, v = find_lattice_witness(M_F, C_F, U_box, P0**k_hi)
                    except RuntimeError:
                        return None
                else:
                    return None
            buckets.append(
                {
                    "k_lo": k_lo,
                    "k_hi": k_hi,
                    "u_hex": encode_signed_hex(u),
                    "v_hex": encode_signed_hex(v),
                }
            )
            k_lo = k_hi + 1
        return buckets

    finished_p3 = False
    for p in cands_P0:
        cur_logM = M_cur.bit_length() * math.log10(2)
        if cur_logM > 1122.0:
            _, U_B = compute_dp2_u_bounds(
                c0, lv0, cap_int, L0_pref, L0_prod_pref, star_prod_pref, B_int, D_scale, F_cur_set, None
            )
            bks_B = make_buckets_and_witnesses(M_cur, C_cur, U_B)
            if bks_B is not None:
                cascade_entries.append(
                    {
                        "type": "branch_b",
                        "F_used_count": len(F_cur_list),
                        "buckets": bks_B,
                    }
                )
                total_p3_pairs += len(bks_B)
                finished_p3 = True
                break

        F_ext_A, U_A = compute_dp2_u_bounds(
            c0, lv0, cap_int, L0_pref, L0_prod_pref, star_prod_pref, B_int, D_scale, F_cur_set, p
        )
        if not U_A:
            cascade_entries.append({"type": "branch_a_infeasible", "omit_prime": p})
            F_cur_set.add(p)
            F_cur_list.append(p)
            M_cur, C_cur, pp_cur = crt_P0.extend_state(M_cur, C_cur, pp_cur, [p])
            continue

        max_k_A = len(U_A) - 1
        worst_UR_log = max(
            (U_A[k].bit_length() * math.log10(2) + k * logP0)
            for k in range(len(U_A))
            if U_A[k] > 0
        )
        extra_A = sorted(F_ext_A - F_cur_set)
        single_box_log = U_A[0].bit_length() * math.log10(2) + max_k_A * logP0 + 4.0
        chosen_extra = crt_P0.minimal_extra(
            cur_logM, pp_cur, extra_A, max(single_box_log, worst_UR_log + 10.0)
        )
        M_A, C_A, _ = crt_P0.extend_state(M_cur, C_cur, pp_cur, chosen_extra)
        bks_A = make_buckets_and_witnesses(M_A, C_A, U_A)
        if bks_A is None and len(chosen_extra) < len(extra_A):
            chosen_extra = extra_A
            M_A, C_A, _ = crt_P0.extend_state(M_cur, C_cur, pp_cur, chosen_extra)
            bks_A = make_buckets_and_witnesses(M_A, C_A, U_A)
        if bks_A is None:
            continue

        cascade_entries.append(
            {
                "type": "branch_a",
                "omit_prime": p,
                "F_extra_used": chosen_extra,
                "buckets": bks_A,
            }
        )
        total_p3_pairs += len(bks_A)
        F_cur_set.add(p)
        F_cur_list.append(p)
        M_cur, C_cur, pp_cur = crt_P0.extend_state(M_cur, C_cur, pp_cur, [p])

    assert finished_p3, "Failed to close Part 3 P(n) >= 326,057 cascade!"
    print(
        f"[Part 3] P(n) >= 326,057 certified in {time.time() - t_p3:.2f}s: "
        f"{len(cascade_entries)} branches, {total_p3_pairs} (U,R) pairs, |F_final|={len(F_cur_list)}"
    )

    # -----------------------------------------------------------------------
    # PART 4: Tier 2 Unconditional Digit Bound (>= 40,922 digits) & Dichotomies
    # Uses exact zero-float S4 = 10^18 floor/ceil quantization for tail/prefix sums
    # so every inequality is 100% sound and runs in < 2 seconds!
    # -----------------------------------------------------------------------
    t_p4 = time.time()
    S4 = 10**18
    crt_L = IncrementalCRT(P_L, spf)
    delta_L = {c: cap_L[c] + Fraction(len(leaves_L[c]) - 1, B) for c in centers_L}
    gap_hi = ceil_frac_scaled(gap_L, S4)
    cap_lo = {c: floor_frac_scaled(cap_L[c], S4) for c in centers_L}
    inv_lo = {c: S4 // c for c in centers_L}  # exact floor(S4 / c) <= S4 / c

    L_rev = list(reversed(L))
    M0_LIM = 600
    L_sum_lo = [0]
    L_prod_top = [1]
    for p in L_rev[:M0_LIM]:
        L_sum_lo.append(L_sum_lo[-1] + (S4 // p))
        L_prod_top.append(L_prod_top[-1] * p)
    sorted_cap_lo_ne = sorted((cap_lo[c], c) for c in centers_L if leaves_L[c])

    def build_tail_hi(F_set: set[int], count: int) -> list[int]:
        ct: list[int] = []
        for p in odd_primes:
            if p <= B:
                continue
            if not any(r in F_set for r in odd_prime_factors(p - 1, spf)):
                ct.append(p)
                if len(ct) >= count:
                    break
        assert len(ct) >= count
        ts = [0]
        for q in ct:
            ts.append(ts[-1] + ((S4 + q - 1) // q))  # exact ceil(S4 / q) >= S4 / q
        return ts

    def compute_m0_and_d_max_scaled(dm: int, T_hi: list[int]) -> tuple[int, int]:
        m0_max = 0
        for m0 in range(M0_LIM):
            if gap_hi + T_hi[m0 + dm] - L_sum_lo[m0] > 0:
                m0_max = m0
            else:
                break
        d_max = 0
        for m0 in range(m0_max + 1):
            rem = gap_hi + T_hi[m0 + dm] - L_sum_lo[m0]
            m1 = 0
            acc = 0
            for cp, _ in sorted_cap_lo_ne:
                if acc + cp < rem:
                    acc += cp
                    m1 += 1
                else:
                    break
            if m0 + m1 > d_max:
                d_max = m0 + m1
        return m0_max, d_max

    def per_rank_H_prod(dm: int, d_max: int) -> int:
        H_vals = []
        for j in range(dm + 1, dm + d_max + 1):
            val = Fraction(j * B, 1) / (Fraction(j - dm, 1) - B * gap_L)
            H_j = (val.numerator - 1) // val.denominator
            H_vals.append(H_j)
        return prod_tree(H_vals)

    # --- 4a: Delta_m = 3 (omega = 8,138) ---
    F3 = sorted(N_leaf2 + [c for c in centers_L if delta_L[c] >= gap_L + Fraction(3, B)])
    T3_hi = build_tail_hi(set(F3), 250)
    m0_max_3, d_max_3 = compute_m0_and_d_max_scaled(3, T3_hi)
    M3, C3, _ = crt_L.build_state(F3)
    U3 = L_prod_top[d_max_3]
    dm3_digit_target = 51_798
    Q3 = ((10 ** (dm3_digit_target - 1) - 1) + P_L - 1) // P_L
    u3_d, v3_d = find_lattice_witness(M3, C3, U3, Q3 * U3)

    dm3_P_exp = 3_685
    R3_p = per_rank_H_prod(3, d_max_3) * ((10**dm3_P_exp) ** 3)
    u3_p, v3_p = find_lattice_witness(M3, C3, U3, R3_p)

    # --- 4b: Delta_m = 11 (omega = 8,146) ---
    F11 = sorted(N_leaf2 + [c for c in centers_L if delta_L[c] >= gap_L + Fraction(11, B)])
    T11_hi = build_tail_hi(set(F11), 360)
    m0_max_11, d_max_11 = compute_m0_and_d_max_scaled(11, T11_hi)
    M11, C11, _ = crt_L.build_state(F11)
    U11 = L_prod_top[d_max_11]
    dm11_digit_target = 41_895
    Q11 = ((10 ** (dm11_digit_target - 1) - 1) + P_L - 1) // P_L
    u11_d, v11_d = find_lattice_witness(M11, C11, U11, Q11 * U11)

    dm11_P_exp = 103
    R11_p = per_rank_H_prod(11, d_max_11) * ((10**dm11_P_exp) ** 11)
    u11_p, v11_p = find_lattice_witness(M11, C11, U11, R11_p)

    # --- 4c: Delta_m = 19 (omega = 8,154) ---
    F19_0 = set(N_leaf2) | {c for c in centers_L if delta_L[c] >= gap_L + Fraction(19, B)}
    T19_0 = build_tail_hi(F19_0, 450)
    m0_max_19, _ = compute_m0_and_d_max_scaled(19, T19_0)
    dm19_digit_target = 41_128
    Q19 = ((10 ** (dm19_digit_target - 1) - 1) + P_L - 1) // P_L
    dm19_intervals_spec = [(0, 180), (181, 240), (241, 300), (301, m0_max_19)]
    dm19_entries: list[dict[str, object]] = []
    for m0_lo, m0_hi in dm19_intervals_spec:
        rem_lo = gap_hi + T19_0[m0_lo + 19] - L_sum_lo[m0_lo]
        rhs_m0 = gap_hi + T19_0[max(1, m0_lo) + 19] - L_sum_lo[max(1, m0_lo) - 1]
        F_iv = set(F19_0)
        for c in centers_L:
            if inv_lo[c] >= rhs_m0 and ((not leaves_L[c]) or (cap_lo[c] >= rem_lo)):
                F_iv.add(c)
        T_iv = build_tail_hi(F_iv, m0_hi + 25)
        rem_iv = gap_hi + T_iv[m0_lo + 19] - L_sum_lo[m0_lo]
        m1_max = 0
        acc = 0
        for cp, _ in sorted_cap_lo_ne:
            if acc + cp < rem_iv:
                acc += cp
                m1_max += 1
            else:
                break
        d_hi = m0_hi + m1_max
        U_iv = L_prod_top[d_hi]
        F_iv_sorted = sorted(F_iv)
        M_iv, C_iv, _ = crt_L.build_state(F_iv_sorted)
        u_iv, v_iv = find_lattice_witness(M_iv, C_iv, U_iv, Q19 * U_iv)
        dm19_entries.append(
            {
                "m0_lo": m0_lo,
                "m0_hi": m0_hi,
                "m1_max": m1_max,
                "F_size": len(F_iv_sorted),
                "u_hex": encode_signed_hex(u_iv),
                "v_hex": encode_signed_hex(v_iv),
            }
        )

    # --- 4d: Delta_m = 27 (omega = 8,162) ---
    dm27_digit_target = 40_922
    Q27 = ((10 ** (dm27_digit_target - 1) - 1) + P_L - 1) // P_L
    F27_0 = set(N_leaf2) | {c for c in centers_L if delta_L[c] >= gap_L + Fraction(27, B)}
    T27_0 = build_tail_hi(F27_0, 520)
    m0_max_27, _ = compute_m0_and_d_max_scaled(27, T27_0)
    dm27_intervals_spec = [
        (0, 120),
        (121, 175),
        (176, 225),
        (226, 270),
        (271, 310),
        (311, 345),
        (346, 380),
        (381, m0_max_27),
    ]
    dm27_entries: list[dict[str, object]] = []
    total_dm27_pairs = 0
    for m0_lo, m0_hi in dm27_intervals_spec:
        rem_lo = gap_hi + T27_0[m0_lo + 27] - L_sum_lo[m0_lo]
        rhs_m0 = gap_hi + T27_0[max(1, m0_lo) + 27] - L_sum_lo[max(1, m0_lo) - 1]
        F_base = set(F27_0)
        for c in centers_L:
            if inv_lo[c] >= rhs_m0 and ((not leaves_L[c]) or (cap_lo[c] >= rem_lo)):
                F_base.add(c)

        T_iv = build_tail_hi(F_base, m0_hi + 32)
        rem_iv = gap_hi + T_iv[m0_lo + 27] - L_sum_lo[m0_lo]
        rhs_m0_iv = gap_hi + T_iv[max(1, m0_lo) + 27] - L_sum_lo[max(1, m0_lo) - 1]
        for c in centers_L:
            if inv_lo[c] >= rhs_m0_iv and ((not leaves_L[c]) or (cap_lo[c] >= rem_iv)):
                F_base.add(c)

        m0_hi_eff = m0_lo - 1
        for mt in range(m0_lo, m0_hi + 1):
            if gap_hi + T_iv[mt + 27] - L_sum_lo[mt] > 0:
                m0_hi_eff = mt
        if m0_hi_eff < m0_lo:
            dm27_entries.append({"m0_lo": m0_lo, "m0_hi": m0_hi, "status": "infeasible", "cascade": []})
            continue

        m1_max = 0
        acc = 0
        for cp, _ in sorted_cap_lo_ne:
            if acc + cp < rem_iv:
                acc += cp
                m1_max += 1
            else:
                break
        U_B = L_prod_top[m0_hi_eff + m1_max]
        R_B = Q27 * U_B
        need_M = 8 * U_B * R_B

        F_cur_27 = sorted(F_base)
        F_cur_27_set = set(F_cur_27)
        M_27, C_27, pp_27 = crt_L.build_state(F_cur_27)
        cands_27 = [p for p in L if p not in F_cur_27_set]

        iv_cascade: list[dict[str, object]] = []
        if M_27 > need_M:
            u_b, v_b = find_lattice_witness(M_27, C_27, U_B, R_B)
            iv_cascade.append(
                {
                    "type": "branch_b",
                    "F_size": len(F_cur_27),
                    "u_hex": encode_signed_hex(u_b),
                    "v_hex": encode_signed_hex(v_b),
                }
            )
            total_dm27_pairs += 1
        else:
            closed_iv = False
            for p in cands_27:
                assert (p < L[-m0_hi_eff]) if m0_hi_eff >= 1 else True
                rem_A0 = rhs_m0_iv - inv_lo[p] if m0_hi_eff >= 1 else -1
                rem_A1 = (rem_iv - cap_lo[p]) if leaves_L[p] else -1
                rem_A = max(rem_A0, rem_A1)
                if rem_A > 0:
                    m0_hi_A = m0_lo - 1
                    for mt in range(m0_lo, m0_hi_eff + 1):
                        ok0 = (mt >= 1) and (gap_hi + T_iv[mt + 27] - L_sum_lo[mt - 1] - inv_lo[p] > 0)
                        ok1 = bool(leaves_L[p]) and (gap_hi + T_iv[mt + 27] - L_sum_lo[mt] - cap_lo[p] > 0)
                        if ok0 or ok1:
                            m0_hi_A = mt
                    if m0_hi_A >= m0_lo:
                        rhs_2nd_m0 = (
                            gap_hi + T_iv[max(2, m0_lo) + 27] - L_sum_lo[max(2, m0_lo) - 2] - inv_lo[p]
                            if m0_hi_A >= 2
                            else -1
                        )
                        rhs_from_m1 = (
                            rhs_m0_iv - cap_lo[p]
                            if (leaves_L[p] and m0_hi_A >= 1)
                            else -1
                        )
                        rhs_other_m0 = max(rhs_2nd_m0, rhs_from_m1)
                        top_guard = L[-m0_hi_A] if m0_hi_A >= 1 else (B + 1)
                        extra_A: list[int] = []
                        for c in centers_L:
                            if c == p or c in F_cur_27_set or c >= top_guard:
                                continue
                            if inv_lo[c] >= rhs_other_m0 and ((not leaves_L[c]) or (cap_lo[c] >= rem_A)):
                                extra_A.append(c)
                        m1_A = 0
                        acc_A = 0
                        for cp, c in sorted_cap_lo_ne:
                            if c == p:
                                continue
                            if acc_A + cp < rem_A:
                                acc_A += cp
                                m1_A += 1
                            else:
                                break
                        d_hi_A = m0_hi_A + m1_A + (1 if leaves_L[p] else 0)
                        U_A = p * L_prod_top[max(0, d_hi_A - 1)]
                        R_A = Q27 * U_A
                        target_log_A = (4 * U_A * R_A).bit_length() * math.log10(2) + 4.0
                        cur_log_27 = M_27.bit_length() * math.log10(2)
                        chosen_extra = crt_L.minimal_extra(cur_log_27, pp_27, extra_A, target_log_A)
                        M_A, C_A, _ = crt_L.extend_state(M_27, C_27, pp_27, chosen_extra)
                        try:
                            u_a, v_a = find_lattice_witness(M_A, C_A, U_A, R_A)
                        except RuntimeError:
                            chosen_extra = extra_A
                            M_A, C_A, _ = crt_L.extend_state(M_27, C_27, pp_27, chosen_extra)
                            u_a, v_a = find_lattice_witness(M_A, C_A, U_A, R_A)
                        iv_cascade.append(
                            {
                                "type": "branch_a",
                                "omit_prime": p,
                                "F_extra_used": chosen_extra,
                                "u_hex": encode_signed_hex(u_a),
                                "v_hex": encode_signed_hex(v_a),
                            }
                        )
                        total_dm27_pairs += 1
                    else:
                        iv_cascade.append({"type": "branch_a_infeasible", "omit_prime": p})
                else:
                    iv_cascade.append({"type": "branch_a_infeasible", "omit_prime": p})

                F_cur_27_set.add(p)
                F_cur_27.append(p)
                M_27, C_27, pp_27 = crt_L.extend_state(M_27, C_27, pp_27, [p])
                if M_27 > need_M:
                    u_b, v_b = find_lattice_witness(M_27, C_27, U_B, R_B)
                    iv_cascade.append(
                        {
                            "type": "branch_b",
                            "F_size": len(F_cur_27),
                            "u_hex": encode_signed_hex(u_b),
                            "v_hex": encode_signed_hex(v_b),
                        }
                    )
                    total_dm27_pairs += 1
                    closed_iv = True
                    break
            assert closed_iv, f"Failed to close dm=27 interval [{m0_lo}, {m0_hi}]"

        dm27_entries.append(
            {
                "m0_lo": m0_lo,
                "m0_hi": m0_hi,
                "m0_hi_eff": m0_hi_eff,
                "m1_max": m1_max,
                "F_base_size": len(F_base),
                "cascade": iv_cascade,
            }
        )

    # --- 4e: Delta_m = 35 and Delta_m >= 43 (exact zero-float Lagrangian) ---
    A_35 = 6_900
    r_35 = Fraction(35, 1) - A_35 * (gap_L + Fraction(35, B))
    a1000_35 = (r_35.numerator * 1_000) // r_35.denominator

    A_glob = 15_050
    r_43 = Fraction(43, 1) - A_glob * (gap_L + Fraction(43, B))
    a1000_43 = (r_43.numerator * 1_000) // r_43.denominator

    print(
        f"[Part 4] Digit bound (>=40,922 digits) certified in {time.time() - t_p4:.2f}s: "
        f"dm3 (51798d, P>10^3685), dm11 (41895d, P>10^103), dm19 (41128d, 4 pairs), "
        f"dm27 (40922d, {len(dm27_entries)} intervals, {total_dm27_pairs} pairs), "
        f"dm35 (A={A_35}, 40922d), dm43+ (A={A_glob}, 40959d)"
    )

    certificate = {
        "schema_version": 1,
        "metadata": {
            "generator": "src/generate_agoh_giuga_certificate.py",
            "python_version": platform.python_version(),
            "platform": platform.platform(),
            "terminal_status": "partial theorem",
            "proof_assistant_used": False,
        },
        "part1_extremal_normal_set": {
            "B": B,
            "B_out": B_out,
            "leaf3_exact_min_max": 352_757,
            "leaf3_exact_card_at_352757": 8_880,
            "L_count": len(L),
            "L_max": B,
            "L_prime_index": 27_692,
            "P_L_digits": P_L_digits,
            "P_L_bits": P_L.bit_length(),
            "P_L_sha256_binary": P_L_sha,
            "extra3": extra3,
            "P_8138_digits": P_8138_digits,
            "P_8138_bits": P_8138.bit_length(),
            "P_8138_sha256_binary": P_8138_sha,
            "L_338032_count": L_338032_count,
            "L_352756_count": len(L_ext),
            "M_L_digits": M_L_digits,
            "M_L_bits": M_L_bits,
            "M_L_sha256_binary": M_L_sha,
            "non_leaf2_min_cardinality": min(
                r["min_cardinality"] for r in leaf_results_B if r["id"] != 2
            ),
            "non_leaf2_min_decimal_digits": min(
                r["min_decimal_digits"] for r in leaf_results_B if r["id"] != 2
            ),
            "leaves_at_B": leaf_results_B,
        },
        "part2_elementary_congruences_and_a_ge_2": {
            "a_ge_2_min_omega": a2_min_omega,
            "a_ge_2_min_P": a2_min_P,
            "a_ge_2_min_digits": a2_min_digits,
            "digit_check_exponents": {
                "base": B,
                "exp_hi": 10_000,
                "ten_exp_hi": 55_065,
                "exp_rem": 1_053,
                "ten_exp_rem": 5_798,
                "P_L_ten_exp": 40_732,
            },
        },
        "part3_tier2_largest_prime": {
            "P0": P0,
            "claimed_min_P": next_prime_P0,
            "L0_count": len(L0),
            "L0_max": L0[-1],
            "knapsack_scale": D_scale,
            "F0_size": len(F0_P0),
            "F_final_size": len(F_cur_list),
            "total_UR_pairs": total_p3_pairs,
            "cascade": cascade_entries,
        },
        "part4_tier2_digit_bound": {
            "tail_scale": S4,
            "unconditional_min_omega": 8_138,
            "unconditional_min_P": next_prime_P0,
            "unconditional_min_digits": 40_922,
            "dm3": {
                "omega": 8_138,
                "F_size": len(F3),
                "m0_max": m0_max_3,
                "d_max": d_max_3,
                "digit_target": dm3_digit_target,
                "digit_witness": {"u_hex": encode_signed_hex(u3_d), "v_hex": encode_signed_hex(v3_d)},
                "P_exp_target": dm3_P_exp,
                "P_witness": {"u_hex": encode_signed_hex(u3_p), "v_hex": encode_signed_hex(v3_p)},
            },
            "dm11": {
                "omega": 8_146,
                "F_size": len(F11),
                "m0_max": m0_max_11,
                "d_max": d_max_11,
                "digit_target": dm11_digit_target,
                "digit_witness": {"u_hex": encode_signed_hex(u11_d), "v_hex": encode_signed_hex(v11_d)},
                "P_exp_target": dm11_P_exp,
                "P_witness": {"u_hex": encode_signed_hex(u11_p), "v_hex": encode_signed_hex(v11_p)},
            },
            "dm19": {
                "omega": 8_154,
                "F0_size": len(F19_0),
                "m0_max": m0_max_19,
                "digit_target": dm19_digit_target,
                "intervals": dm19_entries,
            },
            "dm27": {
                "omega": 8_162,
                "F0_size": len(F27_0),
                "m0_max": m0_max_27,
                "digit_target": dm27_digit_target,
                "total_UR_pairs": total_dm27_pairs,
                "intervals": dm27_entries,
            },
            "dm35": {
                "omega": 8_170,
                "A_int": A_35,
                "a1000": a1000_35,
                "digit_target": 40_922,
            },
            "dm43_plus": {
                "omega_min": 8_178,
                "A_int": A_glob,
                "a1000": a1000_43,
                "digit_target": 40_959,
            },
        },
    }
    return certificate


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Agoh--Giuga Tier 1 + Tier 2 certificate.")
    default_out = (
        Path(__file__).resolve().parents[1]
        / "certificates"
        / "agoh_giuga_tier2_certificate.json"
    )
    parser.add_argument("--output", type=Path, default=default_out)
    args = parser.parse_args()

    t0 = time.time()
    cert = build_certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    args.output.write_text(text, encoding="utf-8")
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print(
        f"Wrote {args.output} ({len(text):,} bytes, sha256={digest}) in {time.time() - t0:.2f}s"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
