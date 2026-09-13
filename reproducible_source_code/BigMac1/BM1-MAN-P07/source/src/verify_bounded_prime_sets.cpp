#include <gmpxx.h>

#include <chrono>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

using Mask = unsigned __int128;

unsigned lowest_index(Mask mask) {
  const std::uint64_t low = static_cast<std::uint64_t>(mask);
  if (low != 0) return static_cast<unsigned>(__builtin_ctzll(low));
  return 64U + static_cast<unsigned>(
                   __builtin_ctzll(static_cast<std::uint64_t>(mask >> 64)));
}

unsigned highest_index(Mask mask) {
  const std::uint64_t high = static_cast<std::uint64_t>(mask >> 64);
  if (high != 0) {
    return 127U - static_cast<unsigned>(__builtin_clzll(high));
  }
  return 63U - static_cast<unsigned>(
                   __builtin_clzll(static_cast<std::uint64_t>(mask)));
}

struct Verifier {
  std::vector<int> primes;
  std::vector<Mask> incompatible;
  mpz_class universe_n = 1;
  mpz_class universe_phi = 1;
  std::uint64_t nodes = 0;
  std::uint64_t prunes = 0;
  std::uint64_t exact_tests = 0;
  std::uint64_t solutions = 0;

  explicit Verifier(int bound) {
    if (bound < 3) throw std::invalid_argument("bound must be at least 3");
    std::vector<bool> sieve(bound + 1, true);
    sieve[0] = sieve[1] = false;
    for (int d = 2; d * d <= bound; ++d) {
      if (!sieve[d]) continue;
      for (int m = d * d; m <= bound; m += d) sieve[m] = false;
    }
    for (int p = 3; p <= bound; p += 2) {
      if (sieve[p]) primes.push_back(p);
    }
    if (primes.size() > 127) {
      throw std::invalid_argument("this verifier supports at most 127 odd primes");
    }

    incompatible.assign(primes.size(), 0);
    for (std::size_t i = 0; i < primes.size(); ++i) {
      universe_n *= primes[i];
      universe_phi *= primes[i] - 1;
      for (std::size_t j = 0; j < i; ++j) {
        if ((primes[i] - 1) % primes[j] == 0) {
          incompatible[i] |= Mask{1} << j;
          incompatible[j] |= Mask{1} << i;
        }
      }
    }
  }

  void divide_mask(Mask mask, mpz_class& a, mpz_class& b) const {
    while (mask != 0) {
      const unsigned j = lowest_index(mask);
      mask &= mask - 1;
      a /= primes[j];
      b /= primes[j] - 1;
    }
  }

  void inspect_fresh_candidate(const mpz_class& n, const mpz_class& phi,
                               unsigned selected) {
    if (selected < 2 || n <= 2 * phi) return;
    ++exact_tests;
    const mpz_class index = n / phi;
    // This is a second exact evaluator: it reconstructs the defining equality
    // from the floor quotient instead of taking a remainder of n-1.
    if (index * phi + 1 == n) ++solutions;
  }

  void visit(Mask undecided, const mpz_class& undecided_n,
             const mpz_class& undecided_phi, const mpz_class& n,
             const mpz_class& phi, unsigned selected, bool fresh) {
    ++nodes;
    if (fresh) inspect_fresh_candidate(n, phi, selected);
    if (undecided == 0) return;

    if (n * undecided_n <= 2 * phi * undecided_phi) {
      ++prunes;
      return;
    }

    // Deliberately branch from the largest prime downward.  This makes the
    // enumeration order independent of the forward search implementation.
    const unsigned i = highest_index(undecided);
    const Mask bit = Mask{1} << i;

    mpz_class without_i_n = undecided_n;
    mpz_class without_i_phi = undecided_phi;
    divide_mask(bit, without_i_n, without_i_phi);

    const Mask killed = undecided & incompatible[i];
    mpz_class include_n = without_i_n;
    mpz_class include_phi = without_i_phi;
    divide_mask(killed, include_n, include_phi);
    visit(undecided & ~bit & ~killed, include_n, include_phi, n * primes[i],
          phi * (primes[i] - 1), selected + 1, true);

    visit(undecided & ~bit, without_i_n, without_i_phi, n, phi, selected,
          false);
  }

  void run() {
    const Mask all = (Mask{1} << primes.size()) - 1;
    visit(all, universe_n, universe_phi, mpz_class{1}, mpz_class{1}, 0,
          false);
  }
};

}  // namespace

int main(int argc, char** argv) {
  try {
    if (argc != 2) {
      std::cerr << "usage: verify_bounded_prime_sets PRIME_BOUND\n";
      return 2;
    }
    const int bound = std::stoi(argv[1]);
    Verifier verifier(bound);
    const auto start = std::chrono::steady_clock::now();
    verifier.run();
    const std::chrono::duration<double> elapsed =
        std::chrono::steady_clock::now() - start;
    std::cout << "bound=" << bound << '\n'
              << "odd_primes=" << verifier.primes.size() << '\n'
              << "nodes=" << verifier.nodes << '\n'
              << "ratio_prunes=" << verifier.prunes << '\n'
              << "exact_tests=" << verifier.exact_tests << '\n'
              << "solutions=" << verifier.solutions << '\n'
              << "elapsed_seconds=" << elapsed.count() << '\n';
    return verifier.solutions == 0 ? 0 : 1;
  } catch (const std::exception& e) {
    std::cerr << "error: " << e.what() << '\n';
    return 2;
  }
}
