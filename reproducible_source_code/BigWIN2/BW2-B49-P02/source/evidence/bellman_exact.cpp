#include <algorithm>
#include <array>
#include <bit>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

// Exhaustive Bellman solver for the frozen (n,s)=(3,2) game in source.md.
// There are deliberately no symmetry reductions, dominance rules, branch-and-
// bound cutoffs, or restrictions on guesses.  Every one of the 48 legal guesses
// is scored at every nonempty state reached by the recurrence.

using Mask = std::uint64_t;

struct Item {
    std::array<int, 3> p{}; // value at each position, zero based
    int colors = 0;         // bit j is the color attached to value j
    std::string code;
};

struct Entry {
    std::uint8_t value = 0;
    std::uint8_t action = 255;
};

static std::vector<Item> items;
static std::array<std::array<Mask, 8>, 48> feedback_masks{};
static std::array<std::unordered_map<Mask, Entry>, 7> memo;
static std::array<std::uint64_t, 7> action_evaluations{};

static int feedback(const Item &g, const Item &x) {
    int u = 0;
    for (int i = 0; i < 3; ++i) {
        const int value = g.p[i];
        const bool rank_ok = (value == x.p[i]);
        const bool color_ok = (((g.colors >> value) & 1) ==
                               ((x.colors >> value) & 1));
        if (rank_ok && color_ok) u |= 1 << i;
    }
    return u;
}

static int solve(Mask a, int r) {
    if (a == 0 || r == 0) return 0;
    auto &table = memo[r];
    if (auto it = table.find(a); it != table.end()) return it->second.value;

    int best = -1;
    int best_g = -1;
    for (int g = 0; g < 48; ++g) {
        ++action_evaluations[r];
        int score = ((a >> g) & Mask{1}) ? 1 : 0; // feedback [3]
        for (int u = 0; u < 7; ++u) {
            score += solve(a & feedback_masks[g][u], r - 1);
        }
        if (score > best) {
            best = score;
            best_g = g;
        }
    }
    table.emplace(a, Entry{static_cast<std::uint8_t>(best),
                           static_cast<std::uint8_t>(best_g)});
    return best;
}

static std::string hex_mask(Mask m) {
    std::ostringstream out;
    out << std::hex << std::setfill('0') << std::setw(12) << m;
    return out.str();
}

static void write_feedback_table(const std::string &path) {
    std::ofstream out(path);
    out << "guess_index,guess_code,secret_index,secret_code,feedback_mask,feedback_set\n";
    for (int g = 0; g < 48; ++g) {
        for (int x = 0; x < 48; ++x) {
            int u = feedback(items[g], items[x]);
            out << g << ',' << items[g].code << ',' << x << ',' << items[x].code
                << ',' << u << ",\"{";
            bool first = true;
            for (int i = 0; i < 3; ++i) if ((u >> i) & 1) {
                if (!first) out << ' ';
                out << (i + 1);
                first = false;
            }
            out << "}\"\n";
        }
    }
}

static void write_items(const std::string &path) {
    std::ofstream out(path);
    out << "index,code,permutation,colors_by_value\n";
    for (int i = 0; i < 48; ++i) {
        out << i << ',' << items[i].code << ','
            << (items[i].p[0] + 1) << (items[i].p[1] + 1)
            << (items[i].p[2] + 1) << ',';
        for (int j = 0; j < 3; ++j) out << ((items[i].colors >> j) & 1);
        out << '\n';
    }
}

static void write_root_decompositions(const std::string &path, Mask full) {
    std::ofstream out(path);
    out << "horizon,value,action_index,action_code,feedback_mask,cell_mask,cell_size,child_value\n";
    for (int r = 1; r <= 6; ++r) {
        const auto entry = memo[r].at(full);
        int g = entry.action;
        // Include the terminal cell explicitly; it contributes immediately.
        for (int u = 0; u < 8; ++u) {
            Mask child = full & feedback_masks[g][u];
            int child_value = (u == 7) ? std::popcount(child) : solve(child, r - 1);
            out << r << ',' << int(entry.value) << ',' << g << ',' << items[g].code
                << ',' << u << ',' << hex_mask(child) << ',' << std::popcount(child)
                << ',' << child_value << '\n';
        }
    }
}

