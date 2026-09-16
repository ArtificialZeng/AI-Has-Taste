# Primary-source comparison for the recurrence proof candidate

Job: newwin-00001-p02-research-0e4a4dc1b1e3.
Inspected and searched: 2026-09-12.

The nearest inspected primary work is Jia Huang and Erkko Lehtonen,
*Associative-commutative Spectra for Some Varieties of Groupoids*,
Enumerative Combinatorics and Applications 4:4 (2024), Article S2R29.
The [journal PDF](https://ecajournal.haifa.ac.il/Volume2024/ECA2024_S2A29.pdf)
is copied in full to `evidence/external/huang-lehtonen-2024.pdf`; the full
cached extracted text is also copied to the adjacent `.txt` file.
`evidence/external/provenance.json` records their original locations, byte
counts, and SHA-256 hashes. These are primary-source inputs, not an authored
manuscript. The PDF hash agrees with the intake record.

I independently extracted and read PDF page 1 (Definition 1.1) and page 17
(Section 7). The former uses fixed-order one-use variables for the
associative spectrum. The latter gives exactly the operation table in
source.md and lists nine initial counts, relating them to a Padovan
trisection while leaving a general result undetermined. This is the nearest
prior mathematical statement used to assess the candidate's contribution.

I also opened the live [author preprint HTML, Section 7](https://arxiv.org/html/2401.15786v1#S7)
and [arXiv version page](https://arxiv.org/abs/2401.15786). The table, the
nine-term list, and the absence of a general result in that discussion agree
with the copied journal pages. The retrieved version page lists v1. The
journal PDF web open returned an Internal Error, and a direct HTTPS download
from the command environment was denied by the network sandbox. Neither
failure is evidence about the mathematics; the copied complete primary
document and live author HTML provide the needed comparison.

Live query strings in this research pass included:

* `"SC258" associative spectrum`
* `"Huang" "Lehtonen" "Padovan"`
* `"SC258" "spectrum" "groupoids"`, restricted to arxiv.org and ecajournal.haifa.ac.il
* `"associative spectrum" "Padovan"`
* `"associative spectra" "SC258"`
* `"SC258" "normal forms"`
* `"Associative-commutative spectra for some varieties of groupoids"`
* `"SC258" groupoid Padovan proof`
* `"pruning" "associative spectrum"`
* `"Padovan" "groupoid" recurrence`

The relevant hits led to the journal paper and its author preprint. Numerous
SC258 and pruning hits concerned unrelated subjects and were excluded;
secondary index pages were used only as locators. No later equivalent
all-arity resolution was found in this bounded search. This is not a proof
of priority or a complete citation-network review. Unindexed work,
unpublished results, and broader finite-algebra classifications have not
been exhaustively searched. The previous bounded screen remains in
`evidence/triage-literature.md`.

The candidate's proposed delta is explicit: it proves that pruning gives
distinct ordered term functions exactly when the resulting labeled trees
differ, classifies the possible omitted terminal intervals, and deduces the
original all-n recurrence. The proof does not use a recurrence attributed
to OEIS as a premise. It does not settle the other tables or the
associative-commutative spectrum mentioned alongside SC258.

Bibliographic issue for the later citation phase: the journal PDF header
prints DOI suffix ECA2024V4S3R29, while the arXiv-linked metadata displays
ECA2024V4S4R29. This discrepancy has not been resolved here; cite the verified
title, authors, journal, article number, and direct primary URL unless the
DOI is checked separately. It does not affect the operation table or proof.
