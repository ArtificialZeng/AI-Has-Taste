# Breaker / Certifier / Referee report

Date: 2026-08-29  
Scope: only `15_type_d9_normalized_flow`  
Arithmetic: integers and `fractions.Fraction`; no floating point, random
search, modular inference, or proof assistant.

## Outcome of this branch

No infeasibility witness exists for the tested quotient LP: the supplied
`discovery/d9_orbit_flow_candidate.json` passes an independent exact verifier.
Subject to the elementary signed-cycle classification and the lifting argument
spelled out below, it is an exact normalized flow for `Abs(D_9)`, not merely
numerical evidence.

The audit also reproduces element-by-element finite baselines for `D_4`,
`D_5`, and `D_6`, and checks the formula-level cell multiplicities against
complete enumeration for every orbit pair in those three groups.

## Definitions rebuilt from scratch

An element of `D_n` is an even signed permutation

```text
w(e_i) = (-1)^(a_i) e_(sigma(i)),   sum_i a_i = 0 mod 2.
```

For every cycle of `sigma`, call it positive or negative according as the xor
of its `a_i` labels is zero or one.  If `p(w)` is the number of positive
cycles, Carter's codimension formula gives

```text
rank(w) = codim Fix(w) = n - p(w).
```

The reflections are the `n(n-1)` signed transpositions: for every unordered
pair `{i,j}`, either both signs are zero or both signs are one.  The complete
element enumerator declares `w -> wt` to be an upper cover exactly when `t` is
one of these reflections and `rank(wt)=rank(w)+1`.

The quotient used by the D9 certificate is the action of `B_n` by conjugation
on the normal subgroup `D_n`.  Its cells are indexed by a bipartition
`(lambda,mu)`, where `lambda` lists positive-cycle lengths and `mu` lists
negative-cycle lengths; `len(mu)` is even.  The cell size is

```text
             2^n n!
|O_(l,m)| = ------------------,
             2^(l(l)+l(m)) z_l z_m
```

where `z_l = product_i i^(m_i) m_i!`.  These cells sum exactly to
`2^(n-1)n!`.

This is a legitimate automorphism quotient even when one `B_n` class splits
into two `D_n` conjugacy classes: `D_n` is normal in `B_n`, and conjugation by
`B_n` preserves the set of `D_n` reflections and hence absolute order.

## Independently reconstructed cover support and multiplicities

The formula verifier represents every signed cycle as `(length,sign)` and
generically performs all cycle joins and splits.  It retains a surgery only
when `n-#positive_cycles` increases by one.  Thus the familiar three upper
operations are *derived* rather than assumed:

- join two positive cycles to a positive cycle;
- join a positive and a negative cycle to a negative cycle;
- split one positive cycle into two negative cycles.

For a fixed source element, joining cycles of lengths `a,b` contributes
`2ab` reflections.  Splitting a positive cycle of length `L` into negative
cycles of lengths `a,L-a` contributes `L` reflections if `a<L/2`, and `L/2`
if `a=L/2`.  Summing over repeated cycles gives the exact out-degree
`d_(O,O')`.  Hence

```text
E_(O,O') = |O| d_(O,O'),
d'_(O,O') = E_(O,O') / |O'|.
```

The verifier checks that every `d'` is a positive integer.  It also checks the
global identity

```text
sum_(O,O') E_(O,O') = |D_n| n(n-1)/2,
```

which follows because every pair `(w,t)` lies on one end of a unique cover and
is counted once upward and once downward.

If the candidate quotient flow assigns total mass `F_(O,O')` to a cell pair,
the independently reconstructed full-edge lift is

```text
f(x,y) = F_(O,O') / E_(O,O')
```

for every cover `x -> y` in that cell pair.  Exact quotient conservation then
gives, for each `x in O` and `y in O'`,

```text
sum_y f(x,y) = 1/|rank_i|,
sum_x f(x,y) = 1/|rank_(i+1)|.
```

The verifier nevertheless recomputes both equalities explicitly as rational
identities for every quotient cell at every rank transition.

## Exact results

### Complete element baselines

| group | order | rank sizes | B-cells | D-conjugacy orbits | full covers | status |
|---|---:|---|---:|---:|---:|---|
| `D_4` | 192 | `1,12,50,84,45` | 11 | 13 | 1,152 | ACCEPT |
| `D_5` | 1,920 | `1,20,150,520,809,420` | 18 | 18 | 19,200 | ACCEPT |
| `D_6` | 23,040 | `1,30,355,2100,6439,9390,4725` | 34 | 37 | 345,600 | ACCEPT |

