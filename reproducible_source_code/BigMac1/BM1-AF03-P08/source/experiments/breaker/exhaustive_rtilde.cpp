#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

namespace {

constexpr int MAX_N = 10;
constexpr int MAX_Q_DEG = 2 * (MAX_N - 2);
constexpr int MAX_T_DEG = MAX_Q_DEG / 2;
using Code = std::uint64_t;
using Id = std::uint16_t;
using Coeff = std::uint32_t;
using Poly = std::array<Coeff, MAX_T_DEG + 1>;
using DensePoly = std::vector<Coeff>;

struct VecHash {
  std::size_t operator()(const DensePoly& v) const noexcept {
    std::uint64_t h = 1469598103934665603ULL;
    for (Coeff x : v) {
      for (int k = 0; k < 4; ++k) {
        h ^= (x >> (8 * k)) & 0xffU;
        h *= 1099511628211ULL;
      }
    }
    return static_cast<std::size_t>(h);
  }
};

struct Element {
  Code code{};
  std::vector<std::uint8_t> reduced_word;
  std::uint8_t length{};
};

struct Block {
  std::vector<Id> lowers;
  std::vector<Poly> values;
};

struct Failure {
  int n{};
  std::vector<int> u;
  std::vector<int> v;
  int len_u{};
  int len_v{};
  DensePoly normalized;
};

struct RunResult {
  int n{};
  std::size_t elements{};
  std::uint64_t comparable_pairs{};
  std::uint64_t rejected_pairs{};
  Coeff max_coefficient{};
  std::size_t top_interval_cover_count{};
  bool cover_crosscheck{};
  bool top_fibonacci_check{};
  std::uint64_t digest{};
  double seconds{};
  std::map<std::string, std::uint64_t> factor_patterns;
};

std::string utc_now() {
  const std::time_t now = std::time(nullptr);
  std::tm tm{};
#if defined(_WIN32)
  gmtime_s(&tm, &now);
#else
  gmtime_r(&now, &tm);
#endif
  std::ostringstream out;
  out << std::put_time(&tm, "%Y-%m-%dT%H:%M:%SZ");
  return out.str();
}

Code identity_code(int n) {
  Code c = 0;
  for (int i = 0; i < n; ++i) c |= Code(i + 1) << (4 * i);
  return c;
}

int at(Code c, int pos) { return static_cast<int>((c >> (4 * pos)) & 0xfU); }

Code right_multiply(Code c, int s) {
  const int i = s - 1;
  const Code a = (c >> (4 * i)) & 0xfU;
  const Code b = (c >> (4 * (i + 1))) & 0xfU;
  const Code mask = (Code(0xf) << (4 * i)) | (Code(0xf) << (4 * (i + 1)));
  c &= ~mask;
  c |= a << (4 * (i + 1));
  c |= b << (4 * i);
  return c;
}

std::vector<int> decode(Code c, int n) {
  std::vector<int> p(n);
  for (int i = 0; i < n; ++i) p[i] = at(c, i);
  return p;
}

int inversion_length(Code c, int n) {
  int ans = 0;
  for (int i = 0; i < n; ++i)
    for (int j = i + 1; j < n; ++j) ans += at(c, i) > at(c, j);
  return ans;
}

std::vector<std::uint8_t> omega_word(int n) {
  std::vector<std::uint8_t> word;
  for (int j = 2; j <= n - 1; ++j) {
    word.push_back(static_cast<std::uint8_t>(j));
    word.push_back(static_cast<std::uint8_t>(j - 1));
  }
  return word;
}

Code apply_word(Code c, const std::vector<std::uint8_t>& word) {
  for (std::uint8_t s : word) c = right_multiply(c, s);
  return c;
}

std::unordered_map<Code, std::vector<std::uint8_t>> enumerate_subwords(
    int n, const std::vector<std::uint8_t>& word) {
  std::unordered_map<Code, std::vector<std::uint8_t>> seen;
  seen.emplace(identity_code(n), std::vector<std::uint8_t>{});
  for (std::uint8_t s : word) {
    std::vector<std::pair<Code, std::vector<std::uint8_t>>> old;
    old.reserve(seen.size());
    for (const auto& item : seen) old.push_back(item);
    for (const auto& [p, w] : old) {
      const Code q = right_multiply(p, s);
      if (seen.find(q) == seen.end()) {
        auto qw = w;
        qw.push_back(s);
        if (static_cast<int>(qw.size()) != inversion_length(q, n))
          throw std::runtime_error("newly retained subword is not reduced");
        seen.emplace(q, std::move(qw));
      }
    }
  }
  return seen;
}

std::vector<Code> downward_covers(Code p, int n) {
  std::vector<Code> out;
  for (int i = 0; i < n; ++i) {
    const int pi = at(p, i);
    for (int j = i + 1; j < n; ++j) {
      const int pj = at(p, j);
      if (pi <= pj) continue;
      bool blocked = false;
      for (int k = i + 1; k < j; ++k) {
        const int pk = at(p, k);
        if (pj < pk && pk < pi) {
          blocked = true;
          break;
        }
      }
      if (!blocked) {
        Code q = p;
        for (int s = i + 1; s <= j; ++s) q = right_multiply(q, s);
        for (int s = j - 1; s >= i + 1; --s) q = right_multiply(q, s);
        if (inversion_length(q, n) + 1 != inversion_length(p, n))
          throw std::runtime_error("invalid Bruhat cover implementation");
        out.push_back(q);
      }
    }
  }
  return out;
}

std::unordered_set<Code> cover_lower_interval(Code top, int n) {
  std::unordered_set<Code> seen{top};
  std::queue<Code> todo;
  todo.push(top);
  while (!todo.empty()) {
    const Code p = todo.front();
    todo.pop();
    for (Code q : downward_covers(p, n)) {
      if (seen.insert(q).second) todo.push(q);
    }
  }
  return seen;
}

DensePoly trim(DensePoly p) {
  while (p.size() > 1 && p.back() == 0) p.pop_back();
  return p;
}

DensePoly multiply(const DensePoly& a, const DensePoly& b) {
  DensePoly c(a.size() + b.size() - 1, 0);
  for (std::size_t i = 0; i < a.size(); ++i) {
    for (std::size_t j = 0; j < b.size(); ++j) {
      const std::uint64_t value = std::uint64_t(c[i + j]) +
                                  std::uint64_t(a[i]) * b[j];
      if (value > std::numeric_limits<Coeff>::max())
        throw std::overflow_error("allowed-product coefficient overflow");
      c[i + j] = static_cast<Coeff>(value);
    }
  }
  return c;
}

std::vector<DensePoly> fibonacci_polynomials(int max_h) {
  std::vector<DensePoly> f(max_h + 1);
  f[0] = {1};
  f[1] = {1};
  for (int h = 2; h <= max_h; ++h) {
    f[h] = f[h - 1];
    if (f[h].size() < f[h - 2].size() + 1) f[h].resize(f[h - 2].size() + 1, 0);
    for (std::size_t j = 0; j < f[h - 2].size(); ++j) {
      const std::uint64_t value = std::uint64_t(f[h][j + 1]) + f[h - 2][j];
      if (value > std::numeric_limits<Coeff>::max())
        throw std::overflow_error("Fibonacci coefficient overflow");
      f[h][j + 1] = static_cast<Coeff>(value);
    }
  }
  return f;
}

using ProductCatalog = std::unordered_map<DensePoly, std::vector<int>, VecHash>;

void generate_products_rec(int h, int max_h, int max_degree,
                           const std::vector<DensePoly>& fib, DensePoly current,
                           std::vector<int> factors, ProductCatalog& catalog) {
  if (h > max_h) {
    catalog.emplace(std::move(current), std::move(factors));
    return;
  }
  const int factor_degree = static_cast<int>(fib[h].size()) - 1;
  DensePoly power_product = std::move(current);
  std::vector<int> power_factors = std::move(factors);
  while (static_cast<int>(power_product.size()) - 1 <= max_degree) {
    generate_products_rec(h + 1, max_h, max_degree, fib, power_product,
                          power_factors, catalog);
    if (static_cast<int>(power_product.size()) - 1 + factor_degree > max_degree) break;
    power_product = multiply(power_product, fib[h]);
    power_factors.push_back(h);
  }
}

ProductCatalog allowed_products(const std::vector<DensePoly>& fib) {
  ProductCatalog catalog;
  generate_products_rec(2, 2 * MAX_T_DEG + 1, MAX_T_DEG, fib, {1}, {}, catalog);
  return catalog;
}

std::vector<Id> lower_ids_from_word(
    int n, const std::vector<std::uint8_t>& word,
    const std::unordered_map<Code, Id>& ids) {
  std::unordered_set<Code> lower{identity_code(n)};
  for (std::uint8_t s : word) {
    std::vector<Code> old(lower.begin(), lower.end());
    for (Code p : old) lower.insert(right_multiply(p, s));
  }
  std::vector<Id> ans;
  ans.reserve(lower.size());
  for (Code p : lower) {
    const auto it = ids.find(p);
    if (it == ids.end()) throw std::runtime_error("subword element absent from top interval");
    ans.push_back(it->second);
  }
  std::sort(ans.begin(), ans.end());
  return ans;
}

const Poly* lookup(const std::vector<Block>& blocks, Id upper, Id lower) {
  const Block& block = blocks.at(upper);
  const auto it = std::lower_bound(block.lowers.begin(), block.lowers.end(), lower);
  if (it == block.lowers.end() || *it != lower) return nullptr;
  return &block.values[static_cast<std::size_t>(it - block.lowers.begin())];
}

std::string factor_pattern(const std::vector<int>& factors) {
  if (factors.empty()) return "empty";
  std::ostringstream out;
  for (std::size_t i = 0; i < factors.size(); ++i) {
    if (i) out << '*';
    out << 'F' << factors[i];
  }
  return out.str();
}

void digest_byte(std::uint64_t& digest, std::uint8_t x) {
  digest ^= x;
  digest *= 1099511628211ULL;
}

template <typename T>
void digest_scalar(std::uint64_t& digest, T x) {
  for (std::size_t k = 0; k < sizeof(T); ++k)
    digest_byte(digest, static_cast<std::uint8_t>((x >> (8 * k)) & T(0xff)));
}

RunResult run_n(int n, const std::vector<DensePoly>& fib,
                const ProductCatalog& catalog, std::vector<Failure>& failures) {
  const auto started = std::chrono::steady_clock::now();
  const auto omega = omega_word(n);
  auto subword_map = enumerate_subwords(n, omega);
  const Code top = apply_word(identity_code(n), omega);
  const auto cover_set = cover_lower_interval(top, n);
  bool cover_ok = cover_set.size() == subword_map.size();
  if (cover_ok) {
    for (const auto& [p, unused] : subword_map) {
      (void)unused;
      if (cover_set.find(p) == cover_set.end()) {
        cover_ok = false;
        break;
      }
    }
  }
  if (!cover_ok) throw std::runtime_error("independent top-interval enumerations disagree");

  std::vector<Element> elements;
  elements.reserve(subword_map.size());
  for (auto& [p, word] : subword_map) {
    elements.push_back({p, std::move(word), static_cast<std::uint8_t>(inversion_length(p, n))});
  }
  std::sort(elements.begin(), elements.end(), [](const Element& a, const Element& b) {
    if (a.length != b.length) return a.length < b.length;
    return a.code < b.code;
  });
  if (elements.size() > std::numeric_limits<Id>::max())
    throw std::runtime_error("element ID type too small");
  std::unordered_map<Code, Id> ids;
  ids.reserve(elements.size() * 2);
  for (std::size_t i = 0; i < elements.size(); ++i)
    ids.emplace(elements[i].code, static_cast<Id>(i));

  std::vector<Block> blocks(elements.size());
  RunResult result;
  result.n = n;
  result.elements = elements.size();
  result.top_interval_cover_count = cover_set.size();
  result.cover_crosscheck = cover_ok;
  result.digest = 1469598103934665603ULL;

  for (std::size_t vi = 0; vi < elements.size(); ++vi) {
    const Id vid = static_cast<Id>(vi);
    const Element& v = elements[vi];
    Block& current = blocks[vi];
    current.lowers = lower_ids_from_word(n, v.reduced_word, ids);
    current.values.resize(current.lowers.size());
    result.comparable_pairs += current.lowers.size();

    int descent = 0;
    if (v.length > 0) {
      for (int s = 1; s < n; ++s) {
        if (at(v.code, s - 1) > at(v.code, s)) {
          descent = s;
          break;
        }
      }
      if (descent == 0) throw std::runtime_error("nonidentity permutation has no descent");
    }
    Id vsid = 0;
    if (descent) {
      const auto it = ids.find(right_multiply(v.code, descent));
      if (it == ids.end()) throw std::runtime_error("vs absent from interval");
      vsid = it->second;
      if (elements[vsid].length + 1 != v.length || vsid >= vid)
        throw std::runtime_error("upper recurrence did not decrease length/order");
    }

    for (std::size_t pos = 0; pos < current.lowers.size(); ++pos) {
      const Id uid = current.lowers[pos];
      const Element& u = elements[uid];
      const int diff = int(v.length) - int(u.length);
      if (diff < 0 || diff > MAX_Q_DEG) throw std::runtime_error("invalid length difference");
      Poly value{};
      if (uid == vid) {
        value[0] = 1;
      } else if (at(u.code, descent - 1) > at(u.code, descent)) {
        const auto us_it = ids.find(right_multiply(u.code, descent));
        if (us_it == ids.end()) throw std::runtime_error("us absent from top interval");
        const Poly* source = lookup(blocks, vsid, us_it->second);
        if (!source) throw std::runtime_error("descent recurrence source absent");
        value = *source;
      } else {
        const Poly* q_term = lookup(blocks, vsid, uid);
        if (!q_term) throw std::runtime_error("lifting-property q-term absent");
        value = *q_term;
        const auto us_it = ids.find(right_multiply(u.code, descent));
        if (us_it != ids.end()) {
          const Poly* shifted = lookup(blocks, vsid, us_it->second);
          if (shifted) {
            for (int j = 0; j < MAX_T_DEG; ++j) {
              const std::uint64_t sum = std::uint64_t(value[j + 1]) + (*shifted)[j];
              if (sum > std::numeric_limits<Coeff>::max())
                throw std::overflow_error("Rtilde coefficient overflow");
              value[j + 1] = static_cast<Coeff>(sum);
            }
          }
        }
      }
      if (value[0] != 1) throw std::runtime_error("normalized leading coefficient is not one");
      for (Coeff c : value) result.max_coefficient = std::max(result.max_coefficient, c);
      current.values[pos] = value;

      DensePoly normalized(value.begin(), value.begin() + diff / 2 + 1);
      normalized = trim(std::move(normalized));
      const auto factor_it = catalog.find(normalized);
      if (factor_it == catalog.end()) {
        ++result.rejected_pairs;
        if (failures.size() < 100) {
          failures.push_back({n, decode(u.code, n), decode(v.code, n), u.length,
                              v.length, normalized});
        }
      } else {
        ++result.factor_patterns[factor_pattern(factor_it->second)];
      }
      digest_scalar(result.digest, static_cast<std::uint16_t>(uid));
      digest_scalar(result.digest, static_cast<std::uint16_t>(vid));
      digest_scalar(result.digest, static_cast<std::uint8_t>(normalized.size()));
      for (Coeff c : normalized) digest_scalar(result.digest, c);
    }
  }

  const Id top_id = ids.at(top);
  const Id identity_id = ids.at(identity_code(n));
  const Poly* top_value = lookup(blocks, top_id, identity_id);
  if (!top_value) throw std::runtime_error("top value absent");
  DensePoly actual(top_value->begin(), top_value->begin() + (2 * (n - 2)) / 2 + 1);
  actual = trim(std::move(actual));
  result.top_fibonacci_check = actual == fib[n - 2];
  if (!result.top_fibonacci_check)
    throw std::runtime_error("known top-endpoint q-Fibonacci formula failed");

  const auto stopped = std::chrono::steady_clock::now();
  result.seconds = std::chrono::duration<double>(stopped - started).count();
  return result;
}

void write_int_array(std::ostream& out, const std::vector<int>& values) {
  out << '[';
  for (std::size_t i = 0; i < values.size(); ++i) {
    if (i) out << ',';
    out << values[i];
  }
  out << ']';
}

void write_coeff_array(std::ostream& out, const DensePoly& values) {
  out << '[';
  for (std::size_t i = 0; i < values.size(); ++i) {
    if (i) out << ',';
    out << values[i];
  }
  out << ']';
}

void write_summary(const std::string& path, const std::string& started,
                   const std::string& finished, std::size_t catalog_size,
                   const std::vector<RunResult>& results) {
  std::ofstream out(path);
  if (!out) throw std::runtime_error("cannot open summary output");
  out << "{\n  \"schema_version\": 1,\n";
  out << "  \"status\": \"discovery_only_not_a_certificate\",\n";
  out << "  \"started_utc\": \"" << started << "\",\n";
  out << "  \"finished_utc\": \"" << finished << "\",\n";
  out << "  \"compiler\": \"" << __VERSION__ << "\",\n";
  out << "  \"cplusplus\": " << __cplusplus << ",\n";
  out << "  \"coefficient_type_bits\": " << 8 * sizeof(Coeff) << ",\n";
  out << "  \"coefficient_overflow_policy\": \"guarded_abort_before_storage\",\n";
  out << "  \"allowed_product_catalog_size\": " << catalog_size << ",\n";
  out << "  \"runs\": [\n";
  for (std::size_t i = 0; i < results.size(); ++i) {
    const auto& r = results[i];
    out << "    {\"n\":" << r.n << ",\"elements\":" << r.elements
        << ",\"comparable_pairs\":" << r.comparable_pairs
        << ",\"rejected_pairs\":" << r.rejected_pairs
        << ",\"max_coefficient\":" << r.max_coefficient
        << ",\"top_interval_cover_count\":" << r.top_interval_cover_count
        << ",\"cover_crosscheck\":" << (r.cover_crosscheck ? "true" : "false")
        << ",\"top_fibonacci_check\":" << (r.top_fibonacci_check ? "true" : "false")
        << ",\"fnv1a64_digest\":\"" << std::hex << std::setw(16)
        << std::setfill('0') << r.digest << std::dec << std::setfill(' ')
        << "\",\"seconds\":" << std::fixed << std::setprecision(6) << r.seconds
        << ",\"factor_patterns\":{";
    bool first = true;
    for (const auto& [pattern, count] : r.factor_patterns) {
      if (!first) out << ',';
      first = false;
      out << '\"' << pattern << "\":" << count;
    }
    out << "}}" << (i + 1 == results.size() ? "\n" : ",\n");
  }
  out << "  ]\n}\n";
}

void write_failures(const std::string& path, const std::vector<Failure>& failures) {
  std::ofstream out(path);
  if (!out) throw std::runtime_error("cannot open failure output");
  out << "{\n  \"status\": \"raw_discovery_candidates_not_certificates\",\n";
  out << "  \"retention_limit\": 100,\n  \"candidates\": [\n";
  for (std::size_t i = 0; i < failures.size(); ++i) {
    const auto& f = failures[i];
    out << "    {\"n\":" << f.n << ",\"u\":";
    write_int_array(out, f.u);
    out << ",\"v\":";
    write_int_array(out, f.v);
    out << ",\"length_u\":" << f.len_u << ",\"length_v\":" << f.len_v
        << ",\"g\":" << f.len_v - f.len_u << ",\"normalized_t_coefficients\":";
    write_coeff_array(out, f.normalized);
    out << '}';
    out << (i + 1 == failures.size() ? "\n" : ",\n");
  }
  out << "  ]\n}\n";
}

}  // namespace

int main(int argc, char** argv) {
  try {
    if (argc != 3) {
      std::cerr << "usage: exhaustive_rtilde SUMMARY_JSON CANDIDATE_JSON\n";
      return 2;
    }
    const std::string started = utc_now();
    const auto fib = fibonacci_polynomials(2 * MAX_T_DEG + 1);
    const auto catalog = allowed_products(fib);
    std::vector<RunResult> results;
    std::vector<Failure> failures;
    for (int n = 2; n <= MAX_N; ++n) {
      RunResult r = run_n(n, fib, catalog, failures);
      std::cout << "n=" << n << " elements=" << r.elements
                << " pairs=" << r.comparable_pairs
                << " rejected=" << r.rejected_pairs
                << " max_coeff=" << r.max_coefficient
                << " seconds=" << std::fixed << std::setprecision(3) << r.seconds << '\n';
      results.push_back(std::move(r));
    }
    const std::string finished = utc_now();
    write_summary(argv[1], started, finished, catalog.size(), results);
    if (!failures.empty()) write_failures(argv[2], failures);
    return failures.empty() ? 0 : 1;
  } catch (const std::exception& ex) {
    std::cerr << "fatal: " << ex.what() << '\n';
    return 3;
  }
}
