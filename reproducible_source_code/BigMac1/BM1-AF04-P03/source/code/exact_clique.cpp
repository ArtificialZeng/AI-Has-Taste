#include <algorithm>
#include <array>
#include <bit>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>

namespace {
constexpr int V = 31;
constexpr int MAX_N = 4761;
constexpr int WORDS = (MAX_N + 63) / 64;
using Triple = std::array<int, 3>;
using Block = std::array<int, 5>;
using Mask = std::array<std::uint64_t, WORDS>;

template <std::size_t N>
std::array<int, N> canonical(const std::array<int, N>& input) {
  std::array<int, N> best{};
  best.fill(V);
  for (int shift = 0; shift < V; ++shift) {
    std::array<int, N> candidate{};
    for (std::size_t i = 0; i < N; ++i) candidate[i] = (input[i] + shift) % V;
    std::sort(candidate.begin(), candidate.end());
    best = std::min(best, candidate);
  }
  return best;
}

struct Column {
  Block block;
  std::array<int, 10> resource;
  std::array<unsigned char, 15> pair_weight;
};

std::vector<Column> build_columns() {
  std::set<Triple> triples;
  for (int a = 0; a < V; ++a)
    for (int b = a + 1; b < V; ++b)
      for (int c = b + 1; c < V; ++c) triples.insert(canonical(Triple{a, b, c}));
  if (triples.size() != 145) throw std::runtime_error("triple count");
  std::map<Triple, int> triple_id;
  int id = 0;
  for (const auto& triple : triples) triple_id[triple] = id++;

  std::set<Block> blocks;
  for (int a = 0; a < V; ++a)
    for (int b = a + 1; b < V; ++b)
      for (int c = b + 1; c < V; ++c)
        for (int d = c + 1; d < V; ++d)
          for (int e = d + 1; e < V; ++e) blocks.insert(canonical(Block{a, b, c, d, e}));
  if (blocks.size() != 5481) throw std::runtime_error("block count");

  std::vector<Column> columns;
  for (const auto& block : blocks) {
    std::array<int, 10> resources{};
    int pos = 0;
    for (int a = 0; a < 5; ++a)
      for (int b = a + 1; b < 5; ++b)
        for (int c = b + 1; c < 5; ++c)
          resources[pos++] = triple_id.at(canonical(Triple{block[a], block[b], block[c]}));
    std::sort(resources.begin(), resources.end());
    if (std::adjacent_find(resources.begin(), resources.end()) == resources.end()) {
      std::array<unsigned char, 15> pair_weight{};
      for (int a = 0; a < 5; ++a)
        for (int b = a + 1; b < 5; ++b) {
          const int residue = (block[a] - block[b] + V) % V;
          const int distance = std::min(residue, V - residue);
          ++pair_weight[distance - 1];
        }
      if (std::accumulate(pair_weight.begin(), pair_weight.end(), 0) != 10)
        throw std::runtime_error("pair weight count");
      columns.push_back(Column{block, resources, pair_weight});
    }
  }
  if (columns.size() != MAX_N) throw std::runtime_error("valid column count");
  return columns;
}

bool compatible(const Column& a, const Column& b) {
  int i = 0, j = 0;
  while (i < 10 && j < 10) {
    if (a.resource[i] == b.resource[j]) return false;
    if (a.resource[i] < b.resource[j]) ++i;
    else ++j;
  }
  return true;
}

bool any(const Mask& mask, int words = WORDS) {
  for (int i = 0; i < words; ++i) if (mask[i]) return true;
  return false;
}

int cardinality(const Mask& mask, int words = WORDS) {
  int result = 0;
  for (int i = 0; i < words; ++i) result += std::popcount(mask[i]);
  return result;
}

int pop_first(Mask& mask, int words = WORDS) {
  for (int word = 0; word < words; ++word) {
    if (!mask[word]) continue;
    const int bit = std::countr_zero(mask[word]);
    mask[word] &= mask[word] - 1;
    return 64 * word + bit;
  }
  return -1;
}

void clear(Mask& mask, int vertex) {
  mask[vertex / 64] &= ~(std::uint64_t{1} << (vertex % 64));
}

struct Solver {
  const std::vector<Mask>& adjacency;
  const std::vector<Column>& columns;
  const std::vector<int>& new_to_old;
  int target;
  int vertex_count;
  int word_count;
  std::uint64_t nodes = 0;
  std::vector<int> clique;
  std::vector<int> witness;
  std::array<unsigned char, 15> pair_used{};