static void write_all_states(const std::string &path) {
    std::ofstream out(path);
    out << "horizon,state_mask,state_size,value,action_index,action_code";
    for (int u = 0; u < 8; ++u) out << ",cell" << u << "_mask,cell" << u << "_size";
    out << '\n';
    for (int r = 1; r <= 6; ++r) {
        std::vector<std::pair<Mask, Entry>> rows(memo[r].begin(), memo[r].end());
        std::sort(rows.begin(), rows.end(), [](const auto &a, const auto &b) {
            return a.first < b.first;
        });
        for (const auto &[a, entry] : rows) {
            const int g = entry.action;
            out << r << ',' << hex_mask(a) << ',' << std::popcount(a) << ','
                << int(entry.value) << ',' << g << ',' << items[g].code;
            for (int u = 0; u < 8; ++u) {
                Mask child = a & feedback_masks[g][u];
                out << ',' << hex_mask(child) << ',' << std::popcount(child);
            }
            out << '\n';
        }
    }
}

int main(int argc, char **argv) {
    const std::string out_dir = (argc >= 2) ? argv[1] : "evidence/bellman-output";

    std::array<int, 3> p{0, 1, 2};
    do {
        for (int c = 0; c < 8; ++c) {
            std::string code;
            for (int i = 0; i < 3; ++i) code.push_back(char('1' + p[i]));
            code.push_back('-');
            for (int j = 0; j < 3; ++j) code.push_back(char('0' + ((c >> j) & 1)));
            items.push_back(Item{p, c, code});
        }
    } while (std::next_permutation(p.begin(), p.end()));
    if (items.size() != 48) return 2;

    for (int g = 0; g < 48; ++g) {
        for (int x = 0; x < 48; ++x) {
            feedback_masks[g][feedback(items[g], items[x])] |= Mask{1} << x;
        }
        Mask cover = 0;
        for (int u = 0; u < 8; ++u) {
            if (cover & feedback_masks[g][u]) return 3;
            cover |= feedback_masks[g][u];
        }
        if (cover != ((Mask{1} << 48) - 1)) return 4;
        if (feedback_masks[g][7] != (Mask{1} << g)) return 5;
    }

    for (int r = 1; r <= 6; ++r) memo[r].reserve(100000);
    const Mask full = (Mask{1} << 48) - 1;
    std::array<int, 7> values{};
    const auto start = std::chrono::steady_clock::now();
    for (int r = 1; r <= 6; ++r) {
        values[r] = solve(full, r);
        const double sec = std::chrono::duration<double>(
            std::chrono::steady_clock::now() - start).count();
        const Entry root = memo[r].at(full);
        std::cerr << "r=" << r << " value=" << values[r]
                  << " action=" << int(root.action) << ':' << items[root.action].code
                  << " seconds=" << sec << '\n';
    }

    write_items(out_dir + "/items.csv");
    write_feedback_table(out_dir + "/feedback.csv");
    write_root_decompositions(out_dir + "/root-decompositions.csv", full);
    write_all_states(out_dir + "/states.csv");

    std::ofstream summary(out_dir + "/summary.txt");
    summary << "Bellman values:";
    for (int r = 1; r <= 6; ++r) summary << ' ' << values[r];
    summary << "\nCircularShift benchmark: 1 8 24 40 47 48\n";
    for (int r = 1; r <= 6; ++r) {
        const Entry root = memo[r].at(full);
        summary << "r=" << r << " states=" << memo[r].size()
                << " actions_evaluated=" << action_evaluations[r]
                << " root_action=" << int(root.action) << ':' << items[root.action].code
                << " value=" << int(root.value) << '\n';
    }
    const double sec = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - start).count();
    summary << "elapsed_seconds=" << std::setprecision(12) << sec << '\n';
    summary.close();

    std::cout << "Bellman values:";
    for (int r = 1; r <= 6; ++r) std::cout << ' ' << values[r];
    std::cout << '\n';
    for (int r = 1; r <= 6; ++r) {
        std::cout << "r=" << r << " states=" << memo[r].size()
                  << " actions=" << action_evaluations[r] << '\n';
    }
    std::cout << "elapsed_seconds=" << std::setprecision(12) << sec << '\n';
}
