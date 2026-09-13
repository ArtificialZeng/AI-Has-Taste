#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

namespace {

constexpr int kMaxN = 10;
constexpr int kMaxGap = 16;
constexpr int kMaxXDegree = kMaxGap / 2;
using Perm = std::array<std::uint8_t, kMaxN>;
using Poly = std::array<std::uint32_t, kMaxXDegree + 1>;
using RPoly = std::array<std::int64_t, kMaxGap + 1>;

struct PolyHash {
  std::size_t operator()(const Poly& p) const noexcept {
    std::uint64_t h = 1469598103934665603ULL;
    for (std::uint32_t c : p) {
      for (int j = 0; j < 4; ++j) {
        h ^= (c >> (8 * j)) & 0xffU;
        h *= 1099511628211ULL;
      }
    }
    return static_cast<std::size_t>(h);
  }
};

struct RPolyHash {
  std::size_t operator()(const RPoly& p) const noexcept {
    std::uint64_t h = 1469598103934665603ULL;
    for (std::int64_t coefficient : p) {
      const std::uint64_t c = static_cast<std::uint64_t>(coefficient);
      for (int j = 0; j < 8; ++j) {
        h ^= (c >> (8 * j)) & 0xffU;
        h *= 1099511628211ULL;
      }
    }
    return static_cast<std::size_t>(h);
  }
};

struct Certificate {
  int endpoint_n = -1;
  std::vector<int> omega;
  std::vector<std::uint64_t> expected_sizes;
  std::vector<std::uint64_t> expected_pairs;
};

[[noreturn]] void fail(const std::string& message) {
  throw std::runtime_error(message);
}

std::vector<std::string> split(const std::string& s, char delimiter) {
  std::vector<std::string> out;
  std::stringstream stream(s);
  std::string item;
  while (std::getline(stream, item, delimiter)) out.push_back(item);
  if (!s.empty() && s.back() == delimiter) out.emplace_back();
  return out;
}

std::uint64_t parse_u64(const std::string& s) {
  if (s.empty()) fail("empty unsigned integer");
  std::uint64_t value = 0;
  for (char ch : s) {
    if (ch < '0' || ch > '9') fail("invalid unsigned integer: " + s);
    const std::uint64_t digit = static_cast<unsigned>(ch - '0');
    if (value > (std::numeric_limits<std::uint64_t>::max() - digit) / 10)
      fail("unsigned integer overflow: " + s);
    value = value * 10 + digit;
  }
  return value;
}

std::vector<std::uint64_t> parse_u64_csv(const std::string& s) {
  std::vector<std::uint64_t> out;
  for (const std::string& item : split(s, ',')) out.push_back(parse_u64(item));
  return out;
}

std::vector<int> parse_int_csv(const std::string& s) {
  std::vector<int> out;
  for (std::uint64_t value : parse_u64_csv(s)) {
    if (value > static_cast<std::uint64_t>(std::numeric_limits<int>::max()))
      fail("integer too large");
    out.push_back(static_cast<int>(value));
  }
  return out;
}

Certificate parse_certificate(const std::string& path) {
  std::ifstream input(path);
  if (!input) fail("cannot open certificate: " + path);
  std::map<std::string, std::string> fields;
  std::string line;
  int line_number = 0;
  while (std::getline(input, line)) {
    ++line_number;
    if (!line.empty() && line.back() == '\r') line.pop_back();
    if (line.empty()) fail("blank line at certificate line " + std::to_string(line_number));
    const std::size_t pos = line.find('=');
    if (pos == std::string::npos || pos == 0)
      fail("malformed certificate line " + std::to_string(line_number));
    const std::string key = line.substr(0, pos);
    const std::string value = line.substr(pos + 1);
    if (!fields.emplace(key, value).second) fail("duplicate certificate key: " + key);
  }
  const std::set<std::string> required = {
      "format", "endpoint_n", "omega", "fibonacci_initial",
      "fibonacci_recurrence", "expected_interval_sizes",
      "expected_comparable_pairs", "claim", "end"};
  std::set<std::string> actual;
  for (const auto& [key, value] : fields) {
    (void)value;
    actual.insert(key);
  }
  if (actual != required) fail("certificate keys are missing or unknown");
  if (fields.at("format") != "KL_R_FIB_CERTIFICATE_V1") fail("bad format marker");
  if (fields.at("fibonacci_initial") != "1,1") fail("bad Fibonacci initial data");
  if (fields.at("fibonacci_recurrence") != "F_h=F_{h-1}+xF_{h-2}")
    fail("bad Fibonacci recurrence");
  if (fields.at("claim") != "ALL_PAIRS_FACTOR") fail("unsupported certificate claim");
  if (fields.at("end") != "TRUE") fail("missing end marker");

  Certificate cert;
  const std::uint64_t endpoint_n = parse_u64(fields.at("endpoint_n"));
  if (endpoint_n != static_cast<std::uint64_t>(kMaxN))
    fail("this verifier is bound to endpoint_n=10");
  cert.endpoint_n = kMaxN;
  cert.omega = parse_int_csv(fields.at("omega"));
  cert.expected_sizes = parse_u64_csv(fields.at("expected_interval_sizes"));
  cert.expected_pairs = parse_u64_csv(fields.at("expected_comparable_pairs"));
  if (cert.expected_sizes.size() != 9 || cert.expected_pairs.size() != 9)
    fail("expected count vectors must cover n=2,...,10");
  return cert;
}

Perm identity_perm() {
  Perm w{};
  for (int i = 0; i < kMaxN; ++i) w[i] = static_cast<std::uint8_t>(i + 1);
  return w;
}

Perm endpoint_perm(int n) {
  Perm v = identity_perm();
  if (n == 2) return v;
  for (int i = 0; i < n - 2; ++i) v[i] = static_cast<std::uint8_t>(i + 3);
  v[n - 2] = 1;
  v[n - 1] = 2;
  return v;
}

std::uint64_t encode(const Perm& w, int n) {
  std::uint64_t code = 0;
  for (int i = 0; i < n; ++i) code = (code << 4) | w[i];
  return code;
}

std::string perm_string(const Perm& w, int n) {
  std::ostringstream out;
  out << '[';
  for (int i = 0; i < n; ++i) {
    if (i) out << ',';
    out << static_cast<int>(w[i]);
  }
  out << ']';
  return out.str();
}

int coxeter_length(const Perm& w, int n) {
  int ans = 0;
  for (int i = 0; i < n; ++i)
    for (int j = i + 1; j < n; ++j) ans += (w[i] > w[j]);
  return ans;
}

bool bruhat_leq_rank_matrix(const Perm& u, const Perm& v, int n) {
  // Independent rank-matrix evaluator.
  std::array<int, kMaxN + 1> ucounts{};
  std::array<int, kMaxN + 1> vcounts{};
  for (int p = 0; p < n; ++p) {
    ++ucounts[u[p]];
    ++vcounts[v[p]];
    int urank = 0;
    int vrank = 0;
    for (int r = 1; r <= n; ++r) {
      urank += ucounts[r];
      vrank += vcounts[r];
      if (urank < vrank) return false;
    }
  }
  return true;
}

std::vector<int> canonical_omega(int n) {
  std::vector<int> word;
  for (int j = 2; j < n; ++j) {
    word.push_back(j);
    word.push_back(j - 1);
  }
  return word;
}

Perm multiply_word(const std::vector<int>& word, int n) {
  Perm w = identity_perm();
  for (int s : word) {
    if (s < 1 || s >= n) fail("simple reflection outside S_n");
    std::swap(w[s - 1], w[s]);
  }
  return w;
}

std::set<std::uint64_t> subword_lower_set(const std::vector<int>& word, int n) {
  if (word.size() >= 31) fail("subword cross-check word is too long");
  std::set<std::uint64_t> result;
  const std::uint32_t limit = std::uint32_t{1} << word.size();
  for (std::uint32_t mask = 0; mask < limit; ++mask) {
    Perm w = identity_perm();
    for (std::size_t k = 0; k < word.size(); ++k)
      if ((mask >> k) & 1U) std::swap(w[word[k] - 1], w[word[k]]);
    result.insert(encode(w, n));
  }
  return result;
}

std::vector<Perm> full_symmetric_group_filter(int n, const Perm& endpoint) {
  // Primary verifier enumeration: visit all n! permutations, independently
  // of the discovery program's subword enumeration.
  Perm w = identity_perm();
  std::vector<Perm> result;
  do {
    if (bruhat_leq_rank_matrix(w, endpoint, n)) result.push_back(w);
  } while (std::next_permutation(w.begin(), w.begin() + n));
  return result;
}

int poly_degree(const Poly& p) {
  for (int i = kMaxXDegree; i >= 0; --i)
    if (p[i] != 0) return i;
  return -1;
}

Poly poly_multiply(const Poly& a, const Poly& b) {
  Poly out{};
  for (int i = 0; i <= kMaxXDegree; ++i) {
    if (a[i] == 0) continue;
    for (int j = 0; i + j <= kMaxXDegree; ++j) {
      if (b[j] == 0) continue;
      const std::uint64_t value = static_cast<std::uint64_t>(out[i + j]) +
                                  static_cast<std::uint64_t>(a[i]) * b[j];
      if (value > std::numeric_limits<std::uint32_t>::max())
        fail("polynomial coefficient overflow");
      out[i + j] = static_cast<std::uint32_t>(value);
    }
  }
  return out;
}

std::string poly_string(const Poly& p, const std::string& variable) {
  std::ostringstream out;
  bool first = true;
  for (int i = 0; i <= kMaxXDegree; ++i) {
    const std::uint32_t c = p[i];
    if (!c) continue;
    if (!first) out << '+';
    first = false;
    if (i == 0 || c != 1) out << c;
    if (i > 0) {
      if (c != 1) out << '*';
      out << variable;
      if (i > 1) out << '^' << i;
    }
  }
  return first ? "0" : out.str();
}

struct FibonacciMonoid {
  std::vector<Poly> fib;
  std::vector<Poly> products;
  std::vector<std::vector<std::uint8_t>> witnesses;
  std::unordered_map<Poly, std::uint32_t, PolyHash> product_id;
  std::unordered_set<std::string> visited_states;

