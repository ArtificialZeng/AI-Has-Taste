#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <tuple>
#include <vector>

using Order = std::array<uint8_t, 3>;
using Profile = std::array<uint8_t, 6>;
using Matching = std::array<uint8_t, 6>;

struct Action {
    std::array<uint8_t, 6> input_agent{};
    std::array<std::array<uint8_t, 13>, 6> order_map{};
    std::string label;
};

static std::vector<std::array<uint8_t, 3>> permutations3() {
    std::vector<std::array<uint8_t, 3>> result;
    std::array<uint8_t, 3> p{0, 1, 2};
    do result.push_back(p); while (std::next_permutation(p.begin(), p.end()));
    return result;
}

static std::array<uint8_t, 3> inverse3(const std::array<uint8_t, 3>& p) {
    std::array<uint8_t, 3> result{};
    for (uint8_t i = 0; i < 3; ++i) result[p[i]] = i;
    return result;
}

static std::vector<Order> weak_orders() {
    std::vector<Order> result;
    for (uint8_t a = 0; a < 3; ++a)
        for (uint8_t b = 0; b < 3; ++b)
            for (uint8_t c = 0; c < 3; ++c) {
                Order r{a, b, c};
                uint8_t hi = std::max({a, b, c});
                bool used[3] = {false, false, false};
                used[a] = used[b] = used[c] = true;
                bool normalized = true;
                for (uint8_t x = 0; x <= hi; ++x) normalized &= used[x];
                if (normalized) result.push_back(r);
            }
    return result;
}

static uint8_t order_index(const std::vector<Order>& orders, const Order& target) {
    auto it = std::find(orders.begin(), orders.end(), target);
    assert(it != orders.end());
    return static_cast<uint8_t>(it - orders.begin());
}

static std::vector<Action> actions(const std::vector<Order>& orders) {
    std::vector<Action> result;
    const auto perms = permutations3();
    for (uint8_t swapped = 0; swapped < 2; ++swapped) {
        for (uint8_t pi = 0; pi < perms.size(); ++pi) {
            for (uint8_t qi = 0; qi < perms.size(); ++qi) {
                const auto ip = inverse3(perms[pi]);
                const auto iq = inverse3(perms[qi]);
                Action g;
                g.label = std::string(swapped ? "swap:" : "preserve:")
                    + std::to_string(pi) + "," + std::to_string(qi);
                std::array<std::array<uint8_t, 3>, 6> coordinate_map{};
                if (!swapped) {
                    // Old m_i -> new m_{p(i)}; old w_j -> new w_{q(j)}.
                    for (uint8_t k = 0; k < 3; ++k) {
                        g.input_agent[k] = ip[k];
                        coordinate_map[k] = iq;
                    }
                    for (uint8_t l = 0; l < 3; ++l) {
                        g.input_agent[3 + l] = 3 + iq[l];
                        coordinate_map[3 + l] = ip;
                    }
                } else {
                    // Old m_i -> new w_{p(i)}; old w_j -> new m_{q(j)}.
                    for (uint8_t k = 0; k < 3; ++k) {
                        g.input_agent[k] = 3 + iq[k];
                        coordinate_map[k] = ip;
                    }
                    for (uint8_t l = 0; l < 3; ++l) {
                        g.input_agent[3 + l] = ip[l];
                        coordinate_map[3 + l] = iq;
                    }
                }
                for (uint8_t a = 0; a < 6; ++a) {
                    for (uint8_t o = 0; o < 13; ++o) {
                        Order image{};
                        for (uint8_t x = 0; x < 3; ++x)
                            image[x] = orders[o][coordinate_map[a][x]];
                        g.order_map[a][o] = order_index(orders, image);
                    }
                }
                result.push_back(g);
            }
        }
    }
    return result;
}

static uint32_t encode_profile(const Profile& p) {
    uint32_t code = 0;
    for (uint8_t x : p) code = 13 * code + x;
    return code;
}

static Profile decode_profile(uint32_t code) {
    Profile p{};
    for (int i = 5; i >= 0; --i) {
        p[i] = code % 13;
        code /= 13;
    }
    return p;
}

static uint32_t transform_code(const Profile& p, const Action& g) {
    uint32_t code = 0;
    for (uint8_t a = 0; a < 6; ++a)
        code = 13 * code + g.order_map[a][p[g.input_agent[a]]];
    return code;
}

