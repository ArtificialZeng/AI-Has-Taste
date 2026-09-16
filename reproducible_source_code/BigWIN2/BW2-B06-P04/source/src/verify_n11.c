/*
 * Independent, fail-closed verifier for nac11_four_way.cert.
 *
 * This file shares no code with discover_n11.c.  In particular, NAC witnesses
 * are checked by bitset transitive closure rather than the discovery program's
 * disjoint-set routine.  Every input graph is checked for (2,3)-tightness by
 * direct enumeration of every relevant vertex subset.
 */

#include <ctype.h>
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum { N = 11, PAIRS = 55, EXPECTED = 2039273 };

typedef struct {
    uint16_t nb[N];
    int eu[PAIRS], ev[PAIRS];
    uint64_t eb[PAIRS];
    int m;
} Graph;

static uint64_t subset_edges[1815];
static unsigned char subset_bound[1815];
static int subset_tests = 0;

static int read_integer_amid_text(FILE *f, uint64_t *value) {
    int ch;
    uint64_t z = 0;
    while ((ch = fgetc(f)) != EOF && !isdigit((unsigned char)ch)) { }
    if (ch == EOF) return 0;
    do {
        z = 10u * z + (unsigned)(ch - '0');
        ch = fgetc(f);
    } while (ch != EOF && isdigit((unsigned char)ch));
    *value = z;
    return 1;
}

static void decode(uint64_t code, Graph *h) {
    int x, y, p = PAIRS - 1;
    memset(h, 0, sizeof(*h));
    for (x = 0; x < N; ++x) {
        for (y = x + 1; y < N; ++y, --p) {
            uint64_t q = UINT64_C(1) << p;
            if (code & q) {
                h->nb[x] |= (uint16_t)(1u << y);
                h->nb[y] |= (uint16_t)(1u << x);
                h->eu[h->m] = x;
                h->ev[h->m] = y;
                h->eb[h->m] = q;
                ++h->m;
            }
        }
    }
}

static void prepare_laman_subsets(void) {
    int s;
    for (s = 0; s < (1 << N); ++s) {
        int k = __builtin_popcount((unsigned)s);
        int x, y, p = PAIRS - 1;
        uint64_t q = 0;
        if (k < 4 || k > 10) continue; /* sizes 2 and 3 are automatic in a simple graph */
        for (x = 0; x < N; ++x)
            for (y = x + 1; y < N; ++y, --p)
                if ((s & (1 << x)) && (s & (1 << y))) q |= UINT64_C(1) << p;
        subset_edges[subset_tests] = q;
        subset_bound[subset_tests] = (unsigned char)(2 * k - 3);
        ++subset_tests;
    }
    if (subset_tests != 1815) {
        fprintf(stderr, "internal subset table error: %d\n", subset_tests);
        exit(10);
    }
}

static int is_laman(uint64_t code) {
    int i;
    if (__builtin_popcountll(code) != 2 * N - 3) return 0;
    if (code >> PAIRS) return 0;
    for (i = 0; i < subset_tests; ++i)
        if (__builtin_popcountll(code & subset_edges[i]) > subset_bound[i]) return 0;
    return 1;
}

/* Exact reachability closure for one colour. */
static void colour_closure(const Graph *h, uint64_t selected, uint16_t reach[N]) {
    int i, j, k;
    for (i = 0; i < N; ++i) reach[i] = (uint16_t)(1u << i);
    for (i = 0; i < h->m; ++i) if (selected & h->eb[i]) {
        reach[h->eu[i]] |= (uint16_t)(1u << h->ev[i]);
        reach[h->ev[i]] |= (uint16_t)(1u << h->eu[i]);
    }
    for (k = 0; k < N; ++k)
        for (i = 0; i < N; ++i)
            if (reach[i] & (1u << k)) reach[i] |= reach[k];
    /* Defensive symmetry check catches malformed internal state. */
    for (i = 0; i < N; ++i)
        for (j = 0; j < N; ++j)
            if (!!(reach[i] & (1u << j)) != !!(reach[j] & (1u << i))) exit(11);
}