The complete enumeration detects the split `D_n` conjugacy classes:

- `D_4`: `P[2,2]N[-]`, `P[4]N[-]`;
- `D_5`: none;
- `D_6`: `P[2,2,2]N[-]`, `P[4,2]N[-]`, `P[6]N[-]`.

Every one of the 16, 36, and 83 quotient cover-cell multiplicity triples
`(E,d_out,d_in)` for `D_4,D_5,D_6` agrees between the complete enumerator and
the generic surgery formulas.

### D8 baseline candidate

```text
|D_8|                         = 5,160,960
B_8 orbit cells               = 95
quotient support pairs        = 330
nonzero quotient flows        = 172
full Hasse covers             = 144,506,880
candidate status              = ACCEPT
```

### D9 target candidate

```text
|D_9|                         = 92,897,280
rank sizes                    =
  1, 72, 2220, 38304, 405174, 2702448,
  11228300, 27491616, 34812945, 16216200
B_9 orbit cells               = 150
quotient support pairs        = 609
nonzero quotient flows        = 284
full Hasse covers             = 3,344,302,080
candidate status              = ACCEPT
lifted equations              = exact rational
```

The D9 candidate SHA-256 is
`1139852c155f754f6b998b15bf3fcd0f42942351a609e283615cb7599002beca`.
The formula verifier SHA-256 at this audit is
`fb1e14209cbdb299a98c7049c8c0b23c8ad0467070c3ef06b9d445fbeb6284da`.

## Adversarial rejection tests

The two verifiers fail closed on malformed or incomplete inputs.  Automated
mutations change a rank size, delete a type, change a cell-edge multiplicity,
change a flow numerator/cleared amount, change a class size, or corrupt the
split-class list.  Every mutation is rejected.

## Referee warnings

1. **There is no ordinary rank symmetry.**  The rank polynomial
   `product_i(1+e_i q)` is not palindromic.  Already `D_4` has ranks
   `1,12,50,84,45`.  No rank transition may be omitted on a bare appeal to
   “rank symmetry.”
2. **Name the quotient action.**  Calling the cells merely “conjugacy classes
   of `D_n`” is false in even rank when a class splits.  The compact candidate
   uses `B_n`-conjugacy cells in `D_n`, which is valid for the reason above.
3. **Do not confuse quotient mass with per-edge mass.**  The lift divides
   `F_(O,O')` by the total original edge count `E_(O,O')`, not by an orbit
   size, one-sided degree, or nothing at all.
4. **Finite result only.**  The accepted D9 certificate contains no proved
   recurrence `D_n -> D_(n+1)`.  It certifies `D_9`; extrapolation remains a
   separate conjectural route.
5. The D9 verifier does not enumerate all 92,897,280 group elements.  Its
   generic cell-degree formulas are exact combinatorics, and their complete
   element-level validation through `D_6` is an independent regression test,
   but the manuscript must include a human proof of the cycle surgery and
   degree formulas.

## Reproduction commands

Run the exact D9 verifier and its rejection tests:

```bash
python tests/verify_breaker_orbit_candidate.py \
  discovery/d9_orbit_flow_candidate.json --self-test-mutations
```

Rebuild and independently verify the last element-level baseline in this
branch:

```bash
python discovery/breaker_element_audit.py 6 \
  --output discovery/breaker_d6_element_audit.json
python tests/verify_breaker_element_certificate.py \
  discovery/breaker_d6_element_audit.json --self-test-mutations
```

Run all cross-checks, including D8/D9 and the cellwise comparison between the
generic formulas and complete `D_4,D_5,D_6` enumerations:

```bash
python -m unittest -v tests/test_breaker_crosscheck.py
```

## Files created by this branch

- `discovery/breaker_element_audit.py`
- `discovery/breaker_d4_element_audit.json`
- `discovery/breaker_d5_element_audit.json`
- `discovery/breaker_d6_element_audit.json`
- `tests/verify_breaker_element_certificate.py`
- `tests/verify_breaker_orbit_candidate.py`
- `tests/test_breaker_crosscheck.py`
- `notes/breaker.md`

