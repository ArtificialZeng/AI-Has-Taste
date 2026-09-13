// Exact exhaustive weak-abelian-square test on h^4(0), with an h^3 cross-check.
//
// For a fixed split q, a left interval [p,q) and a right interval [q,r)
// have the same normalized Parikh vector iff their five counts, divided by
// their gcd, give the same primitive signature.  The loops below insert every
// left signature and query every right signature, so a completed sweep covers
// every 0 <= p < q < r <= |h^k(0)| exactly at its unique split q.

#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <sstream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <vector>

namespace {

constexpr std::array<std::uint8_t, 14> BASE = {
    0, 1, 2, 1, 3, 1, 0, 1, 3, 1, 4, 3, 1, 0};

struct Signature {
  std::uint64_t lo;
  std::uint16_t hi;
};

struct Witness {
  bool found = false;
  std::uint32_t p = 0;
  std::uint32_t q = 0;
  std::uint32_t r = 0;
  std::array<std::uint32_t, 5> x{};
  std::array<std::uint32_t, 5> y{};
  Signature signature{};
};

std::vector<std::uint8_t> morph(const std::vector<std::uint8_t>& word) {
  std::vector<std::uint8_t> out;
  out.reserve(word.size() * BASE.size());
  for (std::uint8_t a : word) {
    for (std::uint8_t b : BASE) out.push_back((a + b) % 5);
  }
  return out;
}

std::vector<std::uint8_t> iterate(int power) {
  std::vector<std::uint8_t> word{0};
  for (int k = 0; k < power; ++k) word = morph(word);
  return word;
}

inline Signature primitive_signature(
    const std::array<std::uint32_t, 5>& c, std::uint32_t length) {
  // gcd(c[0],...,c[4]) = gcd(length,c[0],...,c[3]).  Starting with
  // length usually reaches 1 after only one or two gcd calls.
  std::uint32_t g = std::gcd(length, c[0]);
  if (g != 1) g = std::gcd(g, c[1]);
  if (g != 1) g = std::gcd(g, c[2]);
  if (g != 1) g = std::gcd(g, c[3]);

  std::uint32_t a0 = c[0], a1 = c[1], a2 = c[2], a3 = c[3], a4 = c[4];
  if (g != 1) {
    a0 /= g;
    a1 /= g;
    a2 /= g;
    a3 /= g;
    a4 /= g;
  }
  return {static_cast<std::uint64_t>(a0) |
              (static_cast<std::uint64_t>(a1) << 16) |
              (static_cast<std::uint64_t>(a2) << 32) |
              (static_cast<std::uint64_t>(a3) << 48),
          static_cast<std::uint16_t>(a4)};
}

inline std::uint64_t hash_signature(Signature s) {
  // Exactness comes from key comparison; this mixer only selects probe slots.
  std::uint64_t x = s.lo ^ (static_cast<std::uint64_t>(s.hi) *
                            UINT64_C(0x9e3779b97f4a7c15));
  x ^= x >> 30;
  x *= UINT64_C(0xbf58476d1ce4e5b9);
  x ^= x >> 27;
  x *= UINT64_C(0x94d049bb133111eb);
  return x ^ (x >> 31);
}

class EpochHashTable {
 public:
  explicit EpochHashTable(std::size_t maximum_items) {
    std::size_t capacity = 16;
    while (capacity < 4 * maximum_items) capacity *= 2;
    lo_.resize(capacity);
    hi_.resize(capacity);
    position_.resize(capacity);
    stamp_.assign(capacity, 0);
  }

  void begin_split(std::size_t items) {
    ++epoch_;
    capacity_ = 16;
    while (capacity_ < 4 * std::max<std::size_t>(items, 1)) capacity_ *= 2;
    mask_ = capacity_ - 1;
  }

  void insert_if_absent(Signature key, std::uint32_t p) {
    std::size_t slot = hash_signature(key) & mask_;
    while (stamp_[slot] == epoch_) {
      if (lo_[slot] == key.lo && hi_[slot] == key.hi) return;
      slot = (slot + 1) & mask_;
    }
    stamp_[slot] = epoch_;
    lo_[slot] = key.lo;
    hi_[slot] = key.hi;
    position_[slot] = p;
  }

  bool find(Signature key, std::uint32_t& p) const {
    std::size_t slot = hash_signature(key) & mask_;
    while (stamp_[slot] == epoch_) {
      if (lo_[slot] == key.lo && hi_[slot] == key.hi) {
        p = position_[slot];
        return true;
      }
      slot = (slot + 1) & mask_;
    }
    return false;
  }

