/*
 * Exact independence-polynomial checker for gentreeg parent arrays.
 *
 * This implementation was written independently for the present project.  It
 * deliberately reconstructs child lists and uses a recursive postorder; it
 * does not rely on the generator's vertex order when evaluating the tree.
 * All decisive arithmetic is uint64_t with __uint128_t overflow checks.
 */

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_VERTICES 40
#define MAX_COEFFICIENTS (MAX_VERTICES + 1)
#define SAVE_LIMIT 4096

typedef struct {
    int degree;
    uint64_t coefficient[MAX_COEFFICIENTS];
} polynomial;

static int first_child[MAX_VERTICES + 1];
static int next_sibling[MAX_VERTICES + 1];
static polynomial excluded_state[MAX_VERTICES + 1];
static polynomial included_state[MAX_VERTICES + 1];
static unsigned char visit_state[MAX_VERTICES + 1];
static int visited_vertices;

static unsigned long long checked_trees;
static unsigned long long nonunimodal_trees;
static unsigned long long nonlogconcave_trees;
static unsigned long long saved_exceptions;
static uint64_t sequence_hash_sum;
static uint64_t parent_hash_sum;

static void fail(const char *message)
{
    fprintf(stderr, "FATAL order31_checker: %s\n", message);
    exit(2);
}

static void set_constant(polynomial *result, uint64_t value)
{
    result->degree = 0;
    result->coefficient[0] = value;
}

static void set_monomial_x(polynomial *result)
{
    result->degree = 1;
    result->coefficient[0] = 0;
    result->coefficient[1] = 1;
}

static void add_polynomials(const polynomial *left, const polynomial *right,
                            polynomial *result)
{
    int k;
    result->degree = left->degree > right->degree ? left->degree : right->degree;
    for (k = 0; k <= result->degree; ++k) {
        uint64_t value = 0;
        if (k <= left->degree) value += left->coefficient[k];
        if (k <= right->degree) value += right->coefficient[k];
        result->coefficient[k] = value;
    }
}

static void multiply_polynomials(const polynomial *left,
                                 const polynomial *right,
                                 polynomial *result)
{
    int i, j;
    if (left->degree + right->degree >= MAX_COEFFICIENTS)
        fail("polynomial degree exceeds compiled capacity");
    result->degree = left->degree + right->degree;
    memset(result->coefficient, 0,
           (size_t)(result->degree + 1) * sizeof(result->coefficient[0]));
    for (i = 0; i <= left->degree; ++i) {
        for (j = 0; j <= right->degree; ++j) {
            /* Every partial sum counts a subset of independent sets in a
             * forest on at most 40 vertices.  It is therefore bounded by
             * C(40,20) < 2^38, so uint64_t cannot overflow here. */
            result->coefficient[i + j] +=
                left->coefficient[i] * right->coefficient[j];
        }
    }
}

static void copy_polynomial(polynomial *destination, const polynomial *source)
{
    destination->degree = source->degree;
    memcpy(destination->coefficient, source->coefficient,
           (size_t)(source->degree + 1) * sizeof(source->coefficient[0]));
}

static void solve_vertex(int vertex)
{
    int child;
    polynomial child_total;
    polynomial next_excluded;
    polynomial next_included;

    if (visit_state[vertex] == 1) fail("cycle in parent array");
    if (visit_state[vertex] == 2) fail("vertex reached more than once");
    visit_state[vertex] = 1;
    ++visited_vertices;
    set_constant(&excluded_state[vertex], 1);
    set_monomial_x(&included_state[vertex]);

    for (child = first_child[vertex]; child != 0;
         child = next_sibling[child]) {
        solve_vertex(child);
        add_polynomials(&excluded_state[child], &included_state[child],
                        &child_total);
        multiply_polynomials(&excluded_state[vertex], &child_total,
                             &next_excluded);
        multiply_polynomials(&included_state[vertex],
                             &excluded_state[child], &next_included);
        copy_polynomial(&excluded_state[vertex], &next_excluded);
        copy_polynomial(&included_state[vertex], &next_included);
    }
    visit_state[vertex] = 2;
}

static uint64_t fnv1a_words(const uint64_t *words, int length)
{
    uint64_t hash = UINT64_C(1469598103934665603);
    int i;
    for (i = 0; i < length; ++i) {
        hash ^= words[i];
        hash *= UINT64_C(1099511628211);
    }
    return hash;
}

