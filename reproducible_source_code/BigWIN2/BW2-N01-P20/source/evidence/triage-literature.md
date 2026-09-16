# Bounded primary-literature screen

Job `newwin-00001-p20-triage-41e54da15a7f`; retrieval/check date 2026-09-12.

1. Erik Insko, Katie Johnson, Shaun Sullivan, *A Combinatorial Model for
   Lane Merging: Limited Capacity Lanes*, ECA 6:2 (2026), S2R9,
   DOI 10.54550/ECA2026V6S2R9.
   URL: https://ecajournal.haifa.ac.il/Volume2026/ECA2026_S2A9.pdf .
   Re-extracted and inspected printed pp. 11--12 directly from the supplied
   primary PDF `literature/insko-johnson-sullivan-limited.pdf` using
   `pdftotext -f 11 -l 12 -layout`. Its SHA256 is
   `6ad684580a2c11fac0227ed4182297b799d59f28956e4efade2cd3c1c093b466`,
   matching the handoff. Corollary 7.2 supplies the piecewise exact
   expectation, bounds away from the middle, and an exact central value.
   Section 8, question 2 asks for better near-center approximation.
   The published upper sum ends at 2m-1-k and subtracts C(2m-1,k);
   symmetry identifies this subtraction with the last term, proving
   agreement with the source's endpoint 2m-2-k. The all-A two-term
   floor-corrected formulation is the user's refinement of the question.
   Live web opens of this PDF and the journal mirror
   https://ecajournal.kms-ks.org/Volume2026/ECA2026_S2A9.pdf returned
   internal errors. The actual cached primary text remains inspectable;
   a later publisher revision was not verified by live PDF retrieval.

2. Aurora Hiveley and Doron Zeilberger, *The Combinatorics of Multi-Lane
   Merging*, arXiv:2607.26334v1 (28 July 2026).
   Live primary URLs https://arxiv.org/abs/2607.26334 and
   https://arxiv.org/html/2607.26334v1 opened successfully. The live
   submission history lists v1. Inspected Introduction, Theorem 1,
   Sections 6--7, and reference 2; the supplied local HTML has the same
   relevant statements. The theorem counts final lane configurations
   across arrival sequences with multiple lanes. Section 6 tabulates
   lane-length sums. The limited-capacity work is separately cited.
   This is not a fixed-red-count, capacity-constrained gap expansion,
   and the inspected text supplies no equivalent uniform two-term bound.

Queries actually issued in this job:

- `"A Combinatorial Model for Lane Merging" "Limited Capacity" asymptotic`
- `"lane merging" "central" "approximation" binomial`
- `"lane merging" "gap" "asymptotic" Insko Johnson Sullivan`
- `"lane merging" "central window"`

Results led back to the primary limited-capacity paper and to unrelated
traffic-control material. Search snippets were used only as leads. No
matching central-window expansion was found in the inspected primary
sources. This does not establish priority or exhaustive absence.
The earlier Bardenova et al. JIS 26 (2023), 23.5.3 remains an uninspected
background lead in this bounded job.

Both `literature/p20-intake-handoff.md` and
`literature/p20-triage-recovery-handoff.md` were enumerated and read.
There is no historical registry or artifact_payload file within the
project; the supervisor's broader deduplication report was not independently
reproduced and is not relabeled as a current-worker check. The local
comparison finds no equivalence with the later multi-lane result.

Source status: **open-supported parent question; precise refinement's
current status uncertain beyond this bounded screen**. No prior proof or
disproof of the frozen expansion was located. Suitability: **advance**,
because the full target is precise, the missing uniform estimates have a
concrete elementary verifier, and the result would address the cited
approximation gap. Classical methods and limited novelty remain explicit
contribution risks, not mathematical obstructions.

Tool note: an optional BeautifulSoup import was unavailable; direct live
HTML inspection completed the comparison without installing dependencies.
