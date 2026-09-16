# Independent mathematical review

**Verdict: accept the exact frozen claim.** The argument proves the proposed
bijection for every integer n >= 0 and hence the full original enumeration and
formal generating function. There is no scope reduction or additional condition
on the square.

Job: `newwin-00001-p07-referee-c12d29d44a4f`.
Review date: 2026-09-12.
Snapshot: `fe32cd463141d526a90ca7859d55059aa1c6d3392a12234796cdd4a3af87ba8e`.
Frozen kind/status: `resolution-paper` / `proved`.

## Inputs and scope

The review used `source.md`, `problem.md`, `claim.json`, `audit/snapshot.json`,
and its listed proof, verifier, finite observations, literature screen, and
primary HTML. The actual cited primary passages were also inspected online.
No owner checkpoint, scheduling state, earlier job transcript, or earlier
audit verdict was consulted. The proposer assertions of completeness were
not used as evidence. No additional agent or model process was used.

All eight frozen file hashes match, and the snapshot digest independently
matches the SHA-256 of the sorted-key compact JSON file mapping. The frozen
source remains byte-for-byte unchanged, with SHA-256
`f55a25a1a14dbeef692d590d1d55513ad3e234065d61da1ae130416417c7a59e`.
Only referee artifacts in `audit/` were written.

The source and claim use classical subsequence patterns and compositional
powers. The permutation class contains every 312/321-avoider whose cube avoids
2143, with no restriction on its square. The composition class consists of ordered positive
compositions with at most one part outside {1,3}; the exceptional position
is arbitrary and carries no extra mark. Both empty objects are included.
These definitions agree across the frozen source, interpretation, and claim.

## Reconstruction of the decisive proof

1. **Every input avoider has the claimed unique encoding.** Let d be the
   position of 1 in a nonempty 312/321-avoider. If an entry before 1 exceeded
   an entry after 1, those three entries would form 312. Hence all values in
   the length-d prefix are smaller than those in the suffix, and the prefix
   value set is exactly [d]. A descent before 1 would form 321 together with
   1. The prefix is therefore (2,3,...,d,1). Standardizing the suffix by
   subtracting d preserves both avoidance conditions. Recursion terminates
   because it removes at least one entry at every step.

   Conversely, in a direct sum of these cyclic blocks, every entry has at
   most one smaller entry to its right. Either forbidden triple would require
   two. For an arbitrary block list the first minimum occurs at the end of
   its first block, so the recursion retrieves that first part and then the
   remaining list. Induction gives both inverse identities, on the entire
   composition class and the entire avoidance class, respectively. This
   establishes uniqueness and size preservation, not just surjectivity.

2. **Cubing is computed on the invariant intervals.** For a block of length
   d, the action is addition of 1 modulo d, using residues 1,...,d. Its cube is

   \[
   q_d(i)=1+((i-1+3)\bmod d).
   \]

   Thus q_1=(1), q_2=(2,1), q_3=(1,2,3), and for d>=4,
   q_d=(4,5,...,d,1,2,3). The interval of positions and values of each block
   is invariant under all three evaluations, so the cube of the direct sum
   is the direct sum of these q_d. The increasing cases are exactly d=1,3.
   For d=2 the inversion is explicit; for d>=4 the adjacent values d,1
   give an inversion.

3. **Each cubed block avoids 2143.** A non-increasing q_d consists of two
   increasing runs. Every subsequence still has at most one descent between
   successive selected entries: all entries selected from the first run
   precede those selected from the second. The pattern 2143 has two such
   descents. This argument applies to classical patterns, not merely to
   consecutive occurrences. The identity and length-two cases also satisfy
   avoidance.

4. **The direct-sum criterion is exact.** Inversions cannot cross a direct-sum
   boundary. Two inverted summands, the earlier one containing an inversion
   at a<b and the later one an inversion at c<e, give

   \[
   a<b<c<e,\qquad q(b)<q(a)<q(e)<q(c),
   \]

   and hence a 2143 occurrence. Conversely, a 2143 occurrence contains
   inversion pairs (a,b) and (c,e), each within one summand. If both pairs
   belonged to the same summand, all four selected entries would be within
   it, contradicting its internal avoidance. An occurrence therefore requires
   two distinct inverted summands. The hypothesis that every summand itself
   avoids 2143 is essential and is proved in step 3.

   Combining steps 2--4 proves, for every finite positive block list,

   \[
   \left(\bigoplus_i\epsilon_{d_i}\right)^3\text{ avoids }2143
   \quad\Longleftrightarrow\quad
   |\{i:d_i\notin\{1,3\}\}|\leq1.
   \]

   Restricting the already established inverse maps gives exactly the
   claimed bijection. No equality of cubes is used to infer equality of
   the original permutations.

