#include <stdio.h>
#include <stdlib.h>
#include <flint/flint.h>
#include <flint/fmpz.h>
#include <flint/fmpz_mat.h>
#include <flint/fmpq.h>
#include <flint/fmpq_mat.h>

int main(int argc, char **argv) {
    if (argc != 3) {
        fprintf(stderr, "usage: %s INPUT OUTPUT\n", argv[0]);
        return 2;
    }
    FILE *input = fopen(argv[1], "r");
    if (!input) return 3;
    long rows, cols;
    if (fscanf(input, "%ld %ld", &rows, &cols) != 2 || rows != cols) return 4;
    fmpz_mat_t A, b;
    fmpq_mat_t x;
    fmpz_mat_init(A, rows, cols);
    fmpz_mat_init(b, rows, 1);
    fmpq_mat_init(x, cols, 1);
    for (slong i = 0; i < rows; i++) {
        for (slong j = 0; j < cols; j++) {
            if (!fmpz_fread(input, fmpz_mat_entry(A, i, j))) return 5;
        }
        if (!fmpz_fread(input, fmpz_mat_entry(b, i, 0))) return 6;
    }
    fclose(input);
    int nonsingular = fmpq_mat_solve_fmpz_mat_multi_mod(x, A, b);
    if (!nonsingular) {
        fprintf(stderr, "selected integer basis is singular\n");
        return 7;
    }
    FILE *output = fopen(argv[2], "w");
    if (!output) return 8;
    fprintf(output, "%ld\n", cols);
    for (slong i = 0; i < cols; i++) {
        fmpq_fprint(output, fmpq_mat_entry(x, i, 0));
        fputc('\n', output);
    }
    fclose(output);
    fmpq_mat_clear(x);
    fmpz_mat_clear(b);
    fmpz_mat_clear(A);
    flint_cleanup();
    return 0;
}