  FibonacciMonoid() {
    fib.resize(2 * kMaxXDegree + 2);
    fib[0][0] = 1;
    fib[1][0] = 1;
    for (std::size_t h = 2; h < fib.size(); ++h) {
      fib[h] = fib[h - 1];
      for (int j = 0; j < kMaxXDegree; ++j) {
        const std::uint64_t value = static_cast<std::uint64_t>(fib[h][j + 1]) +
                                    fib[h - 2][j];
        if (value > std::numeric_limits<std::uint32_t>::max())
          fail("Fibonacci coefficient overflow");
        fib[h][j + 1] = static_cast<std::uint32_t>(value);
      }
    }
    Poly one{};
    one[0] = 1;
    std::vector<std::uint8_t> factors;
    enumerate(2, one, factors);
  }

  std::string state_key(int start_h, const Poly& p) const {
    std::ostringstream out;
    out << start_h;
    for (std::uint32_t c : p) out << ':' << c;
    return out.str();
  }

  void enumerate(int start_h, const Poly& current,
                 std::vector<std::uint8_t>& factors) {
    const std::string state = state_key(start_h, current);
    if (!visited_states.insert(state).second) return;
    auto [it, inserted] = product_id.emplace(current, products.size());
    if (inserted) {
      products.push_back(current);
      witnesses.push_back(factors);
    }
    const int current_degree = poly_degree(current);
    for (int h = start_h; h < static_cast<int>(fib.size()); ++h) {
      const int next_degree = current_degree + poly_degree(fib[h]);
      if (next_degree > kMaxXDegree) continue;
      const Poly next = poly_multiply(current, fib[h]);
      factors.push_back(static_cast<std::uint8_t>(h));
      enumerate(h, next, factors);
      factors.pop_back();
    }
  }
};

std::uint64_t binomial(int n, int k) {
  if (k < 0 || k > n) return 0;
  k = std::min(k, n - k);
  std::uint64_t value = 1;
  for (int j = 1; j <= k; ++j) value = value * (n - k + j) / j;
  return value;
}

void checked_add(std::int64_t& target, __int128 delta) {
  const __int128 value = static_cast<__int128>(target) + delta;
  if (value < std::numeric_limits<std::int64_t>::min() ||
      value > std::numeric_limits<std::int64_t>::max())
    fail("ordinary R-polynomial coefficient overflow");
  target = static_cast<std::int64_t>(value);
}

RPoly ordinary_from_normalized_tilde(const Poly& b, int gap) {
  // Source identity with Q=z^2:
  // R_{u,v}(z^2)=z^gap * Rtilde_{u,v}(z-z^{-1}).
  RPoly result{};
  for (int j = 0; j <= poly_degree(b); ++j) {
    if (b[j] == 0) continue;
    const int power = gap - 2 * j;
    if (power < 0) fail("normalized tilde polynomial exceeds its gap");
    for (int k = 0; k <= power; ++k) {
      const int q_exponent = gap - j - k;
      const __int128 magnitude = static_cast<__int128>(b[j]) * binomial(power, k);
      checked_add(result[q_exponent], (k & 1) ? -magnitude : magnitude);
    }
  }
  return result;
}

struct OrdinaryImages {
  std::array<std::vector<RPoly>, kMaxGap + 1> polynomials;
  std::array<std::unordered_map<RPoly, std::uint32_t, RPolyHash>,
             kMaxGap + 1>
      class_by_polynomial;

