#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

struct Result {
  std::uint64_t nodes = 1;
  std::uint64_t leaves = 0;
  std::uint64_t node_limit = std::numeric_limits<std::uint64_t>::max();
  int maximum_length = 0;
  bool complete = true;
  std::vector<std::uint64_t> depth_histogram{1};
  std::vector<std::string> maximizers;
};

std::string encode_word(const std::vector<int>& word) {
  std::string out;
  for (std::size_t i = 0; i < word.size(); ++i) {
    if (i != 0) out.push_back(',');
    out += std::to_string(word[i]);
  }
  return out;
}

bool creates_additive_square(const std::vector<std::int64_t>& sums) {
  const std::size_t n = sums.size() - 1;
  for (std::size_t h = 1; 2 * h <= n; ++h) {
    const std::int64_t left = sums[n - h] - sums[n - 2 * h];
    const std::int64_t right = sums[n] - sums[n - h];
    if (left == right) return true;
  }
  return false;
}

void search(const std::vector<int>& alphabet, std::vector<int>& word,
            std::vector<std::int64_t>& sums, Result& result) {
  if (!result.complete) return;
  bool extended = false;
  for (const int value : alphabet) {
    sums.push_back(sums.back() + value);
    if (!creates_additive_square(sums)) {
      extended = true;
      word.push_back(value);
      ++result.nodes;
      if (result.nodes > result.node_limit) {
        result.complete = false;
      } else {
        if (result.depth_histogram.size() <= word.size()) {
          result.depth_histogram.resize(word.size() + 1, 0);
        }
        ++result.depth_histogram[word.size()];
        search(alphabet, word, sums, result);
      }
      word.pop_back();
    }
    sums.pop_back();
    if (!result.complete) return;
  }
  if (!extended) {
    ++result.leaves;
    const int length = static_cast<int>(word.size());
    if (length > result.maximum_length) {
      result.maximum_length = length;
      result.maximizers.assign(1, encode_word(word));
    } else if (length == result.maximum_length) {
      result.maximizers.push_back(encode_word(word));
    }
  }
}

std::vector<int> normalize(std::vector<int> alphabet) {
  if (alphabet.empty()) throw std::invalid_argument("alphabet is empty");
  std::sort(alphabet.begin(), alphabet.end());
  if (std::adjacent_find(alphabet.begin(), alphabet.end()) != alphabet.end()) {
    throw std::invalid_argument("alphabet contains duplicates");
  }
  const int origin = alphabet.front();
  for (int& value : alphabet) value -= origin;
  int divisor = 0;
  for (const int value : alphabet) divisor = std::gcd(divisor, value);
  if (divisor == 0) divisor = 1;
  for (int& value : alphabet) value /= divisor;
  return alphabet;
}

void print_json(const std::vector<int>& alphabet, const Result& result,
                double seconds) {
  std::cout << "{\"alphabet\":[";
  for (std::size_t i = 0; i < alphabet.size(); ++i) {
    if (i != 0) std::cout << ',';
    std::cout << alphabet[i];
  }
  std::cout << "],\"complete\":" << (result.complete ? "true" : "false")
            << ",\"nodes\":" << result.nodes
            << ",\"leaves\":" << result.leaves
            << ",\"maximum_length\":" << result.maximum_length
            << ",\"maximizer_count\":" << result.maximizers.size()
            << ",\"maximizers\":[";
  for (std::size_t i = 0; i < result.maximizers.size(); ++i) {
    if (i != 0) std::cout << ',';
    std::cout << '\"' << result.maximizers[i] << '\"';
  }
  std::cout << "],\"depth_histogram\":[";
  for (std::size_t i = 0; i < result.depth_histogram.size(); ++i) {
    if (i != 0) std::cout << ',';
    std::cout << result.depth_histogram[i];
  }
  std::cout << "],\"runtime_seconds\":" << seconds << "}\n";
}

}  // namespace

int main(int argc, char** argv) {
  try {
    std::uint64_t node_limit = std::numeric_limits<std::uint64_t>::max();
    std::vector<int> alphabet;
    for (int i = 1; i < argc; ++i) {
      const std::string arg(argv[i]);
      if (arg == "--node-limit") {
        if (++i == argc) throw std::invalid_argument("missing node limit");
        node_limit = std::stoull(argv[i]);
      } else {
        alphabet.push_back(std::stoi(arg));
      }
    }
    alphabet = normalize(std::move(alphabet));
    Result result;
    result.node_limit = node_limit;
    std::vector<int> word;
    std::vector<std::int64_t> sums{0};
    const auto started = std::chrono::steady_clock::now();
    search(alphabet, word, sums, result);
    const double seconds = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - started).count();
    print_json(alphabet, result, seconds);
    return result.complete ? EXIT_SUCCESS : 2;
  } catch (const std::exception& error) {
    std::cerr << "error: " << error.what() << '\n';
    return EXIT_FAILURE;
  }
}
