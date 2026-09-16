# Candidate partial theorem: clumped-letter insertion at maximal sorting time

Proposer: `newwin-00001-p05-research-6c0e4e7ea54b`, 2026-09-12.
This is a proof dossier for independent review, not an accepted manuscript.
The original length-2k+2 classification and enumeration remain unresolved.

## Exact statement

Let phi be the aba-avoiding greedy stack map in `problem.md`, and let T(w)
be its sorting time, including T(w)=0 for an already sorted word. Let r>=3,
and let q use exactly r letters, each occurring twice, except that at most
one letter is allowed to occur three times. Adjacent equal letters in q are
allowed. Let W be any word obtained by inserting finitely many new letters
into q, subject only to the condition that **each new letter has all of its
occurrences in a single contiguous block in W**. Different new letters may
occupy adjacent blocks, and a new block may be inserted in any gap of q.

**Theorem (computer-assisted finite base).**

    T(W)=r  if and only if  T(q)=r.

This asserts invariance of maximal sorting time, not equality of all sorting
times. For example q=0102102 has T(q)=1, while q3 has T(q3)=2. These are
below the maximum r=3 and do not contradict the theorem.

**Corollary B.** If q is run-free on r>=3 letters, every letter occurs at
least twice, and 2r<=|q|<=2r+1, then for a new terminal letter x,

    T(qx)=r  if and only if  T(q)=r.

The theorem allows more than a terminal marker and does not require q to
be run-free. The profile condition of the corollary implies precisely the
profile condition of the theorem.

## Elementary dependencies, with proofs

1. **First-letter formula.** If w=a s_1 a s_2 ... a s_m, with no a in any
   s_i and possibly empty s_i, then

       phi(w)=phi(s_1) phi(s_2) ... phi(s_m) a^m.

   The initial a remains at the stack bottom. Before any subsequent a can
   be pushed, all intervening non-a stack entries must be popped. Thus each
   s_i is processed independently, and all a's leave together at the end.
   This is Xia's lemma, also cited as Lemma 2.1 by Choi--Gan--Li--Zhu.

2. **Persistence and sorting bound.** A clumped letter remains clumped:
   once its input block can be pushed, every remaining copy can be pushed
   without a new obstruction. When such a stack block must be popped, all
   copies leave together before the obstruction is cleared. The first
   unclumped letter becomes clumped in each unsorted pass. Indeed, strip
   the leading clumped blocks and use the first-letter formula on the
   remaining suffix; the stripped blocks move to the end without splitting
   the newly formed block. Consequently if there are at most r unclumped
   letters initially, sorting takes at most r passes. In particular
   T(q)<=r and T(W)<=r.

3. **Deletion commutes for clumped letters.** If c is clumped, then

       D_c(phi(w))=phi(D_c(w)),

   where D_c deletes every c. Induct on |w| using the first-letter formula.
   If the first letter is c, write w=c^m u and both sides equal phi(u).
   Otherwise all c's lie in exactly one first-letter-free segment; apply
   induction in that segment and concatenate the other segment outputs.
   Persistence permits iteration. Deleting any collection of clumped
   letters therefore commutes through all passes and cannot increase
   sorting time. In particular T(q)<=T(W).

4. **Finite representation of arbitrary marker blocks.** For a fixed old
   word q of length n, it suffices to consider one distinct singleton marker
   in each gap belonging to an arbitrary subset of its n+1 gaps. To see
   this directly, first replace each new clumped letter block by one copy.
   The stack processes that entire block as a unit, so the replacement
   preserves the positions of all old letters through every pass. Next
   collapse every maximal contiguous string of distinct new singleton
   markers to a single fresh singleton marker. Such a string is pushed
   uninterruptedly, since none of its letters occurs anywhere else. Any
   later pop episode either stops above the entire string or pops it all:
   no future input matches a letter strictly inside it. The string leaves
   as a contiguous reversed string and has the same property at every
   subsequent pass. Thus collapsing it also preserves old-letter order
   and whether any old-letter block is separated by markers. All markers
   stay clumped in both systems, so full sortedness is preserved. Finally,
   marker names are irrelevant up to relabeling. This proves the asserted
   finite reduction; it is not an assumption about bounded marker count.

## Complete finite base r=3

There are 15 RGS representatives with profile (2,2,2), and 105 with profile
(3,2,2). These follow respectively from

    6!/(2!^3 3!) = 15,
    7!/(3! 2!^2 2!) = 105.

The RGS generator in `research-pass1.py` enumerates all words with each
multiplicity at least two and at most four. At lengths 6 and 7 with exactly
three letters these are exactly the two profiles above. Its pruning only
discards prefixes whose remaining positions cannot complete the required
multiplicities, or whose next choice would exceed the multiplicity bound.
Every valid RGS appears once. The independent multinomial counts check its
domain totals.

