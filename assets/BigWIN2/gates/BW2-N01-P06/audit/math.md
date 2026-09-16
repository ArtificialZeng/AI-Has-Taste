# Mathematical referee report

**Verdict: accept the exact frozen candidate.** The original universally
quantified recurrence is disproved. The accepted kind is `resolution-paper`
and the accepted original status is `disproved`, exactly as frozen in
`claim.json`.

Referee job: `newwin-00001-p06-referee-77844d5045e9`.
Review date: 2026-09-12 UTC.
Snapshot digest:
`22825940b33678e004a1abf4303fabd54b21ca9aca01f8dbc54739e2cc80fa67`.

## Scope and integrity

The submitted claim concerns classical subsequence avoidance of 312 and
54321 by a permutation of {1,...,n}, and classical 132 avoidance by its
composition square. The empty permutation contributes a_0=1. The candidate
asserts all counts through n=11, validity of the proposed recurrence for
6<=n<=10, and its first failure at n=11. It does not assert a corrected
recurrence beyond that range.

I read the frozen original, interpretation, claim, snapshot, and its listed
proof, source, programs, and calculation artifacts. Large membership and
certificate files were read in full by the fresh verification program.
Owner confidence statements were not evidence for this decision. I did not
read checkpoint.md, state.json, earlier audit verdicts, or job transcripts.
All 18 snapshot file hashes and the canonical mapping digest matched before
and after verification. No frozen input was changed. In particular source.md
retains SHA-256
`51c5a2d559d1c8a858630d9de8afe0fb10e5b862ee0f2f5b544c8d7868fe9a75`.

## Reconstructed counting argument

Let b_n count the members ending in 1. If 1 is in position k of a
312-avoider, an entry x before it and y after it must satisfy x<y; otherwise
x,1,y gives 312. Hence the first k values are exactly {1,...,k}, and the
permutation decomposes uniquely as rho direct-sum tau, with rho ending in 1.
The two classical forbidden patterns cannot straddle this boundary, and
squaring preserves the two blocks.

If tau is nonempty, an inversion in tau squared, preceded by any value of
rho squared, would form 132. Thus tau squared must be the identity. Conversely,
rho squared avoiding 132 together with an identity right block suffices:
the only possible mixed 132 would require an inversion in the right block.
The empty right block is allowed.

A 312-avoiding involution is layered. Indeed, if its 1 is in position j,
the preceding decomposition isolates {1,...,j}; involutivity forces the first
value to be j. Any ascent between this first value and the terminal 1 gives
312 with j. Thus that block is the decreasing permutation delta_j. Induction
applies to the suffix. Conversely, decreasing direct-sum blocks give a
312-avoiding involution. Avoiding 54321 bounds every block size by four.

For a member not ending in 1, delete the final decreasing block of its
nonempty layered suffix. Its size j lies in {1,2,3,4}, and the remainder is
a nonempty member of C_(n-j). Conversely, appending delta_j to such a member
preserves all conditions. The boundary is an ascent, so j is precisely the
final decreasing-run length and the alternatives are disjoint. Consequently

    a_n = b_n + sum_{j=1}^{min(4,n-1)} a_(n-j)  (n>=1).

The exclusion of j=n avoids double-counting a wholly decreasing permutation
as both an endpoint and an empty-prefix extension. For n>=5 this gives the
four-term reduction in the dossier. In particular, the original assertion at
each n>=6 is equivalent to b_n=n-1. There is no assumption of hereditary
square avoidance in this argument.

For endpoint completeness, write a length-n endpoint as (alpha+1),1.
A terminal minimum cannot participate in 312. A five-term descent in this
endpoint exists exactly when alpha contains a four-term descent. The
classical endpoint domain at n=11 is therefore a copy of Av_10(312,4321).

For 312-avoiders of length m with decreasing-subsequence length at most h,
the decomposition at the minimum has a left part alpha of length k and a
right part beta of length m-1-k. Its decreasing-subsequence length is
max(LDS(alpha)+1,LDS(beta)). This proves

    f_h(0)=1; f_0(m)=0 for m>0;
    f_h(m)=sum_{k=0}^{m-1} f_(h-1)(k) f_h(m-1-k).

The formula also covers empty alpha and beta. Recalculation gives
f_3(m), for m=0,...,10, equal to
(1,1,2,5,13,34,89,233,610,1597,4181). Thus 4,181 distinct valid classical
endpoint tuples exhaust the domain. The submitted certificate has exactly
that property; its exclusion and inclusion tests are checked below.

## Independent exact verification

I authored and executed `audit/referee_verify.py`, importing no owner code.
Reproduce it from the project root with:

    python3 audit/referee_verify.py

It visits every permutation in S_n for every 0<=n<=11, totalling 43,954,714
tuples; each per-n total is checked against n!. It uses neither the proposed
recurrence nor the direct-sum reduction to generate or count members.

