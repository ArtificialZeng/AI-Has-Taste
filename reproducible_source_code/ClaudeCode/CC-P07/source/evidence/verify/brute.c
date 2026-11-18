/* brute K: enumerate ALL ordered sequences of K distinct cards of 52,
 * canonicalize each, count distinct canonical codes (orbit count). */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
static int cmp64(const void *a, const void *b) { uint64_t x = *(const uint64_t *)a, y = *(const uint64_t *)b; return x < y ? -1 : x > y; }
static uint64_t *buf; static size_t nb; static int K; static int seq[8]; static int usedc[52];
static void rec(int i) {
  if (i == K) {
    int sm[4] = {-1,-1,-1,-1}, rm[13], ns = 0, nr = 0; uint64_t code = 0;
    for (int t = 0; t < 13; t++) rm[t] = -1;
    for (int t = 0; t < K; t++) { int s = seq[t] / 13, r = seq[t] % 13; if (sm[s] < 0) sm[s] = ns++; if (rm[r] < 0) rm[r] = nr++; code = code * 64 + sm[s] * 13 + rm[r]; }
    buf[nb++] = code; return;
  }
  for (int c = 0; c < 52; c++) if (!usedc[c]) { usedc[c] = 1; seq[i] = c; rec(i + 1); usedc[c] = 0; }
}
int main(int argc, char **argv) {
  K = atoi(argv[1]); size_t tot = 1; for (int i = 0; i < K; i++) tot *= (52 - i);
  buf = malloc(tot * 8); rec(0); qsort(buf, nb, 8, cmp64);
  size_t u = 0; for (size_t i = 0; i < nb; i++) if (!i || buf[i] != buf[i - 1]) u++;
  printf("brute k=%d: %zu sequences, %zu distinct canonical patterns\n", K, nb, u); return 0;
}
