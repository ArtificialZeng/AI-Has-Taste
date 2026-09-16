# Exact SAT nonexistence audit for the ternary length-11 case

Job: `win-00084-p06-research-fa957a0a5bec`  
Date: 2026-09-10  
Arithmetic: exact over `F_3`

## Claimed mathematical consequence

There is no rank-six matrix in `F_3^(6 x 11)` having four pairwise-disjoint
recovery sets for every column.  Combined with Theorem 23 of the frozen
primary source, which gives

`11 <= ASP(6,4,3) <= ASB(6,4,3) <= 12`,

this implies `ASP(6,4,3) = 12`.  The argument below reduces the existence
question exactly to a CNF and then checks a DRUP refutation of that CNF.

## 1. Complete reduction to normalized systematic matrices

Suppose first that a length-11 matrix `G` with the required property exists.

1. **There is no zero column.**  If a zero column were deleted, rank would
   remain six.  For every remaining target, delete that zero coordinate from
   each of its old recovery sets; spans and pairwise disjointness do not
   change.  This would give a length-10, dimension-six, four-all-symbol PIR
   matrix, contradicting the lower bound 11 in Theorem 23.  Thus every column
   of `G` is nonzero.
2. Choose six basis columns, permute them to the first six positions, and
   left-multiply by the inverse of their `6 x 6` submatrix.  Lemma 3 of the
   source (or direct multiplication of every recovery equation) shows that
   left multiplication preserves the property.  Hence it suffices to consider
   `G = (I_6 | A)` with five nonzero columns in `A`.
3. Multiplying an individual column `g_j` by a nonzero scalar preserves the
   property: an equation `g_i = sum_j alpha_j g_j` becomes
   `lambda_i g_i = sum_j (lambda_i alpha_j/lambda_j)(lambda_j g_j)`.
   Normalize each column of `A` so that its first nonzero entry is 1.
4. For any nonzero target `g_i`, four disjoint recovery sets exist if and only
   if there are three pairwise-disjoint recoveries avoiding coordinate `i`, in
   addition to `{i}`.  Indeed, at most one of four disjoint sets contains `i`.
   Replace that set by `{i}`; if none contains `i`, discard any one set and add
   `{i}`.  The converse is immediate.
5. Apply the preceding point to `e_1`.  Each of its three target-avoiding
   recoveries must use an `A` column whose first coordinate is nonzero, because
   `e_2,...,e_6` all have first coordinate zero.  Disjointness makes these
   three `A` columns distinct.  After projective normalization their first
   entries are 1.  Permuting the five `A` columns therefore permits the
   convention that the first three entries in row 1 are 1 and that every
   row-1-nonzero `A` column precedes every row-1-zero `A` column.

All transformations above are reversible up to the stated symmetries, so they
lose no possible matrix.

## 2. Meaning of the CNF

`evidence/systematic_sat_search.py` constructs the fixed file
`evidence/systematic_search.cnf`.  It has 7,428 variables and 34,731 clauses.
Every field-valued variable is represented by three Boolean literals and has
one at-least-one and three pairwise at-most-one clauses, so it takes exactly
one value in `{0,1,2}`.

### Matrix clauses

The variables `a_r_p` are the 30 entries of `A`.

- One clause per parity column requires at least one nonzero entry.
- For row `r`, the clause saying “an earlier entry is nonzero, or `a_r_p` is
  not 2” makes the first nonzero entry equal to 1.
- Unit clauses set the first entries of parity columns 1--3 to 1.
- The four adjacent clauses forbid a row-1-zero column immediately before a
  row-1-one column.  Since normalization already forbids 2 in row 1, these
  clauses put all row-1 ones before all row-1 zeros.

These are exactly the normalizations justified in Section 1.

### Recovery clauses

For each target `t` and each of three nontrivial recoveries `s`, the trits
`c_t_s_j` are coefficients on the eleven columns.

- `c_t_s_t = 0` makes the recovery avoid its target.
- For a fixed target and coordinate, binary clauses forbid two distinct
  recoveries from both having a nonzero coefficient there.  Thus their
  coefficient supports are pairwise disjoint.