  bool pair_feasible(int vertex) const {
    const auto& weight = columns[new_to_old[vertex]].pair_weight;
    for (int distance = 0; distance < 15; ++distance)
      if (pair_used[distance] + weight[distance] > 9) return false;
    return true;
  }

  void add_pair(int vertex) {
    const auto& weight = columns[new_to_old[vertex]].pair_weight;
    for (int distance = 0; distance < 15; ++distance)
      pair_used[distance] += weight[distance];
  }

  void remove_pair(int vertex) {
    const auto& weight = columns[new_to_old[vertex]].pair_weight;
    for (int distance = 0; distance < 15; ++distance)
      pair_used[distance] -= weight[distance];
  }

  void filter_pair_feasible(Mask& mask) const {
    for (int word = 0; word < word_count; ++word) {
      std::uint64_t bits = mask[word];
      while (bits) {
        const int bit = std::countr_zero(bits);
        const int vertex = 64 * word + bit;
        if (vertex >= vertex_count || !pair_feasible(vertex))
          mask[word] &= ~(std::uint64_t{1} << bit);
        bits &= bits - 1;
      }
    }
  }

  bool expand(int size, Mask candidates) {
    ++nodes;
    if (size + cardinality(candidates, word_count) < target) return false;
    std::vector<int> order;
    std::vector<int> colors;
    order.reserve(cardinality(candidates, word_count));
    colors.reserve(order.capacity());
    Mask uncolored = candidates;
    int color = 0;
    while (any(uncolored, word_count)) {
      ++color;
      Mask available = uncolored;
      while (any(available, word_count)) {
        const int vertex = pop_first(available, word_count);
        clear(uncolored, vertex);
        order.push_back(vertex);
        colors.push_back(color);
        for (int word = 0; word < word_count; ++word)
          available[word] &= ~adjacency[vertex][word];
      }
    }
    Mask remaining = candidates;
    for (int i = static_cast<int>(order.size()) - 1; i >= 0; --i) {
      if (size + colors[i] < target) return false;
      const int vertex = order[i];
      if (!pair_feasible(vertex)) {
        clear(remaining, vertex);
        continue;
      }
      clique.push_back(vertex);
      add_pair(vertex);
      if (size + 1 >= target) {
        witness = clique;
        return true;
      }
      Mask next{};
      for (int word = 0; word < word_count; ++word)
        next[word] = remaining[word] & adjacency[vertex][word];
      filter_pair_feasible(next);
      if (size + 1 + cardinality(next, word_count) >= target && expand(size + 1, next))
        return true;
      remove_pair(vertex);
      clique.pop_back();
      clear(remaining, vertex);
    }
    return false;
  }
};

std::vector<int> multiplier_representatives(const std::vector<Column>& columns) {
  std::map<Block, int> index;
  for (int i = 0; i < MAX_N; ++i) index[columns[i].block] = i;
  std::vector<unsigned char> seen(MAX_N);
  std::vector<int> reps;
  for (int i = 0; i < MAX_N; ++i) {
    if (seen[i]) continue;
    std::set<int> orbit;
    for (int unit = 1; unit < V; ++unit) {
      Block scaled{};
      for (int j = 0; j < 5; ++j) scaled[j] = unit * columns[i].block[j] % V;
      orbit.insert(index.at(canonical(scaled)));
    }
    for (int vertex : orbit) seen[vertex] = 1;
    reps.push_back(*orbit.begin());
  }
  if (reps.size() != 162) throw std::runtime_error("multiplier orbit count");
  return reps;
}

void write_witness(const std::string& path, const std::vector<int>& witness,
                   const std::vector<int>& new_to_old, const std::vector<Column>& columns,
                   int fixed_old = -1) {
  std::vector<Block> blocks;
  if (fixed_old >= 0) blocks.push_back(columns[fixed_old].block);
  for (int vertex : witness) blocks.push_back(columns[new_to_old[vertex]].block);
  std::sort(blocks.begin(), blocks.end());
  std::ofstream out(path);
  out << "{\n  \"schema\": \"cyclic-315-candidate-v1\",\n  \"target\": 13,\n  \"blocks\": [\n";
  for (std::size_t i = 0; i < blocks.size(); ++i) {
    out << "    [";
    for (int j = 0; j < 5; ++j) out << (j ? ", " : "") << blocks[i][j];
    out << "]" << (i + 1 == blocks.size() ? "\n" : ",\n");
  }
  out << "  ]\n}\n";
}
}  // namespace

