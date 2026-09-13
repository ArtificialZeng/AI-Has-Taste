# Exact order-four support computation

This dossier implements the precise fixed-order reading in `problem.md`.  All
calculations are over Boolean supports; no floating-point values or sampled
weights occur.

## Encoding and complete legal alphabet

For row support masks $r_i\in\{1,\ldots,15\}$, a support is encoded as

\[
m=r_1+2^4r_2+2^8r_3+2^{12}r_4.
\]

Thus a displayed hexadecimal word `d4d3d2d1` has row 1 mask `d1`, row 2
mask `d2`, row 3 mask `d3`, and row 4 mask `d4`; bit $j-1$ denotes column
$j$.  Enumerating $r_1,r_2,r_3,r_4\in\{1,\ldots,15\}$ visits exactly
$15^4=50,625$ row-nonempty supports.

For every support and every level $r=1,2,3,4$, the enumerator checks directly:

1. row-allowability and GR for the leading $r\times r$ block;
2. row-allowability and GE for every leading $s\times s$ block with $r<s\le4$;
3. a nonzero entry in columns $1,\ldots,r$ for every row below $r$.

GE and GR are checked for every pair of disjoint nonempty row subsets, with
strict expansion only for GR.  Taking the union over the four levels gives
37,833 distinct admitted supports.  Counts at levels $1,2,3,4$, before
deduplicating their union, are respectively

\[
(4096,15806,25462,35347).
\]

The counts by exact four-bit level-membership mask are

| mask (hex) | 0 | 2 | 4 | 6 | 8 | a | c | e | f |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| count | 12792 | 512 | 1328 | 646 | 10901 | 958 | 9798 | 9594 | 4096 |

Here bit $r-1$ records admission at level $r$; mask 0 is the complement of
the legal alphabet among the 50,625 row-nonempty supports.

## Exhaustive nonscrambling frontiers

Let \(\mathcal L\) be the legal support alphabet, let \(I\) be the Boolean
identity, and define

\[
F_0=\{I\},\qquad
F_{d+1}=\{A\odot B:A\in\mathcal L,\ B\in F_d,
                 A\odot B\text{ is nonscrambling}\}.
\]

This recurrence loses no nonscrambling word by discarding scrambling partial
products.  Indeed, if $B$ is scrambling and $A$ is row-allowable, choose
any $k\in F_A(\{i\})$ and $\ell\in F_A(\{j\})$.  Rows $k,\ell$ of $B$
have a common supported column, which therefore occurs in both rows $i,j$ of
$A\odot B$.  Thus left multiplication by any legal support preserves
scrambling.  Induction shows that $F_d$ is exactly the set of nonscrambling
Boolean products of all legal words of length $d$.

The complete sorted frontier sizes are

| length | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| frontier size | 1 | 19946 | 13532 | 9802 | 6258 | 3332 | 1720 | 988 | 566 | 316 | 120 | 0 |

Consequently every legal 11-factor product is scrambling, while a legal
10-factor nonscrambling product exists.

## Exact maximal witness

The following table lists $P_1,\ldots,P_{10}$, one level proving each
factor's admission, and the cumulative Boolean product $P_t\odot\cdots\odot
P_1$.  The level tests themselves are reproduced by both checkers.

| $t$ | factor | admitted level | cumulative product |
|---:|:---:|---:|:---:|
| 0 | — | — | `8421` |
| 1 | `a126` | 2 | `a126` |
| 2 | `423a` | 3 | `126a` |
| 3 | `c586` | 4 | `3a16` |
| 4 | `a215` | 2 | `316e` |
| 5 | `4643` | 3 | `171e` |
| 6 | `21a6` | 2 | `1e17` |
| 7 | `42a3` | 3 | `e117` |
| 8 | `9368` | 4 | `f71e` |
| 9 | `3126` | 2 | `fe17` |
| 10 | `2345` | 3 | `17ef` |

The final product has row masks `[f,e,7,1]`.  Its second and fourth rows have
masks `e` and `1`, whose intersection is zero, so it is not scrambling.  Every
listed support has a positive stochastic realization, for example by assigning
equal positive weight to all supported entries in each row.

## Reproduction and cross-check

`search_exact.cpp` constructs the full legal alphabet using explicit pairs of
disjoint subsets, generates every frontier, and writes the entire alphabet and
all frontier states to `frontier_certificate.txt` (not merely their counts).
`verify_certificate.cpp` is a separate implementation: it scans all 65,536
binary relations, rebuilds GE/GR through ternary assignments of each row index
to neither set, $I$, or $J$, and compares the complete sorted legal alphabet
and every complete sorted frontier against the certificate.  It also multiplies
the witness by a direct Boolean routine.  Its successful output is preserved in
`verification_report.txt`.

Reproduction commands from the project root are:

```sh
clang++ -O3 -std=c++17 evidence/search_exact.cpp -o /tmp/bigmac_search_exact
/tmp/bigmac_search_exact evidence/search_result.json evidence/frontier_certificate.txt
clang++ -O3 -std=c++17 evidence/verify_certificate.cpp -o /tmp/bigmac_verify_certificate
/tmp/bigmac_verify_certificate evidence/frontier_certificate.txt evidence/verification_report.txt
```

The exact computational conclusion, for the frozen class in `problem.md`, is

\[
h_{\mathrm{scr}}(\mathcal A_4)=11.
\]
