/*
 * Independent Certifier for the 11-vertex TT3-packing sweep.
 *
 * This file does not import Builder output or code.  It independently parses
 * each tournament, declares a triple transitive by its internal outdegree
 * multiset, builds the compatibility graph of triples, and asks whether that
 * graph has a clique of the target size.  A clique is exactly a family of
 * pairwise pair-disjoint triples.  The recursion branches on including or
 * excluding the first remaining compatibility-graph vertex; its sole pruning
 * rule is the exact cardinality upper bound on remaining candidates.
 */

#include <CommonCrypto/CommonDigest.h>
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_N 11
#define MAX_TRIS 165
#define WORDS 3
#define MAX_PACK 18

typedef struct {
    uint64_t pair_mask;
    unsigned char vertex[3];
    int conflicts;
} Triple;

typedef struct {
    int n;
    int target;
    int pair_count;
    Triple triples[MAX_TRIS];
    int triple_count;
    uint64_t later_compatible[MAX_TRIS][WORDS];
    unsigned char stack[MAX_PACK];
    unsigned char answer[MAX_PACK];
    uint64_t nodes;
} Instance;

static int pair_number(int n, int x, int y)
{
    if (x > y) {
        const int z = x;
        x = y;
        y = z;
    }
    return x * (2 * n - x - 1) / 2 + (y - x - 1);
}

static int arc_forward(const char *bits, int n, int from, int to)
{
    const int p = pair_number(n, from, to);
    return from < to ? bits[p] == '1' : bits[p] == '0';
}

static int triple_is_transitive(const char *bits, int n, int a, int b, int c)
{
    int wins_a = arc_forward(bits, n, a, b) + arc_forward(bits, n, a, c);
    int wins_b = arc_forward(bits, n, b, a) + arc_forward(bits, n, b, c);
    int wins_c = arc_forward(bits, n, c, a) + arc_forward(bits, n, c, b);
    return wins_a == 2 || wins_b == 2 || wins_c == 2;
}

static int compare_triples(const void *left, const void *right)
{
    const Triple *a = (const Triple *)left;
    const Triple *b = (const Triple *)right;
    if (a->conflicts != b->conflicts) return a->conflicts - b->conflicts;
    if (a->pair_mask < b->pair_mask) return -1;
    if (a->pair_mask > b->pair_mask) return 1;
    return 0;
}

static int population(const uint64_t set[WORDS])
{
    return __builtin_popcountll(set[0]) +
           __builtin_popcountll(set[1]) +
           __builtin_popcountll(set[2]);
}

static int first_member(const uint64_t set[WORDS])
{
    for (int w = 0; w < WORDS; ++w) {
        if (set[w]) return 64 * w + __builtin_ctzll(set[w]);
    }
    return -1;
}

static void remove_member(uint64_t set[WORDS], int member)
{
    set[member / 64] &= ~(UINT64_C(1) << (member % 64));
}

static int find_clique(Instance *in, uint64_t candidates[WORDS], int depth)
{
    in->nodes++;
    if (depth >= in->target) {
        memcpy(in->answer, in->stack, (size_t)in->target);
        return 1;
    }
    while (population(candidates) >= in->target - depth) {
        const int chosen = first_member(candidates);
        if (chosen < 0 || chosen >= in->triple_count) return 0;
        in->stack[depth] = (unsigned char)chosen;
        uint64_t next[WORDS];
        for (int w = 0; w < WORDS; ++w)
            next[w] = candidates[w] & in->later_compatible[chosen][w];
        if (find_clique(in, next, depth + 1)) return 1;
        remove_member(candidates, chosen);
    }
    return 0;
}

