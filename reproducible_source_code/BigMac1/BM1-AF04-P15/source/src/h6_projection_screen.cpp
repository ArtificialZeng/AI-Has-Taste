#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <stdexcept>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

namespace {

struct Witness {
  int start;
  int half;
  int end;
  std::int64_t left_sum;
};

std::vector<int> h6_prefix(int length) {
  const std::array<std::array<int, 3>, 6> images{{
      {{0, 2, 4}}, {{0, 3, 5}}, {{1, 3, 5}},
      {{1, 3, 2}}, {{0, 5, 4}}, {{1, 2, 4}},
  }};
  std::vector<int> word{0};
  while (static_cast<int>(word.size()) < length) {
    std::vector<int> next;
    next.reserve(word.size() * 3);
    for (const int letter : word) {
      next.insert(next.end(), images[letter].begin(), images[letter].end());
    }
    word.swap(next);
  }
  word.resize(length);
  return word;
}

std::pair<int, int> normalize_perpendicular(std::int64_t dx, std::int64_t dy) {
  const std::int64_t divisor = std::gcd(std::llabs(dx), std::llabs(dy));
  std::int64_t p = dy / divisor;
  std::int64_t q = -dx / divisor;
  if (p < 0 || (p == 0 && q < 0)) {
    p = -p;
    q = -q;
  }
  return {static_cast<int>(p), static_cast<int>(q)};
}

int height(const std::pair<int, int>& direction) {
  return std::max(std::abs(direction.first), std::abs(direction.second));
}

}  // namespace

int main(int argc, char** argv) {
  try {
    int prefix_length = 10000;
    int max_height = 100;
    for (int i = 1; i < argc; ++i) {
      const std::string arg(argv[i]);
      if (arg == "--prefix" && i + 1 < argc) prefix_length = std::stoi(argv[++i]);
      else if (arg == "--height" && i + 1 < argc) max_height = std::stoi(argv[++i]);
      else throw std::invalid_argument("usage: h6_projection_screen [--prefix N] [--height H]");
    }
    if (prefix_length < 2 || max_height < 1) throw std::invalid_argument("invalid bound");

    const std::array<std::pair<int, int>, 6> weights{{
        {0, 0}, {1, 1}, {2, 1}, {0, 1}, {2, 0}, {1, 0},
    }};
    const std::vector<int> word = h6_prefix(prefix_length);
    std::vector<std::int64_t> sx(prefix_length + 1, 0), sy(prefix_length + 1, 0);
    for (int i = 0; i < prefix_length; ++i) {
      sx[i + 1] = sx[i] + weights[word[i]].first;
      sy[i + 1] = sy[i] + weights[word[i]].second;
    }

    std::map<std::pair<int, int>, Witness> killed;
    std::uint64_t pairs = 0;
    for (int end = 2; end <= prefix_length; ++end) {
      for (int half = 1; 2 * half <= end; ++half) {
        ++pairs;
        const int start = end - 2 * half;
        const std::int64_t lx = sx[end - half] - sx[start];
        const std::int64_t ly = sy[end - half] - sy[start];
        const std::int64_t rx = sx[end] - sx[end - half];
        const std::int64_t ry = sy[end] - sy[end - half];
        const std::int64_t dx = lx - rx;
        const std::int64_t dy = ly - ry;
        if (dx == 0 && dy == 0) {
          throw std::runtime_error("vector additive square found in certified h6 prefix");
        }
        const auto direction = normalize_perpendicular(dx, dy);
        if (height(direction) <= max_height && !killed.contains(direction)) {
          const std::int64_t projected = direction.first * lx + direction.second * ly;
          killed.emplace(direction, Witness{start, half, end, projected});
        }
      }
    }

    std::vector<std::pair<int, int>> universe;
    std::vector<std::pair<int, int>> survivors;
    for (int p = 0; p <= max_height; ++p) {
      for (int q = -max_height; q <= max_height; ++q) {
        if (p == 0 && q <= 0) continue;
        if (std::gcd(p, std::abs(q)) != 1) continue;
        const std::pair<int, int> direction{p, q};
        universe.push_back(direction);
        if (!killed.contains(direction)) survivors.push_back(direction);
      }
    }
    auto order = [](const auto& left, const auto& right) {
      return std::tuple(height(left), left.first, left.second) <
             std::tuple(height(right), right.first, right.second);
    };
    std::sort(survivors.begin(), survivors.end(), order);

    std::cout << "prefix_length=" << prefix_length << '\n'
              << "height_bound=" << max_height << '\n'
              << "block_pairs=" << pairs << '\n'
              << "primitive_directions=" << universe.size() << '\n'
              << "killed_directions=" << universe.size() - survivors.size() << '\n'
              << "surviving_directions=" << survivors.size() << '\n';
    if (!survivors.empty()) {
      std::cout << "smallest_survivor=" << survivors.front().first << ','
                << survivors.front().second << '\n';
    }
    std::cout << "first_survivors=";
    for (std::size_t i = 0; i < std::min<std::size_t>(10, survivors.size()); ++i) {
      if (i) std::cout << ';';
      std::cout << survivors[i].first << ',' << survivors[i].second;
    }
    std::cout << '\n';

    const std::pair<int, int> example{1, 0};
    if (const auto iterator = killed.find(example); iterator != killed.end()) {
      const Witness& witness = iterator->second;
      std::cout << "example_killed_direction=1,0\n"
                << "example_interval=" << witness.start << ',' << witness.end << '\n'
                << "example_half_length=" << witness.half << '\n'
                << "example_equal_sum=" << witness.left_sum << '\n';
    }
    return EXIT_SUCCESS;
  } catch (const std::exception& error) {
    std::cerr << "error: " << error.what() << '\n';
    return EXIT_FAILURE;
  }
}
