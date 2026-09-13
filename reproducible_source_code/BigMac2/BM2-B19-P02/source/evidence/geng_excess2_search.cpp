#include <algorithm>
#include <array>
#include <chrono>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <vector>

namespace {
constexpr int FULL_N = 24;
constexpr int H_N = 18;
using Adj = std::array<uint32_t, FULL_N>;

bool has_cycle(const Adj& adj, int n, int length) {
    std::array<int, FULL_N> path{};
    uint32_t used = 0;
    for (int start = 0; start < n; ++start) {
        used = uint32_t(1) << start;
        path[0] = start;
        auto dfs = [&](auto&& self, int depth, int last) -> bool {
            if (depth == length)
                return ((adj[last] >> start) & 1U) && path[1] < path[length - 1];
            uint32_t choices = adj[last] & ~used;
            // The start is the least vertex on a canonically enumerated cycle.
            choices &= ~((uint32_t(1) << (start + 1)) - 1U);
            while (choices) {
                int v = __builtin_ctz(choices);
                choices &= choices - 1;
                used |= uint32_t(1) << v;
                path[depth] = v;
                if (self(self, depth + 1, v)) return true;
                used &= ~(uint32_t(1) << v);
            }
            return false;
        };
        if (dfs(dfs, 1, start)) return true;
    }
    return false;
}

Adj parse_graph6(const std::string& line) {
    Adj a{};
    int n = static_cast<unsigned char>(line[0]) - 63;
    if (n != H_N) {
        std::cerr << "expected graph6 order 18\n";
        std::exit(2);
    }
    int pos = 1, remaining = 0, byte = 0;
    auto bit = [&]() {
        if (remaining == 0) {
            byte = static_cast<unsigned char>(line[pos++]) - 63;
            remaining = 6;
        }
        int b = (byte >> (--remaining)) & 1;
        return b;
    };
    // graph6 upper triangle is column-major: (0,1),(0,2),(1,2),...
    for (int high = 1; high < n; ++high)
        for (int low = 0; low < high; ++low)
            if (bit()) {
                int u = low + 6, v = high + 6;
                a[u] |= uint32_t(1) << v;
                a[v] |= uint32_t(1) << u;
            }
    return a;
}

void add_edge(Adj& a, int u, int v) {
    a[u] |= uint32_t(1) << v;
    a[v] |= uint32_t(1) << u;
}

std::vector<std::vector<std::vector<int>>> assignments(
    const std::vector<int>& ports, int matching) {
    std::vector<std::vector<std::vector<int>>> out;
    if (matching == 0) {
        // All five arms are symmetric: enumerate the 945 set partitions into pairs.
        std::vector<std::vector<int>> groups;
        auto rec = [&](auto&& self, std::vector<int> left) -> void {
            if (left.empty()) { out.push_back(groups); return; }
            int x = left[0];
            for (size_t j = 1; j < left.size(); ++j) {
                int y = left[j];
                std::vector<int> next;
                for (size_t k = 1; k < left.size(); ++k) if (k != j) next.push_back(left[k]);
                groups.push_back({x, y});
                self(self, next);
                groups.pop_back();
            }
        };
        rec(rec, ports);
    } else if (matching == 1) {
        // Arms 1,2 are symmetric singleton arms; arms 3,4,5 symmetric pair arms.
        for (size_t i = 0; i < ports.size(); ++i)
            for (size_t j = i + 1; j < ports.size(); ++j) {
                std::vector<int> left;
                for (size_t k = 0; k < ports.size(); ++k) if (k != i && k != j) left.push_back(ports[k]);
                std::vector<std::vector<int>> groups{{ports[i]}, {ports[j]}};
                auto rec = [&](auto&& self, std::vector<int> rem) -> void {
                    if (rem.empty()) { out.push_back(groups); return; }
                    int x = rem[0];
                    for (size_t q = 1; q < rem.size(); ++q) {
                        int y = rem[q];
                        std::vector<int> next;
                        for (size_t k = 1; k < rem.size(); ++k) if (k != q) next.push_back(rem[k]);
                        groups.push_back({x, y}); self(self, next); groups.pop_back();
                    }
                };
                rec(rec, left);
            }
    } else {
        // Arm 5 takes a pair.  The other ports are partitioned into the two
        // endpoint-pairs of matching edges (1,2) and (3,4), modulo the gadget's
        // wreath-product automorphism group.
        for (size_t i = 0; i < ports.size(); ++i)
            for (size_t j = i + 1; j < ports.size(); ++j) {
                std::vector<int> left;
                for (size_t k = 0; k < ports.size(); ++k) if (k != i && k != j) left.push_back(ports[k]);
                int x = left[0];
                for (size_t q = 1; q < left.size(); ++q) {
                    int y = left[q];
                    std::vector<int> other;
                    for (size_t k = 1; k < left.size(); ++k) if (k != q) other.push_back(left[k]);
                    std::vector<std::vector<int>> g{{x}, {y}, {other[0]}, {other[1]}, {ports[i], ports[j]}};
                    // Canonical order of the two matched edges.
                    if (g[0][0] > g[1][0]) std::swap(g[0], g[1]);
                    if (g[2][0] > g[3][0]) std::swap(g[2], g[3]);
                    if (g[0][0] > g[2][0]) { std::swap(g[0], g[2]); std::swap(g[1], g[3]); }
                    out.push_back(g);
                }
            }
        std::sort(out.begin(), out.end());
        out.erase(std::unique(out.begin(), out.end()), out.end());
    }
    return out;
}

void write_witness(const std::string& path, const Adj& a) {
    std::ofstream out(path);
    for (int v = 0; v < FULL_N; ++v) {
        out << v << ':';
        for (int w = 0; w < FULL_N; ++w) if ((a[v] >> w) & 1U) out << ' ' << w;
        out << '\n';
    }
}
}

