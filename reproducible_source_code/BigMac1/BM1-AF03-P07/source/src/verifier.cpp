#include <algorithm>
#include <array>
#include <bit>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <thread>
#include <utility>
#include <vector>

// Independent verifier for the finite K-Knuth shape-interval certificate.
//
// Independence boundary:
//   * this file does not include discovery.cpp and reads no discovery state;
//   * tableaux are encoded cell-by-cell in an 80-bit diagonal-dependent code,
//     rather than by row bitsets;
//   * enumeration is shape-first, then row-major filling, rather than adding
//     equal-letter rook strips;
//   * interval convexity is checked as Up(S) intersect Down(S) subset S using
//     bitsets, rather than enumerating each endpoint interval recursively.

namespace audit {

struct Code {
  std::uint64_t lo = 0;
  std::uint64_t hi = 0;
  friend bool operator==(const Code&, const Code&) = default;
  friend bool operator<(const Code& a, const Code& b) {
    return a.hi < b.hi || (a.hi == b.hi && a.lo < b.lo);
  }
};

struct Grid {
  std::array<std::array<std::uint8_t, 8>, 8> a{};
  std::array<std::uint8_t, 8> length{};
};

struct Codec {
  std::array<std::array<unsigned, 8>, 8> offset{};
  std::array<std::array<unsigned, 8>, 8> width{};
  unsigned bits = 0;

  Codec() {
    for (unsigned r = 0; r < 8; ++r) {
      for (unsigned c = 0; c < 8 - r; ++c) {
        const unsigned diagonal = r + c + 1;
        const unsigned choices = 10 - diagonal;  // absent plus diagonal..8.
        unsigned w = 0;
        while ((1U << w) < choices) ++w;
        offset[r][c] = bits;
        width[r][c] = w;
        bits += w;
      }
    }
    if (bits != 80) throw std::runtime_error("unexpected independent code width");
  }

  Code encode(const Grid& grid) const {
    unsigned __int128 z = 0;
    for (unsigned r = 0; r < 8; ++r) {
      for (unsigned c = 0; c < grid.length[r]; ++c) {
        const unsigned value = grid.a[r][c];
        const unsigned diagonal = r + c + 1;
        if (value < diagonal || value > 8) {
          throw std::runtime_error("cell outside codec range");
        }
        const unsigned digit = value - diagonal + 1;
        z |= static_cast<unsigned __int128>(digit) << offset[r][c];
      }
    }
    return {static_cast<std::uint64_t>(z), static_cast<std::uint64_t>(z >> 64)};
  }

