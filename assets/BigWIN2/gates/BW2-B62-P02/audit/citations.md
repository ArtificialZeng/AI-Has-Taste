# Citation and bibliography audit

## Method and frozen extraction

This noninteractive audit used search verification on 2026-09-07. The first
pass extracted the four claim/citation pairs and froze them, without
verification, in `audit/citation-claim-ledger.json`, bound to SHA-256
`d621b46e8416739cfff803dd1b9ba669ead25bff4e060372a7b16615c4963ea6`.
The second pass verified only that ledger. Per-citation delegation was not used
because the job prompt expressly prohibited agents and other workers. Structured
source locations and per-claim results are preserved in
`audit/citation-verification.json`.

## Claim-to-source verification

| ID | Key | Status | Exact source location and support |
|---|---|---|---|
| CIT-001 | `ConnorEtAl2026` | Verified (paraphrase) | Connor et al., arXiv:2509.25150v3, PDF p. 4, defines comparison by each agent's best match in the set, strict votes in both directions, popular-winning sets, and instance dimension. The official arXiv record identifies v3 and its six authors: <https://arxiv.org/abs/2509.25150>. |
| CIT-002 | `ConnorEtAl2026` | Verified (exact) | The same PDF, p. 4 Table 1, gives the marriage/unweighted-with-ties entry as `2,3`; p. 10, Theorem 3.3, gives a popular-winning set of size three for the general weighted-with-ties marriage case. Exact full-text searches for `K_{3,3}`, `three-by-three`, `3-by-3`, and `fixed complete` found no fixed census. |
| CIT-003 | `ZengEtAl2026` | Verified (paraphrase) | The primary Preprints.org record, Sections 3, 4, and especially 6, describes integer predicates, symmetry-reduced orbit enumeration, a standard-library verifier, and a separate exact implementation for fixed ternary coordinate libraries: <https://www.preprints.org/manuscript/202608.1658>. The manuscript accurately limits this to an architectural comparison. |
| CIT-004 | `LamPitrouSeibert2015` | Verified (paraphrase) | The official LLVM-HPC2 workshop agenda identifies Lam and the paper, while the publication abstract describes a Python JIT compiler focused on scientific and array-oriented computing; the official Numba documentation recommends the ACM proceedings paper. DOI <https://doi.org/10.1145/2833157.2833162>. |

All title, author, identifier, venue/type, and date fields were checked against
the primary/official records. The canonical bibliography already records the
Connor paper's official 2025 submission year and separately identifies v3 and
its 4 September 2026 revision. No metadata repair or citation-key change was
required in this attempt. No claim was misquoted, numerically erroneous,
misleading, or unsupported.

## Bibliography coverage and necessity

- Connor et al. is indispensable: it is the problem-origin, definition, general
  bound, and closest-prior-result source.
- Lam--Pitrou--Seibert is needed for the nontrivial software-method description
  of Numba as the JIT used by the exhaustive programs.
- Zeng et al. is the single genuinely relevant active user-library work. Its
  body-flow citation supports the expressly limited comparison of exact finite
  certificate architectures; it is not presented as a mathematical dependency.

The bibliography is therefore not library-only and not padded. The manuscript
derives its elementary counting identities and states its computational
predicate self-containedly; no additional external result is silently relied
upon. The absence of a priority claim avoids converting the bounded literature
screen into a novelty theorem.

Mechanical extraction found three cited keys and three canonical BibTeX
entries, with no missing, unused, duplicate, or AUX-inconsistent key. The final
BibTeX/log scan found no undefined citation, missing database entry, repeated
entry, or bibliography warning.
