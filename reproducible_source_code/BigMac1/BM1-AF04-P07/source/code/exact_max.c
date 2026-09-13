/* Exact maximum TT3 packing for retained Breaker candidates (not the sweep). */

#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_N 11
#define MAX_TRIS 165
#define MAX_PAIRS 55
#define MAX_ON_PAIR 9
#define MAX_PACK 18

typedef struct { uint64_t mask; unsigned char a, b, c; } Tri;

static int n, pair_count, pair_id[MAX_N][MAX_N];
static unsigned char arc[MAX_N][MAX_N];
static Tri tri[MAX_TRIS];
static int tri_count;
static unsigned char on_pair[MAX_PAIRS][MAX_ON_PAIR], on_count[MAX_PAIRS];
static unsigned char current[MAX_PACK], optimum[MAX_PACK];
static int best;
static uint64_t nodes;

static void solve(uint64_t used, uint64_t dead, int depth)
{
    ++nodes;
    if (depth > best) {
        best = depth;
        memcpy(optimum, current, (size_t)depth);
    }
    uint64_t blocked = used | dead;
    int changed = 1;
    while (changed) {
        changed = 0;
        for (int p = 0; p < pair_count; ++p) {
            const uint64_t bit = UINT64_C(1) << p;
            if (blocked & bit) continue;
            int possible = 0;
            for (int j = 0; j < on_count[p]; ++j)
                if ((tri[on_pair[p][j]].mask & blocked) == 0) {
                    possible = 1;
                    break;
                }
            if (!possible) {
                blocked |= bit;
                dead |= bit;
                changed = 1;
            }
        }
    }
    const int live = pair_count - __builtin_popcountll(blocked);
    if (depth + live / 3 <= best) return;

    int pivot = -1, minimum = MAX_ON_PAIR + 1;
    for (int p = 0; p < pair_count; ++p) {
        if (blocked & (UINT64_C(1) << p)) continue;
        int options = 0;
        for (int j = 0; j < on_count[p]; ++j)
            if ((tri[on_pair[p][j]].mask & blocked) == 0) ++options;
        if (options < minimum) {
            minimum = options;
            pivot = p;
            if (options == 1) break;
        }
    }
    if (pivot < 0) return;
    for (int j = 0; j < on_count[pivot]; ++j) {
        const int t = on_pair[pivot][j];
        if (tri[t].mask & blocked) continue;
        current[depth] = (unsigned char)t;
        solve(used | tri[t].mask, dead, depth + 1);
    }
    solve(used, dead | (UINT64_C(1) << pivot), depth);
}

static int prepare(const char *bits)
{
    memset(on_count, 0, sizeof(on_count));
    for (int i = 0; i < n; ++i)
        for (int j = i + 1; j < n; ++j) {
            const int forward = bits[pair_id[i][j]] == '1';
            arc[i][j] = (unsigned char)forward;
            arc[j][i] = (unsigned char)!forward;
        }
    tri_count = 0;
    for (int a = 0; a < n; ++a)
        for (int b = a + 1; b < n; ++b)
            for (int c = b + 1; c < n; ++c) {
                const int cyclic = (arc[a][b] && arc[b][c] && arc[c][a]) ||
                                   (arc[b][a] && arc[c][b] && arc[a][c]);
                if (cyclic) continue;
                Tri *t = &tri[tri_count];
                t->a = (unsigned char)a;
                t->b = (unsigned char)b;
                t->c = (unsigned char)c;
                const int ps[3] = {pair_id[a][b], pair_id[a][c], pair_id[b][c]};
                t->mask = (UINT64_C(1) << ps[0]) |
                          (UINT64_C(1) << ps[1]) |
                          (UINT64_C(1) << ps[2]);
                for (int z = 0; z < 3; ++z)
                    on_pair[ps[z]][on_count[ps[z]]++] = (unsigned char)tri_count;
                ++tri_count;
            }
    return 1;
}

int main(int argc, char **argv)
{
    if (argc != 2) {
        fprintf(stderr, "usage: %s N < tournaments.bits\n", argv[0]);
        return 2;
    }
    n = atoi(argv[1]);
    if (n < 3 || n > MAX_N) return 2;
    pair_count = n * (n - 1) / 2;
    int p = 0;
    for (int i = 0; i < n; ++i)
        for (int j = i + 1; j < n; ++j)
            pair_id[i][j] = p++;

    char line[128];
    uint64_t number = 0;
    while (fgets(line, sizeof(line), stdin)) {
        size_t length = strcspn(line, "\r\n");
        line[length] = '\0';
        if ((int)length != pair_count || strspn(line, "01") != length) {
            fprintf(stderr, "malformed line=%" PRIu64 "\n", number + 1);
            return 2;
        }
        prepare(line);
        best = -1;
        nodes = 0;
        solve(0, 0, 0);
        ++number;
        printf("MAX line=%" PRIu64 " bits=%s value=%d nodes=%" PRIu64 " witness=",
               number, line, best, nodes);
        for (int i = 0; i < best; ++i) {
            const Tri *t = &tri[optimum[i]];
            printf("%u,%u,%u%s", t->a, t->b, t->c, i + 1 == best ? "" : ";");
        }
        putchar('\n');
    }
    return ferror(stdin) ? 2 : 0;
}
