/* experiment: move-ordering variants; prints nodes and cpu per variant */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
#include "vsolve.h"
static int VAR;
static int mobility(const uint8_t *v, int n) {
  int m = 0;
  for (int k = 0; k + 1 < n; k++) { m += VS_adj[v[k]][v[k+1]]; if (k + 3 < n) m += VS_adj[v[k]][v[k+3]]; }
  return m;
}
static int score(const uint8_t *w, int n, int k, int is3) {
  switch (VAR) {
  case 1: return mobility(w, n);
  case 2: return k;
  case 4: return -2 * k + is3;
  case 6: return mobility(w, n) * 64 - k;
  case 7: return -2 * (k + (is3 ? 3 : 1)) - is3;
  case 8: return -2 * (k + (is3 ? 3 : 1)) + is3;
  case 9: return -mobility(w, n) * 64 - k;
  default: return 0;
  }
}
static int dfs2(const uint8_t *v, int n) {
  if (n == 1) return 1;
  if (n == 2) return VS_adj[v[0]][v[1]];
  if (!vs_connected(v, n)) return 0;
  uint64_t a, b; vs_pack(v, n, &a, &b);
  if (vs_lookup(a, b)) return 0;
  VS_nodes++;
  uint8_t w[34][18]; int sc[34], idx[34], m = 0;
  for (int k = 0; k + 1 < n; k++) {
    if (VS_adj[v[k]][v[k + 1]]) {
      memcpy(w[m], v, k); memcpy(w[m] + k, v + k + 1, n - k - 1);
      sc[m] = score(w[m], n - 1, k, 0); idx[m] = m; m++;
    }
    if (k + 3 < n && VS_adj[v[k]][v[k + 3]]) {
      memcpy(w[m], v, n); w[m][k] = v[k + 3]; memmove(w[m] + k + 3, v + k + 4, n - k - 4);
      sc[m] = score(w[m], n - 1, k, 1); idx[m] = m; m++;
    }
  }
  /* sort idx by score desc (stable insertion) */
  for (int i = 1; i < m; i++) { int x = idx[i], j = i; while (j > 0 && sc[idx[j-1]] < sc[x]) { idx[j] = idx[j-1]; j--; } idx[j] = x; }
  for (int i = 0; i < m; i++) if (dfs2(w[idx[i]], n - 1)) return 1;
  vs_insert(a, b);
  return 0;
}
int main(int argc, char **argv) {
  VAR = atoi(argv[2]);
  FILE *f = fopen(argv[1], "rb"); vs_init();
  uint8_t r[18]; long cnt = 0, win = 0; clock_t t0 = clock();
  uint64_t hist[8] = {0};
  while (fread(r, 1, 18, f) == 18) {
    uint64_t b = VS_nodes;
    VS_stamp++; VS_count = 0;
    int w = (VAR < 0) ? vs_solve(r, 18) : dfs2(r, 18);
    uint64_t d = VS_nodes - b; int h = 0; while (d >= 10 && h < 7) { d /= 10; h++; } hist[h]++;
    win += w; cnt++;
  }
  printf("VAR %d: %ld recs, %ld win, nodes %llu, cpu %.2fs, nodes-hist(log10):", VAR, cnt, win, (unsigned long long)VS_nodes, (double)(clock()-t0)/CLOCKS_PER_SEC);
  for (int i = 0; i < 8; i++) printf(" %llu", (unsigned long long)hist[i]); printf("\n");
}
