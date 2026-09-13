#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * Independent checker for n14_certificate.tsv.
 *
 * This intentionally does not reuse verify_n14.c's shift-and-reduce
 * multiplication, primitive generator, logarithm table, or FWHT computation.
 * Multiplication is carryless-product followed by polynomial long division.
 * Irreducibility is checked by exhaustive absence of factors of degree <= 7.
 * Every saved Walsh coefficient is recomputed as a direct character sum, and
 * every saved rho correlation is recomputed using linear multiplication maps.
 */

enum { DEG = 14, Q = 1 << DEG };
static const uint32_t MODULUS = 0x4021u;

static int32_t saved_spectrum[2][Q];
static int64_t saved_correlation[2][Q];
static int64_t saved_total[2][Q];
static int64_t saved_count[2][Q];
static uint8_t seen_spectrum[2][Q];
static uint8_t seen_count[2][Q];
static uint8_t member[2][Q];
static uint8_t multiplicity[2][Q];
static uint16_t elements[2][Q / 2];
static uint8_t trace_value[Q];

static void fail(const char *message) {
    fprintf(stderr, "AUDIT_ERROR: %s\n", message);
    exit(1);
}

static int poly_degree(uint32_t p) {
    int degree = -1;
    while (p != 0) {
        ++degree;
        p >>= 1;
    }
    return degree;
}

static uint32_t polynomial_remainder(uint32_t dividend, uint32_t divisor) {
    const int divisor_degree = poly_degree(divisor);
    while (poly_degree(dividend) >= divisor_degree) {
        const int shift = poly_degree(dividend) - divisor_degree;
        dividend ^= divisor << shift;
    }
    return dividend;
}

static void certify_irreducible_by_trial_factors(void) {
    unsigned candidates = 0;
    /* A reducible degree-14 polynomial has a factor of degree at most 7.
       Constant term 1 forces every factor to have constant term 1. */
    for (unsigned degree = 1; degree <= 7; ++degree) {
        const uint32_t monic = 1u << degree;
        const uint32_t middle_limit = 1u << (degree - 1);
        for (uint32_t middle = 0; middle < middle_limit; ++middle) {
            const uint32_t candidate = monic | (middle << 1) | 1u;
            ++candidates;
            if (polynomial_remainder(MODULUS, candidate) == 0) {
                fprintf(stderr, "factor found: 0x%x\n", candidate);
                fail("modulus is reducible");
            }
        }
    }
    if (candidates != 127) fail("trial-factor domain coverage error");
}

static uint16_t gf_mul(uint16_t a, uint16_t b) {
    uint32_t carryless_product = 0;
    for (unsigned i = 0; i < DEG; ++i)
        if ((b >> i) & 1u) carryless_product ^= (uint32_t)a << i;
    return (uint16_t)polynomial_remainder(carryless_product, MODULUS);
}

static uint16_t gf_pow(uint16_t base, uint32_t exponent) {
    uint16_t answer = 1;
    while (exponent != 0) {
        if (exponent & 1u) answer = gf_mul(answer, base);
        base = gf_mul(base, base);
        exponent >>= 1;
    }
    return answer;
}

static uint8_t absolute_trace(uint16_t a) {
    uint16_t sum = 0;
    uint16_t conjugate = a;
    for (unsigned j = 0; j < DEG; ++j) {
        sum ^= conjugate;
        conjugate = gf_mul(conjugate, conjugate);
    }
    if (sum != 0 && sum != 1) fail("trace is not in the prime field");
    return (uint8_t)sum;
}

static int k_index(unsigned k) {
    if (k == 3) return 0;
    if (k == 5) return 1;
    return -1;
}