- Every recovery has exactly one `minimum_t_s=j` variable.  That choice forces
  coefficient `j` to be nonzero and every earlier coefficient to be zero.
  Further clauses require the three minima to increase strictly.  Every
  nonempty collection of three disjoint supports can be ordered this way, so
  this removes only the permutation symmetry of the recoveries.

For row `r`, the encoded equation is

`c_t_s_r + sum_(p=0)^4 c_t_s_(6+p) a_r_p = (g_t)_r`.

When `t=r<6`, the first term is omitted because it is already fixed to zero.
For a systematic target the right side is the appropriate unit-vector entry;
for a parity target it is `a_r_(t-6)`.  Multiplication and addition gates use
all nine input pairs in their complete modulo-3 truth tables.  Exact-one trits
therefore make every gate, and hence every displayed equation, exact.

## 3. Soundness and completeness of the encoding

From a satisfying assignment, decode the one-hot `A` entries and coefficients.
The matrix is `(I_6|A)`, hence has rank six; the matrix clauses make all parity
columns nonzero and normalized.  For every target, the three coefficient
supports avoid the target and are pairwise disjoint, and the row equations say
that each recovers the target.  Adding the singleton target gives four
pairwise-disjoint recovery sets.

Conversely, normalize any putative matrix as in Section 1.  Choose coefficient
representations for three target-avoiding disjoint recoveries and remove
coordinates with zero coefficients.  Each support is nonempty because its
target is nonzero.  Order the three supports by their distinct least indices,
assign the corresponding coefficient and minimum trits, and assign every
arithmetic gate its actual value in `F_3`.  Every clause is then satisfied.

Thus the CNF is satisfiable if and only if the frozen length-11 matrix exists.

## 4. Differential validation of the encoder

`evidence/validate_sat_encoding_broad.py` is a separate semantic oracle.  For
each fixed `A`, it enumerates all 121 projective directions of the
five-dimensional kernel of `(I_6|A)`, derives every target-avoiding recovery
support, and computes the exact maximum disjoint packing by a union-mask
dynamic program.  It does not reuse the encoder's arithmetic gates, recovery
variables, or model decoder.

The saved report `evidence/encoding_validation_broad_report.json` covers 25
normalized matrices (five structured/degenerate cases and 20 seeded cases),
all eleven targets, and both Minisat22 and CaDiCaL 1.9.5.  All 550 solver
statuses agree with the oracle, with both positive and negative individual
target instances represented; there are zero mismatches.  This finite test is
an encoding audit, not the nonexistence proof.

## 5. Certified UNSAT result

The decisive byte bindings are:

- CNF: `a0b8624f0f8b19b8f114b266f87cb72879add9ec60ed3fd555f9cfd549e821be`
- Glucose4 DRUP trace:
  `4c97d3c4b46ddbbe6f286a151b91a2ff8f16fb7452054685ac806160e57a84a3`

The Glucose report records UNSAT and 833,442 proof lines.  In this pass,
`evidence/replay_drup.py` reread the fixed CNF and trace using Minisat22 only
as a unit-propagation engine.  For every nondeletion proof clause `C`, it ran
unit propagation under the negation of every literal of `C`, required a
conflict, and only then retained `C`.  It checked 426,775 RUP additions,
ignored 406,667 deletions by retaining those already-validated clauses, and
reached the empty clause on the final proof line.  The pass-2 report is
`evidence/systematic_drup_replay_pass2.json` and has `accepted: true`.

This replay rule is sound by induction.  The input formula entails each
retained RUP clause because its negation unit-propagates to contradiction in a
database consisting only of the input and previously entailed clauses.
Ignoring deletions preserves those consequences and therefore does not change
the formula's models.  The final entailed empty clause proves the CNF
unsatisfiable.

As a nondecisive cross-check, a fresh CaDiCaL 1.9.5 run regenerated a
byte-identical CNF and also returned UNSAT.  Its Python proof export omitted a
final empty clause, so `evidence/systematic_cadical_drup_replay.json` correctly
has `accepted: false`; that incomplete trace is not used as a certificate.
No external DRAT-to-LRAT checker was installed in the bounded environment.

## Gap list

No mathematical or certificate gap is known in the stated finite
nonexistence result.  The literature/novelty status remains bounded by the
search documented in `literature/triage-search-20260910.md`; priority is not
claimed here.  A fresh referee should independently audit the reduction and
replay the fixed certificate before accepting the resolution.