static uint64_t fixed_profiles(const Action& g) {
    // Fixed equations are p[a] = order_map[a][p[input_agent[a]]].
    std::array<std::array<uint8_t, 13>, 6> inverse_map{};
    for (uint8_t a = 0; a < 6; ++a)
        for (uint8_t o = 0; o < 13; ++o)
            inverse_map[a][g.order_map[a][o]] = o;
    bool visited[6] = {false, false, false, false, false, false};
    uint64_t count = 1;
    for (uint8_t start = 0; start < 6; ++start) {
        if (visited[start]) continue;
        uint8_t cycle_choices = 0;
        for (uint8_t initial = 0; initial < 13; ++initial) {
            uint8_t a = start;
            uint8_t value = initial;
            do {
                visited[a] = true;
                value = inverse_map[a][value];
                a = g.input_agent[a];
            } while (a != start);
            cycle_choices += (value == initial);
        }
        // Reset cycle visit marking is unnecessary; choices use only its maps.
        count *= cycle_choices;
    }
    return count;
}

static std::vector<Matching> all_matchings() {
    std::vector<Matching> result;
    for (uint8_t mask_m = 0; mask_m < 8; ++mask_m) {
        uint8_t size = __builtin_popcount(mask_m);
        for (uint8_t mask_w = 0; mask_w < 8; ++mask_w) {
            if (__builtin_popcount(mask_w) != size) continue;
            std::vector<uint8_t> men, women;
            for (uint8_t i = 0; i < 3; ++i) if (mask_m & (1 << i)) men.push_back(i);
            for (uint8_t j = 0; j < 3; ++j) if (mask_w & (1 << j)) women.push_back(j);
            do {
                Matching m{3, 3, 3, 3, 3, 3};
                for (uint8_t i = 0; i < size; ++i) {
                    m[men[i]] = women[i];
                    m[3 + women[i]] = men[i];
                }
                result.push_back(m);
            } while (std::next_permutation(women.begin(), women.end()));
        }
    }
    // Match the deterministic order in triage_singleton_check.py: by size,
    // then lexicographic subsets and images.
    std::stable_sort(result.begin(), result.end(), [](const Matching& x, const Matching& y) {
        int sx = 0, sy = 0;
        for (int i = 0; i < 3; ++i) { sx += x[i] != 3; sy += y[i] != 3; }
        if (sx != sy) return sx < sy;
        std::array<int, 3> xm{}, ym{};
        for (int i = 0; i < 3; ++i) { xm[i] = x[i]; ym[i] = y[i]; }
        return xm < ym;
    });
    return result;
}

static std::string matching_string(const Matching& m) {
    std::string s = "{";
    bool first = true;
    for (uint8_t i = 0; i < 3; ++i) if (m[i] != 3) {
        if (!first) s += ",";
        first = false;
        s += "m" + std::to_string(i) + "-w" + std::to_string(m[i]);
    }
    return s + "}";
}

struct PopularityCache {
    std::array<int8_t, 4096> result{}; // -1 unknown, 0 losing, 1 winning
    std::array<int8_t, 4096> witness{};
    PopularityCache() { result.fill(-1); witness.fill(-1); }
};

static uint16_t rank_code(const std::array<uint8_t, 6>& q) {
    uint16_t code = 0;
    for (uint8_t x : q) code = 4 * code + x;
    return code;
}

static std::array<uint8_t, 6> decode_rank_code(uint16_t code) {
    std::array<uint8_t, 6> q{};
    for (int a = 5; a >= 0; --a) { q[a] = code % 4; code /= 4; }
    return q;
}

static bool popular(uint16_t qcode,
                    const std::array<std::array<uint8_t, 6>, 34>& matching_ranks,
                    PopularityCache& cache) {
    if (cache.result[qcode] != -1) return cache.result[qcode];
    const auto q = decode_rank_code(qcode);
    for (uint8_t y = 0; y < 34; ++y) {
        int margin = 0;
        for (uint8_t a = 0; a < 6; ++a)
            margin += (q[a] < matching_ranks[y][a]) - (q[a] > matching_ranks[y][a]);
        if (margin < 0) {
            cache.result[qcode] = 0;
            cache.witness[qcode] = y;
            return false;
        }
    }
    cache.result[qcode] = 1;
    return true;
}

struct ProfileResult {
    uint8_t dimension = 3;
    std::array<int8_t, 2> winning_pair{-1, -1};
};

