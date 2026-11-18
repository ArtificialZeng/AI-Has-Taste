/* poison PART NPART c1 c2 ... cm : for the fixed prefix c1..cm (m < 18), try
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
static uint8_t deal[18], rest[52]; static int m, nrest, used[52];
static long tried = 0, wins = 0;
static void rec(int pos) {
  if (pos == 18) {
    tried++;
    if (vs_solve(deal, 18)) {
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
    if (m + 1 == 18) { tried++; if (vs_solve(deal, 18)) { wins++; printf("WINNABLE first=%d\n", rest[i]); } }
    else rec(m + 1);
    used[i] = 0;
  }
  printf("POISON-CHECK part %d/%d prefix_len %d: completions tried %ld, winnable %ld, nodes %llu, cpu %.1fs\n",
         part, npart, m, tried, wins, (unsigned long long)VS_nodes, (double)(clock() - t0) / CLOCKS_PER_SEC);
  return 0;
}
