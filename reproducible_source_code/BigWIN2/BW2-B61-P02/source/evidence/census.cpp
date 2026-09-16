// Exact exhaustive Hall-universality census for n <= 6.
//
// Input columns: n, canonical graph6, decimal edge mask.  Edge-mask bit k is
// pair (u,v) with v=1..n-1 and u=0..v-1.  For each labelled H, this program
// computes exact Hilton--Johnson Hall feasibility and graphic-list
// colorability.  Per-H Boolean arrays are packed in increasing H-mask order,
// eight little-endian status bits per byte, and written as lowercase hex.

#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <vector>

using std::uint64_t;

struct Rep {
    int n;
    std::string graph6;
    int gmask;
};

static int pair_index(int u, int v) {
    if (u > v) std::swap(u, v);
    return v * (v - 1) / 2 + u;
}

static std::vector<int> adjacency(int n, int edge_mask) {
    std::vector<int> a(n, 0);
    for (int v = 1; v < n; ++v) {
        for (int u = 0; u < v; ++u) {
            if ((edge_mask >> pair_index(u, v)) & 1) {
                a[u] |= 1 << v;
                a[v] |= 1 << u;
            }
        }
    }
    return a;
}

static bool connected_subset(int subset, const std::vector<int>& a) {
    if (!subset) return false;
    int seen = subset & -subset;
    int frontier = seen;
    while (frontier) {
        int vbit = frontier & -frontier;
        frontier ^= vbit;
        int v = __builtin_ctz(static_cast<unsigned>(vbit));
        int add = a[v] & subset & ~seen;
        seen |= add;
        frontier |= add;
    }
    return seen == subset;
}

struct HTables {
    int hn;
    int vn;
    std::vector<std::uint8_t> alpha;  // alpha[h * vn + subset]
    std::vector<uint64_t> connected;  // bit U set iff nonempty H[U] connected
};

static HTables make_h_tables(int n) {
    const int m = n * (n - 1) / 2;
    const int hn = 1 << m;
    const int vn = 1 << n;
    HTables t{hn, vn, std::vector<std::uint8_t>(hn * vn),
              std::vector<uint64_t>(hn, 0)};
    for (int h = 0; h < hn; ++h) {
        auto a = adjacency(n, h);
        std::uint8_t* alpha = t.alpha.data() + h * vn;
        alpha[0] = 0;
        for (int s = 1; s < vn; ++s) {
            const int vbit = s & -s;
            const int v = __builtin_ctz(static_cast<unsigned>(vbit));
            const int without = s ^ vbit;
            alpha[s] = std::max<int>(alpha[without],
                    1 + alpha[without & ~a[v]]);
            if (connected_subset(s, a)) t.connected[h] |= uint64_t(1) << s;
        }
    }
    return t;
}

static void enumerate_assignments_rec(
        int n, int v, const std::vector<int>& lists, std::vector<int>& chosen,
        int conflict_mask, std::vector<uint64_t>& histogram) {
    if (v == n) {
        ++histogram[conflict_mask];
        return;
    }
    int colors = lists[v];
    while (colors) {
        const int cbit = colors & -colors;
        colors ^= cbit;
        const int color = __builtin_ctz(static_cast<unsigned>(cbit));
        int next_conflict = conflict_mask;
        for (int u = 0; u < v; ++u) {
            if (chosen[u] == color) next_conflict |= 1 << pair_index(u, v);
        }
        chosen[v] = color;
        enumerate_assignments_rec(n, v + 1, lists, chosen, next_conflict,
                                  histogram);
    }
}

