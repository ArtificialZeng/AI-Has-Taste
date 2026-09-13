#include <algorithm>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

// Breaker specialized to alphabet [3].  Every SSYT is encoded by six counts
// (a,b,c,d,e,f) for rows 1^a2^b3^c / 2^d3^e / 3^f.  The exact validity
// conditions are d<=a, d+e<=a+b, and f<=d.

using Word = std::vector<int>;
using Tableau = std::vector<std::vector<int>>;

static void bump(Tableau &tableau, int value) {
    for (auto &row : tableau) {
        auto position = std::upper_bound(row.begin(), row.end(), value);
        if (position == row.end()) {
            row.push_back(value);
            return;
        }
        std::swap(value, *position);
    }
    tableau.push_back({value});
}

static void multiply(Tableau &tableau, const Word &word) {
    for (int value : word) bump(tableau, value);
}

static std::string key(const Tableau &tableau) {
    std::ostringstream text;
    for (const auto &row : tableau) {
        text << '[';
        for (int value : row) text << value << ',';
        text << ']';
    }
    return text.str();
}

static Word reading_word(const Tableau &tableau) {
    Word word;
    for (auto row = tableau.rbegin(); row != tableau.rend(); ++row) {
        word.insert(word.end(), row->begin(), row->end());
    }
    return word;
}

struct Item {
    std::string serial;
    Tableau tableau;
    Word representative;
};

static void append_repeated(std::vector<int> &row, int value, int count) {
    row.insert(row.end(), count, value);
}

static std::vector<Item> six_coordinate_classes(
    int minimum_size,
    int maximum_size,
    bool require_packed,
    std::map<int, std::uint64_t> &counts
) {
    std::vector<std::vector<Item>> by_size(maximum_size + 1);
    for (int a = 0; a <= maximum_size; ++a)
    for (int b = 0; a + b <= maximum_size; ++b)
    for (int c = 0; a + b + c <= maximum_size; ++c)
    for (int d = 0; a + b + c + d <= maximum_size; ++d) {
        if (d > a) continue;
        for (int e = 0; a + b + c + d + e <= maximum_size; ++e) {
            if (d + e > a + b) continue;
            for (int f = 0; a + b + c + d + e + f <= maximum_size; ++f) {
                if (f > d) continue;
                const int size = a + b + c + d + e + f;
                if (size < minimum_size) continue;
                if (require_packed && !(a > 0 && b + d > 0 && c + e + f > 0)) continue;
                Tableau tableau;
                if (a + b + c > 0) {
                    tableau.emplace_back();
                    append_repeated(tableau.back(), 1, a);
                    append_repeated(tableau.back(), 2, b);
                    append_repeated(tableau.back(), 3, c);
                }
                if (d + e > 0) {
                    tableau.emplace_back();
                    append_repeated(tableau.back(), 2, d);
                    append_repeated(tableau.back(), 3, e);
                }
                if (f > 0) tableau.push_back(std::vector<int>(f, 3));
                const Word representative = reading_word(tableau);
                Tableau check;
                multiply(check, representative);
                if (check != tableau) throw std::logic_error("invalid coordinate tableau");
                by_size[size].push_back({key(tableau), tableau, representative});
            }
        }
    }
    std::vector<Item> all;
    for (int size = minimum_size; size <= maximum_size; ++size) {
        auto &items = by_size[size];
        std::sort(items.begin(), items.end(), [](const Item &x, const Item &y) {
            return x.serial < y.serial;
        });
        for (std::size_t i = 1; i < items.size(); ++i) {
            if (items[i - 1].serial == items[i].serial) throw std::logic_error("duplicate coordinate");
        }
        counts[size] = items.size();
        all.insert(all.end(), items.begin(), items.end());
    }
    return all;
}

class Bits {
  public:
    explicit Bits(const std::string &path) : output(path, std::ios::binary) {
        if (!output) throw std::runtime_error("cannot create trace");
    }
    void add(bool value) {
        byte = static_cast<unsigned char>((byte << 1) | (value ? 1 : 0));
        ++used;
        ++number_bits;
        if (used == 8) flush();
    }
    void finish() {
        if (used) {
            byte = static_cast<unsigned char>(byte << (8 - used));
            flush();
        }
        output.flush();
        if (!output) throw std::runtime_error("failed to write trace");
    }
    std::uint64_t bits() const { return number_bits; }
    std::uint64_t bytes() const { return number_bytes; }
  private:
    void flush() {
        output.put(static_cast<char>(byte));
        byte = 0;
        used = 0;
        ++number_bytes;
    }
    std::ofstream output;
    unsigned char byte = 0;
    int used = 0;
    std::uint64_t number_bits = 0;
    std::uint64_t number_bytes = 0;
};

static int exact_integer(const char *text) {
    std::string input(text);
    std::size_t consumed = 0;
    int answer = std::stoi(input, &consumed);
    if (consumed != input.size()) throw std::invalid_argument("bad integer argument");
    return answer;
}

static void count_json(std::ostream &out, const std::map<int, std::uint64_t> &counts) {
    out << '{';
    bool first = true;
    for (const auto &[size, count] : counts) {
        if (!first) out << ',';
        first = false;
        out << '"' << size << "\":" << count;
    }
    out << '}';
}

static void word_json(std::ostream &out, const Word &word) {
    out << '[';
    for (std::size_t i = 0; i < word.size(); ++i) {
        if (i) out << ',';
        out << word[i];
    }
    out << ']';
}

