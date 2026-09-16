/*
 * Discovery program for the locked n=11 unique-NAC proposition.
 *
 * This program is deliberately not the release verifier.  It searches only
 * until it has two colour-swap inequivalent NAC-colourings.  Residual graphs
 * are classified structurally.  The output is a four-way certificate:
 *
 *   2 g r1 r2   two literal red-edge masks (blue is g xor ri)
 *   A g         no stable cut and exactly one triangular prism
 *   B g         a 0-extension graph with exactly one open step
 *   T g         a 2-tree
 *
 * Graphs and colour masks use the 55-bit upper-triangular encoding described
 * in Zenodo record 1245517.  No floating-point arithmetic is used.
 */

#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NV 11
#define NE 55
#define LAMAN_EDGES 19
#define MAX_CLASSES 19

typedef struct {
    int u[LAMAN_EDGES], v[LAMAN_EDGES];
    uint64_t bit[LAMAN_EDGES];
    int edge_index[NV][NV];
    int cls_of_edge[LAMAN_EDGES];
    int class_count;
    uint64_t class_mask[MAX_CLASSES];
    int class_size[MAX_CLASSES];
    uint64_t graph_mask;
    uint64_t solutions[2];
    int solution_count;
    uint64_t nodes;
} Search;

static int next_uint64(FILE *f, uint64_t *out) {
    int c;
    uint64_t x = 0;
    do {
        c = fgetc(f);
        if (c == EOF) return 0;
    } while (c < '0' || c > '9');
    do {
        x = x * 10u + (uint64_t)(c - '0');
        c = fgetc(f);
    } while (c >= '0' && c <= '9');
    *out = x;
    return 1;
}

static int dsu_find(int p[NV], int x) {
    while (p[x] != x) {
        p[x] = p[p[x]];
        x = p[x];
    }
    return x;
}

static void dsu_union(int p[NV], int a, int b) {
    a = dsu_find(p, a);
    b = dsu_find(p, b);
    if (a != b) p[b] = a;
}

static int edge_colouring_is_nac(const Search *s, uint64_t red) {
    uint64_t blue = s->graph_mask ^ red;
    int pr[NV], pb[NV];
    int i;
    if (red == 0 || blue == 0 || (red & ~s->graph_mask) != 0) return 0;
    for (i = 0; i < NV; ++i) pr[i] = pb[i] = i;
    for (i = 0; i < LAMAN_EDGES; ++i) {
        if (red & s->bit[i]) dsu_union(pr, s->u[i], s->v[i]);
        else dsu_union(pb, s->u[i], s->v[i]);
    }
    for (i = 0; i < LAMAN_EDGES; ++i) {
        if (red & s->bit[i]) {
            if (dsu_find(pb, s->u[i]) == dsu_find(pb, s->v[i])) return 0;
        } else {
            if (dsu_find(pr, s->u[i]) == dsu_find(pr, s->v[i])) return 0;
        }
    }
    return 1;
}

static int edge_root(int p[LAMAN_EDGES], int x) {
    while (p[x] != x) {
        p[x] = p[p[x]];
        x = p[x];
    }
    return x;
}

static void edge_union(int p[LAMAN_EDGES], int a, int b) {
    a = edge_root(p, a);
    b = edge_root(p, b);
    if (a != b) p[b] = a;
}