static int valid_nac_witness(const Graph *h, uint64_t graph_code, uint64_t red) {
    uint64_t blue;
    uint16_t rr[N], rb[N];
    int e;
    if (red & ~graph_code) return 0;
    blue = graph_code ^ red;
    if (red == 0 || blue == 0) return 0;
    colour_closure(h, red, rr);
    colour_closure(h, blue, rb);
    for (e = 0; e < h->m; ++e) {
        int u = h->eu[e], v = h->ev[e];
        if (red & h->eb[e]) {
            if (rb[u] & (1u << v)) return 0;
        } else {
            if (rr[u] & (1u << v)) return 0;
        }
    }
    return 1;
}

static int triangles(const Graph *h) {
    int a, b, count = 0;
    for (a = 0; a < N; ++a)
        for (b = a + 1; b < N; ++b)
            if (h->nb[a] & (1u << b))
                count += __builtin_popcount((unsigned)(h->nb[a] & h->nb[b] & (uint16_t)~((1u << (b + 1)) - 1u)));
    return count;
}

/* Uses the highest-index available degree-two vertex, intentionally unlike
 * the discovery program. */
static int reverse_h1(const Graph *h, int *open) {
    uint16_t live = (1u << N) - 1u;
    int left = N, opens = 0;
    while (left > 2) {
        int v, chosen = -1;
        for (v = N - 1; v >= 0; --v)
            if ((live & (1u << v)) && __builtin_popcount((unsigned)(h->nb[v] & live)) == 2) {
                chosen = v;
                break;
            }
        if (chosen < 0) return 0;
        {
            uint16_t z = h->nb[chosen] & live;
            int u = __builtin_ctz((unsigned)z);
            int w;
            z &= (uint16_t)(z - 1u);
            w = __builtin_ctz((unsigned)z);
            if (!(h->nb[u] & (1u << w))) ++opens;
        }
        live &= (uint16_t)~(1u << chosen);
        --left;
    }
    {
        int u = __builtin_ctz((unsigned)live);
        uint16_t rest = live & (uint16_t)(live - 1u);
        int v = __builtin_ctz((unsigned)rest);
        if (!(h->nb[u] & (1u << v))) return 0;
    }
    *open = opens;
    return 1;
}

static int triangular_prisms(const Graph *h) {
    int s, answer = 0;
    for (s = 0; s < (1 << N); ++s) {
        int x, cubic = 1, has_triangle = 0;
        if (__builtin_popcount((unsigned)s) != 6) continue;
        for (x = 0; x < N; ++x) if (s & (1 << x))
            if (__builtin_popcount((unsigned)(h->nb[x] & s)) != 3) { cubic = 0; break; }
        if (!cubic) continue;
        for (x = 0; x < N && !has_triangle; ++x) if (s & (1 << x)) {
            uint16_t z = h->nb[x] & (uint16_t)s;
            int y;
            for (y = x + 1; y < N; ++y)
                if ((z & (1u << y)) && (h->nb[y] & z)) { has_triangle = 1; break; }
        }
        if (has_triangle) ++answer; /* the other cubic graph on six vertices is K_3,3 */
    }
    return answer;
}

static int stable_cut_exists(const Graph *h) {
    int cut;
    uint16_t universe = (1u << N) - 1u;
    for (cut = 0; cut < (1 << N); ++cut) {
        uint16_t outside = universe & (uint16_t)~cut;
        uint16_t reached, wave;
        int x, stable = 1;
        if (__builtin_popcount((unsigned)outside) < 2) continue;
        for (x = 0; x < N; ++x) if (cut & (1 << x))
            if (h->nb[x] & cut) { stable = 0; break; }
        if (!stable) continue;
        reached = wave = (uint16_t)(1u << __builtin_ctz((unsigned)outside));
        while (wave) {
            uint16_t next = 0;
            for (x = 0; x < N; ++x) if (wave & (1u << x)) next |= h->nb[x];
            next &= outside;
            next &= (uint16_t)~reached;
            reached |= next;
            wave = next;
        }
        if (reached != outside) return 1;
    }
    return 0;
}

static uint64_t mix64(uint64_t x) {
    x ^= x >> 30; x *= UINT64_C(0xbf58476d1ce4e5b9);
    x ^= x >> 27; x *= UINT64_C(0x94d049bb133111eb);
    return x ^ (x >> 31);
}

