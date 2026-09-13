#define main geng_search_program_main
#include "geng_excess2_search.cpp"
#undef main

#include <iostream>
#include <numeric>
#include <set>
#include <sstream>

namespace {

using Groups = std::vector<std::vector<int>>;

std::string key(Groups g, int matching) {
    for (auto& block : g) std::sort(block.begin(), block.end());
    if (matching == 0) {
        std::sort(g.begin(), g.end());
    } else if (matching == 1) {
        if (g[0] > g[1]) std::swap(g[0], g[1]);
        std::sort(g.begin() + 2, g.end());
    } else {
        if (g[0] > g[1]) std::swap(g[0], g[1]);
        if (g[2] > g[3]) std::swap(g[2], g[3]);
        if (std::pair{g[0], g[1]} > std::pair{g[2], g[3]}) {
            std::swap(g[0], g[2]);
            std::swap(g[1], g[3]);
        }
    }
    std::ostringstream out;
    for (const auto& block : g) {
        out << '[';
        for (int x : block) out << x << ',';
        out << ']';
    }
    return out.str();
}

std::set<std::string> exhaustive_orbits(int matching) {
    const int count = 10 - 2 * matching;
    std::vector<int> p(count);
    std::iota(p.begin(), p.end(), 100);
    std::set<std::string> result;
    do {
        Groups g;
        if (matching == 0) {
            for (int arm = 0; arm < 5; ++arm)
                g.push_back({p[2 * arm], p[2 * arm + 1]});
        } else if (matching == 1) {
            g = {{p[0]}, {p[1]}, {p[2], p[3]},
                 {p[4], p[5]}, {p[6], p[7]}};
        } else {
            g = {{p[0]}, {p[1]}, {p[2]}, {p[3]}, {p[4], p[5]}};
        }
        result.insert(key(std::move(g), matching));
    } while (std::next_permutation(p.begin(), p.end()));
    return result;
}

}  // namespace

int main() {
    const std::array<size_t, 3> expected{945, 420, 45};
    for (int matching = 0; matching <= 2; ++matching) {
        std::vector<int> ports(10 - 2 * matching);
        std::iota(ports.begin(), ports.end(), 100);
        const auto production = assignments(ports, matching);
        std::set<std::string> production_keys;
        for (const auto& g : production) production_keys.insert(key(g, matching));
        const auto independent = exhaustive_orbits(matching);
        if (production.size() != expected[matching] ||
            production_keys.size() != production.size() ||
            production_keys != independent) {
            std::cerr << "FAIL matching=" << matching
                      << " vector=" << production.size()
                      << " unique=" << production_keys.size()
                      << " exhaustive=" << independent.size() << '\n';
            return 1;
        }
        std::cout << "PASS matching=" << matching
                  << " orbit_representatives=" << production.size() << '\n';
    }
    return 0;
}
