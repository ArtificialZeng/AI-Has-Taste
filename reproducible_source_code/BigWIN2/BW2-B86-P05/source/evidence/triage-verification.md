# Triage verification record

Date: 2026-09-10 (Asia/Shanghai)  
Job: `win-00086-p05-triage-6a25ad865982`

## Source and status checks

- `source.md` was read with SHA-256
  `d75270377823488dfaa65912e4a0a2bd57b396960d1b0ebb4865216db77bfb7f`.
- Z. He and J. Wu, *Nonexistence Results and Constructions for Signed
  Difference Sets*, <https://arxiv.org/abs/2608.22936>, was inspected on
  2026-09-10. The arXiv history showed only v1 (submitted 2026-08-24).
  Equation (1.1) gives the definition, equations (2.3)--(2.4) and Lemma 2.1
  give the principal/nonprincipal character conditions, and Theorem 4.4 is
  the nearest near-full-support obstruction. The paper reports a fixed
  open-case snapshot and does not state a resolution of this exact entry.
- The authors' primary reproducibility repository,
  <https://github.com/zhiwenhe94/sds-open-case-verification>, was inspected on
  2026-09-10. Its README says that `sds.json` is a fixed LJCR snapshot and
  defines status `Open` as unresolved. The frozen source records the exact
  row as `Open` at commit
  `de57332884c7bf417544285dee9a2cbb015a5fae`.
- D. M. Gordon, *Signed Difference Sets*,
  <https://arxiv.org/abs/2212.10630>, was inspected for the foundational
  definition and normalization convention. Bounded exact-assertion and
  equivalent-language searches found no later primary paper resolving this
  entry. This is a literature-screening result, not proof of novelty.
- Limitation: the 4.95 MB live GitHub JSON row could not be rendered by the
  web interface, and direct shell retrieval was network-blocked. Therefore
  the current live database row was not independently extracted; the frozen
  commit status and current repository metadata were verified separately.

## Exact computational checks

`python3 evidence/exact_character_check.py` completed successfully. It found
48 matrices in (GL(2,3)), all 28 unordered negative pairs, and exactly two
orbits: opposite pairs (size 4) and independent pairs (size 24). No pair had
all eight nonprincipal Eisenstein norms equal to 7, and no pair had all eight
nonzero autocorrelations equal to 1. Script SHA-256:
`14df63f42720c4064149d01f51ee0bf2c3d61225afdcfbc53682343d90d6f81a`.

As a symmetry-free cross-check,
`python3 evidence/full_assignment_check.py` enumerates all
(9\cdot2^8=2304) placements/sign assignments using only integer periodic
autocorrelations. It reports zero solutions. These finite computations are
exact evidence and replayable checks, but triage does not certify the proof.

## Hand check behind the proposed proof

After the justified principal-character, translation, and global-sign
normalizations, the two negative points are either opposite or independent.
For an opposite pair a character trivial on their line gives norm 25. For an
independent pair a character taking value (omega) at both points gives norm
13. Both contradict the necessary norm 7. A later fresh referee must audit
the normalizations, orbit exhaustion, and character choices without relying
on the computations alone.
