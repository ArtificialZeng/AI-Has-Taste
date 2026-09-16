# Citation and bibliography audit

**Verdict: accept.** Eight citation keys and their fixed nearby claims were
verified. All eight occur in the canonical bibliography and final auxiliary
file; there are no missing or unused entries, and no key changed. The canonical
files are `manuscript/main.tex` and `manuscript/references.bib`.

The two-pass evidence is in `audit/citation-claim-ledger.json`,
`audit/citation-verification.json`, and `audit/source-locations.json`. The
row-32 user-library preprint has an ordinary body-flow citation and is bound to
citation attempt 2 and runner launch `bb11bb01-258b-4d78-9bcf-45ceca476259`.

The bibliography is claim-driven rather than Excel-only or padded. OEIS is
cited for the recurrence and live occurrence list; Zeng only for the reported
lower-frontier occurrence; Bays--Hudson for the segmented sieve; Oliveira e
Silva--Herzog--Pardi for a published large-scale finite-verification precedent;
Harris et al. and Lam--Pitrou--Seibert for software provenance; and RFC 9923
for FNV-1a and the little-endian convention. The frozen code, not the RFC,
defines the project-specific tuple serialization. None substitutes for the
accepted exact certificate.

The final key checker reports 8 cited keys, 8 bibliography keys, 0 missing,
0 unused, and identical TeX/AUX key sets. Final LaTeX and BibTeX logs have no
undefined citation, missing database entry, repeated entry, or bibliography
warning. Serial verification was required because the job prohibited agents.
