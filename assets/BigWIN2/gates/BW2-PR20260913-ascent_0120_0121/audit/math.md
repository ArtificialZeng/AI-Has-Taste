# Mathematical referee report

Verdict: **accept** the exact frozen candidate.

Job: `primary-20260913-ascent-0120-0121-referee-42ef846d2b26`.
Snapshot: `958c9a78449aa3cc908c65a2d985d4d117bbf5501f48ff8886bd6a1970d24761`.
Review date: 2026-09-13.
Frozen kind: `resolution-paper`. Frozen original status: `proved`.

The accepted result is the all-length structural enumeration of the full
0120/0121-avoiding ascent-sequence class, with precisely the matrices,
initial rows, formal generating series, coefficient formula, and arithmetic
bound submitted in `claim.json`. The original statement explicitly permits
a uniform structural enumeration beyond exhaustive word generation. The
candidate meets that alternative. This decision does not replace the claim
with a restricted class or a partial-result scope.

## Inputs and integrity

I read `source.md`, `problem.md`, `claim.json`, `audit/snapshot.json`, the
complete proof, checker, results, literature comparison, and registry screen
listed in the snapshot. In the listed primary HTML I inspected Section 1
including Table 1, Section 2, and Section 6; I also inspected the relevant
primary-source passages live. Unrelated proofs in that source were not
dependencies requiring audit. No checkpoint, scheduling state, earlier
review, or job transcript was used. Proposer assertions of confidence were
not evidence for the decision.

All nine frozen file hashes match, and the canonical hash of the snapshot's
file mapping equals its digest. These checks passed before and after the
independent computations. The immutable `source.md` has SHA-256
`c3511d885d5d487049ba8d52247444c1e27c6005f320a593c5aa5ffbb7bfd48b`.
No frozen input was edited. This is a fresh referee task with an independently
written verifier, not a claim of statistical independence or external peer
review.

## Reconstruction of the proof

Write a=asc(w), S for the letters seen in a nonempty prefix, and B for the
union of the two lower values of every increasing triple in w. For an
avoiding prefix, appending v creates a forbidden occurrence exactly when
v belongs to B. The ascent condition independently requires 0<=v<=a+1.
Thus the eligible numerical alphabet is exactly E={0,...,a+1} minus B.
Both equality-preserving patterns are covered, with arbitrary increasing
indices; no adjacency condition is introduced.

The bound max(w)<=asc(w) follows by induction for every ascent sequence.
If an appended letter exceeds the old ascent count a, it must equal a+1;
the inductive maximum bound forces that append to be an ascent. The first
nonzero letter is 1. Consequently, after the first letter at least 2,

    B={0} union {u>0: an occurrence of u has a larger letter later}.

For the forward inclusion, every positive lower endpoint of an increasing
triple has a larger later letter. For the reverse inclusion, the initial
zero precedes each positive occurrence, giving the required triple; a
triple 0,1,v also guarantees the membership of zero. Binary prefixes have
no increasing triple and hence have empty B.

For an avoiding postbinary prefix, its final letter l cannot lie in B.
Any triple banning l must end before the final position, since its third
letter is larger than l, so a final l would complete a forbidden pattern.
Every smaller seen letter is banned, using the final l as the larger later
letter (and the established ban of zero). Therefore l is the least seen
eligible letter. The top eligible value a+1 is unseen, by the maximum
bound. Ranking E gives exactly a state (k,H) with k>=2 and a nonempty
H contained in {0,...,k-2}; the final rank is min(H).

Appending the eligible value of rank t bans exactly the previously seen
values below that value, in addition to the old B. If t<=min(H), there is
no ascent and no newly banned eligible letter. The child is (k,H union
{t}). If t>min(H), the append is an ascent. Precisely
r=|{h in H:h<t}| old eligible values disappear, and the new upper bound
a+2 contributes one unseen largest eligible value. Every surviving old
seen rank shifts down by r, and the appended rank becomes t-r. This is
exactly the second transition in the claim, with child width k+1-r.
Here r>=1, so the width does not increase.

These rules are closed on the entire declared domain, including labels
viewed abstractly: r<=t<=k-1 ensures the new width is at least 2, and all
seen ranks remain below the new top rank. Every rank denotes one numerical
choice. Summing over ranks therefore retains multiplicities even when
several choices have the same child label. Induction on suffix length d,
starting with one empty suffix, proves c_s(d)=(T_K^d 1)_s. This is the
decisive quotient argument; it does not assume that numerical gaps can be
discarded without checking their effect on future ascent bounds.

