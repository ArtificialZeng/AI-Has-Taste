#include <algorithm>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

// Discovery implementation.  The independent verifier deliberately does not
// compile or import this file.

using Word = std::vector<int>;
using Tableau = std::vector<std::vector<int>>;

static void insert_row(Tableau &t, int x) {
    for (auto &row : t) {
        auto it = std::upper_bound(row.begin(), row.end(), x);
        if (it == row.end()) {
            row.push_back(x);
            return;
        }
        std::swap(x, *it);
    }
    t.push_back({x});
}

static Tableau insertion_tableau(const Word &word) {
    Tableau t;
    for (int x : word) insert_row(t, x);
    return t;
}

static void insert_word(Tableau &t, const Word &word) {
    for (int x : word) insert_row(t, x);
}

static std::string tableau_key(const Tableau &t) {
    std::ostringstream out;
    for (const auto &row : t) {
        out << '[';
        for (int x : row) out << x << ',';
        out << ']';
    }
    return out.str();
}

// Reading bottom rows first and each row left-to-right gives a word whose
// row-insertion tableau is t.
static Word row_reading_word(const Tableau &t) {
    Word word;
    for (auto r = t.rbegin(); r != t.rend(); ++r) {
        word.insert(word.end(), r->begin(), r->end());
    }
    return word;
}

static bool has_support_123(const Tableau &t) {
    bool seen[4] = {false, false, false, false};
    for (const auto &row : t) {
        for (int x : row) {
            if (x < 1 || x > 3) return false;
            seen[x] = true;
        }
    }
    return seen[1] && seen[2] && seen[3];
}

struct ClassRepresentative {
    std::string key;
    Tableau tableau;
    Word word;
    int length;
};

static void enumerate_leaf_tableaux(
    int alphabet,
    int remaining,
    Tableau current,
    std::map<std::string, Tableau> &out
) {
    if (remaining == 0) {
        out.emplace(tableau_key(current), std::move(current));
        return;
    }
    for (int x = 1; x <= alphabet; ++x) {
        Tableau next = current;
        insert_row(next, x);
        enumerate_leaf_tableaux(alphabet, remaining - 1, std::move(next), out);
    }
}

static std::vector<ClassRepresentative> enumerate_classes(
    int alphabet,
    int min_length,
    int max_length,
    bool require_support_123,
    std::map<int, std::uint64_t> &counts
) {
    std::vector<ClassRepresentative> classes;
    for (int n = min_length; n <= max_length; ++n) {
        std::map<std::string, Tableau> at_length;
        enumerate_leaf_tableaux(alphabet, n, {}, at_length);
        std::uint64_t accepted = 0;
        for (const auto &[key, t] : at_length) {
            if (require_support_123 && !has_support_123(t)) continue;
            Word representative = row_reading_word(t);
            if (insertion_tableau(representative) != t) {
                throw std::logic_error("row-reading representative failed");
            }
            classes.push_back({key, t, std::move(representative), n});
            ++accepted;
        }
        counts[n] = accepted;
    }
    return classes;
}

class BitWriter {
  public:
    explicit BitWriter(const std::string &path) : output_(path, std::ios::binary) {
        if (!output_) throw std::runtime_error("cannot open trace output");
    }

    void write(bool bit) {
        byte_ = static_cast<unsigned char>((byte_ << 1) | (bit ? 1 : 0));
        ++used_;
        ++bits_;
        if (used_ == 8) flush_byte();
    }

    void finish() {
        if (used_ != 0) {
            byte_ = static_cast<unsigned char>(byte_ << (8 - used_));
            flush_byte();
        }
        output_.flush();
        if (!output_) throw std::runtime_error("failed writing trace output");
    }

    std::uint64_t bits() const { return bits_; }
    std::uint64_t bytes() const { return bytes_; }

  private:
    void flush_byte() {
        output_.put(static_cast<char>(byte_));
        byte_ = 0;
        used_ = 0;
        ++bytes_;
    }

    std::ofstream output_;
    unsigned char byte_ = 0;
    int used_ = 0;
    std::uint64_t bits_ = 0;
    std::uint64_t bytes_ = 0;
};

