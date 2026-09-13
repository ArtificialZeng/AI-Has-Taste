/*
 * Builder scanner for arc-disjoint transitive triples in tournaments.
 *
 * Input: one strict gentourng ASCII tournament per line.
 * Output: a single fail-closed summary, or the first below-target tournament.
 *
 * Exact search invariant.  A state consists of used pair-indices, permanently
 * dead pair-indices, and a partial packing.  For a chosen live pair e, every
 * extension either covers e with one currently available transitive triple or
 * leaves e dead.  These branches are exhaustive.  The only numeric bound is
 * the integer fact that r additional triples require 3r live pairs.
 *
 * This is discovery/Builder code.  certifier_scan.c is intentionally an
 * independently written search with a different recursion.
 */

#include <CommonCrypto/CommonDigest.h>
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_N 11
#define MAX_PAIRS 55
#define MAX_TRIS 165
#define MAX_ON_PAIR 9
#define MAX_PACK 18

typedef struct {
    uint64_t mask;
    unsigned char a, b, c;
} Triangle;

typedef struct {
    int n;
    int pairs;
    int target;
    int pair_index[MAX_N][MAX_N];
    unsigned char beats[MAX_N][MAX_N];
    Triangle tri[MAX_TRIS];
    int ntri;
    unsigned char on_pair[MAX_PAIRS][MAX_ON_PAIR];
    unsigned char non_pair[MAX_PAIRS];
    unsigned char current[MAX_PACK];
    unsigned char witness[MAX_PACK];
    uint64_t nodes;
} Search;

static int search_target(Search *s, uint64_t used, uint64_t dead, int depth)
{
    s->nodes++;
    if (depth >= s->target) {
        memcpy(s->witness, s->current, (size_t)s->target);
        return 1;
    }

    uint64_t blocked = used | dead;
    int changed = 1;
    while (changed) {
        changed = 0;
        for (int p = 0; p < s->pairs; ++p) {
            const uint64_t bit = UINT64_C(1) << p;
            if (blocked & bit) continue;
            int available = 0;
            for (int q = 0; q < s->non_pair[p]; ++q) {
                const int t = s->on_pair[p][q];
                if ((s->tri[t].mask & blocked) == 0) {
                    available = 1;
                    break;
                }
            }
            if (!available) {
                dead |= bit;
                blocked |= bit;
                changed = 1;
            }
        }
    }

    const int live = s->pairs - __builtin_popcountll(blocked);
    if (depth + live / 3 < s->target) return 0;

    int chosen_pair = -1;
    int chosen_count = MAX_ON_PAIR + 1;
    for (int p = 0; p < s->pairs; ++p) {
        if (blocked & (UINT64_C(1) << p)) continue;
        int count = 0;
        for (int q = 0; q < s->non_pair[p]; ++q) {
            const int t = s->on_pair[p][q];
            if ((s->tri[t].mask & blocked) == 0) ++count;
        }
        if (count < chosen_count) {
            chosen_count = count;
            chosen_pair = p;
            if (count == 1) break;
        }
    }
    if (chosen_pair < 0) return 0;

    for (int q = 0; q < s->non_pair[chosen_pair]; ++q) {
        const int t = s->on_pair[chosen_pair][q];
        if (s->tri[t].mask & blocked) continue;
        s->current[depth] = (unsigned char)t;
        if (search_target(s, used | s->tri[t].mask, dead, depth + 1)) return 1;
    }
    return search_target(s, used, dead | (UINT64_C(1) << chosen_pair), depth);
}

static int prepare(Search *s, const char *bits)
{
    for (int i = 0; i < s->n; ++i) {
        s->beats[i][i] = 0;
        for (int j = i + 1; j < s->n; ++j) {
            const int p = s->pair_index[i][j];
            const unsigned char forward = (unsigned char)(bits[p] == '1');
            s->beats[i][j] = forward;
            s->beats[j][i] = (unsigned char)!forward;
        }
    }

    memset(s->non_pair, 0, sizeof(s->non_pair));
    s->ntri = 0;
    for (int a = 0; a < s->n; ++a) {
        for (int b = a + 1; b < s->n; ++b) {
            for (int c = b + 1; c < s->n; ++c) {
                const int cyclic =
                    (s->beats[a][b] && s->beats[b][c] && s->beats[c][a]) ||
                    (s->beats[b][a] && s->beats[c][b] && s->beats[a][c]);
                if (cyclic) continue;
                if (s->ntri >= MAX_TRIS) return 0;
                Triangle *t = &s->tri[s->ntri];
                t->a = (unsigned char)a;
                t->b = (unsigned char)b;
                t->c = (unsigned char)c;
                const int p0 = s->pair_index[a][b];
                const int p1 = s->pair_index[a][c];
                const int p2 = s->pair_index[b][c];
                t->mask = (UINT64_C(1) << p0) |
                          (UINT64_C(1) << p1) |
                          (UINT64_C(1) << p2);
                const int ps[3] = {p0, p1, p2};
                for (int z = 0; z < 3; ++z) {
                    if (s->non_pair[ps[z]] >= MAX_ON_PAIR) return 0;
                    s->on_pair[ps[z]][s->non_pair[ps[z]]++] =
                        (unsigned char)s->ntri;
                }
                ++s->ntri;
            }
        }
    }
    return 1;
}

