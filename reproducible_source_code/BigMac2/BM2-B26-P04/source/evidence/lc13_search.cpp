#include <algorithm>
#include <array>
#include <bit>
#include <chrono>
#include <cstdint>
#include <deque>
#include <fstream>
#include <iostream>
#include <random>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <vector>

namespace {

constexpr int N = 13;
constexpr int E = N * (N - 1) / 2;

struct Key {
  std::uint64_t lo = 0;
  std::uint64_t hi = 0;
  bool operator==(const Key &) const = default;
};

struct KeyHash {
  std::size_t operator()(const Key &x) const noexcept {
    std::uint64_t z = x.lo ^ (x.hi + 0x9e3779b97f4a7c15ULL +
                              (x.lo << 6) + (x.lo >> 2));
    z ^= z >> 30;
    z *= 0xbf58476d1ce4e5b9ULL;
    z ^= z >> 27;
    z *= 0x94d049bb133111ebULL;
    z ^= z >> 31;
    return static_cast<std::size_t>(z);
  }
};

struct Graph {
  Key key;
  std::array<std::uint16_t, N> row{};
};

std::array<std::array<int, N>, N> edge_pos;
std::array<Key, 1 << N> clique_mask;

void flip(Key &x, int p) {
  if (p < 64) x.lo ^= (1ULL << p);
  else x.hi ^= (1ULL << (p - 64));
}

bool get(const Key &x, int p) {
  if (p < 64) return (x.lo >> p) & 1ULL;
  return (x.hi >> (p - 64)) & 1ULL;
}

Key xored(Key a, const Key &b) {
  a.lo ^= b.lo;
  a.hi ^= b.hi;
  return a;
}

void initialize_tables() {
  for (auto &a : edge_pos) a.fill(-1);
  int p = 0;
  // graph6 order: (0,1), (0,2), (1,2), (0,3), ...
  for (int j = 1; j < N; ++j) {
    for (int i = 0; i < j; ++i) {
      edge_pos[i][j] = edge_pos[j][i] = p++;
    }
  }
  if (p != E) throw std::logic_error("edge table size");
  for (int s = 0; s < (1 << N); ++s) {
    Key m;
    for (int j = 1; j < N; ++j) {
      if (!((s >> j) & 1)) continue;
      for (int i = 0; i < j; ++i) {
        if ((s >> i) & 1) flip(m, edge_pos[i][j]);
      }
    }
    clique_mask[s] = m;
  }
}

Graph from_key(Key key) {
  Graph g;
  g.key = key;
  for (int j = 1; j < N; ++j) {
    for (int i = 0; i < j; ++i) {
      if (get(key, edge_pos[i][j])) {
        g.row[i] |= std::uint16_t(1U << j);
        g.row[j] |= std::uint16_t(1U << i);
      }
    }
  }
  return g;
}

Graph decode_graph6(const std::string &s) {
  if (s.size() != 14 || static_cast<unsigned char>(s[0]) != 63 + N)
    throw std::invalid_argument("expected a 14-byte graph6 string of order 13");
  Key key;
  for (int p = 0; p < E; ++p) {
    int value = static_cast<unsigned char>(s[1 + p / 6]) - 63;
    if (value < 0 || value > 63) throw std::invalid_argument("bad graph6 byte");
    if ((value >> (5 - p % 6)) & 1) flip(key, p);
  }
  return from_key(key);
}

std::string encode_graph6(const Graph &g) {
  std::string s(14, '?');
  s[0] = static_cast<char>(63 + N);
  for (int c = 0; c < 13; ++c) {
    int value = 0;
    for (int k = 0; k < 6; ++k) {
      int p = 6 * c + k;
      if (p < E && get(g.key, p)) value |= 1 << (5 - k);
    }
    s[1 + c] = static_cast<char>(63 + value);
  }
  return s;
}

Graph local_complement(const Graph &g, int v) {
  Graph h = g;
  const std::uint16_t neighbors = g.row[v];
  h.key = xored(g.key, clique_mask[neighbors]);
  std::uint16_t todo = neighbors;
  while (todo) {
    int u = std::countr_zero(todo);
    todo &= std::uint16_t(todo - 1);
    h.row[u] ^= std::uint16_t(neighbors & ~(1U << u));
  }
  return h;
}

bool independent_dfs(const std::array<std::uint16_t, N> &row,
                     std::uint16_t candidates, int need,
                     std::uint16_t chosen, std::uint16_t &answer) {
  if (need == 0) {
    answer = chosen;
    return true;
  }
  while (std::popcount(candidates) >= need) {
    int v = std::countr_zero(candidates);
    candidates &= std::uint16_t(candidates - 1);
    if (independent_dfs(row,
                        std::uint16_t(candidates & ~row[v]), need - 1,
                        std::uint16_t(chosen | (1U << v)), answer))
      return true;
  }
  return false;
}

std::uint16_t independent_five(const Graph &g) {
  std::uint16_t answer = 0;
  independent_dfs(g.row, std::uint16_t((1U << N) - 1), 5, 0, answer);
  return answer;
}

struct TrialResult {
  enum class Status { fail, cap, pass } status;
  std::size_t discovered;
  std::size_t processed;
  Graph failing_graph;
  std::uint16_t independent_set = 0;
};

TrialResult orbit_trial(const Graph &start, std::size_t cap,
                        bool progress = false) {
  std::unordered_set<Key, KeyHash> seen;
  seen.reserve(cap < 1000000 ? 2 * cap : cap + cap / 3);
  std::deque<Graph> queue;
  seen.insert(start.key);
  queue.push_back(start);
  std::size_t processed = 0;
  while (!queue.empty()) {
    Graph g = queue.front();
    queue.pop_front();
    ++processed;
    if (auto set = independent_five(g))
      return {TrialResult::Status::fail, seen.size(), processed, g, set};
    for (int v = 0; v < N; ++v) {
      Graph h = local_complement(g, v);
      if (seen.insert(h.key).second) {
        queue.push_back(h);
        if (seen.size() >= cap)
          return {TrialResult::Status::cap, seen.size(), processed, {}, 0};
      }
    }
    if (progress && processed % 100000 == 0)
      std::cerr << "processed=" << processed << " discovered=" << seen.size()
                << " queue=" << queue.size() << '\n' << std::flush;
  }
  return {TrialResult::Status::pass, seen.size(), processed, {}, 0};
}

void write_u64_le(std::ostream &out, std::uint64_t x) {
  for (int i = 0; i < 8; ++i) out.put(static_cast<char>((x >> (8 * i)) & 255));
}

void write_u16_le(std::ostream &out, std::uint16_t x) {
  out.put(static_cast<char>(x & 255));
  out.put(static_cast<char>((x >> 8) & 255));
}

void write_u32_le(std::ostream &out, std::uint32_t x) {
  for (int i = 0; i < 4; ++i) out.put(static_cast<char>((x >> (8 * i)) & 255));
}

void certify_to_file(const Graph &start, const std::string &path) {
  struct Node {
    Graph graph;
    std::uint32_t parent;
    std::uint8_t move;
  };
  std::unordered_set<Key, KeyHash> seen;
  seen.reserve(1000000);
  std::vector<Node> nodes;
  nodes.reserve(800000);
  std::deque<std::uint32_t> queue;
  seen.insert(start.key);
  nodes.push_back({start, UINT32_MAX, UINT8_MAX});
  queue.push_back(0);
  std::size_t processed = 0;
  while (!queue.empty()) {
    const std::uint32_t index = queue.front();
    queue.pop_front();
    const Graph g = nodes[index].graph;
    ++processed;
    if (auto set = independent_five(g)) {
      std::cerr << "certificate aborted: independent five-set in state "
                << encode_graph6(g) << '\n';
      throw std::runtime_error("candidate fails");
    }
    for (int v = 0; v < N; ++v) {
      Graph h = local_complement(g, v);
      if (seen.insert(h.key).second) {
        if (nodes.size() >= UINT32_MAX) throw std::runtime_error("orbit too large");
        const auto child = static_cast<std::uint32_t>(nodes.size());
        nodes.push_back({h, index, static_cast<std::uint8_t>(v)});
        queue.push_back(child);
      }
    }
    if (processed % 100000 == 0)
      std::cerr << "processed=" << processed << " discovered=" << seen.size()
                << " queue=" << queue.size() << '\n' << std::flush;
  }

  std::ofstream out(path, std::ios::binary);
  if (!out) throw std::runtime_error("cannot open certificate output");
  out.write("LC13ORB2", 8);
  write_u64_le(out, nodes.size());
  for (const Node &node : nodes) {
    write_u64_le(out, node.graph.key.lo);
    write_u16_le(out, static_cast<std::uint16_t>(node.graph.key.hi));
    write_u32_le(out, node.parent);
    out.put(static_cast<char>(node.move));
  }
  out.close();
  if (!out) throw std::runtime_error("failed while writing certificate");
  std::cout << "certificate graph6=" << encode_graph6(start)
            << " orbit_size=" << nodes.size() << " processed=" << processed
            << " path=" << path << " status=PASS_CLOSED_ORBIT\n";
}

void print_result(const std::string &label, const Graph &g,
                  const TrialResult &r) {
  std::cout << label << " graph6=" << encode_graph6(g)
            << " discovered=" << r.discovered
            << " processed=" << r.processed;
  if (r.status == TrialResult::Status::pass) {
    std::cout << " status=PASS_CLOSED_ORBIT";
  } else if (r.status == TrialResult::Status::cap) {
    std::cout << " status=SURVIVED_CAP";
  } else {
    std::cout << " status=FAIL independent_set=";
    for (int v = 0; v < N; ++v)
      if ((r.independent_set >> v) & 1) std::cout << v << ',';
    std::cout << " failing_graph6=" << encode_graph6(r.failing_graph);
  }
  std::cout << '\n' << std::flush;
}

Graph paley13() {
  Key key;
  constexpr std::array<bool, 13> residue =
      {false, true, false, true, true, false, false,
       false, false, true, true, false, true};
  for (int j = 1; j < N; ++j)
    for (int i = 0; i < j; ++i)
      if (residue[(j - i + N) % N]) flip(key, edge_pos[i][j]);
  return from_key(key);
}

Graph random_graph(std::mt19937_64 &rng) {
  Key key{rng(), rng() & ((1ULL << (E - 64)) - 1)};
  return from_key(key);
}

}  // namespace

