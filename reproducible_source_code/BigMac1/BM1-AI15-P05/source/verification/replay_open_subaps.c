/*
 * Independent lower-bound replay for the post-frontier Erdős #647 scan.
 *
 * This program deliberately does not use the discovery program's Montgomery,
 * Miller--Rabin, Pollard-rho, or cofactor-classification code.  It performs a
 * segmented exact division of every AP value by all primes <= SMALL_LIMIT.
 * A cell is cheaply killed only by the rigorous lower bound
 *
 *     tau(F) >= tau(removed small-prime part) * (2 if cofactor>1 else 1).
 *
 * Undecided cells are printed as HARD records.  The Python wrapper factors
 * those integers from scratch with an independent deterministic 64-bit
 * Miller--Rabin/Pollard-rho implementation and fails closed if any remains.
 */

#include <errno.h>
#include <inttypes.h>
#include <pthread.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define KMAX 16
#define SMALL_LIMIT 100000u
#define BLOCK 100000u
#define A_CONST UINT64_C(61573632120)

static const uint32_t A_PRIMES[9] = {2,3,5,7,11,13,17,19,23};
static const uint32_t A_EXPS[9] = {3,2,1,1,1,1,1,1,2};

typedef struct { uint32_t r, s; uint64_t B; } Pair;
typedef struct {
    uint64_t D;
    uint32_t tau_const;
    int nvar;
    uint32_t p[9], a[9];
    uint64_t root[9];
} Peel;

static Pair *pairs = NULL;
static int pair_count = 0, next_pair = 0;
static uint64_t u_lo = 0, u_hi = 0;
static uint32_t *small_primes = NULL, *a_inv = NULL, small_count = 0;
static pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
static uint64_t global_pairs = 0, global_cells = 0, global_hard = 0;
static uint64_t global_kills[KMAX + 1];

static void die(const char *msg) {
    fprintf(stderr, "FATAL: %s\n", msg);
    exit(2);
}

static uint64_t powmod(uint64_t b, uint64_t e, uint64_t m) {
    uint64_t out = 1;
    b %= m;
    while (e) {
        if (e & 1) out = (uint64_t)((__uint128_t)out * b % m);
        b = (uint64_t)((__uint128_t)b * b % m);
        e >>= 1;
    }
    return out;
}

static uint64_t inv_prime(uint64_t x, uint64_t p) {
    if (x % p == 0) die("inverse requested for nonunit");
    return powmod(x % p, p - 2, p);
}

static uint32_t valuation_abs(int64_t x, uint32_t p) {
    uint64_t y = x < 0 ? (uint64_t)(-(__int128)x) : (uint64_t)x;
    uint32_t e = 0;
    while (y % p == 0) { y /= p; e++; }
    return e;
}

static uint64_t positive_mod_i64(int64_t x, uint64_t p) {
    int64_t z = x % (int64_t)p;
    return (uint64_t)(z < 0 ? z + (int64_t)p : z);
}

static void compute_peel(int64_t c, Peel *out) {
    out->D = 1;
    out->tau_const = 1;
    out->nvar = 0;
    if (c == 0) die("unexpected zero AP constant");
    for (int j = 0; j < 9; j++) {
        uint32_t p = A_PRIMES[j], a = A_EXPS[j];
        uint32_t b = valuation_abs(c, p);
        uint64_t pa = 1;
        for (uint32_t t = 0; t < (b < a ? b : a); t++) pa *= p;
        out->D *= pa;
        if (b < a) {
            out->tau_const *= b + 1;
        } else {
            out->tau_const *= a + 1;
            uint64_t p_to_a = 1;
            for (uint32_t t = 0; t < a; t++) p_to_a *= p;
            int64_t c1 = c / (int64_t)p_to_a;
            uint64_t A1 = A_CONST / p_to_a;
            uint64_t cmod = positive_mod_i64(c1, p);
            int q = out->nvar++;
            out->p[q] = p;
            out->a[q] = a;
            out->root[q] = ((p - cmod) % p) * inv_prime(A1, p) % p;
        }
    }
}