The initialization is also exact. A binary prefix with a>=1 ascents can
exit to each v in {2,...,a+1}. The exit makes an ascent, bans exactly 0
and 1, and leaves E={2,...,a+2} with only v seen. Thus K=a+1 and the
initial label is (K,{v-2}); summing its K-1 distinct choices gives b_K.
No binary prefix with a=0 can exit.

Let q=z/(1-z). A binary prefix starting in zero with a>=1 ascents has
2a nonempty alternating runs if it ends in one, and 2a+1 if it ends in
zero. Its weight is q^(2a)+q^(2a+1)=z^(2a)/(1-z)^(2a+1).
Multiplying by z for the exit gives q^(2K-1). Every nonbinary word has
a unique maximal binary prefix, exit value, and suffix, so the assembly
is disjoint and exhaustive. Completely binary words contribute 2^(n-1)
for n>=1; their series together with the empty word is (1-z)/(1-2z).
This proves the claimed expression

    F(z)=(1-z)/(1-2z)
         +sum_{K>=2} (z/(1-z))^(2K-1) b_K(I-zT_K)^(-1)1.

All operations here take place in Z[[z]]. Each summand starts in degree
2K-1, and the inverse has the formal expansion sum_d z^d T_K^d. Hence
each coefficient uses finitely many summands and no analytic convergence
or exchange of divergent sums is involved. Extracting the coefficient
of q^(2K-1) yields binom(n-d-1,2K-2) in exactly the stated range, proving
the finite coefficient formula. The empty word is handled separately and
the sums are empty at lengths 1 and 2, as required.

## State bound, computation cost, and original scope

The domain size is sum_{k=2}^K (2^(k-1)-1)=2^K-K-1. The minimum length
of a prefix with exit width K is 2K-1, attained by (01)^(K-1) followed
by an allowed exit. Thus L=floor((N+1)/2) suffices through degree N.
Every label (K,H) is realizable by that binary prefix, an exit of value
max(H)+2, and the remaining values h+2 in decreasing order.

There are at most L outgoing choices per postbinary label. Propagating
counts over N levels uses O(N L 2^L) additions. At each level there are
O(N) binary states (a,last), with O(N) exits each, giving the stated
O(N^3) bound for their contribution. Constructing the explicit edges by
scanning length-at-most-L rank sets takes O(L^2 2^L) elementary work,
which is absorbed by O(N L 2^L). Counting arrays require O(2^L+N)
live values, separately from the stored edges. This is an arithmetic
bound; integer sizes and bit-operation costs are not assumed constant.

This is an informative resolution of the frozen structural-enumeration
target. A finite system for a fixed exit width handles suffixes of every
length and gives rational continuation functions. The full coefficient
algorithm uses O(N L 2^L+N^3) additions while the class already contains
2^(N-1) binary words of length N. The proved quotient therefore supplies
substantial compression and a uniform structural description. It is not
an arbitrary restriction to bounded word length or an extra forbidden
pattern. No scalar rationality, algebraicity, analytic radius, minimality
of the quotient, or simpler closed form is needed or accepted.

The K=2 block has two self transitions. For K=3, the three top-width
equations in the proof follow directly from the rule. With
D=1-5z+8z^2-5z^3, solving them gives

    c_0=(1-4z+6z^2-3z^3)/((1-2z)D),
    c_1=(1-2z+2z^2)/D.

Their sum is the rational function displayed in the dossier. The claimed
formula has no small-width normalization or multiplicity error.

## Independent exact checks actually performed

The new standard-library script `audit/referee_checks.py` does not import
or run the proposer's checker. Its output is
`audit/referee-check-results.json`.

- It enumerates all ascent sequences through length 9 without avoidance
  pruning and tests the literal forbidden condition over all quadruples.
  All 31,240 ascent sequences at length 9 are included; 1,980 survive.
- It performs a separate unmerged literal-word census through length 13,
  determining forbidden append values directly from increasing triples
  of indices. The resulting counts are
  1,1,2,5,13,34,90,244,683,1980,5945,18470,59306,196547.
