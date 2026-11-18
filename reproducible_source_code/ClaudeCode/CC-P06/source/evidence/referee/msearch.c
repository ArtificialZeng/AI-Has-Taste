/* Referee's search for signatures of high multiplicity on m x n grids.
 *
 * Enumerates every single loop L of the (m+1)x(n+1) vertex grid by
 * backtracking over the vertices in row-major order (plug/mate bookkeeping,
 * so every leaf is exactly one loop, each loop exactly once).
 *
 * For every L it computes  mult(L) = #{ S in ker A : L xor d(S) is a single loop
 * with the same signature as L }  (A = cell adjacency matrix over GF(2),
 * d(S) = boundary of the cell set S), which equals the multiplicity of the
 * signature of L.  The local conditions (same clue in every cell, degree 0/2 at
 * every vertex for L xor d(S)) are tracked incrementally as a bit mask "alive"
 * over the 2^dim - 1 nonzero S; connectivity of L xor d(S) is checked at the leaf.
 *
 * Option P > 0: prune every branch with fewer than P alive sets.  This is a
 * complete search for signatures of multiplicity >= P+1 (alive sets only shrink).
 *
 * Option dump (P = 0 only): also stores the signature of every loop, sorts
 * them and counts equal signatures directly -- a check that does not use the
 * totally-even theory at all.
 *
 * usage: msearch m n P dump
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#define MAXE 192
#define EW 3
#define AW 4

typedef struct { uint64_t w[AW]; } amask;
typedef struct { uint64_t w[EW]; } eset;

static int M, N, NV, NE, NC, P, DUMP;
static int dimK, nT;
static eset T[256];
static amask okc[64][16];   /* per cell, per L-pattern (top,bottom,left,right) */
static amask okv[81][16];   /* per vertex, per L-pattern (up,down,left,right) */
static int vinc[81][4];     /* incident edges of vertex: up, down, left, right (-1 none) */
static int eend[MAXE][2];

static long long hist[300];       /* hist[k] = number of loops whose signature has multiplicity k */
static long long nloops = 0, leaves_alive = 0;
static long long witness_printed = 0;

static uint64_t *sigs_lo = NULL; static uint8_t *sigs_hi = NULL; static long long nsig = 0, capsig = 0;

static inline int Hid(int r, int c) { return r * N + c; }
static inline int Vid(int r, int c) { return (M + 1) * N + r * (N + 1) + c; }
static inline int eget(const eset *s, int e) { return (s->w[e >> 6] >> (e & 63)) & 1; }
static inline void eset1(eset *s, int e) { s->w[e >> 6] |= 1ULL << (e & 63); }
static inline void eclr(eset *s, int e) { s->w[e >> 6] &= ~(1ULL << (e & 63)); }

static eset L;  /* current loop edges */

static int single_cycle(const eset *X) {
    int cnt = 0, first = -1;
    for (int i = 0; i < EW; i++) cnt += __builtin_popcountll(X->w[i]);
    for (int e = 0; e < NE; e++) if (eget(X, e)) { first = e; break; }
    if (first < 0) return 0;
    int start = eend[first][0], v = eend[first][1], pe = first, steps = 1;
    while (v != start) {
        int ne = -1;
        for (int d = 0; d < 4; d++) {
            int e = vinc[v][d];
            if (e >= 0 && e != pe && eget(X, e)) { ne = e; break; }
        }
        if (ne < 0) return 0;
        v = (eend[ne][0] == v) ? eend[ne][1] : eend[ne][0];
        pe = ne; steps++;
        if (steps > cnt) return 0;
    }
    return steps == cnt;
}

static inline int apop(const amask *a) {
    int s = 0; for (int i = 0; i < AW; i++) s += __builtin_popcountll(a->w[i]); return s;
}

/* mate[p]: other end of the open path whose end sits at frontier position p
 * (p = 0..N column plugs, p = N+1 the left plug), -1 if empty. */
typedef struct { signed char mate[16]; } fr;