static int insert_unique(uint64_t *table, size_t cap, uint64_t x) {
    size_t p = (size_t)(mix64(x) & (cap - 1));
    while (table[p] && table[p] != x) p = (p + 1) & (cap - 1);
    if (table[p] == x) return 0;
    table[p] = x;
    return 1;
}

static int fail_at(uint64_t row, const char *why) {
    fprintf(stderr, "VERIFY_FAIL row=%" PRIu64 " reason=%s\n", row, why);
    return 1;
}

int main(int argc, char **argv) {
    FILE *data, *cert;
    char magic[32];
    int version, order;
    uint64_t advertised, row;
    uint64_t counts[256] = {0};
    const size_t hcap = (size_t)1u << 22;
    uint64_t *seen;
    if (argc != 3) {
        fprintf(stderr, "usage: %s LamanGraphs11.txt nac11_four_way.cert\n", argv[0]);
        return 2;
    }
    data = fopen(argv[1], "rb");
    cert = fopen(argv[2], "rb");
    if (!data || !cert) { perror("open"); return 2; }
    if (fscanf(cert, "%31s %d %d %" SCNu64, magic, &version, &order, &advertised) != 4)
        return fail_at(0, "malformed header");
    if (strcmp(magic, "NAC11CERT") || version != 1 || order != N || advertised != EXPECTED)
        return fail_at(0, "wrong header values");
    seen = (uint64_t *)calloc(hcap, sizeof(uint64_t));
    if (!seen) { perror("calloc"); return 2; }
    prepare_laman_subsets();

    for (row = 0; row < advertised; ++row) {
        uint64_t source_g, cert_g, r1 = 0, r2 = 0;
        char tag;
        Graph h;
        int open = -1;
        if (!read_integer_amid_text(data, &source_g)) return fail_at(row, "dataset ended early");
        if (fscanf(cert, " %c %" SCNu64, &tag, &cert_g) != 2) return fail_at(row, "certificate ended early");
        if (source_g != cert_g) return fail_at(row, "dataset/certificate graph mismatch");
        if (!insert_unique(seen, hcap, source_g)) return fail_at(row, "duplicate graph encoding");
        if (!is_laman(source_g)) return fail_at(row, "graph is not Laman");
        decode(source_g, &h);
        if (h.m != 19) return fail_at(row, "decoded edge count is not 19");
        if (tag == '2') {
            if (fscanf(cert, " %" SCNu64 " %" SCNu64, &r1, &r2) != 2)
                return fail_at(row, "missing NAC masks");
            if (!valid_nac_witness(&h, source_g, r1) || !valid_nac_witness(&h, source_g, r2))
                return fail_at(row, "invalid NAC witness");
            if (r1 == r2 || r1 == (source_g ^ r2))
                return fail_at(row, "NAC witnesses are colour-swap equivalent");
        } else if (tag == 'T') {
            if (!reverse_h1(&h, &open) || open != 0 || triangles(&h) != N - 2)
                return fail_at(row, "invalid 2-tree certificate");
        } else if (tag == 'B') {
            if (!reverse_h1(&h, &open) || open != 1 || triangles(&h) != N - 3)
                return fail_at(row, "invalid one-open-step certificate");
        } else if (tag == 'A') {
            if (triangular_prisms(&h) != 1 || stable_cut_exists(&h))
                return fail_at(row, "invalid G_sc/one-prism certificate");
        } else {
            return fail_at(row, "unknown certificate tag");
        }
        ++counts[(unsigned char)tag];
        if (((row + 1) % 250000u) == 0)
            fprintf(stderr, "verified=%" PRIu64 "\n", row + 1);
    }
    {
        uint64_t extra;
        char t;
        if (read_integer_amid_text(data, &extra)) return fail_at(advertised, "dataset has extra record");
        if (fscanf(cert, " %c", &t) == 1) return fail_at(advertised, "certificate has trailing token");
    }
    free(seen);
    fclose(data);
    fclose(cert);
    printf("VERIFIED exact_rows=%d two=%" PRIu64 " A=%" PRIu64
           " B=%" PRIu64 " T=%" PRIu64 " subset_tests_per_graph=%d\n",
           EXPECTED, counts['2'], counts['A'], counts['B'], counts['T'], subset_tests);
    return 0;
}