 private:
  std::vector<std::uint64_t> lo_;
  std::vector<std::uint16_t> hi_;
  std::vector<std::uint32_t> position_;
  std::vector<std::uint32_t> stamp_;
  std::uint32_t epoch_ = 0;
  std::size_t capacity_ = 0;
  std::size_t mask_ = 0;
};

struct SweepResult {
  Witness witness;
  std::uint64_t left_signatures_inserted = 0;
  std::uint64_t right_signatures_queried = 0;
  std::uint32_t splits_completed = 0;
  double seconds = 0.0;
};

SweepResult sweep(const std::vector<std::uint8_t>& word) {
  const std::uint32_t n = static_cast<std::uint32_t>(word.size());
  EpochHashTable table(n);
  SweepResult result;
  const auto started = std::chrono::steady_clock::now();

  for (std::uint32_t q = 1; q < n; ++q) {
    table.begin_split(q);
    std::array<std::uint32_t, 5> counts{};
    for (std::uint32_t p = q; p-- > 0;) {
      ++counts[word[p]];
      Signature sig = primitive_signature(counts, q - p);
      table.insert_if_absent(sig, p);
      ++result.left_signatures_inserted;
    }

    counts.fill(0);
    for (std::uint32_t r = q + 1; r <= n; ++r) {
      ++counts[word[r - 1]];
      Signature sig = primitive_signature(counts, r - q);
      ++result.right_signatures_queried;
      std::uint32_t p = 0;
      if (table.find(sig, p)) {
        Witness& w = result.witness;
        w.found = true;
        w.p = p;
        w.q = q;
        w.r = r;
        w.signature = sig;
        for (std::uint32_t i = p; i < q; ++i) ++w.x[word[i]];
        for (std::uint32_t i = q; i < r; ++i) ++w.y[word[i]];
        const std::uint32_t m = q - p, ell = r - q;
        for (int i = 0; i < 5; ++i) {
          if (static_cast<std::uint64_t>(ell) * w.x[i] !=
              static_cast<std::uint64_t>(m) * w.y[i]) {
            throw std::runtime_error("internal exact-witness check failed");
          }
        }
        result.seconds = std::chrono::duration<double>(
                             std::chrono::steady_clock::now() - started)
                             .count();
        return result;
      }
    }
    result.splits_completed = q;
    if (q % 1000 == 0) {
      const double elapsed = std::chrono::duration<double>(
                                 std::chrono::steady_clock::now() - started)
                                 .count();
      std::cerr << "q=" << q << '/' << (n - 1) << " elapsed=" << elapsed
                << "s\n";
    }
  }
  result.seconds = std::chrono::duration<double>(
                       std::chrono::steady_clock::now() - started)
                       .count();
  return result;
}

// Small self-contained SHA-256 implementation, used only to bind the exact
// raw-byte word (letters are bytes 0,...,4) reported in the certificate.
class Sha256 {
 public:
  void update(const std::uint8_t* data, std::size_t len) {
    bit_length_ += static_cast<std::uint64_t>(len) * 8;
    while (len > 0) {
      const std::size_t take = std::min(len, 64 - buffer_length_);
      std::copy(data, data + take, buffer_.begin() + buffer_length_);
      buffer_length_ += take;
      data += take;
      len -= take;
      if (buffer_length_ == 64) {
        transform(buffer_.data());
        buffer_length_ = 0;
      }
    }
  }

  std::string finish() {
    buffer_[buffer_length_++] = 0x80;
    if (buffer_length_ > 56) {
      std::fill(buffer_.begin() + buffer_length_, buffer_.end(), 0);
      transform(buffer_.data());
      buffer_length_ = 0;
    }
    std::fill(buffer_.begin() + buffer_length_, buffer_.begin() + 56, 0);
    for (int i = 0; i < 8; ++i)
      buffer_[63 - i] = static_cast<std::uint8_t>(bit_length_ >> (8 * i));
    transform(buffer_.data());
    std::ostringstream out;
    out << std::hex << std::setfill('0');
    for (std::uint32_t x : state_) out << std::setw(8) << x;
    return out.str();
  }

