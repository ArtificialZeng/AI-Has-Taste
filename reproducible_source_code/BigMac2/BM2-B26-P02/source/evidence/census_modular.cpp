// Exhaustive order-eight fixed-start cover-time equality census.
//
// Exactness principle: when every principal system used below is nonsingular
// over F_p, each computed residue is the reduction modulo p of the unique
// rational cover time.  A nonzero residue of a difference therefore proves
// that the rational difference is nonzero.  We use two primes and two
// structurally different cover-time formulations.

#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <queue>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using Graph = std::array<uint8_t, 8>;
using Cover = std::array<int, 8>;

static bool trial_division_prime(int n) {
    if (n < 2) return false;
    if (n % 2 == 0) return n == 2;
    for (int d = 3; static_cast<int64_t>(d) * d <= n; d += 2) {
        if (n % d == 0) return false;
    }
    return true;
}

struct Field {
    int p;
    std::vector<int> inverse;

    explicit Field(int prime) : p(prime), inverse(prime, 0) {
        if (!trial_division_prime(prime)) throw std::runtime_error("field modulus is not prime");
        inverse[1] = 1;
        for (int x = 2; x < p; ++x) {
            inverse[x] = p - static_cast<int>((static_cast<int64_t>(p / x) * inverse[p % x]) % p);
        }
    }

    inline int add(int a, int b) const {
        int x = a + b;
        return x >= p ? x - p : x;
    }
    inline int sub(int a, int b) const {
        int x = a - b;
        return x < 0 ? x + p : x;
    }
    inline int mul(int a, int b) const {
        return static_cast<int>((static_cast<int64_t>(a) * b) % p);
    }
    inline int neg(int a) const { return a == 0 ? 0 : p - a; }
};

static std::string clean_line(std::string line) {
    if (!line.empty() && line.back() == '\r') line.pop_back();
    return line;
}

static Graph decode_graph6(const std::string& line) {
    if (line.size() != 6 || static_cast<unsigned char>(line[0]) != 71) {
        throw std::runtime_error("expected a six-byte, order-eight graph6 record");
    }
    std::array<int, 30> bits{};
    int cursor = 0;
    for (int k = 1; k < 6; ++k) {
        int value = static_cast<unsigned char>(line[k]) - 63;
        if (value < 0 || value >= 64) throw std::runtime_error("invalid graph6 byte");
        for (int shift = 5; shift >= 0; --shift) bits[cursor++] = (value >> shift) & 1;
    }
    Graph graph{};
    cursor = 0;
    for (int v = 1; v < 8; ++v) {
        for (int u = 0; u < v; ++u) {
            if (bits[cursor]) {
                graph[u] |= static_cast<uint8_t>(1U << v);
                graph[v] |= static_cast<uint8_t>(1U << u);
            }
            ++cursor;
        }
    }
    return graph;
}

static int edge_count(const Graph& graph) {
    int twice = 0;
    for (uint8_t row : graph) twice += __builtin_popcount(static_cast<unsigned>(row));
    return twice / 2;
}

static bool connected(const Graph& graph) {
    uint8_t seen = 1;
    uint8_t frontier = 1;
    while (frontier) {
        int x = __builtin_ctz(static_cast<unsigned>(frontier));
        frontier &= static_cast<uint8_t>(frontier - 1);
        uint8_t fresh = static_cast<uint8_t>(graph[x] & ~seen);
        seen |= fresh;
        frontier |= fresh;
    }
    return seen == 255;
}

// Method A linear algebra: full Gauss-Jordan row reduction.
static bool solve_gauss_jordan(int k, int a[8][9], int out[8], const Field& f) {
    for (int col = 0; col < k; ++col) {
        int pivot = col;
        while (pivot < k && a[pivot][col] == 0) ++pivot;
        if (pivot == k) return false;
        if (pivot != col) {
            for (int j = col; j <= k; ++j) std::swap(a[pivot][j], a[col][j]);
        }
        int scale = f.inverse[a[col][col]];
        for (int j = col; j <= k; ++j) a[col][j] = f.mul(a[col][j], scale);
        for (int row = 0; row < k; ++row) {
            if (row == col || a[row][col] == 0) continue;
            int factor = a[row][col];
            for (int j = col; j <= k; ++j) {
                a[row][j] = f.sub(a[row][j], f.mul(factor, a[col][j]));
            }
        }
    }
    for (int i = 0; i < k; ++i) out[i] = a[i][k];
    return true;
}

