# All-length colex-successor proof of the even-period formula

This note completes the dynamical step left open in
`block_transducer_certificate.md`.  It uses the same generic block alphabet,
path graph, zero padding, and exact five-block rule for `H=F^3`.

## Ordered predecessor lists

Adjoin a formal right boundary symbol `0`; at that boundary the permitted
predecessors are the terminal set `INNER`.  Give every predecessor set the
following order:

```
O_0       = (1,9,13,14,6,2,15)
O_1=O_2   = (14,6,2,15,1,9,13)
O_4=O_6   = (8,12,4,14,6,2,15)
O_8=O_9   = (15,1,9,13,8,12,4)
O_12=O_13=O_14=O_15 = (15).
```

Apart from the formal endpoint case, direct comparison with `NEXT` shows
that `O_t` is exactly the set of generic blocks `a` satisfying `t in
NEXT[a]`.  Thus these lists order all, and only, possible predecessors.

For a side `X` in `{L,R}`, define an ordered list `E_m^X(t)` of length-`m`
prefixes recursively.  On the left,

```
E_1^L(t) = ((a): a occurs in O_t and a is in OUTER),
```

in the inherited order.  On the right the first (central) block has the base
orders

```
C_8=C_9=(3,0),  C_4=C_6=(0,3),  C_t=(3) otherwise,
```

and `E_1^R(t)=((a):a in C_t)` for generic `t`, while the exceptional
zero-length-generic language is `E_1^R(0)=((3))`.  For `m>1`, on either side,

```
E_m^X(t) = concatenation over a in O_t of
           (v,a) for v in E_(m-1)^X(a).
```

Induction on `m`, using that each `O_t` is the complete predecessor set,
proves that these lists contain every admissible path exactly once.  In
particular, for `i>=1`, `E_i^L(0)` is exactly `L_i`, and
`E_(i+1)^R(0)` is exactly `R_i`.  The cases `i=0` are respectively the empty
left word and `(3)`.

## Successor lemma

**Lemma.**  On both sides and at every length, the zero-padded map `H` sends
each word of `E_m^X(0)` to the next word of that list, cyclically.

Here is a finite, reproducible induction certificate for the lemma.  Let
`Q_m^X(t)` be the set of aligned pairs of adjacent words in `E_m^X(t)` (not
including wraparound).  The recursive definition gives the exact identity

```
Q_m^X(t) = union over a in O_t of Q_(m-1)^X(a) appended by (a,a),
           together with, for consecutive a,b in O_t, the single pair
           (last(E_(m-1)^X(a)),a) -> (first(E_(m-1)^X(b)),b).
```

The first and last words obey the same one-symbol recursion.  Consequently,
all length-at-most-five factors and five-symbol boundary segments of these
aligned pair languages, including aligned pairs of extrema, obey a finite
deterministic set recurrence.  No word enumeration or cutoff assumption is
made in this recurrence.

The script `research_colex_certificate.py` implements that recurrence.  For
each aligned transition `x -> y`, it checks every interior record

```
local_rule(x[j-2:j+3]) = y[j]
```

and the four zero-padded boundary/spill records.  This is sufficient because
`H` has block radius two.  Short lengths are checked directly.  The entire
finite summary state at left lengths 7 and 8 is identical; the entire state
at right lengths 8 and 9 is identical.  Since the summary update is
deterministic (and both repetitions occur after the five-block window length),
induction gives the same verified state at every later length.  The cyclic
last-to-first pair is included separately at every step.  The exact transcript
is `research_colex_certificate.txt`.  This proves the lemma for all lengths.

Because each recursively ordered list contains every admissible word exactly
once, the lemma says that each induced factor permutation is one cycle.  This
also explains the previously observed seven terminal runs: they are precisely
the seven top-level groups indexed by `O_0`; their prefix traversals are the
shorter lists `E_(m-1)^X(a)`.

## Least period

The previously proved block-transducer lemma gives, for every `i>=0`, exact
invariance and independence of the two factors.  Their cardinalities are

```
A_i = (4^(i+1)-1)/3,
B_i = (2*4^(i+1)-5)/3.
```

The successor lemma proves that these cardinalities are their **least**
`H`-periods, not merely return times.  Moreover `B_i=2*A_i-1`, hence
`gcd(A_i,B_i)=1`; independence therefore makes the least full sampled period
`A_i*B_i`.

Outside the finite defect, the uniform pair follows

```
(0,0) -> (0,1) -> (1,0) -> (0,0).
```

Thus no return to the original finite configuration occurs at a time not
divisible by three.  Since `H=F^3`, the least `F`-period is consequently

```
3*A_i*B_i
 = ((4^(i+1)-1)*(2*4^(i+1)-5))/3
 = (2*4^(2i+2)-7*4^(i+1)+5)/3.
```

This includes `i=0`, where both factor cycles have length one and the least
period is three.  Hence the frozen conjecture holds for every integer `i>=0`.

## Dependency and scope audit

The proof depends on (1) the exact definitions in `problem.md`, (2) the
all-length invariance/decoupling lemma in `block_transducer_certificate.md`,
(3) the path-count proof in `three_step_factor_structure.md`, and (4) the
all-length colex-successor certificate here.  No literature novelty claim is
made by this mathematical certificate.  The only computer-assisted step is a
finite exact truth-table/finite-state induction check; its scripts, recurrence,
window radius, stabilization lengths, and transcripts are disclosed above.
