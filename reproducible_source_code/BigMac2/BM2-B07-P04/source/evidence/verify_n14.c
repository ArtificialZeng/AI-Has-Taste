#include <errno.h>
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

/*
 * Exact verifier for the n=14, k in {3,5} Kasami cyclic-additive claim.
 *
 * Field encoding: the integer sum b_i 2^i encodes sum b_i alpha^i in
 * GF(2)[alpha]/(alpha^14 + alpha^5 + 1).  All arithmetic and transforms are
 * integer-only.  This program is deliberately self-contained: it first runs
 * Rabin's irreducibility test, certifies a generator of GF(2^14)^*, builds the
 * trace-pairing map, enumerates the two Delta sets, and then writes the full
 * Walsh spectra and all 32,764 normalized counts.
 */

enum { DEG = 14, Q = 1 << DEG, ORDER = Q - 1 };
static const uint32_t MODULUS = 0x4021u; /* X^14 + X^5 + 1 */
static const uint16_t REDUCTION = 0x0021u; /* X^14 = X^5 + 1 */
static const uint16_t GENERATOR = 0x0007u; /* 1 + alpha + alpha^2 */

static uint16_t exp_table[2 * ORDER];
static int16_t log_table[Q];
static uint8_t trace_table[Q];
static uint16_t dual_mask[Q];

static void fail(const char *message) {
    fprintf(stderr, "ERROR: %s\n", message);
    exit(1);
}

static int poly_degree(uint32_t a) {
    if (a == 0) return -1;
    return 31 - __builtin_clz(a);
}

static uint32_t poly_mod(uint32_t a, uint32_t f) {
    const int df = poly_degree(f);
    int da;
    while ((da = poly_degree(a)) >= df) a ^= f << (da - df);
    return a;
}

static uint32_t poly_gcd(uint32_t a, uint32_t b) {
    while (b != 0) {
        const uint32_t r = poly_mod(a, b);
        a = b;
        b = r;
    }
    return a;
}

static uint32_t poly_square_mod(uint32_t a, uint32_t f) {
    uint32_t square = 0;
    for (unsigned i = 0; i < DEG; ++i) {
        if ((a >> i) & 1u) square ^= 1u << (2u * i);
    }
    return poly_mod(square, f);
}

static void certify_irreducible(uint32_t *r2, uint32_t *r7,
                                uint32_t *r14, uint32_t *g2,
                                uint32_t *g7) {
    /* Rabin: X^(2^14)=X mod f, and for primes 2,7 dividing 14,
       gcd(X^(2^(14/p))-X,f)=1.  The relevant exponents are 7 and 2. */
    uint32_t r = 0x2u; /* X */
    *r2 = *r7 = *r14 = 0;
    for (unsigned j = 1; j <= DEG; ++j) {
        r = poly_square_mod(r, MODULUS);
        if (j == 2) *r2 = r;
        if (j == 7) *r7 = r;
        if (j == 14) *r14 = r;
    }
    *g2 = poly_gcd(*r2 ^ 0x2u, MODULUS);
    *g7 = poly_gcd(*r7 ^ 0x2u, MODULUS);
    if (*r14 != 0x2u || *g2 != 1u || *g7 != 1u)
        fail("Rabin irreducibility certificate failed");
}

static inline uint16_t gf_mul(uint16_t a, uint16_t b) {
    uint16_t result = 0;
    while (b != 0) {
        if (b & 1u) result ^= a;
        b >>= 1;
        const uint16_t carry = a & (1u << (DEG - 1));
        a = (uint16_t)((a << 1) & (Q - 1));
        if (carry) a ^= REDUCTION;
    }
    return result;
}

static uint16_t gf_pow(uint16_t a, uint32_t exponent) {
    uint16_t result = 1;
    while (exponent != 0) {
        if (exponent & 1u) result = gf_mul(result, a);
        a = gf_mul(a, a);
        exponent >>= 1;
    }
    return result;
}

