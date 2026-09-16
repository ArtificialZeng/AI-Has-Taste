# Exact triage certificate: failure of the interlacing clause

Job: primary-20260913-multiset-rook-triage-cd5e7d22bd0b. Date: 2026-09-13.
This is a locally checked mathematical argument for the next research/review
phase, not an independent referee acceptance or a novelty certification.

Take the non-skew Ferrers board
\(\lambda=(3,3,3,3,4,4)\) and content \(\alpha=(2,2,1,1)\).
There are six rows, with positive nondecreasing lengths, and six letters.
The alphabet is exactly {1,2,3,4}, every content coordinate is positive,
and every refinement considered below is nonzero. This is neither a rectangle
nor a distinct-letter case. No sentinel is used.

## Exhaustive counting certificate

The unique 4 must occupy position 5 or 6. Deleting it gives a permutation
of 11223, and every such permutation has exactly those two legal insertions.
Thus there are \(2\cdot5!/(2!2!)=60\) legal words. Conditional on first
letter 1, 2, or 3 there are respectively 24, 24, or 12 words.
The complete list, with first letters and ascent counts, is
`six-letter-words.tsv`. Its SHA256 is
`740703e89a0388b3f1aa1f75fa37e7fed3e22fee5cff16748a69aa8a7fc51f86`.

For direct checking, the polynomials split by the position of 4 are:

| First letter | 4 in position 5 | 4 in position 6 |
|---|---|---|
| 1 | \(5t^2+7t^3\) | \(2t^2+8t^3+2t^4\) |
| 2 | \(t+9t^2+2t^3\) | \(6t^2+6t^3\) |
| 3 | \(2t+4t^2\) | \(t+4t^2+t^3\) |

These counts were obtained twice: Cartesian-product enumeration in
`triage-interlacing.py`, then a separate remaining-content recursion in
`verify-six-letter.py`, which imports neither the search nor its root test.
The insertion argument above proves that the listed search space is complete.

Consequently
\[
R_3=t(t^2+8t+3),\qquad
R_2=t(8t^2+15t+1),\qquad
R_1=t^2(t+7)(2t+1).
\]

## Exact root-order failure

Definition 8 of the frozen primary source writes
\(\cdots\le a_2\le b_2\le a_1\le b_1\le0\)
for \(f\preceq g\). When \(\deg g=\deg f+1\), this requires
the smallest root of g to be no greater than the smallest root of f.
Definition 9 requires this relation for **every** earlier/later pair.
Conjecture 28's displayed sequence here is \((R_3,R_2,R_1)\).

The roots of \(R_3\) are \(-4-\sqrt{13},-4+\sqrt{13},0\).
The roots of \(R_1\) are \(-7,-1/2,0,0\).
Both are real-rooted with positive leading coefficient, and their degrees
are 3 and 4. Since \(13>9\),
\[
\min\operatorname{root}(R_3)=-4-\sqrt{13}<-7
=\min\operatorname{root}(R_1).
\]
Therefore \(R_3\not\preceq R_1\), contradicting the interlacing clause
under the printed definitions. This uses exact inequalities, not numerical
root approximations or the search program's Boolean output.

The total is \(R=2t^4+24t^3+30t^2+4t\). Exact rational root isolation
finds all four roots real, counting multiplicity. The witness does not
disprove the separately stated universal real-rootedness clause. Since the
original source assertion is a conjunction, failure of its interlacing
clause is a route to a disproof of that conjunction, subject to research
scope confirmation and the required independent referee.

## Search bounds and limits

The screening run tested all 329 nondecreasing boards over {1,2,3,4} of
lengths 1 through 7, all 9371 realized length-four contents, and all 4452
ordered nonzero refinement pairs. Nine pairs failed, with the first two at
length six. This is minimal length **within that finite alphabet bound**;
no global minimality or total-polynomial search result is asserted.

The auxiliary content-coupled compatibility witness in the search JSON is
separate: entries 1 and t+t^2 have non-real-rooted sum 1+t+t^2. Its effective
board is rectangular after an unused column is removed, so it is merely a
diagnostic against an unnecessarily strong induction invariant. The direct
six-letter counterexample supersedes that route as the next research target.
