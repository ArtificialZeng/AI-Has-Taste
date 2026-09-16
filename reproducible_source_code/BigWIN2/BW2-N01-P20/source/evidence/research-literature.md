# Primary-source comparison for the submitted central-window theorem

Research job `newwin-00001-p20-research-f42a5d965fef`; checked 2026-09-12.
The two files matching `literature/*handoff*.md` were enumerated and read.
Their proposed coefficients and recovery route were treated as leads;
`research-proof.md` supplies the missing inequalities independently of
their asserted confidence. No historical-registry search is claimed here.

## Closest primary result

Insko, Johnson and Sullivan, *A Combinatorial Model for Lane Merging:
Limited Capacity Lanes*, ECA 6:2 (2026), S2R9,
[publisher PDF](https://ecajournal.haifa.ac.il/Volume2026/ECA2026_S2A9.pdf),
DOI 10.54550/ECA2026V6S2R9. Printed pp. 11--12 were freshly extracted
from the actual local PDF with `pdftotext -f 11 -l 12 -layout` and read.
Corollary 7.2 gives the exact expectation, off-center bounds and the
central value. Its upper sum is identical to the frozen definition:
the subtracted binomial coefficient removes the last summand by symmetry.
Section 8, question 2 asks for a better approximation near k=m.
The all-A two-term expansion with the floor correction is the user's
precise refinement, rather than the verbatim published question.

The source PDF was copied byte for byte to
`evidence/external/insko-johnson-sullivan-limited.pdf`, SHA256
`6ad684580a2c11fac0227ed4182297b799d59f28956e4efade2cd3c1c093b466`.
It has the same hash as the supplied original primary PDF. Live search
returned the publisher article, but direct live PDF opening failed.
A later publisher revision was therefore not verified.

## Nearby primary comparisons

Hiveley and Zeilberger, *The Combinatorics of Multi-Lane Merging*,
[arXiv abstract](https://arxiv.org/abs/2607.26334) and
[v1 primary HTML](https://arxiv.org/html/2607.26334v1), accessed live.
Introduction, Theorem 1, sections 6--7 and the references were inspected.
Theorem 1 counts final lane configurations for multiple lanes; section 6
tabulates lane lengths. The bounded-capacity paper is separately cited.
These statements use different conditioning and do not give the submitted
central-window remainder. The supplied primary HTML was copied to
`evidence/external/hiveley-zeilberger-2607.26334v1.html`, SHA256
`6e1672202488de1feef59147cd18608899aedf0c796eb733d00840631e10e3d8`.
The relevant statements were compared with the live HTML.

Bardenova, Insko, Johnson and Sullivan, *A Combinatorial Model for Lane
Merging*, JIS 26 (2023), 23.5.3:
[journal page](https://cs.uwaterloo.ca/journals/JIS/VOL26/Insko/insko5.html),
[primary PDF](https://cs.uwaterloo.ca/journals/JIS/VOL26/Insko/insko5.pdf).
The live PDF was newly inspected at the introduction, Lemma 25 and
Corollary 26 (printed pp. 19--20), and Open Problem 39 (printed p. 28).
The corollary gives the limiting right-lane proportion at a fixed driver
ratio for the unrestricted model. The capacity-constrained missing-car
expectation is posed separately as Open Problem 39. These inspected
statements do not provide the present two-term expansion. A shell PDF
download failed; no local copy of this earlier PDF is asserted.

## Search scope and contribution decision

Live queries issued in this research pass:

- `"A Combinatorial Model for Lane Merging" "Limited Capacity" asymptotic`
- `"lane merging" "central" "binomial" approximation`
- `"lane merging" "uniform" "asymptotic"`
- `site.cs.uwaterloo.ca/journals/JIS "A Combinatorial Model for Lane Merging"`
- `"lane merging" "erfc"`
- `"10.54550/ECA2026V6S2R9" approximation`

Search results were leads, with mathematical comparisons based on the
primary texts above. No equivalent two-term formula and all-real-x
uniform error were located in these inspected sources on this date.
This is a bounded literature screen, not a priority proof or an exhaustive
current open-status determination. Uninspected citing work, alternate
terminology, and unpublished solutions remain possible.

The proposed contribution is a full solution of the user's frozen
central-window problem: explicit leading and lattice terms and a uniform
absolute error with elementary explicit constants. It addresses a
specific approximation requested by the closest primary paper. Wallis
bounds, local binomial approximations and trapezoidal summation are
classical; no new general asymptotic method is claimed. This specific
application is submitted as a short full-resolution candidate. A fresh
referee must assess both correctness and sufficient contribution before
any manuscript is prepared.
