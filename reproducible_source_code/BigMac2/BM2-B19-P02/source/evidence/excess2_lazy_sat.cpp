#include <cryptominisat5/cryptominisat.h>

#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using CMSat::Lit;
using CMSat::SATSolver;
using CMSat::lbool;
using CMSat::l_False;
using CMSat::l_True;

namespace {

constexpr int N = 24;

struct CNF {
    int vars = N * (N - 1) / 2;
    std::vector<std::vector<int>> clauses;

    int new_var() { return ++vars; }
    void add(std::vector<int> c) { clauses.push_back(std::move(c)); }
};

int edge_var(int a, int b) {
    if (a > b) std::swap(a, b);
    // 1-based index in lexicographic order (0,1),(0,2),...,(22,23).
    return 1 + a * (2 * N - a - 1) / 2 + (b - a - 1);
}

int neg(int lit) { return -lit; }

// Sinz-style forward sequential counter.  Auxiliary variables need only carry
// the implications that force s[i][j] when at least j inputs are true; the
// overflow clauses then give an equisatisfiable encoding of sum(inputs)<=k.
void at_most(CNF& f, const std::vector<int>& input, int k) {
    const int n = static_cast<int>(input.size());
    if (k >= n) return;
    if (k < 0) {
        f.add({});
        return;
    }
    if (k == 0) {
        for (int x : input) f.add({neg(x)});
        return;
    }
    std::vector<std::vector<int>> s(n, std::vector<int>(k + 1));
    for (int i = 0; i < n; ++i)
        for (int j = 1; j <= k; ++j) s[i][j] = f.new_var();

    f.add({neg(input[0]), s[0][1]});
    for (int i = 1; i < n; ++i) {
        f.add({neg(input[i]), s[i][1]});
        f.add({neg(s[i - 1][1]), s[i][1]});
        for (int j = 2; j <= k; ++j) {
            f.add({neg(s[i - 1][j]), s[i][j]});
            f.add({neg(input[i]), neg(s[i - 1][j - 1]), s[i][j]});
        }
        f.add({neg(input[i]), neg(s[i - 1][k])});
    }
}

void exactly(CNF& f, const std::vector<int>& input, int k) {
    at_most(f, input, k);
    std::vector<int> complements;
    complements.reserve(input.size());
    for (int x : input) complements.push_back(-x);
    at_most(f, complements, static_cast<int>(input.size()) - k);
}

using Fixed = std::map<int, bool>;

void force_edge(Fixed& fixed, int a, int b, bool value) {
    const int e = edge_var(a, b);
    auto [it, inserted] = fixed.emplace(e, value);
    if (!inserted && it->second != value) {
        std::cerr << "inconsistent fixed edge " << a << " " << b << "\n";
        std::exit(2);
    }
}

// Exhaustive and WLOG symmetry fixing for family (5,3^23), conditional on
// C4-freeness.  Vertex 0 has neighbours 1,...,5.  Their induced graph is a
// matching of size m, and no outside vertex meets two of them.  Relabel the
// matching and their distinct outside neighbours canonically.
CNF build_family_A(int matching, Fixed& fixed) {
    CNF f;
    if (matching < 0 || matching > 2) std::exit(2);
    for (int v = 1; v < N; ++v) force_edge(fixed, 0, v, v <= 5);

    std::set<std::pair<int, int>> matching_edges;
    if (matching >= 1) matching_edges.emplace(1, 2);
    if (matching >= 2) matching_edges.emplace(3, 4);
    for (int a = 1; a <= 5; ++a)
        for (int b = a + 1; b <= 5; ++b)
            force_edge(fixed, a, b, matching_edges.count({a, b}) != 0);

    int outside = 6;
    std::array<int, N> outside_owner{};
    outside_owner.fill(-1);
    for (int a = 1; a <= 5; ++a) {
        const bool matched = (a <= 2 * matching);
        const int needed = matched ? 1 : 2;
        for (int j = 0; j < needed; ++j) outside_owner[outside++] = a;
    }
    for (int a = 1; a <= 5; ++a)
        for (int b = 6; b < N; ++b)
            force_edge(fixed, a, b, outside_owner[b] == a);

    for (const auto& [e, value] : fixed) f.add({value ? e : -e});

    std::array<int, N> target{};
    target.fill(3);
    target[0] = 5;
    for (int v = 0; v < N; ++v) {
        int already = 0;
        std::vector<int> undecided;
        for (int w = 0; w < N; ++w) if (v != w) {
            int e = edge_var(v, w);
            auto it = fixed.find(e);
            if (it == fixed.end()) undecided.push_back(e);
            else if (it->second) ++already;
        }
        exactly(f, undecided, target[v] - already);
    }

    // Complete set of C4 edge-blocking clauses (three cycles per 4-set).
    for (int a = 0; a < N; ++a)
        for (int b = a + 1; b < N; ++b)
            for (int c = b + 1; c < N; ++c)
                for (int d = c + 1; d < N; ++d) {
                    f.add({-edge_var(a,b),-edge_var(b,c),-edge_var(c,d),-edge_var(d,a)});
                    f.add({-edge_var(a,b),-edge_var(b,d),-edge_var(d,c),-edge_var(c,a)});
                    f.add({-edge_var(a,c),-edge_var(c,b),-edge_var(b,d),-edge_var(d,a)});
                }
    return f;
}

std::vector<std::vector<int>> enumerate_cycles(
    const std::array<std::array<bool, N>, N>& adj, int length) {
    std::set<std::vector<int>> unique;
    std::array<int, N> path{};
    std::array<bool, N> used{};

    for (int start = 0; start < N; ++start) {
        used.fill(false);
        used[start] = true;
        path[0] = start;
        auto dfs = [&](auto&& self, int depth) -> void {
            int last = path[depth - 1];
            if (depth == length) {
                if (adj[last][start] && path[1] < path[length - 1]) {
                    std::vector<int> edges;
                    edges.reserve(length);
                    for (int i = 0; i < length; ++i)
                        edges.push_back(edge_var(path[i], path[(i + 1) % length]));
                    std::sort(edges.begin(), edges.end());
                    unique.insert(std::move(edges));
                }
                return;
            }
            for (int v = start + 1; v < N; ++v) {
                if (!used[v] && adj[last][v]) {
                    used[v] = true;
                    path[depth] = v;
                    self(self, depth + 1);
                    used[v] = false;
                }
            }
        };
        dfs(dfs, 1);
    }
    return {unique.begin(), unique.end()};
}

void write_cnf(const std::string& path, const CNF& f) {
    std::ofstream out(path);
    out << "p cnf " << f.vars << " " << f.clauses.size() << "\n";
    for (const auto& c : f.clauses) {
        for (int x : c) out << x << ' ';
        out << "0\n";
    }
}

std::set<std::vector<int>> load_cycle_clauses(const std::string& path) {
    std::set<std::vector<int>> result;
    std::ifstream in(path);
    std::string line;
    while (std::getline(in, line)) {
        std::istringstream ss(line);
        std::vector<int> edges;
        int length = 0, x = 0;
        if (!(ss >> length)) continue;
        while (ss >> x) edges.push_back(x);
        if (static_cast<int>(edges.size()) != length) {
            std::cerr << "bad retained cycle line\n";
            std::exit(2);
        }
        std::sort(edges.begin(), edges.end());
        result.insert(std::move(edges));
    }
    return result;
}

void write_cycles(const std::string& path,
                  const std::set<std::vector<int>>& cycles) {
    std::ofstream out(path);
    for (const auto& edges : cycles) {
        out << edges.size();
        for (int e : edges) out << ' ' << e;
        out << '\n';
    }
}

void write_witness(const std::string& path,
                   const std::array<std::array<bool, N>, N>& adj) {
    std::ofstream out(path);
    for (int v = 0; v < N; ++v) {
        out << v << ':';
        for (int w = 0; w < N; ++w) if (adj[v][w]) out << ' ' << w;
        out << '\n';
    }
}

Lit cms_lit(int dimacs) {
    int var0 = std::abs(dimacs) - 1;
    return Lit(static_cast<uint32_t>(var0), dimacs < 0);
}

void add_clause(SATSolver& solver, const std::vector<int>& c) {
    std::vector<Lit> lits;
    lits.reserve(c.size());
    for (int x : c) lits.push_back(cms_lit(x));
    solver.add_clause(lits);
}

} // namespace