// Method B linear algebra: unnormalised forward elimination and backsolve.
static bool solve_forward_back(int k, int a[8][9], int out[8], const Field& f) {
    for (int col = 0; col < k; ++col) {
        int pivot = col;
        while (pivot < k && a[pivot][col] == 0) ++pivot;
        if (pivot == k) return false;
        if (pivot != col) {
            for (int j = col; j <= k; ++j) std::swap(a[pivot][j], a[col][j]);
        }
        int pivot_inverse = f.inverse[a[col][col]];
        for (int row = col + 1; row < k; ++row) {
            if (a[row][col] == 0) continue;
            int factor = f.mul(a[row][col], pivot_inverse);
            a[row][col] = 0;
            for (int j = col + 1; j <= k; ++j) {
                a[row][j] = f.sub(a[row][j], f.mul(factor, a[col][j]));
            }
        }
    }
    for (int row = k - 1; row >= 0; --row) {
        int value = a[row][k];
        for (int j = row + 1; j < k; ++j) value = f.sub(value, f.mul(a[row][j], out[j]));
        if (a[row][row] == 0) return false;
        out[row] = f.mul(value, f.inverse[a[row][row]]);
    }
    return true;
}

// Method A: solve C(x,A) by decreasing size of the visited set A.
static bool visited_set_cover(const Graph& graph, const Field& f, Cover& answer) {
    int degree[8];
    for (int x = 0; x < 8; ++x) degree[x] = __builtin_popcount(static_cast<unsigned>(graph[x]));
    int value[256][8]{};
    for (int size = 7; size >= 1; --size) {
        for (int mask = 1; mask < 255; ++mask) {
            if (__builtin_popcount(static_cast<unsigned>(mask)) != size) continue;
            int vertex[8];
            int k = 0;
            for (int x = 0; x < 8; ++x) if (mask & (1 << x)) vertex[k++] = x;
            int a[8][9]{};
            for (int i = 0; i < k; ++i) {
                int x = vertex[i];
                for (int j = 0; j < k; ++j) {
                    int y = vertex[j];
                    a[i][j] = (x == y) ? degree[x] : ((graph[x] >> y) & 1 ? f.p - 1 : 0);
                }
                int rhs = degree[x];
                uint8_t outside = static_cast<uint8_t>(graph[x] & ~mask);
                while (outside) {
                    int y = __builtin_ctz(static_cast<unsigned>(outside));
                    outside &= static_cast<uint8_t>(outside - 1);
                    rhs = f.add(rhs, value[mask | (1 << y)][y]);
                }
                a[i][k] = rhs;
            }
            int solution[8]{};
            if (!solve_gauss_jordan(k, a, solution, f)) return false;
            for (int i = 0; i < k; ++i) value[mask][vertex[i]] = solution[i];
        }
    }
    for (int s = 0; s < 8; ++s) answer[s] = value[1 << s][s];
    return true;
}

// Method B: inclusion-exclusion over absorbing-set hitting times.
static bool absorbing_ie_cover(const Graph& graph, const Field& f, Cover& answer) {
    int degree[8];
    for (int x = 0; x < 8; ++x) degree[x] = __builtin_popcount(static_cast<unsigned>(graph[x]));
    answer.fill(0);
    // `unhit` is V minus the nonempty absorbing target set.
    for (int unhit = 1; unhit < 255; ++unhit) {
        int vertex[8];
        int k = 0;
        for (int x = 0; x < 8; ++x) if (unhit & (1 << x)) vertex[k++] = x;
        int a[8][9]{};
        for (int i = 0; i < k; ++i) {
            int x = vertex[i];
            for (int j = 0; j < k; ++j) {
                int y = vertex[j];
                a[i][j] = (x == y) ? degree[x] : ((graph[x] >> y) & 1 ? f.p - 1 : 0);
            }
            a[i][k] = degree[x];
        }
        int solution[8]{};
        if (!solve_forward_back(k, a, solution, f)) return false;
        bool positive = ((8 - k) & 1) != 0;
        for (int i = 0; i < k; ++i) {
            int x = vertex[i];
            answer[x] = positive ? f.add(answer[x], solution[i]) : f.sub(answer[x], solution[i]);
        }
    }
    return true;
}

