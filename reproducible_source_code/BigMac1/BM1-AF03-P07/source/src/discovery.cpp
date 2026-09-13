#include <algorithm>
#include <array>
#include <bit>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <queue>
#include <stdexcept>
#include <string>
#include <thread>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

// Discovery implementation of Gaetz--Mastrianni--Patrias--Peck--Robichaux--
// Schwein--Tam Algorithm 1.  A tableau on [n], n <= 8, is encoded by eight
// bytes: byte r is the bit-set of entries in row r.  Strict row increase makes
// this encoding lossless.  The independent verifier does not import this file.

namespace kk {

using Key = std::uint64_t;

static unsigned row_len(std::uint8_t mask) {
  return std::popcount(static_cast<unsigned>(mask));
}

static unsigned kth_entry(std::uint8_t mask, unsigned k) {
  // Zero-based order statistic; fail closed if k is out of range.
  while (mask != 0) {
    const unsigned bit = std::countr_zero(static_cast<unsigned>(mask));
    if (k == 0) return bit + 1;
    mask = static_cast<std::uint8_t>(mask & (mask - 1));
    --k;
  }
  throw std::runtime_error("kth_entry out of range");
}

static std::array<std::uint8_t, 8> unpack(Key key) {
  std::array<std::uint8_t, 8> rows{};
  for (unsigned r = 0; r < 8; ++r) {
    rows[r] = static_cast<std::uint8_t>((key >> (8 * r)) & 0xffU);
  }
  return rows;
}

static Key pack(const std::array<std::uint8_t, 8>& rows) {
  Key key = 0;
  for (unsigned r = 0; r < 8; ++r) {
    key |= static_cast<Key>(rows[r]) << (8 * r);
  }
  return key;
}

static bool valid_tableau(Key key, unsigned n) {
  if (n > 8) return false;
  const auto rows = unpack(key);
  const unsigned allowed = n == 8 ? 0xffU : ((1U << n) - 1U);
  bool seen_empty = false;
  unsigned previous_length = n;
  for (unsigned r = 0; r < 8; ++r) {
    if ((rows[r] & ~allowed) != 0) return false;
    const unsigned length = row_len(rows[r]);
    if (length == 0) seen_empty = true;
    if (seen_empty && length != 0) return false;
    if (length > previous_length) return false;
    if (r > 0) {
      for (unsigned c = 0; c < length; ++c) {
        if (kth_entry(rows[r - 1], c) >= kth_entry(rows[r], c)) return false;
      }
    }
    previous_length = length;
  }
  return true;
}

static Key insert_letter(Key key, unsigned x, unsigned n) {
  if (x == 0 || x > n || n > 8 || !valid_tableau(key, n)) {
    throw std::runtime_error("invalid insert_letter input");
  }
  auto rows = unpack(key);
  unsigned carry = x;
  for (unsigned r = 0; r < n && carry != 0; ++r) {
    const std::uint8_t mask = rows[r];
    const unsigned low_through_carry = (1U << carry) - 1U;
    const std::uint8_t greater =
        static_cast<std::uint8_t>(mask & static_cast<std::uint8_t>(~low_through_carry));
    if (greater != 0) {
      const unsigned y = std::countr_zero(static_cast<unsigned>(greater)) + 1;
      const unsigned position =
          std::popcount(static_cast<unsigned>(mask) & ((1U << (y - 1)) - 1U));
      bool feasible = (mask & (1U << (carry - 1))) == 0;
      if (r > 0) {
        feasible = feasible && row_len(rows[r - 1]) > position &&
                   kth_entry(rows[r - 1], position) < carry;
      }
      if (feasible) {
        rows[r] = static_cast<std::uint8_t>(
            (mask & ~(1U << (y - 1))) | (1U << (carry - 1)));
      }
      carry = y;
    } else {
      const unsigned position = row_len(mask);
      bool feasible = (mask & (1U << (carry - 1))) == 0;
      if (r > 0) {
        feasible = feasible && row_len(rows[r - 1]) > position &&
                   kth_entry(rows[r - 1], position) < carry;
      }
      if (feasible) {
        rows[r] = static_cast<std::uint8_t>(mask | (1U << (carry - 1)));
      }
      carry = 0;  // Hecke insertion terminates in either append case.
    }
  }
  const Key result = pack(rows);
  if (!valid_tableau(result, n)) {
    throw std::runtime_error("insert_letter produced invalid tableau");
  }
  return result;
}

struct Enumeration {
  unsigned n = 0;
  std::vector<Key> states;

