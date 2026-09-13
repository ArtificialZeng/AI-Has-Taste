# Checkpoint

## State and decisive evidence

- `source.md` remains byte-identical, SHA-256
  `8bd964b5b75c92eacd0c227be016ba78920c6b599f27b2331de2cdea771f4e98`.
- The accepted referee record is `audit/math.json`, job
  `bigMac-00003-p01-referee-a05629b0cde1`, bound to evidence snapshot
  `f6645e17ef0677c1caa881429b8de75fbb9db2c4b2f4ed0fd99027c5555af0f1`.
- Release job `bigMac-00003-p01-release-288b9c70330b` clean-built the unchanged
  single-source manuscript and refroze it.  The manuscript digest is
  `2a1f336f0088850ae32cc1ad1db6bd35b78664b26af3a499ddce46fdfbc35320`;
  the three-page PDF digest is
  `3cfe689095e44a9b1e0d5193fbedc15b900446887c5d524b4ff9553126952b0a`.
- `manuscript/main.log` is nonempty, has SHA-256
  `c4c32330c79675a883f1855e039aadf6ee319cffd97a06de0d5109e96beba5f1`,
  and contains no warning, unresolved citation/reference, box warning, or
  error.  All 19 subset fonts are embedded with Unicode maps.
- The explicitly invoked citation checker froze 18 claims before verification.
  All 18 passed.  Korsky's supplied paper and live arXiv record support the
  signed-count convention and exact `1/3` and `47/122` comparisons.  The
  required user-listed Zeng paper was read in full; only its actual coset-block
  and quotient-fiber constructions are attributed, and the manuscript says it
  is not used in the theorem.
- Fresh 160-dpi renders of pages 1, 2, and 3 were individually inspected.  No
  clipping, overlap, illegible mathematics, bad wrapping, or other visual
  defect was found.
- The official `release_gate.py check` returned `ok: true` for this exact
  snapshot/manuscript/PDF/build-log state, with three pages and release job
  provenance `bigMac-00003-p01-release-288b9c70330b`.

## Obstacles

The current web gateway did not expose the exact SSRN/DOI landing pages for
Zeng's paper.  This bounded optional-metadata limitation is recorded in
`audit/citations.md`; author, title, date, and cited content were verified from
the supplied six-page primary PDF and the user-bibliography record.  The paper
does not print or rely on the DOI.  No release blocker remains from that limit.

## One next test

The supervisor should run `release_gate.py publish` and verify that the active
manifest binds PDF digest
`3cfe689095e44a9b1e0d5193fbedc15b900446887c5d524b4ff9553126952b0a`.
