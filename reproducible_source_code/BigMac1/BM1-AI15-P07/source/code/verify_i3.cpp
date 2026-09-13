#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <limits>
#include <regex>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

// Independent verifier for scan_i3 output.  It uses a classical Eratosthenes
// SPF table, refactors all three numerator terms for each n (no rolling cache),
// chooses the largest odd factor as its anchor, and evaluates the remaining
// primes with Legendre valuations rather than Lucas's digit predicate.

namespace {

using u32 = std::uint32_t;
using u64 = std::uint64_t;

std::string read_all(const std::string& path) {
    std::ifstream in(path);
    if (!in) throw std::runtime_error("cannot open input");
    std::ostringstream buffer;
    buffer << in.rdbuf();
    return buffer.str();
}

struct ParsedInput {
    u32 n_min;
    u32 n_max;
};

ParsedInput parse_strict_certificate(const std::string& text) {
    // Accept exactly the scanner's seven-field null-result object.  Anchoring
    // the whole regex rejects duplicate keys, trailing payloads, non-null
    // witnesses, missing fields, and a changed schema or i-stratum.
    const std::regex pattern(
        R"(^\s*\{\s*"schema"\s*:\s*"erdos699-i3-scan-v1"\s*,\s*)"
        R"("n_min"\s*:\s*([0-9]+)\s*,\s*)"
        R"("n_max"\s*:\s*([0-9]+)\s*,\s*)"
        R"("i"\s*:\s*3\s*,\s*)"
        R"("candidate_indices_tested"\s*:\s*[0-9]+\s*,\s*)"
        R"("weak_counterexample"\s*:\s*null\s*,\s*)"
        R"("elapsed_ms_diagnostic_only"\s*:\s*[0-9]+\s*\}\s*$)");
    std::smatch match;
    if (!std::regex_match(text, match, pattern)) {
        throw std::runtime_error("malformed, incomplete, duplicated, or non-null certificate");
    }
    const unsigned long long lo = std::stoull(match[1].str());
    const unsigned long long hi = std::stoull(match[2].str());
    if (lo > std::numeric_limits<u32>::max() ||
        hi > std::numeric_limits<u32>::max()) {
        throw std::runtime_error("range integer out of uint32 bounds");
    }
    return {static_cast<u32>(lo), static_cast<u32>(hi)};
}

std::vector<u32> eratosthenes_spf(u32 limit) {
    std::vector<u32> spf(static_cast<std::size_t>(limit) + 1, 0);
    for (u32 x = 2; x <= limit; ++x) {
        if (spf[x] != 0) continue;
        spf[x] = x;
        if (static_cast<u64>(x) * x > limit) continue;
        for (u64 y = static_cast<u64>(x) * x; y <= limit; y += x) {
            if (spf[static_cast<u32>(y)] == 0) spf[static_cast<u32>(y)] = x;
        }
    }
    return spf;
}

void factor_distinct_odd_part(u32 value, const std::vector<u32>& spf,
                              std::set<u32>& factors) {
    while (value > 1) {
        u32 p = spf[value];
        if (p == 0) p = value;
        if (p > 3) factors.insert(p);
        do {
            value /= p;
        } while (value > 1 && value % p == 0);
    }
}

u32 factorial_valuation(u32 value, u32 p) {
    u32 sum = 0;
    while (value > 0) {
        value /= p;
        sum += value;
    }
    return sum;
}

bool prime_divides_binomial(u32 n, u32 k, u32 p) {
    return factorial_valuation(n, p) >
           factorial_valuation(k, p) + factorial_valuation(n - k, p);
}

std::vector<u32> digits_base(u32 n, u32 p) {
    std::vector<u32> digits;
    do {
        digits.push_back(n % p);
        n /= p;
    } while (n > 0);
    return digits;
}

std::vector<u32> anchor_avoiders(u32 n, u32 p) {
    const auto digits = digits_base(n, p);
    std::vector<u32> values{0};
    u64 place = 1;
    for (u32 bound : digits) {
        std::vector<u32> next;
        const u64 capacity = static_cast<u64>(values.size()) * (bound + 1);
        if (capacity > std::numeric_limits<std::size_t>::max()) {
            throw std::runtime_error("candidate capacity overflow");
        }
        next.reserve(static_cast<std::size_t>(capacity));
        for (u32 old : values) {
            for (u32 d = 0; d <= bound; ++d) {
                const u64 value = static_cast<u64>(old) + place * d;
                if (value <= n / 2) next.push_back(static_cast<u32>(value));
            }
        }
        values.swap(next);
        place *= p;
    }
    values.erase(std::remove_if(values.begin(), values.end(),
                                [](u32 j) { return j < 4; }),
                 values.end());
    return values;
}

bool verify_range(u32 n_min, u32 n_max, u64& candidates_checked) {
    const auto spf = eratosthenes_spf(n_max);
    for (u32 n = std::max<u32>(n_min, 8); n <= n_max; ++n) {
        std::set<u32> factor_set;
        factor_distinct_odd_part(n, spf, factor_set);
        factor_distinct_odd_part(n - 1, spf, factor_set);
        factor_distinct_odd_part(n - 2, spf, factor_set);
        if (n % 9 <= 2) factor_set.insert(3);
        if (factor_set.empty()) throw std::runtime_error("empty odd factor set");

        const u32 anchor = *factor_set.rbegin();
        const auto candidates = anchor_avoiders(n, anchor);
        candidates_checked += candidates.size();
        for (u32 j : candidates) {
            bool common_odd_prime_exists = false;
            for (u32 p : factor_set) {
                if (prime_divides_binomial(n, j, p)) {
                    common_odd_prime_exists = true;
                    break;
                }
            }
            if (!common_odd_prime_exists) {
                std::cerr << "counterexample reconstructed: n=" << n
                          << " i=3 j=" << j << "\n";
                return false;
            }
        }
        if (n == n_max) break;  // prevent uint32 wrap at the endpoint
    }
    return true;
}

}  // namespace

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: verify_i3 SCAN_RESULT.json\n";
        return 2;
    }
    try {
        const std::string input = read_all(argv[1]);
        const ParsedInput parsed = parse_strict_certificate(input);
        const u32 n_min = parsed.n_min;
        const u32 n_max = parsed.n_max;
        if (n_min > n_max || n_max < 8) throw std::runtime_error("invalid range");

        const auto start = std::chrono::steady_clock::now();
        u64 checked = 0;
        const bool ok = verify_range(n_min, n_max, checked);
        const auto elapsed_ms = std::chrono::duration_cast<std::chrono::milliseconds>(
                                    std::chrono::steady_clock::now() - start)
                                    .count();
        if (!ok) return 1;
        std::cout << "VERIFIED erdos699 i=3 n=[" << n_min << ',' << n_max
                  << "] anchor_candidates=" << checked
                  << " elapsed_ms_diagnostic_only=" << elapsed_ms << "\n";
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "verification failed closed: " << e.what() << "\n";
        return 2;
    }
}