  void recurse(unsigned label, std::array<std::uint8_t, 8>& rows) {
    if (label > n) {
      states.push_back(pack(rows));
      return;
    }
    std::array<unsigned, 8> addable{};
    unsigned count = 0;
    addable[count++] = 0;
    unsigned row_count = 0;
    while (row_count < n && rows[row_count] != 0) ++row_count;
    for (unsigned r = 0; r < row_count; ++r) {
      if (row_len(rows[r]) > row_len(rows[r + 1])) addable[count++] = r + 1;
    }
    const unsigned choices = 1U << count;
    for (unsigned subset = 0; subset < choices; ++subset) {
      for (unsigned j = 0; j < count; ++j) {
        if ((subset >> j) & 1U) {
          rows[addable[j]] = static_cast<std::uint8_t>(
              rows[addable[j]] | (1U << (label - 1)));
        }
      }
      recurse(label + 1, rows);
      for (unsigned j = 0; j < count; ++j) {
        if ((subset >> j) & 1U) {
          rows[addable[j]] = static_cast<std::uint8_t>(
              rows[addable[j]] & ~(1U << (label - 1)));
        }
      }
    }
  }

  explicit Enumeration(unsigned alphabet) : n(alphabet) {
    if (n > 8) throw std::runtime_error("this encoding supports n <= 8");
    std::array<std::uint8_t, 8> rows{};
    recurse(1, rows);
    std::sort(states.begin(), states.end());
    if (std::adjacent_find(states.begin(), states.end()) != states.end()) {
      throw std::runtime_error("duplicate canonical tableau encoding");
    }
    for (const Key key : states) {
      if (!valid_tableau(key, n)) throw std::runtime_error("invalid enumerated tableau");
    }
  }
};

static bool initial(Key key, unsigned n) {
  const auto rows = unpack(key);
  unsigned letters = 0;
  for (const auto row : rows) letters |= row;
  const unsigned full = n == 8 ? 0xffU : ((1U << n) - 1U);
  return letters == full;
}

static std::uint32_t shape_code(Key key) {
  const auto rows = unpack(key);
  std::uint32_t shape = 0;
  for (unsigned r = 0; r < 8; ++r) shape |= row_len(rows[r]) << (4 * r);
  return shape;
}

static std::string key_string(Key key) {
  const auto rows = unpack(key);
  std::string out = "[";
  bool first_row = true;
  for (unsigned r = 0; r < 8 && rows[r] != 0; ++r) {
    if (!first_row) out += ",";
    first_row = false;
    out += "[";
    bool first = true;
    for (unsigned v = 1; v <= 8; ++v) {
      if ((rows[r] >> (v - 1)) & 1U) {
        if (!first) out += ",";
        first = false;
        out += std::to_string(v);
      }
    }
    out += "]";
  }
  out += "]";
  return out;
}

static void self_test() {
  // Paper Examples 2.8 and 2.9.
  const Key ex28 = pack({0x17, 0x2e, 0x20, 0x40, 0, 0, 0, 0});
  if (insert_letter(ex28, 3, 8) != ex28) throw std::runtime_error("Example 2.8 failed");
  const Key ex29 = pack({0x2a, 0xa4, 0x40, 0, 0, 0, 0, 0});
  const Key ex29_expected = pack({0x1a, 0xa4, 0xc0, 0, 0, 0, 0, 0});
  if (insert_letter(ex29, 5, 8) != ex29_expected) {
    throw std::runtime_error("Example 2.9 failed");
  }
  for (unsigned n = 0; n <= 5; ++n) {
    Enumeration enumeration(n);
    static constexpr std::uint64_t all_expected[] = {1, 2, 6, 26, 162, 1450};
    static constexpr std::uint64_t init_expected[] = {1, 1, 3, 13, 87, 849};
    std::uint64_t initial_count = 0;
    for (const Key key : enumeration.states) initial_count += initial(key, n);
    if (enumeration.states.size() != all_expected[n] || initial_count != init_expected[n]) {
      throw std::runtime_error("small enumeration baseline failed");
    }
  }
}

struct FlatIndex {
  static constexpr Key empty = std::numeric_limits<Key>::max();
  std::vector<Key> keys;
  std::vector<std::uint32_t> values;
  std::size_t mask = 0;

