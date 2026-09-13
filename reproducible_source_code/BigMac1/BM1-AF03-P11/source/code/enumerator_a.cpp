#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

// Enumerator A
// - unique multiset permutations of a labelled-small/indistinguishable-large
//   skeleton via std::next_permutation;
// - large entries instantiated increasingly from left to right;
// - push legality evaluated by counting current stack entries larger than x;
// - minimality evaluated from the first half-decreasing iterate.

namespace {

using Perm = std::vector<int>;

Perm stack_map_count(const Perm &p) {
    Perm stack;
    Perm output;
    stack.reserve(p.size());
    output.reserve(p.size());
    for (int x : p) {
        while (true) {
            int larger = 0;
            for (int y : stack) {
                if (y > x && ++larger == 2) break;
            }
            if (larger < 2) break;
            output.push_back(stack.back());
            stack.pop_back();
        }
        stack.push_back(x);
    }
    while (!stack.empty()) {
        output.push_back(stack.back());
        stack.pop_back();
    }
    return output;
}

bool half_decreasing(const Perm &p) {
    const int n = static_cast<int>(p.size());
    int expected = 1;
    for (int index = n - 2; index >= 1; index -= 2) {
        if (p[index] != expected++) return false;
    }
    return true;
}

std::uint64_t factorial(int n) {
    std::uint64_t ans = 1;
    for (int i = 2; i <= n; ++i) ans *= static_cast<std::uint64_t>(i);
    return ans;
}

Perm increasing_lift(const Perm &skeleton, int small_count) {
    Perm p = skeleton;
    int next_large = small_count + 1;
    for (int &x : p) {
        if (x == 0) x = next_large++;
    }
    return p;
}

std::uint64_t fnv1a_update(std::uint64_t h, const Perm &skeleton) {
    constexpr std::uint64_t prime = 1099511628211ULL;
    for (int x : skeleton) {
        h ^= static_cast<unsigned char>(x);
        h *= prime;
    }
    h ^= static_cast<unsigned char>(0xff);
    h *= prime;
    return h;
}

struct Result {
    int n = 0;
    int small_count = 0;
    int large_count = 0;
    std::uint64_t skeletons = 0;
    std::uint64_t qualifying_skeletons = 0;
    std::uint64_t qualifying_terminal_large = 0;
    std::uint64_t permutation_count = 0;
    std::uint64_t fnv1a64 = 1469598103934665603ULL;
    double seconds = 0.0;
};

Result enumerate(int n) {
    Result result;
    result.n = n;
    result.small_count = (n - 1) / 2;
    result.large_count = n - result.small_count;

    Perm skeleton(n, 0);
    for (int i = 1; i <= result.small_count; ++i) {
        skeleton[result.large_count + i - 1] = i;
    }

    const int max_transient = 2 * result.small_count;
    const auto started = std::chrono::steady_clock::now();
    do {
        ++result.skeletons;
        Perm p = increasing_lift(skeleton, result.small_count);
        int transient = 0;
        while (!half_decreasing(p) && transient <= max_transient) {
            p = stack_map_count(p);
            ++transient;
        }
        if (transient == max_transient) {
            ++result.qualifying_skeletons;
            if (skeleton.back() == 0) ++result.qualifying_terminal_large;
            result.fnv1a64 = fnv1a_update(result.fnv1a64, skeleton);
        }
    } while (std::next_permutation(skeleton.begin(), skeleton.end()));

    result.permutation_count =
        result.qualifying_skeletons * factorial(result.large_count);
    result.seconds = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - started).count();
    return result;
}

void print_json(const Result &r) {
    std::cout << "{\n"
              << "  \"schema_version\": 1,\n"
              << "  \"enumerator\": \"A-next-permutation-count-legality\",\n"
              << "  \"length\": " << r.n << ",\n"
              << "  \"small_count\": " << r.small_count << ",\n"
              << "  \"large_count\": " << r.large_count << ",\n"
              << "  \"skeletons\": " << r.skeletons << ",\n"
              << "  \"qualifying_skeletons\": " << r.qualifying_skeletons << ",\n"
              << "  \"qualifying_terminal_large\": " << r.qualifying_terminal_large << ",\n"
              << "  \"permutation_count\": " << r.permutation_count << ",\n"
              << "  \"qualifying_skeleton_fnv1a64\": \"" << std::hex
              << r.fnv1a64 << std::dec << "\",\n"
              << "  \"elapsed_seconds_diagnostic\": " << r.seconds << "\n"
              << "}\n";
}

}  // namespace

int main(int argc, char **argv) {
    if (argc != 2) {
        std::cerr << "usage: enumerator_a LENGTH\n";
        return 64;
    }
    char *end = nullptr;
    const long parsed = std::strtol(argv[1], &end, 10);
    if (*argv[1] == '\0' || *end != '\0' || parsed < 1 || parsed > 20) {
        std::cerr << "LENGTH must be an integer in [1,20]\n";
        return 64;
    }
    print_json(enumerate(static_cast<int>(parsed)));
    return 0;
}
