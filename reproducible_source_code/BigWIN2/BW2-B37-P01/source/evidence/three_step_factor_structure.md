# Three-step factor structure: proved count lemma and exact observations

At a time divisible by three the uniform background is again `(0,0)`.  Encode
a site pair `(b_j,c_j)` by `0,1,2,3` and two consecutive sites by the base-four
block code `4*(2*b_left+c_left)+(2*b_right+c_right)`.  For family parameter
`k=2i`, split the sampled state into the left sites `[-2i-1,-2]` (`i` blocks)
and right sites `[-1,2i]` (`i+1` blocks).

## An exact finite path language

Let the generic block alphabet be

`G = {1,2,4,6,8,9,12,13,14,15}`.

The allowed successors are

```
1,9,13  -> {1,2,8,9}
2,6,14  -> {1,2,4,6}
4,8,12  -> {4,6,8,9}
15      -> G
0       -> {4,6,8,9}
3       -> G.
```

A left word starts in `{1,2,12,13,14,15}` and ends in
`{1,2,6,9,13,14,15}`.  A right word starts in `{0,3}`, ends in the same latter
set, and uses `G` after its first symbol; the length-one initial right word is
the special word `(3)`.

**Proved enumeration lemma.**  The numbers of left words of length `i` and
right words of length `i+1` are respectively

```
A_i = (4^(i+1)-1)/3,
B_i = (2*4^(i+1)-5)/3.
```

Proof certificate: order `G` increasingly, let `M` be the 0-1 adjacency matrix
given by the successor table, and let `e` be the column indicator of the ending
set.  Direct substitution of the ten table rows gives
`(M^2-5M+4I)e=0`.  Thus every relevant path-count sequence obeys
`C_(n+2)=5C_(n+1)-4C_n`.  The left initial counts are `5,21`, giving `A_i`;
the right initial counts are `9,41`, giving `B_i`.  The case `i=0` has one empty
left word and the special right word `(3)`.  This proves only the enumeration
of the explicitly defined languages, not yet their dynamical description for
all lengths.

Notice `B_i=2A_i-1`, so `gcd(A_i,B_i)=1`, and

```
3*A_i*B_i = (2*4^(2i+2)-7*4^(i+1)+5)/3.
```

## Exact dynamical observations

`research_three_step_factors.py` verifies for every `0 <= i <= 5` that:

1. every sampled state is supported on `[-2i-1,2i]`, site `-1` is `00`, and
   site `0` is either `00` or `11`;
2. the left projection repeats with least sampled period `A_i` and exhausts
   the left path language;
3. the right projection repeats with least sampled period `B_i` and exhausts
   the right path language;
4. their coprime product is the least sampled full-orbit period, and the exact
   least `F`-period is three times that product.

The factor-period formulas were frozen after inspection through `i=4`; the
complete `i=5` orbit is an exact held-out confirmation.  The path-language
description was then extracted from data through `i=5`; a separate prefix test
at `i=6` exhausts both proposed factor languages and observes their first
returns at `5461` and `10921`.  It does not enumerate the `i=6` full product
orbit and therefore does not certify `P(12)`.

## Minimal unresolved kernel

It remains to prove uniformly that the three-step map preserves the displayed
interface, acts independently on the two path languages, and is one cycle on
each language.  Those three assertions would prove both the conjectured return
time and leastness: the background excludes returns outside multiples of three,
and the coprime projected least periods force sampled return time at least
`A_i B_i`.
