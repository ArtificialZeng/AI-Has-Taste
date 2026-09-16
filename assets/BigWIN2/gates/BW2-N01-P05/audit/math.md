# Mathematical referee report

**Verdict: accept the exact frozen result-note scope.**

Job: `newwin-00001-p05-referee-fbe90a4ee304` (referee), 2026-09-12 UTC.
Snapshot: `61b1b81b6f23701268cd112fb1ae785237f7da8d66ef730026622b56be7ebd2d`.
Frozen kind: `result-note`. Frozen original status: `unresolved`.

The submitted theorem and its stated terminal-deletion application are valid.
The argument has an explicitly computer-assisted finite base, independently
recomputed in this review. No substantive correction or scope change was needed.

## Scope and integrity

The immutable original question asks for an all-k classification and count of
the length-2k+2 words requiring k passes. The candidate instead proves the
following precise subsidiary theorem, as expressly stated in `claim.json`:

For every r >= 3, let q use r letters, each with multiplicity two except for
at most one with multiplicity three. If deleting an arbitrary finite set A of
additional letters from W gives q, and every letter in A occupies one nonempty
contiguous block of W, then

    T(W) = r  if and only if  T(q) = r.

There is no bound on the number of inserted letters or on their positive block
multiplicities. The old word need not be run-free, insertion inside an old run
is allowed, and A may be empty. The theorem concerns equality to r, not equality
of all sorting times. Its run-free terminal-insertion corollary and application
to the original problem for k >= 4 are also included in this acceptance.

I read the frozen source, interpretation, claim, snapshot, listed proof,
programs, certificates, and source comparison. I did not consult checkpoint,
state, earlier referee reports, job transcripts, or unlisted research evidence.
The submitted programs were inspected but not executed or imported by the new
verifier. No agents or other model workers were used.

All 12 snapshot entries match their recorded SHA-256 values, and independently
serializing the sorted-key compact files mapping reproduces the snapshot
digest. `source.md` retains SHA-256
`dc2bdde5fef1bc7a1651940c02b76b65125ee7ad49eb26c921ac7664c0579a26`.
Details are in `audit/referee-integrity.json`. The supplied journal text was
also reproduced byte-for-byte by extracting the frozen PDF with
`pdftotext -layout`; the extraction is `audit/referee-primary.txt`.

## Reconstruction of the decisive argument

### The stack map, clumping, and deletion

The map uses forbidden subsequences, not consecutive patterns. Reversing the
stack orientation does not change whether it contains aba. All comparisons
are equality or inequality of letters; thus alphabet relabelling commutes
with the map. Sortedness means that every letter's positions form an interval,
without a prescribed order of the resulting blocks. Sorted words remain sorted
under a pass, which reverses their blocks.

For w = a s_1 a s_2 ... a s_m, with a absent from every s_i and empty segments
allowed, the first a stays below the intervening stack contents. Before another
a can be pushed, every intervening non-a entry must leave. Final draining has
the same effect on the last segment. Hence

    phi(w) = phi(s_1) phi(s_2) ... phi(s_m) a^m.

A clumped block can be pushed as a whole. When a later obstruction requires
popping it, legality cannot be restored partway through that block. Thus its
letter stays clumped. Stripping any leading clumped blocks and applying the
first-letter formula to the remaining suffix shows that the first unclumped
letter becomes clumped on every unsorted pass. If initially u letters are
unclumped, the sorting time is therefore at most u. In particular both T(q)
and T(W) are at most r, despite W's larger alphabet.

For a clumped letter c, deletion satisfies

    D_c(phi(w)) = phi(D_c(w)).

This follows by induction on word length from the displayed first-letter
formula. If c is the first letter, its entire block is an initial prefix and
both sides equal the image of the remaining suffix. Otherwise all c's lie in
one first-letter-free segment; apply the induction there. Empty segments cause
no exception. Persistence permits iteration of this identity and successive
deletions of any set of clumped letters. Consequently T(q) <= T(W).

These statements do not themselves imply the candidate theorem: deleting
clumped letters may lower a submaximal time, and the boundary examples below
also show failure of maximal-time invariance outside the claimed profiles.

### Why arbitrarily many marker blocks have a finite base

First compress each new clumped-letter block to one copy. Its copies are
processed together, so this compression changes neither the order of the old
letters nor which old runs are separated by new letters, through every pass.
Now consider any contiguous string of distinct new singletons in one original
gap. Its letters appear nowhere else. They are pushed uninterruptedly. Any
future input causing pops has a different letter from every member of that
string, so a pop episode cannot stop strictly inside it. The whole string is
therefore output contiguously, in reverse order. It retains these properties
on the next pass.

