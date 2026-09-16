# Triage verification record

Job: `win-00085-p01-triage-310493b59e59`  
Date: 2026-09-10 (Asia/Shanghai)

## Frozen-source and handoff check

- Intake SHA-256 of `source.md`:
  `8bdbd0fa48aea26f73f732eaeb115a15243603a548dc4dabaca4647bf1af6990`.
- Enumerating `literature/*handoff*.md` returned no files.

## Primary-source verification

- Mahmoud, arXiv:2607.26214v1:
  https://arxiv.org/abs/2607.26214 and
  https://arxiv.org/pdf/2607.26214. The live arXiv record listed only v1,
  submitted 2026-07-28. PDF p. 11 (parsed page index 10), Question 5.4,
  displays the two requested LU-plus-permutation questions; Theorem 5.3(ii),
  (iii) displays the four generator triples. Limited searches for the title,
  question, and distinctive generator strings found no later primary
  resolution. This supports only `open-supported as of 2026-09-10`.
- Van den Nest--Dehaene--De Moor, arXiv:quant-ph/0404106v2:
  https://arxiv.org/pdf/quant-ph/0404106. PDF p. 5, equation (14), identifies
  the dimensions of binary stabilizer subspaces supported in a coordinate set
  with degree-two local-unitary invariants.

## Replayed exact finite calculation

Running `python3 evidence/triage_exact_check.py` completed successfully. It
checked pairwise commutation, binary rank three, eight distinct signed Pauli
elements per stabilizer, all support profiles, and all 5! or 6! coordinate
permutations. The decisive small support data are:

- `S_A`: the only three-subsets with `d_S(A)=1` are `{1,2,5}` and
  `{3,4,5}`; their intersection has size 1.
- `S_B`: the only three-subsets with `d_S(A)=1` are `{1,3,4}` and
  `{2,3,4}`; their intersection has size 2.
- `S_+`: on four-subsets the histogram of `d_S(A)` is `{0: 12, 1: 3}`.
- `S_-`: on four-subsets the histogram of `d_S(A)` is `{0: 14, 2: 1}`.
- Exhaustion returned zero coordinating permutations for either full profile.

Intersection cardinality and the unlabelled histogram are invariant under a
coordinate permutation. Combined with the cited LU invariant, these exact
observations are a short proof skeleton that both existential assertions are
false. At triage they remain discovery evidence, not a refereed resolution.
