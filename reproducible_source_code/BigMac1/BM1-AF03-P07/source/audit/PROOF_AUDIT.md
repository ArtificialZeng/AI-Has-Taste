# Independent proof audit

Audit date: 2026-08-29  
Endpoint audited: every ordered alphabet of cardinality at most eight  
Verdict: **PASS for `CERTIFIED_FINITE_RESULT`; not a general proof**

## 1. Quantifiers and boundary cases

The audited theorem quantifies over every (0\le n\le8), every K-Knuth class
of initial straight increasing tableaux on ([n]), every comparable pair of
shapes in that class, and every partition between the pair. Incomparable pairs
impose no condition. Equal endpoints give singleton intervals. At (n=0), the
unique empty tableau and empty shape are included. Order-preserving
standardization covers tableaux on any ordered alphabet with at most eight
distinct letters. These are exactly the quantifiers in
`problem/formal_statement.md` and Theorem 4.1 of the manuscript.

## 2. Reconstruction of the finite proof

The audit followed the dependency chain below directly from source rather than
from discovery summaries.

1. **Finiteness.** Strict increase implies (T(i,j)\ge i+j-1), so the shape is
   contained in (delta_n=(n,n-1,\ldots,1)).
2. **Shape universe.** `ShapeFirstEnumeration::choose_shape` in
   `src/verifier.cpp` lines 195--211 chooses every weakly decreasing row-length
   sequence bounded by (n-r), including the empty shape, exactly once.
3. **Fillings.** Lines 213--228 fill a fixed shape in row-major order. The lower
   bound is the maximum of the diagonal bound and one more than the left and
   upper entries. It is necessary and sufficient at the current cell; trying
   every value through (n) is exhaustive. The sorted code list is checked for
   duplicates at lines 185--193.
4. **Canonical representation.** Lines 41--109 use a diagonal-dependent 80-bit
   cell code. Decode rejects non-left-justified rows, nonstraight shapes, and
   nonpartitions; `valid` at lines 111--133 rechecks the alphabet, staircase,
   row, and column conditions. Hash collisions cannot merge tableaux: the
   dictionary compares full `Code` values, not hashes.
5. **Right action.** Lines 135--161 implement exact Hecke row insertion on an
   integer grid and revalidate its result. Lines 269--291 regenerate every
   transition (T\mapsto T\leftarrow a); a target absent from the enumerated
   dictionary is a hard error. The two published insertion examples are
   checked before every endpoint at lines 510--533.
6. **Primitive relations.** Lines 318--355 generate (n) idempotence pairs,
   \(\binom n2\) braid pairs, and (2\binom n3) Knuth pairs. Restricting the
   braid pair to (p<q) loses nothing because the relation is symmetric; the
   (p=q) instance is tautological. At (n=8) this gives exactly 148 rules.
7. **Congruence closure.** Lines 357--392 merge every primitive image at every
   state and queue every successful union. Each queued equality is then closed
   under right insertion by every letter; new unions extend the same queue.
   Processing only successful unions is sufficient because an already
   connected pair has a path of previously queued equalities, whose right
   images are connected by transitivity. The published Algorithm 1 and
   Theorem 3.1 identify the components with tableau K-Knuth classes.
8. **Initial components.** Lines 169--176 compute the exact letter bitset.
   Every primitive relation preserves distinct letters, so initial tableaux
   form whole components. Lines 435--451 count these components and shapes.
9. **Interval predicate.** Lines 453--507 construct the full finite shape
   universe and exact closure bitsets. For a component shape set (S), a
   missing middle shape is precisely a bit of
   \((\uparrow S)\cap(\downarrow S)\setminus S\). A nonzero bit produces and
   validates lower/middle/upper witnesses before returning failure.
10. **Endpoint totals.** The strict driver regenerates (n=0,\ldots,8) and
    compares every tableau, initial-tableau, class, URT, and interval result.
    At (n=8) it also compares all rule and closure loop counters. Any mismatch
    or nonzero verifier exit is rejection.

## 3. Exact reproduced values

The clean reconstruction returned 9,069,306 tableaux, 6,773,991 initial
tableaux, 988,384 initial classes, and 215,295 URTs at (n=8). It found all
988,384 shape sets order-convex. The audit counters were 1,342,257,288
primitive tests, 58,425,112 right-closure tests, and 7,303,139 successful
merges. All published initial-tableau, class, and URT counts for (n\le7) were
reproduced exactly.

The successful run is `results/verification_n0_n8.log`. Its core source hash is
`34adc8c26207209d039dc7a6452743b2e2711d2b5b742bb706a4b108059ca8b7`,
and the certificate hash is
`8e4bb76e15062fa0d60174d061f4a6f21ab8e934f56938d2e878faddd06f0d61`.

## 4. Independence and adversarial checks

`src/verifier.cpp` has no filesystem-reading API and cannot import discovery
states. Relative to `src/discovery.cpp`, it changes state enumeration,
representation, insertion data structure, generic rule construction, and the
interval test. The only shared mathematical ingredient is the published
classification algorithm whose output both paths must represent.

`tests/test_fail_closed.py` confirmed rejection of a missing key, extra trusted
field, Boolean/integer confusion, duplicate JSON key, and altered count; an
intact control was accepted. Compiler diagnostics under
`-Wall -Wextra -Wpedantic` were empty. The floating-point `seconds` field is
diagnostic only and is never used in the theorem or certificate comparison.

## 5. Residual limitation

The audit does not close the general prescribed-cover lemma. K-jdt and K-Knuth
paths do not presently control a chosen one-box shape change. This is gap G01
and is outside the finite theorem. No Lean, Coq, Isabelle, or other proof
assistant was used.