Its 312 detector is justified directly: for a middle position j, an offending
triple exists precisely when some later value lies strictly between p_j and
the maximum of the earlier values. The 54321 detector computes longest
decreasing subsequences using lengths ending at each index. Composition
squares are formed as explicit maps on one-based indices, and square patterns
are tested by generic relative ranks of all triples. Both optimized classical
detectors were compared with generic pattern tests on all 5,914 permutations
through length seven. These finite helper comparisons supplement their
elementary correctness arguments.

The independently obtained counts are:

| n | a_n | b_n (n>=1) |
|---|---:|---:|
| 0 | 1 | — |
| 1 | 1 | 1 |
| 2 | 2 | 1 |
| 3 | 5 | 2 |
| 4 | 11 | 3 |
| 5 | 22 | 3 |
| 6 | 45 | 5 |
| 7 | 89 | 6 |
| 8 | 174 | 7 |
| 9 | 338 | 8 |
| 10 | 655 | 9 |
| 11 | 1265 | 9 |

The run also verified all of the following by exact comparisons:

- The full 1,265-member C_11 set equals the frozen insertion list.
- Every endpoint list for 1<=n<=11 equals the corresponding frozen census.
- The 4,181 classical endpoint tuples in the certificate are distinct and
  equal the complete endpoint domain found by full S_11 enumeration, without
  using the scalar recurrence to establish that equality.
- Every recorded square is the actual composition square. All 4,172 supplied
  exclusion triples have increasing valid indices and relative pattern 132.
  All triples in each of the nine accepted squares avoid 132.
- The classical first-entry counts are 1,597, 1,597, and 987 for entries
  2, 3, and 4. The accepted counts are respectively 5, 0, and 4.
- The scalar domain recurrence and the direct-sum count reduction agree with
  the direct enumeration throughout the claimed range. The relevant numerical
  outputs of all frozen enumerators agree with these newly obtained counts.

The output is `audit/referee_verification.json`; per-length completed results
were saved to `audit/referee_enumeration_progress.json` during the run. A
separate exact parse of the nine permutation/square pairs printed in
`evidence/disproof.md` matched the independently checked list; that check is
recorded in `audit/referee_table_verification.json`.

For n=6,7,8,9,10 the differences between the actual count and the proposed
right-hand side are all zero. At n=11 the difference is -1:

    1265 != 655+338+174+89+10 = 1266.

This establishes both the claimed counterexample and the claimed first-failure
order. The six initial values also agree. One false instance suffices to
disprove the original universal statement; no extrapolation is involved.

## Source comparison and contribution

I checked the frozen primary HTML against the live definitions in Section 1,
the proof of Theorem 4.2, and the recurrence in Section 5. Section 5 specifies
the exact 54321 recurrence and n>=6. The nearest proved case, Theorem 4.2,
uses 4321; its direct-sum/involution method is correctly credited and is
reconstructed above. The conjecture is not a theorem already proved there.
[Archer--Bourne, primary text](https://arxiv.org/html/2505.05218v3#S5).

The live arXiv record identifies v3 of May 13, 2026 as the latest version.
The publisher lists publication on May 19, 2026 in DMTCS 28:1, DOI
10.46298/dmtcs.17199.
[arXiv record](https://arxiv.org/abs/2505.05218),
[publisher record](https://dmtcs.episciences.org/18231).

In addition to reading the frozen literature comparison, I ran these bounded
searches on 2026-09-12:

- `"Archer" "Bourne" "54321" counterexample`
- `"312" "54321" "1265"`
- `"Pattern avoidance in compositions and powers of permutations" "counterexample"`
- `"2505.05218" "conjecture"`
- `"Archer" "Bourne" "54321"`

The returned material included the original-paper metadata, broad listings,
and unrelated matches. No equivalent disproof or later primary resolution
was verified. This is a limited search, not proof of priority or exhaustive
coverage of unpublished work. The frozen contribution uses appropriately
bounded novelty language.

The mathematical delta is an exact refutation of an explicitly stated
published recurrence, including the first failing coefficient and a complete
certificate. It provides a concrete constraint on proposed generalizations
and verified data for subsequent enumeration. The elementary reduction itself
is not claimed as a new method. The contribution passes at its frozen scope.

## Decision and limits

No mathematical gap was identified in the submitted finite computer-assisted
disproof. Scope, correctness, and contribution all pass without changing the
claim. This acceptance covers the complete frozen statement, including its
nine-member endpoint classification and first-failure assertion. It covers
neither a corrected all-n enumeration nor any n=12 observation appearing in
older listed data.

This was a fresh referee context with newly written exact verification code;
it is not a proof-assistant formalization, statistical independence claim,
or journal peer review. No sub-agents, other Codex processes, or background
workers were launched. No manuscript was written. The next workflow step is the runner's
`check-math` gate, followed by a manuscript confined to this accepted scope
with explicit computational disclosure and bounded novelty language.
