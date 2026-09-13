#define main geng_search_program_main
#include "geng_excess2_search.cpp"
#undef main

#include <iostream>

int main() {
    std::string line;
    while (std::getline(std::cin, line)) {
        if (line.empty() || line[0] == '>') continue;
        const Adj a = parse_graph6(line);
        std::cout << 18 << '\n';
        for (int u = 6; u < 24; ++u) {
            for (int v = 6; v < 24; ++v)
                std::cout << (((a[u] >> v) & 1U) ? '1' : '0');
            std::cout << '\n';
        }
    }
}