- For all 8,997 avoiding prefixes of lengths 1 through 10, it checks
  eligible-set invariants and full child-label multisets: 27,466 legal
  edges, including 4,890 non-RGF prefixes in the prefix census.
- It checks closure and literal realizability of all 247 labels through
  width 8, covering 1,757 outgoing choices.
- It checks the binary ascent distribution through length 14, including
  impossible ascent counts, for 105 positive-ascent parameter cases.
- A separately implemented tuple/set continuation recurrence and the
  binomial coefficient formula reproduce all frozen coefficients through
  degree 28. The K=3 rational display also passes 25 exact coefficient
  residual checks, in addition to the algebraic verification above.
- It checks that 010132 satisfies the ascent bounds, avoids both target
  patterns, and contains 021 and 0132 at the indicated index selections.

The proposer's exact-state and stress-test code and serialized results
were inspected. I did not rerun that program, which writes a frozen
result file. Its higher reference-state coverage is not represented as
an independent literal census by this referee. The new finite checks
support the all-length induction; the induction is the proof.

## Primary-source comparison and contribution judgment

The nearest checked benchmark is Liu, Kitaev, and Zhang,
[Simultaneous avoidance of length-4 patterns in ascent sequences,
arXiv:2604.06735v1](https://arxiv.org/html/2604.06735v1).
Section 1 has the same ascent and subsequence definitions; Table 1 has
the same exact pair and initial counts; Section 6 leaves that pair's
enumeration unresolved. Section 2's reductions involving 0121 require
the RGF hypothesis and do not apply to the full present class. The
specific advance is the finite eligible-rank quotient with nonincreasing
width and the all-length matrix enumeration. These are not supplied by
the cited benchmark or by invoking its RGF reductions.

I independently opened the primary PDF of Mansour and Shattuck,
[On ascent sequences avoiding 021 and a pattern of length four,
arXiv:2507.17947v1](https://arxiv.org/pdf/2507.17947), and inspected the
abstract, definitions, Table 1, and the subsequent RGF comparison on
pages 1--3. Its B_n is A_n(021). Its Table 1 entry for 0120 has coefficient
89 at length 6, while the candidate's exact class has 90. The literal
witness 010132 confirms that imposing 021 or 0132 would lose inputs.
This establishes the scope difference from that checked result. It does
not establish that no auxiliary theorem or unknown bijection exists.

The later [0132-Avoiding Ascent Sequences](https://www.mdpi.com/2073-8994/18/7/1174)
is confirmed by publisher search material and the
[author's publication list](https://math.haifa.ac.il/toufik/manpubff.html).
Publisher-indexed excerpts were available, including the introduction,
parts of the generating-tree discussion, and concluding examples. They
mention additional single patterns including 0120, so a restriction
argument about its title alone would not exclude overlap. Direct full
HTML and static PDF retrieval failed in this pass. No complete review
of its Section 3, or of changes in the journal version of the 021 paper,
is claimed. These access limits persist.

Live searches used the exact pair with ascent-sequence/enumeration terms,
the later paper's exact title, and eligible-rank and initial-count terms.
No equivalent theorem was found in the primary material actually
inspected on 2026-09-13. Several broad searches returned irrelevant hits
and add no evidence. The frozen registry screen was read as a bounded
duplicate check; its underlying registry was not independently reread.

The contribution passes at its explicitly frozen, bounded level: a
self-contained all-length enumeration advancing the checked April
benchmark, with useful compression and no mathematical dependency on
an inaccessible source. The unresolved later-source comparison prevents
claiming worldwide priority or complete exclusion of that paper. Neither
is part of the submitted claim. Failed access has not been used as
evidence of novelty or as a mathematical result. The accepted manuscript
scope must retain these limits and attribute the established generating-
tree/transfer-matrix framework appropriately. A later discovery of an
equivalent result would require reassessing the contribution.

## Final decision and handoff

There is no unresolved mathematical gap in the exact frozen enumeration,
its initialization, its quantifiers, or its arithmetic bound. The full
original structural-enumeration alternative and the bounded contribution
claim pass. Verdict: **accept**.

The next workflow test is the runner's `check-math` integrity/provenance
gate. Writing may then proceed at this accepted scope, preserving the
explicit literature limits. No manuscript or publication artifact was
created in this referee job, and no release or journal-acceptance claim
is made.
