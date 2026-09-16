// Independent exhaustive verifier: all n! permutations, direct subsequences.
#include <algorithm>
#include <fstream>
#include <iostream>
#include <numeric>
#include <vector>

bool has312(const std::vector<int>& p) {
  int n = p.size();
  for (int i = 0; i < n; ++i)
    for (int j = i + 1; j < n; ++j)
      if (p[i] > p[j])
        for (int k = j + 1; k < n; ++k)
          if (p[i] > p[k] && p[k] > p[j]) return true;
  return false;
}

bool has54321(const std::vector<int>& p) {
  int n = p.size();
  for (int a = 0; a < n; ++a)
    for (int b = a + 1; b < n; ++b) if (p[a] > p[b])
      for (int c = b + 1; c < n; ++c) if (p[b] > p[c])
        for (int d = c + 1; d < n; ++d) if (p[c] > p[d])
          for (int e = d + 1; e < n; ++e)
            if (p[d] > p[e]) return true;
  return false;
}

bool has132(const std::vector<int>& p) {
  int n = p.size();
  for (int i = 0; i < n; ++i)
    for (int j = i + 1; j < n; ++j)
      for (int k = j + 1; k < n; ++k)
        if (p[i] < p[k] && p[k] < p[j]) return true;
  return false;
}

int main() {
  std::ofstream members("evidence/bruteforce_members_n11.txt");
  std::cout << "{\"method\":\"all permutations, explicit subsequence tests\",\"rows\":[\n";
  for (int n = 0; n <= 11; ++n) {
    std::vector<int> p(n), q(n);
    std::iota(p.begin(), p.end(), 1);
    long long examined = 0, pool = 0, valid = 0, ending1 = 0;
    do {
      ++examined;
      if (has312(p) || has54321(p)) continue;
      ++pool;
      for (int i = 0; i < n; ++i) q[i] = p[p[i] - 1];
      if (has132(q)) continue;
      ++valid;
      if (n && p.back() == 1) ++ending1;
      if (n == 11) {
        for (int i = 0; i < n; ++i) members << (i ? " " : "") << p[i];
        members << '\n';
      }
    } while (std::next_permutation(p.begin(), p.end()));
    std::cout << (n ? "," : "") << "{\"n\":" << n
              << ",\"examined\":" << examined << ",\"avoid312_54321\":" << pool
              << ",\"a_n\":" << valid << ",\"b_n_ending_in_1\":" << ending1 << "}\n";
  }
  std::cout << "]}\n";
}