static void parse_certificate(const char *path) {
    FILE *input = fopen(path, "r");
    if (!input) fail("cannot open certificate");
    char line[512];
    unsigned spectrum_rows[2] = {0, 0};
    unsigned count_rows[2] = {0, 0};
    unsigned direct_rows[2] = {0, 0};
    unsigned line_number = 0;

    while (fgets(line, sizeof(line), input)) {
        ++line_number;
        if (strchr(line, '\n') == NULL && !feof(input))
            fail("certificate line exceeds parser buffer");
        if (line[0] == '#' || line[0] == '\n') continue;
        if (line[0] == 'S' && line[1] == '\t') {
            unsigned k, encoded, encoded_hex;
            int value;
            char extra;
            const int fields = sscanf(line, "S\t%u\t%u\t0x%x\t%d %c",
                                      &k, &encoded, &encoded_hex, &value, &extra);
            const int ki = k_index(k);
            if (fields != 4 || ki < 0 || encoded >= Q || encoded_hex != encoded)
                fail("malformed spectrum row");
            if (seen_spectrum[ki][encoded]) fail("duplicate spectrum row");
            seen_spectrum[ki][encoded] = 1;
            saved_spectrum[ki][encoded] = value;
            ++spectrum_rows[ki];
        } else if (line[0] == 'N' && line[1] == '\t') {
            unsigned k, encoded, encoded_hex;
            int64_t correlation, total, count;
            char extra;
            const int fields = sscanf(
                line, "N\t%u\t%u\t0x%x\t%" SCNd64 "\t%" SCNd64
                      "\t%" SCNd64 " %c",
                &k, &encoded, &encoded_hex, &correlation, &total, &count, &extra);
            const int ki = k_index(k);
            if (fields != 6 || ki < 0 || encoded >= Q || encoded < 2 ||
                encoded_hex != encoded)
                fail("malformed count row");
            if (seen_count[ki][encoded]) fail("duplicate count row");
            seen_count[ki][encoded] = 1;
            saved_correlation[ki][encoded] = correlation;
            saved_total[ki][encoded] = total;
            saved_count[ki][encoded] = count;
            ++count_rows[ki];
        } else if (strncmp(line, "DIRECT_CHECK\t", 13) == 0) {
            unsigned k, encoded, encoded_hex;
            uint64_t count;
            char extra;
            const int fields = sscanf(line,
                "DIRECT_CHECK\t%u\t%u\t0x%x\t%" SCNu64 " %c",
                &k, &encoded, &encoded_hex, &count, &extra);
            const int ki = k_index(k);
            if (fields != 4 || ki < 0 || encoded < 2 || encoded >= Q ||
                encoded_hex != encoded || count != UINT64_C(33554432))
                fail("malformed or failed direct-check row");
            ++direct_rows[ki];
        } else if (strncmp(line, "BEGIN_", 6) == 0 ||
                   strncmp(line, "END_", 4) == 0 ||
                   strncmp(line, "SUMMARY\t", 8) == 0) {
            continue;
        } else {
            fprintf(stderr, "unrecognized certificate line %u: %s",
                    line_number, line);
            fail("unrecognized certificate row");
        }
    }
    if (ferror(input) || fclose(input) != 0) fail("certificate read error");

    for (int ki = 0; ki < 2; ++ki) {
        if (spectrum_rows[ki] != Q || count_rows[ki] != Q - 2 ||
            direct_rows[ki] != 2)
            fail("certificate row count is incomplete");
        for (unsigned a = 0; a < Q; ++a)
            if (!seen_spectrum[ki][a]) fail("missing encoded spectrum value");
        for (unsigned rho = 2; rho < Q; ++rho)
            if (!seen_count[ki][rho]) fail("missing encoded rho value");
    }
}

static void build_trace_table(void) {
    unsigned zeroes = 0;
    for (unsigned a = 0; a < Q; ++a) {
        trace_value[a] = absolute_trace((uint16_t)a);
        zeroes += trace_value[a] == 0;
    }
    if (zeroes != Q / 2) fail("trace is not balanced");
}

static void construct_delta(int ki, uint32_t exponent) {
    unsigned size = 0;
    for (unsigned t = 0; t < Q; ++t) {
        const uint16_t delta = (uint16_t)(gf_pow((uint16_t)t, exponent) ^
            gf_pow((uint16_t)(t ^ 1u), exponent) ^ 1u);
        member[ki][delta] = 1;
        ++multiplicity[ki][delta];
    }
    for (unsigned x = 0; x < Q; ++x) {
        if (member[ki][x]) {
            if (size >= Q / 2 || multiplicity[ki][x] != 2)
                fail("Delta image size/multiplicity failure");
            elements[ki][size++] = (uint16_t)x;
        } else if (multiplicity[ki][x] != 0) {
            fail("Delta membership inconsistency");
        }
    }
    if (size != Q / 2) fail("Delta does not have 8192 elements");
}

static void multiplication_basis(uint16_t multiplier, uint16_t basis[DEG]) {
    for (unsigned i = 0; i < DEG; ++i)
        basis[i] = gf_mul(multiplier, (uint16_t)(1u << i));
}

static inline uint16_t extend_linear_map(unsigned encoded,
                                         const uint16_t basis[DEG],
                                         const uint16_t prior[Q]) {
    const unsigned bit = __builtin_ctz(encoded);
    const unsigned without_bit = encoded & (encoded - 1u);
    return (uint16_t)(prior[without_bit] ^ basis[bit]);
}