 private:
  static constexpr std::array<std::uint32_t, 64> K = {
      0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b,
      0x59f111f1, 0x923f82a4, 0xab1c5ed5, 0xd807aa98, 0x12835b01,
      0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7,
      0xc19bf174, 0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
      0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 0x983e5152,
      0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147,
      0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc,
      0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
      0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819,
      0xd6990624, 0xf40e3585, 0x106aa070, 0x19a4c116, 0x1e376c08,
      0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f,
      0x682e6ff3, 0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
      0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2};

  static std::uint32_t rotr(std::uint32_t x, int n) {
    return (x >> n) | (x << (32 - n));
  }
  void transform(const std::uint8_t* block) {
    std::uint32_t w[64];
    for (int i = 0; i < 16; ++i)
      w[i] = (static_cast<std::uint32_t>(block[4 * i]) << 24) |
             (static_cast<std::uint32_t>(block[4 * i + 1]) << 16) |
             (static_cast<std::uint32_t>(block[4 * i + 2]) << 8) |
             block[4 * i + 3];
    for (int i = 16; i < 64; ++i) {
      const std::uint32_t s0 = rotr(w[i - 15], 7) ^ rotr(w[i - 15], 18) ^
                               (w[i - 15] >> 3);
      const std::uint32_t s1 = rotr(w[i - 2], 17) ^ rotr(w[i - 2], 19) ^
                               (w[i - 2] >> 10);
      w[i] = w[i - 16] + s0 + w[i - 7] + s1;
    }
    auto [a, b, c, d, e, f, g, h] = std::tuple{
        state_[0], state_[1], state_[2], state_[3], state_[4], state_[5],
        state_[6], state_[7]};
    for (int i = 0; i < 64; ++i) {
      const std::uint32_t s1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25);
      const std::uint32_t ch = (e & f) ^ (~e & g);
      const std::uint32_t temp1 = h + s1 + ch + K[i] + w[i];
      const std::uint32_t s0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22);
      const std::uint32_t maj = (a & b) ^ (a & c) ^ (b & c);
      const std::uint32_t temp2 = s0 + maj;
      h = g;
      g = f;
      f = e;
      e = d + temp1;
      d = c;
      c = b;
      b = a;
      a = temp1 + temp2;
    }
    state_[0] += a;
    state_[1] += b;
    state_[2] += c;
    state_[3] += d;
    state_[4] += e;
    state_[5] += f;
    state_[6] += g;
    state_[7] += h;
  }

  std::array<std::uint32_t, 8> state_ = {
      0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
      0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19};
  std::array<std::uint8_t, 64> buffer_{};
  std::size_t buffer_length_ = 0;
  std::uint64_t bit_length_ = 0;
};

std::string sha256(const std::vector<std::uint8_t>& word) {
  Sha256 hash;
  hash.update(word.data(), word.size());
  return hash.finish();
}

std::string json_escape(const std::string& value) {
  std::ostringstream out;
  for (unsigned char c : value) {
    if (c == '"' || c == '\\') out << '\\' << c;
    else if (c >= 0x20) out << c;
    else out << "\\u" << std::hex << std::setw(4) << std::setfill('0')
             << static_cast<int>(c) << std::dec;
  }
  return out.str();
}

std::string letters(const std::vector<std::uint8_t>& word, std::uint32_t a,
                    std::uint32_t b) {
  std::string out;
  out.reserve(b - a);
  for (std::uint32_t i = a; i < b; ++i) out.push_back('0' + word[i]);
  return out;
}

std::string vector_json(const std::array<std::uint32_t, 5>& v) {
  std::ostringstream out;
  out << '[' << v[0] << ", " << v[1] << ", " << v[2] << ", " << v[3]
      << ", " << v[4] << ']';
  return out.str();
}

std::string signature_json(Signature s) {
  std::array<std::uint32_t, 5> v = {
      static_cast<std::uint32_t>(s.lo & 0xffff),
      static_cast<std::uint32_t>((s.lo >> 16) & 0xffff),
      static_cast<std::uint32_t>((s.lo >> 32) & 0xffff),
      static_cast<std::uint32_t>((s.lo >> 48) & 0xffff), s.hi};
  return vector_json(v);
}