For every q, `clumped-marker-base.py` inserts one distinct marker in each
subset of its n+1 gaps. In every case it establishes that phi^2(W) is sorted
if and only if phi^2(q) is sorted:

| old profile | q representatives | masks per q | marked inputs | failures |
|---|---:|---:|---:|---:|
| (2,2,2) | 15 | 128 | 1,920 | 0 |
| (3,2,2) | 105 | 256 | 26,880 | 0 |

Both iterations of every input are independently computed by (i) a literal
test of every forbidden triple of the proposed stack, (ii) the run-stack
implementation, and (iii) the first-letter recursion. All outputs agree.
The literal algorithm is compiled by numba using integer loops; it performs
no random sampling or floating-point mathematical decisions. The other two
implementations execute as ordinary Python. `clumped-marker-base.json`
records each of the 120 q's, the complete number of masks, and its outcome.

Since both times are at most three, the computed equivalence is exactly
T(W)=3 iff T(q)=3. Lemma 4 extends this finite result to arbitrarily many
inserted letters and arbitrary positive block multiplicities. This finite
base is an explicit computer-assisted part of the proof; it is not an
infinite inference from the later numerical B2 searches.

## Induction for every r>=4

Assume the theorem holds for r-1 and suppose T(W)=r. Let A be the set of
inserted letters and let a be the first letter of q. Every old letter is
initially unclumped in W: otherwise the sorting bound would give T(W)<=r-1.
The letters preceding the first a in W are inserted clumped letters, so a
is the first unclumped letter of W. By Lemma 2, a is clumped in phi(W).
It is also clumped in phi(q) by the first-letter formula. All letters in A
remain clumped in phi(W).

Set U=phi(W), v=phi(q), and q_1=D_a(v). By commutation,

    D_{A union {a}}(U)=q_1.

The word q_1 uses exactly r-1 letters with the same multiplicities they had
in q. It still has each letter twice and at most one letter three times.
In U every deleted letter belongs to a single clumped block. Thus (q_1,U)
satisfies the induction hypothesis. Since T(U)=r-1, it gives

    T(q_1)=r-1.

Deleting the clumped a from v cannot increase sorting time, so T(v)>=r-1.
The general bound T(q)<=r gives the reverse inequality T(v)<=r-1 whenever
q is unsorted; q cannot be sorted here because q_1 requires at least three
passes. Hence T(q)=1+T(v)=r. This proves the forward implication. The reverse
implication follows from T(q)<=T(W)<=r. Induction is complete.

## Scope, boundary tests, and contribution

The lower bound r>=3 is necessary: q=0101 has T(q)=1, whereas q2 has T(q2)=2.
No equality of submaximal times is claimed. More general profiles can fail:
q=01201202 has profile (3,2,3), T(q)=2, T(q3)=3. Its exact orbit is in
`clumped-marker-heldout.json`. These demonstrate why the claimed profile
condition matters. The held-out file additionally checks 58,905 marked
inputs on four and five old letters, including multiple adjacent marker
blocks with varying positive multiplicities. These tests are corroboration,
not the base or induction proof.

For completeness, here is the application to the original deletion bridge.
Let k>=4, T(w)=k, |w|=2k+2, and let x be the first letter, of multiplicity m.
Every letter initially occurs at least twice and exactly one letter is
clumped after the first pass, by the strict clump-growth bound. Thus
m is 2, 3, or 4. Write phi(w)=v x^m and set q=trunc(v), r=k-1. Each letter
of v is unclumped, so each occurs at least twice in q and |q|>=2r. If m>=3,
then |q|<=|v|<=2r+1. If m=2, one of the two x-free segments contains a
repetition because some other letter occurs at least three times. The image
of any word containing a repetition has an adjacent equal pair: remove its
unique first letter recursively until the first letter repeats and supplies
the terminal repeated block. Therefore truncation loses at least one position
from v and again |q|<=2r+1. Truncation compatibility (Choi--Gan--Li--Zhu,
Proposition 3.1) gives T(v x^m)=T(qx)=r. Corollary B gives T(q)=r, as required.
The k=3/two-letter boundary is excluded from this application.
Uniform inverse-fiber counting for the original excess-two layer is not
completed here. Accordingly this is proposed only as a **result-note**.

The neighboring minimal-length and next-length counts, including the known
first-letter-four subclass, are due to Choi--Gan--Li--Zhu. The proposed delta
is invariance under arbitrary clumped-letter insertion at maximal time and
its application to the previously unproved deletion step. No equivalent
statement was located in the bounded primary-source comparison recorded in
`literature/research-pass2-20260912.md`; this is not a priority guarantee.

Known mathematical gaps in the stated computer-assisted argument: none
identified by the proposer. Fresh mathematical review is still required,
especially of the marker-block reduction, induction scope, finite-base
completeness, and whether this extension is a sufficiently substantive new
contribution. No independent review or acceptance is claimed in this job.
