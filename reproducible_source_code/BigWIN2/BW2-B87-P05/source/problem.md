# Precise problem reading

## Objects and conventions

Fix an integer `m >= 1` and a positive multiplicity vector
`alpha=(alpha_1,...,alpha_m) in Z_{>0}^m`. Put

```text
N = alpha_1 + ... + alpha_m.
```

Let `W_alpha` be the set of all length-`N` words on the ordered alphabet
`1<2<...<m` in which letter `j` occurs exactly `alpha_j` times. For
`w=w_1...w_N`, an occurrence of the consecutive pattern `21435` starting at
`i` (where `1 <= i <= N-4`) means

```text
w_(i+1) < w_i < w_(i+3) < w_(i+2) < w_(i+4).
```

Thus all five letters in an occurrence are distinct. Define

```text
c(w) = sum_{i=1}^{N-4} 1[w_(i+1)<w_i<w_(i+3)<w_(i+2)<w_(i+4)],
F_alpha(t) = sum_{w in W_alpha} t^c(w) in Z[t].
```

For `sigma in S_m`, `sigma alpha` denotes the corresponding coordinate
reordering. The coordinate orbit (or unordered multiplicity type) of `alpha`
is **stable** when

```text
F_alpha(t) = F_(sigma alpha)(t) for every sigma in S_m.
```

An unordered type is therefore an integer partition of `N`; repeated parts do
not create distinct coordinate orders. Zero coordinates are outside the frozen
quantification and may be deleted. If `N<5` or `m<5`, strictness makes
`c(w)=0` for every word, and `F_alpha(t)=N!/(product_j alpha_j!)`, which is
coordinate-invariant.

## Frozen claim, with quantifiers made explicit

1. For every `m>=1` and every `alpha in Z_{>0}^m` with `sum alpha_j <= 8`,
   the coordinate orbit of `alpha` is stable.
2. For every `m>=1` and every `alpha in Z_{>0}^m` with `sum alpha_j=9`, the
   orbit is unstable if and only if the decreasing rearrangement of `alpha` is
   `(2,1,1,1,1,1,1,1)`. Hence every other integer-partition type at `N=9`
   is stable.
3. For `r in {1,...,8}`, let `alpha^(r)` have `alpha_r=2` and every other
   coordinate equal to `1`. Then

   ```text
   F_(alpha^(r))(t) = 176026 + 5368 t + 46 t^2,  1 <= r <= 4,
   F_(alpha^(r))(t) = 176025 + 5370 t + 45 t^2,  5 <= r <= 8.
   ```

   In particular, no word in any of these eight content classes has three or
   more occurrences.

“Only unstable unordered type” in item 2 means uniqueness among all positive
content vectors of total size nine, not merely among vectors with one repeated
letter.

## Scope, source status, and target delta

The nearest verified source is Chen--Fang--Kitaev, *Stable patterns on
permutations of multisets*, arXiv:2602.13566v2. Its Proposition 4.12 proves
instability when a minimal standard extension has a repeated letter. Remark
4.13 identifies `21435` as an obstruction to that criterion: its minimal
extendable index is `3` and its standard extension is the all-distinct word
`2143657`. Conjecture 6.1 asserts the broader classification that a consecutive
pattern is stable exactly when it is monotone. The paper does not state the
finite first-instability classification or the displayed coefficients above.

Accordingly, the source status of this exact refinement is **new-question**,
not “verified open problem.” The proposed delta is a proof of the exact
minimal length, uniqueness at length nine, and coefficient formulas. The
intended verification route is an independently replayable exhaustive check
plus a mathematical derivation using the possible self-overlaps, their overlap
posets, and coefficient extraction or binomial inversion. Exhaustive generation
alone does not meet the frozen contribution boundary. Proving this claim would
show that `21435` itself is unstable, but would not resolve Conjecture 6.1 for
all consecutive patterns.

Primary-source inspection is recorded in
`literature/arxiv-2602.13566v2-triage.md`.
