# Research pass 2: terminal marker and doubled letters

Job `newwin-00001-p05-research-6c0e4e7ea54b`, 2026-09-12.
This is a bounded research dossier. The original all-k problem is unresolved.
No `literature/*handoff*.md` files were present when the pass began.

## First new exact test

The saved B2 assertion was frozen before this pass: for run-free q on r>=3
letters, each occurring at least twice and at least two occurring exactly
twice, appending a new terminal letter x cannot change T(q)=r-1 into T(qx)=r.

`b2-search.py` exhaustively tested r=5, length 15: 3,591,645 relabeling classes,
zero counterexamples. Full sorting-time histogram: `b2-r5-n15.json`.
Both the direct stack algorithm and an independently expressed first-letter
recursion agree at every computed iterate. This is finite evidence only.
The generator uses RGS, excludes adjacent equal letters, prunes when fewer
positions remain than needed to supply two copies of every letter, and prunes
when more than r-2 letters already have at least three copies. These exclusions
are necessary and sufficient for the stated final domain. An independent
domain count and literal forbidden-triple validation are still to be added.

A C++ compiler was unavailable. The completed test uses sequential numba
compilation of integer Python loops; no subprocess workers or random sampling
are used. The compiler issue has no mathematical implication.

## Exact counterexample: B2 is false

The extension through length 17 refutes B2. At r=5, length 16 there are
11,680,444 inputs and zero failures; at length 17 there are 34,891,823 inputs
and exactly 12 failures. Every failure is serialized in `b2-r5-n17.json`.
The lexicographically first is

    q = 01231230213421431,

with multiplicities (2,5,4,4,2) on the labels (0,1,2,3,4). This word is
run-free and has exactly two doubled letters. It sorts in four passes; q5
sorts in five passes. `b2-validation.json` supplies all six stages of both
orbits for each of the 12 witnesses, checks every original B2 hypothesis,
and recomputes every pass using a literal forbidden-triple stack in addition
to the other two maps. It also verifies the marker-gap recurrence along
each full orbit. In the first witness the marker's gaps are
17,11,12,11,3,0. At step four it separates the two copies of letter 4.

All of these counterexamples have length 17, while the original bridge B
at r=5 allows only lengths 10 and 11. They do not refute B or the original
classification problem. The proposed multiplicity-only proof route is
therefore unavailable. The B2 counterexample is research failure evidence,
not a proposed publishable counterexample to an established conjecture.

Additional held-out B2 domains at r=4, lengths 14,18,24 contain respectively
17,124; 68,100; and 292,644 words, with no failures. These isolated lengths
do not establish all lengths or all r=4 inputs. The r=5 result at 17, together
with the complete saved ranges 10,...,14 and new 15,16 tests, establishes
17 as the shortest five-letter B2 failure length only.

`b2-validation.py` checks each new domain size independently by summing the
inclusion-exclusion formula over all nondecreasing multiplicity profiles
with at least two 2s. The formula and its combinatorial proof are in the
pass-1 notes. Every count agrees. The computation uses exact integers;
elapsed-time fields are administrative floating-point values.

## Revised proof and candidate scope

The original bridge also passes the newly completed r=8 domains: 721,315
words at length 16 and 26,800,291 at length 17, with zero final-pass delays.
These finite counts are in `b2-r8-n16.json` and `b2-r8-n17.json`; despite the
reused filename prefix, these profiles satisfy the original narrower B.
The independent domain validation now covers all eight new search files.

The subsequent structural argument avoids B2. A class with all multiplicities
two and at most one three is preserved when any old letter is removed. The
candidate insertion theorem for r old letters therefore follows by induction
from its r=3 base: after one pass, promote the first old letter to the set of
clumped markers and delete it together with the original markers. This makes
the induction apply to exactly r-1 old letters. The complete proof and the
necessary finite representation of arbitrary clumped-marker insertions are
in `clumped-marker-theorem.md`.

`clumped-marker-base.py` verifies all 15+105 three-letter RGS representatives
and all subsets of their gaps: 28,800 marked inputs, with three maps agreeing
on both passes. The proof explicitly depends on this finite computation.
The induction, rather than an extrapolation of the larger searches, supplies
the all-r conclusion. An additional 58,905 held-out marked inputs, with
four or five old letters and marker blocks of varying positive multiplicity,
pass in `clumped-marker-heldout.json`.

The proposed result-note contains the clumped-insertion theorem and its
corollary proving the original terminal-letter bridge for every k>=4.
Uniform inverse-fiber counting remains unfinished, so original_status is
unresolved. Fresh review must audit the block-collapse reduction, the
induction hypotheses, the exhaustive finite base, and the contribution's
novelty and substance. No independent acceptance is claimed in this pass.
