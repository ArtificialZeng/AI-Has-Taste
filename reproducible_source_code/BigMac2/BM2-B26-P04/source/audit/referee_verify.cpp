#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

namespace {

constexpr int N = 13;
constexpr int EDGE_COUNT = N * (N - 1) / 2;

struct State {
  std::uint64_t lo{};
  std::uint16_t hi{};
  bool operator==(const State&) const = default;
};

struct StateHash {
  std::size_t operator()(const State& s) const noexcept {
    std::uint64_t x = s.lo ^ (std::uint64_t{s.hi} << 17);
    x ^= x >> 33;
    x *= 0xff51afd7ed558ccdULL;
    x ^= x >> 33;
    return static_cast<std::size_t>(x);
  }
};

struct Node {
  State state;
  std::uint32_t parent{};
  std::uint8_t move{};
};

std::array<std::array<int, N>, N> positions{};

void initialize_positions() {
  for (auto& row : positions) row.fill(-1);
  int position = 0;
  for (int right = 1; right < N; ++right) {
    for (int left = 0; left < right; ++left) {
      positions[left][right] = positions[right][left] = position++;
    }
  }
  if (position != EDGE_COUNT) throw std::logic_error("bad edge indexing");
}

bool edge(const State& state, int u, int v) {
  const int position = positions[u][v];
  if (position < 64) return ((state.lo >> position) & 1U) != 0;
  return ((state.hi >> (position - 64)) & 1U) != 0;
}

void toggle(State& state, int u, int v) {
  const int position = positions[u][v];
  if (position < 64) state.lo ^= std::uint64_t{1} << position;
  else state.hi ^= static_cast<std::uint16_t>(1U << (position - 64));
}

State local_complement(const State& state, int vertex) {
  State result = state;
  std::array<int, N> neighbors{};
  int degree = 0;
  for (int u = 0; u < N; ++u) {
    if (u != vertex && edge(state, vertex, u)) neighbors[degree++] = u;
  }
  for (int a = 0; a < degree; ++a) {
    for (int b = a + 1; b < degree; ++b) {
      toggle(result, neighbors[a], neighbors[b]);
    }
  }
  return result;
}

std::uint64_t read_unsigned(std::istream& input, int bytes) {
  std::uint64_t value = 0;
  for (int i = 0; i < bytes; ++i) {
    const int byte = input.get();
    if (byte == std::char_traits<char>::eof()) throw std::runtime_error("truncated certificate");
    value |= std::uint64_t{static_cast<unsigned char>(byte)} << (8 * i);
  }
  return value;
}

State decode_graph6(const std::string& graph6) {
  if (graph6.size() != 14 || static_cast<unsigned char>(graph6.front()) - 63 != N) {
    throw std::runtime_error("graph6 order or length mismatch");
  }
  State state;
  for (int position = 0; position < EDGE_COUNT; ++position) {
    const int value = static_cast<unsigned char>(graph6[1 + position / 6]) - 63;
    if (value < 0 || value > 63) throw std::runtime_error("invalid graph6 byte");
    if ((value >> (5 - position % 6)) & 1) {
      const int right = [&] {
        int p = 0;
        for (int j = 1; j < N; ++j) {
          for (int i = 0; i < j; ++i, ++p) if (p == position) return j;
        }
        return -1;
      }();
      int p = 0;
      int left = -1;
      for (int j = 1; j <= right && left < 0; ++j) {
        for (int i = 0; i < j; ++i, ++p) if (p == position) { left = i; break; }
      }
      toggle(state, left, right);
    }
  }
  return state;
}

std::pair<std::uint64_t, std::uint16_t> induced_edge_mask(const std::vector<int>& vertices) {
  State mask;
  for (std::size_t i = 0; i < vertices.size(); ++i) {
    for (std::size_t j = i + 1; j < vertices.size(); ++j) toggle(mask, vertices[i], vertices[j]);
  }
  return {mask.lo, mask.hi};
}

void combinations(int next, int need, std::vector<int>& chosen,
                  std::vector<std::pair<std::uint64_t, std::uint16_t>>& masks) {
  if (need == 0) {
    masks.push_back(induced_edge_mask(chosen));
    return;
  }
  for (int v = next; v <= N - need; ++v) {
    chosen.push_back(v);
    combinations(v + 1, need - 1, chosen, masks);
    chosen.pop_back();
  }
}

bool is_paley13(const State& state) {
  const std::array<bool, 13> residue =
      {false, true, false, true, true, false, false, false, false, true, true, false, true};
  for (int i = 0; i < N; ++i) {
    for (int j = i + 1; j < N; ++j) {
      if (edge(state, i, j) != residue[(j - i + N) % N]) return false;
    }
  }
  return true;
}

}  // namespace