static void leaf(amask alive, unsigned __int128 sig, int has4) {
    nloops++;
    int mult = 1;
    if (apop(&alive)) {
        leaves_alive++;
        for (int t = 0; t < nT; t++) if ((alive.w[t >> 6] >> (t & 63)) & 1) {
            eset X; for (int i = 0; i < EW; i++) X.w[i] = L.w[i] ^ T[t].w[i];
            if (single_cycle(&X)) mult++;
        }
    }
    hist[mult]++;
    if (mult >= 5 && witness_printed < 20) {
        witness_printed++;
        printf("WITNESS mult=%d sig=", mult);
        for (int r = 0; r < M; r++) { for (int c = 0; c < N; c++) {
            int cl = 0, cell = r * N + c;
            cl += eget(&L, Hid(r, c)) + eget(&L, Hid(r + 1, c)) + eget(&L, Vid(r, c)) + eget(&L, Vid(r, c + 1));
            (void)cell; printf("%d", cl); } printf(r < M - 1 ? "/" : "\n"); }
        fflush(stdout);
    }
    if (DUMP && !has4) {
        if (nsig == capsig) {
            capsig = capsig ? capsig * 2 : (1 << 20);
            sigs_lo = realloc(sigs_lo, capsig * sizeof(uint64_t));
            sigs_hi = realloc(sigs_hi, capsig);
            if (!sigs_lo || !sigs_hi) { fprintf(stderr, "out of memory\n"); exit(1); }
        }
        sigs_lo[nsig] = (uint64_t)sig; sigs_hi[nsig] = (uint8_t)(sig >> 64); nsig++;
    }
}

static void rec(int k, fr F, int nopen, int closed, uint64_t top, amask alive,
                unsigned __int128 sig, int has4) {
    if (k == NV) { if (closed) leaf(alive, sig, has4); return; }
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
                if (a == N + 1) {           /* both ends of the same path: closes a loop */
                    if (no != 2) continue;  /* another path is still open */
                    cl = 1;
                } else { G.mate[a] = b; G.mate[b] = a; }
                G.mate[c] = -1; G.mate[N + 1] = -1; no -= 2;
            } else if (up) {
                if (rt) { int a = G.mate[c]; G.mate[N + 1] = a; G.mate[a] = N + 1; G.mate[c] = -1; }
                /* dn: the end stays at column c */
            } else if (lf) {
                if (dn) { int a = G.mate[N + 1]; G.mate[c] = a; G.mate[a] = c; G.mate[N + 1] = -1; }
            } else {                        /* rt && dn: a new path */
                G.mate[c] = N + 1; G.mate[N + 1] = c; no += 2;
            }
        }
        /* deg == 0: positions c and N+1 are empty and stay empty */
        /* local checks */
        amask a2 = alive;
        int lv = (up ? 1 : 0) | (dn ? 2 : 0) | (lf ? 4 : 0) | (rt ? 8 : 0);
        int vid = r * (N + 1) + c;
        for (int i = 0; i < AW; i++) a2.w[i] &= okv[vid][lv].w[i];
        unsigned __int128 s2 = sig; int h4 = has4;
        if (r >= 1 && c < N) {
            int ttop = (top >> c) & 1;
            int rgt = (F.mate[c + 1] >= 0);   /* v[r-1][c+1], not yet consumed */
            int lp = (ttop ? 1 : 0) | (rt ? 2 : 0) | (up ? 4 : 0) | (rgt ? 8 : 0);
            int cell = (r - 1) * N + c;
            for (int i = 0; i < AW; i++) a2.w[i] &= okc[cell][lp].w[i];
            int clue = __builtin_popcount(lp);
            if (clue == 4) h4 = 1; else s2 |= ((unsigned __int128)clue) << (2 * cell);
        }
        if (P > 0 && apop(&a2) < P) continue;
        uint64_t t2 = (top & ~(1ULL << c)) | ((uint64_t)rt << c);
        if (rt) eset1(&L, Hid(r, c));
        if (dn) eset1(&L, Vid(r, c));
        rec(k + 1, G, no, cl, t2, a2, s2, h4);
        if (rt) eclr(&L, Hid(r, c));
        if (dn) eclr(&L, Vid(r, c));
    }
}

