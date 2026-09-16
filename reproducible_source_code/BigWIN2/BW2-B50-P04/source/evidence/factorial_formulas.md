# Exact factorial formulas for all surviving two-black-square classes

Provenance: `win-00050-p04-research-a2ddb7bf5fd0` (research pass 2,
2026-09-07). Coordinates are one-based. These formulas, together with the
word-count reduction in `finite_census.md`, cover every configuration. Their
discrete all-`n` maximization is not proved here.

## Block-permanent expansion

Put the across words split by a black square first and the down words split by
a black square first. In every surviving class the biadjacency matrix has a
block form

```text
[ A  B ]
[ C  J ]
```

where `J` is an all-one rectangular block, except in the corner--interior case
where it has one forbidden corner edge. Choose a matching `P` in `A`. Every
unmatched special across word must then be injected through `B` into ordinary
columns, and every unmatched special down word must be injected through `C`
from ordinary rows. The unused ordinary vertices can be matched in `t!` ways
through `J`. Summing over the matchings `P` gives the formulas below. This is a
proof of the formulas: the construction partitions every perfect matching by
its set of special-to-special edges, and all stated injection factors count
disjoint interval choices.

For later use, if two split coordinates are `x<y`, put

```text
a=x-1,  b=y-x-1,  c=n-y,
I2(a,b,c) = ac,
U(a,b,c)  = ac(a+b-1),
V(a,b,c)  = ac(b+c-1),
I4(a,b,c) = ac[ab+ac-a+b^2+bc-3b-c+1].
```

Here `I4` counts injections of all four interval words (left and right at each
split coordinate) into the ordinary coordinates. Removing the right word at
the lower split gives `U`; removing the left word at the upper split gives
`V`; removing both gives `I2`. These identities follow by assigning the chosen
ordinary coordinates to the three disjoint regions of sizes `a,b,c`. More
explicitly, the lower-left word has support `A`, the lower-right word `B union
C`, the upper-left word `A union B`, and the upper-right word `C`. First choose
the mandatory outer words in `ac` ways. If all four words remain, the other two
choices contribute

```text
b(a+b-2) + (c-1)(a+b-1),
```

according as the lower-right choice lies in `B` or in the remaining part of
`C`; expansion gives the displayed `I4`. If one or both middle-facing words
are removed, the same argument immediately gives `U`, `V`, and `I2`.

## The `n+1` classes

After reflection, a corner--interior pair has black squares `(1,1)` and
`(r,c)`, where `2<=r,c<=n-1`. For `n>=4` its count is

```text
(n-c)(n-r)(n-4)! [(c-1)(r-1)(n-3) - (c-2)(r-2)].                 (C)
```

For `n=3` its sole instance has count `1`. The first term before factoring is
the all-one-core count
`(c-1)(n-c)(r-1)(n-r)(n-3)!`; the subtracted term forces the one forbidden
ordinary corner edge and is
`(c-2)(n-c)(r-2)(n-r)(n-4)!`.

After reflection, an edge-cross pair has black squares `(1,c)` and `(r,1)`,
where `2<=r,c<=n-1`. Its count is

```text
(n-c)(n-r)[(c-2)(r-2)(n-3)! + (n-2)!].                         (E)
```

The two summands respectively use zero or one of the sole special-to-special
edges (the white corner `(1,1)`).

## The `n+2` classes

For two black squares `(r,c1),(r,c2)` in one interior row, with
`2<=c1<c2<=n-1` and `c2>c1+1`, the count is

```text
(c1-1)(c2-c1-1)(n-c2)
 (r-1)(r-2)(n-r)(n-r-1)(n-5)!.                                (S)
```

The transposed formula covers a common interior column. The factors are the
injections of the three across intervals and the two upper plus two lower down
intervals. A zero factor correctly detects an impossible perfect matching.

Finally suppose the two squares have distinct interior rows and columns. Let
`r_-<r_+` and `c_-<c_+`, and evaluate `(I4,U,V,I2)` on the row triple
`(r_--1,r_+-r_--1,n-r_+)` and on the analogous column triple. Add

```text
I4_col I4_row (n-6)! + H (n-5)! + I2_col I2_row (n-4)!,        (I)
```

omitting a term whose factorial has negative argument. If the lower-row black
square is in the lower-numbered column (parallel order), then

```text
H = U_col V_row + V_col U_row.
```

For crossed order,

```text
H = U_col U_row + V_col V_row.
```

The three terms use zero, one, or both of the two mutually disjoint white
cross-intersection edges. This also explains why only the order type enters.

## Exact regression and a falsified provisional maximum

Run

```text
python3 evidence/verify_factorial_formulas.py
```

The script evaluates the appropriate formula on every canonical orbit in
`census_n3_n8.json`. It checks 620 orbits whose orbit sizes total all 4,278
configurations; every formula value equals the independently computed word-
graph permanent.

The opposite-corner construction is not the all-`n` maximum. At `n=15`, the
edge-cross pair `{(1,7),(7,1)}` has, by (E),

```text
8^2(5^2+13)12! = 2432*12!,
```

whereas opposite corners have

```text
15!-2*14!+13! = 2379*12!.
```

Thus the former exceeds the latter by `53*12! = 25,387,084,800`. This exact
counterexample refutes the pass-1 extrapolation from `n<=8`; it does not settle
the original maximization problem.