int main(int argc, char** argv) {
  try {
    if (argc != 3) throw std::runtime_error("usage: referee_verify GRAPH6 ORBIT");
    initialize_positions();
    const State candidate = decode_graph6(argv[1]);
    if (!is_paley13(candidate)) throw std::runtime_error("graph6 is not P(13)");

    std::ifstream input(argv[2], std::ios::binary);
    if (!input) throw std::runtime_error("cannot open certificate");
    std::array<char, 8> magic{};
    input.read(magic.data(), magic.size());
    if (std::string(magic.data(), magic.size()) != "LC13ORB2") throw std::runtime_error("bad magic");
    const std::uint64_t count = read_unsigned(input, 8);
    std::vector<Node> nodes;
    nodes.reserve(count);
    for (std::uint64_t i = 0; i < count; ++i) {
      Node node;
      node.state.lo = read_unsigned(input, 8);
      node.state.hi = static_cast<std::uint16_t>(read_unsigned(input, 2));
      node.parent = static_cast<std::uint32_t>(read_unsigned(input, 4));
      node.move = static_cast<std::uint8_t>(read_unsigned(input, 1));
      if (node.state.hi >= (1U << (EDGE_COUNT - 64))) throw std::runtime_error("out-of-domain high bit");
      nodes.push_back(node);
    }
    if (input.peek() != std::char_traits<char>::eof()) throw std::runtime_error("trailing certificate bytes");
    if (count != 711440) throw std::runtime_error("claimed orbit size mismatch");
    if (!(nodes.front().state == candidate)) throw std::runtime_error("root mismatch");
    if (nodes.front().parent != UINT32_MAX || nodes.front().move != UINT8_MAX) throw std::runtime_error("root sentinel mismatch");

    std::unordered_set<State, StateHash> states;
    states.reserve(count * 2);
    for (const Node& node : nodes) {
      if (!states.insert(node.state).second) throw std::runtime_error("duplicate state");
    }

    std::uint32_t previous_parent = 0;
    for (std::uint64_t i = 1; i < count; ++i) {
      const Node& node = nodes[i];
      if (node.parent >= i || node.move >= N) throw std::runtime_error("invalid discovery record");
      if (node.parent < previous_parent) throw std::runtime_error("discovery order is not FIFO-compatible");
      previous_parent = node.parent;
      if (!(local_complement(nodes[node.parent].state, node.move) == node.state)) {
        throw std::runtime_error("false discovery edge");
      }
    }

    std::uint64_t closure_moves = 0;
    for (const Node& node : nodes) {
      for (int vertex = 0; vertex < N; ++vertex) {
        if (!states.contains(local_complement(node.state, vertex))) throw std::runtime_error("orbit is not closed");
        ++closure_moves;
      }
    }

    std::vector<int> chosen;
    std::vector<std::pair<std::uint64_t, std::uint16_t>> five_masks;
    combinations(0, 5, chosen, five_masks);
    if (five_masks.size() != 1287) throw std::runtime_error("bad five-subset enumeration");
    std::uint64_t alpha_checks = 0;
    for (const Node& node : nodes) {
      for (const auto& [lo, hi] : five_masks) {
        ++alpha_checks;
        if ((node.state.lo & lo) == 0 && (node.state.hi & hi) == 0) {
          throw std::runtime_error("independent five-set found");
        }
      }
    }

    const State& state834 = nodes.at(834).state;
    const auto four_mask = induced_edge_mask({0, 1, 2, 3});
    if ((state834.lo & four_mask.first) != 0 || (state834.hi & four_mask.second) != 0) {
      throw std::runtime_error("claimed independent four-set is not independent");
    }

    std::cout << "verdict=PASS"
              << " orbit_size=" << count
              << " unique_states=" << states.size()
              << " tree_edges=" << count - 1
              << " closure_moves=" << closure_moves
              << " five_subsets=" << five_masks.size()
              << " alpha_checks=" << alpha_checks
              << " independent_four_state=834"
              << " independent_four_vertices=0,1,2,3"
              << " candidate_is_paley13=true\n";
    return 0;
  } catch (const std::exception& error) {
    std::cerr << "verdict=FAIL reason=" << error.what() << '\n';
    return 1;
  }
}
