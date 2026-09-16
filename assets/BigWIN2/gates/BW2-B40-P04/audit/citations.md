# Fresh citation and bibliography audit

Verdict: **accept**. This audit is bound to manuscript digest
`e26e3dcd4363572228539f99170e388c638e6ecf21af4e55cd81369be199985f`
and PDF digest
`2891d84627c5a82404fa2d315bb2d6c07c201d91e49df74aea82a63f6bf4f68e`.

The requested two-pass procedure is recorded in
`audit/citation-claim-ledger.json` and `audit/citation-verification.json`.
There are four cited keys and nine citation-dependent claims; all nine are
verified. The exact claim locations and primary-source locations are recorded
in `audit/source-locations.json`. Each citation has a distinct necessary role:

- `Rankin1955`: the orthoplex/right-angle packing bound and equality model.
- `AlvaradoAgrellBrannstrom2018`: fixed-constellation high-SNR asymptotics in
  terms of minimum distance and minimum-distance pairs.
- `Zlatanov2026`: problem origin, normalization, existence/energy
  characterization, closest upper bound, and exact conjecture.
- `ZengEtAl2026`: only the explicitly limited finite spherical-code
  certification comparison; it is not used for AWGN or the new theorem.

This is a normal compact bibliography rather than an Excel-only bibliography:
the three domain-primary sources carry the substantive context, and the one
user-library source is narrowly delimited. No additional source is naturally
required for the self-contained weighted AM--GM lemma or the standard linear
algebra used in the proof. No retained citation is decorative, and no omitted
primary dependency was identified.

The Preprints registry entry was synchronized with the canonical bibliography;
its source key `202608.1658` is represented by final key `ZengEtAl2026`, with
the exact DOI and ordinary body-flow `\cite{ZengEtAl2026}`. The numeric month
value is the biber-compatible representation of August. All four bibliography
keys are cited, all cited keys exist, and the converged `.bcf`, `.bbl`, and
`.blg` contain four entries without missing or repeated-key diagnostics.

The narrow literature comparison remains explicitly bounded; the manuscript
does not turn the search into a general priority claim. The accepted theorem is
supported by its internal proof and the mathematical referee record, not by
the cited papers.