  static Key mix(Key x) {
    x += 0x9e3779b97f4a7c15ULL;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
    x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
    return x ^ (x >> 31);
  }

  explicit FlatIndex(const std::vector<Key>& states) {
    std::size_t capacity = 1;
    while (capacity * 7 < states.size() * 10) capacity <<= 1;
    keys.assign(capacity, empty);
    values.resize(capacity);
    mask = capacity - 1;
    for (std::uint32_t id = 0; id < states.size(); ++id) {
      std::size_t slot = static_cast<std::size_t>(mix(states[id])) & mask;
      while (keys[slot] != empty) slot = (slot + 1) & mask;
      keys[slot] = states[id];
      values[slot] = id;
    }
  }

  std::uint32_t at(Key key) const {
    std::size_t slot = static_cast<std::size_t>(mix(key)) & mask;
    while (keys[slot] != empty) {
      if (keys[slot] == key) return values[slot];
      slot = (slot + 1) & mask;
    }
    throw std::runtime_error("transition target absent from canonical enumeration");
  }
};

struct Dsu {
  std::vector<std::int32_t> parent;

  explicit Dsu(std::size_t size) : parent(size, -1) {
    if (size >= static_cast<std::size_t>(std::numeric_limits<std::int32_t>::max())) {
      throw std::runtime_error("DSU size exceeds int32 certificate format");
    }
  }

  std::uint32_t find(std::uint32_t x) {
    std::uint32_t root = x;
    while (parent[root] >= 0) root = static_cast<std::uint32_t>(parent[root]);
    while (x != root) {
      const std::uint32_t next = static_cast<std::uint32_t>(parent[x]);
      parent[x] = static_cast<std::int32_t>(root);
      x = next;
    }
    return root;
  }

  bool unite(std::uint32_t a, std::uint32_t b) {
    if (a == b) return false;
    a = find(a);
    b = find(b);
    if (a == b) return false;
    if (parent[a] > parent[b]) std::swap(a, b);  // a has at least b's size.
    parent[a] += parent[b];
    parent[b] = static_cast<std::int32_t>(a);
    return true;
  }
};

static std::vector<std::uint32_t> build_transitions(
    const std::vector<Key>& states, unsigned n) {
  FlatIndex index(states);
  std::vector<std::uint32_t> transition(states.size() * n);
  const unsigned hardware = std::max(1U, std::thread::hardware_concurrency());
  const unsigned thread_count = std::min(12U, hardware);
  std::vector<std::thread> workers;
  workers.reserve(thread_count);
  for (unsigned worker = 0; worker < thread_count; ++worker) {
    const std::size_t begin = states.size() * worker / thread_count;
    const std::size_t end = states.size() * (worker + 1) / thread_count;
    workers.emplace_back([&, begin, end]() {
      for (std::size_t id = begin; id < end; ++id) {
        for (unsigned letter = 1; letter <= n; ++letter) {
          transition[id * n + letter - 1] =
              index.at(insert_letter(states[id], letter, n));
        }
      }
    });
  }
  for (auto& worker : workers) worker.join();
  return transition;
}

struct Classification {
  Dsu dsu;
  std::vector<std::uint64_t> merge_queue;
  std::uint64_t primitive_tests = 0;
  std::uint64_t closure_tests = 0;