static ProfileResult dimension_at_most_two(
        const Profile& profile, const std::vector<Order>& orders,
        const std::vector<Matching>& matchings) {
    std::array<std::array<uint8_t, 6>, 34> ranks{};
    std::array<uint16_t, 34> codes{};
    for (uint8_t mi = 0; mi < 34; ++mi) {
        for (uint8_t a = 0; a < 6; ++a) {
            uint8_t partner = matchings[mi][a];
            ranks[mi][a] = partner == 3 ? 3 : orders[profile[a]][partner];
        }
        codes[mi] = rank_code(ranks[mi]);
    }
    PopularityCache cache;
    for (uint8_t i = 0; i < 34; ++i) if (popular(codes[i], ranks, cache))
        return ProfileResult{1, {static_cast<int8_t>(i), -1}};
    for (uint8_t i = 0; i < 34; ++i)
        for (uint8_t j = i + 1; j < 34; ++j) {
            std::array<uint8_t, 6> best{};
            for (uint8_t a = 0; a < 6; ++a)
                best[a] = std::min(ranks[i][a], ranks[j][a]);
            if (popular(rank_code(best), ranks, cache))
                return ProfileResult{2, {static_cast<int8_t>(i), static_cast<int8_t>(j)}};
        }
    return ProfileResult{};
}

static void print_extremal_certificate(
        const Profile& profile, const std::vector<Order>& orders,
        const std::vector<Matching>& matchings) {
    std::array<std::array<uint8_t, 6>, 34> ranks{};
    std::array<uint16_t, 34> codes{};
    for (uint8_t mi = 0; mi < 34; ++mi) {
        for (uint8_t a = 0; a < 6; ++a) {
            uint8_t partner = matchings[mi][a];
            ranks[mi][a] = partner == 3 ? 3 : orders[profile[a]][partner];
        }
        codes[mi] = rank_code(ranks[mi]);
    }
    PopularityCache cache;
    std::cout << "EXTREMAL_PROFILE_IDS=";
    for (uint8_t a = 0; a < 6; ++a) std::cout << (a ? "," : "") << int(profile[a]);
    std::cout << "\nEXTREMAL_PROFILE_RANKS=";
    for (uint8_t a = 0; a < 6; ++a) {
        if (a) std::cout << ";";
        std::cout << int(orders[profile[a]][0]) << int(orders[profile[a]][1])
                  << int(orders[profile[a]][2]);
    }
    std::cout << "\nPAIR_FAILURE_WITNESSES_BEGIN\n";
    for (uint8_t i = 0; i < 34; ++i) {
        popular(codes[i], ranks, cache);
        std::cout << "C=" << int(i) << " W=" << int(cache.witness[codes[i]]) << "\n";
    }
    for (uint8_t i = 0; i < 34; ++i)
        for (uint8_t j = i + 1; j < 34; ++j) {
            std::array<uint8_t, 6> best{};
            for (uint8_t a = 0; a < 6; ++a)
                best[a] = std::min(ranks[i][a], ranks[j][a]);
            uint16_t code = rank_code(best);
            popular(code, ranks, cache);
            std::cout << "C=" << int(i) << "," << int(j)
                      << " W=" << int(cache.witness[code]) << "\n";
        }
    std::cout << "PAIR_FAILURE_WITNESSES_END\n";
    for (uint8_t i = 0; i < 34; ++i)
        for (uint8_t j = i + 1; j < 34; ++j)
            for (uint8_t k = j + 1; k < 34; ++k) {
                std::array<uint8_t, 6> best{};
                for (uint8_t a = 0; a < 6; ++a)
                    best[a] = std::min({ranks[i][a], ranks[j][a], ranks[k][a]});
                if (popular(rank_code(best), ranks, cache)) {
                    std::cout << "WINNING_TRIPLE=" << int(i) << "," << int(j)
                              << "," << int(k) << "\n";
                    std::cout << "WINNING_TRIPLE_MATCHINGS="
                              << matching_string(matchings[i]) << ";"
                              << matching_string(matchings[j]) << ";"
                              << matching_string(matchings[k]) << "\n";
                    for (uint8_t y = 0; y < 34; ++y) {
                        int margin = 0;
                        for (uint8_t a = 0; a < 6; ++a)
                            margin += (best[a] < ranks[y][a]) - (best[a] > ranks[y][a]);
                        std::cout << "TRIPLE_MARGIN Y=" << int(y) << " M=" << margin << "\n";
                    }
                    return;
                }
            }
    assert(false && "Theorem 3.3 predicts a winning triple");
}