void write_result(const std::vector<std::uint8_t>& h3, const SweepResult& r3,
                  const std::vector<std::uint8_t>& h4, const SweepResult& r4,
                  const std::string& output_path) {
  std::ofstream out(output_path);
  if (!out) throw std::runtime_error("cannot open output file");
  out << "{\n"
      << "  \"base\": \"01213101314310\",\n"
      << "  \"method\": \"For each split q, insert the primitive Parikh signature of every factor ending at q into an exact open-addressed hash table, then query the signature of every factor starting at q. Hash collisions are resolved by full packed-signature equality.\",\n"
      << "  \"completeness\": \"Every triple 0 <= p < q < r <= 38416 occurs uniquely at split q. The sweep either returns an exactly rechecked witness or, if completed, has queried every right factor against all left factors at that split.\",\n"
      << "  \"word_encoding_for_digest\": \"raw bytes with values 0,1,2,3,4\",\n"
      << "  \"h3_crosscheck\": {\n"
      << "    \"prefix_length\": " << h3.size() << ",\n"
      << "    \"prefix_sha256\": \"" << sha256(h3) << "\",\n"
      << "    \"expected_prefix_sha256\": \"d75c5ab42c29c34f3b71c5c981cd0c6abf23f40dd10ce9e3ead29a5bdf1e003d\",\n"
      << "    \"outcome\": \""
      << (r3.witness.found ? "violation" : "no_violation_in_finite_prefix")
      << "\",\n"
      << "    \"left_signatures_inserted\": " << r3.left_signatures_inserted
      << ",\n"
      << "    \"right_signatures_queried\": " << r3.right_signatures_queried
      << ",\n"
      << "    \"expected_right_signatures_queried\": 3763396,\n"
      << "    \"seconds\": " << std::fixed << std::setprecision(6)
      << r3.seconds << "\n"
      << "  },\n"
      << "  \"test\": \"all triples 0 <= p < q < r <= 38416 for h^4(0)\",\n"
      << "  \"power\": 4,\n"
      << "  \"prefix_length\": " << h4.size() << ",\n"
      << "  \"prefix_sha256\": \"" << sha256(h4) << "\",\n"
      << "  \"outcome\": \""
      << (r4.witness.found ? "violation" : "no_violation_in_finite_prefix")
      << "\",\n"
      << "  \"splits_completed\": " << r4.splits_completed << ",\n"
      << "  \"left_signatures_inserted_before_stop\": "
      << r4.left_signatures_inserted << ",\n"
      << "  \"right_signatures_queried_before_stop\": "
      << r4.right_signatures_queried << ",\n"
      << "  \"expected_each_side_if_complete\": 737875320,\n"
      << "  \"seconds\": " << r4.seconds << ",\n"
      << "  \"witness\": ";
  if (!r4.witness.found) {
    out << "null\n";
  } else {
    const Witness& w = r4.witness;
    out << "{\n"
        << "    \"p\": " << w.p << ",\n"
        << "    \"q\": " << w.q << ",\n"
        << "    \"r\": " << w.r << ",\n"
        << "    \"m\": " << (w.q - w.p) << ",\n"
        << "    \"n\": " << (w.r - w.q) << ",\n"
        << "    \"x\": \""
        << json_escape(letters(h4, w.p, w.q)) << "\",\n"
        << "    \"y\": \""
        << json_escape(letters(h4, w.q, w.r)) << "\",\n"
        << "    \"parikh_x\": " << vector_json(w.x) << ",\n"
        << "    \"parikh_y\": " << vector_json(w.y) << ",\n"
        << "    \"primitive_signature\": "
        << signature_json(w.signature) << "\n"
        << "  }\n";
  }
  out << "}\n";
}

}  // namespace

int main() {
  try {
    const auto h3 = iterate(3);
    const auto r3 = sweep(h3);
    const std::string h3_digest = sha256(h3);
    if (h3.size() != 2744 ||
        h3_digest !=
            "d75c5ab42c29c34f3b71c5c981cd0c6abf23f40dd10ce9e3ead29a5bdf1e003d" ||
        r3.witness.found || r3.right_signatures_queried != 3763396) {
      throw std::runtime_error("h^3 implementation cross-check failed");
    }
    std::cerr << "h^3 cross-check passed in " << r3.seconds << "s\n";

    const auto h4 = morph(h3);
    if (h4.size() != 38416) throw std::runtime_error("wrong h^4 length");
    const auto r4 = sweep(h4);
    write_result(h3, r3, h4, r4, "evidence/h4_collinearity.json");
    std::cerr << "h^4 sweep finished in " << r4.seconds << "s; outcome="
              << (r4.witness.found ? "violation" : "no violation") << '\n';
    return 0;
  } catch (const std::exception& e) {
    std::cerr << "error: " << e.what() << '\n';
    return 1;
  }
}