  Classification(std::size_t state_count,
                 const std::vector<std::uint32_t>& transition,
                 unsigned n)
      : dsu(state_count) {
    merge_queue.reserve(state_count - 1);
    const auto step = [&](std::uint32_t state, unsigned letter) {
      return transition[static_cast<std::size_t>(state) * n + letter - 1];
    };
    const auto merge = [&](std::uint32_t a, std::uint32_t b) {
      if (dsu.unite(a, b)) {
        merge_queue.push_back((static_cast<std::uint64_t>(a) << 32) | b);
      }
    };

    for (std::uint32_t state = 0; state < state_count; ++state) {
      for (unsigned p = 1; p <= n; ++p) {
        const auto p1 = step(state, p);
        merge(p1, step(p1, p));
        ++primitive_tests;
      }
      for (unsigned p = 1; p <= n; ++p) {
        for (unsigned q = p + 1; q <= n; ++q) {
          merge(step(step(step(state, p), q), p),
                step(step(step(state, q), p), q));
          ++primitive_tests;
        }
      }
      for (unsigned x = 1; x <= n; ++x) {
        for (unsigned y = x + 1; y <= n; ++y) {
          for (unsigned z = y + 1; z <= n; ++z) {
            merge(step(step(step(state, x), z), y),
                  step(step(step(state, z), x), y));
            merge(step(step(step(state, y), x), z),
                  step(step(step(state, y), z), x));
            primitive_tests += 2;
          }
        }
      }
      if (state_count >= 1000000 && state % 1000000 == 0 && state != 0) {
        std::cerr << "primitive_progress=" << state << "/" << state_count
                  << " merges=" << merge_queue.size() << "\n";
      }
    }

    for (std::size_t head = 0; head < merge_queue.size(); ++head) {
      const std::uint32_t a = static_cast<std::uint32_t>(merge_queue[head] >> 32);
      const std::uint32_t b = static_cast<std::uint32_t>(merge_queue[head]);
      for (unsigned letter = 1; letter <= n; ++letter) {
        merge(step(a, letter), step(b, letter));
        ++closure_tests;
      }
      if (merge_queue.size() >= 1000000 && head % 1000000 == 0 && head != 0) {
        std::cerr << "closure_progress=" << head << "/" << merge_queue.size()
                  << "\n";
      }
    }
  }
};

static std::array<unsigned, 8> decode_shape(std::uint32_t code) {
  std::array<unsigned, 8> rows{};
  for (unsigned r = 0; r < 8; ++r) rows[r] = (code >> (4 * r)) & 0xfU;
  return rows;
}

static bool shape_subset(std::uint32_t lower, std::uint32_t upper, unsigned n) {
  const auto a = decode_shape(lower);
  const auto b = decode_shape(upper);
  for (unsigned r = 0; r < n; ++r) {
    if (a[r] > b[r]) return false;
  }
  return true;
}

static bool missing_in_interval(std::uint32_t lower, std::uint32_t upper,
                                const std::vector<std::uint32_t>& present,
                                unsigned n, std::uint32_t& missing) {
  const auto lo = decode_shape(lower);
  const auto hi = decode_shape(upper);
  const auto visit = [&](auto&& self, unsigned row, unsigned previous,
                         std::uint32_t code) -> bool {
    if (row == n) {
      if (!std::binary_search(present.begin(), present.end(), code)) {
        missing = code;
        return true;
      }
      return false;
    }
    const unsigned maximum = std::min(previous, hi[row]);
    if (lo[row] > maximum) throw std::runtime_error("invalid interval endpoints");
    for (unsigned value = lo[row]; value <= maximum; ++value) {
      if (self(self, row + 1, value, code | (value << (4 * row)))) return true;
    }
    return false;
  };
  return visit(visit, 0, n, 0);
}

struct Result {
  unsigned n = 0;
  std::uint64_t all_tableaux = 0;
  std::uint64_t initial_tableaux = 0;
  std::uint64_t initial_classes = 0;
  std::uint64_t urts = 0;
  std::uint64_t primitive_tests = 0;
  std::uint64_t closure_tests = 0;
  std::uint64_t merges = 0;
  bool interval_complete = true;
  std::uint32_t witness_root = 0;
  std::uint32_t lower = 0;
  std::uint32_t upper = 0;
  std::uint32_t missing = 0;
  Key lower_tableau = 0;
  Key upper_tableau = 0;
};

static Result classify_and_check(const std::vector<Key>& states, unsigned n) {
  const auto transition_start = std::chrono::steady_clock::now();
  auto transition = build_transitions(states, n);
  const auto transition_end = std::chrono::steady_clock::now();
  std::cerr << "transition_seconds="
            << std::chrono::duration<double>(transition_end - transition_start).count()
            << "\n";

  const auto classify_start = std::chrono::steady_clock::now();
  Classification classification(states.size(), transition, n);
  const auto classify_end = std::chrono::steady_clock::now();
  std::cerr << "classification_seconds="
            << std::chrono::duration<double>(classify_end - classify_start).count()
            << "\n";
  std::vector<std::uint32_t>().swap(transition);

  Result result;
  result.n = n;
  result.all_tableaux = states.size();
  result.primitive_tests = classification.primitive_tests;
  result.closure_tests = classification.closure_tests;
  result.merges = classification.merge_queue.size();

  std::vector<std::uint32_t> component_sizes(states.size(), 0);
  std::vector<std::uint64_t> root_shapes;
  for (std::uint32_t id = 0; id < states.size(); ++id) {
    if (!initial(states[id], n)) continue;
    ++result.initial_tableaux;
    const std::uint32_t root = classification.dsu.find(id);
    ++component_sizes[root];
    root_shapes.push_back((static_cast<std::uint64_t>(root) << 32) |
                          shape_code(states[id]));
  }
  for (const auto size : component_sizes) {
    if (size != 0) {
      ++result.initial_classes;
      if (size == 1) ++result.urts;
    }
  }
  std::vector<std::uint32_t>().swap(component_sizes);
  std::sort(root_shapes.begin(), root_shapes.end());
  root_shapes.erase(std::unique(root_shapes.begin(), root_shapes.end()), root_shapes.end());

  const auto interval_start = std::chrono::steady_clock::now();
  for (std::size_t begin = 0; begin < root_shapes.size();) {
    std::size_t end = begin + 1;
    const std::uint32_t root = static_cast<std::uint32_t>(root_shapes[begin] >> 32);
    while (end < root_shapes.size() &&
           static_cast<std::uint32_t>(root_shapes[end] >> 32) == root) ++end;
    if (end - begin > 1) {
      std::vector<std::uint32_t> shapes;
      shapes.reserve(end - begin);
      for (std::size_t k = begin; k < end; ++k) {
        shapes.push_back(static_cast<std::uint32_t>(root_shapes[k]));
      }
      for (std::size_t i = 0; i < shapes.size() && result.interval_complete; ++i) {
        for (std::size_t j = 0; j < shapes.size(); ++j) {
          if (i == j || !shape_subset(shapes[i], shapes[j], n)) continue;
          std::uint32_t missing = 0;
          if (missing_in_interval(shapes[i], shapes[j], shapes, n, missing)) {
            result.interval_complete = false;
            result.witness_root = root;
            result.lower = shapes[i];
            result.upper = shapes[j];
            result.missing = missing;
            break;
          }
        }
      }
    }
    if (!result.interval_complete) break;
    begin = end;
  }
  const auto interval_end = std::chrono::steady_clock::now();
  std::cerr << "interval_seconds="
            << std::chrono::duration<double>(interval_end - interval_start).count()
            << "\n";

  if (!result.interval_complete) {
    for (std::uint32_t id = 0; id < states.size(); ++id) {
      if (!initial(states[id], n) || classification.dsu.find(id) != result.witness_root) {
        continue;
      }
      const auto shape = shape_code(states[id]);
      if (shape == result.lower && result.lower_tableau == 0) result.lower_tableau = states[id];
      if (shape == result.upper && result.upper_tableau == 0) result.upper_tableau = states[id];
    }
  }
  return result;
}

static std::string shape_string(std::uint32_t shape, unsigned n) {
  const auto rows = decode_shape(shape);
  std::string out = "[";
  bool first = true;
  for (unsigned r = 0; r < n && rows[r] != 0; ++r) {
    if (!first) out += ",";
    first = false;
    out += std::to_string(rows[r]);
  }
  out += "]";
  return out;
}

static void write_result(const Result& result, const std::string& path) {
  std::ofstream out(path);
  if (!out) throw std::runtime_error("cannot open result path");
  out << "{\n"
      << "  \"schema_version\": 1,\n"
      << "  \"n\": " << result.n << ",\n"
      << "  \"all_tableaux\": " << result.all_tableaux << ",\n"
      << "  \"initial_tableaux\": " << result.initial_tableaux << ",\n"
      << "  \"initial_classes\": " << result.initial_classes << ",\n"
      << "  \"urts\": " << result.urts << ",\n"
      << "  \"primitive_tests\": " << result.primitive_tests << ",\n"
      << "  \"closure_tests\": " << result.closure_tests << ",\n"
      << "  \"merges\": " << result.merges << ",\n"
      << "  \"interval_complete\": "
      << (result.interval_complete ? "true" : "false") << ",\n"
      << "  \"witness\": ";
  if (result.interval_complete) {
    out << "null\n";
  } else {
    out << "{\n"
        << "    \"component_root_discovery_id\": " << result.witness_root << ",\n"
        << "    \"lower_shape\": " << shape_string(result.lower, result.n) << ",\n"
        << "    \"upper_shape\": " << shape_string(result.upper, result.n) << ",\n"
        << "    \"missing_shape\": " << shape_string(result.missing, result.n) << ",\n"
        << "    \"lower_tableau\": " << key_string(result.lower_tableau) << ",\n"
        << "    \"upper_tableau\": " << key_string(result.upper_tableau) << "\n"
        << "  }\n";
  }
  out << "}\n";
  if (!out) throw std::runtime_error("failed while writing result");
}

}  // namespace kk