static std::string word_json(const Word &word) {
    std::ostringstream out;
    out << '[';
    for (std::size_t i = 0; i < word.size(); ++i) {
        if (i) out << ',';
        out << word[i];
    }
    out << ']';
    return out.str();
}

static void print_count_map(std::ostream &out, const std::map<int, std::uint64_t> &counts) {
    out << '{';
    bool first = true;
    for (const auto &[n, count] : counts) {
        if (!first) out << ',';
        first = false;
        out << '"' << n << "\":" << count;
    }
    out << '}';
}

struct Options {
    int u_min_length = 3;
    int u_max_length = 8;
    int w_alphabet = 3;
    int w_max_length = 10;
    int k_first = 3;
    int k_last = 14;
    std::string trace_path;
    std::string result_path;
    bool self_test = false;
};

static int parse_positive(const char *text, const std::string &name, bool allow_zero = false) {
    std::string s(text);
    std::size_t used = 0;
    long value = 0;
    try {
        value = std::stol(s, &used);
    } catch (...) {
        throw std::invalid_argument("invalid integer for " + name);
    }
    if (used != s.size() || value < (allow_zero ? 0 : 1) || value > 1000) {
        throw std::invalid_argument("out-of-range integer for " + name);
    }
    return static_cast<int>(value);
}

static Options parse_options(int argc, char **argv) {
    Options options;
    for (int i = 1; i < argc; ++i) {
        std::string arg(argv[i]);
        if (arg == "--self-test") {
            options.self_test = true;
            continue;
        }
        if (i + 1 >= argc) throw std::invalid_argument("missing value for " + arg);
        const char *value = argv[++i];
        if (arg == "--u-min-length") options.u_min_length = parse_positive(value, arg);
        else if (arg == "--u-max-length") options.u_max_length = parse_positive(value, arg);
        else if (arg == "--w-alphabet") options.w_alphabet = parse_positive(value, arg);
        else if (arg == "--w-max-length") options.w_max_length = parse_positive(value, arg, true);
        else if (arg == "--k-first") options.k_first = parse_positive(value, arg);
        else if (arg == "--k-last") options.k_last = parse_positive(value, arg);
        else if (arg == "--trace") options.trace_path = value;
        else if (arg == "--result") options.result_path = value;
        else throw std::invalid_argument("unknown option " + arg);
    }
    return options;
}

static void run_self_test() {
    assert(insertion_tableau({1, 3, 2}) == Tableau({{1, 2}, {3}}));
    assert(insertion_tableau({3, 1, 2}) == Tableau({{1, 2}, {3}}));
    assert(insertion_tableau({2, 1, 3}) == insertion_tableau({2, 3, 1}));
    assert(insertion_tableau({1, 2, 1}) == insertion_tableau({2, 1, 1}));
    assert(insertion_tableau({2, 1, 2}) == insertion_tableau({2, 2, 1}));
    Tableau hand = {{1, 1, 3}, {2, 3}, {4}};
    assert(insertion_tableau(row_reading_word(hand)) == hand);
    std::cout << "SELF_TEST_OK\n";
}