Collapsing such a string to one fresh singleton hence gives matching stack
transitions at the ends of the string and matching old-letter output, with
the same old-letter separations. All new letters in both systems stay clumped,
so sortedness of the complete outputs agrees at every iteration. This argument
applies to each originally occupied gap; if two strings subsequently meet,
neither can split. Thus at most one distinct singleton per occupied gap is a
complete reduction, not a numerical assumption about marker count. It also
covers adjacent marker blocks and insertion inside an old constant run.

### Complete three-letter base

There are 15 unlabelled words of profile (2,2,2) and 105 of profile (3,2,2):
respectively 6!/(2!^3 3!) and 7!/(3! 2!^2 2!). In every gap-subset case the
question is whether the second image is sorted. Since both times are bounded
by three, this is precisely the required equivalence at maximal time three.

The independent script `audit/referee-checks.py` uses only the Python standard
library. It enumerates all labelled ternary words of each relevant length,
filters by the exact profile, and then takes the canonical quotient. This is
a different generator from the submitted multiplicity-pruned RGS recursion.
Its stack is represented top first; for every proposed push it scans all
triples of positions for the literal forbidden subsequence. It tests sortedness
using position intervals, independently of the submitted run-count predicate.
The program uses explicit exceptions for failed checks, so Python optimization
cannot disable them.

Executed command: `python3 audit/referee-checks.py`.
The completed certificate is `audit/referee-checks.json`.

| Profile | Old representatives | Gap subsets per word | Marked inputs | Old words requiring 3 passes | Marked inputs requiring 3 passes | Failures |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| (2,2,2) | 15 | 128 | 1,920 | 1 | 128 | 0 |
| (3,2,2) | 105 | 256 | 26,880 | 12 | 3,072 | 0 |

The independently generated 120-word domain equals the complete submitted
certificate domain, with no duplicate certificate entries. Every per-word
outcome and mask total agrees. Both passes were recomputed on all 28,800 marked
inputs, and deleting the singleton markers reproduced the corresponding old
word at every recorded iterate. The finite transcript digest is recorded in
the new certificate. This is exhaustive exact computation, not sampling or a
floating-point fit.

The submitted literal, run-stack, and first-letter programs were also read.
Their stack conventions, greedy retry, final draining, multiplicity pruning,
and gap masks match their stated purposes. Correctness of the accepted finite
base does not require trusting their imports, numba installation, or recorded
success flag, because the separate standard-library computation covers its
whole domain.

### Induction for r >= 4

Assume the theorem for r-1 and suppose T(W)=r. The clump bound forces all r
old letters to be initially unclumped in W. If a is the first letter of q,
only inserted clumped blocks precede its first occurrence in W. Therefore a
is the first unclumped letter of W and becomes clumped in U=phi(W). It is
also clumped in v=phi(q) by the first-letter formula.

Set q_1=D_a(v). Deletion commutation gives D_(A union {a})(U)=q_1. Every deleted
letter is clumped in U. Importantly, q_1 has exactly r-1 old letters with their
original multiplicities; it still has all multiplicities two except possibly
one three. No run-free assumption is introduced. Thus this pair is within the
induction hypothesis, including when some letters of q_1 are already clumped.

Because T(U)=r-1, the induction hypothesis gives T(q_1)=r-1. Deleting the
clumped a from v cannot increase sorting time, so T(v)>=r-1. This also rules
out q being already sorted. Hence T(q)=1+T(v)>=r; the clump bound gives
T(q)<=r, and equality follows. Conversely T(q)=r together with
T(q)<=T(W)<=r forces T(W)=r. The induction reaches the verified r=3 base
and never invokes an invalid two-letter case.

### Application to the original deletion step

Let k>=4, |w|=2k+2, T(w)=k, and let its first letter x have multiplicity m.
Strict clump growth implies zero initial clumped letters and exactly one after
the first pass. Thus every letter occurs at least twice, m is 2, 3, or 4, and
phi(w)=v x^m with all other letters still unclumped. With r=k-1 and
q=trunc(v), each old letter of q has at least two runs, so |q|>=2r.

For m>=3, |v|<=2r+1. For m=2, one other letter has at least three occurrences;
one of the two x-free segments therefore has a repetition. The image of a word
with a repetition contains an adjacent equal pair: repeatedly remove a unique
first letter in the first-letter formula until a repeated first letter is
reached, whose terminal block supplies that pair. Thus truncation loses at least
one position from v, again giving |q|<=2r+1.

Truncation compatibility implies equality of sorting times between a word and
its truncation: their truncated iterates agree, and sortedness is equivalent
to having no repeated letter in the truncation. Consequently
T(qx)=T(v x^m)=k-1=r. The profile and r>=3 hypotheses now hold, so the accepted
theorem implies T(q)=r. This proves the claimed first-letter deletion bridge
for k>=4, without asserting the remaining inverse-fiber classification.

