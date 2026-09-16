# Exact block-transducer certificate for three-step factorization

Let $H=F^3$, sampled when the uniform background pair is `(0,0)`.  Pair
sites as `(2r-1,2r)` and encode their two site-pairs `(b,c)` by a block in
`{0,...,15}` as in `three_step_factor_structure.md`.

## Proved structural lemma

For every $i\geq0$, zero-padding a word in the left language $L_i$ or
right language $R_i$ and applying $H$ gives another word in the same
language, with zero outside its original block interval.  Moreover, for every
$l\in L_i$ and $r\in R_i$,

\[
H(lr)=H(l)H(r),
\]

where the maps on the right use zero padding.  Thus the central interface is
exactly decoupled, and $H$ induces separate permutations of the two finite
path languages.  This lemma does **not** say that either permutation is a
single cycle.

## Why the finite certificate is exhaustive

After three radius-one updates, the output site pair at $j$ depends only on
input sites from $j-3$ through $j+3$.  Hence one output two-site block
depends on exactly the displayed five-block window centered there.  The
function `local_rule` in `research_block_transducer.py` evaluates this rule
directly by three applications of the exact rule-115 update.  Its complete
`16^5` truth table has SHA-256

`8daa099568b0ddd2641c338c7e006173826db9c18662d0f8330138b6be80f0d2`.

For an interior input path, membership of one output block uses a five-block
window, and admissibility of two adjacent output blocks uses a six-block
window.  The script exhausts all 3,070 and 12,286 such paths.  Because the
input languages are one-step path languages, these are all possible interior
contexts at every word length.

Only the first two and last two output blocks can see a padded boundary.  The
script exhausts all admissible length-six boundary contexts (including paths
that need not extend to the opposite boundary, a strengthening) and separately
checks every shorter word where the two boundary neighborhoods overlap.

Across the interface, only the last two left outputs and first two right
outputs can depend on the other factor.  Exhausting the 511 possible generic
left terminal contexts and 254 possible right initial contexts gives 129,794
comparisons with the corresponding zero-padded outputs.  All comparisons are
equal.  The 15,272 shorter equal-length factor pairs are checked separately.
This establishes the identity above for arbitrary length by locality.

Finally, $F$, hence $H$, is injective: from $F(b,c)=(c,d)$, recover
$b_j=d_j\oplus\delta_{115}(c_{j-1},c_j,c_{j+1})$.  An injective self-map of
each finite invariant language is a permutation.

## New exact finite consequences and remaining gap

Direct factor evolution now establishes the proposed least factor periods
$A_i,B_i$ through $i=8$; `i=7,8` were held out after freezing the terminal
run pattern.  Combined with exact decoupling and
$\gcd(A_i,B_i)=1$, this certifies the original period formula for every
`0 <= i <= 8` without enumerating the product orbit.

The last block occurs in one cyclic run of each indicated length.  For the
left factor the cyclic schedule is

\[
1^{A_{i-1}},\ 9^{A_{i-1}-1},\ 13,\ 14,\
6^{A_{i-1}-1},\ 2^{A_{i-1}},\ 15,
\]

and for the right factor it is

\[
1^{B_{i-1}},\ 9^{B_{i-1}+1},\ 13,\ 14,\
6^{B_{i-1}+1},\ 2^{B_{i-1}},\ 15.
\]

These lengths sum to $4A_{i-1}+1$ and $4B_{i-1}+5$, respectively, and
equal the proved numbers of language words with each last symbol.  The
all-length single-run/exhaustion statement is still an observation.  It is
now the only missing dynamical step.