static uint64_t first_congruent(uint64_t start, uint64_t root, uint64_t p) {
    uint64_t smod = start % p;
    return start + (root + p - smod) % p;
}

static uint64_t exact_F(uint64_t u, int64_t c) {
    __int128 z = (__int128)A_CONST * u + c;
    if (z <= 0 || z > INT64_MAX) die("AP value outside certified signed-64 domain");
    return (uint64_t)z;
}

static void *worker(void *unused) {
    (void)unused;
    uint64_t *rem = malloc((size_t)BLOCK * sizeof(uint64_t));
    uint64_t *tau_part = malloc((size_t)BLOCK * sizeof(uint64_t));
    uint8_t *alive = malloc((size_t)BLOCK);
    if (!rem || !tau_part || !alive) die("allocation failure");

    uint64_t local_pairs = 0, local_cells = 0, local_hard = 0;
    uint64_t local_kills[KMAX + 1] = {0};

    for (;;) {
        pthread_mutex_lock(&lock);
        int idx = next_pair < pair_count ? next_pair++ : -1;
        pthread_mutex_unlock(&lock);
        if (idx < 0) break;
        Pair P = pairs[idx];
        local_pairs++;

        Peel peel[KMAX + 1];
        for (int k = 1; k <= KMAX; k++) {
            int64_t c = (int64_t)P.B - k;
            compute_peel(c, &peel[k]);
        }

        for (uint64_t block_lo = u_lo; block_lo <= u_hi; block_lo += BLOCK) {
            uint64_t block_hi = block_lo + BLOCK - 1;
            if (block_hi > u_hi) block_hi = u_hi;
            uint32_t len = (uint32_t)(block_hi - block_lo + 1);
            memset(alive, 1, len);
            local_cells += len;

            for (int k = 1; k <= KMAX; k++) {
                int64_t c = (int64_t)P.B - k;
                Peel *pi = &peel[k];

                for (uint32_t i = 0; i < len; i++) if (alive[i]) {
                    uint64_t F = exact_F(block_lo + i, c);
                    if (F % pi->D != 0) die("constant peel does not divide AP value");
                    rem[i] = F / pi->D;
                    tau_part[i] = pi->tau_const;
                }

                for (int q = 0; q < pi->nvar; q++) {
                    uint64_t p = pi->p[q];
                    uint64_t first = first_congruent(block_lo, pi->root[q], p);
                    for (uint64_t u = first; u <= block_hi; u += p) {
                        uint32_t i = (uint32_t)(u - block_lo);
                        if (!alive[i]) continue;
                        uint32_t extra = 0;
                        while (rem[i] % p == 0) { rem[i] /= p; extra++; }
                        if (extra == 0) die("varying A-prime root had zero extra valuation");
                        uint32_t a = pi->a[q];
                        tau_part[i] = tau_part[i] / (a + 1) * (a + extra + 1);
                    }
                }

                for (uint32_t q = 0; q < small_count; q++) {
                    uint64_t p = small_primes[q];
                    uint64_t cmod = positive_mod_i64(c, p);
                    uint64_t root = ((p - cmod) % p) * (uint64_t)a_inv[q] % p;
                    uint64_t first = first_congruent(block_lo, root, p);
                    for (uint64_t u = first; u <= block_hi; u += p) {
                        uint32_t i = (uint32_t)(u - block_lo);
                        if (!alive[i]) continue;
                        uint32_t e = 0;
                        while (rem[i] % p == 0) { rem[i] /= p; e++; }
                        if (e == 0) die("ordinary prime root did not divide residual");
                        tau_part[i] *= e + 1;
                    }
                }

                uint64_t budget = (uint64_t)k + 2;
                for (uint32_t i = 0; i < len; i++) if (alive[i]) {
                    uint64_t lower = tau_part[i];
                    if (rem[i] > 1) lower *= 2;
                    if (lower > budget) {
                        alive[i] = 0;
                        local_kills[k]++;
                    }
                }
            }

            for (uint32_t i = 0; i < len; i++) if (alive[i]) {
                uint64_t u = block_lo + i;
                uint64_t n = exact_F(u, (int64_t)P.B);
                pthread_mutex_lock(&lock);
                printf("HARD r=%u s=%u u=%" PRIu64 " n=%" PRIu64 "\n",
                       P.r, P.s, u, n);
                fflush(stdout);
                pthread_mutex_unlock(&lock);
                local_hard++;
            }
        }
    }

    pthread_mutex_lock(&lock);
    global_pairs += local_pairs;
    global_cells += local_cells;
    global_hard += local_hard;
    for (int k = 1; k <= KMAX; k++) global_kills[k] += local_kills[k];
    pthread_mutex_unlock(&lock);

    free(rem); free(tau_part); free(alive);
    return NULL;
}

