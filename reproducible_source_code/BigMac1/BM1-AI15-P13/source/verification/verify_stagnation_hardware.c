/* Independent hardware check of certificates/binary64_stagnation.json.
 * Compile without contraction or fast-math; this verifier checks the host is
 * binary64 and in round-to-nearest mode before running the trace.
 */
#pragma STDC FENV_ACCESS ON

#include <float.h>
#include <fenv.h>
#include <inttypes.h>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int64_t read_integer(const char *text, const char *key) {
    const char *p = strstr(text, key);
    char *end = NULL;
    long long value;
    if (p == NULL) {
        fprintf(stderr, "missing JSON key: %s\n", key);
        exit(2);
    }
    p = strchr(p, ':');
    if (p == NULL) exit(2);
    value = strtoll(p + 1, &end, 10);
    if (end == p + 1) exit(2);
    return (int64_t)value;
}

int main(int argc, char **argv) {
    const char *path = argc == 2 ? argv[1] : "certificates/binary64_stagnation.json";
    FILE *fp;
    long length;
    char *text;
    int64_t Ai, ui, vi, bi, Bi;
    volatile double A, u, v, b, y, z, alpha, vz, beta, theta, product, x;

    if (argc > 2) {
        fprintf(stderr, "usage: %s [certificate.json]\n", argv[0]);
        return 2;
    }
    if (FLT_RADIX != 2 || DBL_MANT_DIG != 53 || DBL_MAX_EXP != 1024 ||
        DBL_MIN_EXP != -1021 || fegetround() != FE_TONEAREST) {
        fprintf(stderr, "host is not supported IEEE binary64 round-to-nearest\n");
        return 2;
    }
    fp = fopen(path, "rb");
    if (!fp) return 2;
    if (fseek(fp, 0, SEEK_END) || (length = ftell(fp)) < 0 || fseek(fp, 0, SEEK_SET)) return 2;
    text = malloc((size_t)length + 1);
    if (!text || fread(text, 1, (size_t)length, fp) != (size_t)length) return 2;
    text[length] = '\0';
    fclose(fp);

    Ai = read_integer(text, "\"A_integer\"");
    ui = read_integer(text, "\"u_integer\"");
    vi = read_integer(text, "\"v_integer\"");
    bi = read_integer(text, "\"b_integer\"");
    Bi = read_integer(text, "\"B_integer\"");
    free(text);
    if (Ai != 1 || ui != 1 || vi != INT64_C(9007199254740992) || bi != 1) return 3;
    if (Ai + ui * vi != Bi || Bi != INT64_C(9007199254740993)) return 3;

    A = (double)Ai; u = (double)ui; v = (double)vi; b = (double)bi;
    y = b / A;
    z = u / A;
    alpha = v * y;
    vz = v * z;
    beta = 1.0 + vz;
    theta = alpha / beta;
    product = theta * z;
    x = y - product;
    if (y != 1.0 || z != 1.0 || alpha != 0x1p53 || vz != 0x1p53 ||
        beta != 0x1p53 || theta != 1.0 || x != 0.0) return 4;

    for (int k = 0; k < 32; ++k) {
        volatile double Ax = A * x;
        volatile double vx = v * x;
        volatile double q = vx * u;
        volatile double first = b - Ax;
        volatile double r = first - q;
        volatile double yr = r / A;
        volatile double alpha_r = v * yr;
        volatile double theta_r = alpha_r / beta;
        volatile double correction_product = theta_r * z;
        volatile double partial = x + yr;
        volatile double next_x = partial - correction_product;
        if (r != 1.0 || yr != 1.0 || alpha_r != 0x1p53 ||
            theta_r != 1.0 || next_x != 0.0) return 5;
        x = next_x;
    }
    /* At x=0, both normwise and componentwise residual ratios equal |b|/|b|. */
    if (x != 0.0 || fabs(b) / fabs(b) != 1.0) return 6;
    printf("HARDWARE-CHECKED: beta=0x1p+53, all_iterates=0, backward_error=1, iterations=32\n");
    return 0;
}
