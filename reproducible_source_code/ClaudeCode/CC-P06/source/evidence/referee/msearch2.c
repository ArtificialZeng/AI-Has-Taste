/* Referee's pruned search for signatures of multiplicity >= P+1 on m x n grids
 * (generalisation of msearch.c to grids up to 13 x 13 cells, without the dump).
 *
 * Backtracking over all single loops L (vertex by vertex, row-major, mate
 * bookkeeping so that leaves are exactly the single loops).  alive = set of
 * nonzero totally even sets d(S), S in ker A, such that L xor d(S) so far has
 * degree 0/2 at every processed vertex and the clue of L in every completed cell.
 * Branches with |alive| < P are cut; this is complete for multiplicity >= P+1
 * because a signature of multiplicity k has, for each of its loops L, k-1 sets
 * that stay alive along the whole path of L.  At a leaf the true multiplicity is
 * 1 + #{alive sets S : L xor d(S) is a single loop}.
 *
 * usage: msearch2 m n P [maxwitness]
 * Output: histogram of true multiplicities >= P+1 (counted over loops; each
 * signature of multiplicity k is reached exactly k times) and witness lines
 * "SIG mult rows..." for each such loop.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#define CW 3      /* words for cell masks (<= 192 cells) */
#define EW 6      /* words for edge sets (<= 384 edges) */

static int M, N, NV, NE, NC, P, AW;
static int dimK, nT;
static uint64_t *Tset;            /* nT x EW */
static uint64_t *okc, *okv;       /* [cell][16][AW], [vertex][16][AW] */
static uint64_t *abuf;            /* (NV+1) x AW */
static int vinc[200][4];
static int eend[400][2];
static long long hist[10000], nodes = 0, nleaves = 0;
static uint64_t Lw[EW];

static inline int Hid(int r, int c) { return r * N + c; }
static inline int Vid(int r, int c) { return (M + 1) * N + r * (N + 1) + c; }
static inline int bget(const uint64_t *s, int e) { return (s[e >> 6] >> (e & 63)) & 1; }
static inline void bset(uint64_t *s, int e) { s[e >> 6] |= 1ULL << (e & 63); }
static inline void bclr(uint64_t *s, int e) { s[e >> 6] &= ~(1ULL << (e & 63)); }

static int single_cycle(const uint64_t *X) {
    int cnt = 0, first = -1;
    for (int i = 0; i < EW; i++) cnt += __builtin_popcountll(X[i]);
    for (int e = 0; e < NE; e++) if (bget(X, e)) { first = e; break; }
    if (first < 0) return 0;
    int start = eend[first][0], v = eend[first][1], pe = first, steps = 1;
    while (v != start) {
        int ne = -1;
        for (int d = 0; d < 4; d++) { int e = vinc[v][d]; if (e >= 0 && e != pe && bget(X, e)) { ne = e; break; } }
        if (ne < 0) return 0;
        v = (eend[ne][0] == v) ? eend[ne][1] : eend[ne][0];
        pe = ne; if (++steps > cnt) return 0;
    }
    return steps == cnt;
}

typedef struct { signed char mate[16]; } fr;

static void leaf(const uint64_t *alive) {
    nleaves++;
    int mult = 1;
    for (int t = 0; t < nT; t++) if ((alive[t >> 6] >> (t & 63)) & 1) {
        uint64_t X[EW]; for (int i = 0; i < EW; i++) X[i] = Lw[i] ^ Tset[t * EW + i];
        if (single_cycle(X)) mult++;
    }
    hist[mult]++;
    if (mult >= P + 1) {
        printf("SIG %d ", mult);
        for (int r = 0; r < M; r++) {
            for (int c = 0; c < N; c++)
                printf("%d", bget(Lw, Hid(r, c)) + bget(Lw, Hid(r + 1, c)) + bget(Lw, Vid(r, c)) + bget(Lw, Vid(r, c + 1)));
            printf(r < M - 1 ? " " : "\n");
        }
    }
}