static inline uint16_t gf_mul_log(uint16_t a, uint16_t b) {
    if (a == 0 || b == 0) return 0;
    return exp_table[(unsigned)log_table[a] + (unsigned)log_table[b]];
}

static void build_multiplicative_tables(uint16_t order_witness[4]) {
    uint8_t seen[Q];
    memset(seen, 0, sizeof(seen));
    for (unsigned i = 0; i < Q; ++i) log_table[i] = -1;

    uint16_t value = 1;
    for (unsigned i = 0; i < ORDER; ++i) {
        if (value == 0 || seen[value]) fail("generator orbit repeated early");
        seen[value] = 1;
        exp_table[i] = value;
        log_table[value] = (int16_t)i;
        value = gf_mul(value, GENERATOR);
    }
    if (value != 1) fail("generator orbit does not close at order 16383");
    for (unsigned x = 1; x < Q; ++x)
        if (!seen[x]) fail("generator orbit omits a nonzero field element");
    for (unsigned i = 0; i < ORDER; ++i)
        exp_table[i + ORDER] = exp_table[i];

    /* 16383 = 3 * 43 * 127.  These values explicitly certify exact order. */
    order_witness[0] = gf_pow(GENERATOR, ORDER);
    order_witness[1] = gf_pow(GENERATOR, ORDER / 3);
    order_witness[2] = gf_pow(GENERATOR, ORDER / 43);
    order_witness[3] = gf_pow(GENERATOR, ORDER / 127);
    if (order_witness[0] != 1 || order_witness[1] == 1 ||
        order_witness[2] == 1 || order_witness[3] == 1)
        fail("primitive-generator order certificate failed");

    /* Cross-check every log-table multiplication against polynomial reduction. */
    for (unsigned i = 0; i < ORDER; ++i) {
        const uint16_t a = exp_table[i];
        const uint16_t b = exp_table[(7919u * i + 1237u) % ORDER];
        if (gf_mul(a, b) != gf_mul_log(a, b))
            fail("log multiplication disagrees with polynomial multiplication");
    }
}

static uint8_t absolute_trace(uint16_t x) {
    uint16_t sum = 0;
    uint16_t power = x;
    for (unsigned i = 0; i < DEG; ++i) {
        sum ^= power;
        power = gf_mul(power, power);
    }
    if (sum > 1) fail("absolute trace did not land in GF(2)");
    return (uint8_t)sum;
}

static void build_trace_pairing(void) {
    unsigned trace_zeroes = 0;
    uint8_t seen_dual[Q];
    memset(seen_dual, 0, sizeof(seen_dual));

    for (unsigned x = 0; x < Q; ++x) {
        trace_table[x] = absolute_trace((uint16_t)x);
        if (trace_table[x] == 0) ++trace_zeroes;
    }
    if (trace_zeroes != Q / 2) fail("absolute trace is not balanced");

    for (unsigned a = 0; a < Q; ++a) {
        uint16_t mask = 0;
        for (unsigned i = 0; i < DEG; ++i) {
            const uint16_t basis = (uint16_t)(1u << i);
            if (trace_table[gf_mul((uint16_t)a, basis)]) mask |= basis;
        }
        dual_mask[a] = mask;
        if (seen_dual[mask]) fail("trace-pairing dual map is not injective");
        seen_dual[mask] = 1;
    }
}

static void fwht(int32_t values[Q]) {
    for (unsigned half = 1; half < Q; half <<= 1) {
        for (unsigned base = 0; base < Q; base += 2 * half) {
            for (unsigned j = 0; j < half; ++j) {
                const int32_t u = values[base + j];
                const int32_t v = values[base + half + j];
                values[base + j] = u + v;
                values[base + half + j] = u - v;
            }
        }
    }
}

struct delta_data {
    uint8_t member[Q];
    uint8_t multiplicity[Q];
    uint16_t elements[Q / 2];
    int32_t spectrum[Q];
    unsigned size;
};

