/* poisonbfs: same as poison.c but uses the exhaustive BFS solver (no memo, no pruning).
 * poison PART NPART c1 c2 ... cm : for the fixed prefix c1..cm (m < 18), try
 * every ordered choice of 18-m further distinct cards (from the 52-m unused
 * ones) and count winnable deals with the verifier's own solver (vsolve.h).
 * Work is split by the index of the first appended card: this process does
 * the indices i with i % NPART == PART. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
#include "vsolve.h"
/* ---------- independent BFS solver ---------- */
typedef struct { uint64_t a, b; } k128;
static int kcmp(const void *x, const void *y) {
  const k128 *p = x, *q = y;
  if (p->a != q->a) return p->a < q->a ? -1 : 1;
  if (p->b != q->b) return p->b < q->b ? -1 : 1;
  return 0;
}
static void unpack(k128 k, uint8_t *v, int n) {
  uint8_t t[18];
  uint64_t x = k.a, y = k.b;
  for (int i = 9; i >= 0; i--) { t[i] = x & 63; x >>= 6; }
  for (int i = 17; i >= 10; i--) { t[i] = y & 63; y >>= 6; }
  memcpy(v, t, n);
}
static int adjb(int a, int b) { return a / 13 == b / 13 || a % 13 == b % 13; }
static size_t BFS_maxlayer;
static int bfs_solve(const uint8_t *deal, int n) {
  size_t cap = 1024, cnt = 1;
  k128 *cur = malloc(cap * sizeof(k128));
  vs_pack(deal, n, &cur[0].a, &cur[0].b);
  BFS_maxlayer = 1;
  for (int len = n; len > 1; len--) {
    size_t ncap = 1024, ncnt = 0;
    k128 *nxt = malloc(ncap * sizeof(k128));
    for (size_t i = 0; i < cnt; i++) {
      uint8_t v[18], w[18];
      unpack(cur[i], v, len);
      for (int k = 0; k + 1 < len; k++) {
        if (adjb(v[k], v[k + 1])) {
          int m = 0;
          for (int j = 0; j < len; j++) if (j != k) w[m++] = v[j];
          if (ncnt == ncap) { ncap *= 2; nxt = realloc(nxt, ncap * sizeof(k128)); }
          vs_pack(w, len - 1, &nxt[ncnt].a, &nxt[ncnt].b); ncnt++;
        }
        if (k + 3 < len && adjb(v[k], v[k + 3])) {
          int m = 0;
          for (int j = 0; j < len; j++) {
            if (j == k) w[m++] = v[k + 3];
            else if (j != k + 3) w[m++] = v[j];
          }
          if (ncnt == ncap) { ncap *= 2; nxt = realloc(nxt, ncap * sizeof(k128)); }
          vs_pack(w, len - 1, &nxt[ncnt].a, &nxt[ncnt].b); ncnt++;
        }
      }
    }
    free(cur);
    qsort(nxt, ncnt, sizeof(k128), kcmp);
    size_t u = 0;
    for (size_t i = 0; i < ncnt; i++)
      if (u == 0 || kcmp(&nxt[i], &nxt[u - 1]) != 0) nxt[u++] = nxt[i];
    cur = nxt; cnt = u;
    if (cnt > BFS_maxlayer) BFS_maxlayer = cnt;
    if (cnt == 0) { free(cur); return 0; }
  }
  free(cur);
  return 1;
}


static uint8_t deal[18], rest[52]; static int m, nrest, used[52];
static long tried = 0, wins = 0;
static void rec(int pos) {
  if (pos == 18) {
    tried++;
    if (bfs_solve(deal, 18)) {
      wins++;
      if (wins <= 10) { printf("WINNABLE:"); for (int i = 0; i < 18; i++) printf(" %d", deal[i]); printf("\n"); }
    }
    return;
  }
  for (int i = 0; i < nrest; i++) if (!used[i]) { used[i] = 1; deal[pos] = rest[i]; rec(pos + 1); used[i] = 0; }
}
int main(int argc, char **argv) {
  int part = atoi(argv[1]), npart = atoi(argv[2]);
  m = argc - 3; int in[52] = {0};
  for (int i = 0; i < m; i++) { int c = atoi(argv[3 + i]); if (c < 0 || c > 51 || in[c]) { fprintf(stderr, "bad prefix\n"); return 2; } in[c] = 1; deal[i] = c; }
  for (int c = 0; c < 52; c++) if (!in[c]) rest[nrest++] = c;
  vs_init();
  clock_t t0 = clock();
  for (int i = 0; i < nrest; i++) {
    if (i % npart != part) continue;
    used[i] = 1; deal[m] = rest[i];
    if (m + 1 == 18) { tried++; if (bfs_solve(deal, 18)) { wins++; printf("WINNABLE first=%d\n", rest[i]); } }
    else rec(m + 1);
    used[i] = 0;
  }
  printf("POISON-CHECK(BFS) part %d/%d prefix_len %d: completions tried %ld, winnable %ld, nodes %llu, cpu %.1fs\n",
         part, npart, m, tried, wins, (unsigned long long)VS_nodes, (double)(clock() - t0) / CLOCKS_PER_SEC);
  return 0;
}