int main() {
    const auto orders = weak_orders();
    const auto group = actions(orders);
    const auto matchings = all_matchings();
    constexpr uint32_t PROFILE_COUNT = 4826809; // 13^6
    assert(orders.size() == 13 && group.size() == 72 && matchings.size() == 34);
    assert(encode_profile(decode_profile(PROFILE_COUNT - 1)) == PROFILE_COUNT - 1);

    uint64_t burnside_sum = 0;
    std::cout << "CXX_COMPILER=" << __VERSION__ << "\n";
    std::cout << "WEAK_ORDERS=" << orders.size() << " MATCHINGS=" << matchings.size()
              << " LABELLED_PROFILES=" << PROFILE_COUNT << " GROUP_ORDER=" << group.size() << "\n";
    for (uint8_t gi = 0; gi < group.size(); ++gi) {
        uint64_t fixed = fixed_profiles(group[gi]);
        burnside_sum += fixed;
        std::cout << "BURNSIDE g=" << int(gi) << " label=" << group[gi].label
                  << " fixed=" << fixed << "\n";
    }
    assert(burnside_sum % group.size() == 0);
    const uint64_t burnside_orbits = burnside_sum / group.size();
    std::cout << "BURNSIDE_SUM=" << burnside_sum
              << " BURNSIDE_ORBITS=" << burnside_orbits << "\n";

    std::vector<uint8_t> visited((PROFILE_COUNT + 7) / 8, 0);
    auto is_visited = [&](uint32_t x) { return visited[x >> 3] & (1u << (x & 7)); };
    auto mark = [&](uint32_t x) { visited[x >> 3] |= (1u << (x & 7)); };

    uint64_t orbit_count = 0, covered = 0;
    std::array<uint64_t, 4> orbit_dimensions{0, 0, 0, 0};
    std::array<uint64_t, 4> labelled_dimensions{0, 0, 0, 0};
    bool have_extremal = false;
    Profile first_extremal{};
    for (uint32_t code = 0; code < PROFILE_COUNT; ++code) {
        if (is_visited(code)) continue;
        const Profile p = decode_profile(code);
        std::array<uint32_t, 72> images{};
        for (uint8_t gi = 0; gi < group.size(); ++gi) images[gi] = transform_code(p, group[gi]);
        std::sort(images.begin(), images.end());
        auto last = std::unique(images.begin(), images.end());
        assert(images[0] == code); // Ascending unvisited scan produces the canonical member.
        uint32_t orbit_size = last - images.begin();
        for (auto it = images.begin(); it != last; ++it) mark(*it);
        covered += orbit_size;
        ++orbit_count;

        ProfileResult r = dimension_at_most_two(p, orders, matchings);
        ++orbit_dimensions[r.dimension];
        labelled_dimensions[r.dimension] += orbit_size;
        if (r.dimension == 3 && !have_extremal) {
            have_extremal = true;
            first_extremal = p;
            std::cout << "FIRST_DIMENSION_3_CODE=" << code << " ORBIT_INDEX=" << orbit_count << "\n";
        }
        if (orbit_count % 10000 == 0)
            std::cout << "PROGRESS_ORBITS=" << orbit_count << " COVERED=" << covered << "\n";
    }
    assert(covered == PROFILE_COUNT);
    assert(orbit_count == burnside_orbits);
    uint64_t labelled_total = labelled_dimensions[1] + labelled_dimensions[2] + labelled_dimensions[3];
    assert(labelled_total == PROFILE_COUNT);
    std::cout << "ORBIT_ENUMERATION_ORBITS=" << orbit_count << " COVERED=" << covered << "\n";
    std::cout << "ORBIT_DIMENSIONS d1=" << orbit_dimensions[1] << " d2=" << orbit_dimensions[2]
              << " d3=" << orbit_dimensions[3] << "\n";
    std::cout << "LABELLED_DIMENSIONS d1=" << labelled_dimensions[1] << " d2="
              << labelled_dimensions[2] << " d3=" << labelled_dimensions[3] << "\n";
    if (have_extremal) print_extremal_certificate(first_extremal, orders, matchings);
    else std::cout << "NO_DIMENSION_3_PROFILE\n";
    std::cout << "VERIFIED_COMPLETE_CENSUS\n";
}