static int witness_ok(const Search *s)
{
    uint64_t used = 0;
    for (int i = 0; i < s->target; ++i) {
        const Triangle *t = &s->tri[s->witness[i]];
        if (used & t->mask) return 0;
        used |= t->mask;
        const int a = t->a, b = t->b, c = t->c;
        const int cyclic =
            (s->beats[a][b] && s->beats[b][c] && s->beats[c][a]) ||
            (s->beats[b][a] && s->beats[c][b] && s->beats[a][c]);
        if (cyclic) return 0;
    }
    return 1;
}

static void print_sha256(const unsigned char digest[CC_SHA256_DIGEST_LENGTH])
{
    for (int i = 0; i < CC_SHA256_DIGEST_LENGTH; ++i) printf("%02x", digest[i]);
}

int main(int argc, char **argv)
{
    if (argc != 3) {
        fprintf(stderr, "usage: %s N TARGET\n", argv[0]);
        return 2;
    }
    Search s;
    memset(&s, 0, sizeof(s));
    s.n = atoi(argv[1]);
    s.target = atoi(argv[2]);
    if (s.n < 3 || s.n > MAX_N || s.target < 0 || s.target > MAX_PACK) {
        fprintf(stderr, "invalid N or TARGET\n");
        return 2;
    }
    s.pairs = s.n * (s.n - 1) / 2;
    int p = 0;
    for (int i = 0; i < s.n; ++i)
        for (int j = i + 1; j < s.n; ++j)
            s.pair_index[i][j] = p++;

    CC_SHA256_CTX hash;
    CC_SHA256_Init(&hash);
    char *line = NULL;
    size_t capacity = 0;
    ssize_t length;
    uint64_t count = 0, total_nodes = 0, maximum_nodes = 0;
    while ((length = getline(&line, &capacity, stdin)) >= 0) {
        if (length > 0 && line[length - 1] == '\n') --length;
        if (length > 0 && line[length - 1] == '\r') --length;
        if (length != s.pairs) {
            fprintf(stderr, "MALFORMED line=%" PRIu64 " length=%zd expected=%d\n",
                    count + 1, length, s.pairs);
            free(line);
            return 2;
        }
        for (int i = 0; i < s.pairs; ++i) {
            if (line[i] != '0' && line[i] != '1') {
                fprintf(stderr, "MALFORMED line=%" PRIu64 " nonbinary-position=%d\n",
                        count + 1, i);
                free(line);
                return 2;
            }
        }
        line[length] = '\0';
        CC_SHA256_Update(&hash, line, (CC_LONG)length);
        CC_SHA256_Update(&hash, "\n", 1);
        if (!prepare(&s, line)) {
            fprintf(stderr, "INTERNAL prepare failure at line=%" PRIu64 "\n", count + 1);
            free(line);
            return 2;
        }
        s.nodes = 0;
        const int found = search_target(&s, 0, 0, 0);
        total_nodes += s.nodes;
        if (s.nodes > maximum_nodes) maximum_nodes = s.nodes;
        ++count;
        if (!found) {
            printf("BELOW_TARGET n=%d target=%d line=%" PRIu64 " bits=%s nodes=%" PRIu64 "\n",
                   s.n, s.target, count, line, s.nodes);
            free(line);
            return 1;
        }
        if (!witness_ok(&s)) {
            fprintf(stderr, "INTERNAL witness rejection at line=%" PRIu64 "\n", count);
            free(line);
            return 2;
        }
    }
    if (ferror(stdin)) {
        fprintf(stderr, "input read error\n");
        free(line);
        return 2;
    }
    free(line);
    unsigned char digest[CC_SHA256_DIGEST_LENGTH];
    CC_SHA256_Final(digest, &hash);
    printf("BUILDER_OK n=%d target=%d count=%" PRIu64 " sha256=", s.n, s.target, count);
    print_sha256(digest);
    printf(" nodes=%" PRIu64 " max_nodes=%" PRIu64 "\n", total_nodes, maximum_nodes);
    return 0;
}
