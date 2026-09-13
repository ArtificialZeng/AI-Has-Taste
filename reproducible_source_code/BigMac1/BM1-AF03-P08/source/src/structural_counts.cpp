#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <set>
#include <vector>

namespace {

using Perm = std::array<std::uint8_t, 10>;

int length(const Perm& w, int n) {
  int ans = 0;
  for (int i = 0; i < n; ++i) {
    for (int j = i + 1; j < n; ++j) ans += (w[i] > w[j]);
  }
  return ans;
}

bool bruhat_leq(const Perm& u, const Perm& v, int n) {
  // Rank-matrix criterion: # {i <= p : u(i) <= r} >= the corresponding
  // number for v, for every prefix p and value threshold r.
  std::array<int, 11> cu{};
  std::array<int, 11> cv{};
  for (int p = 0; p < n; ++p) {
    ++cu[u[p]];
    ++cv[v[p]];
    int su = 0;
    int sv = 0;
    for (int r = 1; r <= n; ++r) {
      su += cu[r];
      sv += cv[r];
      if (su < sv) return false;
    }
  }
  return true;
}

std::vector<Perm> lower_interval(int n) {
  std::vector<int> omega;
  for (int j = 2; j < n; ++j) {
    omega.push_back(j);
    omega.push_back(j - 1);
  }
  std::set<Perm> unique;
  for (std::uint32_t mask = 0; mask < (std::uint32_t{1} << omega.size()); ++mask) {
    Perm w{};
    for (int i = 0; i < 10; ++i) w[i] = static_cast<std::uint8_t>(i + 1);
    for (std::size_t k = 0; k < omega.size(); ++k) {
      if ((mask >> k) & 1U) std::swap(w[omega[k] - 1], w[omega[k]]);
    }
    unique.insert(w);
  }
  return {unique.begin(), unique.end()};
}

}  // namespace

int main() {
  for (int n = 2; n <= 10; ++n) {
    const auto elems = lower_interval(n);
    std::array<std::uint64_t, 17> by_gap{};
    std::uint64_t pairs = 0;
    for (const Perm& v : elems) {
      const int lv = length(v, n);
      for (const Perm& u : elems) {
        if (!bruhat_leq(u, v, n)) continue;
        ++pairs;
        ++by_gap[lv - length(u, n)];
      }
    }
    std::cout << "n=" << n << " elements=" << elems.size()
              << " comparable_pairs=" << pairs << " gaps=";
    for (int d = 0; d <= 2 * n - 4; ++d) {
      if (d) std::cout << ',';
      std::cout << by_gap[d];
    }
    std::cout << '\n';
  }
}
