/* verify K FILE LO HI OUTCODES
 * Checks records [LO,HI) of FILE (18-byte records; HI=-1 means to the end):
 *   - not the all-255 "no witness" sentinel
 *   - 18 cards in 0..51, pairwise distinct
 *   - deal winnable by the verifier's own solver (vsolve.h)
 * and writes the canonical pattern code (uint64) of the first K cards of each
 * valid record to OUTCODES.  Canonical pattern: suits relabelled 0,1,.. in order
 * of first appearance, ranks relabelled 0,1,.. in order of first appearance;
 * code = sum over i of (s'_i*13+r'_i) * 64^(K-1-i). */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
#include "vsolve.h"

static uint64_t canon(const uint8_t *c, int K, int *already) {
  int sm[4], rm[13], ns = 0, nr = 0; uint64_t code = 0; int same = 1;
  for (int i = 0; i < 4; i++) sm[i] = -1;
  for (int i = 0; i < 13; i++) rm[i] = -1;
  for (int i = 0; i < K; i++) {
    int s = c[i] / 13, r = c[i] % 13;
    if (sm[s] < 0) sm[s] = ns++;
    if (rm[r] < 0) rm[r] = nr++;
    if (sm[s] != s || rm[r] != r) same = 0;
    code = code * 64 + (uint64_t)(sm[s] * 13 + rm[r]);
  }
  *already = same;
  return code;
}

int main(int argc, char **argv) {
  if (argc < 6) { fprintf(stderr, "usage: verify K FILE LO HI OUTCODES\n"); return 2; }
  int K = atoi(argv[1]);
  const char *fn = argv[2];
  long lo = atol(argv[3]), hi = atol(argv[4]);
  FILE *f = fopen(fn, "rb");
  if (!f) { perror(fn); return 2; }
  fseek(f, 0, SEEK_END); long sz = ftell(f);
  if (sz % 18) fprintf(stderr, "WARNING %s size %ld not a multiple of 18\n", fn, sz);
  long nrec = sz / 18;
  if (hi < 0 || hi > nrec) hi = nrec;
  if (lo > hi) lo = hi;
  fseek(f, lo * 18, SEEK_SET);
  FILE *out = fopen(argv[5], "wb");
  if (!out) { perror(argv[5]); return 2; }
  vs_init();
  long n = 0, sentinel = 0, invalid = 0, win = 0, lose = 0, canonical_prefix = 0;
  uint64_t maxnodes = 0;
  clock_t t0 = clock();
  uint8_t r[18];
  for (long i = lo; i < hi; i++) {
    if (fread(r, 1, 18, f) != 18) { fprintf(stderr, "short read at record %ld\n", i); invalid++; break; }
    n++;
    int all255 = 1, ok = 1;
    for (int j = 0; j < 18; j++) if (r[j] != 255) all255 = 0;
    if (all255) { sentinel++; if (sentinel <= 10) printf("SENTINEL %s rec %ld\n", fn, i); continue; }
    uint64_t seen = 0;
    for (int j = 0; j < 18; j++) {
      if (r[j] >= 52 || (seen >> r[j] & 1)) { ok = 0; break; }
      seen |= 1ULL << r[j];
    }
    if (!ok) {
      invalid++;
      if (invalid <= 10) { printf("INVALID %s rec %ld:", fn, i); for (int j = 0; j < 18; j++) printf(" %d", r[j]); printf("\n"); }
      continue;
    }
    uint64_t before = VS_nodes;
    int w = vs_solve(r, 18);
    if (VS_nodes - before > maxnodes) maxnodes = VS_nodes - before;
    if (w) win++;
    else {
      lose++;
      if (lose <= 10) { printf("NOT-WINNABLE %s rec %ld:", fn, i); for (int j = 0; j < 18; j++) printf(" %d", r[j]); printf("\n"); }
    }
    int already;
    uint64_t code = canon(r, K, &already);
    canonical_prefix += already;
    /* write code for every valid record, winnable or not; losers are reported
       separately and their codes are tagged with the top bit so they do not
       count as covered */
    if (!w) code |= 1ULL << 63;
    fwrite(&code, 8, 1, out);
  }
  fclose(out); fclose(f);
  double secs = (double)(clock() - t0) / CLOCKS_PER_SEC;
  printf("SUMMARY file=%s range=[%ld,%ld) records=%ld sentinel=%ld invalid=%ld winnable=%ld notwinnable=%ld "
         "prefix_literally_canonical=%ld nodes=%llu maxnodes=%llu tablefull=%llu cpu=%.1fs\n",
         fn, lo, hi, n, sentinel, invalid, win, lose, canonical_prefix,
         (unsigned long long)VS_nodes, (unsigned long long)maxnodes, (unsigned long long)VS_full, secs);
  return 0;
}