/* ---- kernel of the cell adjacency matrix over GF(2) ---- */
static int kernel(uint64_t *basis) {
    uint64_t R[64]; int piv[64], rank = 0;
    for (int r = 0; r < M; r++) for (int c = 0; c < N; c++) {
        uint64_t m = 0;
        if (r > 0) m |= 1ULL << ((r - 1) * N + c);
        if (r < M - 1) m |= 1ULL << ((r + 1) * N + c);
        if (c > 0) m |= 1ULL << (r * N + c - 1);
        if (c < N - 1) m |= 1ULL << (r * N + c + 1);
        R[r * N + c] = m;
    }
    uint64_t A[64]; memcpy(A, R, sizeof(R));
    int ispiv[64] = {0};
    for (int col = 0; col < NC; col++) {
        int sel = -1;
        for (int i = rank; i < NC; i++) if ((R[i] >> col) & 1) { sel = i; break; }
        if (sel < 0) continue;
        uint64_t tmp = R[rank]; R[rank] = R[sel]; R[sel] = tmp;
        for (int i = 0; i < NC; i++) if (i != rank && ((R[i] >> col) & 1)) R[i] ^= R[rank];
        piv[rank] = col; ispiv[col] = 1; rank++;
    }
    int d = 0;
    for (int f = 0; f < NC; f++) if (!ispiv[f]) {
        uint64_t v = 1ULL << f;
        for (int i = 0; i < rank; i++) if ((R[i] >> f) & 1) v |= 1ULL << piv[i];
        for (int i = 0; i < NC; i++) if (__builtin_popcountll(A[i] & v) & 1) { fprintf(stderr, "kernel bug\n"); exit(1); }
        basis[d++] = v;
    }
    return d;
}