## Additional attacks and limitations of computation

The new verifier tested marker compression on 480 further exact inputs: every
one of the 120 base words with four gap patterns (initial, terminal, all gaps,
and alternating gaps), three distinct adjacent new blocks per occupied gap,
and block sizes from one through four. Input lengths reached 67. Compression
and full sortedness agreed at times 0, 1, 2, and 3 in every case. These are
finite corroboration of the compression proof, not its justification for
unbounded parameters.

It also independently reconstructed every entry of the three submitted
boundary orbits:

- q=0101: T(q)=1 and T(q2)=2, showing why r=2 is excluded.
- q=0102102: T(q)=1 and T(q3)=2, showing why equality of submaximal times is
  not part of the theorem.
- q=01201202: T(q)=2 and T(q3)=3, showing failure with two old triples.

The larger submitted held-out program and its 58,905-case coverage summary
were inspected but that complete run was not independently repeated. Neither
it nor the earlier M_k census is used as a proof dependency. The original
classification and enumeration remain unresolved in this candidate, exactly
as declared in the frozen workflow fields.

## Primary-source comparison and contribution

The closest primary source is Choi, Gan, Li, and Zhu, *Set Partitions that
Require a Maximum Number of Sorts Through the aba-avoiding Stack*, ECA 5:1
(2025), S2R1, DOI 10.54550/ECA2025V5S1R1. Its Theorems 1.1--1.2 classify/count
the first two length layers; Lemma 2.1 gives segmentation, Corollaries 2.1--2.2
give clump growth, and Proposition 3.1 gives truncation compatibility. Its
Lemma 3.5 already includes the first-letter-four subclass at length 2k+2.
Those results are properly attributed, rather than counted as the present
contribution. I checked the frozen text and its matching PDF extraction.
[Journal primary source](https://ecajournal.haifa.ac.il/Volume2025/ECA2025_S2A1.pdf).

I also reopened Janabel Xia's *Deterministic Stack-Sorting for Set Partitions*,
especially the map definition and Section 3's first-letter and clump arguments.
The arXiv v1 labels its alphabet-size bound Theorem 3.2; journal numbering is
different. The candidate's elementary dependencies match the actual statements
and were reconstructed above.
[Xia primary text](https://arxiv.org/html/2309.14644v1).

Ganesh, Xia, and Ying's *More Results on Stack-Sorting for Set Partitions*
studies image membership, fertility, and multiple-pattern avoidance. Its stated
results and relevant introductory/preliminary passages do not give this
arbitrary-clumped-insertion invariance principle.
[Ganesh--Xia--Ying primary text](https://arxiv.org/html/2408.05377v1).

The independent bounded web screen on 2026-09-12 used the exact paper title
and combinations including `"aba-avoiding" "clumped" insertion deletion`,
`site:arxiv.org "aba-avoiding" "maximum"`,
`site:ecajournal.haifa.ac.il "clumped" "deletion"`,
`"aba-avoiding" "clumped-letter"`, and
`"stack-sorting" "set partitions" "insertion" "maximum"`.
Focused text searches for insertion/deletion in Xia, and for clumped,
singleton, insertion/deletion in Ganesh--Xia--Ying, found no equivalent claim.
Some general search results were irrelevant and were not used as mathematical
sources. No equivalent theorem was located in the sources examined on this
date; this is a bounded literature assessment, not a proof of priority.

The precise delta is invariance of the maximal time under an arbitrary number
of already clumped inserted letters for a natural deletion-closed profile
family. The cited counts concern words whose total alphabet has size r and
do not supply this conclusion for the larger alphabet of W. The unrestricted
version fails by an exact boundary example, so deletion commutation plus the
alphabet bound alone is insufficient. The complete finite base and the
profile-preserving induction add a nontrivial statement. Its concrete use is
the proved terminal-letter reduction for the original next length layer.
These features meet the result-note contribution requirement; no arbitrary
toy restriction or duplicate of the stated neighboring counts is being accepted.

## Remaining work and final decision

No mathematical gap remains in the submitted theorem, finite reduction,
verified base, induction, or stated k>=4 application. Acceptance includes the
unbounded marker quantifiers and adjacent old-letter repetitions. It does not
resolve the original uniform inverse-fiber classification or determine M_k.
The computer-assisted base and the bounded scope of the literature search
must remain explicit in any manuscript.

**Final decision: accept**, with `kind=result-note` and
`original_status=unresolved` unchanged. The next workflow test is the runner's
mathematical integrity/provenance gate before drafting the accepted scope.
No manuscript or PDF was written in this job.
