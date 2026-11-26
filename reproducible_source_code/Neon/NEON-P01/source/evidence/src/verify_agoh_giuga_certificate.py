#!/usr/bin/env python3
"""Standalone 100% zero-float fail-closed verifier for the Agoh--Giuga Tier 1 + Tier 2 certificate.

Uses Python standard library ONLY and ZERO floating-point arithmetic anywhere
in the program (not even for non-decisive helpers or timing). All rational and
integer inequalities are recomputed independently from first principles.

Exit status is 0 iff every mathematical check succeeds; any malformed, missing,
or mathematically invalid certificate fails closed with a nonzero exit code.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
import time


# ---------------------------------------------------------------------------
# Exact integer & rational primitives (ZERO floats)
# ---------------------------------------------------------------------------


STAR_SCALE = 10**18


def fail(msg: str) -> None:
    raise ValueError(f"VERIFICATION FAILED: {msg}")


def require(cond: bool, msg: str) -> None:
    if not cond:
        fail(msg)


def is_exact_int(val: object) -> bool:
    return isinstance(val, int) and not isinstance(val, bool)


def req_int(
    val: object,
    field: str,
    min_val: int | None = None,
    max_val: int | None = None,
) -> int:
    require(is_exact_int(val), f"expected exact int for {field}")
    ival: int = val  # type: ignore[assignment]
    if min_val is not None:
        require(ival >= min_val, f"{field} must be >= {min_val}, got {ival}")
    if max_val is not None:
        require(ival <= max_val, f"{field} must be <= {max_val}, got {ival}")
    return ival


def req_dict(val: object, field: str) -> dict[str, object]:
    require(isinstance(val, dict), f"expected JSON object for {field}")
    return val  # type: ignore[return-value]


def req_list(val: object, field: str) -> list[object]:
    require(isinstance(val, list), f"expected JSON list for {field}")
    return val  # type: ignore[return-value]


def req_key(mapping: dict[str, object], key: str, ctx: str) -> object:
    if key not in mapping:
        fail(f"missing required key {key!r} in {ctx}")
    return mapping[key]


def req_int_list(val: object, field: str, min_val: int | None = None) -> list[int]:
    items = req_list(val, field)
    out: list[int] = []
    for i, item in enumerate(items):
        out.append(req_int(item, f"{field}[{i}]", min_val=min_val))
    return out


def decode_signed_hex(text: object, field: str) -> int:
    require(isinstance(text, str) and len(text) >= 3, f"expected hex string for {field}")
    s = str(text)
    if s.startswith("-0x"):
        require(len(s) >= 4, f"empty hex digits for {field}")
        return -int(s[3:], 16)
    if s.startswith("0x"):
        return int(s[2:], 16)
    fail(f"malformed signed hex string for {field}: {s[:24]!r}")
    return 0


def sieve_primes(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * ((limit - p * p) // p + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def is_prime_exact(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    limit = math.isqrt(n)
    while d <= limit:
        if n % d == 0:
            return False
        d += 2
    return True


def build_spf(limit: int) -> list[int]:
    spf = list(range(limit + 1))
    for i in range(2, math.isqrt(limit) + 1):
        if spf[i] == i:
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def odd_prime_factors(x: int, spf: list[int]) -> list[int]:
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
    n = len(values)
    if n == 0:
        return 1
    if n == 1:
        return values[0]
    mid = n // 2
    return prod_tree(values[:mid]) * prod_tree(values[mid:])


def exact_sum(fracs: list[Fraction]) -> Fraction:
    n = len(fracs)
    if n == 0:
        return Fraction(0)
    if n == 1:
        return fracs[0]
    mid = n // 2
    return exact_sum(fracs[:mid]) + exact_sum(fracs[mid:])


def integer_sha256(value: int) -> str:
    return hashlib.sha256(
        value.to_bytes((value.bit_length() + 7) // 8, "big")
    ).hexdigest()


def floor_frac_scaled(f: Fraction, scale: int) -> int:
    return (f.numerator * scale) // f.denominator


def ceil_frac_scaled(f: Fraction, scale: int) -> int:
    return (f.numerator * scale + f.denominator - 1) // f.denominator


def verify_exact_digits(value: int, expected_digits: int, label: str) -> None:
    req_int(expected_digits, f"{label}: expected_digits", min_val=1)
    require(
        10 ** (expected_digits - 1) <= value < 10**expected_digits,
        f"{label}: value does not have exactly {expected_digits} decimal digits",
    )


def verify_normal_set(primes_list: list[int], spf: list[int], label: str) -> None:
    pset = set(primes_list)
    require(len(pset) == len(primes_list), f"{label}: duplicate primes in set")
    spf_limit = len(spf) - 1
    for p in primes_list:
        require(
            is_exact_int(p) and 3 <= p <= spf_limit and p % 2 == 1 and spf[p] == p,
            f"{label}: non-odd-prime element {p!r}",
        )
        for q in odd_prime_factors(p - 1, spf):
            require(q not in pset, f"{label}: normality violated ({q} | {p}-1)")


# ---------------------------------------------------------------------------
# Independent audited Star-Pack construction (exact Fraction audit of every star)
# ---------------------------------------------------------------------------


def build_and_audit_star_pack(
    N: list[int],
    F: list[int],
    B: int,
    odd_primes: list[int],
    spf: list[int],
    label: str,
) -> dict[str, object]:
    N_set = set(N)
    F_set = set(F)
    require(N_set.isdisjoint(F_set), f"{label}: N and F overlap")
    if N:
        verify_normal_set(N, spf, f"{label}: N")

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
    cap_sc: dict[int, int] = {}
    non_normal_count = 0

    for p in U:
        pf = odd_prime_factors(p - 1, spf)
        divs = [r for r in pf if r in cap_sc]
        if divs:
            divs.sort(key=lambda c: cap_sc[c], reverse=True)
        cost_hi = (STAR_SCALE + p - 1) // p
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
            cap_sc[p] = STAR_SCALE // p

    # Independent exact Fraction audit of EVERY star (does not trust cap_sc)
    seen: set[int] = set()
    cap: dict[int, Fraction] = {}
    for c in centers:
        require(c not in seen, f"{label}: duplicate center {c}")
        seen.add(c)
        for q in leaves[c]:
            require(q not in seen, f"{label}: duplicate leaf {q}")
            require(q > c and (q - 1) % c == 0, f"{label}: invalid star edge ({c}, {q})")
            seen.add(q)
        leaf_sum = exact_sum([Fraction(1, q) for q in leaves[c]])
        rem = Fraction(1, c) - leaf_sum
        require(rem > 0, f"{label}: exact star dominance failed at {c}")
        cap[c] = rem
    require(seen == set(U), f"{label}: star partition does not equal U")

    all_centers = sorted(N + centers)
    total_sum = exact_sum([Fraction(1, p) for p in all_centers])
    if non_normal_count == 0:
        verify_normal_set(all_centers, spf, f"{label}: all_centers")
    return {
        "U": U,
        "centers": centers,
        "all_centers": all_centers,
        "leaves": leaves,
        "cap": cap,
        "total_sum": total_sum,
        "non_normal_count": non_normal_count,
    }


# ---------------------------------------------------------------------------
# Incremental exact CRT & 2D lattice witness verifier
# ---------------------------------------------------------------------------


def crt_merge(m1: int, r1: int, m2: int, r2: int) -> tuple[int, int]:
    if m1 == 1:
        return (m2, r2 % m2)
    if m2 == 1:
        return (m1, r1 % m1)
    require(math.gcd(m1, m2) == 1, "CRT: moduli not coprime")
    k = ((r2 - r1) * pow(m1, -1, m2)) % m2
    return (m1 * m2, r1 + m1 * k)


def crt_combine_tree(arr: list[tuple[int, int]]) -> tuple[int, int]:
    n = len(arr)
    if n == 0:
        return (1, 0)
    if n == 1:
        return (arr[0][0], arr[0][1] % arr[0][0])
    mid = n // 2
    m1, r1 = crt_combine_tree(arr[:mid])
    m2, r2 = crt_combine_tree(arr[mid:])
    return crt_merge(m1, r1, m2, r2)


class ExactIncrementalCRT:
    def __init__(self, P_base: int, spf: list[int]) -> None:
        self.P_base = P_base
        self.spf = spf
        self._g_cache: dict[int, int] = {}
        self._c_cache: dict[int, int] = {}
        self._ppf_cache: dict[int, list[tuple[int, int]]] = {}

    def _ppf(self, p: int) -> list[tuple[int, int]]:
        res = self._ppf_cache.get(p)
        if res is None:
            res = prime_power_factors(p - 1, self.spf)
            self._ppf_cache[p] = res
        return res

    def _giuga(self, p: int) -> int:
        res = self._g_cache.get(p)
        if res is None:
            require(self.P_base % p == 0, f"CRT: prime {p} does not divide P_base")
            val = (self.P_base % (p * p)) // p
            require(val != 0, f"CRT: P_base divisible by {p}^2")
            res = pow(val, -1, p)
            self._g_cache[p] = res
        return res

    def _carm(self, qe: int) -> int:
        res = self._c_cache.get(qe)
        if res is None:
            val = self.P_base % qe
            require(math.gcd(val, qe) == 1, f"CRT: gcd(P_base, {qe}) != 1")
            res = pow(val, -1, qe)
            self._c_cache[qe] = res
        return res

    def build_state(self, F_list: list[int]) -> tuple[int, int, dict[int, int]]:
        require(len(F_list) >= 1, "CRT: empty forced set")
        require(len(set(F_list)) == len(F_list), "CRT: duplicate prime in F_list")
        pp_max: dict[int, int] = {}
        for p in F_list:
            for q, qe in self._ppf(p):
                if qe > pp_max.get(q, 0):
                    pp_max[q] = qe
        f_set = set(F_list)
        for q in pp_max:
            require(q not in f_set, f"CRT: normality failure ({q} in F and divides lam(F))")
        mod_rem: list[tuple[int, int]] = [(p, self._giuga(p)) for p in F_list]
        for qe in pp_max.values():
            mod_rem.append((qe, self._carm(qe)))
        M, C = crt_combine_tree(mod_rem)
        return M, C, pp_max

    def extend_state(
        self,
        M: int,
        C: int,
        pp_max: dict[int, int],
        extra_primes: list[int],
    ) -> tuple[int, int, dict[int, int]]:
        if not extra_primes:
            return M, C, pp_max
        new_pp = dict(pp_max)
        add_pairs: list[tuple[int, int]] = []
        upgraded: dict[int, tuple[int, int]] = {}
        for p in extra_primes:
            add_pairs.append((p, self._giuga(p)))
            for q, qe in self._ppf(p):
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
                require(M_cur % old_qe == 0, "CRT extend: old_qe does not divide M_cur")
                M_cur //= old_qe
                C_cur %= M_cur
            add_pairs.append((new_qe, self._carm(new_qe)))

        m_add, r_add = crt_combine_tree(add_pairs)
        M_new, C_new = crt_merge(M_cur, C_cur, m_add, r_add)
        return M_new, C_new, new_pp


def verify_lattice_witness(
    M: int,
    C: int,
    U: int,
    R: int,
    u: int,
    v: int,
    label: str,
) -> None:
    require(M > 1 and U >= 1 and R >= 1, f"{label}: invalid bounds M/U/R")
    require(not (u == 0 and v == 0), f"{label}: zero lattice witness")
    require((u - C * v) % M == 0, f"{label}: witness (u, v) not in lattice Lambda_F")
    if u * v < 0:
        require(
            abs(v) * R + abs(u) * U < M,
            f"{label}: opposite-sign witness fails |v|*R + |u|*U < M",
        )
    elif u * v > 0:
        require(
            abs(v) * R < M and abs(u) * U < M,
            f"{label}: same-sign witness fails max(|v|*R, |u|*U) < M",
        )
        g = math.gcd(abs(u), abs(v))
        require(
            (abs(u) // g > R) or (abs(v) // g > U),
            f"{label}: same-sign primitive ray lies inside [1, R] x [1, U]",
        )
    else:
        fail(f"{label}: degenerate axis-aligned witness u={u}, v={v}")


# ---------------------------------------------------------------------------
# Fast sound zero-float 2D knapsack for Part 3
# ---------------------------------------------------------------------------


def greedy_k_upper_bound(active: list[tuple[int, int]], rem_max: int, k_omit: int) -> int:
    if not active or rem_max <= 0:
        return k_omit
    for l_cnt, ci in active:
        require(is_exact_int(l_cnt) and l_cnt >= 1, f"invalid star leaf count {l_cnt!r}")
        require(is_exact_int(ci) and ci > 0, f"non-positive star capacity {ci!r}")
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
# Verification of Mod-8/16, r=2 barrier, and all 4 certificate parts
# ---------------------------------------------------------------------------


def verify_mod16_congruence_exhaustively() -> None:
    inv16 = {1: 1, 3: 11, 5: 13, 7: 7, 9: 9, 11: 3, 13: 5, 15: 15}
    for x, inv_x in inv16.items():
        require((x * inv_x) % 16 == 1, f"inv16 table error at {x}")
    for base in (1, 3, 5, 7, 9, 11, 13, 15):
        for k in (1, 3, 5, 7):
            d1 = (inv16[k] - inv16[(base * k) % 16]) % 16
            d2 = (inv16[k + 8] - inv16[(base * (k + 8)) % 16]) % 16
            require(d1 == d2, f"+8 invariance failed at base={base}, k={k}")
    for c1 in range(2):
        for c3 in range(8):
            for c5 in range(8):
                for c7 in range(8):
                    r = c3 + c7
                    if r % 4 not in (0, 1):
                        continue
                    m = c1 + c3 + c5 + c7
                    s_inv = (c1 + 11 * c3 + 13 * c5 + 7 * c7) % 16
                    n_mod = (pow(3, c3, 16) * pow(5, c5, 16) * pow(7, c7, 16)) % 16
                    a_mod = (s_inv - inv16[n_mod]) % 16
                    lhs = (m - a_mod - 1) % 16
                    rhs = (2 * r + 8 * c3) % 16 if r % 4 == 0 else (2 * (r - 1) + 8 * c5) % 16
                    require(lhs == rhs, f"mod-16 formula mismatch at {(c1, c3, c5, c7)}")
                    require(lhs % 8 == 0, f"mod-8 congruence mismatch at {(c1, c3, c5, c7)}")


def verify_r2_barrier_constants() -> None:
    # t_0(3)^3 = (5 + 2*sqrt(13))/27 < 4523/10000 and t_0(3)^3 + 1/10^5 < 4523/10000
    rhs1 = 27 * 4_523 - 50_000
    require(rhs1 == 72_121 and 13 * (20_000**2) < rhs1**2, "r=2 t0(3)^3 < 0.4523 failed")
    rhs2 = 27 * 45_229 - 500_000
    require(13 * (200_000**2) < rhs2**2, "r=2 t0(3)^3 + 10^-5 < 0.4523 failed")


def verify_certificate(cert: dict[str, object]) -> dict[str, object]:
    t0_ns = time.monotonic_ns()
    cert_obj = req_dict(cert, "certificate root")
    schema_v = req_int(req_key(cert_obj, "schema_version", "root"), "schema_version")
    require(schema_v == 1, "unsupported schema_version")

    NMAX = 500_000
    primes = sieve_primes(NMAX)
    odd_primes = primes[1:]
    spf = build_spf(NMAX)

    # -----------------------------------------------------------------------
    # Verify Part 1: 7-leaf Star-Pack Exact Extremal Normal-Set Theorem
    # -----------------------------------------------------------------------
    p1 = req_dict(req_key(cert_obj, "part1_extremal_normal_set", "root"), "part1_extremal_normal_set")
    B = req_int(req_key(p1, "B", "part1"), "part1.B")
    B_out = req_int(req_key(p1, "B_out", "part1"), "part1.B_out")
    require(B == 321_053 and B_out == 352_756, "unexpected B or B_out")
    require(odd_primes[27_691] == 321_053, "q_27692 != 321053")

    leaves_raw = req_list(req_key(p1, "leaves_at_B", "part1"), "part1.leaves_at_B")
    require(len(leaves_raw) == 7, "expected 7 leaves")

    branch_primes = [3, 5, 7, 23, 83]
    branch_set = set(branch_primes)
    parsed_leaves: list[tuple[int, list[int], list[int], dict[str, object]]] = []
    seen_ids: set[int] = set()
    for l_idx, lf_obj in enumerate(leaves_raw):
        lf = req_dict(lf_obj, f"leaves_at_B[{l_idx}]")
        lf_id = req_int(req_key(lf, "id", f"leaf[{l_idx}]"), f"leaf[{l_idx}].id", min_val=1)
        require(lf_id not in seen_ids, f"duplicate leaf id {lf_id}")
        seen_ids.add(lf_id)
        N_lf = req_int_list(req_key(lf, "N", f"leaf {lf_id}"), f"leaf {lf_id}.N", min_val=3)
        F_lf = req_int_list(req_key(lf, "F", f"leaf {lf_id}"), f"leaf {lf_id}.F", min_val=3)
        require(len(set(N_lf)) == len(N_lf), f"leaf {lf_id}: duplicate prime in N")
        require(len(set(F_lf)) == len(F_lf), f"leaf {lf_id}: duplicate prime in F")
        require(
            set(N_lf).issubset(branch_set) and set(F_lf).issubset(branch_set),
            f"leaf {lf_id}: N/F must be subsets of branch_primes={branch_primes}",
        )
        require(set(N_lf).isdisjoint(set(F_lf)), f"leaf {lf_id}: N and F overlap")
        if lf_id == 2:
            require(
                sorted(N_lf) == [5, 7, 23, 83] and sorted(F_lf) == [3],
                "Leaf 2 must have N=[5, 7, 23, 83] and F=[3]",
            )
        if lf_id == 3:
            require(
                sorted(N_lf) == [5, 7, 23] and sorted(F_lf) == [3, 83],
                "Leaf 3 must have N=[5, 7, 23] and F=[3, 83]",
            )
        parsed_leaves.append((lf_id, N_lf, F_lf, lf))

    for mask in range(1 << len(branch_primes)):
        chosen = {branch_primes[i] for i in range(len(branch_primes)) if (mask >> i) & 1}
        matched = []
        for lf_id, N_lf, F_lf, _ in parsed_leaves:
            if set(N_lf).issubset(chosen) and set(F_lf).isdisjoint(chosen):
                matched.append(lf_id)
        require(len(matched) == 1, f"7-leaf partition failed at mask={mask}: matched={matched}")

    leaf2_sp = None
    min_non_leaf2_card = None
    min_non_leaf2_digits = None
    for lf_id, N_lf, F_lf, lf in parsed_leaves:
        sp = build_and_audit_star_pack(N_lf, F_lf, B, odd_primes, spf, f"Part1 Leaf {lf_id} at B")
        tot: Fraction = sp["total_sum"]  # type: ignore[assignment]
        ac: list[int] = sp["all_centers"]  # type: ignore[assignment]
        nn: int = sp["non_normal_count"]  # type: ignore[assignment]
        c_cnt = req_int(req_key(lf, "center_count_at_B", f"Leaf {lf_id}"), f"Leaf {lf_id}.center_count_at_B")
        nn_cnt = req_int(
            req_key(lf, "non_normal_centers_at_B", f"Leaf {lf_id}"),
            f"Leaf {lf_id}.non_normal_centers_at_B",
        )
        require(len(ac) == c_cnt, f"Leaf {lf_id} center count mismatch")
        require(nn == nn_cnt, f"Leaf {lf_id} non-normal count mismatch")
        if lf_id == 2:
            leaf2_sp = sp
            require(nn == 0, "Leaf 2 must be 100% normal at B")
            require(tot > 1 and (tot - Fraction(1, B)) < 1, "Leaf 2 sum threshold mismatch")
            require(len(ac) == 8_135 and ac[-1] == 321_053, "Leaf 2 L != L_27692")
            cap_L_chk: dict[int, Fraction] = sp["cap"]  # type: ignore[assignment]
            require(min(cap_L_chk.values()) == Fraction(1, B), "Leaf 2 min cap != 1/B")
            require(Fraction(1, B) > tot - 1, "Leaf 2 1/B <= gap")
        else:
            require(tot < 1, f"Non-Leaf-2 Leaf {lf_id} has sum >= 1 at B")
            gap_below = B * (1 - tot)
            t_extra = gap_below.numerator // gap_below.denominator + 1
            t_cert = req_int(req_key(lf, "extra_gt_B_min", f"Leaf {lf_id}"), f"Leaf {lf_id}.extra_gt_B_min")
            require(t_extra == t_cert, f"Leaf {lf_id} t_extra mismatch")
            min_card = len(ac) + t_extra
            mc_cert = req_int(
                req_key(lf, "min_cardinality", f"Leaf {lf_id}"), f"Leaf {lf_id}.min_cardinality"
            )
            require(min_card == mc_cert, f"Leaf {lf_id} min_cardinality mismatch")
            prod_lb = prod_tree(ac) * (B**t_extra)
            md_cert = req_int(
                req_key(lf, "min_decimal_digits", f"Leaf {lf_id}"),
                f"Leaf {lf_id}.min_decimal_digits",
                min_val=1,
            )
            verify_exact_digits(prod_lb, md_cert, f"Leaf {lf_id} product LB")
            if min_non_leaf2_card is None or min_card < min_non_leaf2_card:
                min_non_leaf2_card = min_card
            if min_non_leaf2_digits is None or md_cert < min_non_leaf2_digits:
                min_non_leaf2_digits = md_cert
            sp_out = build_and_audit_star_pack(
                N_lf, F_lf, B_out, odd_primes, spf, f"Part1 Leaf {lf_id} at B_out"
            )
            require(sp_out["total_sum"] < 1, f"Leaf {lf_id} exceeds 1 at B_out={B_out}")  # type: ignore[operator]

    require(leaf2_sp is not None, "Leaf 2 missing")
    require(min_non_leaf2_card == 8_846, "non-Leaf-2 min cardinality != 8846")
    require(min_non_leaf2_digits == 44_628, "non-Leaf-2 min digits != 44628")

    leaf3_exact = build_and_audit_star_pack(
        [5, 7, 23], [3, 83], 352_757, odd_primes, spf, "Part1 Leaf 3 at 352757"
    )
    require(leaf3_exact["non_normal_count"] == 0, "Leaf 3 at 352757 not normal")
    tot3: Fraction = leaf3_exact["total_sum"]  # type: ignore[assignment]
    require(tot3 > 1 and (tot3 - Fraction(1, 352_757)) < 1, "Leaf 3 at 352757 sum check failed")
    require(len(leaf3_exact["all_centers"]) == 8_880, "Leaf 3 at 352757 card != 8880")  # type: ignore[arg-type]
    cap3: dict[int, Fraction] = leaf3_exact["cap"]  # type: ignore[assignment]
    require(min(cap3.values()) > tot3 - 1, "Leaf 3 uniqueness margin failed")

    leaf2_ext = build_and_audit_star_pack(
        [5, 7, 23, 83], [3], B_out, odd_primes, spf, "Part1 Leaf 2 at B_out"
    )
    require(leaf2_ext["non_normal_count"] == 0, "Leaf 2 not normal through B_out=352756")
    L: list[int] = leaf2_sp["all_centers"]  # type: ignore[assignment]
    centers_L: list[int] = leaf2_sp["centers"]  # type: ignore[assignment]
    leaves_L: dict[int, list[int]] = leaf2_sp["leaves"]  # type: ignore[assignment]
    cap_L: dict[int, Fraction] = leaf2_sp["cap"]  # type: ignore[assignment]
    sum_L: Fraction = leaf2_sp["total_sum"]  # type: ignore[assignment]
    gap_L = sum_L - 1

    L_ext: list[int] = leaf2_ext["all_centers"]  # type: ignore[assignment]
    require(sum(1 for p in L_ext if p <= 338_032) == 8_512, "|L_338032| != 8512")
    require(
        len(L_ext) == req_int(req_key(p1, "L_352756_count", "part1"), "part1.L_352756_count"),
        "|L_352756| mismatch",
    )

    P_L = prod_tree(L)
    verify_exact_digits(P_L, 40_733, "P(L)")
    require(P_L.bit_length() == 135_311, "P(L) bit length != 135311")
    P_L_sha = integer_sha256(P_L)
    require(P_L_sha == req_key(p1, "P_L_sha256_binary", "part1"), "P(L) SHA-256 mismatch")

    idx_B = L_ext.index(B)
    extra3 = L_ext[idx_B + 1 : idx_B + 4]
    extra3_cert = req_int_list(req_key(p1, "extra3", "part1"), "part1.extra3", min_val=3)
    require(extra3 == [321_073, 321_109, 321_143] and extra3 == extra3_cert, "extra3 mismatch")
    P_8138 = P_L * extra3[0] * extra3[1] * extra3[2]
    verify_exact_digits(P_8138, 40_750, "P_8138")
    require(P_8138.bit_length() == 135_366, "P_8138 bit length != 135366")
    P_8138_sha = integer_sha256(P_8138)
    require(P_8138_sha == req_key(p1, "P_8138_sha256_binary", "part1"), "P_8138 SHA-256 mismatch")

    L_alt = L[:-1] + [321_073]
    verify_normal_set(L_alt, spf, "Non-uniqueness witness L_alt")
    require(len(L_alt) == 8_135, "L_alt size != 8135")
    require(sum_L - Fraction(1, 321_053) + Fraction(1, 321_073) > 1, "L_alt sum <= 1")

    lam_L = 1
    for p in L:
        lam_L = math.lcm(lam_L, p - 1)
    M_L = P_L * lam_L
    verify_exact_digits(M_L, 54_909, "M_L")
    require(M_L.bit_length() == 182_403, "M_L bit length != 182403")
    M_L_sha = integer_sha256(M_L)
    if "M_L_bits" in p1:
        require(req_int(p1["M_L_bits"], "part1.M_L_bits") == 182_403, "M_L_bits mismatch")
    if "M_L_sha256_binary" in p1:
        require(p1["M_L_sha256_binary"] == M_L_sha, "M_L SHA-256 mismatch")

    # -----------------------------------------------------------------------
    # Verify Part 2: Mod-8/16 congruences, r=2 barrier constants, and a >= 2
    # -----------------------------------------------------------------------
    verify_mod16_congruence_exhaustively()
    verify_r2_barrier_constants()

    p2 = req_dict(req_key(cert_obj, "part2_elementary_congruences_and_a_ge_2", "root"), "part2")
    a2_omega = req_int(req_key(p2, "a_ge_2_min_omega", "part2"), "part2.a_ge_2_min_omega")
    require(a2_omega == 8_135 + 321_053 == 329_188, "a>=2 min omega mismatch")
    require(321_053 % 6 == 5, "321053 mod 6 != 5")
    a2_min_P = 321_053 + 6 * (321_053 // 2) + 2
    a2_P_cert = req_int(req_key(p2, "a_ge_2_min_P", "part2"), "part2.a_ge_2_min_P")
    require(a2_min_P == 1_284_211 and a2_min_P == a2_P_cert, "a>=2 min P mismatch")
    require(is_prime_exact(a2_min_P), "1284211 is not prime")
    require(321_053**10_000 > 10**55_065, "321053^10000 > 10^55065 failed")
    require(321_053**1_053 > 10**5_798, "321053^1053 > 10^5798 failed")
    require(P_L >= 10**40_732, "P_L >= 10^40732 failed")
    a2_digits_cert = req_int(req_key(p2, "a_ge_2_min_digits", "part2"), "part2.a_ge_2_min_digits")
    require(
        40_732 + 32 * 55_065 + 5_798 + 1 == 1_808_611 == a2_digits_cert,
        "a>=2 min digits mismatch",
    )

    # -----------------------------------------------------------------------
    # Verify Part 3: Tier 2 Largest Prime Bound P(n) >= 326,057
    # -----------------------------------------------------------------------
    p3 = req_dict(req_key(cert_obj, "part3_tier2_largest_prime", "root"), "part3")
    P0 = req_int(req_key(p3, "P0", "part3"), "part3.P0")
    require(P0 == 326_056, "unexpected P0")
    next_prime_P0 = next(p for p in odd_primes if p > P0)
    claimed_min_P = req_int(req_key(p3, "claimed_min_P", "part3"), "part3.claimed_min_P")
    require(next_prime_P0 == 326_057 and next_prime_P0 == claimed_min_P, "next prime mismatch")
    require(P0 <= B_out, "P0 exceeds non-Leaf-2 exclusion threshold B_out")

    sp_P0 = build_and_audit_star_pack([5, 7, 23, 83], [3], P0, odd_primes, spf, "Part3 Leaf 2 at P0")
    require(sp_P0["non_normal_count"] == 0, "Part3 Leaf 2 not normal at P0")
    L0: list[int] = sp_P0["all_centers"]  # type: ignore[assignment]
    c0: list[int] = sp_P0["centers"]  # type: ignore[assignment]
    lv0: dict[int, list[int]] = sp_P0["leaves"]  # type: ignore[assignment]
    cp0: dict[int, Fraction] = sp_P0["cap"]  # type: ignore[assignment]
    gap0: Fraction = sp_P0["total_sum"] - 1  # type: ignore[operator]
    require(
        len(L0) == req_int(req_key(p3, "L0_count", "part3"), "part3.L0_count")
        and L0[-1] == req_int(req_key(p3, "L0_max", "part3"), "part3.L0_max"),
        "Part3 L0 metadata mismatch",
    )

    P_L0 = prod_tree(L0)
    crt_P0 = ExactIncrementalCRT(P_L0, spf)
    D_scale = req_int(req_key(p3, "knapsack_scale", "part3"), "part3.knapsack_scale", min_val=10**9)
    B_int = ceil_frac_scaled(gap0, D_scale)
    cap_int = {c: floor_frac_scaled(cp0[c], D_scale) for c in c0}
    require(min(cap_int.values()) > 0, "Part3 knapsack_scale too small: zero scaled capacity")

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
    F_cur_set = set(F0_P0)
    F_cur_list = sorted(F0_P0)
    M_cur, C_cur, pp_cur = crt_P0.build_state(F_cur_list)
    c0_set = set(c0)

    cascade = req_list(req_key(p3, "cascade", "part3"), "part3.cascade")
    require(len(cascade) >= 1, "Part3 cascade empty")
    closed_p3 = False
    verified_p3_pairs = 0

    for idx, entry_obj in enumerate(cascade):
        entry = req_dict(entry_obj, f"part3.cascade[{idx}]")
        etype = req_key(entry, "type", f"part3.cascade[{idx}]")
        if etype == "branch_a_infeasible":
            p = req_int(req_key(entry, "omit_prime", f"part3[{idx}]"), f"part3[{idx}].omit_prime", min_val=3)
            require(p in c0_set and p not in F_cur_set, f"Part3 step {idx}: invalid omit_prime {p}")
            _, U_A = compute_dp2_u_bounds(
                c0, lv0, cap_int, L0_pref, L0_prod_pref, star_prod_pref, B_int, D_scale, F_cur_set, p
            )
            require(len(U_A) == 0, f"Part3 step {idx}: branch_a_infeasible is actually feasible")
            F_cur_set.add(p)
            F_cur_list.append(p)
            M_cur, C_cur, pp_cur = crt_P0.extend_state(M_cur, C_cur, pp_cur, [p])
        elif etype == "branch_a":
            p = req_int(req_key(entry, "omit_prime", f"part3[{idx}]"), f"part3[{idx}].omit_prime", min_val=3)
            require(p in c0_set and p not in F_cur_set, f"Part3 step {idx}: invalid omit_prime {p}")
            F_ext_A, U_A = compute_dp2_u_bounds(
                c0, lv0, cap_int, L0_pref, L0_prod_pref, star_prod_pref, B_int, D_scale, F_cur_set, p
            )
            F_extra = req_int_list(entry.get("F_extra_used", []), f"part3[{idx}].F_extra_used", min_val=3)
            require(len(set(F_extra)) == len(F_extra), f"Part3 step {idx}: duplicate in F_extra_used")
            for q in F_extra:
                require(q in F_ext_A and q not in F_cur_set, f"Part3 step {idx}: unforced prime {q}")
            M_A, C_A, _ = crt_P0.extend_state(M_cur, C_cur, pp_cur, F_extra)

            buckets = req_list(req_key(entry, "buckets", f"part3[{idx}]"), f"part3[{idx}].buckets")
            max_k = len(U_A) - 1
            expected_k = 0
            for b_idx, bk_obj in enumerate(buckets):
                bk = req_dict(bk_obj, f"part3[{idx}].buckets[{b_idx}]")
                k_lo = req_int(req_key(bk, "k_lo", f"part3[{idx}][{b_idx}]"), f"part3[{idx}][{b_idx}].k_lo", min_val=0)
                k_hi = req_int(req_key(bk, "k_hi", f"part3[{idx}][{b_idx}]"), f"part3[{idx}][{b_idx}].k_hi", min_val=0)
                require(k_lo <= k_hi, f"Part3 step {idx} bucket {b_idx}: invalid k range")
                while expected_k < len(U_A) and U_A[expected_k] == 0:
                    expected_k += 1
                require(expected_k < len(U_A), f"Part3 step {idx} bucket {b_idx}: superfluous trailing bucket")
                require(k_lo == expected_k, f"Part3 step {idx} bucket {b_idx}: gap at k={expected_k}")
                U_box = max(U_A[k_lo : min(k_hi + 1, len(U_A))])
                R_box = P0**k_hi
                u_w = decode_signed_hex(req_key(bk, "u_hex", f"part3[{idx}][{b_idx}]"), f"Part3[{idx}][{b_idx}].u")
                v_w = decode_signed_hex(req_key(bk, "v_hex", f"part3[{idx}][{b_idx}]"), f"Part3[{idx}][{b_idx}].v")
                verify_lattice_witness(M_A, C_A, U_box, R_box, u_w, v_w, f"Part3[{idx}][{b_idx}]")
                verified_p3_pairs += 1
                expected_k = k_hi + 1
            require(expected_k > max_k, f"Part3 step {idx}: buckets did not cover max_k={max_k}")
            F_cur_set.add(p)
            F_cur_list.append(p)
            M_cur, C_cur, pp_cur = crt_P0.extend_state(M_cur, C_cur, pp_cur, [p])
        elif etype == "branch_b":
            require(idx == len(cascade) - 1, "Part3: branch_b must be final cascade entry")
            _, U_B = compute_dp2_u_bounds(
                c0, lv0, cap_int, L0_pref, L0_prod_pref, star_prod_pref, B_int, D_scale, F_cur_set, None
            )
            buckets = req_list(req_key(entry, "buckets", "part3.branch_b"), "part3.branch_b.buckets")
            max_k = len(U_B) - 1
            expected_k = 0
            for b_idx, bk_obj in enumerate(buckets):
                bk = req_dict(bk_obj, f"part3[B].buckets[{b_idx}]")
                k_lo = req_int(req_key(bk, "k_lo", f"part3[B][{b_idx}]"), f"part3[B][{b_idx}].k_lo", min_val=0)
                k_hi = req_int(req_key(bk, "k_hi", f"part3[B][{b_idx}]"), f"part3[B][{b_idx}].k_hi", min_val=0)
                require(k_lo <= k_hi, f"Part3 branch_b bucket {b_idx}: invalid k range")
                while expected_k < len(U_B) and U_B[expected_k] == 0:
                    expected_k += 1
                require(expected_k < len(U_B), f"Part3 branch_b bucket {b_idx}: superfluous trailing bucket")
                require(k_lo == expected_k, f"Part3 branch_b bucket {b_idx}: gap at k={expected_k}")
                U_box = max(U_B[k_lo : min(k_hi + 1, len(U_B))])
                R_box = P0**k_hi
                u_w = decode_signed_hex(req_key(bk, "u_hex", f"part3[B][{b_idx}]"), f"Part3[B][{b_idx}].u")
                v_w = decode_signed_hex(req_key(bk, "v_hex", f"part3[B][{b_idx}]"), f"Part3[B][{b_idx}].v")
                verify_lattice_witness(M_cur, C_cur, U_box, R_box, u_w, v_w, f"Part3[B][{b_idx}]")
                verified_p3_pairs += 1
                expected_k = k_hi + 1
            require(expected_k > max_k, f"Part3 branch_b: buckets did not cover max_k={max_k}")
            closed_p3 = True
        else:
            fail(f"Part3 step {idx}: unknown entry type {etype!r}")

    require(closed_p3, "Part3 cascade did not terminate with branch_b")
    require(
        verified_p3_pairs == req_int(req_key(p3, "total_UR_pairs", "part3"), "part3.total_UR_pairs", min_val=1),
        "Part3 pair count mismatch",
    )

    # -----------------------------------------------------------------------
    # Verify Part 4: Tier 2 Digit Bound (>= 40,922 digits) & Dichotomies
    # -----------------------------------------------------------------------
    p4 = req_dict(req_key(cert_obj, "part4_tier2_digit_bound", "root"), "part4_tier2_digit_bound")
    S4 = req_int(req_key(p4, "tail_scale", "part4"), "part4.tail_scale", min_val=10**12)

    crt_L = ExactIncrementalCRT(P_L, spf)
    delta_L = {c: cap_L[c] + Fraction(len(leaves_L[c]) - 1, B) for c in centers_L}
    gap_hi = ceil_frac_scaled(gap_L, S4)
    cap_lo = {c: floor_frac_scaled(cap_L[c], S4) for c in centers_L}
    inv_lo = {c: S4 // c for c in centers_L}

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
        require(len(ct) >= count, f"insufficient tail primes > B ({len(ct)} < {count})")
        ts = [0]
        for q in ct:
            ts.append(ts[-1] + ((S4 + q - 1) // q))
        return ts

    def compute_m0_and_d_max_scaled(dm: int, T_hi: list[int]) -> tuple[int, int]:
        m0_max = 0
        for m0 in range(M0_LIM):
            require(m0 + dm < len(T_hi), "tail sum table too short")
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
            require(Fraction(H_j, 1) < val and val <= Fraction(H_j + 1, 1), "H_j rounding error")
            H_vals.append(H_j)
        return prod_tree(H_vals)

    # --- 4a: Delta_m = 3 (omega = 8,138) ---
    dm3 = p4["dm3"]
    F3 = sorted(N_leaf2 + [c for c in centers_L if delta_L[c] >= gap_L + Fraction(3, B)])
    T3_hi = build_tail_hi(set(F3), 250)
    m0_max_3, d_max_3 = compute_m0_and_d_max_scaled(3, T3_hi)
    require(m0_max_3 == dm3["m0_max"] and d_max_3 == dm3["d_max"], "dm3 m0_max/d_max mismatch")
    M3, C3, _ = crt_L.build_state(F3)
    U3 = L_prod_top[d_max_3]
    Q3 = ((10 ** (dm3["digit_target"] - 1) - 1) + P_L - 1) // P_L
    verify_lattice_witness(
        M3, C3, U3, Q3 * U3,
        decode_signed_hex(dm3["digit_witness"]["u_hex"], "dm3.digit.u"),
        decode_signed_hex(dm3["digit_witness"]["v_hex"], "dm3.digit.v"),
        "Part4 dm3 digit",
    )
    R3_p = per_rank_H_prod(3, d_max_3) * ((10 ** dm3["P_exp_target"]) ** 3)
    verify_lattice_witness(
        M3, C3, U3, R3_p,
        decode_signed_hex(dm3["P_witness"]["u_hex"], "dm3.P.u"),
        decode_signed_hex(dm3["P_witness"]["v_hex"], "dm3.P.v"),
        "Part4 dm3 P(n)",
    )

    # --- 4b: Delta_m = 11 (omega = 8,146) ---
    dm11 = p4["dm11"]
    F11 = sorted(N_leaf2 + [c for c in centers_L if delta_L[c] >= gap_L + Fraction(11, B)])
    T11_hi = build_tail_hi(set(F11), 360)
    m0_max_11, d_max_11 = compute_m0_and_d_max_scaled(11, T11_hi)
    require(m0_max_11 == dm11["m0_max"] and d_max_11 == dm11["d_max"], "dm11 m0_max/d_max mismatch")
    M11, C11, _ = crt_L.build_state(F11)
    U11 = L_prod_top[d_max_11]
    Q11 = ((10 ** (dm11["digit_target"] - 1) - 1) + P_L - 1) // P_L
    verify_lattice_witness(
        M11, C11, U11, Q11 * U11,
        decode_signed_hex(dm11["digit_witness"]["u_hex"], "dm11.digit.u"),
        decode_signed_hex(dm11["digit_witness"]["v_hex"], "dm11.digit.v"),
        "Part4 dm11 digit",
    )
    R11_p = per_rank_H_prod(11, d_max_11) * ((10 ** dm11["P_exp_target"]) ** 11)
    verify_lattice_witness(
        M11, C11, U11, R11_p,
        decode_signed_hex(dm11["P_witness"]["u_hex"], "dm11.P.u"),
        decode_signed_hex(dm11["P_witness"]["v_hex"], "dm11.P.v"),
        "Part4 dm11 P(n)",
    )

    # --- 4c: Delta_m = 19 (omega = 8,154) ---
    dm19 = p4["dm19"]
    F19_0 = set(N_leaf2) | {c for c in centers_L if delta_L[c] >= gap_L + Fraction(19, B)}
    T19_0 = build_tail_hi(F19_0, 450)
    m0_max_19, _ = compute_m0_and_d_max_scaled(19, T19_0)
    require(m0_max_19 == dm19["m0_max"], "dm19 m0_max mismatch")
    Q19 = ((10 ** (dm19["digit_target"] - 1) - 1) + P_L - 1) // P_L

    expected_m0 = 0
    for iv_idx, iv in enumerate(dm19["intervals"]):
        m0_lo, m0_hi = iv["m0_lo"], iv["m0_hi"]
        require(m0_lo == expected_m0 and m0_lo <= m0_hi, f"dm19 interval {iv_idx} gap/order error")
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
        U_iv = L_prod_top[m0_hi + m1_max]
        M_iv, C_iv, _ = crt_L.build_state(sorted(F_iv))
        verify_lattice_witness(
            M_iv, C_iv, U_iv, Q19 * U_iv,
            decode_signed_hex(iv["u_hex"], f"dm19[{iv_idx}].u"),
            decode_signed_hex(iv["v_hex"], f"dm19[{iv_idx}].v"),
            f"Part4 dm19[{iv_idx}]",
        )
        expected_m0 = m0_hi + 1
    require(expected_m0 > m0_max_19, "dm19 intervals did not cover [0, m0_max_19]")

    # --- 4d: Delta_m = 27 (omega = 8,162) ---
    dm27 = p4["dm27"]
    F27_0 = set(N_leaf2) | {c for c in centers_L if delta_L[c] >= gap_L + Fraction(27, B)}
    T27_0 = build_tail_hi(F27_0, 520)
    m0_max_27, _ = compute_m0_and_d_max_scaled(27, T27_0)
    require(m0_max_27 == dm27["m0_max"], "dm27 m0_max mismatch")
    Q27 = ((10 ** (dm27["digit_target"] - 1) - 1) + P_L - 1) // P_L

    expected_m0 = 0
    verified_dm27_pairs = 0
    centers_L_set = set(centers_L)
    for iv_idx, iv in enumerate(dm27["intervals"]):
        m0_lo, m0_hi = iv["m0_lo"], iv["m0_hi"]
        require(m0_lo == expected_m0 and m0_lo <= m0_hi, f"dm27 interval {iv_idx} gap/order error")
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
            require(iv.get("status") == "infeasible", f"dm27[{iv_idx}] expected infeasible status")
            expected_m0 = m0_hi + 1
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

        F_cur_27 = sorted(F_base)
        F_cur_27_set = set(F_cur_27)
        M_27, C_27, pp_27 = crt_L.build_state(F_cur_27)
        iv_cascade = iv["cascade"]
        require(isinstance(iv_cascade, list) and len(iv_cascade) >= 1, f"dm27[{iv_idx}] empty cascade")
        closed_iv = False
        for s_idx, step in enumerate(iv_cascade):
            stype = step.get("type")
            if stype in ("branch_a", "branch_a_infeasible"):
                p = step["omit_prime"]
                require(p in centers_L_set and p not in F_cur_27_set, f"dm27[{iv_idx}][{s_idx}] invalid p={p}")
                if m0_hi_eff >= 1:
                    require(p < L[-m0_hi_eff], f"dm27[{iv_idx}][{s_idx}] p={p} overlaps top m0 primes")
                rem_A0 = rhs_m0_iv - inv_lo[p] if m0_hi_eff >= 1 else -1
                rem_A1 = (rem_iv - cap_lo[p]) if leaves_L[p] else -1
                rem_A = max(rem_A0, rem_A1)
                m0_hi_A = m0_lo - 1
                if rem_A > 0:
                    for mt in range(m0_lo, m0_hi_eff + 1):
                        ok0 = (mt >= 1) and (gap_hi + T_iv[mt + 27] - L_sum_lo[mt - 1] - inv_lo[p] > 0)
                        ok1 = bool(leaves_L[p]) and (gap_hi + T_iv[mt + 27] - L_sum_lo[mt] - cap_lo[p] > 0)
                        if ok0 or ok1:
                            m0_hi_A = mt
                if stype == "branch_a_infeasible":
                    require(rem_A <= 0 or m0_hi_A < m0_lo, f"dm27[{iv_idx}][{s_idx}] branch_a is feasible")
                else:
                    require(rem_A > 0 and m0_hi_A >= m0_lo, f"dm27[{iv_idx}][{s_idx}] branch_a infeasible")
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
                    F_ext_A = set(F_cur_27_set)
                    for c in centers_L:
                        if c == p or c in F_cur_27_set or c >= top_guard:
                            continue
                        if inv_lo[c] >= rhs_other_m0 and ((not leaves_L[c]) or (cap_lo[c] >= rem_A)):
                            F_ext_A.add(c)
                    F_extra = step.get("F_extra_used", [])
                    require(isinstance(F_extra, list), f"dm27[{iv_idx}][{s_idx}] F_extra_used not list")
                    require(len(set(F_extra)) == len(F_extra), f"dm27[{iv_idx}][{s_idx}] dup F_extra_used")
                    for q in F_extra:
                        require(q in F_ext_A and q not in F_cur_27_set, f"dm27[{iv_idx}][{s_idx}] unforced {q}")
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
                    M_A, C_A, _ = crt_L.extend_state(M_27, C_27, pp_27, F_extra)
                    verify_lattice_witness(
                        M_A, C_A, U_A, Q27 * U_A,
                        decode_signed_hex(step["u_hex"], f"dm27[{iv_idx}][{s_idx}].u"),
                        decode_signed_hex(step["v_hex"], f"dm27[{iv_idx}][{s_idx}].v"),
                        f"Part4 dm27[{iv_idx}][{s_idx}]",
                    )
                    verified_dm27_pairs += 1
                F_cur_27_set.add(p)
                F_cur_27.append(p)
                M_27, C_27, pp_27 = crt_L.extend_state(M_27, C_27, pp_27, [p])
            elif stype == "branch_b":
                require(s_idx == len(iv_cascade) - 1, f"dm27[{iv_idx}] branch_b not final")
                verify_lattice_witness(
                    M_27, C_27, U_B, R_B,
                    decode_signed_hex(step["u_hex"], f"dm27[{iv_idx}][B].u"),
                    decode_signed_hex(step["v_hex"], f"dm27[{iv_idx}][B].v"),
                    f"Part4 dm27[{iv_idx}][B]",
                )
                verified_dm27_pairs += 1
                closed_iv = True
            else:
                fail(f"dm27[{iv_idx}][{s_idx}] unknown type {stype!r}")
        require(closed_iv, f"dm27[{iv_idx}] did not close with branch_b")
        expected_m0 = m0_hi + 1
    require(expected_m0 > m0_max_27, "dm27 intervals did not cover [0, m0_max_27]")
    require(verified_dm27_pairs == dm27["total_UR_pairs"], "dm27 pair count mismatch")

    # --- 4e: Delta_m = 35 and Delta_m >= 43 (exact zero-float Lagrangian) ---
    P_top = P_L // (10**40_729)
    require(P_L >= P_top * (10**40_729), "P_top check failed")

    def verify_lagrangian_case(A_int: int, dm: int, excluded: set[int], target_digits: int, label: str) -> None:
        require(isinstance(A_int, int) and 0 < A_int < B, f"{label}: invalid A_int={A_int}")
        for c in centers_L:
            if c in excluded:
                continue
            T = leaves_L[c]
            if not T:
                continue
            prod_T = prod_tree(T)
            if c * (B ** (len(T) - 1)) <= prod_T:
                continue
            ad = A_int * delta_L[c]
            ok = False
            for v in (1, 2, 5, 10, 20, 50, 100, 200, 500, 1_000):
                u = (ad.numerator * v) // ad.denominator
                exp_B = v * (len(T) - 1) - u
                if exp_B >= 0:
                    cond = (c**v) * (B**exp_B) <= (prod_T**v)
                else:
                    cond = (c**v) <= (B ** (-exp_B)) * (prod_T**v)
                if cond:
                    ok = True
                    break
            require(ok, f"{label}: star dominance check failed at c={c}")
        r = Fraction(dm, 1) - A_int * (gap_L + Fraction(dm, B))
        require(r > 0, f"{label}: non-positive r")
        a1000 = (r.numerator * 1_000) // r.denominator
        require(Fraction(a1000, 1_000) <= r, f"{label}: a1000 rounding check failed")
        lhs = (P_top**1_000) * (B**a1000)
        rhs = 10 ** (1_000 * (target_digits - 1 - 40_729))
        require(lhs >= rhs, f"{label}: exact integer digit inequality failed for {target_digits}")

    dm35 = p4["dm35"]
    F35 = set(N_leaf2) | {c for c in centers_L if delta_L[c] >= gap_L + Fraction(35, B)}
    verify_lagrangian_case(dm35["A_int"], 35, F35, dm35["digit_target"], "Part4 dm35")

    dm43 = p4["dm43_plus"]
    verify_lagrangian_case(dm43["A_int"], 43, set(N_leaf2), dm43["digit_target"], "Part4 dm43+")

    # Final unconditional consistency check across all cases!
    min_digits_all = min(
        min_non_leaf2_digits,
        p2["a_ge_2_min_digits"],
        dm3["digit_target"],
        dm11["digit_target"],
        dm19["digit_target"],
        dm27["digit_target"],
        dm35["digit_target"],
        dm43["digit_target"],
    )
    require(min_digits_all == p4["unconditional_min_digits"] == 40_922, "final digit bound mismatch")
    require(p4["unconditional_min_omega"] == 8_138, "final omega bound mismatch")
    require(p4["unconditional_min_P"] == 326_057, "final P(n) bound mismatch")

    elapsed_ms = (time.monotonic_ns() - t0_ns) // 1_000_000
    return {
        "status": "VERIFIED",
        "zero_float_arithmetic": True,
        "elapsed_ms": elapsed_ms,
        "python_version": platform.python_version(),
        "unconditional_bounds": {
            "omega_at_least": 8_138,
            "largest_prime_at_least": 326_057,
            "decimal_digits_at_least": 40_922,
        },
        "extremal_normal_set": {
            "L_count": 8_135,
            "L_max": 321_053,
            "P_L_digits": 40_733,
            "P_L_sha256_binary": P_L_sha,
            "P_8138_digits": 40_750,
            "P_8138_sha256_binary": P_8138_sha,
            "outside_leaf2_exact_min_max": 352_757,
            "M_L_digits": 54_909,
        },
        "a_ge_2_bounds": {
            "omega_at_least": 329_188,
            "largest_prime_at_least": 1_284_211,
            "decimal_digits_at_least": 1_808_611,
        },
        "dichotomies": {
            "omega_8138": {"digits_at_least": dm3["digit_target"], "P_gt_10_pow": dm3["P_exp_target"]},
            "omega_8146": {"digits_at_least": dm11["digit_target"], "P_gt_10_pow": dm11["P_exp_target"]},
            "omega_8154": {"digits_at_least": dm19["digit_target"]},
        },
        "verified_UR_pairs": {
            "part3_P_ge_326057": verified_p3_pairs,
            "part4_dm3": 2,
            "part4_dm11": 2,
            "part4_dm19": len(dm19["intervals"]),
            "part4_dm27": verified_dm27_pairs,
            "total": verified_p3_pairs + 4 + len(dm19["intervals"]) + verified_dm27_pairs,
        },
    }


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Standalone zero-float fail-closed verifier for the Agoh--Giuga certificate."
    )
    default_cert = (
        Path(__file__).resolve().parents[1]
        / "certificates"
        / "agoh_giuga_tier2_certificate.json"
    )
    parser.add_argument("certificate", nargs="?", type=Path, default=default_cert)
    args = parser.parse_args()

    require(args.certificate.is_file(), f"certificate file not found: {args.certificate}")
    raw = args.certificate.read_text(encoding="utf-8")
    cert = json.loads(raw)
    summary = verify_certificate(cert)
    summary["certificate_path"] = str(args.certificate)
    summary["certificate_sha256"] = file_sha256(args.certificate)
    summary["verifier_sha256"] = file_sha256(Path(__file__).resolve())
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