int main(int argc, char **argv) {
    try {
        Options options = parse_options(argc, argv);
        if (options.self_test) {
            run_self_test();
            return 0;
        }
        if (options.trace_path.empty() || options.result_path.empty()) {
            throw std::invalid_argument("--trace and --result are required");
        }
        if (options.u_min_length < 3 || options.u_max_length < options.u_min_length) {
            throw std::invalid_argument("invalid u length interval");
        }
        if (options.w_alphabet < 1 || options.k_first < 1 || options.k_last < options.k_first) {
            throw std::invalid_argument("invalid alphabet or exponent interval");
        }

        const auto start = std::chrono::steady_clock::now();
        std::map<int, std::uint64_t> u_counts;
        std::map<int, std::uint64_t> w_counts;
        const auto u_classes = enumerate_classes(
            3, options.u_min_length, options.u_max_length, true, u_counts
        );
        const auto w_classes = enumerate_classes(
            options.w_alphabet, 0, options.w_max_length, false, w_counts
        );

        BitWriter trace(options.trace_path);
        std::uint64_t violations = 0;
        Word first_u;
        Word first_w;
        int first_k = -1;
        bool first_membership = false;
        bool second_membership = false;
        const int final_exponent = options.k_last + 1;

        for (const auto &u : u_classes) {
            std::vector<Tableau> powers(final_exponent + 1);
            for (int k = 1; k <= final_exponent; ++k) {
                powers[k] = powers[k - 1];
                insert_word(powers[k], u.word);
            }
            for (const auto &w : w_classes) {
                Tableau right = w.tableau; // P(w u^k), updated below.
                std::vector<bool> membership(final_exponent + 1, false);
                for (int k = 1; k <= final_exponent; ++k) {
                    insert_word(right, u.word);
                    if (k >= options.k_first) {
                        Tableau left = powers[k];
                        insert_word(left, w.word);
                        membership[k] = (left == right);
                    }
                }
                for (int k = options.k_first; k <= final_exponent; ++k) {
                    trace.write(membership[k]);
                }
                for (int k = options.k_first; k <= options.k_last; ++k) {
                    if (membership[k] != membership[k + 1]) {
                        ++violations;
                        if (first_k < 0) {
                            first_u = u.word;
                            first_w = w.word;
                            first_k = k;
                            first_membership = membership[k];
                            second_membership = membership[k + 1];
                        }
                    }
                }
            }
        }
        trace.finish();

        const auto stop = std::chrono::steady_clock::now();
        const double seconds = std::chrono::duration<double>(stop - start).count();
        const std::uint64_t pairs =
            static_cast<std::uint64_t>(u_classes.size()) *
            static_cast<std::uint64_t>(w_classes.size());
        const std::uint64_t adjacent =
            pairs * static_cast<std::uint64_t>(options.k_last - options.k_first + 1);

        std::ofstream out(options.result_path);
        if (!out) throw std::runtime_error("cannot open result output");
        out << "{\n";
        out << "  \"schema_version\": 1,\n";
        out << "  \"claim\": \""
            << (violations == 0 ? "finite_no_membership_change" : "counterexample_found")
            << "\",\n";
        out << "  \"parameters\": {\"u_alphabet\":3,\"u_require_packed\":true,"
            << "\"u_min_length\":" << options.u_min_length
            << ",\"u_max_length\":" << options.u_max_length
            << ",\"w_alphabet\":" << options.w_alphabet
            << ",\"w_min_length\":0"
            << ",\"w_max_length\":" << options.w_max_length
            << ",\"k_first\":" << options.k_first
            << ",\"k_last_compared\":" << options.k_last << "},\n";
        out << "  \"counts\": {\"u_classes_by_length\":";
        print_count_map(out, u_counts);
        out << ",\"w_classes_by_length\":";
        print_count_map(out, w_counts);
        out << ",\"u_classes_total\":" << u_classes.size()
            << ",\"w_classes_total\":" << w_classes.size()
            << ",\"class_pairs\":" << pairs
            << ",\"membership_bits\":" << trace.bits()
            << ",\"trace_bytes\":" << trace.bytes()
            << ",\"adjacent_membership_comparisons\":" << adjacent
            << ",\"violations\":" << violations << "},\n";
        out << "  \"first_violation\":";
        if (first_k < 0) {
            out << "null,\n";
        } else {
            out << "{\"schema_version\":1,\"claim\":\"membership_changes\","
                << "\"u\":" << word_json(first_u)
                << ",\"w\":" << word_json(first_w)
                << ",\"k_a\":" << first_k
                << ",\"k_b\":" << first_k + 1
                << ",\"membership_a\":" << (first_membership ? "true" : "false")
                << ",\"membership_b\":" << (second_membership ? "true" : "false")
                << "},\n";
        }
        out << "  \"runtime_seconds_diagnostic_only\":" << seconds << "\n";
        out << "}\n";
        out.flush();
        if (!out) throw std::runtime_error("failed writing result output");

        std::cout << "u_classes=" << u_classes.size()
                  << " w_classes=" << w_classes.size()
                  << " class_pairs=" << pairs
                  << " adjacent_comparisons=" << adjacent
                  << " violations=" << violations
                  << " trace_bits=" << trace.bits()
                  << " seconds=" << seconds << "\n";
        return violations == 0 ? 0 : 2;
    } catch (const std::exception &error) {
        std::cerr << "ERROR: " << error.what() << '\n';
        return 1;
    }
}
