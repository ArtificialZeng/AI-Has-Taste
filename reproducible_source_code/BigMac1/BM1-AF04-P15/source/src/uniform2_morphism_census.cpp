#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

using Morphism = std::array<std::array<int, 2>, 4>;

std::vector<int> fixed_prefix(const Morphism& morphism, std::size_t length) {
  std::vector<int> word{0};
  while (word.size() < length) {
    std::vector<int> next;
    next.reserve(word.size() * 2);
    for (const int letter : word) {
      next.push_back(morphism[letter][0]);
      next.push_back(morphism[letter][1]);
    }
    word.swap(next);
  }
  word.resize(length);
  return word;
}

struct Square {
  int start;
  int half_length;
  int end;
};

Square first_abelian_square(const std::vector<int>& word) {
  std::vector<std::array<int, 4>> counts(word.size() + 1);
  counts[0] = {0, 0, 0, 0};
  for (std::size_t i = 0; i < word.size(); ++i) {
    counts[i + 1] = counts[i];
    ++counts[i + 1][word[i]];
  }
  for (int end = 2; end <= static_cast<int>(word.size()); ++end) {
    for (int half = 1; 2 * half <= end; ++half) {
      const int start = end - 2 * half;
      bool equal = true;
      for (int letter = 0; letter < 4; ++letter) {
        const int left = counts[end - half][letter] - counts[start][letter];
        const int right = counts[end][letter] - counts[end - half][letter];
        equal = equal && (left == right);
      }
      if (equal) return {start, half, end};
    }
  }
  return {-1, -1, -1};
}

Morphism decode(std::uint32_t code) {
  Morphism morphism{};
  morphism[0][0] = 0;  // Prolongable on 0.
  morphism[0][1] = static_cast<int>(code % 4);
  code /= 4;
  for (int letter = 1; letter < 4; ++letter) {
    for (int position = 0; position < 2; ++position) {
      morphism[letter][position] = static_cast<int>(code % 4);
      code /= 4;
    }
  }
  return morphism;
}

std::string encode(const Morphism& morphism) {
  std::string text;
  for (int letter = 0; letter < 4; ++letter) {
    if (letter) text.push_back(';');
    text += std::to_string(morphism[letter][0]);
    text += std::to_string(morphism[letter][1]);
  }
  return text;
}

}  // namespace

int main(int argc, char** argv) {
  try {
    int prefix_length = 128;
    if (argc == 3 && std::string(argv[1]) == "--prefix") {
      prefix_length = std::stoi(argv[2]);
    } else if (argc != 1) {
      throw std::invalid_argument("usage: uniform2_morphism_census [--prefix N]");
    }
    if (prefix_length < 2) throw std::invalid_argument("prefix too short");

    constexpr std::uint32_t total = 4U * 16U * 16U * 16U;
    std::array<std::uint64_t, 129> endpoint_histogram{};
    int latest_endpoint = -1;
    std::uint64_t latest_count = 0;
    std::vector<std::string> latest_morphisms;
    Square latest_witness{-1, -1, -1};

    for (std::uint32_t code = 0; code < total; ++code) {
      const Morphism morphism = decode(code);
      const std::vector<int> word = fixed_prefix(morphism, prefix_length);
      const Square square = first_abelian_square(word);
      if (square.end < 0) {
        std::cerr << "unresolved_morphism=" << encode(morphism) << '\n';
        return 2;
      }
      if (square.end >= static_cast<int>(endpoint_histogram.size())) {
        throw std::runtime_error("histogram bound too small");
      }
      ++endpoint_histogram[square.end];
      if (square.end > latest_endpoint) {
        latest_endpoint = square.end;
        latest_count = 1;
        latest_morphisms.assign(1, encode(morphism));
        latest_witness = square;
      } else if (square.end == latest_endpoint) {
        ++latest_count;
        latest_morphisms.push_back(encode(morphism));
      }
    }

    std::sort(latest_morphisms.begin(), latest_morphisms.end());
    std::cout << "morphisms=" << total << '\n'
              << "prefix_length=" << prefix_length << '\n'
              << "all_contain_abelian_square=1\n"
              << "latest_first_endpoint=" << latest_endpoint << '\n'
              << "latest_first_count=" << latest_count << '\n'
              << "example_morphism=" << latest_morphisms.front() << '\n'
              << "example_start=" << latest_witness.start << '\n'
              << "example_half_length=" << latest_witness.half_length << '\n';
    std::cout << "endpoint_histogram=";
    bool first = true;
    for (std::size_t endpoint = 0; endpoint < endpoint_histogram.size(); ++endpoint) {
      if (endpoint_histogram[endpoint] == 0) continue;
      if (!first) std::cout << ',';
      first = false;
      std::cout << endpoint << ':' << endpoint_histogram[endpoint];
    }
    std::cout << '\n';
    return EXIT_SUCCESS;
  } catch (const std::exception& error) {
    std::cerr << "error: " << error.what() << '\n';
    return EXIT_FAILURE;
  }
}