int main(int argc, char** argv) {
  try {
    kk::self_test();
    unsigned n = 7;
    bool count_only = false;
    bool classify = false;
    std::string output_path;
    for (int i = 1; i < argc; ++i) {
      const std::string arg = argv[i];
      if (arg == "--count-only") count_only = true;
      else if (arg == "--classify") classify = true;
      else if (arg == "--output" && i + 1 < argc) output_path = argv[++i];
      else if (arg == "--n" && i + 1 < argc) n = static_cast<unsigned>(std::stoul(argv[++i]));
      else throw std::runtime_error(
          "usage: discovery [--n N] [--count-only|--classify] [--output PATH]");
    }
    const auto start = std::chrono::steady_clock::now();
    kk::Enumeration enumeration(n);
    std::uint64_t initial_count = 0;
    for (const kk::Key key : enumeration.states) initial_count += kk::initial(key, n);
    const auto end = std::chrono::steady_clock::now();
    std::cout << "n=" << n << " all_tableaux=" << enumeration.states.size()
              << " initial_tableaux=" << initial_count
              << " enumeration_seconds="
              << std::chrono::duration<double>(end - start).count() << "\n";
    if (classify && !count_only) {
      const kk::Result result = kk::classify_and_check(enumeration.states, n);
      std::cout << "initial_classes=" << result.initial_classes
                << " urts=" << result.urts
                << " interval_complete=" << std::boolalpha << result.interval_complete
                << " primitive_tests=" << result.primitive_tests
                << " closure_tests=" << result.closure_tests
                << " merges=" << result.merges << "\n";
      if (!result.interval_complete) {
        std::cout << "lower_shape=" << kk::shape_string(result.lower, n)
                  << " upper_shape=" << kk::shape_string(result.upper, n)
                  << " missing_shape=" << kk::shape_string(result.missing, n)
                  << " lower_tableau=" << kk::key_string(result.lower_tableau)
                  << " upper_tableau=" << kk::key_string(result.upper_tableau) << "\n";
      }
      if (!output_path.empty()) kk::write_result(result, output_path);
    } else if (!count_only) {
      std::cout << "specify --classify for the full Algorithm 1 computation\n";
    }
    return 0;
  } catch (const std::exception& ex) {
    std::cerr << "ERROR: " << ex.what() << "\n";
    return 1;
  }
}