static void rec(int k, fr F, int nopen, int closed, uint64_t top) {
    nodes++;
    uint64_t *alive = abuf + (size_t)k * AW, *a2 = abuf + (size_t)(k + 1) * AW;
    if (k == NV) { if (closed) leaf(alive); return; }
    int r = k / (N + 1), c = k % (N + 1);
    int up = (r >= 1) && F.mate[c] >= 0;
    int lf = (c >= 1) && F.mate[N + 1] >= 0;
    int maxrt = (c < N), maxdn = (r < M);
    for (int rt = 0; rt <= maxrt; rt++) for (int dn = 0; dn <= maxdn; dn++) {
        int deg = up + lf + rt + dn;
        if (deg != 0 && deg != 2) continue;
        if (closed && deg) continue;
        fr G = F; int no = nopen, cl = closed;
        if (deg == 2) {
            if (up && lf) {
                int a = G.mate[c], b = G.mate[N + 1];
                if (a == N + 1) { if (no != 2) continue; cl = 1; }
                else { G.mate[a] = b; G.mate[b] = a; }
                G.mate[c] = -1; G.mate[N + 1] = -1; no -= 2;
            } else if (up) {
                if (rt) { int a = G.mate[c]; G.mate[N + 1] = a; G.mate[a] = N + 1; G.mate[c] = -1; }
            } else if (lf) {
                if (dn) { int a = G.mate[N + 1]; G.mate[c] = a; G.mate[a] = c; G.mate[N + 1] = -1; }
            } else { G.mate[c] = N + 1; G.mate[N + 1] = c; no += 2; }
        }
        int lv = (up ? 1 : 0) | (dn ? 2 : 0) | (lf ? 4 : 0) | (rt ? 8 : 0);
        const uint64_t *tv = okv + ((size_t)(r * (N + 1) + c) * 16 + lv) * AW;
        int pc = 0;
        if (r >= 1 && c < N) {
            int ttop = (top >> c) & 1, rgt = (F.mate[c + 1] >= 0);
            int lp = (ttop ? 1 : 0) | (rt ? 2 : 0) | (up ? 4 : 0) | (rgt ? 8 : 0);
            const uint64_t *tc = okc + ((size_t)((r - 1) * N + c) * 16 + lp) * AW;
            for (int i = 0; i < AW; i++) { a2[i] = alive[i] & tv[i] & tc[i]; pc += __builtin_popcountll(a2[i]); }
        } else {
            for (int i = 0; i < AW; i++) { a2[i] = alive[i] & tv[i]; pc += __builtin_popcountll(a2[i]); }
        }
        if (pc < P) continue;
        uint64_t t2 = (top & ~(1ULL << c)) | ((uint64_t)rt << c);
        if (rt) bset(Lw, Hid(r, c));
        if (dn) bset(Lw, Vid(r, c));
        rec(k + 1, G, no, cl, t2);
        if (rt) bclr(Lw, Hid(r, c));
        if (dn) bclr(Lw, Vid(r, c));
    }
}

