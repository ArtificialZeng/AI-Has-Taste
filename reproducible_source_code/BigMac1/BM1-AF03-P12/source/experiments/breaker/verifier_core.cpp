#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

// Independent certification core.  Unlike discovery.cpp, this enumerates
// semistandard tableaux directly from partition shapes and evaluates P(word)
// by column-inserting the reversed word.

using Rows = std::vector<std::vector<int>>;
using Letters = std::vector<int>;

struct Representative {
    std::string serial;
    Rows rows;
    Letters row_word;
    int size;
};

static std::string serial(const Rows &rows) {
    std::ostringstream text;
    for (const auto &row : rows) {
        text << '[';
        for (int x : row) text << x << ',';
        text << ']';
    }
    return text.str();
}

static Letters make_row_word(const Rows &rows) {
    Letters answer;
    for (auto row = rows.rbegin(); row != rows.rend(); ++row) {
        answer.insert(answer.end(), row->begin(), row->end());
    }
    return answer;
}

static void generate_partitions(
    int remaining,
    int ceiling,
    std::vector<int> &prefix,
    std::vector<std::vector<int>> &answer
) {
    if (remaining == 0) {
        answer.push_back(prefix);
        return;
    }
    const int upper = std::min(remaining, ceiling);
    for (int first = upper; first >= 1; --first) {
        prefix.push_back(first);
        generate_partitions(remaining - first, first, prefix, answer);
        prefix.pop_back();
    }
}

static void fill_shape(
    Rows &rows,
    const std::vector<std::pair<int, int>> &cells,
    std::size_t position,
    int alphabet,
    bool packed,
    std::vector<Representative> &answer
) {
    if (position == cells.size()) {
        if (packed) {
            bool found[4] = {false, false, false, false};
            for (const auto &row : rows) for (int x : row) {
                if (x >= 1 && x <= 3) found[x] = true;
            }
            if (!(found[1] && found[2] && found[3])) return;
        }
        answer.push_back({serial(rows), rows, make_row_word(rows), static_cast<int>(cells.size())});
        return;
    }
    const auto [i, j] = cells[position];
    int lower = 1;
    if (j > 0) lower = std::max(lower, rows[i][j - 1]);
    if (i > 0) lower = std::max(lower, rows[i - 1][j] + 1);
    for (int x = lower; x <= alphabet; ++x) {
        rows[i][j] = x;
        fill_shape(rows, cells, position + 1, alphabet, packed, answer);
    }
}

static std::vector<Representative> enumerate_ssyt(
    int alphabet,
    int minimum_size,
    int maximum_size,
    bool packed,
    std::map<int, std::uint64_t> &counts
) {
    std::vector<Representative> all;
    for (int size = minimum_size; size <= maximum_size; ++size) {
        std::vector<std::vector<int>> shapes;
        std::vector<int> prefix;
        generate_partitions(size, size, prefix, shapes);
        std::vector<Representative> current;
        for (const auto &shape : shapes) {
            if (static_cast<int>(shape.size()) > alphabet) continue;
            Rows rows;
            std::vector<std::pair<int, int>> cells;
            for (int i = 0; i < static_cast<int>(shape.size()); ++i) {
                rows.push_back(std::vector<int>(shape[i], 0));
                for (int j = 0; j < shape[i]; ++j) cells.push_back({i, j});
            }
            fill_shape(rows, cells, 0, alphabet, packed, current);
        }
        std::sort(current.begin(), current.end(), [](const auto &a, const auto &b) {
            return a.serial < b.serial;
        });
        counts[size] = current.size();
        all.insert(all.end(), current.begin(), current.end());
    }
    return all;
}

static void insert_column(Rows &rows, int x) {
    int column = 0;
    while (true) {
        int row = 0;
        while (row < static_cast<int>(rows.size()) && column < static_cast<int>(rows[row].size())) {
            if (rows[row][column] >= x) break;
            ++row;
        }
        if (row == static_cast<int>(rows.size()) || column == static_cast<int>(rows[row].size())) {
            if (row == static_cast<int>(rows.size())) {
                if (column != 0) throw std::logic_error("invalid outer corner");
                rows.push_back({x});
            } else {
                if (static_cast<int>(rows[row].size()) != column) {
                    throw std::logic_error("invalid row boundary");
                }
                rows[row].push_back(x);
            }
            return;
        }
        std::swap(rows[row][column], x);
        ++column;
    }
}

static void insert_reversal(Rows &rows, const Letters &word) {
    for (auto x = word.rbegin(); x != word.rend(); ++x) insert_column(rows, *x);
}