static int initialize_search(Search *s, uint64_t g) {
    int pos = NE - 1, m = 0, a, b, i, j, k;
    int ep[LAMAN_EDGES], root_to_class[LAMAN_EDGES];
    memset(s, 0, sizeof(*s));
    s->graph_mask = g;
    for (i = 0; i < NV; ++i)
        for (j = 0; j < NV; ++j) s->edge_index[i][j] = -1;
    for (a = 0; a < NV; ++a) {
        for (b = a + 1; b < NV; ++b, --pos) {
            uint64_t bit = UINT64_C(1) << pos;
            if (g & bit) {
                if (m >= LAMAN_EDGES) return 0;
                s->u[m] = a;
                s->v[m] = b;
                s->bit[m] = bit;
                s->edge_index[a][b] = s->edge_index[b][a] = m;
                ++m;
            }
        }
    }
    if (m != LAMAN_EDGES) return 0;

    for (i = 0; i < LAMAN_EDGES; ++i) ep[i] = i;
    /* Every triangle is monochromatic in every NAC-colouring. */
    for (i = 0; i < NV; ++i) {
        for (j = i + 1; j < NV; ++j) {
            int ij = s->edge_index[i][j];
            if (ij < 0) continue;
            for (k = j + 1; k < NV; ++k) {
                int ik = s->edge_index[i][k];
                int jk = s->edge_index[j][k];
                if (ik >= 0 && jk >= 0) {
                    edge_union(ep, ij, ik);
                    edge_union(ep, ij, jk);
                }
            }
        }
    }
    for (i = 0; i < LAMAN_EDGES; ++i) root_to_class[i] = -1;
    for (i = 0; i < LAMAN_EDGES; ++i) {
        int r = edge_root(ep, i);
        int c = root_to_class[r];
        if (c < 0) {
            c = s->class_count++;
            root_to_class[r] = c;
        }
        s->cls_of_edge[i] = c;
        s->class_mask[c] |= s->bit[i];
        ++s->class_size[c];
    }
    return 1;
}

/* Rebuild both monochromatic connectivity structures and close all forced
 * class assignments.  This is exact unit propagation for the criterion that
 * no edge of one colour may have endpoints connected in the other colour. */
static int propagate(const Search *s, int8_t asn[MAX_CLASSES]) {
    int changed;
    do {
        int pr[NV], pb[NV], i, c;
        changed = 0;
        for (i = 0; i < NV; ++i) pr[i] = pb[i] = i;
        for (i = 0; i < LAMAN_EDGES; ++i) {
            c = s->cls_of_edge[i];
            if (asn[c] == 0) dsu_union(pr, s->u[i], s->v[i]);
            else if (asn[c] == 1) dsu_union(pb, s->u[i], s->v[i]);
        }
        for (c = 0; c < s->class_count; ++c) {
            int force_r = 0, force_b = 0;
            for (i = 0; i < LAMAN_EDGES; ++i) {
                if (s->cls_of_edge[i] != c) continue;
                if (dsu_find(pr, s->u[i]) == dsu_find(pr, s->v[i])) force_r = 1;
                if (dsu_find(pb, s->u[i]) == dsu_find(pb, s->v[i])) force_b = 1;
            }
            if (asn[c] == 0 && force_b) return 0;
            if (asn[c] == 1 && force_r) return 0;
            if (asn[c] < 0) {
                if (force_r && force_b) return 0;
                if (force_r || force_b) {
                    asn[c] = force_r ? 0 : 1;
                    changed = 1;
                }
            }
        }
    } while (changed);
    return 1;
}

static void search_rec(Search *s, int8_t asn[MAX_CLASSES]) {
    int c, choice = -1, best = -1;
    int8_t child[MAX_CLASSES];
    uint64_t red = 0;
    if (s->solution_count >= 2) return;
    ++s->nodes;
    if (!propagate(s, asn)) return;
    for (c = 0; c < s->class_count; ++c) {
        if (asn[c] < 0 && s->class_size[c] > best) {
            best = s->class_size[c];
            choice = c;
        }
    }
    if (choice < 0) {
        for (c = 0; c < s->class_count; ++c)
            if (asn[c] == 0) red |= s->class_mask[c];
        if (edge_colouring_is_nac(s, red)) {
            int q;
            for (q = 0; q < s->solution_count; ++q)
                if (s->solutions[q] == red || s->solutions[q] == (s->graph_mask ^ red)) return;
            s->solutions[s->solution_count++] = red;
        }
        return;
    }
    memcpy(child, asn, sizeof(child));
    child[choice] = 0;
    search_rec(s, child);
    if (s->solution_count >= 2) return;
    memcpy(child, asn, sizeof(child));
    child[choice] = 1;
    search_rec(s, child);
}

