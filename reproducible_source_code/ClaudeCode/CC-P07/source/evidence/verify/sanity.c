/* Sanity checks for the verifier's solver:
 *  (1) Knuth's example deal from ex. 7.2.2.2-486 and the two bad first moves;
 *  (2) random 18-card deals: DFS solver vs an independent exhaustive
 *      breadth-first (layer by layer) enumeration of all reachable states.
 * usage: sanity NRANDOM SEED */
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

/* ---------- card parsing ---------- */
static int card(const char *s) {
  /* rank letters: A 2..9 T J Q K ; suits: C D H S -> 0 1 2 3 */
  const char *R = "A23456789TJQK", *S = "CDHS";
  int r = (int)(strchr(R, s[0]) - R), su = (int)(strchr(S, s[1]) - S);
  return su * 13 + r;
}

static uint64_t rs;
static uint64_t rnd(void) { /* splitmix64 */
  uint64_t z = (rs += 0x9E3779B97F4A7C15ULL);
  z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL;
  z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
  return z ^ (z >> 31);
}

int main(int argc, char **argv) {
  int N = argc > 1 ? atoi(argv[1]) : 10000;
  rs = argc > 2 ? strtoull(argv[2], 0, 10) : 12345;
  vs_init();
  /* Knuth's example: JH 5H TC 8D JC AC KS AH 4C 8S 5S 5D 2D TS AS 6H 3H TD */
  const char *ex[18] = {"JH","5H","TC","8D","JC","AC","KS","AH","4C","8S","5S","5D","2D","TS","AS","6H","3H","TD"};
  uint8_t d[18], w[18];
  for (int i = 0; i < 18; i++) d[i] = card(ex[i]);
  printf("Knuth example: DFS %d BFS %d (expect 1 1)\n", vs_solve(d, 18), bfs_solve(d, 18));
  /* AC (position 6, index 5) captures JC (position 5, index 4): delete index 4 */
  { int m = 0; for (int i = 0; i < 18; i++) if (i != 4) w[m++] = d[i]; }
  printf("after AC takes JC: DFS %d BFS %d (expect 0 0)\n", vs_solve(w, 17), bfs_solve(w, 17));
  /* AC (index 5) captures TC (position 3, index 2): w[2]=d[5], delete index 5 */
  { int m = 0; for (int i = 0; i < 18; i++) { if (i == 2) w[m++] = d[5]; else if (i != 5) w[m++] = d[i]; } }
  printf("after AC takes TC: DFS %d BFS %d (expect 0 0)\n", vs_solve(w, 17), bfs_solve(w, 17));
  /* all legal first moves of the example */
  printf("first moves of example (pos of mover -> pos captured : DFS BFS):\n");
  for (int k = 0; k < 17; k++)
    for (int s = 1; s <= 3; s += 2) {
      if (k + s >= 18 || !adjb(d[k], d[k + s])) continue;
      int m = 0;
      for (int i = 0; i < 18; i++) { if (i == k) w[m++] = d[k + s]; else if (i != k + s) w[m++] = d[i]; }
      printf("  %s(%d)->%s(%d): %d %d\n", ex[k + s], k + s + 1, ex[k], k + 1, vs_solve(w, 17), bfs_solve(w, 17));
    }

  /* random deals */
  int wins = 0, disagree = 0; size_t maxl = 0;
  for (int t = 0; t < N; t++) {
    uint8_t deck[52];
    for (int i = 0; i < 52; i++) deck[i] = i;
    for (int i = 0; i < 18; i++) { int j = i + (int)(rnd() % (52 - i)); uint8_t x = deck[i]; deck[i] = deck[j]; deck[j] = x; }
    int a = vs_solve(deck, 18), b = bfs_solve(deck, 18);
    if (BFS_maxlayer > maxl) maxl = BFS_maxlayer;
    wins += a;
    if (a != b) { disagree++; if (disagree < 5) { printf("DISAGREE:"); for (int i = 0; i < 18; i++) printf(" %d", deck[i]); printf("\n"); } }
  }
  printf("random deals: %d, DFS wins %d (%.2f%%), DFS/BFS disagreements %d, max BFS layer %zu\n",
         N, wins, 100.0 * wins / N, disagree, maxl);
  return disagree ? 1 : 0;
}
