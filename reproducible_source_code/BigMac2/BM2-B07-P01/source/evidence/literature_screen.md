# Focused literature screen (2026-09-08)

## Sources inspected

1. Hikaru Manabe, *Purely Periodic Three-move Subtraction Games*,
   arXiv:2609.05358v1 (2026), locally preserved as
   `literature/2609.05358v1.pdf` (SHA-256
   `39457676064479f1ff52fded8697695c1ddd598f63665996b2eb889ec6fa66ca`).
   Theorem 32 proves the admissible-angle direction; Conjecture 50 states
   necessity.  The paper says necessity remains open outside identified
   slices/families.  Its bibliography was checked for prior fixed-shape
   results.

2. Anonymous, *Notes on Subtraction Games*, dated 2009-07-16, eight-page
   informal PDF hosted at
   <https://subtractiongames.wordpress.com/wp-content/uploads/2012/02/subgames2.pdf>
   (web text inspected 2026-09-08; author metadata and a stable publication
   record were not present).  Theorem 6.6 **states without a proof** that
   for \(S=\{2,5,c\}\), \(c>7\), the preperiod is \(c+8\) for
   \(c\equiv0\pmod7\), \(c+3\) for \(c\equiv4\pmod7\), and zero otherwise.
   It also states an eventual-period table.  The displayed period
   \(c+3\) for residues 3 and 6 conflicts with exact mex computation and
   with Manabe's candidate \(c+5\); for example, \(c=10\) has least period
   15, not 13.  The note uses an indexing convention beginning with
   \(G(1)\), contains visible unfinished passages elsewhere, and supplies
   no argument after Theorem 6.6.  It is therefore important prior evidence
   for the classification, but not an audited proof of the frozen claim.

3. Shun-ichi Zhang, *On the linearity of the periods of subtraction games*,
   Theoretical Computer Science 985 (2024), 114350,
   <https://doi.org/10.1016/j.tcs.2023.114350>.  Its abstract and the uses
   catalogued in Manabe were screened.  It proves several linear families,
   but the searches performed did not identify the complete \(\{2,5,c\}\)
   classification there.

## Searches and limitation

Exact web/arXiv searches included `"{2,5,c}" subtraction game`,
`"{2, 5, c}" subtraction game`, `"2, 5, c" Sprague Grundy`, and the exact
title of Manabe's paper.  These found the 2009 note above and Manabe's 2026
preprint, but no peer-reviewed or arXiv proof of the fixed-shape theorem.
This is a focused screen, not proof of priority.  Accordingly the candidate
contribution is described conservatively as a complete, reproducible proof
of the frozen claim and of exact word formulae, while recording that the
overall preperiod classification was already stated informally in 2009.
