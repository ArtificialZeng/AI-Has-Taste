#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <string>
#include <vector>

using Matrix = std::uint16_t;

static std::array<unsigned char, 65536> popcount16{};

static std::array<unsigned char, 4> rows(Matrix a) {
    return {static_cast<unsigned char>(a & 15u),
            static_cast<unsigned char>((a >> 4) & 15u),
            static_cast<unsigned char>((a >> 8) & 15u),
            static_cast<unsigned char>((a >> 12) & 15u)};
}

// Tests GE (strict=false) or GR (strict=true) on the leading s-by-s block.
// Row-allowability of that block is checked explicitly.
static bool expansion_property(const std::array<unsigned char, 4>& r,
                               int s, bool strict) {
    const unsigned char columns = static_cast<unsigned char>((1u << s) - 1u);
    const int limit = 1 << s;
    std::array<unsigned char, 16> image{};
    for (int i = 0; i < s; ++i) {
        if ((r[i] & columns) == 0) return false;
    }
    for (int subset = 1; subset < limit; ++subset) {
        unsigned char value = 0;
        for (int i = 0; i < s; ++i) {
            if (subset & (1 << i)) value = static_cast<unsigned char>(value | (r[i] & columns));
        }
        image[subset] = value;
    }
    for (int I = 1; I < limit; ++I) {
        for (int J = 1; J < limit; ++J) {
            if (I & J) continue;
            const unsigned char x = image[I];
            const unsigned char y = image[J];
            if (x & y) continue;
            const int lhs = popcount16[static_cast<unsigned char>(x | y)];
            const int rhs = popcount16[static_cast<unsigned char>(I | J)];
            if (lhs < rhs + (strict ? 1 : 0)) return false;
        }
    }
    return true;
}

static bool legal_at_level(const std::array<unsigned char, 4>& r, int level) {
    if (!expansion_property(r, level, true)) return false;
    for (int s = level + 1; s <= 4; ++s) {
        if (!expansion_property(r, s, false)) return false;
    }
    const unsigned char first = static_cast<unsigned char>((1u << level) - 1u);
    for (int i = level; i < 4; ++i) {
        if ((r[i] & first) == 0) return false;
    }
    return true;
}

static unsigned char legal_levels(Matrix a) {
    const auto r = rows(a);
    unsigned char answer = 0;
    for (int level = 1; level <= 4; ++level) {
        if (legal_at_level(r, level)) answer = static_cast<unsigned char>(answer | (1u << (level - 1)));
    }
    return answer;
}

static bool scrambling(Matrix a) {
    const auto r = rows(a);
    for (int i = 0; i < 4; ++i) {
        for (int j = i + 1; j < 4; ++j) {
            if ((r[i] & r[j]) == 0) return false;
        }
    }
    return true;
}

// Boolean matrix product left * right.
static Matrix multiply(Matrix left, Matrix right) {
    const auto l = rows(left);
    const auto r = rows(right);
    std::array<unsigned char, 16> unions{};
    for (int subset = 1; subset < 16; ++subset) {
        const int bit = __builtin_ctz(subset);
        unions[subset] = static_cast<unsigned char>(unions[subset & (subset - 1)] | r[bit]);
    }
    Matrix product = 0;
    for (int i = 0; i < 4; ++i) {
        product = static_cast<Matrix>(product | (static_cast<Matrix>(unions[l[i]]) << (4 * i)));
    }
    return product;
}

static std::string hex4(Matrix a) {
    static constexpr char digits[] = "0123456789abcdef";
    std::string out(4, '0');
    for (int i = 3; i >= 0; --i) {
        out[i] = digits[a & 15u];
        a = static_cast<Matrix>(a >> 4);
    }
    return out;
}