static void build_prime_table(void) {
    uint8_t *composite = calloc(SMALL_LIMIT + 1u, 1);
    if (!composite) die("prime-table allocation failure");
    for (uint32_t p = 2; (uint64_t)p * p <= SMALL_LIMIT; p++)
        if (!composite[p])
            for (uint32_t q = p * p; q <= SMALL_LIMIT; q += p) composite[q] = 1;
    small_primes = malloc(10000u * sizeof(uint32_t));
    a_inv = malloc(10000u * sizeof(uint32_t));
    if (!small_primes || !a_inv) die("prime-list allocation failure");
    for (uint32_t p = 2; p <= SMALL_LIMIT; p++) if (!composite[p]) {
        int divides_A = 0;
        for (int j = 0; j < 9; j++) if (p == A_PRIMES[j]) divides_A = 1;
        if (divides_A) continue;
        small_primes[small_count] = p;
        a_inv[small_count] = (uint32_t)inv_prime(A_CONST, p);
        small_count++;
    }
    free(composite);
}

int main(int argc, char **argv) {
    if (argc != 6) {
        fprintf(stderr, "usage: %s sieve_subaps.tsv u_lo u_hi threads expected_pairs\n", argv[0]);
        return 2;
    }
    errno = 0;
    u_lo = strtoull(argv[2], NULL, 10);
    u_hi = strtoull(argv[3], NULL, 10);
    int thread_count = atoi(argv[4]);
    int expected_pairs = atoi(argv[5]);
    if (errno || u_lo == 0 || u_hi < u_lo) die("invalid u interval");
    if (thread_count < 1 || thread_count > 64) die("thread count outside 1..64");

    FILE *in = fopen(argv[1], "r");
    if (!in) die("cannot open pair file");
    pairs = malloc((size_t)(expected_pairs + 1) * sizeof(Pair));
    if (!pairs) die("pair allocation failure");
    while (pair_count <= expected_pairs &&
           fscanf(in, "%u %u %" SCNu64,
                  &pairs[pair_count].r, &pairs[pair_count].s,
                  &pairs[pair_count].B) == 3) pair_count++;
    fclose(in);
    if (pair_count != expected_pairs) die("pair count mismatch");

    build_prime_table();
    fprintf(stderr, "independent replay: pairs=%d u=[%" PRIu64 ",%" PRIu64
                    "] threads=%d small_primes=%u\n",
            pair_count, u_lo, u_hi, thread_count, small_count);

    pthread_t threads[64];
    for (int j = 0; j < thread_count; j++)
        if (pthread_create(&threads[j], NULL, worker, NULL)) die("pthread_create failed");
    for (int j = 0; j < thread_count; j++) pthread_join(threads[j], NULL);

    uint64_t cheap = 0;
    for (int k = 1; k <= KMAX; k++) cheap += global_kills[k];
    printf("SUMMARY pairs=%" PRIu64 " cells=%" PRIu64
           " cheap_kills=%" PRIu64 " hard=%" PRIu64 "\n",
           global_pairs, global_cells, cheap, global_hard);
    printf("KILLS");
    for (int k = 1; k <= KMAX; k++) printf(" %d:%" PRIu64, k, global_kills[k]);
    printf("\n");

    free(pairs); free(small_primes); free(a_inv);
    return 0;
}
