# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the exact `resolution-paper` claim frozen in
`audit/snapshot.json` (snapshot digest
`9192d4d22df71aa3cafa514ea148858d23e56a971b396d396d0208e56f29727c`).
The SHA-256 digests of `source.md`, `problem.md`, `claim.json`, and all three
listed files under `evidence/` agree with the snapshot.  The immutable source
still has digest
`3359f80c72e10e411b339956c0e9bffb5fb0dd12ead27f9abc277b088c588622`.
The claim is full-scope: arbitrary field, every `n,m >= 2`, all three requested
invariants, all small cases, and the Cohen--Macaulay classification.

## Reconstruction of the argument

Let `X=x_1...x_n` and let `Y[a,b]=y_a...y_b`.  Direct distance counting in
the original broom gives the leaf ball `X Y[1,min(m,3)]`.  A ball centered at
`y_j` contains the leaves precisely for `j <= 3`; its path part has indices
from `max(1,j-3)` through `min(m,j+3)`.  After deleting duplicates and proper
multiples, this gives a principal ideal `(X Y[1,m])` for `m=2,3`, and for
`m>=4` gives exactly

```
I_(n,m)=(X Y[1,3], Y[a,a+6] for 1<=a<=m-7, Y[m-3,m]).
```

The last possible seven-windows are removed because they contain the terminal
four-window; no two displayed supports contain one another.  This checks the
structural reduction used by the proof, including `m=4,...,8`.

The mapping-cone lemma used in the evidence is valid in the required strength.
For a monomial ideal `A` in variables not including `u` and `f=uv`, the exact
sequence is

```
0 -> R/(A:v)(-deg f) --f--> R/A -> R/(A,f) -> 0.
```

Choose minimal multigraded resolutions over the variables of `A`.  After the
multidegree shift by `f`, every nonzero entry of a comparison map has positive
`u`-degree, whereas the two original differentials are minimal.  Thus the cone
is minimal.  The same reasoning works for a product of new variables.  It
therefore gives the asserted exact maxima for projective dimension and
regularity, rather than mere upper bounds.

For the auxiliary terminal interval ideal `L_t`, separating its first
seven-window gives, for `t>=8`,

```
L_t=(z_1...z_7)+L_(t-1),
(L_(t-1):z_1...z_7)=(z_8)+L_(t-8),
```

with the latter ideal supported on `z_8,...,z_t`.  Dividing the shifted
generators verifies the colon identity: all windows beginning at positions
`2,...,8` become multiples of `z_8`, and the later windows and terminal
four-window are exactly `L_(t-8)`.  This also checks the overlap cases
`8<=t<=11`.  Hence, with quotient invariants `p_t,r_t`,

```
p_t=max(p_(t-1),p_(t-8)+2),
r_t=max(r_(t-1),r_(t-8)+6).
```

The bases are `(0,0)` for `0<=t<=3` and `(1,3)` for `4<=t<=7`.
Substitution, separately in all four residue classes modulo four, proves

```
p_t=floor(t/4),   r_t=3 floor(t/4).
```

For the radius-three path ideal `Q_t`, separating the left terminal
four-window gives

```
Q_t=(z_1z_2z_3z_4)+L_(t-1),
(L_(t-1):z_1z_2z_3z_4)=Q_(t-4)
```

for `t>=5`.  Direct division checks `t=5,...,8`; thereafter the first surviving
seven-window supplies the new left four-window, the next three quotients are
multiples of it, and the remaining generators are precisely those of
`Q_(t-4)`.  The resulting minimal recurrence and the principal bases
`1<=t<=4` give

```
pd(K[z]/Q_t)=ceil(t/4),
reg(K[z]/Q_t)=t-ceil(t/4).
```

Finally,

```
I_(n,m)=(X Y[1,3])+L_m,
(L_m:Y[1,3])=Q_(m-3)
```

for `m>=4`.  The colon identity again follows generator by generator and is
valid at the first endpoint `m=4`.  Since all `x_i` are new variables for
`L_m`, the minimal cone gives

```
pd(S/I_(n,m))=max(floor(m/4),ceil((m-3)/4)+1)
             =floor(m/4)+1,

reg(S/I_(n,m))
 =max(3 floor(m/4), n+2+(m-3)-ceil((m-3)/4))
 =n+m-1-floor(m/4).
```

Here `ceil((m-3)/4)=floor(m/4)`.  If `m=4c+s`, `0<=s<=3`, the second
regularity entry exceeds the first by `n+s-1>0`, using the stated hypothesis
`n>=2`.  For `m=2,3`, the ideal is principal of degree `n+m`, so both formulas
continue to hold.  Thus the assertion of no exceptional small values is
justified.

## Height and Cohen--Macaulay cases

The ideal is squarefree, so height is the minimum cardinality of a cover of
the displayed generator supports.  The cases `m=2,3` have height one.  For
`4<=m<=6`, `y_(m-3)` meets both displayed generators, again giving height one.

For `m>=7`, write `m=7q+r` with `0<=r<=6`.  The leaf support, the `q-1`
seven-windows

```
Y[4+7i,10+7i]  (0<=i<=q-2),
```

and the terminal support `Y[m-3,m]` are `q+1` pairwise disjoint generator
supports (with the middle list empty when `q=1`).  The last middle interval
ends at `7q-4`, before the terminal interval begins.  This proves the lower
bound `q+1`.  Conversely,

```
{y_(3+7i):0<=i<=q-1} union {y_(m-3)}
```

has `q+1` distinct vertices, meets the leaf and terminal supports, and meets
every seven-window because successive marked indices are at most seven apart,
with the boundary gaps also covered.  Therefore

```
ht(I_(n,m))=floor(m/7)+1
```

in every case.

Auslander--Buchsbaum in the ambient polynomial ring reduces
Cohen--Macaulayness to `pd=ht`.  Thus one must solve
`floor(m/4)=floor(m/7)`.  The common value zero gives `m=2,3`; the common
value one gives only `m=7`; and for a common value `k>=2`, the intervals
`[4k,4k+3]` and `[7k,7k+6]` are disjoint.  Hence the classification
`m in {2,3,7}` for every `n>=2` is exact.

## Independent checks actually performed

I parsed the frozen exact table independently of its stored summary and checked
its 46 cases against the three formulas.  I also performed a separate exact
calculation that did not import the submitted verifier: it reconstructed the
radius-three balls by BFS for `n=4`, formed the minimal supports, and computed
multigraded Tor as the homology of each multidegree strand of the Taylor
resolution.  Boundary ranks were computed over both the rationals and
`F_2`; height was recomputed by exhaustive hitting-set search.  For

```
m = 2,3,4,6,7,8,9,11,12,13,14,15,
```

both fields gave exactly the claimed projective dimension and regularity, and
the exhaustive heights gave `floor(m/7)+1`.  These checks include values of `n`
outside the submitted table and all relevant early transition points.  They
are corroborative only; the quantified result is established by the exact
colon identities and minimal recurrences above.

## Source comparison, gaps, and verdict

The frozen source comparison identifies the cited nearby work as treating the
square/radius-two broom ideal, while this claim treats the cube/radius-three
family with seven-variable interior windows and four-variable terminal
windows.  No bibliographic-priority claim is part of the candidate, and this
review makes none.  Within the authorized frozen evidence, the mathematical
delta and the full-scope resolution are clear; later citation review may audit
the bibliographic description separately.

I found no missing endpoint, unproved cancellation assertion, characteristic
restriction, or gap in the height argument.  The claim settles the original
problem exactly as frozen, and its stated contribution is commensurate with
that scope.

**Verdict: accept.**
