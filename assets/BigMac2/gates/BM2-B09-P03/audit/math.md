# Fresh mathematical audit

Referee job: `bigMac-00009-p03-referee-f8c9131a6de4`  
Frozen snapshot: `eedc974190423e8943ef82f6b963b7444c569a84a97db0d7dab2272f1b5f3797`

## Scope reviewed

The frozen claim is the full resolution of the question in `source.md`, under
the precise reading in `problem.md`: the alphabet is the union over all four
admissible levels for one fixed ordering, factors have arbitrary positive
stochastic weights on their supports, and the requested horizon is uniform
over all factor words.  The candidate does not replace this alphabet by the
level-four component, choose a level separately for each test, or restrict the
weights.  Its asserted value is

\[
h_{\rm scr}(\mathcal A_4)=11.
\]

I recomputed the SHA-256 digest of every file named by
`audit/snapshot.json`; every digest, including those of `source.md`,
`problem.md`, and `claim.json`, agrees with the frozen mapping.

## Reconstruction of the decisive argument

Every stochastic support is a four-tuple of nonzero four-bit row masks, so
there are exactly \(15^4=50{,}625\) possibilities.  Conversely each such
support has a positive stochastic realization, obtained for example by
putting equal positive mass on the supported entries of each row.  Because
all factors are nonnegative, the support of a product is its Boolean support
product.  Thus both the upper and lower bounds may be decided entirely at the
support level, without any generic-weight or cancellation assumption.

For each support and level \(r\), the programs test row-allowability and GR on
the leading \(r\)-block, row-allowability and GE on every larger leading
block, and the bottom-left row-allowability condition.  I checked these tests
against the displayed definitions.  In particular, when the two image sets
are disjoint, the GE comparison is
\(|F(I)\cup F(J)|\ge |I\cup J|\), while GR uses the integer-equivalent test
\(|F(I)\cup F(J)|\ge |I\cup J|+1\).  The level-four rectangular condition is
correctly vacuous, and taking the Boolean union of the four level tests
correctly handles supports admitted at more than one level.  The resulting
legal alphabet has 37,833 distinct supports.

Let \(L\) be that alphabet and let \(F_0\) contain only the Boolean identity.
The computed recurrence is

\[
F_{d+1}=\{A B:A\in L,\ B\in F_d,\ AB\text{ nonscrambling}\}.
\]

This recurrence is exhaustive even though scrambling intermediate states are
discarded.  Indeed, if \(B\) is scrambling and \(A\) is row-allowable, choose
an index \(k\) supported in row \(i\) of \(A\) and an index \(\ell\)
supported in row \(j\).  Rows \(k,\ell\) of \(B\) meet in some column, which
then lies in both corresponding rows of \(AB\).  Hence left multiplication
by a legal factor preserves scrambling.  Induction therefore identifies
\(F_d\) with the complete set of nonscrambling products of exact length
\(d\).

The complete frontier cardinalities freshly reproduced from the frozen
inputs are

| length | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(|F_d|\) | 1 | 19946 | 13532 | 9802 | 6258 | 3332 | 1720 | 988 | 566 | 316 | 120 | 0 |

Thus every eleven-factor product is scrambling.  The frozen ten-factor word

`a126, 423a, c586, a215, 4643, 21a6, 42a3, 9368, 3126, 2345`

has each factor in the rebuilt legal alphabet and has Boolean product `17ef`.
In the row-packed convention its rows are `[f,e,7,1]`; rows 2 and 4 have
disjoint masks `e` and `1`.  It is therefore a legal nonscrambling product of
length ten.  Together the two facts give the claimed exact horizon.

## Checks actually performed

- I inspected both C++ implementations line by line against the frozen
  definitions, including mask orientation, leading-block truncation,
  disjoint-subset quantifiers, the union over levels, Boolean multiplication,
  and the scrambling predicate.
- I compiled and freshly ran `verify_certificate.cpp`.  It enumerated all
  65,536 relations, independently rebuilt the legal union using ternary
  assignments for disjoint row subsets, recomputed every complete frontier,
  and directly multiplied the witness.  It accepted the full certificate;
  the fresh output is `audit/referee_recheck.txt`.
- I also compiled and freshly ran `search_exact.cpp` to new audit-side output
  paths.  The regenerated result JSON and 94,442-line certificate are
  byte-for-byte identical to the frozen files, with SHA-256 digests
  `26889934f9036be2405171be7a453613ca5a24bed9d7e7c69ba80b628940d8fe`
  and `a2b338958bad75f6fd2ed97343928994f4c88f25193d78532b6dc02762d82fa7`,
  respectively.
- The code does not use floating point or sample weights.  Its state space is
  the entire 16-bit relation space, so no legal support pattern is omitted.

## Source comparison and limitations

The frozen source asks for exactly a longest nonscrambling Boolean word and a
complete upper-bound certificate over all legal supports; the reviewed claim
supplies both at the original scope.  `problem.md` records the nearest prior
interval as \(3\le H\le18\), so the value 11 is a genuine resolution relative
to that frozen boundary, not a subsidiary result.  The cited primary PDF is
not among the snapshot-listed evidence files and, under the referee's evidence
restriction, I did not independently re-audit its bibliographic or priority
claims.  This does not enter the self-contained finite proof above, and the
candidate expressly retains `status-uncertain` literature language and makes
no global-priority claim.

No mathematical gap remains in the frozen candidate scope.  The computation
is finite, exact, fully serialized, reproducible, and checked by a second
implementation whose formulation of the admission predicate differs from the
generator's.

## Verdict

**Accept.**  Scope, correctness/evidence, and the full-resolution contribution
all pass for the exact frozen claim `h_scr(A_4)=11`.
