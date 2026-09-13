#include <gmpxx.h>

#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

using Mask = unsigned __int128;

unsigned lowest_index(Mask mask) {
  const std::uint64_t low = static_cast<std::uint64_t>(mask);
  if (low != 0) return static_cast<unsigned>(__builtin_ctzll(low));
  const std::uint64_t high = static_cast<std::uint64_t>(mask >> 64);
  return 64U + static_cast<unsigned>(__builtin_ctzll(high));
}

std::uint64_t popcount(Mask mask) {
  return static_cast<std::uint64_t>(
      __builtin_popcountll(static_cast<std::uint64_t>(mask)) +
      __builtin_popcountll(static_cast<std::uint64_t>(mask >> 64)));
}

struct Counters {
  std::uint64_t nodes = 0;
  std::uint64_t ratio_prunes = 0;
  std::uint64_t conflict_eliminations = 0;
  std::uint64_t exact_tests = 0;
  std::uint64_t solutions = 0;
};

struct Search {
  int bound;
  std::vector<int> primes;
  std::vector<Mask> future_conflicts;
  mpz_class all_numerator = 1;
  mpz_class all_denominator = 1;
  Counters count;

  explicit Search(int b) : bound(b) {
    if (bound < 3) throw std::invalid_argument("bound must be at least 3");
    std::vector<bool> is_prime(bound + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int p = 2; p * p <= bound; ++p) {
      if (!is_prime[p]) continue;
      for (int m = p * p; m <= bound; m += p) is_prime[m] = false;
    }
    for (int p = 3; p <= bound; p += 2) {
      if (is_prime[p]) primes.push_back(p);
    }
    if (primes.size() > 127) {
      throw std::invalid_argument("this verifier supports at most 127 odd primes");
    }

    future_conflicts.assign(primes.size(), 0);
    for (std::size_t i = 0; i < primes.size(); ++i) {
      for (std::size_t j = i + 1; j < primes.size(); ++j) {
        if ((primes[j] - 1) % primes[i] == 0) {
          future_conflicts[i] |= (Mask{1} << j);
        }
      }
    }

    for (int p : primes) {
      all_numerator *= p;
      all_denominator *= p - 1;
    }
  }

  bool optimistic_ratio_at_most_two(const mpz_class& n, const mpz_class& phi,
                                    const mpz_class& available_numerator,
                                    const mpz_class& available_denominator) const {
    // The product over all compatible, undecided primes is a rigorous upper
    // bound for every completion of this node.
    return n * available_numerator <= 2 * phi * available_denominator;
  }

  void remove_factors(Mask removed, mpz_class& numerator,
                      mpz_class& denominator) const {
    while (removed != 0) {
      const unsigned i = lowest_index(removed);
      removed &= removed - 1;
      numerator /= primes[i];
      denominator /= primes[i] - 1;
    }
  }

  void dfs(Mask available, const mpz_class& available_numerator,
           const mpz_class& available_denominator, const mpz_class& n,
           const mpz_class& phi, unsigned selected, Mask selected_mask,
           bool test_current) {
    ++count.nodes;

    if (test_current && selected >= 2 && n > 2 * phi) {
      ++count.exact_tests;
      if ((n - 1) % phi == 0) {
        ++count.solutions;
        std::cout << "solution_factors=";
        bool first = true;
        for (std::size_t j = 0; j < primes.size(); ++j) {
          if ((selected_mask & (Mask{1} << j)) == 0) continue;
          std::cout << (first ? "" : ",") << primes[j];
          first = false;
        }
        std::cout << " n=" << n << " phi=" << phi
                  << " index=" << (n - 1) / phi << '\n';
      }
    }

    if (available == 0) return;
    if (optimistic_ratio_at_most_two(n, phi, available_numerator,
                                     available_denominator)) {
      ++count.ratio_prunes;
      return;
    }

    const unsigned i = lowest_index(available);
    const Mask bit = Mask{1} << i;

    mpz_class exclude_numerator = available_numerator;
    mpz_class exclude_denominator = available_denominator;
    remove_factors(bit, exclude_numerator, exclude_denominator);

    const Mask conflicts = future_conflicts[i] & available;
    count.conflict_eliminations += popcount(conflicts);
    mpz_class include_numerator = exclude_numerator;
    mpz_class include_denominator = exclude_denominator;
    remove_factors(conflicts, include_numerator, include_denominator);
    dfs(available & ~bit & ~conflicts, include_numerator, include_denominator,
        n * primes[i], phi * (primes[i] - 1), selected + 1,
        selected_mask | bit, true);

    dfs(available & ~bit, exclude_numerator, exclude_denominator, n, phi,
        selected, selected_mask, false);
  }

  void run() {
    const Mask available = (Mask{1} << primes.size()) - 1;
    dfs(available, all_numerator, all_denominator, mpz_class{1}, mpz_class{1},
        0, Mask{0}, false);
  }
};

}  // namespace

int main(int argc, char** argv) {
  try {
    if (argc != 2) {
      std::cerr << "usage: search_bounded_prime_sets PRIME_BOUND\n";
      return 2;
    }
    const int bound = std::stoi(argv[1]);
    Search search(bound);
    const auto start = std::chrono::steady_clock::now();
    search.run();
    const auto stop = std::chrono::steady_clock::now();
    const std::chrono::duration<double> elapsed = stop - start;
    std::cout << "bound=" << bound << '\n'
              << "odd_primes=" << search.primes.size() << '\n'
              << "nodes=" << search.count.nodes << '\n'
              << "ratio_prunes=" << search.count.ratio_prunes << '\n'
              << "conflict_eliminations="
              << search.count.conflict_eliminations << '\n'
              << "exact_tests=" << search.count.exact_tests << '\n'
              << "solutions=" << search.count.solutions << '\n'
              << "elapsed_seconds=" << elapsed.count() << '\n';
    return search.count.solutions == 0 ? 0 : 1;
  } catch (const std::exception& e) {
    std::cerr << "error: " << e.what() << '\n';
    return 2;
  }
}