static int kernel(uint64_t basis[][CW]) {
    static uint64_t R[200][CW], A[200][CW];
    memset(R, 0, sizeof(R));
    for (int r = 0; r < M; r++) for (int c = 0; c < N; c++) {
        uint64_t *m = R[r * N + c];
        if (r > 0) bset(m, (r - 1) * N + c);
        if (r < M - 1) bset(m, (r + 1) * N + c);
        if (c > 0) bset(m, r * N + c - 1);
        if (c < N - 1) bset(m, r * N + c + 1);
    }
    memcpy(A, R, sizeof(R));
    int piv[200], ispiv[200] = {0}, rank = 0;
    for (int col = 0; col < NC; col++) {
        int sel = -1;
        for (int i = rank; i < NC; i++) if (bget(R[i], col)) { sel = i; break; }
        if (sel < 0) continue;
        for (int w = 0; w < CW; w++) { uint64_t t = R[rank][w]; R[rank][w] = R[sel][w]; R[sel][w] = t; }
        for (int i = 0; i < NC; i++) if (i != rank && bget(R[i], col)) for (int w = 0; w < CW; w++) R[i][w] ^= R[rank][w];
        piv[rank] = col; ispiv[col] = 1; rank++;
    }
    int d = 0;
    for (int f = 0; f < NC; f++) if (!ispiv[f]) {
        uint64_t v[CW] = {0}; bset(v, f);
        for (int i = 0; i < rank; i++) if (bget(R[i], f)) bset(v, piv[i]);
        for (int i = 0; i < NC; i++) { int p = 0; for (int w = 0; w < CW; w++) p += __builtin_popcountll(A[i][w] & v[w]); if (p & 1) { fprintf(stderr, "kernel bug\n"); exit(1); } }
        memcpy(basis[d++], v, sizeof(v));
    }
    return d;
}

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: msearch2 m n P\n"); return 1; }
    M = atoi(argv[1]); N = atoi(argv[2]); P = atoi(argv[3]);
    NV = (M + 1) * (N + 1); NE = (M + 1) * N + M * (N + 1); NC = M * N;
    if (NC > 64 * CW || NE > 64 * EW || N + 2 > 16 || NV > 199 || N > 60) { fprintf(stderr, "too big\n"); return 1; }
    for (int r = 0; r <= M; r++) for (int c = 0; c < N; c++) { int e = Hid(r, c); eend[e][0] = r * (N + 1) + c; eend[e][1] = r * (N + 1) + c + 1; }
    for (int r = 0; r < M; r++) for (int c = 0; c <= N; c++) { int e = Vid(r, c); eend[e][0] = r * (N + 1) + c; eend[e][1] = (r + 1) * (N + 1) + c; }
    for (int r = 0; r <= M; r++) for (int c = 0; c <= N; c++) {
        int v = r * (N + 1) + c;
        vinc[v][0] = r > 0 ? Vid(r - 1, c) : -1; vinc[v][1] = r < M ? Vid(r, c) : -1;
        vinc[v][2] = c > 0 ? Hid(r, c - 1) : -1; vinc[v][3] = c < N ? Hid(r, c) : -1;
    }
    static uint64_t basis[200][CW];
    dimK = kernel(basis);
    if (dimK > 16) { fprintf(stderr, "kernel too big\n"); return 1; }
    nT = (1 << dimK) - 1; AW = (nT + 63) / 64; if (AW == 0) AW = 1;
    Tset = calloc((size_t)nT * EW, sizeof(uint64_t));
    for (int t = 0; t < nT; t++) {
        uint64_t S[CW] = {0};
        for (int i = 0; i < dimK; i++) if (((t + 1) >> i) & 1) for (int w = 0; w < CW; w++) S[w] ^= basis[i][w];
        uint64_t *Ts = Tset + (size_t)t * EW;
        for (int r = 0; r <= M; r++) for (int c = 0; c < N; c++) {
            int a = r > 0 ? bget(S, (r - 1) * N + c) : 0, b = r < M ? bget(S, r * N + c) : 0;
            if (a != b) bset(Ts, Hid(r, c));
        }
        for (int r = 0; r < M; r++) for (int c = 0; c <= N; c++) {
            int a = c > 0 ? bget(S, r * N + c - 1) : 0, b = c < N ? bget(S, r * N + c) : 0;
            if (a != b) bset(Ts, Vid(r, c));
        }
        for (int v = 0; v < NV; v++) { int d = 0; for (int j = 0; j < 4; j++) if (vinc[v][j] >= 0) d += bget(Ts, vinc[v][j]); if (d & 1) { fprintf(stderr, "odd vertex\n"); return 1; } }
        for (int r = 0; r < M; r++) for (int c = 0; c < N; c++) {
            int d = bget(Ts, Hid(r, c)) + bget(Ts, Hid(r + 1, c)) + bget(Ts, Vid(r, c)) + bget(Ts, Vid(r, c + 1));
            if (d & 1) { fprintf(stderr, "odd cell\n"); return 1; }
        }
    }
    okc = calloc((size_t)NC * 16 * AW, sizeof(uint64_t));
    okv = calloc((size_t)NV * 16 * AW, sizeof(uint64_t));
    abuf = calloc((size_t)(NV + 2) * AW, sizeof(uint64_t));
    for (int r = 0; r < M; r++) for (int c = 0; c < N; c++) for (int t = 0; t < nT; t++) {
        uint64_t *Ts = Tset + (size_t)t * EW;
        int tp = bget(Ts, Hid(r, c)) | (bget(Ts, Hid(r + 1, c)) << 1) | (bget(Ts, Vid(r, c)) << 2) | (bget(Ts, Vid(r, c + 1)) << 3);
        for (int lp = 0; lp < 16; lp++)
            if (__builtin_popcount(tp & lp) == __builtin_popcount(tp & ~lp & 15))
                okc[((size_t)(r * N + c) * 16 + lp) * AW + (t >> 6)] |= 1ULL << (t & 63);
    }
    for (int v = 0; v < NV; v++) for (int t = 0; t < nT; t++) {
        uint64_t *Ts = Tset + (size_t)t * EW; int tv = 0;
        for (int j = 0; j < 4; j++) if (vinc[v][j] >= 0 && bget(Ts, vinc[v][j])) tv |= 1 << j;
        for (int lv = 0; lv < 16; lv++)
            if (__builtin_popcount(lv ^ tv) <= 2) okv[((size_t)v * 16 + lv) * AW + (t >> 6)] |= 1ULL << (t & 63);
    }
    printf("grid %dx%d cells, kernel dim %d, %d nonzero totally even sets, prune P=%d\n", M, N, dimK, nT, P);
    fflush(stdout);
    for (int t = 0; t < nT; t++) abuf[t >> 6] |= 1ULL << (t & 63);
    fr F; for (int i = 0; i < 16; i++) F.mate[i] = -1;
    memset(Lw, 0, sizeof(Lw));
    rec(0, F, 0, 0, 0);
    printf("search nodes %lld, loops reached %lld\n", nodes, nleaves);
    printf("exact multiplicities >= %d (k: loops, signatures = loops/k):\n", P + 1);
    for (int k = P + 1; k < 10000; k++) if (hist[k]) printf("  %d: %lld loops, %lld signatures%s\n", k, hist[k], hist[k] / k, hist[k] % k ? " NOT DIVISIBLE" : "");
    printf("END\n");
    return 0;
}