5. **The enumerator has no overcount.** Put
   A(z)=1/(1-z-z^3) and E(z)=z^2+z^4/(1-z). An admissible composition has
   either no exceptional part, or a unique exceptional part between a unique
   ordinary prefix and suffix. Its generating function is therefore

   \[
   A+AEA=\frac1{1-z-z^3}
   +\frac{z^2+z^4/(1-z)}{(1-z-z^3)^2}.
   \]

   All series are formal over the integers; positive part sizes make each
   coefficient a finite sum, and all denominators have constant term one.
   There is no analytic limiting argument or division by a potentially
   vanishing numerical quantity.

The empty list, n=0, a first minimum at d=1 or d=n, single blocks, repeated
ordinary parts, arbitrarily large exceptional parts, and arbitrarily long
ordinary separators are all covered by these arguments. The proof has no
unproved external mathematical dependency or circular step.

## Fresh computational attacks actually completed

`python3 audit/referee_verify.py` completed successfully and produced
`audit/referee-check.json`. This new standard-library script imports no
proposer code, uses direct ranks of subsequences, enumerates compositions
by binary cuts, and computes cubes by three literal applications.

- All **409,114 permutations** of sizes 0 through 9 were checked for the
  input avoidance conditions. For every size, the entire resulting set
  matched the cyclic-block image, and the entire cube-avoiding subset
  matched the restricted image. Both inverse identities were also checked.
  The resulting counts are 1,1,2,4,7,13,23,39,66,110.
- All **1,057 lists** of zero, one, or two arbitrary nonempty 2143-avoiders
  of sizes 1 through 4 were tested against the generic direct-sum lemma.
  The block pool has 32 members and is not restricted to cyclic blocks.
- Every single block of size **1 through 40** and all **400 lists** of at
  most three parts from {1,2,3,4,5,6,7} passed the cube criterion using the
  direct four-subsequence rank detector.
- Formal coefficients through degree **100** agreed between A+EA^2 and
  an independent last-part dynamic count of zero/one-exception compositions.
- Deliberate pitfalls were checked: the one-block permutation 2143 violates
  the lemma if internal avoidance is omitted; (3) and (1,1,1) have different
  encodings but equal cubes; and (2,2) has an identity square but a forbidden
  cube. These illustrate why the proof's actual hypotheses matter.

No counterexample was found. The proposer script and its recorded ranges
were inspected, but its larger tests were not rerun or represented as fresh
referee tests. The all-n conclusion comes from the proof above, not from
finite enumeration. No proof assistant or statistical independence claim
is involved.

## Primary-source comparison and contribution

The nearest result is the cyclic-block encoding in Archer--Bourne,
Lemma 3.1. Their Theorem 3.5 treats squares, while Section 5 explicitly
poses this cube enumeration with no square restriction and an exceptional
part in any position. I compared these passages in the frozen full HTML
with the [versioned primary text](https://arxiv.org/html/2505.05218v3).
The [arXiv history](https://arxiv.org/abs/2505.05218) currently ends at
v3, 13 May 2026; the [publisher record](https://dmtcs.episciences.org/18231)
identifies the May 2026 journal publication.

Archer--Geary, Lemma 2.1, gives compatibility of powers with direct sums.
Its Section 5 and Theorem 5.2 use cyclic blocks for 231/321-avoiders and
length-three targets; the 132 result allows a non-divisor only in the first
part. These statements and the theorem's proof were inspected in the
[primary PDF](https://arxiv.org/pdf/2312.14351). Inference from this comparison:
the machinery is closely related, but the inspected result does not state
the two-inversion 2143 criterion with its unrestricted exceptional position.

The precise contribution is the proved restriction of the known encoding,
including its inverse and complete generating series, settling the expressly
posed conjecture. This is a narrow full resolution with a useful structural
description, not a claim of a new general theory of permutation powers.
Its brevity does not leave any missing quantified cases.

Fresh queries on 2026-09-12 were:

- `"312" "321" "2143" "cube" proof`
- `"Archer" "Bourne" "conjecture" "2143"`
- `"2143" "third power" permutations`
- `"Pattern avoidance in compositions and powers of permutations" conjecture solution`

Relevant returned primary records were the source paper and its publisher
entry; no later equivalent resolution was identified. Unrelated hits were
not treated as evidence. This limited search and the inspected comparisons
support the candidate's bounded novelty language. They do not establish
absolute priority or exclude unpublished or unindexed solutions.

## Gaps, verdict, and next step

No unresolved mathematical gap was found in the frozen candidate. Scope,
correctness, and the identified contribution pass. The outcome is **accept**,
with `candidate_kind=resolution-paper` and `original_status=proved` exactly
as frozen in `claim.json`.

The release contract was read completely before writing `audit/math.json`.
That file binds only this verdict, this job, this snapshot, and this report.
The runner should now perform `check-math` and, if provenance and integrity
pass, dispatch manuscript preparation at the accepted scope. This referee
job creates no manuscript, PDF, publication record, or fabricated role file.
Manuscript, citation, build, and visual release checks remain later phases.