static int cmp_sig(const void *a, const void *b) {
    const unsigned __int128 x = *(const unsigned __int128 *)a, y = *(const unsigned __int128 *)b;
    return x < y ? -1 : x > y;
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: msearch m n [P] [dump]\n"); return 1; }
    M = atoi(argv[1]); N = atoi(argv[2]); P = argc > 3 ? atoi(argv[3]) : 0; DUMP = argc > 4 ? atoi(argv[4]) : 0;
    NV = (M + 1) * (N + 1); NE = (M + 1) * N + M * (N + 1); NC = M * N;
    if (NC > 64 || NE > MAXE || N + 2 > 16 || NV > 81) { fprintf(stderr, "too big\n"); return 1; }
    if (DUMP && 2 * NC > 128) { fprintf(stderr, "dump needs 2*cells <= 128\n"); return 1; }
    for (int r = 0; r <= M; r++) for (int c = 0; c < N; c++) { int e = Hid(r, c); eend[e][0] = r * (N + 1) + c; eend[e][1] = r * (N + 1) + c + 1; }
    for (int r = 0; r < M; r++) for (int c = 0; c <= N; c++) { int e = Vid(r, c); eend[e][0] = r * (N + 1) + c; eend[e][1] = (r + 1) * (N + 1) + c; }
    for (int r = 0; r <= M; r++) for (int c = 0; c <= N; c++) {
        int v = r * (N + 1) + c;
        vinc[v][0] = r > 0 ? Vid(r - 1, c) : -1; vinc[v][1] = r < M ? Vid(r, c) : -1;
        vinc[v][2] = c > 0 ? Hid(r, c - 1) : -1; vinc[v][3] = c < N ? Hid(r, c) : -1;
    }
    uint64_t basis[64];
    dimK = kernel(basis);
    nT = (1 << dimK) - 1;
    if (nT > 64 * AW) { fprintf(stderr, "kernel too big\n"); return 1; }
    for (int t = 0; t < nT; t++) {
        uint64_t S = 0;
        for (int i = 0; i < dimK; i++) if (((t + 1) >> i) & 1) S ^= basis[i];
        memset(&T[t], 0, sizeof(eset));
        for (int r = 0; r <= M; r++) for (int c = 0; c < N; c++) {
            int a = r > 0 ? (S >> ((r - 1) * N + c)) & 1 : 0, b = r < M ? (S >> (r * N + c)) & 1 : 0;
            if (a != b) eset1(&T[t], Hid(r, c));
        }
        for (int r = 0; r < M; r++) for (int c = 0; c <= N; c++) {
            int a = c > 0 ? (S >> (r * N + c - 1)) & 1 : 0, b = c < N ? (S >> (r * N + c)) & 1 : 0;
            if (a != b) eset1(&T[t], Vid(r, c));
        }
        /* sanity: totally even */
        for (int v = 0; v < NV; v++) { int d = 0; for (int j = 0; j < 4; j++) if (vinc[v][j] >= 0) d += eget(&T[t], vinc[v][j]); if (d & 1) { fprintf(stderr, "not even at vertex\n"); return 1; } }
        for (int r = 0; r < M; r++) for (int c = 0; c < N; c++) {
            int d = eget(&T[t], Hid(r, c)) + eget(&T[t], Hid(r + 1, c)) + eget(&T[t], Vid(r, c)) + eget(&T[t], Vid(r, c + 1));
            if (d & 1) { fprintf(stderr, "not even at cell\n"); return 1; }
        }
    }
    memset(okc, 0, sizeof(okc)); memset(okv, 0, sizeof(okv));
    for (int r = 0; r < M; r++) for (int c = 0; c < N; c++) for (int t = 0; t < nT; t++) {
        int tp = eget(&T[t], Hid(r, c)) | (eget(&T[t], Hid(r + 1, c)) << 1) | (eget(&T[t], Vid(r, c)) << 2) | (eget(&T[t], Vid(r, c + 1)) << 3);
        for (int lp = 0; lp < 16; lp++)
            if (__builtin_popcount(tp & lp) == __builtin_popcount(tp & ~lp & 15))
                okc[r * N + c][lp].w[t >> 6] |= 1ULL << (t & 63);
    }
    for (int v = 0; v < NV; v++) for (int t = 0; t < nT; t++) {
        int tv = 0;
        for (int j = 0; j < 4; j++) if (vinc[v][j] >= 0 && eget(&T[t], vinc[v][j])) tv |= 1 << j;
        for (int lv = 0; lv < 16; lv++)
            if (__builtin_popcount(lv ^ tv) <= 2) okv[v][lv].w[t >> 6] |= 1ULL << (t & 63);
    }
    printf("grid %dx%d cells, kernel dim %d, nonzero totally even sets %d, prune P=%d\n", M, N, dimK, nT, P);
    fflush(stdout);
    fr F; for (int i = 0; i < 16; i++) F.mate[i] = -1;
    amask all; memset(&all, 0, sizeof(all));
    for (int t = 0; t < nT; t++) all.w[t >> 6] |= 1ULL << (t & 63);
    memset(&L, 0, sizeof(L));
    rec(0, F, 0, 0, 0, all, 0, 0);
    printf("loops reached as leaves: %lld (leaves with some alive set: %lld)\n", nloops, leaves_alive);
    printf("multiplicity histogram over loops (k: loops, signatures=loops/k):\n");
    for (int k = 1; k < 300; k++) if (hist[k]) printf("  %d: %lld loops, %lld signatures%s\n", k, hist[k], hist[k] / k, hist[k] % k ? "  (NOT DIVISIBLE!)" : "");
    if (DUMP) {
        /* theory-free check: sort signatures and count runs */
        unsigned __int128 *a = malloc(nsig * sizeof(unsigned __int128));
        for (long long i = 0; i < nsig; i++) a[i] = ((unsigned __int128)sigs_hi[i] << 64) | sigs_lo[i];
        free(sigs_lo); free(sigs_hi);
        qsort(a, nsig, sizeof(unsigned __int128), cmp_sig);
        long long h2[300] = {0};
        for (long long i = 0; i < nsig;) { long long j = i; while (j < nsig && a[j] == a[i]) j++; h2[j - i < 299 ? j - i : 299]++; i = j; }
        printf("direct grouping of %lld signatures (unit squares excluded, %d of them):\n", nsig, M * N);
        for (int k = 1; k < 300; k++) if (h2[k]) printf("  multiplicity %d: %lld signatures\n", k, h2[k]);
    }
    return 0;
}
