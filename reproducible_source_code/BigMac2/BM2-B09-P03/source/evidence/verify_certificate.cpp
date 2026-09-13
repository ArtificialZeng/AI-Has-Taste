#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

using Matrix = std::uint16_t;

static int cardinality(unsigned x) { return __builtin_popcount(x); }

static unsigned row(Matrix a, int i) { return (a >> (4 * i)) & 15u; }

// Independent formulation of GE/GR: enumerate ternary assignments of each
// domain index to neither set, I, or J.  Thus disjointness is automatic.
static bool leading_expansion(Matrix a, int size, bool strict) {
    const unsigned col_mask = (1u << size) - 1u;
    for (int i = 0; i < size; ++i) {
        if ((row(a, i) & col_mask) == 0) return false;
    }
    int assignments = 1;
    for (int i = 0; i < size; ++i) assignments *= 3;
    for (int code = 0; code < assignments; ++code) {
        int digits = code;
        unsigned I = 0, J = 0, image_I = 0, image_J = 0;
        for (int i = 0; i < size; ++i) {
            const int label = digits % 3;
            digits /= 3;
            if (label == 1) {
                I |= 1u << i;
                image_I |= row(a, i) & col_mask;
            } else if (label == 2) {
                J |= 1u << i;
                image_J |= row(a, i) & col_mask;
            }
        }
        if (I == 0 || J == 0 || (image_I & image_J)) continue;
        const int lhs = cardinality(image_I | image_J);
        const int rhs = cardinality(I | J) + (strict ? 1 : 0);
        if (lhs < rhs) return false;
    }
    return true;
}

static bool admitted_at(Matrix a, int level) {
    if (!leading_expansion(a, level, true)) return false;
    for (int size = level + 1; size <= 4; ++size) {
        if (!leading_expansion(a, size, false)) return false;
    }
    const unsigned accessible_columns = (1u << level) - 1u;
    for (int i = level; i < 4; ++i) {
        if ((row(a, i) & accessible_columns) == 0) return false;
    }
    return true;
}

static bool admitted(Matrix a) {
    for (int i = 0; i < 4; ++i) if (row(a, i) == 0) return false;
    for (int level = 1; level <= 4; ++level) {
        if (admitted_at(a, level)) return true;
    }
    return false;
}

static bool scrambling(Matrix a) {
    for (int i = 0; i < 4; ++i) {
        for (int j = i + 1; j < 4; ++j) {
            if ((row(a, i) & row(a, j)) == 0) return false;
        }
    }
    return true;
}

// Direct Boolean multiplication, used only for the short witness.
static Matrix direct_product(Matrix left, Matrix right) {
    Matrix answer = 0;
    for (int i = 0; i < 4; ++i) {
        unsigned image = 0;
        for (int k = 0; k < 4; ++k) {
            if (row(left, i) & (1u << k)) image |= row(right, k);
        }
        answer |= static_cast<Matrix>(image << (4 * i));
    }
    return answer;
}

static Matrix parse_hex(const std::string& text) {
    std::size_t used = 0;
    const unsigned long value = std::stoul(text, &used, 16);
    if (used != text.size() || value > 65535ul) throw std::runtime_error("bad hex matrix: " + text);
    return static_cast<Matrix>(value);
}

static void require(bool condition, const std::string& message) {
    if (!condition) throw std::runtime_error(message);
}

struct Certificate {
    std::vector<Matrix> alphabet;
    std::vector<std::vector<Matrix>> frontiers;
    int horizon = -1;
    std::vector<Matrix> witness;
    Matrix product = 0;
};

static Certificate read_certificate(const std::string& path) {
    std::ifstream in(path);
    require(static_cast<bool>(in), "cannot open certificate");
    std::string token;
    in >> token;
    require(token == "BIGMAC4-CERT-v1", "wrong certificate header");
    Certificate c;
    std::size_t count = 0;
    in >> token >> count;
    require(token == "ALPHABET", "missing alphabet header");
    c.alphabet.reserve(count);
    for (std::size_t i = 0; i < count; ++i) {
        in >> token;
        c.alphabet.push_back(parse_hex(token));
    }
    while (in >> token) {
        if (token == "FRONTIER") {
            int depth;
            in >> depth >> count;
            require(depth == static_cast<int>(c.frontiers.size()), "nonconsecutive frontier depth");
            std::vector<Matrix> f;
            f.reserve(count);
            for (std::size_t i = 0; i < count; ++i) {
                in >> token;
                f.push_back(parse_hex(token));
            }
            c.frontiers.push_back(std::move(f));
        } else if (token == "HORIZON") {
            in >> c.horizon;
            break;
        } else {
            throw std::runtime_error("unexpected certificate token before horizon: " + token);
        }
    }
    in >> token >> count;
    require(token == "WITNESS", "missing witness header");
    c.witness.reserve(count);
    for (std::size_t i = 0; i < count; ++i) {
        in >> token;
        c.witness.push_back(parse_hex(token));
    }
    in >> token;
    require(token == "PRODUCT", "missing product header");
    in >> token;
    c.product = parse_hex(token);
    in >> token;
    require(token == "END", "missing END marker");
    in >> token;
    require(!in, "trailing certificate data");
    return c;
}