int main(int argc, char** argv) {
    if (argc != 4) {
        std::cerr << "usage: geng_excess2_search <matching 0..2> <log> <witness>\n";
        return 2;
    }
    int matching = std::stoi(argv[1]);
    std::ofstream log(argv[2]);
    uint64_t graphs = 0, h_survivors = 0, assignments_tested = 0, c4_reject = 0, c8_reject = 0, c16_reject = 0;
    auto begun = std::chrono::steady_clock::now();
    std::string line;
    while (std::getline(std::cin, line)) {
        if (line.empty() || line[0] == '>') continue;
        ++graphs;
        Adj h = parse_graph6(line);
        if (has_cycle(h, FULL_N, 8) || has_cycle(h, FULL_N, 16)) continue;
        ++h_survivors;
        std::vector<int> ports;
        for (int v = 6; v < FULL_N; ++v)
            if (__builtin_popcount(h[v]) == 2) ports.push_back(v);
        if (static_cast<int>(ports.size()) != 10 - 2 * matching) {
            std::cerr << "degree count mismatch\n";
            return 2;
        }
        auto assns = assignments(ports, matching);
        for (const auto& groups : assns) {
            ++assignments_tested;
            Adj g = h;
            for (int a = 1; a <= 5; ++a) add_edge(g, 0, a);
            if (matching >= 1) add_edge(g, 1, 2);
            if (matching >= 2) add_edge(g, 3, 4);
            for (size_t a = 0; a < groups.size(); ++a)
                for (int port : groups[a]) add_edge(g, static_cast<int>(a) + 1, port);
            if (has_cycle(g, FULL_N, 4)) { ++c4_reject; continue; }
            if (has_cycle(g, FULL_N, 8)) { ++c8_reject; continue; }
            if (has_cycle(g, FULL_N, 16)) { ++c16_reject; continue; }
            write_witness(argv[3], g);
            double sec = std::chrono::duration<double>(std::chrono::steady_clock::now() - begun).count();
            log << "SAT_WITNESS matching=" << matching << " graphs=" << graphs
                << " H_survivors=" << h_survivors << " assignments=" << assignments_tested
                << " seconds=" << sec << " graph6_H=" << line << '\n';
            return 10;
        }
        if (graphs % 100000 == 0) {
            double sec = std::chrono::duration<double>(std::chrono::steady_clock::now() - begun).count();
            log << "PROGRESS graphs=" << graphs << " H_survivors=" << h_survivors
                << " assignments=" << assignments_tested << " seconds=" << sec << '\n';
            log.flush();
        }
    }
    double sec = std::chrono::duration<double>(std::chrono::steady_clock::now() - begun).count();
    log << "EXHAUSTED matching=" << matching << " graphs=" << graphs
        << " H_survivors=" << h_survivors << " assignments=" << assignments_tested
        << " c4_reject=" << c4_reject << " c8_reject=" << c8_reject
        << " c16_reject=" << c16_reject << " seconds=" << sec << '\n';
    std::cout << "EXHAUSTED graphs=" << graphs << " H_survivors=" << h_survivors
              << " assignments=" << assignments_tested << '\n';
    return 20;
}