static void find_two_nac(Search *s) {
    int8_t asn[MAX_CLASSES];
    int c;
    for (c = 0; c < MAX_CLASSES; ++c) asn[c] = -1;
    /* Quotient global colour swap by requiring the first triangle class red. */
    asn[0] = 0;
    search_rec(s, asn);
}

static void adjacency_from_mask(uint64_t g, uint16_t adj[NV]) {
    int a, b, pos = NE - 1;
    for (a = 0; a < NV; ++a) adj[a] = 0;
    for (a = 0; a < NV; ++a)
        for (b = a + 1; b < NV; ++b, --pos)
            if (g & (UINT64_C(1) << pos)) {
                adj[a] |= (uint16_t)(1u << b);
                adj[b] |= (uint16_t)(1u << a);
            }
}

static int triangle_count(uint64_t g) {
    uint16_t adj[NV];
    int a, b, c, total = 0;
    adjacency_from_mask(g, adj);
    for (a = 0; a < NV; ++a)
        for (b = a + 1; b < NV; ++b)
            if (adj[a] & (1u << b))
                for (c = b + 1; c < NV; ++c)
                    if ((adj[a] & (1u << c)) && (adj[b] & (1u << c))) ++total;
    return total;
}

/* Returns one exact reverse 0-extension order and its number of open steps. */
static int h1_open_steps(uint64_t g, int *open_steps) {
    uint16_t adj[NV], active = (1u << NV) - 1u;
    int remaining = NV, open = 0, i;
    adjacency_from_mask(g, adj);
    while (remaining > 2) {
        int v = -1, u = -1, w = -1;
        for (i = 0; i < NV; ++i) {
            if ((active & (1u << i)) && __builtin_popcount((unsigned)(adj[i] & active)) == 2) {
                v = i;
                break;
            }
        }
        if (v < 0) return 0;
        for (i = 0; i < NV; ++i) if ((adj[v] & active) & (1u << i)) {
            if (u < 0) u = i; else w = i;
        }
        if (!(adj[u] & (1u << w))) ++open;
        active &= (uint16_t)~(1u << v);
        --remaining;
    }
    {
        int a = -1, b = -1;
        for (i = 0; i < NV; ++i) if (active & (1u << i)) {
            if (a < 0) a = i; else b = i;
        }
        if (a < 0 || b < 0 || !(adj[a] & (1u << b))) return 0;
    }
    *open_steps = open;
    return 1;
}

static int prism_count(uint64_t g) {
    uint16_t adj[NV];
    int mask, total = 0;
    adjacency_from_mask(g, adj);
    for (mask = 0; mask < (1 << NV); ++mask) {
        int v, edge_twice = 0, all_three = 1, has_triangle = 0;
        if (__builtin_popcount((unsigned)mask) != 6) continue;
        for (v = 0; v < NV; ++v) if (mask & (1 << v)) {
            int d = __builtin_popcount((unsigned)(adj[v] & mask));
            edge_twice += d;
            if (d != 3) all_three = 0;
        }
        if (!all_three || edge_twice != 18) continue;
        for (v = 0; v < NV && !has_triangle; ++v) if (mask & (1 << v)) {
            int w;
            uint16_t nb = adj[v] & (uint16_t)mask;
            for (w = v + 1; w < NV; ++w)
                if ((nb & (1u << w)) && (adj[w] & nb)) { has_triangle = 1; break; }
        }
        if (has_triangle) ++total;
    }
    return total;
}