static void construct_delta(unsigned k, uint32_t exponent,
                            struct delta_data *data) {
    memset(data, 0, sizeof(*data));
    for (unsigned t = 0; t < Q; ++t) {
        const uint16_t value = (uint16_t)(
            gf_pow((uint16_t)t, exponent) ^
            gf_pow((uint16_t)(t ^ 1u), exponent) ^ 1u);
        data->member[value] = 1;
        if (data->multiplicity[value] == UINT8_MAX)
            fail("Delta multiplicity overflow");
        ++data->multiplicity[value];
    }
    for (unsigned x = 0; x < Q; ++x) {
        if (data->member[x]) {
            if (data->size >= Q / 2) fail("Delta image has more than 8192 values");
            data->elements[data->size++] = (uint16_t)x;
            if (data->multiplicity[x] != 2)
                fail("Delta map is not exactly two-to-one on its image");
        } else if (data->multiplicity[x] != 0) {
            fail("Delta membership/multiplicity inconsistency");
        }
    }
    if (data->size != Q / 2) fail("Delta set does not have size 8192");

    int32_t standard_transform[Q];
    for (unsigned x = 0; x < Q; ++x)
        standard_transform[x] = data->member[x] ? 1 : 0;
    fwht(standard_transform);
    for (unsigned a = 0; a < Q; ++a)
        data->spectrum[a] = standard_transform[dual_mask[a]];
    if (data->spectrum[0] != (int32_t)data->size)
        fail("zero Walsh coefficient does not equal Delta size");

    int64_t parseval = 0;
    for (unsigned a = 0; a < Q; ++a)
        parseval += (int64_t)data->spectrum[a] * data->spectrum[a];
    if (parseval != (int64_t)Q * data->size)
        fail("Walsh spectrum fails Parseval identity");

    /* Direct character sums at fixed encoded a values cross-check the dual FWHT. */
    static const uint16_t checks[] = {
        0x0000u, 0x0001u, 0x0002u, 0x0003u, 0x0007u,
        0x0123u, 0x2000u, 0x2aabu, 0x3fffu
    };
    for (unsigned j = 0; j < sizeof(checks) / sizeof(checks[0]); ++j) {
        const uint16_t a = checks[j];
        int32_t direct = 0;
        for (unsigned ix = 0; ix < data->size; ++ix) {
            const uint16_t x = data->elements[ix];
            direct += trace_table[gf_mul(a, x)] ? -1 : 1;
        }
        if (direct != data->spectrum[a]) {
            fprintf(stderr, "k=%u, a=0x%04x: direct=%d transform=%d\n",
                    k, a, direct, data->spectrum[a]);
            fail("direct Walsh check failed");
        }
    }
}

static uint64_t direct_triple_count(const struct delta_data *data,
                                    uint16_t rho) {
    uint16_t rho_y[Q / 2];
    uint16_t one_rho_z[Q / 2];
    for (unsigned i = 0; i < data->size; ++i) {
        rho_y[i] = gf_mul_log(rho, data->elements[i]);
        one_rho_z[i] = gf_mul_log((uint16_t)(rho ^ 1u), data->elements[i]);
    }
    uint64_t count = 0;
    for (unsigned iz = 0; iz < data->size; ++iz) {
        const uint16_t shift = one_rho_z[iz];
        for (unsigned iy = 0; iy < data->size; ++iy)
            count += data->member[rho_y[iy] ^ shift];
    }
    return count;
}

static int64_t cube_i64(int64_t x) { return x * x * x; }