  Grid decode(Code code) const {
    const unsigned __int128 z =
        static_cast<unsigned __int128>(code.lo) |
        (static_cast<unsigned __int128>(code.hi) << 64);
    Grid grid;
    bool shape_ended = false;
    unsigned previous_length = 8;
    for (unsigned r = 0; r < 8; ++r) {
      unsigned length = 0;
      for (unsigned c = 0; c < 8 - r; ++c) {
        const unsigned mask = (1U << width[r][c]) - 1U;
        const unsigned digit = static_cast<unsigned>((z >> offset[r][c]) & mask);
        if (digit == 0) {
          for (unsigned d = c + 1; d < 8 - r; ++d) {
            const unsigned later_mask = (1U << width[r][d]) - 1U;
            if (((z >> offset[r][d]) & later_mask) != 0) {
              throw std::runtime_error("non-left-justified encoded shape");
            }
          }
          break;
        }
        grid.a[r][c] = static_cast<std::uint8_t>(r + c + digit);
        ++length;
      }
      grid.length[r] = static_cast<std::uint8_t>(length);
      if (length == 0) shape_ended = true;
      if (shape_ended && length != 0) throw std::runtime_error("non-straight encoded shape");
      if (length > previous_length) throw std::runtime_error("encoded shape is not a partition");
      previous_length = length;
    }
    return grid;
  }
};

static bool valid(const Grid& g, unsigned n) {
  if (n > 8) return false;
  bool ended = false;
  unsigned previous = n;
  for (unsigned r = 0; r < 8; ++r) {
    const unsigned length = g.length[r];
    if (r < n) {
      if (length > n - r || length > previous) return false;
    } else if (length != 0) {
      return false;
    }
    if (length == 0) ended = true;
    if (ended && length != 0) return false;
    for (unsigned c = 0; c < length; ++c) {
      const unsigned value = g.a[r][c];
      if (value == 0 || value > n || value < r + c + 1) return false;
      if (c > 0 && g.a[r][c - 1] >= value) return false;
      if (r > 0 && g.a[r - 1][c] >= value) return false;
    }
    previous = length;
  }
  return true;
}

static Grid insert(Grid g, unsigned letter, unsigned n) {
  if (!valid(g, n) || letter == 0 || letter > n) {
    throw std::runtime_error("invalid independent insertion input");
  }
  unsigned carry = letter;
  for (unsigned r = 0; r < n && carry != 0; ++r) {
    unsigned c = 0;
    while (c < g.length[r] && g.a[r][c] <= carry) ++c;
    if (c < g.length[r]) {
      const unsigned bumped = g.a[r][c];
      bool replace = (c == 0 || g.a[r][c - 1] < carry);
      if (r > 0) replace = replace && c < g.length[r - 1] && g.a[r - 1][c] < carry;
      if (replace) g.a[r][c] = static_cast<std::uint8_t>(carry);
      carry = bumped;
    } else {
      bool append = (c == 0 || g.a[r][c - 1] < carry);
      if (r > 0) append = append && g.length[r - 1] > c && g.a[r - 1][c] < carry;
      if (append) {
        g.a[r][c] = static_cast<std::uint8_t>(carry);
        ++g.length[r];
      }
      carry = 0;
    }
  }
  if (!valid(g, n)) throw std::runtime_error("independent insertion broke tableau validity");
  return g;
}

static std::uint32_t shape_code(const Grid& g) {
  std::uint32_t code = 0;
  for (unsigned r = 0; r < 8; ++r) code |= unsigned(g.length[r]) << (4 * r);
  return code;
}

static bool is_initial(const Grid& g, unsigned n) {
  unsigned seen = 0;
  for (unsigned r = 0; r < n; ++r) {
    for (unsigned c = 0; c < g.length[r]; ++c) seen |= 1U << (g.a[r][c] - 1);
  }
  const unsigned expected = n == 8 ? 0xffU : ((1U << n) - 1U);
  return seen == expected;
}

struct ShapeFirstEnumeration {
  unsigned n;
  const Codec& codec;
  std::vector<Code> tableaus;
  std::vector<std::uint32_t> shapes;
  Grid grid;

  ShapeFirstEnumeration(unsigned alphabet, const Codec& c) : n(alphabet), codec(c) {
    choose_shape(0, n);
    std::sort(tableaus.begin(), tableaus.end());
    if (std::adjacent_find(tableaus.begin(), tableaus.end()) != tableaus.end()) {
      throw std::runtime_error("duplicate in shape-first enumeration");
    }
    std::sort(shapes.begin(), shapes.end());
    shapes.erase(std::unique(shapes.begin(), shapes.end()), shapes.end());
  }

  void choose_shape(unsigned row, unsigned previous) {
    if (row == n) {
      shapes.push_back(shape_code(grid));
      std::vector<std::pair<unsigned, unsigned>> cells;
      for (unsigned r = 0; r < n; ++r) {
        for (unsigned c = 0; c < grid.length[r]; ++c) cells.emplace_back(r, c);
      }
      fill(cells, 0);
      return;
    }
    const unsigned maximum = std::min(previous, n - row);
    for (unsigned length = 0; length <= maximum; ++length) {
      grid.length[row] = static_cast<std::uint8_t>(length);
      choose_shape(row + 1, length);
    }
    grid.length[row] = 0;
  }

  void fill(const std::vector<std::pair<unsigned, unsigned>>& cells, std::size_t at) {
    if (at == cells.size()) {
      if (!valid(grid, n)) throw std::runtime_error("shape-first generator made invalid tableau");
      tableaus.push_back(codec.encode(grid));
      return;
    }
    const auto [r, c] = cells[at];
    unsigned lower = r + c + 1;
    if (c > 0) lower = std::max(lower, unsigned(grid.a[r][c - 1]) + 1);
    if (r > 0) lower = std::max(lower, unsigned(grid.a[r - 1][c]) + 1);
    for (unsigned value = lower; value <= n; ++value) {
      grid.a[r][c] = static_cast<std::uint8_t>(value);
      fill(cells, at + 1);
    }
    grid.a[r][c] = 0;
  }
};

struct Dictionary {
  static constexpr std::uint64_t empty_word = std::numeric_limits<std::uint64_t>::max();
  std::vector<Code> slots;
  std::vector<std::uint32_t> ids;
  std::size_t mask;

  static std::uint64_t avalanche(std::uint64_t x) {
    x ^= x >> 33;
    x *= 0xff51afd7ed558ccdULL;
    x ^= x >> 33;
    x *= 0xc4ceb9fe1a85ec53ULL;
    return x ^ (x >> 33);
  }