int main(int argc, char** argv) {
    const std::string certificate_path = argc >= 2 ? argv[1] : "evidence/frontier_certificate.txt";
    const std::string report_path = argc >= 3 ? argv[2] : "evidence/verification_report.txt";
    try {
        const Certificate c = read_certificate(certificate_path);

        std::vector<Matrix> rebuilt_alphabet;
        std::size_t row_nonempty_count = 0;
        for (unsigned value = 0; value <= 65535u; ++value) {
            const Matrix a = static_cast<Matrix>(value);
            bool row_nonempty = true;
            for (int i = 0; i < 4; ++i) row_nonempty = row_nonempty && row(a, i) != 0;
            if (row_nonempty) ++row_nonempty_count;
            if (admitted(a)) rebuilt_alphabet.push_back(a);
        }
        require(row_nonempty_count == 50625, "row-nonempty domain count is not 15^4");
        require(std::is_sorted(c.alphabet.begin(), c.alphabet.end()), "certificate alphabet is not sorted");
        require(std::adjacent_find(c.alphabet.begin(), c.alphabet.end()) == c.alphabet.end(),
                "certificate alphabet has duplicates");
        require(rebuilt_alphabet == c.alphabet, "certificate alphabet differs from independently rebuilt union");

        require(!c.frontiers.empty(), "no frontiers");
        require(c.frontiers[0] == std::vector<Matrix>{static_cast<Matrix>(0x8421u)},
                "depth-zero frontier is not the identity");
        std::array<unsigned char, 65536> is_nonscrambling{};
        for (unsigned value = 0; value <= 65535u; ++value) {
            is_nonscrambling[value] = scrambling(static_cast<Matrix>(value)) ? 0 : 1;
        }

        std::vector<std::size_t> counts;
        counts.push_back(1);
        std::vector<Matrix> previous = c.frontiers[0];
        for (std::size_t depth = 1; depth < c.frontiers.size(); ++depth) {
            std::array<unsigned char, 65536> reached{};
            for (Matrix right : previous) {
                std::array<unsigned char, 16> image{};
                for (int subset = 0; subset < 16; ++subset) {
                    unsigned value = 0;
                    for (int k = 0; k < 4; ++k) {
                        if (subset & (1 << k)) value |= row(right, k);
                    }
                    image[subset] = static_cast<unsigned char>(value);
                }
                for (Matrix left : rebuilt_alphabet) {
                    const Matrix product = static_cast<Matrix>(
                        image[row(left, 0)] |
                        (static_cast<Matrix>(image[row(left, 1)]) << 4) |
                        (static_cast<Matrix>(image[row(left, 2)]) << 8) |
                        (static_cast<Matrix>(image[row(left, 3)]) << 12));
                    if (is_nonscrambling[product]) reached[product] = 1;
                }
            }
            std::vector<Matrix> rebuilt_frontier;
            for (unsigned value = 0; value <= 65535u; ++value) {
                if (reached[value]) rebuilt_frontier.push_back(static_cast<Matrix>(value));
            }
            require(rebuilt_frontier == c.frontiers[depth],
                    "frontier mismatch at depth " + std::to_string(depth));
            counts.push_back(rebuilt_frontier.size());
            previous = std::move(rebuilt_frontier);
        }
        require(c.horizon + 1 == static_cast<int>(c.frontiers.size()), "horizon/frontier count mismatch");
        require(c.horizon >= 1, "invalid horizon");
        require(c.frontiers[c.horizon].empty(), "horizon frontier is nonempty");
        require(!c.frontiers[c.horizon - 1].empty(), "preceding frontier is empty");

        require(static_cast<int>(c.witness.size()) == c.horizon - 1, "witness has wrong length");
        Matrix product = static_cast<Matrix>(0x8421u);
        for (Matrix factor : c.witness) {
            require(std::binary_search(rebuilt_alphabet.begin(), rebuilt_alphabet.end(), factor),
                    "witness has a nonadmitted factor");
            product = direct_product(factor, product);
        }
        require(product == c.product, "witness product differs from certificate product");
        require(!scrambling(product), "witness product is scrambling");
        require(std::binary_search(c.frontiers[c.horizon - 1].begin(),
                                   c.frontiers[c.horizon - 1].end(), product),
                "witness product is absent from maximal frontier");

        std::ofstream report(report_path);
        require(static_cast<bool>(report), "cannot open report file");
        report << "VERIFIED BIGMAC4-CERT-v1\n";
        report << "row_nonempty_supports 50625\n";
        report << "legal_union_count " << rebuilt_alphabet.size() << "\n";
        report << "frontier_counts";
        for (std::size_t n : counts) report << " " << n;
        report << "\n";
        report << "horizon " << c.horizon << "\n";
        report << "witness_length " << c.witness.size() << "\n";
        report << "witness_product_hex 17ef_expected " << std::hex << product << std::dec << "\n";
        report << "status exact_certificate_verified\n";
        report.close();
        std::cout << "Verified certificate; wrote " << report_path << "\n";
        return 0;
    } catch (const std::exception& error) {
        std::cerr << "VERIFICATION FAILED: " << error.what() << "\n";
        return 1;
    }
}