static int build_instance(Instance *in, const char *bits)
{
    unsigned char on_pair[55][9];
    unsigned char on_count[55] = {0};
    in->triple_count = 0;
    for (int a = 0; a < in->n; ++a) {
        for (int b = a + 1; b < in->n; ++b) {
            for (int c = b + 1; c < in->n; ++c) {
                if (!triple_is_transitive(bits, in->n, a, b, c)) continue;
                Triple *t = &in->triples[in->triple_count++];
                t->vertex[0] = (unsigned char)a;
                t->vertex[1] = (unsigned char)b;
                t->vertex[2] = (unsigned char)c;
                t->pair_mask = (UINT64_C(1) << pair_number(in->n, a, b)) |
                               (UINT64_C(1) << pair_number(in->n, a, c)) |
                               (UINT64_C(1) << pair_number(in->n, b, c));
                t->conflicts = 0;
                uint64_t pairs = t->pair_mask;
                while (pairs) {
                    const int p = __builtin_ctzll(pairs);
                    pairs &= pairs - 1;
                    if (on_count[p] >= 9) return 0;
                    on_pair[p][on_count[p]++] = (unsigned char)(in->triple_count - 1);
                }
            }
        }
    }
    if (in->triple_count > MAX_TRIS) return 0;
    for (int p = 0; p < in->pair_count; ++p)
        for (int i = 0; i < on_count[p]; ++i)
            for (int j = i + 1; j < on_count[p]; ++j) {
                ++in->triples[on_pair[p][i]].conflicts;
                ++in->triples[on_pair[p][j]].conflicts;
            }
    qsort(in->triples, (size_t)in->triple_count, sizeof(Triple), compare_triples);

    memset(in->later_compatible, 0, sizeof(in->later_compatible));
    for (int i = 0; i < in->triple_count; ++i)
        for (int j = i + 1; j < in->triple_count; ++j)
            in->later_compatible[i][j / 64] |= UINT64_C(1) << (j % 64);
    memset(on_count, 0, sizeof(on_count));
    for (int i = 0; i < in->triple_count; ++i) {
        uint64_t pairs = in->triples[i].pair_mask;
        while (pairs) {
            const int p = __builtin_ctzll(pairs);
            pairs &= pairs - 1;
            on_pair[p][on_count[p]++] = (unsigned char)i;
        }
    }
    for (int p = 0; p < in->pair_count; ++p)
        for (int a = 0; a < on_count[p]; ++a)
            for (int b = a + 1; b < on_count[p]; ++b) {
                const int i = on_pair[p][a], j = on_pair[p][b];
                in->later_compatible[i][j / 64] &= ~(UINT64_C(1) << (j % 64));
            }
    return 1;
}

static int answer_is_valid(const Instance *in, const char *bits)
{
    uint64_t used = 0;
    for (int k = 0; k < in->target; ++k) {
        const int index = in->answer[k];
        if (index < 0 || index >= in->triple_count) return 0;
        const Triple *t = &in->triples[index];
        if (used & t->pair_mask) return 0;
        used |= t->pair_mask;
        if (!triple_is_transitive(bits, in->n,
                                  t->vertex[0], t->vertex[1], t->vertex[2]))
            return 0;
    }
    return 1;
}

static void print_digest(const unsigned char digest[CC_SHA256_DIGEST_LENGTH])
{
    for (int i = 0; i < CC_SHA256_DIGEST_LENGTH; ++i) printf("%02x", digest[i]);
}

int main(int argc, char **argv)
{
    if (argc != 3) {
        fprintf(stderr, "usage: %s N TARGET\n", argv[0]);
        return 2;
    }
    Instance in;
    memset(&in, 0, sizeof(in));
    in.n = atoi(argv[1]);
    in.target = atoi(argv[2]);
    if (in.n < 3 || in.n > MAX_N || in.target < 0 || in.target > MAX_PACK) {
        fprintf(stderr, "invalid N or TARGET\n");
        return 2;
    }
    in.pair_count = in.n * (in.n - 1) / 2;

    CC_SHA256_CTX hash;
    CC_SHA256_Init(&hash);
    char *line = NULL;
    size_t capacity = 0;
    ssize_t length;
    uint64_t count = 0, total_nodes = 0, maximum_nodes = 0;
    while ((length = getline(&line, &capacity, stdin)) >= 0) {
        if (length > 0 && line[length - 1] == '\n') --length;
        if (length > 0 && line[length - 1] == '\r') --length;
        if (length != in.pair_count) {
            fprintf(stderr, "MALFORMED line=%" PRIu64 " length=%zd expected=%d\n",
                    count + 1, length, in.pair_count);
            free(line);
            return 2;
        }
        for (int i = 0; i < in.pair_count; ++i) {
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
        if (!build_instance(&in, line)) {
            fprintf(stderr, "INTERNAL build failure line=%" PRIu64 "\n", count + 1);
            free(line);
            return 2;
        }
        uint64_t candidates[WORDS] = {0, 0, 0};
        for (int i = 0; i < in.triple_count; ++i)
            candidates[i / 64] |= UINT64_C(1) << (i % 64);
        in.nodes = 0;
        const int found = find_clique(&in, candidates, 0);
        total_nodes += in.nodes;
        if (in.nodes > maximum_nodes) maximum_nodes = in.nodes;
        ++count;
        if (!found) {
            printf("CERTIFIER_BELOW_TARGET n=%d target=%d line=%" PRIu64
                   " bits=%s nodes=%" PRIu64 "\n",
                   in.n, in.target, count, line, in.nodes);
            free(line);
            return 1;
        }
        if (!answer_is_valid(&in, line)) {
            fprintf(stderr, "INTERNAL answer rejection line=%" PRIu64 "\n", count);
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
    printf("CERTIFIER_OK n=%d target=%d count=%" PRIu64 " sha256=",
           in.n, in.target, count);
    print_digest(digest);
    printf(" nodes=%" PRIu64 " max_nodes=%" PRIu64 "\n", total_nodes, maximum_nodes);
    return 0;
}
