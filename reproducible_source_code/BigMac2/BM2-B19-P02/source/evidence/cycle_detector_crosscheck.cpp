#define main geng_search_program_main
#include "geng_excess2_search.cpp"
#undef main

#include <cstdint>
#include <iostream>
#include <random>

namespace {

// Deliberately separate reference implementation: adjacency is queried by
// scanning vertices, and every oriented simple path is explored.  It uses none
// of the production detector's minimum-start or orientation pruning.
bool reference_has_cycle(const Adj& a, int n, int length) {
    std::array<int, FULL_N> path{};
    std::array<bool, FULL_N> used{};
    for (int root = 0; root < n; ++root) {
        used.fill(false);
        used[root] = true;
        path[0] = root;
        auto search = [&](auto&& self, int depth) -> bool {
            const int last = path[depth - 1];
            if (depth == length) return ((a[last] >> root) & 1U) != 0;
            for (int next = 0; next < n; ++next) {
                if (!used[next] && ((a[last] >> next) & 1U)) {
                    used[next] = true;
                    path[depth] = next;
                    if (self(self, depth + 1)) return true;
                    used[next] = false;
                }
            }
            return false;
        };
        if (search(search, 1)) return true;
    }
    return false;
}

void set_mask_graph(Adj& a, int n, uint64_t mask) {
    a.fill(0);
    int bit = 0;
    for (int u = 0; u < n; ++u)
        for (int v = u + 1; v < n; ++v, ++bit)
            if ((mask >> bit) & 1ULL) add_edge(a, u, v);
}

void ring(Adj& a, int n) {
    a.fill(0);
    for (int v = 0; v < n; ++v) add_edge(a, v, (v + 1) % n);
}

void require_equal(const Adj& a, int n, int length, uint64_t case_id) {
    const bool got = has_cycle(a, n, length);
    const bool want = reference_has_cycle(a, n, length);
    if (got != want) {
        std::cerr << "MISMATCH n=" << n << " length=" << length
                  << " case=" << case_id << " production=" << got
                  << " reference=" << want << '\n';
        std::exit(1);
    }
}

}  // namespace

int main() {
    uint64_t checked = 0;
    Adj a{};

    // Exhaustive truth-table comparison for every graph on six vertices.
    for (uint64_t mask = 0; mask < (1ULL << 15); ++mask) {
        set_mask_graph(a, 6, mask);
        require_equal(a, 6, 4, mask);
        ++checked;
    }

    // Exact-cycle boundary fixtures, including lengths close to but unequal
    // to the target length.
    for (int n = 3; n <= 24; ++n) {
        ring(a, n);
        for (int length : {4, 8, 16}) {
            require_equal(a, n, length, static_cast<uint64_t>(n * 100 + length));
            ++checked;
        }
    }

    // Fixed-seed sparse and medium-density cases.  Keeping n <= 18 makes the
    // unpruned reference search practical even when a requested cycle is absent.
    std::mt19937_64 rng(0x5a17c0de9b31ULL);
    for (int trial = 0; trial < 12000; ++trial) {
        const int n = 8 + static_cast<int>(rng() % 11);
        const int threshold = 40 + static_cast<int>(rng() % 180); // /1000
        a.fill(0);
        for (int u = 0; u < n; ++u)
            for (int v = u + 1; v < n; ++v)
                if (static_cast<int>(rng() % 1000) < threshold) add_edge(a, u, v);
        require_equal(a, n, 4, static_cast<uint64_t>(trial));
        require_equal(a, n, 8, static_cast<uint64_t>(trial));
        if (n >= 16 && trial % 8 == 0)
            require_equal(a, n, 16, static_cast<uint64_t>(trial));
        checked += 2 + (n >= 16 && trial % 8 == 0 ? 1 : 0);
    }

    std::cout << "PASS compared=" << checked
              << " exhaustive_n6_C4=32768 random_seed=0x5a17c0de9b31" << '\n';
    return 0;
}