int main(int argc, char** argv) {
    if (argc != 5) {
        std::cerr << "usage: excess2_lazy_sat A <matching:0..2> <seconds> <prefix>\n";
        return 2;
    }
    const std::string family = argv[1];
    const int subtype = std::stoi(argv[2]);
    const double seconds = std::stod(argv[3]);
    const std::string prefix = argv[4];
    if (family != "A" && family != "A8") {
        std::cerr << "only family A is implemented in this pass\n";
        return 2;
    }
    const bool include16 = (family == "A");

    Fixed fixed;
    CNF f = build_family_A(subtype, fixed);
    const std::string cycles_path = prefix + ".cycles";
    auto retained = load_cycle_clauses(cycles_path);
    for (const auto& edges : retained) {
        std::vector<int> clause;
        for (int e : edges) clause.push_back(-e);
        f.add(std::move(clause));
    }

    SATSolver solver;
    solver.set_num_threads(1);
    solver.new_vars(static_cast<uint32_t>(f.vars));
    for (const auto& c : f.clauses) add_clause(solver, c);

    std::ofstream log(prefix + ".log", std::ios::app);
    const auto begun = std::chrono::steady_clock::now();
    size_t iteration = 0;
    while (true) {
        const double elapsed = std::chrono::duration<double>(
            std::chrono::steady_clock::now() - begun).count();
        if (elapsed >= seconds) {
            write_cycles(cycles_path, retained);
            write_cnf(prefix + ".cnf", f);
            log << "STOP time elapsed=" << elapsed << " iterations=" << iteration
                << " retained=" << retained.size() << "\n";
            std::cout << "UNKNOWN iterations=" << iteration
                      << " retained=" << retained.size() << "\n";
            return 0;
        }
        lbool status = solver.solve();
        ++iteration;
        if (status == l_False) {
            write_cycles(cycles_path, retained);
            write_cnf(prefix + ".cnf", f);
            log << "UNSAT iterations=" << iteration << " retained=" << retained.size()
                << " elapsed=" << elapsed << "\n";
            std::cout << "UNSAT iterations=" << iteration
                      << " retained=" << retained.size() << "\n";
            return 20;
        }
        if (status != l_True) {
            write_cycles(cycles_path, retained);
            write_cnf(prefix + ".cnf", f);
            log << "UNKNOWN solver iterations=" << iteration << "\n";
            return 0;
        }

        const auto& model = solver.get_model();
        std::array<std::array<bool, N>, N> adj{};
        for (int a = 0; a < N; ++a)
            for (int b = a + 1; b < N; ++b) {
                int e = edge_var(a, b);
                bool value = model[static_cast<size_t>(e - 1)] == l_True;
                adj[a][b] = adj[b][a] = value;
            }

        auto c8 = enumerate_cycles(adj, 8);
        std::vector<std::vector<int>> c16;
        if (include16) c16 = enumerate_cycles(adj, 16);
        size_t added = 0;
        for (const auto* collection : {&c8, &c16}) {
            for (const auto& edges : *collection) {
                if (retained.insert(edges).second) {
                    std::vector<int> clause;
                    clause.reserve(edges.size());
                    for (int e : edges) clause.push_back(-e);
                    add_clause(solver, clause);
                    f.add(std::move(clause));
                    ++added;
                }
            }
        }
        if (added == 0) {
            write_witness(prefix + ".witness", adj);
            write_cycles(cycles_path, retained);
            write_cnf(prefix + ".cnf", f);
            log << "SAT_WITNESS iterations=" << iteration << " retained=" << retained.size()
                << " elapsed=" << elapsed << "\n";
            std::cout << "SAT_WITNESS iterations=" << iteration << "\n";
            return 10;
        }
        if (iteration <= 10 || iteration % 100 == 0) {
            const double now = std::chrono::duration<double>(
                std::chrono::steady_clock::now() - begun).count();
            log << "ITER " << iteration << " c8=" << c8.size()
                << " c16=" << c16.size() << " added=" << added
                << " retained=" << retained.size() << " elapsed=" << now << "\n";
            log.flush();
        }
        if (iteration % 250 == 0) write_cycles(cycles_path, retained);
    }
}