int main(int argc, char **argv) {
  try {
    initialize_tables();
    if (argc < 2) {
      std::cerr << "usage: lc13_search paley CAP | graph6 STRING CAP | "
                   "random TRIALS CAP SEED | certify STRING OUTPUT\n";
      return 2;
    }
    const std::string mode = argv[1];
    if (mode == "paley" && argc == 3) {
      Graph g = paley13();
      auto r = orbit_trial(g, std::stoull(argv[2]), true);
      print_result("paley13", g, r);
    } else if (mode == "graph6" && argc == 4) {
      Graph g = decode_graph6(argv[2]);
      auto r = orbit_trial(g, std::stoull(argv[3]), true);
      print_result("input", g, r);
    } else if (mode == "random" && argc == 5) {
      const std::size_t trials = std::stoull(argv[2]);
      const std::size_t cap = std::stoull(argv[3]);
      const std::uint64_t seed = std::stoull(argv[4]);
      std::mt19937_64 rng(seed);
      std::size_t best = 0;
      for (std::size_t t = 1; t <= trials; ++t) {
        Graph g = random_graph(rng);
        auto r = orbit_trial(g, cap, false);
        if (r.discovered > best || r.status != TrialResult::Status::fail) {
          best = r.discovered;
          print_result("random_trial=" + std::to_string(t), g, r);
        }
        if (r.status != TrialResult::Status::fail) return 0;
      }
      std::cout << "random_complete trials=" << trials << " cap=" << cap
                << " seed=" << seed << " best_discovered=" << best << '\n';
    } else if (mode == "certify" && argc == 4) {
      Graph g = decode_graph6(argv[2]);
      certify_to_file(g, argv[3]);
    } else {
      throw std::invalid_argument("invalid arguments");
    }
  } catch (const std::exception &e) {
    std::cerr << "error: " << e.what() << '\n';
    return 2;
  }
}
