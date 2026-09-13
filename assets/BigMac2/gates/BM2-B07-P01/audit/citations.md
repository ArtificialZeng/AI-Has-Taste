# Fresh citation and claim-to-source audit

Audit job: `bigMac-00007-p01-release-73c3ff96116c`; audit date: 2026-09-08.
The requested `citation-check-skill` was explicitly invoked in advisory search
mode.  Its two-pass discipline was used: the list below was fixed before any
search verification, then each item was checked against primary records and
the compiled manuscript.  The skill did not override the accepted mathematics
or any user-designated bibliography.

## Pass 1: extracted claims

- C01: Manabe's 2026 preprint exists with the title and arXiv metadata printed
  in the bibliography.
- C02: Manabe proves that an admissible angle gives full-nim pure periodicity
  and that the least period is the least admissible candidate; necessity is
  Conjecture 50.
- C03: for `(a,b)=(2,5)`, the three source predicates specialize to
  `Theta_7={2,5}`, `Theta_{c+2}={1,5}`, and `Theta_{c+5}={2,3,6}`.
- C04: Manabe's cited results include the endpoint `c=6` and exclude a
  proper-divisor collapse for this primitive non-harmonic shape.
- C05: Zhang's 2024 paper exists with the title, venue, article number and DOI
  in the bibliography, and treats other fixed-base slices rather than the
  complete all-`c` `{2,5,c}` family.
- C06: the anonymous *Notes on Subtraction Games* exists, is dated July 16,
  2009, and its Theorem 6.6 states the cited preperiod classification for
  `{2,5,c}` without supplying the proof used in this manuscript.
- C07: that note's displayed positive-period table is discrepant: it gives
  `c+3` in residues 3 and 6, while the source criterion and the proved theorem
  here give `c+5`.
- C08: all three bibliography entries resolve in the rendered PDF and every
  nearby attribution is bounded to what the inspected source supports.

## Pass 2: fixed-list verification

| Claim | Status | Evidence and support check |
|---|---|---|
| C01 | Verified (exact) | Local `literature/2609.05358v1.pdf`, including its title page, is arXiv:2609.05358v1 by Hikaru Manabe, dated 4 September 2026.  Fresh title, author/year/title, venue, and arXiv-ID searches returned the same current arXiv abstract record. |
| C02 | Verified (exact/paraphrase) | In the local PDF, Theorem 32 (PDF pp. 21--23) states the sufficient criterion, full nim-sequence pure periodicity and least admissible period; Proposition 46 (PDF p. 32) proves minimality; Conjecture 50 (PDF p. 33) states necessity.  The hypotheses `a>=2`, primitivity, `c>b`, and non-additivity are retained in the manuscript. |
| C03 | Verified (exact derivation) | Substitution `a=2`, `b=5`, `delta=3`, `eta=1`, `epsilon=1` into Lemma 14, Theorem 28 (PDF pp. 19--20), and Theorem 57 (PDF p. 35) gives exactly the three displayed sets. |
| C04 | Verified (exact/paraphrase) | For `c=6`, all hypotheses of Theorem 32 hold and residue 6 is in `Theta_{c+5}`.  Proposition 46 rules out a shorter period; its harmonic exception is irrelevant because 5 is not a multiple of 2. |
| C05 | Verified (metadata exact; scope paraphrase) | Fresh author/year/title, exact-title, venue, and DOI searches located the Elsevier record and Shenxing Zhang's author-hosted paper.  They give *On the linearity of the periods of subtraction games*, *Theoretical Computer Science* 985 (2024), article 114350, DOI `10.1016/j.tcs.2023.114350`.  The paper's abstract and Theorem 1.4 give the fixed-`S`, varying-`c` program and only specified slices; Manabe's discussion (PDF pp. 6 and 34--35) likewise identifies Zhang's `b=2a`, `b=a+1`, and ultimately bipartite slices, not a complete `{2,5,c}` classification. |
| C06 | Verified (exact) | Fresh title/date/filename searches located the primary PDF at `https://subtractiongames.files.wordpress.com/2012/02/subgames2.pdf`.  Its title page says July 16, 2009, and PDF page 7 (printed p. 6) has Theorem 6.6 with preperiod `c+8` for residue 0, `c+3` for residue 4, and zero otherwise.  The next item is Theorem 6.7; no proof of Theorem 6.6 is supplied there. |
| C07 | Verified (exact) | Theorem 6.6 of that note prints period `c+3` for residues 3 and 6.  Manabe's specialized admissibility theorem gives candidate `c+b=c+5` there, agreeing with the present proved statement.  The manuscript calls this only a discrepancy and makes no priority claim. |
| C08 | Verified | `pdftotext` shows numbered references `[1]`--`[3]` and their in-text uses, with no question marks or missing entries.  The final compiler log has no undefined citation or reference diagnostics. |

## Dependency and limitation review

The complete publication source list was checked exactly as declared:
`evidence/fixed_shape_certificate.py`, `manuscript/main.tex`, and
`manuscript/references.bib`.  The TeX file has no authored imports beyond the
declared bibliography; the certificate is the explicitly mentioned supporting
file.  Generated `.bbl` and TeX system packages are build products/system
dependencies, not authored publication sources.

`literature/user_bibliography_check.md` was explicitly checked and is absent
from the project, so no user-workbook DOI/BibTeX record exists here to inspect,
override, or draw an additional citation from.  This operational absence is
not treated as evidence that any cited work is nonexistent.  The manuscript
already includes the genuinely relevant Manabe and Zhang papers.  All three
cited records and their nearby claims were verified within the bounded audit.
No unsupported novelty claim, contradicted attribution, removable citation,
undefined key, or remaining citation-access limitation was found.

Primary records consulted in pass 2 were the local Manabe v1 PDF and current
arXiv record (`https://arxiv.org/abs/2609.05358`), the Elsevier DOI record and
Zhang author-hosted paper (`https://doi.org/10.1016/j.tcs.2023.114350`), and
the anonymous note PDF above.  The search date for every record was 2026-09-08.

Verdict: **accept**.