static int verify_one_k(FILE *certificate, unsigned k, uint32_t exponent,
                        struct delta_data *data, uint16_t *bad_rho,
                        int64_t *bad_count, int64_t *min_count,
                        int64_t *max_count) {
    construct_delta(k, exponent, data);
    fprintf(certificate, "BEGIN_SPECTRUM\t%u\n", k);
    fprintf(certificate, "# columns: S, k, encoded_a_decimal, encoded_a_hex, S_k(a)\n");
    for (unsigned a = 0; a < Q; ++a)
        fprintf(certificate, "S\t%u\t%u\t0x%04x\t%d\n",
                k, a, a, data->spectrum[a]);
    fprintf(certificate, "END_SPECTRUM\t%u\n", k);
    fprintf(certificate, "BEGIN_COUNTS\t%u\n", k);
    fprintf(certificate,
            "# columns: N, k, encoded_rho_decimal, encoded_rho_hex, "
            "nonzero_character_sum, full_character_sum, exact_count\n");

    const int64_t zero_term = cube_i64((int64_t)data->size);
    const int64_t target = INT64_C(33554432);
    *min_count = INT64_MAX;
    *max_count = INT64_MIN;
    *bad_rho = 0;
    *bad_count = target;

    unsigned processed = 0;
    for (unsigned rho = 0; rho < Q; ++rho) {
        if (rho == 0 || rho == 1) continue;
        const unsigned lr = (unsigned)log_table[rho];
        const unsigned ls = (unsigned)log_table[rho ^ 1u];
        int64_t correlation = 0;
        for (unsigned j = 0; j < ORDER; ++j) {
            const int64_t u = data->spectrum[exp_table[j]];
            const int64_t v = data->spectrum[exp_table[j + lr]];
            const int64_t w = data->spectrum[exp_table[j + ls]];
            correlation += u * v * w;
        }
        const int64_t total = zero_term + correlation;
        if (total % Q != 0) fail("character sum is not divisible by field size");
        const int64_t count = total / Q;
        if (count < *min_count) *min_count = count;
        if (count > *max_count) *max_count = count;
        fprintf(certificate, "N\t%u\t%u\t0x%04x\t%" PRId64
                             "\t%" PRId64 "\t%" PRId64 "\n",
                k, rho, rho, correlation, total, count);
        if (count != target && *bad_rho == 0) {
            *bad_rho = (uint16_t)rho;
            *bad_count = count;
        }
        ++processed;
        if ((processed & 2047u) == 0)
            fprintf(stdout, "k=%u exact transform: %u/16382 rho values\n",
                    k, processed);
    }
    if (processed != Q - 2) fail("did not cover all admissible rho values");
    fprintf(certificate, "END_COUNTS\t%u\n", k);

    if (*bad_rho != 0) {
        const uint64_t direct = direct_triple_count(data, *bad_rho);
        fprintf(certificate,
                "COUNTEREXAMPLE_CHECK\t%u\t%u\t0x%04x\t%" PRIu64 "\n",
                k, *bad_rho, *bad_rho, direct);
        if (direct != (uint64_t)*bad_count)
            fail("direct count does not match transform counterexample");
        return 0;
    }

    /* Independent O(|Delta|^2) enumeration at two fixed rho values. */
    static const uint16_t spot_rho[] = {0x0002u, 0x2000u};
    for (unsigned j = 0; j < sizeof(spot_rho) / sizeof(spot_rho[0]); ++j) {
        const uint64_t direct = direct_triple_count(data, spot_rho[j]);
        fprintf(certificate, "DIRECT_CHECK\t%u\t%u\t0x%04x\t%" PRIu64 "\n",
                k, spot_rho[j], spot_rho[j], direct);
        if (direct != (uint64_t)target) fail("direct triple-count spot check failed");
    }
    return 1;
}

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "usage: %s CERTIFICATE.tsv\n", argv[0]);
        return 64;
    }
    const clock_t started = clock();

    uint32_t r2, r7, r14, g2, g7;
    certify_irreducible(&r2, &r7, &r14, &g2, &g7);
    uint16_t order_witness[4];
    build_multiplicative_tables(order_witness);
    build_trace_pairing();

    FILE *certificate = fopen(argv[1], "w");
    if (!certificate) {
        fprintf(stderr, "cannot open %s: %s\n", argv[1], strerror(errno));
        return 1;
    }
    fprintf(certificate, "# DM07-04 exact n=14 certificate version 1\n");
    fprintf(certificate, "# arithmetic: integer-only GF(2) polynomial arithmetic\n");
    fprintf(certificate, "# field_order: 16384\n");
    fprintf(certificate, "# modulus_bits: 0x%04x\n", MODULUS);
    fprintf(certificate, "# modulus: X^14 + X^5 + 1\n");
    fprintf(certificate,
            "# basis_encoding: integer sum(b_i*2^i) = sum(b_i*alpha^i), 0<=i<14\n");
    fprintf(certificate,
            "# Rabin: X^(2^2)=0x%04x; gcd(remainder+X,p)=0x%04x\n",
            r2, g2);
    fprintf(certificate,
            "# Rabin: X^(2^7)=0x%04x; gcd(remainder+X,p)=0x%04x\n",
            r7, g7);
    fprintf(certificate, "# Rabin: X^(2^14)=0x%04x (=X)\n", r14);
    fprintf(certificate, "# multiplicative_generator: 0x%04x\n", GENERATOR);
    fprintf(certificate,
            "# generator powers e=16383,5461,381,129: 0x%04x 0x%04x 0x%04x 0x%04x\n",
            order_witness[0], order_witness[1], order_witness[2],
            order_witness[3]);
    fprintf(certificate,
            "# formula: 16384*N_k(rho)=sum_a S_k(a)S_k(a*rho)S_k(a*(1+rho))\n");

    struct delta_data *data = malloc(sizeof(*data));
    if (!data) fail("allocation failed");
    uint16_t bad_rho[2];
    int64_t bad_count[2], min_count[2], max_count[2];

    fprintf(stdout,
            "field p=X^14+X^5+1 (0x%04x): Rabin remainders "
            "r2=0x%04x r7=0x%04x r14=0x%04x, gcds=%u,%u\n",
            MODULUS, r2, r7, r14, g2, g7);
    fprintf(stdout,
            "generator 0x%04x order witnesses: %04x %04x %04x %04x\n",
            GENERATOR, order_witness[0], order_witness[1],
            order_witness[2], order_witness[3]);

    const int ok3 = verify_one_k(certificate, 3, 57, data, &bad_rho[0],
                                 &bad_count[0], &min_count[0], &max_count[0]);
    fprintf(stdout,
            "k=3: |Delta|=%u, all rho covered, count range=[%" PRId64
            ",%" PRId64 "]%s\n",
            data->size, min_count[0], max_count[0],
            ok3 ? ", direct checks passed" : ", COUNTEREXAMPLE");

    const int ok5 = verify_one_k(certificate, 5, 993, data, &bad_rho[1],
                                 &bad_count[1], &min_count[1], &max_count[1]);
    fprintf(stdout,
            "k=5: |Delta|=%u, all rho covered, count range=[%" PRId64
            ",%" PRId64 "]%s\n",
            data->size, min_count[1], max_count[1],
            ok5 ? ", direct checks passed" : ", COUNTEREXAMPLE");

    fprintf(certificate,
            "SUMMARY\tk3_delta=8192\tk3_min=%" PRId64
            "\tk3_max=%" PRId64 "\tk5_delta=8192\tk5_min=%" PRId64
            "\tk5_max=%" PRId64 "\tstatus=%s\n",
            min_count[0], max_count[0], min_count[1], max_count[1],
            (ok3 && ok5) ? "PROVED_FINITE_ASSERTION" : "DISPROVED_FINITE_ASSERTION");
    if (fclose(certificate) != 0) fail("failed while closing certificate");
    free(data);

    const double seconds = (double)(clock() - started) / CLOCKS_PER_SEC;
    fprintf(stdout, "certificate=%s\n", argv[1]);
    fprintf(stdout, "cpu_seconds=%.3f\n", seconds);
    fprintf(stdout, "FINAL_STATUS=%s\n",
            (ok3 && ok5) ? "PROVED_FINITE_ASSERTION" : "DISPROVED_FINITE_ASSERTION");
    return 0;
}
