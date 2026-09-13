#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <string>
#include <vector>

// Discovery/certification scanner for the complete i=3 stratum.
// All tests are integer tests.  For an odd prime p, Lucas says that
// p does not divide C(n,j) iff every base-p digit of j is at most the
// corresponding digit of n.

namespace {

using u32 = std::uint32_t;
using u64 = std::uint64_t;

std::vector<u32> smallest_prime_factor(u32 limit) {
    std::vector<u32> spf(static_cast<std::size_t>(limit) + 1, 0);
    std::vector<u32> primes;
    primes.reserve(limit > 10 ? static_cast<std::size_t>(limit / 10) : 4);
    for (u32 x = 2; x <= limit; ++x) {
        if (spf[x] == 0) {
            spf[x] = x;
            primes.push_back(x);
        }
        for (u32 p : primes) {
            const u64 y = static_cast<u64>(p) * x;
            if (y > limit || p > spf[x]) break;
            spf[static_cast<u32>(y)] = p;
        }
    }
    return spf;
}

std::vector<u32> odd_prime_divisors_gt3(u32 value,
                                         const std::vector<u32>& spf) {
    std::vector<u32> out;
    while (value > 1) {
        const u32 p = spf[value];
        if (p > 3) out.push_back(p);
        do {
            value /= p;
        } while (value > 1 && value % p == 0);
    }
    return out;
}

bool lucas_nondivisible(u32 n, u32 k, u32 p) {
    while (n > 0 || k > 0) {
        if (k % p > n % p) return false;
        n /= p;
        k /= p;
    }
    return true;
}

u64 subdigit_count_capped(u32 n, u32 p, u64 cap) {
    u64 count = 1;
    do {
        const u64 factor = static_cast<u64>(n % p) + 1;
        if (factor != 0 && count > cap / factor) return cap;
        count *= factor;
        if (count >= cap) return cap;
        n /= p;
    } while (n > 0);
    return count;
}

void enumerate_subdigits_rec(const std::vector<u32>& digits, u32 p,
                             std::size_t pos, u64 place, u64 value,
                             u32 lower, u32 upper,
                             std::vector<u32>& out) {
    if (value > upper) return;
    if (pos == digits.size()) {
        if (value >= lower) out.push_back(static_cast<u32>(value));
        return;
    }
    for (u32 d = 0; d <= digits[pos]; ++d) {
        const u64 next = value + static_cast<u64>(d) * place;
        if (next > upper) break;
        enumerate_subdigits_rec(digits, p, pos + 1,
                                place * static_cast<u64>(p), next,
                                lower, upper, out);
    }
}

std::vector<u32> lucas_nondisivisible_indices(u32 n, u32 p,
                                              u32 lower, u32 upper) {
    std::vector<u32> digits;
    for (u32 x = n; x > 0; x /= p) digits.push_back(x % p);
    std::vector<u32> out;
    const u64 reserve_hint = subdigit_count_capped(n, p, 1'000'000);
    out.reserve(static_cast<std::size_t>(std::min<u64>(reserve_hint, 1'000'000)));
    enumerate_subdigits_rec(digits, p, 0, 1, 0, lower, upper, out);
    return out;
}

void append_unique(std::vector<u32>& values, const std::vector<u32>& add) {
    for (u32 p : add) {
        if (std::find(values.begin(), values.end(), p) == values.end()) {
            values.push_back(p);
        }
    }
}

struct Result {
    bool found = false;
    u32 n = 0;
    u32 j = 0;
    std::vector<u32> odd_primes;
    u64 candidate_indices = 0;
};

Result scan(u32 n_min, u32 n_max) {
    const auto spf = smallest_prime_factor(n_max);
    std::vector<u32> ring[3];
    u64 candidate_indices = 0;

    for (u32 x = 1; x <= n_max; ++x) {
        ring[x % 3] = x >= 2 ? odd_prime_divisors_gt3(x, spf)
                             : std::vector<u32>{};
        if (x < n_min || x < 8) continue;

        const u32 n = x;
        std::vector<u32> factors;
        append_unique(factors, ring[n % 3]);
        append_unique(factors, ring[(n - 1) % 3]);
        append_unique(factors, ring[(n - 2) % 3]);

        // The numerator n(n-1)(n-2) contains exactly one multiple of 3.
        // After division by 3!, the prime 3 remains precisely when that
        // multiple is divisible by 9.
        if (n % 9 <= 2) factors.push_back(3);
        std::sort(factors.begin(), factors.end());
        factors.erase(std::unique(factors.begin(), factors.end()), factors.end());

        if (factors.empty()) {
            std::cerr << "internal error: C(" << n << ",3) has no odd prime\n";
            std::exit(3);
        }

        u32 anchor = factors.front();
        u64 best_count = std::numeric_limits<u64>::max();
        for (u32 p : factors) {
            const u64 count = subdigit_count_capped(n, p, best_count);
            if (count < best_count || (count == best_count && p > anchor)) {
                best_count = count;
                anchor = p;
            }
        }

        const auto candidates =
            lucas_nondisivisible_indices(n, anchor, 4, n / 2);
        candidate_indices += candidates.size();
        for (u32 j : candidates) {
            bool avoids_every_odd_factor = true;
            for (u32 p : factors) {
                if (!lucas_nondivisible(n, j, p)) {
                    avoids_every_odd_factor = false;
                    break;
                }
            }
            if (avoids_every_odd_factor) {
                return {true, n, j, factors, candidate_indices};
            }
        }
    }
    return {false, 0, 0, {}, candidate_indices};
}

u32 parse_u32(const char* text) {
    const unsigned long long value = std::stoull(text);
    if (value > std::numeric_limits<u32>::max()) {
        throw std::out_of_range("value exceeds uint32");
    }
    return static_cast<u32>(value);
}

}  // namespace

int main(int argc, char** argv) {
    if (argc != 3) {
        std::cerr << "usage: scan_i3 N_MIN N_MAX\n";
        return 2;
    }
    const u32 n_min = parse_u32(argv[1]);
    const u32 n_max = parse_u32(argv[2]);
    if (n_min > n_max || n_max < 8) {
        std::cerr << "invalid range\n";
        return 2;
    }

    const auto started = std::chrono::steady_clock::now();
    const Result result = scan(n_min, n_max);
    const auto elapsed_ms = std::chrono::duration_cast<std::chrono::milliseconds>(
                                std::chrono::steady_clock::now() - started)
                                .count();

    std::cout << "{\n"
              << "  \"schema\": \"erdos699-i3-scan-v1\",\n"
              << "  \"n_min\": " << n_min << ",\n"
              << "  \"n_max\": " << n_max << ",\n"
              << "  \"i\": 3,\n"
              << "  \"candidate_indices_tested\": "
              << result.candidate_indices << ",\n"
              << "  \"weak_counterexample\": ";
    if (!result.found) {
        std::cout << "null,\n";
    } else {
        std::cout << "{\"n\": " << result.n << ", \"i\": 3, \"j\": "
                  << result.j << ", \"odd_prime_divisors_of_binom_n_3\": [";
        for (std::size_t k = 0; k < result.odd_primes.size(); ++k) {
            if (k) std::cout << ", ";
            std::cout << result.odd_primes[k];
        }
        std::cout << "]},\n";
    }
    std::cout << "  \"elapsed_ms_diagnostic_only\": " << elapsed_ms << "\n}\n";
    return result.found ? 1 : 0;
}