static void recompute_all_spectra_directly(void) {
    uint16_t products[Q];
    uint16_t basis[DEG];
    products[0] = 0;
    for (unsigned a = 0; a < Q; ++a) {
        multiplication_basis((uint16_t)a, basis);
        int32_t sum3 = member[0][0] ? 1 : 0;
        int32_t sum5 = member[1][0] ? 1 : 0;
        for (unsigned x = 1; x < Q; ++x) {
            products[x] = extend_linear_map(x, basis, products);
            const int32_t sign = trace_value[products[x]] ? -1 : 1;
            sum3 += member[0][x] ? sign : 0;
            sum5 += member[1][x] ? sign : 0;
        }
        if (sum3 != saved_spectrum[0][a] || sum5 != saved_spectrum[1][a]) {
            fprintf(stderr,
                    "spectrum mismatch a=0x%04x: got (%d,%d), saved (%d,%d)\n",
                    a, sum3, sum5, saved_spectrum[0][a], saved_spectrum[1][a]);
            fail("direct spectrum reconstruction disagrees with certificate");
        }
    }
}

static void recompute_all_correlations(void) {
    uint16_t product_rho[Q];
    uint16_t product_one_rho[Q];
    uint16_t basis_rho[DEG];
    uint16_t basis_one_rho[DEG];
    const int64_t target_total = INT64_C(549755813888);
    const int64_t target_count = INT64_C(33554432);

    product_rho[0] = 0;
    product_one_rho[0] = 0;
    for (unsigned rho = 2; rho < Q; ++rho) {
        multiplication_basis((uint16_t)rho, basis_rho);
        multiplication_basis((uint16_t)(rho ^ 1u), basis_one_rho);
        int64_t full3 = (int64_t)saved_spectrum[0][0] *
                        saved_spectrum[0][0] * saved_spectrum[0][0];
        int64_t full5 = (int64_t)saved_spectrum[1][0] *
                        saved_spectrum[1][0] * saved_spectrum[1][0];
        for (unsigned a = 1; a < Q; ++a) {
            product_rho[a] = extend_linear_map(a, basis_rho, product_rho);
            product_one_rho[a] =
                extend_linear_map(a, basis_one_rho, product_one_rho);
            full3 += (int64_t)saved_spectrum[0][a] *
                     saved_spectrum[0][product_rho[a]] *
                     saved_spectrum[0][product_one_rho[a]];
            full5 += (int64_t)saved_spectrum[1][a] *
                     saved_spectrum[1][product_rho[a]] *
                     saved_spectrum[1][product_one_rho[a]];
        }
        const int64_t full[2] = {full3, full5};
        for (int ki = 0; ki < 2; ++ki) {
            const int64_t correlation = full[ki] - target_total;
            if (full[ki] != target_total || full[ki] % Q != 0 ||
                full[ki] / Q != target_count ||
                saved_correlation[ki][rho] != correlation ||
                saved_total[ki][rho] != full[ki] ||
                saved_count[ki][rho] != full[ki] / Q) {
                fprintf(stderr,
                        "rho=0x%04x k=%d: corr=%" PRId64
                        " full=%" PRId64 " count=%" PRId64 "\n",
                        rho, ki == 0 ? 3 : 5, correlation, full[ki], full[ki] / Q);
                fail("full correlation/count audit failed");
            }
        }
    }
}

static uint64_t direct_count(int ki, uint16_t rho) {
    uint16_t first[Q / 2];
    uint16_t second[Q / 2];
    for (unsigned j = 0; j < Q / 2; ++j) {
        first[j] = gf_mul(rho, elements[ki][j]);
        second[j] = gf_mul((uint16_t)(rho ^ 1u), elements[ki][j]);
    }
    uint64_t count = 0;
    for (unsigned z = 0; z < Q / 2; ++z)
        for (unsigned y = 0; y < Q / 2; ++y)
            count += member[ki][first[y] ^ second[z]];
    return count;
}

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "usage: %s CERTIFICATE.tsv\n", argv[0]);
        return 64;
    }
    certify_irreducible_by_trial_factors();
    parse_certificate(argv[1]);
    build_trace_table();
    construct_delta(0, 57);
    construct_delta(1, 993);
    recompute_all_spectra_directly();
    recompute_all_correlations();

    /* Held-out direct checks: neither rho occurs among the producer's spots. */
    static const uint16_t held_out[] = {0x1555u, 0x3ffeu};
    for (int ki = 0; ki < 2; ++ki) {
        for (unsigned j = 0; j < sizeof(held_out) / sizeof(held_out[0]); ++j) {
            const uint64_t count = direct_count(ki, held_out[j]);
            printf("held_out_direct k=%d rho=0x%04x count=%" PRIu64 "\n",
                   ki == 0 ? 3 : 5, held_out[j], count);
            if (count != UINT64_C(33554432))
                fail("held-out direct count failed");
        }
    }

    printf("trial_factor_candidates=127\n");
    printf("certificate_spectrum_rows=32768\n");
    printf("certificate_count_rows=32764\n");
    printf("delta_sizes=8192,8192; all image multiplicities=2\n");
    printf("direct_spectra_recomputed=32768\n");
    printf("full_correlations_recomputed=32764\n");
    printf("AUDIT_STATUS=PASS\n");
    return 0;
}
