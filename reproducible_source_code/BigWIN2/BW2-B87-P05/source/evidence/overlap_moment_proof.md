# Overlap-poset and binomial-moment proof for `21435`

This note proves the frozen classification in `source.md`.  All positions below
are positions in a word, and every inequality is strict.  Put

```text
D(alpha) = product_j alpha_j!,
e_k(alpha) = sum_{|S|=k} product_{j in S} alpha_j,
B_k(alpha) = sum_{w in W_alpha} binom(c(w),k).
```

As usual, `e_k=0` if there are fewer than `k` coordinates.

## 1. Compatible overlaps

An occurrence beginning at position `i` imposes the chain

```text
w_(i+1) < w_i < w_(i+3) < w_(i+2) < w_(i+4).       (1)
```

Two overlapping occurrences whose starts differ by 1 are impossible: their
combined inequalities contain a directed cycle (in zero-based local position
notation, `2<1<0<3<2`).  A difference of 3 is likewise impossible, since the
combined relations contain `3<2<4<3`.  Differences 2 and 4 are compatible.

At difference 2, the two copies of (1) combine into the seven-element chain

```text
w_(i+1) < w_i < w_(i+3) < w_(i+2)
          < w_(i+5) < w_(i+4) < w_(i+6).            (2)
```

At difference 4, set

```text
a1=w_(i+1), a2=w_i, a3=w_(i+3), a4=w_(i+2), c=w_(i+4),
b=w_(i+5), d1=w_(i+7), d2=w_(i+6), d3=w_(i+8).
```

The combined poset is

```text
a1 < a2 < a3 < a4 < c < d1 < d2 < d3,
                         b < c,                      (3)
```

where `b` is incomparable with each `a_j`.  These assertions follow simply by
writing (1) for the two starts; the exact closure calculation is replayed by
`overlap_moment_check.py`.

For `N<=9`, two occurrence starts differ by at most 4, so the preceding list is
complete.  If a word has at least three occurrences, every pair of their starts
must therefore differ by 2 or 4.  The only possible three-start set is
`{1,3,5}`, necessarily at `N=9`.  The three copies of (1) then combine into
the nine-element chain

```text
w_2 < w_1 < w_4 < w_3 < w_6 < w_5 < w_8 < w_7 < w_9. (4)
```

Consequently, a word of length at most 9 having any repeated letter has at most
two occurrences.  (The all-distinct content at `N=9` needs no such bound for
stability, because its coordinate orbit is a singleton.)

## 2. The first two binomial moments

For one fixed start, choose the five distinct alphabet ranks used in (1).
For a chosen five-set `S`, its ranks have a unique placement in the chain, and
the unconstrained positions can be filled in

```text
(N-5)! / product_j (alpha_j-1[j in S])!
```

ways.  Summing over `S` and over the `N-4` starts gives, for `N>=5`,

```text
B_1(alpha) = (N-4)(N-5)! e_5(alpha) / D(alpha).       (5)
```

In particular, the first moment is symmetric in the coordinates.

For a marked pair at separation 2, (2) similarly gives the fixed-pair count

```text
C_2(alpha) = (N-7)! e_7(alpha) / D(alpha).            (6)
```

There are `N-6` such start pairs when `N>=7`.  Separation 4 can occur in the
range under consideration only when `N=9`; write its fixed-pair count as
`Q(alpha)`.  Hence, for `N<=9`,

```text
B_2(alpha) = 1[N>=7](N-6) C_2(alpha) + 1[N=9]Q(alpha). (7)
```

The only incomparable pairs in (3) are `{b,a_j}`.  Thus an order-preserving
assignment of a positive content to all nine elements can have either no
repetition or exactly one repeated rank of multiplicity two.  It follows that

```text
Q(alpha)=0
```

for every repeated content except unordered type `{2,1^7}`.  For completeness,
if all nine ranks are distinct then `Q=5`, corresponding to the five possible
locations of `b` among the four-element lower chain; this case has a singleton
coordinate orbit.

Now let `alpha^(r)=(1,...,1)` on eight ranks except `alpha_r=2`.  In (3), the
two equal positions must be `b` and one of the `a_j`.  The lower five positions
then use four distinct ranks, while `c,d1,d2,d3` use the other four.  Since all
lower ranks are less than all upper ranks, they are respectively
`{1,2,3,4}` and `{5,6,7,8}`.  The chain fixes every assignment once the repeated
rank is specified.  Therefore

```text
Q(alpha^(r)) = 1  if 1<=r<=4,
Q(alpha^(r)) = 0  if 5<=r<=8.                         (8)
```

## 3. Stability and the two exceptional polynomials

For every content with a repeated letter, (4) shows `c(w)<=2`.  If
`A_j=[t^j]F_alpha(t)` and `T=|W_alpha|=N!/D(alpha)`, binomial inversion reduces
to

```text
A_2=B_2,
A_1=B_1-2B_2,
A_0=T-B_1+B_2.                                       (9)
```

For `N<=8`, the three quantities on the right are symmetric functions of the
coordinates by (5)--(7), so every repeated content is stable; an all-distinct
content again has a singleton orbit.  At `N=9`, the same argument applies to
every repeated content except `{2,1^7}`, because its `Q` term is zero.  This
proves stability for every other unordered type.

For `alpha^(r)`, direct evaluation of the symmetric terms gives

```text
T = 9!/2 = 181440,
e_5(alpha^(r)) = 2*C(7,4)+C(7,5) = 91,
B_1 = 5*4!*91/2 = 5460,
e_7(alpha^(r)) = 2*C(7,6)+C(7,7) = 15,
C_2 = 2!*15/2 = 15,
B_2 = 3*15 + Q(alpha^(r)).
```

Equations (8)--(9) now yield

```text
F_(alpha^(r))(t) = 176026 + 5368t + 46t^2,  1<=r<=4,
F_(alpha^(r))(t) = 176025 + 5370t + 45t^2,  5<=r<=8.
```

The polynomials differ, so this type is unstable.  Equation (4) also proves,
without enumeration, that no word in these repeated-letter classes has three
or more occurrences.  Together with the preceding stability argument, this
establishes all three parts of the frozen claim.

