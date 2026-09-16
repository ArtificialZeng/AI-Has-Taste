# Precise problem: determine `s_1(4)`

## Frozen mathematical reading

For each positive integer `k`, let `P(k)` be the following assertion:

> For every ordered sequence `(a_1,...,a_k)` of integers satisfying
> `4 \nmid a_i` for every `i`, there are four distinct indices
> `1 <= i_1 < i_2 < i_3 < i_4 <= k` such that
> `a_{i_1}+a_{i_2}+a_{i_3}+a_{i_4}` is divisible by `4` but not by `16`.

Then

`s_1(4) = min { k in Z_{>0} : P(k) }`.

The indices, not the integer values, must be distinct. Equal values may occur
at different positions and may all be selected. The selected set has exactly
four positions. Since `P(k)` implies `P(k+1)` (apply `P(k)` to any `k`
positions), this is a threshold problem.

## Exact finite reduction

Put

`A = {1,2,3,5,6,7,9,10,11,13,14,15} subset Z/16Z`.

The hypothesis `4 \nmid a_i` and the desired sum both depend only on each
`a_i mod 16`. A sum is divisible by `4` but not by `16` exactly when its
residue modulo `16` is in `{4,8,12}`. Consequently, `P(k)` is equivalent to:

> Every length-`k` sequence over `A` has four distinct positions whose residue
> sum modulo `16` belongs to `{4,8,12}`.

The property is invariant under permuting positions. Sorting therefore gives
a bijection between permutation orbits and nondecreasing `k`-multisets over
the 12 residues. There are `C(12+k-1,k)` such multisets: 75,582 at `k=8` and
167,960 at `k=9`. This reduction retains multiplicities and loses no ordered
case.

## Scope

The task is only the exact value at `n=4`, rank `r=1`. Statements for another
`n` or rank, for distinct-valued sets instead of sequences, for a selected
length other than exactly four, or merely for sums divisible by `4` are not
the frozen problem.

## Prior result and proposed contribution

Sun, arXiv:2606.18234v5, Definition 1.3, Theorem 1.3, Remark 1.4, and
Conjecture 1.2, proves `9 <= s_1(4) <= 13` and conjectures `s_1(4)=9` as a
case of `s_1(n)=2n+1`. The source was inspected at
<https://arxiv.org/html/2606.18234v5> on 2026-09-10; details and the related
literature distinction are in `literature/triage_literature.md`.

Target contribution: nearest prior result `[9,13]`; proposed delta, prove the
sharp upper bound `s_1(4) <= 9` (and hence equality); verification route,
combine the residue reduction above with complete exact finite coverage and a
fresh independent verifier or a compact analytic classification.

The fresh triage checker in `evidence/exact_residue_check.py` reports no
avoiding length-nine multiset and supplies length-eight avoiders. This is an
exact finite observation from one implementation, not yet an independently
audited resolution.
