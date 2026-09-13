#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

// Enumerator B
// - recursive skeleton generation (different order from Enumerator A);
// - large entries instantiated decreasingly from left to right;
// - push legality checked by searching pairs below the proposed new top;
// - transient length found by literal repeated-state/cycle detection, without
//   importing the half-decreasing characterization.

namespace {

using Perm = std::vector<int>;

bool legal_new_top_by_pairs(const Perm &stack, int x) {
    for (std::size_t i = 0; i < stack.size(); ++i) {
        if (stack[i] <= x) continue;
        for (std::size_t j = i + 1; j < stack.size(); ++j) {
            if (stack[j] > x) return false;
        }
    }
    return true;
}

Perm stack_map_pair_search(const Perm &p) {
    Perm stack;
    Perm output;
    stack.reserve(p.size());
    output.reserve(p.size());
    for (int x : p) {
        while (!legal_new_top_by_pairs(stack, x)) {
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

int literal_preperiod(Perm p, int fail_limit) {
    std::vector<Perm> seen;
    seen.reserve(static_cast<std::size_t>(fail_limit + 3));
    for (int step = 0; step <= fail_limit + 1; ++step) {
        const auto it = std::find(seen.begin(), seen.end(), p);
        if (it != seen.end()) {
            return static_cast<int>(it - seen.begin());
        }
        seen.push_back(p);
        p = stack_map_pair_search(p);
    }
    return -1;
}

std::uint64_t factorial(int n) {
    std::uint64_t ans = 1;
    for (int i = 2; i <= n; ++i) ans *= static_cast<std::uint64_t>(i);
    return ans;
}

Perm decreasing_lift(const Perm &skeleton, int n) {
    Perm p = skeleton;
    int next_large = n;
    for (int &x : p) {
        if (x == 0) x = next_large--;
    }
    return p;
}

struct Result {
    int n = 0;
    int small_count = 0;
    int large_count = 0;
    std::uint64_t skeletons = 0;
    std::uint64_t qualifying_skeletons = 0;
    std::uint64_t qualifying_terminal_large = 0;
    std::uint64_t permutation_count = 0;
    std::uint64_t cycle_detection_failures = 0;
    double seconds = 0.0;
};

class RecursiveEnumerator {
  public:
    explicit RecursiveEnumerator(int n) : n_(n), m_((n - 1) / 2),
        large_count_(n - m_), skeleton_(n, -1), used_(m_ + 1, false) {
        result_.n = n_;
        result_.small_count = m_;
        result_.large_count = large_count_;
    }

    Result run() {
        const auto started = std::chrono::steady_clock::now();
        visit(0, large_count_);
        result_.permutation_count =
            result_.qualifying_skeletons * factorial(large_count_);
        result_.seconds = std::chrono::duration<double>(
            std::chrono::steady_clock::now() - started).count();
        return result_;
    }

  private:
    void visit(int position, int large_left) {
        if (position == n_) {
            ++result_.skeletons;
            const Perm p = decreasing_lift(skeleton_, n_);
            // The horizon is deliberately longer than the claimed maximal
            // transient: a periodic orbit need not be a fixed point (already
            // S_2 has a 2-cycle).  A missing repeat is a closed failure.
            const int mu = literal_preperiod(p, 4 * n_ + 4);
            if (mu < 0) {
                ++result_.cycle_detection_failures;
            } else if (mu == 2 * m_) {
                ++result_.qualifying_skeletons;
                if (skeleton_.back() == 0) ++result_.qualifying_terminal_large;
            }
            return;
        }

        // Deliberately visit labelled small tokens before the large token;
        // this is not the lexicographic multiset order used by Enumerator A.
        for (int x = m_; x >= 1; --x) {
            if (!used_[x]) {
                used_[x] = true;
                skeleton_[position] = x;
                visit(position + 1, large_left);
                used_[x] = false;
            }
        }
        if (large_left > 0) {
            skeleton_[position] = 0;
            visit(position + 1, large_left - 1);
        }
    }

    int n_;
    int m_;
    int large_count_;
    Perm skeleton_;
    std::vector<bool> used_;
    Result result_;
};

void print_json(const Result &r) {
    std::cout << "{\n"
              << "  \"schema_version\": 1,\n"
              << "  \"enumerator\": \"B-recursive-pair-search-cycle-detection\",\n"
              << "  \"length\": " << r.n << ",\n"
              << "  \"small_count\": " << r.small_count << ",\n"
              << "  \"large_count\": " << r.large_count << ",\n"
              << "  \"skeletons\": " << r.skeletons << ",\n"
              << "  \"qualifying_skeletons\": " << r.qualifying_skeletons << ",\n"
              << "  \"qualifying_terminal_large\": " << r.qualifying_terminal_large << ",\n"
              << "  \"permutation_count\": " << r.permutation_count << ",\n"
              << "  \"cycle_detection_failures\": " << r.cycle_detection_failures << ",\n"
              << "  \"elapsed_seconds_diagnostic\": " << r.seconds << "\n"
              << "}\n";
}

}  // namespace

int main(int argc, char **argv) {
    if (argc != 2) {
        std::cerr << "usage: enumerator_b LENGTH\n";
        return 64;
    }
    char *end = nullptr;
    const long parsed = std::strtol(argv[1], &end, 10);
    if (*argv[1] == '\0' || *end != '\0' || parsed < 1 || parsed > 20) {
        std::cerr << "LENGTH must be an integer in [1,20]\n";
        return 64;
    }
    print_json(RecursiveEnumerator(static_cast<int>(parsed)).run());
    return 0;
}