int main(int argc, char** argv) {
    const std::string output_path = argc >= 2 ? argv[1] : "evidence/search_result.json";
    const std::string certificate_path = argc >= 3 ? argv[2] : "evidence/frontier_certificate.txt";
    for (int i = 1; i < 65536; ++i) {
        popcount16[i] = static_cast<unsigned char>(popcount16[i >> 1] + (i & 1));
    }
    std::vector<Matrix> alphabet;
    std::array<std::uint32_t, 4> level_counts{};
    std::array<std::uint32_t, 16> exact_level_mask_counts{};
    std::array<unsigned char, 65536> levels{};
    for (int a0 = 1; a0 < 16; ++a0) {
        for (int a1 = 1; a1 < 16; ++a1) {
            for (int a2 = 1; a2 < 16; ++a2) {
                for (int a3 = 1; a3 < 16; ++a3) {
                    const Matrix a = static_cast<Matrix>(a0 | (a1 << 4) | (a2 << 8) | (a3 << 12));
                    const unsigned char mask = legal_levels(a);
                    levels[a] = mask;
                    ++exact_level_mask_counts[mask];
                    if (mask) alphabet.push_back(a);
                    for (int level = 0; level < 4; ++level) {
                        if (mask & (1u << level)) ++level_counts[level];
                    }
                }
            }
        }
    }
    std::sort(alphabet.begin(), alphabet.end());

    const Matrix identity = static_cast<Matrix>(0x8421u);
    std::vector<std::vector<Matrix>> frontiers;
    frontiers.push_back({identity});
    std::vector<std::vector<Matrix>> parent;
    std::vector<std::vector<Matrix>> factor;
    parent.emplace_back(65536, std::numeric_limits<Matrix>::max());
    factor.emplace_back(65536, std::numeric_limits<Matrix>::max());

    int horizon = -1;
    for (int depth = 1; depth <= 18; ++depth) {
        std::array<unsigned char, 65536> present{};
        std::vector<Matrix> next;
        std::vector<Matrix> p(65536, std::numeric_limits<Matrix>::max());
        std::vector<Matrix> f(65536, std::numeric_limits<Matrix>::max());
        for (Matrix previous : frontiers.back()) {
            for (Matrix a : alphabet) {
                const Matrix product = multiply(a, previous);
                if (scrambling(product) || present[product]) continue;
                present[product] = 1;
                next.push_back(product);
                p[product] = previous;
                f[product] = a;
            }
        }
        std::sort(next.begin(), next.end());
        frontiers.push_back(std::move(next));
        parent.push_back(std::move(p));
        factor.push_back(std::move(f));
        std::cerr << "depth " << depth << ": " << frontiers.back().size() << " nonscrambling products\n";
        if (frontiers.back().empty()) {
            horizon = depth;
            break;
        }
    }
    if (horizon < 0) {
        std::cerr << "No empty frontier through the known bound 18.\n";
        return 2;
    }

    Matrix state = frontiers[horizon - 1].front();
    const Matrix terminal_state = state;
    std::vector<Matrix> witness(horizon - 1);
    for (int depth = horizon - 1; depth >= 1; --depth) {
        witness[depth - 1] = factor[depth][state];
        state = parent[depth][state];
    }
    if (state != identity) {
        std::cerr << "Broken parent chain.\n";
        return 3;
    }
    Matrix reconstructed = identity;
    for (Matrix a : witness) {
        if (!levels[a]) {
            std::cerr << "Witness contains an illegal factor.\n";
            return 4;
        }
        reconstructed = multiply(a, reconstructed);
    }
    if (reconstructed != terminal_state || scrambling(reconstructed)) {
        std::cerr << "Witness verification failed.\n";
        return 5;
    }

    std::ofstream out(output_path);
    if (!out) {
        std::cerr << "Cannot open output file.\n";
        return 6;
    }
    out << "{\n";
    out << "  \"method\": \"complete enumeration of 15^4 row-nonempty supports and exact Boolean left products\",\n";
    out << "  \"row_nonempty_supports\": 50625,\n";
    out << "  \"legal_union_count\": " << alphabet.size() << ",\n";
    out << "  \"legal_level_counts\": [" << level_counts[0] << ", " << level_counts[1] << ", " << level_counts[2] << ", " << level_counts[3] << "],\n";
    out << "  \"exact_level_mask_counts\": {\n";
    bool first_mask = true;
    for (int mask = 0; mask < 16; ++mask) {
        if (exact_level_mask_counts[mask] == 0) continue;
        if (!first_mask) out << ",\n";
        first_mask = false;
        out << "    \"" << std::hex << mask << std::dec << "\": " << exact_level_mask_counts[mask];
    }
    out << "\n  },\n";
    out << "  \"nonscrambling_frontier_counts_by_length\": [";
    for (int depth = 0; depth <= horizon; ++depth) {
        if (depth) out << ", ";
        out << frontiers[depth].size();
    }
    out << "],\n";
    out << "  \"horizon\": " << horizon << ",\n";
    out << "  \"witness_convention\": \"listed P_1,...,P_(h-1); product is P_(h-1)*...*P_1\",\n";
    out << "  \"witness_hex_row_packed\": [";
    for (std::size_t i = 0; i < witness.size(); ++i) {
        if (i) out << ", ";
        out << "\"" << hex4(witness[i]) << "\"";
    }
    out << "],\n";
    out << "  \"witness_level_masks_hex\": [";
    for (std::size_t i = 0; i < witness.size(); ++i) {
        if (i) out << ", ";
        out << "\"" << std::hex << static_cast<int>(levels[witness[i]]) << std::dec << "\"";
    }
    out << "],\n";
    out << "  \"witness_product_hex_row_packed\": \"" << hex4(reconstructed) << "\",\n";
    out << "  \"witness_product_rows_hex\": [";
    const auto terminal_rows = rows(reconstructed);
    for (int i = 0; i < 4; ++i) {
        if (i) out << ", ";
        out << "\"" << std::hex << static_cast<int>(terminal_rows[i]) << std::dec << "\"";
    }
    out << "],\n";
    out << "  \"disjoint_product_row_pairs_zero_based\": [";
    bool first_pair = true;
    for (int i = 0; i < 4; ++i) {
        for (int j = i + 1; j < 4; ++j) {
            if (terminal_rows[i] & terminal_rows[j]) continue;
            if (!first_pair) out << ", ";
            first_pair = false;
            out << "[" << i << ", " << j << "]";
        }
    }
    out << "]\n";
    out << "}\n";
    out.close();

    // A deliberately simple, complete text certificate.  It records the entire
    // legal alphabet and every sorted nonscrambling exact-length frontier, so a
    // separate implementation can compare sets rather than trusting counts.
    std::ofstream cert(certificate_path);
    if (!cert) {
        std::cerr << "Cannot open certificate file.\n";
        return 7;
    }
    cert << "BIGMAC4-CERT-v1\n";
    cert << "ALPHABET " << alphabet.size() << "\n";
    for (Matrix a : alphabet) cert << hex4(a) << "\n";
    for (int depth = 0; depth <= horizon; ++depth) {
        cert << "FRONTIER " << depth << " " << frontiers[depth].size() << "\n";
        for (Matrix a : frontiers[depth]) cert << hex4(a) << "\n";
    }
    cert << "HORIZON " << horizon << "\n";
    cert << "WITNESS " << witness.size() << "\n";
    for (Matrix a : witness) cert << hex4(a) << "\n";
    cert << "PRODUCT " << hex4(reconstructed) << "\n";
    cert << "END\n";
    cert.close();
    std::cout << "Wrote " << output_path << "\n";
    std::cout << "Wrote " << certificate_path << "\n";
    return 0;
}