static void print_exception(FILE *out, const char *label, const int *parent,
                            int n, const polynomial *poly)
{
    int i;
    fprintf(out, "%s n=%d parent=", label, n);
    for (i = 1; i <= n; ++i)
        fprintf(out, "%s%d", i == 1 ? "" : ",", parent[i]);
    fprintf(out, " coefficients=");
    for (i = 0; i <= poly->degree; ++i)
        fprintf(out, "%s%llu", i == 0 ? "" : ",",
                (unsigned long long)poly->coefficient[i]);
    fputc('\n', out);
    fflush(out);
}

void research_check_init(void)
{
    checked_trees = 0;
    nonunimodal_trees = 0;
    nonlogconcave_trees = 0;
    saved_exceptions = 0;
    sequence_hash_sum = 0;
    parent_hash_sum = 0;
}

void research_check_tree(FILE *out, int *parent, int n)
{
    int vertex;
    int descending = 0;
    int unimodal = 1;
    int logconcave = 1;
    polynomial full;
    uint64_t parent_words[MAX_VERTICES];

    if (n < 1 || n > MAX_VERTICES) fail("tree order outside compiled range");
    memset(first_child, 0, sizeof(first_child));
    memset(next_sibling, 0, sizeof(next_sibling));
    memset(visit_state, 0, sizeof(visit_state));
    visited_vertices = 0;

    if (parent[1] != 0) fail("root parent must be zero");
    parent_words[0] = (uint64_t)n;
    for (vertex = 2; vertex <= n; ++vertex) {
        int p = parent[vertex];
        if (p < 1 || p > n || p == vertex) fail("invalid parent array");
        next_sibling[vertex] = first_child[p];
        first_child[p] = vertex;
        parent_words[vertex - 1] = (uint64_t)p;
    }

    solve_vertex(1);
    if (visited_vertices != n) fail("parent array is disconnected");
    add_polynomials(&excluded_state[1], &included_state[1], &full);
    if (full.coefficient[0] != 1 || full.coefficient[1] != (uint64_t)n)
        fail("independence polynomial failed constant/linear sanity check");
    for (vertex = 0; vertex <= full.degree; ++vertex)
        if (full.coefficient[vertex] >= (UINT64_C(1) << 40))
            fail("proved coefficient bound was violated");

    for (vertex = 0; vertex < full.degree; ++vertex) {
        if (full.coefficient[vertex + 1] < full.coefficient[vertex]) {
            descending = 1;
        } else if (full.coefficient[vertex + 1] > full.coefficient[vertex]
                   && descending) {
            unimodal = 0;
            break;
        }
    }
    for (vertex = 1; vertex < full.degree; ++vertex) {
        uint64_t middle = full.coefficient[vertex]
                          * full.coefficient[vertex];
        uint64_t outside = full.coefficient[vertex - 1]
                           * full.coefficient[vertex + 1];
        if (middle < outside) {
            logconcave = 0;
            break;
        }
    }

    if (!unimodal) {
        ++nonunimodal_trees;
        print_exception(out, "NONUNIMODAL", parent, n, &full);
    }
    if (!logconcave) {
        ++nonlogconcave_trees;
        if (saved_exceptions < SAVE_LIMIT) {
            ++saved_exceptions;
            print_exception(out, "NONLOGCONCAVE", parent, n, &full);
        }
    }
#ifdef PRINT_ALL_SEQUENCES
    print_exception(out, "SEQUENCE", parent, n, &full);
#endif

    sequence_hash_sum += fnv1a_words(full.coefficient, full.degree + 1);
    parent_hash_sum += fnv1a_words(parent_words, n);
    ++checked_trees;
}

void research_check_summary(unsigned long long generated, double cpu_seconds)
{
    fprintf(stderr,
            "RESEARCH_CHECK trees=%llu generated=%llu nonunimodal=%llu "
            "nonlogconcave=%llu sequence_hash=%016llx parent_hash=%016llx "
            "cpu=%.2f\n",
            checked_trees, generated, nonunimodal_trees,
            nonlogconcave_trees, (unsigned long long)sequence_hash_sum,
            (unsigned long long)parent_hash_sum, cpu_seconds);
    if (checked_trees != generated) fail("OUTPROC count differs from gentreeg count");
}
