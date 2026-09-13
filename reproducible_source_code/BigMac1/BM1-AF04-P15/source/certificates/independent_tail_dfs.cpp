#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

struct Counts {
  std::uint64_t nodes = 1;
  std::uint64_t leaves = 0;
  int maximum_length = 0;
  std::vector<std::string> maximizers;
};

std::string encode(const std::vector<int>& word) {
  std::string result;
  for (std::size_t i = 0; i < word.size(); ++i) {
    if (i) result += ',';
    result += std::to_string(word[i]);
  }
  return result;
}

// Independent evaluator: rebuild cumulative sums from the right-hand end of
// the current word.  It does not use the discovery program's prefix sums.
bool good_suffix(const std::vector<int>& word) {
  const std::size_t n = word.size();
  std::vector<std::int64_t> tail(n + 1, 0);
  for (std::size_t k = 1; k <= n; ++k) {
    tail[k] = tail[k - 1] + word[n - k];
  }
  for (std::size_t h = 1; 2 * h <= n; ++h) {
    const std::int64_t right = tail[h];
    const std::int64_t left = tail[2 * h] - tail[h];
    if (left == right) return false;
  }
  return true;
}

void enumerate(const std::vector<int>& alphabet, std::vector<int>& word,
               Counts& counts) {
  bool has_child = false;
  for (const int value : alphabet) {
    word.push_back(value);
    if (good_suffix(word)) {
      has_child = true;
      ++counts.nodes;
      enumerate(alphabet, word, counts);
    }
    word.pop_back();
  }
  if (!has_child) {
    ++counts.leaves;
    const int length = static_cast<int>(word.size());
    if (length > counts.maximum_length) {
      counts.maximum_length = length;
      counts.maximizers.assign(1, encode(word));
    } else if (length == counts.maximum_length) {
      counts.maximizers.push_back(encode(word));
    }
  }
}

std::vector<int> read_alphabet(int argc, char** argv) {
  if (argc < 2) throw std::invalid_argument("alphabet required");
  std::vector<int> alphabet;
  for (int i = 1; i < argc; ++i) alphabet.push_back(std::stoi(argv[i]));
  if (!std::is_sorted(alphabet.begin(), alphabet.end()) ||
      std::adjacent_find(alphabet.begin(), alphabet.end()) != alphabet.end()) {
    throw std::invalid_argument("alphabet must be strictly increasing");
  }
  if (alphabet.front() != 0) throw std::invalid_argument("alphabet not normalized");
  int divisor = 0;
  for (const int value : alphabet) divisor = std::gcd(divisor, value);
  if (divisor != 1 && alphabet.size() > 1) {
    throw std::invalid_argument("alphabet not primitive");
  }
  return alphabet;
}

}  // namespace

int main(int argc, char** argv) {
  try {
    const std::vector<int> alphabet = read_alphabet(argc, argv);
    Counts counts;
    std::vector<int> word;
    enumerate(alphabet, word, counts);
    std::sort(counts.maximizers.begin(), counts.maximizers.end());
    std::cout << "nodes=" << counts.nodes << '\n'
              << "leaves=" << counts.leaves << '\n'
              << "maximum_length=" << counts.maximum_length << '\n'
              << "maximizer_count=" << counts.maximizers.size() << '\n';
    for (const std::string& word_string : counts.maximizers) {
      std::cout << "maximizer=" << word_string << '\n';
    }
    return EXIT_SUCCESS;
  } catch (const std::exception& error) {
    std::cerr << "verification error: " << error.what() << '\n';
    return EXIT_FAILURE;
  }
}
