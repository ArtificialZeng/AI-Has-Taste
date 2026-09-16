# Uniform infeasibility of the `C4` core on `M = 4 (mod 8)`

This file gives a self-contained proof of a stronger statement than the frozen
claim.  Write `b_j=M+j`, `t_i=2M-i`, and
`m=3M/2`.  For every `M>=20` with `M=4 (mod 8)`, there is no AP-free strict
total order of `(M,2M]` satisfying

```
P:  t_13 < b_1,       Q:  t_11 < b_2,
A1: t_5  < b_5,       A3: t_10 < b_3.                 (C4)
```

Here `<` denotes the putative order, not numerical order.  Since these four
relations occur among the fifteen relations of `OG(M)`, this proves the frozen
full-gadget assertion.

## Order rules

For a numerical AP `a<b<c`, AP-freeness says its midpoint is before both
endpoints or after both.  We use the four immediate rules

```
a<b(order) => c<b(order),        c<b(order) => a<b(order),
b<c(order) => b<a(order),        b<a(order) => b<c(order).     (R)
```

On a maximal numerical `g`-ladder (a fixed residue modulo `g`), the relations
between consecutive rungs alternate: one of the two classes modulo `2g`
precedes both neighboring rungs.  Call that half-class the leaders.  This is
obtained by iterating (R) on consecutive triples.

We need the following version of the flood lemma.  It is the same proof as the
source's Lemma 26, but its elementary argument works for every positive even
`g`, in particular `g=8`.

**General flood lemma.**  Let `C` be one residue class `r (mod g)` in the
block, where `g` is even, and let its `g`-ladder have either zigzag phase.  Let
`c = r+g/2 (mod g)`.  Put

```
W_c={w in C : 2c-w is also in (M,2M]}.
```

If `c<w_0` in the order for one `w_0 in W_c`, then `c<w` for every `w in
W_c`.  If `w_0<c`, all these inequalities reverse.

Indeed, the two members `c-e,c+e` of every admissible mirror pair lie in the
opposite leader half-classes of `C`. Rule (R) first copies the seed to the
other member of its mirror pair. For the outward assertion, to pass from
distance `e` to `e+g`, choose the leader in the pair at distance `e`; it
precedes its outward ladder neighbor, so `c<leader<neighbor`, and (R) copies
the result across the new mirror pair. To pass from `e` to `e-g`, choose the
trailer in the nearer pair: its outward neighbor at distance `e` is a leader,
so again `c<leader<trailer`, followed by the mirror rule. For the inward
assertion, at distance `e+g` choose the leader there, which precedes its inward
neighbor at distance `e`, already below `c`; at distance `e-g` choose the
nearer leader, which precedes its outward neighbor at distance `e`, also below
`c`. The mirror rule completes each pair. The admissible distances are a
consecutive interval in the class `g/2 (mod g)`, so these two inductions reach
all of them. The argument works in either phase, hence the conclusion does not
require choosing the phase.

## Lemma 1: `Q+A3` fix the odd phase

**Claim.**  Under AP-freeness, `Q` and `A3` imply `b_5<b_3`.

Suppose instead that `b_3<b_5`.  On the odd `2`-ladder the leaders are then
the values congruent to `M+3 = 3 (mod 4)`.  Set

```
c*=m-1,        c**=m+1.
```

Thus `c* = 1 (mod 4)` is a `4`-flood center for the leader class `3 (mod 4)`,
while `c** = 3 (mod 4)` is itself a leader and is a `4`-flood center for the
class `1 (mod 4)`.

Compare `t_5` with `m`.

* If `t_5<m`, the `2`-flood centered at `m`, seeded by the mirror pair
  `{b_5,t_5}`, puts every odd value below `m`.  A `4`-flood at `c*` gives
  `b_3<c*` (the mirror is `t_5`), and a `2`-flood at `c*`, seeded by
  `c*<m`, gives `c*<t_10` (the mirror is `b_8`).  With `A3` this is the
  cycle `b_3<c*<t_10<b_3`.
* If `m<t_5`, the polar `2`-flood puts `m` below every odd value.  A
  `4`-flood at `c**` gives `c**<t_11` (mirror `b_13`), and a `2`-flood at
  `c**`, seeded by `m<c**`, gives `b_2<c**` (mirror `t_0`).  With `Q` this
  is the cycle `c**<t_11<b_2<c**`.

Both cases are impossible.  All displayed mirrors are in the block for
`M>=20`.

## Lemma 2: an 8-flood flip

**Claim.**  Under AP-freeness and `b_5<b_3`, the pair `P,A1` is impossible.

The odd `2`-ladder leaders are now the class `M+1 = 1 (mod 4)`.  Consequently,
whenever an odd leader is a `4`-flood center and the indicated mirror stays in
the block, it precedes every relevant value in the `3 (mod 4)` class.

First suppose `M=4 (mod 16)`.  Then `m=6 (mod 8)`.  Define

```
c=m-5 = 1 (mod 8),       d=m-1 = 5 (mod 8).
```

A `4`-flood gives `c<t_13`, whose mirror about `c` is `b_3`; hence `P`
gives `c<b_1`.  The `8`-flood centered at `c`, over the class of `b_1`,
then gives `c<d`.  Its seed mirror is `t_11` and its target mirror is `m-9`.
Similarly, a `4`-flood gives `d<t_5`, with mirror `b_3`; `A1` gives
`d<b_5`.  At the boundary `M=20`, `b_5=c`, so this already contradicts
`c<d`.  For `M>=36`, the `8`-flood centered at `d`, over the class of
`b_5`, gives `d<c`; here the seed mirror is `t_7` and the target mirror is
`m+3`.  This is a 2-cycle.  The tightest boundary in the first flood is
`m-9>=M+1`, equivalent to `M>=20`.

Now suppose `M=12 (mod 16)`.  Then `m=2 (mod 8)`.  Define

```
c=m-1 = 1 (mod 8),       d=m-5 = 5 (mod 8).
```

A `4`-flood gives `c<t_13` (mirror `b_11`), so `P` gives `c<b_1`.
The `8`-flood at `c` over the class of `b_1` gives `c<d`; its seed and
target mirrors are `t_3` and `m+3`.

For the reverse relation, a `4`-flood gives `d<t_13` (mirror `b_3`), and
`P` gives `d<b_1`.  Numerically `(b_1,d,t_11)` is an AP, so (R) gives
`d<t_11`.  A `4`-flood centered at the odd leader `t_11` gives `t_11<t_5`
(mirror `t_17`).  Thus `A1` gives `d<b_5`.  Finally the `8`-flood at `d`
over the class of `b_5` gives `d<c`; its seed and target mirrors are `t_15`
and `m-9`.  Again there is a 2-cycle.  The smallest integer in this subclass
is `M=28`, and every named value and mirror is then already in the block.

## Conclusion

Lemma 1 derives `b_5<b_3` from `Q,A3`; Lemma 2 says that orientation is
incompatible with `P,A1`.  Hence the four-attack subsystem `C4` is infeasible
for every `M>=20`, `M=4 (mod 8)`.  The full `OG(M)` contains `C4`, so it too
is infeasible on the frozen residue class.

`check_c4_uniform.py` checks every displayed AP, congruence, mirror, and order
inference on a long exact range.  `c4_exact_sat.py` separately constructs two
independent exact finite models; `c4_crosscheck.jsonl` records agreement at
the five prescribed scales.  These computations audit the schemas but are not
used to replace the universal argument above.