  explicit Dictionary(const std::vector<Code>& keys) {
    std::size_t capacity = 1;
    while (capacity * 2 < keys.size() * 3) capacity <<= 1;
    slots.assign(capacity, Code{empty_word, empty_word});
    ids.resize(capacity);
    mask = capacity - 1;
    for (std::uint32_t id = 0; id < keys.size(); ++id) {
      std::size_t p = avalanche(keys[id].lo ^ std::rotl(keys[id].hi, 17)) & mask;
      while (slots[p].lo != empty_word) p = (p + 1) & mask;
      slots[p] = keys[id];
      ids[p] = id;
    }
  }

  std::uint32_t lookup(Code key) const {
    std::size_t p = avalanche(key.lo ^ std::rotl(key.hi, 17)) & mask;
    while (slots[p].lo != empty_word) {
      if (slots[p] == key) return ids[p];
      p = (p + 1) & mask;
    }
    throw std::runtime_error("insertion target not found by independent dictionary");
  }
};

static std::vector<std::uint32_t> transition_table(
    const std::vector<Code>& states, const Codec& codec, unsigned n) {
  Dictionary dictionary(states);
  std::vector<std::uint32_t> transition(states.size() * n);
  const unsigned threads = std::min(12U, std::max(1U, std::thread::hardware_concurrency()));
  std::vector<std::thread> jobs;
  for (unsigned t = 0; t < threads; ++t) {
    const std::size_t first = states.size() * t / threads;
    const std::size_t last = states.size() * (t + 1) / threads;
    jobs.emplace_back([&, first, last]() {
      for (std::size_t id = first; id < last; ++id) {
        const Grid original = codec.decode(states[id]);
        if (!valid(original, n)) throw std::runtime_error("invalid decoded canonical state");
        for (unsigned letter = 1; letter <= n; ++letter) {
          transition[id * n + letter - 1] =
              dictionary.lookup(codec.encode(insert(original, letter, n)));
        }
      }
    });
  }
  for (auto& job : jobs) job.join();
  return transition;
}

struct UnionFind {
  std::vector<std::int32_t> link;
  explicit UnionFind(std::size_t n) : link(n, -1) {}
  std::uint32_t root(std::uint32_t x) {
    if (link[x] < 0) return x;
    return static_cast<std::uint32_t>(link[x] = static_cast<std::int32_t>(root(link[x])));
  }
  bool join(std::uint32_t x, std::uint32_t y) {
    x = root(x);
    y = root(y);
    if (x == y) return false;
    if (link[x] > link[y]) std::swap(x, y);
    link[x] += link[y];
    link[y] = static_cast<std::int32_t>(x);
    return true;
  }
};

struct Rule {
  std::array<std::uint8_t, 3> left{};
  std::array<std::uint8_t, 3> right{};
  std::uint8_t left_length = 0;
  std::uint8_t right_length = 0;
};

static std::vector<Rule> primitive_rules(unsigned n) {
  std::vector<Rule> rules;
  for (unsigned p = 1; p <= n; ++p) {
    Rule r;
    r.left[0] = p;
    r.right[0] = p;
    r.right[1] = p;
    r.left_length = 1;
    r.right_length = 2;
    rules.push_back(r);
  }
  for (unsigned p = 1; p <= n; ++p) {
    for (unsigned q = p + 1; q <= n; ++q) {
      Rule r;
      r.left = {std::uint8_t(p), std::uint8_t(q), std::uint8_t(p)};
      r.right = {std::uint8_t(q), std::uint8_t(p), std::uint8_t(q)};
      r.left_length = r.right_length = 3;
      rules.push_back(r);
    }
  }
  for (unsigned x = 1; x <= n; ++x) {
    for (unsigned y = x + 1; y <= n; ++y) {
      for (unsigned z = y + 1; z <= n; ++z) {
        Rule first;
        first.left = {std::uint8_t(x), std::uint8_t(z), std::uint8_t(y)};
        first.right = {std::uint8_t(z), std::uint8_t(x), std::uint8_t(y)};
        first.left_length = first.right_length = 3;
        rules.push_back(first);
        Rule second;
        second.left = {std::uint8_t(y), std::uint8_t(x), std::uint8_t(z)};
        second.right = {std::uint8_t(y), std::uint8_t(z), std::uint8_t(x)};
        second.left_length = second.right_length = 3;
        rules.push_back(second);
      }
    }
  }
  return rules;
}

struct Components {
  UnionFind uf;
  std::vector<std::pair<std::uint32_t, std::uint32_t>> work;
  std::uint64_t primitive_tests = 0;
  std::uint64_t closure_tests = 0;

