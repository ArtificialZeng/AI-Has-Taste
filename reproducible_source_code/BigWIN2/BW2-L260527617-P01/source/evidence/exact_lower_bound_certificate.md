# Exact certificate for the lower bound `L(3,5) >= 20`

## Claim and conventions

For the precise free-group problem fixed in `source.md` and `problem.md`, no
3-out-of-5 admissible element has reduced length at most 18.  Consequently

\[
20\leq L(3,5)\leq 26,
\]

where the upper bound is the explicit word checked by
`evidence/verify_upper26.py`.  This does not determine the exact value.

It is convenient to describe a deletion by the generators it *retains*.
Deleting three generators retains a pair, whose projection must be the
identity.  Deleting two retains a triple, whose projection must be nonidentity.

## Complete finite reduction

Every generator occurs in an admissible word.  Indeed, if generator `g` were
absent, then for any two other generators `a,b` the retained-triple projection
on `{a,b,g}` would equal the retained-pair projection on `{a,b}`.  The former
is required nonidentity and the latter identity, a contradiction.

For every generator `g`, retain any pair containing `g`.  Its identity
projection has exponent sum zero in `g`; hence the original word has equally
many `+g` and `-g` letters.  Thus the unsigned occurrence count `c_g` is a
positive even integer.  In particular every admissible length is even and at
least 10.

Conjugating a word commutes with every deletion homomorphism and preserves
identity versus nonidentity.  A shortest admissible word is therefore
cyclically reduced: otherwise removing inverse first and last letters by
conjugation gives a shorter admissible word.  Permuting generators, inverting
any generators independently, and cyclically rotating a cyclically reduced
word also preserve admissibility and length.

After sorting `(c_1,...,c_5)`, the complete list through length 18 is:

| length | sorted unsigned-count patterns |
|---:|---|
| 10 | `(2,2,2,2,2)` |
| 12 | `(2,2,2,2,4)` |
| 14 | `(2,2,2,2,6)`, `(2,2,2,4,4)` |
| 16 | `(2,2,2,2,8)`, `(2,2,2,4,6)`, `(2,2,4,4,4)` |
| 18 | `(2,2,2,2,10)`, `(2,2,2,4,8)`, `(2,2,2,6,6)`, `(2,2,4,4,6)`, `(2,4,4,4,4)` |

`evidence/audit_exact_encoding.py` independently enumerates these positive
even partitions and checks that there are respectively `1,1,2,3,5` cases.

## Exact CNF semantics

`evidence/search_exact_sat.py` constructs one CNF for each row entry.  At each
word position, exactly one of the ten signed generators is selected; adjacent
inverse letters are forbidden.  Sequential-counter constraints require
exactly `c_g/2` copies of each of `+g` and `-g`.

For every retained pair or triple `R` and interval `[i,j)`, a Tseitin variable
`E_R(i,j)` is defined by the equivalence

\[
E_R(i,j)\iff
\begin{cases}
E_R(i+1,j),&w_i\notin R,\\
\displaystyle\bigvee_{i<k<j}
  (w_k=w_i^{-1}\land E_R(i+1,k)\land E_R(k+1,j)),&w_i\in R.
\end{cases}
\]

with `E_R(i,i)=true`.  This is exactly the standard noncrossing-pair grammar
for a word freely reducing to the identity.  For completeness, if a projected
interval reduces to the identity and its first retained letter is `w_i`, that
letter is popped by a uniquely determined later inverse `w_k`; the intervening
and following subwords both reduce to the identity.  The converse follows by
performing those two reductions and cancelling `w_i w_k`.  Induction on
interval length proves the displayed equivalence.  The CNF requires
`E_R(0,L)` for all ten pairs and its negation for all ten triples.

The symmetry constraints retain a representative of every possible shortest
word.  Sort generators by `c_g`; rotate to an occurrence of a least-count
generator, relabel it `1`, and invert its sign so the first letter is `+1`.
Within each equal-count block, label generators by first occurrence.  Finally
invert each remaining generator if necessary so its first occurrence is
positive.  Cyclic reduction makes the last letter different from `-1`.
These are exactly the constraints implemented for a fixed count pattern; no
heuristic pruning is used.

`evidence/audit_exact_encoding.py` regenerated all 12 stored CNFs clause for
clause from the encoder and found them identical.  It also compared the
interval grammar with an independent stack reducer on all 335,923 words of
length at most 7 over two retained generators and one ignored generator.

## UNSAT certificates and replay

The 12 corresponding `.drup` files all end in an empty-clause addition.
The corrected run provenance in `evidence/provenance-correction.md` identifies
PySAT 1.8.dev24 with solver name `glucose3` as their producer, not CaDiCaL
1.9.5.  Independently of that historical record,
`evidence/audit_glucose_reproduction.py` reran every case with `glucose3` and
reproduced all 12 CNFs and all 12 proof files byte for byte; hashes and exact
comparisons are recorded in `evidence/glucose_reproduction_audit.json`.

Proof validity does not depend on the producer attribution.
`evidence/audit_drat_trim.py` ran `drat-trim` separately on every archived
CNF/DRUP pair.  Every process returned exit code zero and emitted exactly one
line `s VERIFIED`; `evidence/drat_trim_audit.json` binds all verdicts to the
CNF, proof, checker, and raw-output SHA-256 digests, and
`evidence/drat_trim_replay.log` preserves the complete outputs.

As a second replay path, `evidence/check_drup.py` checked every addition using
MiniSat 2.2 unit propagation: for each proposed clause `C`, it assumed the
negation of every literal of `C` and required a conflict before adding `C`.
Deletion lines are conservatively ignored.  This is sound because retaining
an already checked consequence only strengthens the working formula, while
induction shows that every retained learned clause is entailed by the original
CNF.  Its exact hashes and replay counts are in `evidence/drup_replay.log`.

As a nondecisive cross-check, the separate integer/array encoding in
`evidence/search_exact_z3.py` returned `unsat` at length 10 with both its stack
and interval-grammar encodings (Z3 4.15.3).  The DRUP replay, not this
cross-check, is the proof-producing exclusion.

Combining the complete finite reduction, exact CNF equivalence, exhaustive
count-pattern coverage, and checked empty clauses excludes a shortest
admissible word of every possible length below 20.  The next unresolved test
is length 20, with its seven positive-even count patterns.