  explicit OrdinaryImages(const FibonacciMonoid& monoid) {
    for (int gap = 0; gap <= kMaxGap; ++gap) {
      polynomials[gap].resize(monoid.products.size());
      for (std::uint32_t class_id = 0; class_id < monoid.products.size(); ++class_id) {
        const Poly& b = monoid.products[class_id];
        if (poly_degree(b) > gap / 2) continue;
        const RPoly r = ordinary_from_normalized_tilde(b, gap);
        polynomials[gap][class_id] = r;
        const auto [it, inserted] =
            class_by_polynomial[gap].emplace(r, class_id);
        if (!inserted && it->second != class_id)
          fail("ordinary/tilde transformation is not injective");
      }
    }
  }
};

struct VerificationStats {
  std::uint64_t interval_size = 0;
  std::uint64_t comparable_pairs = 0;
  std::uint64_t fingerprint = 1469598103934665603ULL;
  std::size_t distinct_products = 0;
  std::uint32_t max_coefficient = 0;
  bool index_sum_pattern_set = false;
};

void enumerate_index_sum_classes(
    int minimum_h, int remaining_sum, const Poly& current,
    const FibonacciMonoid& monoid, std::unordered_set<std::uint32_t>& classes) {
  const auto found = monoid.product_id.find(current);
  if (found == monoid.product_id.end())
    fail("index-sum product is absent from the complete degree catalog");
  classes.insert(found->second);
  for (int h = minimum_h; h <= remaining_sum; ++h) {
    const Poly next = poly_multiply(current, monoid.fib[h]);
    enumerate_index_sum_classes(h, remaining_sum - h, next, monoid, classes);
  }
}

void fingerprint_byte(std::uint64_t& h, std::uint8_t byte) {
  h ^= byte;
  h *= 1099511628211ULL;
}

void fingerprint_u64(std::uint64_t& h, std::uint64_t value) {
  for (int i = 7; i >= 0; --i)
    fingerprint_byte(h, static_cast<std::uint8_t>((value >> (8 * i)) & 0xffU));
}

std::size_t lookup_pair_index(const std::vector<std::uint32_t>& lower_ids,
                              const std::vector<std::uint64_t>& offsets,
                              std::uint32_t top_id, std::uint32_t lower_id) {
  const auto begin = lower_ids.begin() + static_cast<std::ptrdiff_t>(offsets[top_id]);
  const auto end = lower_ids.begin() + static_cast<std::ptrdiff_t>(offsets[top_id + 1]);
  const auto it = std::lower_bound(begin, end, lower_id);
  if (it == end || *it != lower_id) return std::numeric_limits<std::size_t>::max();
  return static_cast<std::size_t>(it - lower_ids.begin());
}

const Poly& checked_class_poly(const FibonacciMonoid& monoid,
                               const std::vector<std::uint32_t>& class_ids,
                               std::size_t pair_index) {
  if (pair_index >= class_ids.size()) fail("pair index outside class table");
  const std::uint32_t class_id = class_ids[pair_index];
  if (class_id >= monoid.products.size()) fail("recurrence read an uninitialized class");
  return monoid.products[class_id];
}

VerificationStats verify_dimension(int n, const std::vector<int>& omega,
                                   const FibonacciMonoid& monoid,
                                   const OrdinaryImages& ordinary_images) {
  const Perm endpoint = endpoint_perm(n);
  const std::vector<int> expected_word = canonical_omega(n);
  if (omega != expected_word) fail("certificate omega does not equal canonical Omega_10");
  if (multiply_word(omega, n) != endpoint) fail("Omega_n does not multiply to v_n");
  if (static_cast<int>(omega.size()) != coxeter_length(endpoint, n))
    fail("Omega_n is not reduced");

  std::vector<Perm> elements = full_symmetric_group_filter(n, endpoint);
  std::set<std::uint64_t> rank_codes;
  for (const Perm& w : elements) rank_codes.insert(encode(w, n));
  const std::set<std::uint64_t> subword_codes = subword_lower_set(omega, n);
  if (rank_codes != subword_codes)
    fail("rank-matrix and subword lower-interval enumerations disagree");

  std::sort(elements.begin(), elements.end(), [n](const Perm& a, const Perm& b) {
    const int la = coxeter_length(a, n);
    const int lb = coxeter_length(b, n);
    if (la != lb) return la < lb;
    return std::lexicographical_compare(a.begin(), a.begin() + n, b.begin(), b.begin() + n);
  });
  const std::size_t element_count = elements.size();
  std::vector<int> lengths(element_count);
  std::unordered_map<std::uint64_t, std::uint32_t> id_by_code;
  id_by_code.reserve(element_count * 2);
  for (std::uint32_t id = 0; id < element_count; ++id) {
    lengths[id] = coxeter_length(elements[id], n);
    if (!id_by_code.emplace(encode(elements[id], n), id).second)
      fail("duplicate lower-interval element");
  }

  std::vector<std::uint64_t> offsets(element_count + 1);
  std::vector<std::uint32_t> lower_ids;
  for (std::uint32_t vid = 0; vid < element_count; ++vid) {
    offsets[vid] = lower_ids.size();
    for (std::uint32_t uid = 0; uid < element_count; ++uid)
      if (bruhat_leq_rank_matrix(elements[uid], elements[vid], n))
        lower_ids.push_back(uid);
  }
  offsets[element_count] = lower_ids.size();

  std::vector<std::uint32_t> tilde_class_ids(
      lower_ids.size(), std::numeric_limits<std::uint32_t>::max());
  std::vector<std::uint32_t> ordinary_class_ids(
      lower_ids.size(), std::numeric_limits<std::uint32_t>::max());
  std::unordered_set<std::uint32_t> seen_classes;
  VerificationStats stats;
  stats.interval_size = element_count;
  stats.comparable_pairs = lower_ids.size();

  Poly one{};
  one[0] = 1;
  const auto one_it = monoid.product_id.find(one);
  if (one_it == monoid.product_id.end()) fail("monoid does not contain the unit");

  for (std::uint32_t vid = 0; vid < element_count; ++vid) {
    int descent = -1;
    for (int i = n - 2; i >= 0; --i) {
      if (elements[vid][i] > elements[vid][i + 1]) {
        descent = i;
        break;
      }
    }
    std::uint32_t vsid = 0;
    if (descent >= 0) {
      Perm vs = elements[vid];
      std::swap(vs[descent], vs[descent + 1]);
      const auto found = id_by_code.find(encode(vs, n));
      if (found == id_by_code.end()) fail("right descent left the lower interval");
      vsid = found->second;
      if (lengths[vsid] + 1 != lengths[vid] || vsid >= vid)
        fail("right descent did not reach an earlier rank");
    }

    for (std::uint64_t pos = offsets[vid]; pos < offsets[vid + 1]; ++pos) {
      const std::uint32_t uid = lower_ids[pos];
      Poly value{};
      RPoly ordinary_value{};
      const int gap = lengths[vid] - lengths[uid];
      if (uid == vid) {
        value = one;
        ordinary_value[0] = 1;
      } else {
        if (descent < 0) fail("non-diagonal pair with descent-free upper endpoint");
        Perm us = elements[uid];
        const bool u_descent = us[descent] > us[descent + 1];
        std::swap(us[descent], us[descent + 1]);
        const auto us_global = id_by_code.find(encode(us, n));
        if (u_descent) {
          if (us_global == id_by_code.end()) fail("descent term left lower interval");
          const std::size_t source = lookup_pair_index(
              lower_ids, offsets, vsid, us_global->second);
          if (source == std::numeric_limits<std::size_t>::max())
            fail("required descent recurrence term is incomparable");
          value = checked_class_poly(monoid, tilde_class_ids, source);
          const std::uint32_t ordinary_class = ordinary_class_ids[source];
          if (ordinary_class >= monoid.products.size())
            fail("ordinary recurrence read an uninitialized class");
          ordinary_value = ordinary_images.polynomials[gap][ordinary_class];
        } else {
          const std::size_t source0 = lookup_pair_index(lower_ids, offsets, vsid, uid);
          if (source0 == std::numeric_limits<std::size_t>::max())
            fail("lifting-property term u<=vs is missing");
          value = checked_class_poly(monoid, tilde_class_ids, source0);
          const std::uint32_t ordinary_class0 = ordinary_class_ids[source0];
          if (ordinary_class0 >= monoid.products.size())
            fail("ordinary recurrence read an uninitialized u,vs class");
          const RPoly& ordinary0 = ordinary_images.polynomials[gap - 1][ordinary_class0];
          for (int exponent = 0; exponent < kMaxGap; ++exponent)
            checked_add(ordinary_value[exponent + 1], ordinary0[exponent]);
          for (int exponent = 0; exponent <= kMaxGap; ++exponent)
            checked_add(ordinary_value[exponent], -static_cast<__int128>(ordinary0[exponent]));
          if (us_global == id_by_code.end())
            fail("lifting-property term us<=v left the lower interval");
          const std::size_t source1 = lookup_pair_index(
              lower_ids, offsets, vsid, us_global->second);
          if (source1 != std::numeric_limits<std::size_t>::max()) {
            const Poly& shifted = checked_class_poly(monoid, tilde_class_ids, source1);
            if (shifted[kMaxXDegree] != 0) fail("x-shift exceeds degree bound");
            for (int j = 0; j < kMaxXDegree; ++j) {
              const std::uint64_t coefficient =
                  static_cast<std::uint64_t>(value[j + 1]) + shifted[j];
              if (coefficient > std::numeric_limits<std::uint32_t>::max())
                fail("recurrence coefficient overflow");
              value[j + 1] = static_cast<std::uint32_t>(coefficient);
            }
            const std::uint32_t ordinary_class1 = ordinary_class_ids[source1];
            if (ordinary_class1 >= monoid.products.size())
              fail("ordinary recurrence read an uninitialized us,vs class");
            const RPoly& ordinary1 =
                ordinary_images.polynomials[gap - 2][ordinary_class1];
            for (int exponent = 0; exponent < kMaxGap; ++exponent)
              checked_add(ordinary_value[exponent + 1], ordinary1[exponent]);
          }
        }
      }

      if (gap < 0 || poly_degree(value) > gap / 2 || value[0] != 1)
        fail("recurrence produced an invalid normalized polynomial");
      const auto membership = monoid.product_id.find(value);
      if (membership == monoid.product_id.end()) {
        const RPoly transformed = ordinary_from_normalized_tilde(value, gap);
        if (ordinary_value != transformed)
          fail("the two exact evaluators disagree on a nonmember candidate");
        std::ostringstream message;
        message << "exact counterexample: n=" << n
                << " u=" << perm_string(elements[uid], n)
                << " v=" << perm_string(elements[vid], n)
                << " gap=" << gap << " B(x)=" << poly_string(value, "x")
                << " dual_recurrence_checked=true Rtilde(q)=";
        bool first = true;
        for (int j = 0; j <= poly_degree(value); ++j) {
          if (!value[j]) continue;
          if (!first) message << '+';
          first = false;
          if (value[j] != 1 || gap - 2 * j == 0) message << value[j];
          if (gap - 2 * j > 0) {
            if (value[j] != 1) message << '*';
            message << 'q';
            if (gap - 2 * j > 1) message << '^' << (gap - 2 * j);
          }
        }
        fail(message.str());
      }
      const auto ordinary_membership =
          ordinary_images.class_by_polynomial[gap].find(ordinary_value);
      if (ordinary_membership == ordinary_images.class_by_polynomial[gap].end())
        fail("ordinary R recurrence produced a non-Fibonacci image");
      if (ordinary_membership->second != membership->second)
        fail("Dyer tilde recurrence and ordinary R recurrence disagree");
      tilde_class_ids[pos] = membership->second;
      ordinary_class_ids[pos] = ordinary_membership->second;
      seen_classes.insert(membership->second);
      for (std::uint32_t c : value) stats.max_coefficient = std::max(stats.max_coefficient, c);
      fingerprint_u64(stats.fingerprint, encode(elements[uid], n));
      fingerprint_u64(stats.fingerprint, encode(elements[vid], n));
      for (std::uint32_t c : value) fingerprint_u64(stats.fingerprint, c);
    }
  }
  stats.distinct_products = seen_classes.size();
  std::unordered_set<std::uint32_t> expected_index_sum_classes;
  enumerate_index_sum_classes(2, n - 2, one, monoid, expected_index_sum_classes);
  if (seen_classes != expected_index_sum_classes)
    fail("observed factor classes do not equal the canonical sum(h_i)<=n-2 set");
  stats.index_sum_pattern_set = true;
  return stats;
}

}  // namespace

