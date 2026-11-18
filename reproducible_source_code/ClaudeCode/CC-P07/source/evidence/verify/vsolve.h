/* Independent Late Binding solver (verifier's own code).
 * State = sequence of top cards v[0..n-1], card c in 0..51, suit c/13, rank c%13.
 * Moves (Knuth ex. 7.2.2.2-484, 'graph quenching'):
 *   if v[k] ~ v[k+1]: delete v[k]          (pile k+1 placed on pile k)
 *   if v[l] ~ v[l+3]: v[l] := v[l+3], delete v[l+3]  (pile l+3 placed on pile l)
 * Win iff length 1 reachable.
 * Memoized DFS: the table stores only states proven LOSING (a state is stored only
 * after all its successors were explored without a win). The table is an
 * optimization only; if it is full we simply stop inserting. */
#ifndef VSOLVE_H
#define VSOLVE_H
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

static uint8_t VS_adj[64][64];

static void vs_init_adj(void) {
  for (int a = 0; a < 64; a++)
    for (int b = 0; b < 64; b++)
      VS_adj[a][b] = (a < 52 && b < 52 && (a / 13 == b / 13 || a % 13 == b % 13)) ? 1 : 0;
}

#define VS_LOGSZ 22
#define VS_SZ (1u << VS_LOGSZ)
#define VS_MAXLOAD ((VS_SZ / 10) * 7)
typedef struct { uint64_t a, b; uint32_t stamp; } vs_ent;
static vs_ent *VS_tab;
static uint32_t VS_stamp = 0;
static uint32_t VS_count = 0;
static uint64_t VS_nodes = 0;     /* states expanded, total */
static uint64_t VS_full = 0;      /* times insertion skipped because table full */

static void vs_init(void) {
  vs_init_adj();
  VS_tab = (vs_ent *)calloc(VS_SZ, sizeof(vs_ent));
  VS_stamp = 0;
}

static inline void vs_pack(const uint8_t *v, int n, uint64_t *a, uint64_t *b) {
  uint64_t x = 0, y = 0;
  for (int i = 0; i < 10; i++) x = (x << 6) | (i < n ? v[i] : 63);
  for (int i = 10; i < 18; i++) y = (y << 6) | (i < n ? v[i] : 63);
  *a = x; *b = y;
}

static inline uint32_t vs_hash(uint64_t a, uint64_t b) {
  uint64_t h = a * 0x9E3779B97F4A7C15ULL ^ (b + 0x632BE59BD9B4E019ULL) * 0xC2B2AE3D27D4EB4FULL;
  h ^= h >> 29; h *= 0xBF58476D1CE4E5B9ULL; h ^= h >> 32;
  return (uint32_t)h & (VS_SZ - 1);
}

static inline int vs_lookup(uint64_t a, uint64_t b) {
  uint32_t h = vs_hash(a, b);
  for (;;) {
    vs_ent *e = &VS_tab[h];
    if (e->stamp != VS_stamp) return 0;
    if (e->a == a && e->b == b) return 1;
    h = (h + 1) & (VS_SZ - 1);
  }
}

static inline void vs_insert(uint64_t a, uint64_t b) {
  if (VS_count >= VS_MAXLOAD) { VS_full++; return; }
  uint32_t h = vs_hash(a, b);
  for (;;) {
    vs_ent *e = &VS_tab[h];
    if (e->stamp != VS_stamp) { e->a = a; e->b = b; e->stamp = VS_stamp; VS_count++; return; }
    if (e->a == a && e->b == b) return;
    h = (h + 1) & (VS_SZ - 1);
  }
}

#ifndef VS_PRUNE
#define VS_PRUNE 1
#endif
static uint64_t VS_pruned = 0;
/* Necessary condition for winnability: the compatibility graph (same suit or
 * same rank) on the current top cards must be connected. Reason: a card leaves
 * the sequence only when a compatible card is placed on it, the surviving card
 * is the compatible one, and cards never change; so each connected component
 * keeps at least one card forever. */
static inline int vs_connected(const uint8_t *v, int n) {
  uint32_t S = 1u << (v[0] / 13), R = 1u << (v[0] % 13);
  uint32_t done = 1, all = (1u << n) - 1;
  int changed = 1;
  while (changed) {
    changed = 0;
    for (int i = 1; i < n; i++)
      if (!(done >> i & 1)) {
        int s = v[i] / 13, r = v[i] % 13;
        if ((S >> s & 1) || (R >> r & 1)) { done |= 1u << i; S |= 1u << s; R |= 1u << r; changed = 1; }
      }
  }
  return done == all;
}
static int vs_dfs(const uint8_t *v, int n) {
  if (n == 1) return 1;
  if (n == 2) return VS_adj[v[0]][v[1]];
  if (VS_PRUNE && !vs_connected(v, n)) { VS_pruned++; return 0; }
  uint64_t a, b;
  vs_pack(v, n, &a, &b);
  if (vs_lookup(a, b)) return 0;
  VS_nodes++;
  uint8_t w[18];
  /* move order: left to right; at each k the 1-step capture before the 3-step */
  for (int k = 0; k + 1 < n; k++) {
    if (VS_adj[v[k]][v[k + 1]]) {
      /* pile k+1 onto pile k: delete v[k] */
      memcpy(w, v, k);
      memcpy(w + k, v + k + 1, n - k - 1);
      if (vs_dfs(w, n - 1)) return 1;
    }
    if (k + 3 < n && VS_adj[v[k]][v[k + 3]]) {
      /* pile k+3 onto pile k */
      memcpy(w, v, n);
      w[k] = v[k + 3];
      memmove(w + k + 3, v + k + 4, n - k - 4);
      if (vs_dfs(w, n - 1)) return 1;
    }
  }
  vs_insert(a, b);
  return 0;
}

/* returns 1 if winnable */
static int vs_solve(const uint8_t *deal, int n) {
  VS_stamp++;
  if (VS_stamp == 0) { memset(VS_tab, 0, (size_t)VS_SZ * sizeof(vs_ent)); VS_stamp = 1; }
  VS_count = 0;
  return vs_dfs(deal, n);
}
#endif