int main(int argc, char** argv) {
  if (argc != 3 && argc != 4) {
    std::cerr << "usage: exact_clique LOG_JSONL WITNESS_JSON [FIXED_VARIABLE]\n";
    return 2;
  }
  const auto start = std::chrono::steady_clock::now();
  const auto columns = build_columns();
  auto old_reps = multiplier_representatives(columns);
  if (argc == 4) {
    const int fixed_variable = std::stoi(argv[3]);
    if (fixed_variable < 1 || fixed_variable > MAX_N) return 2;
    const int fixed_old = fixed_variable - 1;
    std::vector<int> new_to_old;
    for (int old = 0; old < MAX_N; ++old)
      if (old != fixed_old && compatible(columns[fixed_old], columns[old]))
        new_to_old.push_back(old);
    const int active_n = static_cast<int>(new_to_old.size());
    const int active_words = (active_n + 63) / 64;
    if (active_n <= 0 || active_words > WORDS) throw std::runtime_error("fixed neighborhood");
    std::vector<int> degree(active_n);
    for (int i = 0; i < active_n; ++i)
      for (int j = i + 1; j < active_n; ++j)
        if (compatible(columns[new_to_old[i]], columns[new_to_old[j]]))
          ++degree[i], ++degree[j];
    std::vector<int> order(active_n);
    std::iota(order.begin(), order.end(), 0);
    std::sort(order.begin(), order.end(), [&](int left, int right) {
      return degree[left] != degree[right] ? degree[left] > degree[right]
                                           : new_to_old[left] < new_to_old[right];
    });
    std::vector<int> reordered;
    reordered.reserve(active_n);
    for (int index : order) reordered.push_back(new_to_old[index]);
    new_to_old.swap(reordered);
    std::vector<Mask> adjacency(active_n);
    for (int i = 0; i < active_n; ++i)
      for (int j = i + 1; j < active_n; ++j)
        if (compatible(columns[new_to_old[i]], columns[new_to_old[j]])) {
          adjacency[i][j / 64] |= std::uint64_t{1} << (j % 64);
          adjacency[j][i / 64] |= std::uint64_t{1} << (i % 64);
        }
    Solver solver{adjacency, columns, new_to_old, 12, active_n, active_words};
    solver.pair_used = columns[fixed_old].pair_weight;
    Mask candidates{};
    for (int vertex = 0; vertex < active_n; ++vertex)
      candidates[vertex / 64] |= std::uint64_t{1} << (vertex % 64);
    const bool found = solver.expand(0, candidates);
    const double seconds = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - start).count();
    std::ofstream log(argv[1]);
    if (!log) throw std::runtime_error("cannot open log");
    log << "{\"status\":\"" << (found ? "SAT" : "UNSAT_BY_COMPLETE_BRANCHING")
        << "\",\"fixed_variable\":" << fixed_variable
        << ",\"neighbor_vertices\":" << active_n << ",\"nodes\":" << solver.nodes
        << ",\"elapsed_seconds\":" << seconds << "}\n";
    if (found) {
      write_witness(argv[2], solver.witness, new_to_old, columns, fixed_old);
      std::cout << "SAT fixed_variable=" << fixed_variable << " nodes=" << solver.nodes
                << " seconds=" << seconds << "\n";
      return 10;
    }
    std::cout << "UNSAT fixed_variable=" << fixed_variable << " nodes=" << solver.nodes
              << " seconds=" << seconds << "\n";
    return 20;
  }

  // Degree-descending order improves the deterministic greedy coloring.
  std::vector<int> degree(MAX_N);
  for (int i = 0; i < MAX_N; ++i)
    for (int j = i + 1; j < MAX_N; ++j)
      if (compatible(columns[i], columns[j])) ++degree[i], ++degree[j];
  std::vector<int> new_to_old(MAX_N);
  std::iota(new_to_old.begin(), new_to_old.end(), 0);
  std::sort(new_to_old.begin(), new_to_old.end(), [&](int a, int b) {
    return degree[a] != degree[b] ? degree[a] > degree[b] : a < b;
  });
  std::vector<int> old_to_new(MAX_N);
  for (int i = 0; i < MAX_N; ++i) old_to_new[new_to_old[i]] = i;

  std::vector<Mask> adjacency(MAX_N);
  for (int i = 0; i < MAX_N; ++i) {
    for (int j = i + 1; j < MAX_N; ++j) {
      if (!compatible(columns[new_to_old[i]], columns[new_to_old[j]])) continue;
      adjacency[i][j / 64] |= std::uint64_t{1} << (j % 64);
      adjacency[j][i / 64] |= std::uint64_t{1} << (i % 64);
    }
  }

  std::ofstream log(argv[1]);
  if (!log) throw std::runtime_error("cannot open log");
  std::uint64_t total_nodes = 0;
  for (std::size_t branch = 0; branch < old_reps.size(); ++branch) {
    const int old_rep = old_reps[branch];
    const int rep = old_to_new[old_rep];
    Solver solver{adjacency, columns, new_to_old, 13, MAX_N, WORDS};
    solver.clique.push_back(rep);
    solver.add_pair(rep);
    const bool found = solver.expand(1, adjacency[rep]);
    total_nodes += solver.nodes;
    const double seconds = std::chrono::duration<double>(std::chrono::steady_clock::now() - start).count();
    log << "{\"branch\":" << branch << ",\"representative_old_id\":" << old_rep
        << ",\"representative_block\":[";
    for (int j = 0; j < 5; ++j) log << (j ? "," : "") << columns[old_rep].block[j];
    log << "],\"nodes\":" << solver.nodes << ",\"found\":"
        << (found ? "true" : "false") << ",\"elapsed_seconds\":" << seconds << "}\n";
    log.flush();
    std::cerr << "branch " << branch + 1 << "/" << old_reps.size()
              << " nodes=" << solver.nodes << " total_nodes=" << total_nodes
              << " elapsed=" << seconds << " found=" << found << "\n";
    if (found) {
      write_witness(argv[2], solver.witness, new_to_old, columns);
      return 10;
    }
  }
  const double seconds = std::chrono::duration<double>(std::chrono::steady_clock::now() - start).count();
  log << "{\"status\":\"UNSAT_BY_COMPLETE_BRANCHING\",\"branches\":" << old_reps.size() << ","
      << "\"total_nodes\":" << total_nodes << ",\"elapsed_seconds\":" << seconds << "}\n";
  std::cout << "UNSAT branches=" << old_reps.size() << " total_nodes=" << total_nodes
            << " seconds=" << seconds << "\n";
  return 20;
}