  Components(std::size_t count, const std::vector<std::uint32_t>& transition, unsigned n)
      : uf(count) {
    const auto rules = primitive_rules(n);
    work.reserve(count - 1);
    const auto advance = [&](std::uint32_t s, unsigned letter) {
      return transition[std::size_t(s) * n + letter - 1];
    };
    const auto word = [&](std::uint32_t s, const std::array<std::uint8_t, 3>& w,
                          unsigned length) {
      for (unsigned i = 0; i < length; ++i) s = advance(s, w[i]);
      return s;
    };
    const auto join = [&](std::uint32_t a, std::uint32_t b) {
      if (uf.join(a, b)) work.emplace_back(a, b);
    };
    for (std::uint32_t state = 0; state < count; ++state) {
      for (const auto& rule : rules) {
        join(word(state, rule.left, rule.left_length),
             word(state, rule.right, rule.right_length));
        ++primitive_tests;
      }
    }
    for (std::size_t head = 0; head < work.size(); ++head) {
      for (unsigned letter = 1; letter <= n; ++letter) {
        join(advance(work[head].first, letter), advance(work[head].second, letter));
        ++closure_tests;
      }
    }
  }
};

static std::array<unsigned, 8> unpack_shape(std::uint32_t s) {
  std::array<unsigned, 8> row{};
  for (unsigned r = 0; r < 8; ++r) row[r] = (s >> (4 * r)) & 15U;
  return row;
}

static bool contained(std::uint32_t lower, std::uint32_t upper, unsigned n) {
  const auto x = unpack_shape(lower);
  const auto y = unpack_shape(upper);
  for (unsigned r = 0; r < n; ++r) if (x[r] > y[r]) return false;
  return true;
}

struct Summary {
  std::uint64_t all = 0;
  std::uint64_t initial = 0;
  std::uint64_t classes = 0;
  std::uint64_t urts = 0;
  std::uint64_t rules = 0;
  std::uint64_t primitive_tests = 0;
  std::uint64_t closure_tests = 0;
  std::uint64_t merges = 0;
  bool convex = true;
  std::uint32_t lower = 0, middle = 0, upper = 0;
};

static Summary verify(unsigned n) {
  Codec codec;
  ShapeFirstEnumeration enumeration(n, codec);
  auto transition = transition_table(enumeration.tableaus, codec, n);
  Components components(enumeration.tableaus.size(), transition, n);
  std::vector<std::uint32_t>().swap(transition);

  Summary answer;
  answer.all = enumeration.tableaus.size();
  answer.rules = primitive_rules(n).size();
  answer.primitive_tests = components.primitive_tests;
  answer.closure_tests = components.closure_tests;
  answer.merges = components.work.size();
  std::vector<std::uint32_t> sizes(answer.all, 0);
  std::vector<std::uint64_t> root_shape;
  for (std::uint32_t id = 0; id < enumeration.tableaus.size(); ++id) {
    const Grid g = codec.decode(enumeration.tableaus[id]);
    if (!is_initial(g, n)) continue;
    ++answer.initial;
    const std::uint32_t root = components.uf.root(id);
    ++sizes[root];
    root_shape.push_back((std::uint64_t(root) << 32) | shape_code(g));
  }
  for (const unsigned size : sizes) {
    if (size != 0) {
      ++answer.classes;
      answer.urts += size == 1;
    }
  }
  std::vector<std::uint32_t>().swap(sizes);
  std::sort(root_shape.begin(), root_shape.end());
  root_shape.erase(std::unique(root_shape.begin(), root_shape.end()), root_shape.end());

  const auto& universe = enumeration.shapes;
  const std::size_t words = (universe.size() + 63) / 64;
  std::vector<std::uint64_t> upward(universe.size() * words, 0);
  std::vector<std::uint64_t> downward(universe.size() * words, 0);
  for (std::size_t i = 0; i < universe.size(); ++i) {
    for (std::size_t j = 0; j < universe.size(); ++j) {
      if (contained(universe[i], universe[j], n)) {
        upward[i * words + j / 64] |= 1ULL << (j % 64);
        downward[j * words + i / 64] |= 1ULL << (i % 64);
      }
    }
  }
  std::vector<std::uint64_t> has_lower(words), has_upper(words), members(words);
  for (std::size_t begin = 0; begin < root_shape.size();) {
    std::size_t end = begin + 1;
    const std::uint32_t root = root_shape[begin] >> 32;
    while (end < root_shape.size() && std::uint32_t(root_shape[end] >> 32) == root) ++end;
    if (end - begin > 1) {
      std::fill(has_lower.begin(), has_lower.end(), 0);
      std::fill(has_upper.begin(), has_upper.end(), 0);
      std::fill(members.begin(), members.end(), 0);
      std::vector<std::uint32_t> component_shapes;
      for (std::size_t k = begin; k < end; ++k) {
        const std::uint32_t shape = root_shape[k];
        component_shapes.push_back(shape);
        const auto it = std::lower_bound(universe.begin(), universe.end(), shape);
        if (it == universe.end() || *it != shape) throw std::runtime_error("shape outside universe");
        const std::size_t index = it - universe.begin();
        members[index / 64] |= 1ULL << (index % 64);
        for (std::size_t w = 0; w < words; ++w) {
          has_lower[w] |= upward[index * words + w];
          has_upper[w] |= downward[index * words + w];
        }
      }
      for (std::size_t w = 0; w < words; ++w) {
        std::uint64_t bad = has_lower[w] & has_upper[w] & ~members[w];
        if (bad != 0) {
          const std::size_t middle_index = 64 * w + std::countr_zero(bad);
          if (middle_index >= universe.size()) throw std::runtime_error("padding bit set");
          answer.convex = false;
          answer.middle = universe[middle_index];
          for (const auto s : component_shapes) {
            if (contained(s, answer.middle, n)) answer.lower = s;
            if (contained(answer.middle, s, n)) answer.upper = s;
          }
          if (answer.lower == 0 || answer.upper == 0) {
            throw std::runtime_error("closure witness lacks endpoints");
          }
          return answer;
        }
      }
    }
    begin = end;
  }
  return answer;
}

static void insertion_self_test() {
  Codec codec;
  Grid a;
  a.length = {4, 4, 1, 1, 0, 0, 0, 0};
  a.a[0] = {1, 2, 3, 5, 0, 0, 0, 0};
  a.a[1] = {2, 3, 4, 6, 0, 0, 0, 0};
  a.a[2][0] = 6;
  a.a[3][0] = 7;
  if (!(codec.encode(insert(a, 3, 8)) == codec.encode(a))) {
    throw std::runtime_error("published insertion Example 2.8 failed");
  }
  Grid b;
  b.length = {3, 3, 1, 0, 0, 0, 0, 0};
  b.a[0] = {2, 4, 6, 0, 0, 0, 0, 0};
  b.a[1] = {3, 6, 8, 0, 0, 0, 0, 0};
  b.a[2][0] = 7;
  Grid expected = b;
  expected.a[0] = {2, 4, 5, 0, 0, 0, 0, 0};
  expected.length[2] = 2;
  expected.a[2][1] = 8;
  if (!(codec.encode(insert(b, 5, 8)) == codec.encode(expected))) {
    throw std::runtime_error("published insertion Example 2.9 failed");
  }
}

}  // namespace audit

