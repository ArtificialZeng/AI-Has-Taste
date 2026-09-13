# Citation audit

Audit date: 2026-08-29  
Mode: two-pass, claim-by-claim verification against primary records  
Status: **PASS**

## Scope and outcome

The manuscript contains two bibliography entries and fourteen frozen claims in
`audit/CITATION_CLAIMS_PASS1.md`. Both references were independently checked
against their DOI records, publisher/journal pages, arXiv records, and the
relevant theorem or conjecture in the papers. No citation key changed and no
unverified bibliography item remains.

## Berlow2021

- Katalin Berlow, *Restricted Stacks as Functions*, *Discrete Mathematics*
  344(11) (2021), article 112571.
- DOI `10.1016/j.disc.2021.112571` and arXiv `2008.01164` agree on author,
  title, year, and article metadata.
- Definition 1.3 defines the map `s_T`; Theorem 4.5 proves that the periodic
  points of `s_{123,132}` are exactly the half-decreasing permutations.
- The manuscript wording was narrowed from an unnecessary priority claim to
  “defined and studied the T-restricted stack map”.

Primary records:
<https://doi.org/10.1016/j.disc.2021.112571> and
<https://arxiv.org/abs/2008.01164>.

## Zhang2025

- Owen Zhang, *The Order of the (123, 132)-Avoiding Stack Sort*,
  *Enumerative Combinatorics and Applications* 5(3) (2025), article S2R18.
- DOI `10.54550/ECA2025V5S3R18` and arXiv `2405.01854` agree on the substantive
  metadata. The journal's official Crossref export has a malformed author
  field, so the correctly parsed author already in `references.bib` is kept.
- Theorem 1.2 supports the exact maximum transient used in the manuscript.
  Conjecture 4.4 states `|M_{2n}|=(n+1)|M_{2n-1}|`, and the preceding text
  reports verification through `n<=6`.

Primary records:
<https://doi.org/10.54550/ECA2025V5S3R18> and
<https://arxiv.org/abs/2405.01854>.

## Frozen-claim disposition

- CC01, CC02, CC06, CC07: supported directly by the cited primary papers.
- CC03--CC05 and CC09--CC13: new local exact results; supported by the frozen
  integer certificate, the two discovery enumerators, the no-import verifier,
  the exact factorization attack, and `audit/PROOF_AUDIT.md` rather than by an
  external citation.
- CC08: retained only in the bounded form “first relation beyond that reported
  range”; it does not claim worldwide priority.
- CC14: verified from the recorded project process and manuscript source.

The final LaTeX build must still be rerun after the wording change above; this
file audits citation truth and metadata, not typesetting.
