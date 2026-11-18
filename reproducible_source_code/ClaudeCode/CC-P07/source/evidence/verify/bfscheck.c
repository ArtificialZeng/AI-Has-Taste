/* bfscheck FILE STRIDE NMAX : runs the independent exhaustive BFS solver (same
 * code as in sanity.c) on every STRIDE-th complete record of FILE, up to NMAX
 * records, and also the DFS solver; reports counts and disagreements. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
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


int main(int argc, char **argv) {
  FILE *f = fopen(argv[1], "rb"); long stride = atol(argv[2]), nmax = atol(argv[3]);
  vs_init();
  uint8_t r[18]; long i = 0, n = 0, bw = 0, dw = 0, dis = 0;
  while (n < nmax && fread(r, 1, 18, f) == 18) {
    if (i++ % stride) continue;
    n++;
    int b = bfs_solve(r, 18), d = vs_solve(r, 18);
    bw += b; dw += d; if (b != d) dis++;
  }
  printf("bfscheck %s: sampled %ld records (stride %ld), BFS winnable %ld, DFS winnable %ld, disagreements %ld\n", argv[1], n, stride, bw, dw, dis);
  return 0;
}