class PackedBits {
  public:
    explicit PackedBits(const std::string &path) : stream(path, std::ios::binary) {
        if (!stream) throw std::runtime_error("cannot open rebuilt trace");
    }
    void append(bool value) {
        byte = static_cast<unsigned char>((byte << 1) | (value ? 1 : 0));
        ++used;
        ++bit_count;
        if (used == 8) emit();
    }
    void finish() {
        if (used) {
            byte = static_cast<unsigned char>(byte << (8 - used));
            emit();
        }
        stream.flush();
        if (!stream) throw std::runtime_error("cannot finish rebuilt trace");
    }
    std::uint64_t bits() const { return bit_count; }
    std::uint64_t bytes() const { return byte_count; }
  private:
    void emit() {
        stream.put(static_cast<char>(byte));
        byte = 0;
        used = 0;
        ++byte_count;
    }
    std::ofstream stream;
    unsigned char byte = 0;
    int used = 0;
    std::uint64_t bit_count = 0;
    std::uint64_t byte_count = 0;
};

static int integer(const char *text) {
    std::string value(text);
    std::size_t used = 0;
    int answer = std::stoi(value, &used);
    if (used != value.size()) throw std::invalid_argument("invalid integer argument");
    return answer;
}

static void emit_counts(std::ostream &out, const std::map<int, std::uint64_t> &counts) {
    out << '{';
    bool first = true;
    for (const auto &[size, count] : counts) {
        if (!first) out << ',';
        first = false;
        out << '"' << size << "\":" << count;
    }
    out << '}';
}

int main(int argc, char **argv) {
    try {
        if (argc != 9) {
            throw std::invalid_argument(
                "usage: verifier_core UMIN UMAX WALPH WMAX KFIRST KLAST TRACE SUMMARY"
            );
        }
        const int u_min = integer(argv[1]);
        const int u_max = integer(argv[2]);
        const int w_alphabet = integer(argv[3]);
        const int w_max = integer(argv[4]);
        const int k_first = integer(argv[5]);
        const int k_last = integer(argv[6]);
        if (u_min < 3 || u_max < u_min || w_alphabet < 1 || w_max < 0 ||
            k_first < 3 || k_last < k_first) {
            throw std::invalid_argument("invalid finite range");
        }
        std::map<int, std::uint64_t> u_counts;
        std::map<int, std::uint64_t> w_counts;
        const auto us = enumerate_ssyt(3, u_min, u_max, true, u_counts);
        const auto ws = enumerate_ssyt(w_alphabet, 0, w_max, false, w_counts);
        const int final_exponent = k_last + 1;
        PackedBits bits(argv[7]);
        std::uint64_t violations = 0;

        for (const auto &u : us) {
            std::vector<Rows> powers(final_exponent + 1);
            for (int exponent = 1; exponent <= final_exponent; ++exponent) {
                powers[exponent] = powers[exponent - 1];
                insert_reversal(powers[exponent], u.row_word);
            }
            for (const auto &w : ws) {
                Rows left = w.rows;
                std::vector<bool> membership(final_exponent + 1, false);
                for (int exponent = 1; exponent <= final_exponent; ++exponent) {
                    insert_reversal(left, u.row_word);
                    if (exponent >= k_first) {
                        Rows right = powers[exponent];
                        insert_reversal(right, w.row_word);
                        membership[exponent] = left == right;
                    }
                }
                for (int exponent = k_first; exponent <= final_exponent; ++exponent) {
                    bits.append(membership[exponent]);
                }
                for (int exponent = k_first; exponent <= k_last; ++exponent) {
                    violations += membership[exponent] != membership[exponent + 1];
                }
            }
        }
        bits.finish();
        const std::uint64_t pairs =
            static_cast<std::uint64_t>(us.size()) * static_cast<std::uint64_t>(ws.size());
        std::ofstream summary(argv[8]);
        if (!summary) throw std::runtime_error("cannot open summary output");
        summary << "{\"u_counts\":";
        emit_counts(summary, u_counts);
        summary << ",\"w_counts\":";
        emit_counts(summary, w_counts);
        summary << ",\"u_total\":" << us.size()
                << ",\"w_total\":" << ws.size()
                << ",\"pairs\":" << pairs
                << ",\"bits\":" << bits.bits()
                << ",\"bytes\":" << bits.bytes()
                << ",\"adjacent\":" << pairs * static_cast<std::uint64_t>(k_last - k_first + 1)
                << ",\"violations\":" << violations << "}\n";
        summary.flush();
        if (!summary) throw std::runtime_error("cannot finish summary output");
        std::cout << "CERTIFIER_CORE_OK pairs=" << pairs
                  << " adjacent=" << pairs * static_cast<std::uint64_t>(k_last - k_first + 1)
                  << " violations=" << violations << '\n';
        return violations == 0 ? 0 : 2;
    } catch (const std::exception &error) {
        std::cerr << "CERTIFIER_CORE_ERROR " << error.what() << '\n';
        return 1;
    }
}