static std::vector<std::uint8_t> colorable_table(
        int n, const std::vector<int>& lists, std::vector<uint64_t>* hist_out) {
    const int m = n * (n - 1) / 2;
    const int hn = 1 << m;
    std::vector<uint64_t> histogram(hn, 0);
    std::vector<int> chosen(n, -1);
    enumerate_assignments_rec(n, 0, lists, chosen, 0, histogram);
    std::vector<std::uint8_t> result(hn, 0);
    const int all_edges = hn - 1;
    for (int q = 0; q < hn; ++q) {
        if (!histogram[q]) continue;
        const int allowed = all_edges ^ q;
        int h = allowed;
        while (true) {
            result[h] = 1;
            if (h == 0) break;
            h = (h - 1) & allowed;
        }
    }
    if (hist_out) *hist_out = std::move(histogram);
    return result;
}

static std::string pack_hex(const std::vector<std::uint8_t>& bits) {
    static const char* digits = "0123456789abcdef";
    std::string out;
    out.reserve(((bits.size() + 7) / 8) * 2);
    for (std::size_t i = 0; i < bits.size(); i += 8) {
        unsigned byte = 0;
        for (unsigned b = 0; b < 8 && i + b < bits.size(); ++b)
            byte |= unsigned(bits[i + b] != 0) << b;
        out.push_back(digits[byte >> 4]);
        out.push_back(digits[byte & 15]);
    }
    return out;
}

static std::vector<Rep> read_reps(const std::string& path) {
    std::ifstream in(path);
    if (!in) throw std::runtime_error("cannot open representatives file");
    std::string line;
    std::getline(in, line);
    std::vector<Rep> reps;
    while (std::getline(in, line)) {
        std::istringstream ss(line);
        Rep r;
        if (ss >> r.n >> r.graph6 >> r.gmask) reps.push_back(r);
    }
    return reps;
}

int main(int argc, char** argv) {
    if (argc != 3) {
        std::cerr << "usage: census representatives.tsv census_exact.tsv\n";
        return 2;
    }
    const auto reps = read_reps(argv[1]);
    std::ofstream out(argv[2]);
    if (!out) throw std::runtime_error("cannot open output file");
    out << "n\tgraph6\tg_edge_mask\tnum_H\thall_count\tcolorable_count"
           "\tbad_count\twitness_H\thall_bits_hex\tcolorable_bits_hex\n";
    for (int n = 0; n <= 6; ++n) {
        HTables tables = make_h_tables(n);
        int layer_count = 0;
        for (const Rep& r : reps) {
            if (r.n != n) continue;
            ++layer_count;
            auto lists = adjacency(n, r.gmask);
            auto colorable = colorable_table(n, lists, nullptr);
            std::vector<std::uint8_t> hall(tables.hn, 1);
            uint64_t hall_count = 0, colorable_count = 0, bad_count = 0;
            int witness = -1;
            for (int h = 0; h < tables.hn; ++h) {
                uint64_t subsets = tables.connected[h];
                const std::uint8_t* alpha = tables.alpha.data() + h * tables.vn;
                while (subsets) {
                    const int u = __builtin_ctzll(subsets);
                    subsets &= subsets - 1;
                    int rhs = 0;
                    for (int c = 0; c < n; ++c) rhs += alpha[u & lists[c]];
                    if (rhs < __builtin_popcount(static_cast<unsigned>(u))) {
                        hall[h] = 0;
                        break;
                    }
                }
                hall_count += hall[h];
                colorable_count += colorable[h];
                if (colorable[h] && !hall[h]) {
                    std::cerr << "ERROR: colorable without Hall: n=" << n
                              << " G=" << r.graph6 << " H=" << h << "\n";
                    return 3;
                }
                if (hall[h] && !colorable[h]) {
                    ++bad_count;
                    if (witness < 0) witness = h;
                }
            }
            out << n << '\t' << r.graph6 << '\t' << r.gmask << '\t'
                << tables.hn << '\t' << hall_count << '\t' << colorable_count
                << '\t' << bad_count << '\t' << witness << '\t'
                << pack_hex(hall) << '\t' << pack_hex(colorable) << '\n';
        }
        std::cerr << "completed n=" << n << " classes=" << layer_count
                  << " H_per_class=" << tables.hn << "\n";
    }
    return 0;
}