static std::vector<std::string> read_lines(const std::string& path) {
    std::ifstream input(path);
    if (!input) throw std::runtime_error("cannot open " + path);
    std::vector<std::string> lines;
    std::string line;
    while (std::getline(input, line)) lines.push_back(clean_line(line));
    return lines;
}

int main(int argc, char** argv) {
    try {
        if (argc != 4) {
            std::cerr << "usage: census_modular INVENTORY BASE_ROOTS AUGMENTED_ROOTS\n";
            return 2;
        }
        auto began = std::chrono::steady_clock::now();
        const std::array<int, 2> primes{1000003, 1000033};
        Field field0(primes[0]);
        Field field1(primes[1]);
        const std::array<const Field*, 2> fields{&field0, &field1};

        std::vector<std::string> inventory_lines = read_lines(argv[1]);
        std::vector<std::string> base_roots = read_lines(argv[2]);
        if (inventory_lines.size() != 11094) throw std::runtime_error("inventory count is not 11094");
        if (base_roots.size() != inventory_lines.size() * 8) throw std::runtime_error("base-root count mismatch");

        std::unordered_set<std::string> labelled_records;
        std::vector<Graph> graphs;
        std::vector<int> edges;
        int nonedges = 0;
        for (const auto& line : inventory_lines) {
            if (!labelled_records.insert(line).second) throw std::runtime_error("duplicate labelled graph6 record");
            Graph graph = decode_graph6(line);
            int m = edge_count(graph);
            if (!connected(graph) || m < 8 || m > 28) throw std::runtime_error("inventory hypothesis failure");
            graphs.push_back(graph);
            edges.push_back(m);
            nonedges += 28 - m;
        }
        if (nonedges != 150573) throw std::runtime_error("nonedge total mismatch");

        using Pair = std::array<int, 2>;
        std::vector<std::array<Pair, 8>> covers(graphs.size());
        int solver_residue_comparisons = 0;
        for (size_t i = 0; i < graphs.size(); ++i) {
            for (int q = 0; q < 2; ++q) {
                Cover method_a{}, method_b{};
                if (!visited_set_cover(graphs[i], *fields[q], method_a)) {
                    throw std::runtime_error("singular visited-set system modulo prime");
                }
                if (!absorbing_ie_cover(graphs[i], *fields[q], method_b)) {
                    throw std::runtime_error("singular absorbing-chain system modulo prime");
                }
                for (int s = 0; s < 8; ++s) {
                    ++solver_residue_comparisons;
                    if (method_a[s] != method_b[s]) throw std::runtime_error("independent solver mismatch");
                    covers[i][s][q] = method_a[s];
                }
            }
        }

        std::unordered_map<std::string, Pair> rooted_value;
        rooted_value.reserve(base_roots.size());
        int consistent_duplicate_roots = 0;
        for (size_t i = 0; i < graphs.size(); ++i) {
            for (int s = 0; s < 8; ++s) {
                const std::string& key = base_roots[i * 8 + s];
                if (edge_count(decode_graph6(key)) != edges[i]) throw std::runtime_error("base-root edge count mismatch");
                auto [it, inserted] = rooted_value.emplace(key, covers[i][s]);
                if (!inserted) {
                    ++consistent_duplicate_roots;
                    if (it->second != covers[i][s]) throw std::runtime_error("root-canonical value inconsistency");
                }
            }
        }

        std::ifstream augmented(argv[3]);
        if (!augmented) throw std::runtime_error("cannot open augmented-root stream");
        int64_t marked = 0;
        std::array<int64_t, 2> zero_residues{0, 0};
        std::array<int64_t, 2> direct_zero_residues{0, 0};
        int direct_augmented_graphs = 0;
        std::string key;
        for (size_t i = 0; i < graphs.size(); ++i) {
            const Graph& graph = graphs[i];
            for (int v = 1; v < 8; ++v) {
                for (int u = 0; u < v; ++u) {
                    if ((graph[u] >> v) & 1) continue;
                    Graph added = graph;
                    added[u] |= static_cast<uint8_t>(1U << v);
                    added[v] |= static_cast<uint8_t>(1U << u);
                    Cover direct_a{}, direct_b{};
                    if (!visited_set_cover(added, field0, direct_a)) {
                        throw std::runtime_error("singular direct visited-set system modulo first prime");
                    }
                    if (!absorbing_ie_cover(added, field1, direct_b)) {
                        throw std::runtime_error("singular direct absorbing-chain system modulo second prime");
                    }
                    ++direct_augmented_graphs;
                    for (int s = 0; s < 8; ++s) {
                        if (!std::getline(augmented, key)) throw std::runtime_error("short augmented-root stream");
                        key = clean_line(key);
                        if (edge_count(decode_graph6(key)) != edges[i] + 1) {
                            throw std::runtime_error("augmented-root edge count mismatch");
                        }
                        auto it = rooted_value.find(key);
                        if (it == rooted_value.end()) throw std::runtime_error("augmented rooted class absent from inventory");
                        for (int q = 0; q < 2; ++q) {
                            if (it->second[q] == covers[i][s][q]) ++zero_residues[q];
                        }
                        if (direct_a[s] == covers[i][s][0]) ++direct_zero_residues[0];
                        if (direct_b[s] == covers[i][s][1]) ++direct_zero_residues[1];
                        ++marked;
                    }
                }
            }
        }
        if (std::getline(augmented, key)) throw std::runtime_error("long augmented-root stream");
        if (marked != 1204584) throw std::runtime_error("marked-instance count mismatch");
        if (direct_augmented_graphs != nonedges) throw std::runtime_error("direct augmented-graph count mismatch");

        double seconds = std::chrono::duration<double>(std::chrono::steady_clock::now() - began).count();
        bool pass = zero_residues[0] == 0 && zero_residues[1] == 0
            && direct_zero_residues[0] == 0 && direct_zero_residues[1] == 0;
        std::cout
            << "{\n"
            << "  \"status\": \"" << (pass ? "pass" : "modular_zero_requires_exact_followup") << "\",\n"
            << "  \"inventory_records\": " << graphs.size() << ",\n"
            << "  \"inventory_connected_non_tree_hypotheses_checked\": " << graphs.size() << ",\n"
            << "  \"distinct_labelled_graph6_records\": " << labelled_records.size() << ",\n"
            << "  \"nonedges\": " << nonedges << ",\n"
            << "  \"marked_graph_nonedge_start_instances\": " << marked << ",\n"
            << "  \"base_rooted_records\": " << base_roots.size() << ",\n"
            << "  \"distinct_rooted_isomorphism_classes\": " << rooted_value.size() << ",\n"
            << "  \"consistent_duplicate_root_records\": " << consistent_duplicate_roots << ",\n"
            << "  \"primes\": [" << primes[0] << ", " << primes[1] << "],\n"
            << "  \"cover_residue_comparisons_between_solvers\": " << solver_residue_comparisons << ",\n"
            << "  \"singular_principal_systems\": 0,\n"
            << "  \"canonical_lookup_zero_difference_residues\": [" << zero_residues[0] << ", " << zero_residues[1] << "],\n"
            << "  \"direct_augmented_graphs_solved\": " << direct_augmented_graphs << ",\n"
            << "  \"direct_marked_comparisons_per_method\": " << marked << ",\n"
            << "  \"direct_zero_difference_residues\": [" << direct_zero_residues[0] << ", " << direct_zero_residues[1] << "],\n"
            << "  \"method_a\": \"visited-set recurrence with Gauss-Jordan elimination\",\n"
            << "  \"method_b\": \"inclusion-exclusion of absorbing-set hitting times with forward elimination/backsolve\",\n"
            << "  \"canonicalization\": \"nauty labelg, singleton color at distinguished start\",\n"
            << "  \"exactness\": \"successful finite-field systems are reductions of the rational systems; a nonzero residue proves a nonzero rational difference\",\n"
            << "  \"elapsed_seconds\": " << seconds << "\n"
            << "}\n";
        return pass ? 0 : 3;
    } catch (const std::exception& error) {
        std::cerr << "census failure: " << error.what() << "\n";
        return 1;
    }
}