static int has_stable_cut(uint64_t g) {
    uint16_t adj[NV];
    int s;
    adjacency_from_mask(g, adj);
    for (s = 0; s < (1 << NV); ++s) {
        int v, independent = 1;
        uint16_t rem = (uint16_t)(((1u << NV) - 1u) & ~s);
        uint16_t seen = 0, frontier;
        if (__builtin_popcount((unsigned)rem) < 2) continue;
        for (v = 0; v < NV; ++v) if (s & (1 << v)) {
            if (adj[v] & (uint16_t)s) { independent = 0; break; }
        }
        if (!independent) continue;
        frontier = (uint16_t)(rem & (uint16_t)(-(int16_t)rem));
        seen = frontier;
        while (frontier) {
            uint16_t next = 0;
            for (v = 0; v < NV; ++v) if (frontier & (1u << v)) next |= adj[v];
            next &= rem;
            next &= (uint16_t)~seen;
            seen |= next;
            frontier = next;
        }
        if (seen != rem) return 1;
    }
    return 0;
}

int main(int argc, char **argv) {
    FILE *in, *out;
    uint64_t g, processed = 0, limit = UINT64_MAX;
    uint64_t tags_two = 0, tags_a = 0, tags_b = 0, tags_t = 0;
    uint64_t total_nodes = 0, max_nodes = 0;
    if (argc < 3 || argc > 4) {
        fprintf(stderr, "usage: %s LamanGraphs11.txt certificate.txt [limit]\n", argv[0]);
        return 2;
    }
    if (argc == 4) limit = strtoull(argv[3], NULL, 10);
    in = fopen(argv[1], "rb");
    out = fopen(argv[2], "wb");
    if (!in || !out) { perror("open"); return 2; }
    fprintf(out, "NAC11CERT 1 11 2039273\n");
    while (processed < limit && next_uint64(in, &g)) {
        Search s;
        int open = -1, tri;
        if (!initialize_search(&s, g)) {
            fprintf(stderr, "bad edge count at record %" PRIu64 ": %" PRIu64 "\n", processed, g);
            return 3;
        }
        find_two_nac(&s);
        total_nodes += s.nodes;
        if (s.nodes > max_nodes) max_nodes = s.nodes;
        if (s.solution_count >= 2) {
            fprintf(out, "2 %" PRIu64 " %" PRIu64 " %" PRIu64 "\n",
                    g, s.solutions[0], s.solutions[1]);
            ++tags_two;
        } else {
            int h1 = h1_open_steps(g, &open);
            tri = triangle_count(g);
            if (h1 && open == 0 && tri == NV - 2) {
                fprintf(out, "T %" PRIu64 "\n", g);
                ++tags_t;
            } else if (h1 && open == 1 && tri == NV - 3) {
                fprintf(out, "B %" PRIu64 "\n", g);
                ++tags_b;
            } else if (prism_count(g) == 1 && !has_stable_cut(g)) {
                fprintf(out, "A %" PRIu64 "\n", g);
                ++tags_a;
            } else {
                fprintf(out, "X %" PRIu64 " %d", g, s.solution_count);
                if (s.solution_count == 1) fprintf(out, " %" PRIu64, s.solutions[0]);
                fputc('\n', out);
                fprintf(stderr,
                        "UNCLASSIFIED record=%" PRIu64 " graph=%" PRIu64
                        " nac_cap=%d h1=%d open=%d triangles=%d nodes=%" PRIu64 "\n",
                        processed, g, s.solution_count, h1, open, tri, s.nodes);
                fclose(in); fclose(out);
                return 4;
            }
        }
        ++processed;
        if ((processed % 100000u) == 0)
            fprintf(stderr,
                    "progress=%" PRIu64 " two=%" PRIu64 " A=%" PRIu64
                    " B=%" PRIu64 " T=%" PRIu64 " avg_nodes=%.2f max_nodes=%" PRIu64 "\n",
                    processed, tags_two, tags_a, tags_b, tags_t,
                    (double)total_nodes / (double)processed, max_nodes);
    }
    fclose(in);
    fclose(out);
    fprintf(stderr,
            "DONE records=%" PRIu64 " two=%" PRIu64 " A=%" PRIu64
            " B=%" PRIu64 " T=%" PRIu64 " nodes=%" PRIu64 " max_nodes=%" PRIu64 "\n",
            processed, tags_two, tags_a, tags_b, tags_t, total_nodes, max_nodes);
    return 0;
}
