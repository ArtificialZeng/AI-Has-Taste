/* cover K CODEFILE...
 * Loads canonical-prefix codes written by verify, sorts and deduplicates them,
 * independently enumerates ALL canonical K-patterns (recursive generation of
 * sequences of distinct (suit,rank) pairs where each new suit is the next unused
 * suit label and each new rank the next unused rank label), and compares the two
 * sets element by element. Codes with the top bit set (non-winnable records) are
 * excluded from the covered set and counted. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

static int cmp64(const void *a, const void *b) {
  uint64_t x = *(const uint64_t *)a, y = *(const uint64_t *)b;
  return x < y ? -1 : x > y;
}
static uint64_t *all; static size_t nall, capall;
static int used[4][13];
static void gen(int K, int i, int ns, int nr, uint64_t code) {
  if (i == K) {
    if (nall == capall) { capall = capall ? 2 * capall : 1 << 20; all = realloc(all, capall * 8); }
    all[nall++] = code; return;
  }
  for (int s = 0; s <= ns && s < 4; s++)
    for (int r = 0; r <= nr && r < 13; r++) {
      if (used[s][r]) continue;
      used[s][r] = 1;
      gen(K, i + 1, ns + (s == ns), nr + (r == nr), code * 64 + (uint64_t)(s * 13 + r));
      used[s][r] = 0;
    }
}

int main(int argc, char **argv) {
  int K = atoi(argv[1]);
  /* counts by recursive enumeration, k=1..K */
  for (int k = 1; k <= K; k++) { nall = 0; gen(k, 0, 0, 0, 0); printf("enumerated patterns k=%d: %zu\n", k, nall); }
  qsort(all, nall, 8, cmp64);
  for (size_t i = 1; i < nall; i++) if (all[i] == all[i - 1]) { printf("BUG: duplicate in enumeration\n"); return 1; }
  size_t cap = 1 << 20, n = 0; uint64_t *c = malloc(cap * 8); size_t losers = 0;
  for (int a = 2; a < argc; a++) {
    FILE *f = fopen(argv[a], "rb"); if (!f) { perror(argv[a]); return 2; }
    uint64_t x;
    while (fread(&x, 8, 1, f) == 1) {
      if (x >> 63) { losers++; continue; }
      if (n == cap) { cap *= 2; c = realloc(c, cap * 8); }
      c[n++] = x;
    }
    fclose(f);
  }
  printf("codes read (winnable records): %zu, non-winnable records excluded: %zu\n", n, losers);
  qsort(c, n, 8, cmp64);
  size_t u = 0, dups = 0;
  for (size_t i = 0; i < n; i++) {
    if (u && c[i] == c[u - 1]) { dups++; if (dups <= 5) printf("DUPLICATE pattern code %llu\n", (unsigned long long)c[i]); continue; }
    c[u++] = c[i];
  }
  printf("distinct covered patterns: %zu, duplicate records: %zu\n", u, dups);
  /* merge-compare */
  size_t i = 0, j = 0, missing = 0, extra = 0;
  while (i < nall || j < u) {
    if (j == u || (i < nall && all[i] < c[j])) {
      missing++;
      if (missing <= 10) {
        printf("MISSING pattern:");
        for (int t = K - 1; t >= 0; t--) { int v = (all[i] >> (6 * t)) & 63; printf(" (s%d,r%d)", v / 13, v % 13); }
        printf("\n");
      }
      i++;
    } else if (i == nall || c[j] < all[i]) {
      extra++; if (extra <= 10) printf("EXTRA (not a canonical %d-pattern) code %llu\n", K, (unsigned long long)c[j]);
      j++;
    } else { i++; j++; }
  }
  printf("full set size %zu, missing %zu, extra %zu => %s\n", nall, missing, extra,
         (missing == 0 && extra == 0) ? "COVERED EXACTLY" : "NOT COVERED");
  return (missing == 0 && extra == 0) ? 0 : 1;
}