int main(int argc, char **argv) {
    try {
        if (argc != 9) {
            throw std::invalid_argument(
                "usage: coordinate_discovery UMIN UMAX WMAX KFIRST KLAST TRACE RESULT LABEL"
            );
        }
        const int u_min = exact_integer(argv[1]);
        const int u_max = exact_integer(argv[2]);
        const int w_max = exact_integer(argv[3]);
        const int k_first = exact_integer(argv[4]);
        const int k_last = exact_integer(argv[5]);
        const std::string trace_path = argv[6];
        const std::string result_path = argv[7];
        const std::string label = argv[8];
        if (u_min < 3 || u_max < u_min || w_max < 0 || k_first < 3 || k_last < k_first) {
            throw std::invalid_argument("invalid search range");
        }
        const auto start = std::chrono::steady_clock::now();
        std::map<int, std::uint64_t> u_counts;
        std::map<int, std::uint64_t> w_counts;
        const auto us = six_coordinate_classes(u_min, u_max, true, u_counts);
        const auto ws = six_coordinate_classes(0, w_max, false, w_counts);
        const int final_exponent = k_last + 1;
        Bits trace(trace_path);
        std::uint64_t violations = 0;
        Word first_u;
        Word first_w;
        int first_k = -1;
        bool first_membership = false;
        bool next_membership = false;
        for (const auto &u : us) {
            std::vector<Tableau> powers(final_exponent + 1);
            for (int k = 1; k <= final_exponent; ++k) {
                powers[k] = powers[k - 1];
                multiply(powers[k], u.representative);
            }
            for (const auto &w : ws) {
                Tableau right = w.tableau;
                std::vector<bool> membership(final_exponent + 1, false);
                for (int k = 1; k <= final_exponent; ++k) {
                    multiply(right, u.representative);
                    if (k >= k_first) {
                        Tableau left = powers[k];
                        multiply(left, w.representative);
                        membership[k] = left == right;
                    }
                }
                for (int k = k_first; k <= final_exponent; ++k) trace.add(membership[k]);
                for (int k = k_first; k <= k_last; ++k) {
                    if (membership[k] != membership[k + 1]) {
                        ++violations;
                        if (first_k < 0) {
                            first_u = u.representative;
                            first_w = w.representative;
                            first_k = k;
                            first_membership = membership[k];
                            next_membership = membership[k + 1];
                        }
                    }
                }
            }
        }
        trace.finish();
        const auto stop = std::chrono::steady_clock::now();
        const double seconds = std::chrono::duration<double>(stop - start).count();
        const std::uint64_t pairs =
            static_cast<std::uint64_t>(us.size()) * static_cast<std::uint64_t>(ws.size());
        std::ofstream result(result_path);
        if (!result) throw std::runtime_error("cannot create result JSON");
        result << "{\n\"schema_version\":1,\n"
               << "\"claim\":\"" << (violations ? "counterexample_found" : "finite_no_membership_change") << "\",\n"
               << "\"parameters\":{\"u_alphabet\":3,\"u_require_packed\":true,"
               << "\"u_min_length\":" << u_min << ",\"u_max_length\":" << u_max
               << ",\"w_alphabet\":3,\"w_min_length\":0,\"w_max_length\":" << w_max
               << ",\"k_first\":" << k_first << ",\"k_last_compared\":" << k_last << "},\n"
               << "\"counts\":{\"u_classes_by_length\":";
        count_json(result, u_counts);
        result << ",\"w_classes_by_length\":";
        count_json(result, w_counts);
        result << ",\"u_classes_total\":" << us.size()
               << ",\"w_classes_total\":" << ws.size()
               << ",\"class_pairs\":" << pairs
               << ",\"membership_bits\":" << trace.bits()
               << ",\"trace_bytes\":" << trace.bytes()
               << ",\"adjacent_membership_comparisons\":"
               << pairs * static_cast<std::uint64_t>(k_last - k_first + 1)
               << ",\"violations\":" << violations << "},\n"
               << "\"first_violation\":";
        if (first_k < 0) {
            result << "null,\n";
        } else {
            result << "{\"schema_version\":1,\"claim\":\"membership_changes\",\"u\":";
            word_json(result, first_u);
            result << ",\"w\":";
            word_json(result, first_w);
            result << ",\"k_a\":" << first_k << ",\"k_b\":" << first_k + 1
                   << ",\"membership_a\":" << (first_membership ? "true" : "false")
                   << ",\"membership_b\":" << (next_membership ? "true" : "false") << "},\n";
        }
        result << "\"enumerator\":\"six_coordinates_1a2b3c_over_2d3e_over_3f\",\n"
               << "\"run_label\":\"" << label << "\",\n"
               << "\"runtime_seconds_diagnostic_only\":" << seconds << "\n}\n";
        result.flush();
        if (!result) throw std::runtime_error("failed to write result JSON");
        std::cout << "COORDINATE_SEARCH_OK u_classes=" << us.size()
                  << " w_classes=" << ws.size()
                  << " pairs=" << pairs
                  << " adjacent=" << pairs * static_cast<std::uint64_t>(k_last - k_first + 1)
                  << " violations=" << violations
                  << " seconds=" << seconds << '\n';
        return violations == 0 ? 0 : 2;
    } catch (const std::exception &error) {
        std::cerr << "COORDINATE_SEARCH_ERROR " << error.what() << '\n';
        return 1;
    }
}