int main(int argc, char** argv) {
  try {
    if (argc != 2) fail("usage: verify_n10 CERTIFICATE.txt");
    const Certificate cert = parse_certificate(argv[1]);
    const std::vector<int> omega10 = canonical_omega(cert.endpoint_n);
    if (cert.omega != omega10) fail("certificate omega mismatch");
    const FibonacciMonoid monoid;
    const OrdinaryImages ordinary_images(monoid);
    std::cout << "MONOID products_degree_le_8=" << monoid.products.size() << '\n';
    for (int n = 2; n <= cert.endpoint_n; ++n) {
      const VerificationStats stats =
          verify_dimension(n, canonical_omega(n), monoid, ordinary_images);
      const std::size_t slot = static_cast<std::size_t>(n - 2);
      if (stats.interval_size != cert.expected_sizes[slot])
        fail("interval-size claim mismatch at n=" + std::to_string(n));
      if (stats.comparable_pairs != cert.expected_pairs[slot])
        fail("comparable-pair claim mismatch at n=" + std::to_string(n));
      std::cout << "VERIFIED n=" << n << " interval=" << stats.interval_size
                << " pairs=" << stats.comparable_pairs
                << " distinct_B=" << stats.distinct_products
                << " max_coefficient=" << stats.max_coefficient
                << " index_sum_patterns="
                << (stats.index_sum_pattern_set ? "true" : "false")
                << " fingerprint=0x" << std::hex << std::setw(16)
                << std::setfill('0') << stats.fingerprint << std::dec << '\n';
    }
    std::cout << "CERTIFIED_FINITE_RESULT endpoint_n=10 all_pairs_factor=TRUE"
                 " dual_recurrence=TRUE\n";
    return 0;
  } catch (const std::exception& error) {
    std::cerr << "REJECTED: " << error.what() << '\n';
    return 1;
  }
}