int main(int argc, char** argv) {
  try {
    unsigned n = 8;
    if (argc == 3 && std::string(argv[1]) == "--n") {
      n = static_cast<unsigned>(std::stoul(argv[2]));
    } else if (argc != 1) {
      throw std::runtime_error("usage: verifier_core [--n N]");
    }
    if (n > 8) throw std::runtime_error("certificate endpoint must satisfy 0 <= n <= 8");
    audit::insertion_self_test();
    const auto start = std::chrono::steady_clock::now();
    const audit::Summary s = audit::verify(n);
    const auto stop = std::chrono::steady_clock::now();
    std::cout << "{\"n\":" << n
              << ",\"all_tableaux\":" << s.all
              << ",\"initial_tableaux\":" << s.initial
              << ",\"initial_classes\":" << s.classes
              << ",\"urts\":" << s.urts
              << ",\"primitive_rule_count\":" << s.rules
              << ",\"primitive_tests\":" << s.primitive_tests
              << ",\"closure_tests\":" << s.closure_tests
              << ",\"merges\":" << s.merges
              << ",\"interval_complete\":" << (s.convex ? "true" : "false")
              << ",\"seconds\":"
              << std::chrono::duration<double>(stop - start).count() << "}\n";
    return s.convex ? 0 : 2;
  } catch (const std::exception& ex) {
    std::cerr << "VERIFIER_REJECT: " << ex.what() << "\n";
    return 1;
  }
}
