# Search log

## Gate 1: `NOVELTY_LOCK`

Search date: 2026-08-30 (Asia/Shanghai).  Target frozen as the quantified
finite-integer equal-length problem in `problem/formal_statement.md` before
route computation.  The search covered original/publisher records, DOI and
Crossref metadata, arXiv revisions, recent citing/adjacent papers, OpenAlex,
DBLP, MaRDI/zbMATH-linked records, TheoremDB's dated public packet, and public
code discovery.  Google Scholar could not be treated as an exhaustive index;
all negative results below are database- and query-bounded.

### Primary records opened and checked

- TheoremDB P2824 snapshot (reviewed 2026-07-28), including all seven listed
  references and records R18--R32.  It reports the problem open and supplies
  exact inline Python/C++ artifacts for the \(\{0,1,2,4\}\) baseline.
- Ingrid Vukusic, arXiv:2506.21200v1 and the version of record in *American
  Mathematical Monthly* 133(4), 371--375, DOI
  `10.1080/00029890.2025.2545706`.  Crossref returned title, author, volume,
  issue, pages, and publication date 2025-09-09; OpenAlex work
  `W4414163255` returned zero citations on the query date.
- Jonathan Andrade and Lucas Mol, arXiv:2408.15390v2 (2025-02-14) and WORDS
  2025, LNCS, pp. 24--36, DOI `10.1007/978-3-031-97548-6_3`.  Crossref and
  DBLP both identify the version of record; OpenAlex work `W4411772264`
  returned zero citations on the query date.
- Pierre Popoli, Jeffrey Shallit, and Manon Stipulanti, *Additive Word
  Complexity and Walnut*, FSTTCS 2024, DOI
  `10.4230/LIPIcs.FSTTCS.2024.32`; publisher metadata, PDF, introduction,
  additive-power discussion, and bibliography checked.
- Giuseppe Pirillo and Stefano Varricchio, *On uniformly repetitive
  semigroups*, *Semigroup Forum* 49 (1994), 125--129, DOI
  `10.1007/BF02573477`; Crossref metadata and European Digital Mathematics
  Library record checked.  (One secondary index says issue 2/pages 125--130;
  the Crossref/version-of-record metadata says issue 1/pages 125--129, which is
  used here.)
- Allen R. Freedman and Tom C. Brown, *Sequences on Sets of Four Numbers*,
  *Integers* 16 (2016), A33; full 10-page journal PDF, Theorem 1, table,
  historical remarks, and bibliography checked.
- Tom Brown, *Approximations of Additive Squares in Infinite Words*,
  *Integers* 12(5) (2012), 805--809, DOI
  `10.1515/integers-2012-0006`; version-of-record metadata and full paper
  checked.
- Micha\"el Rao and Matthieu Rosenfeld, *Avoiding Two Consecutive Blocks of
  Same Size and Same Sum over \(\mathbb Z^2\)*, *SIAM J. Discrete Math.* 32(4)
  (2018), 2381--2397, DOI `10.1137/17M1149377`; arXiv:1511.05875v2, journal
  PDF, displayed morphism, spectral criterion, theorem, and arXiv ancillary
  source checked.
- Lorenz Halbeisen and Norbert Hungerb\"uhler, *An Application of van der
  Waerden's Theorem in Additive Number Theory*, *Integers* 0 (2000), A7; full
  PDF checked to confirm that adjacent equal-sum segments are not constrained
  to equal lengths.

### Exact web/search queries

- `"additive square" infinite word finite alphabet integers`
- `"additive-square-free" word 62 {0,1,2,4}`
- `site:arxiv.org additive squares words finite alphabet`
- `site:doi.org "additive squares" words`
- `"additive square problem" infinite word 2026`
- `"additive-square-free" OR "additive square-free" morphism`
- `site:github.com "additive square" words`
- `site:arxiv.org "additive square problem"`
- `Pirillo Varricchio "On uniformly repetitive semigroups" DOI`
- `"On uniformly repetitive semigroups" Semigroup Forum 49 1994`
- `"Approximations of additive squares in infinite words" DOI Brown 2012`
- `"Sequences on Sets of Four Numbers" Freedman Brown citations`
- `"Avoiding two consecutive blocks of same size and same sum over Z2"`
- `"Avoiding abelian and additive powers in rich words" DOI journal`
- `Crossref "On uniformly repetitive semigroups" "10.1007/BF02573477"`
- `zbMATH "additive square" infinite word`
- `"Avoiding additive squares over" Rao Rosenfeld SIAM DOI`
- `site:epubs.siam.org "additive squares" "Rosenfeld"`

### API/database checks

- Crossref `/works/{doi}` for Vukusic, Pirillo--Varricchio, Andrade--Mol, and
  Brown; Crossref title/author query recovered Rao--Rosenfeld DOI
  `10.1137/17M1149377`.  A direct Crossref lookup for the case-sensitive
  Dagstuhl DOI returned HTTP 404 even though the Dagstuhl DOI landing page and
  BibTeX export are live; this failed query is retained rather than hidden.
- OpenAlex DOI lookups for Vukusic and Andrade--Mol, including work IDs and
  citation counts as of the query date.
- DBLP author/conference records for Freedman--Brown and WORDS 2025.
- MaRDI's zbMATH/OpenAlex-linked record for Brown (2012).
- Public-code searches found arXiv ancillary code and TheoremDB inline exact
  code, but no GitHub repository claiming a full finite-integer solution.

### Pass-1 conclusion

The source boundary is sound: the canonical \(\mathbb Z\) problem is distinct
from the \(\mathbb Z^2\) construction, additive cubes, close-sum theorems,
unequal-length equal-sum segments, rich-word higher powers, and finite fixed
alphabets.  The most recent primary sources located still call the canonical
problem open.  Formal publication metadata in the supplied packet was partly
stale and has been corrected above.  `NOVELTY_LOCK` is therefore **locked for
discovery**, not a claim that no work after the indexed search exists.

## Gate 6 pass 2: result-specific novelty search

Run after the exact certificates produced the candidate values 86 and 88.
Queries:

- `"g(0, 1, 2, 5)" additive square`
- `"g(0, 1, 3, 5)" additive square`
- `"{0,1,2,5}" "additive square" word`
- `"{0,1,3,5}" "additive square" word`
- `"299596819" additive square`
- `"234485149" additive square`
- exact ten-letter prefixes of each certified maximizer plus `additive`
- `"2-uniform morphism" "abelian square" fixed point four letters`
- `"binary uniform morphism" abelian-square-free`
- `"uniform morphism" "abelian square-free" 4 letters`
- `site:arxiv.org abelian-square-free pure morphic word eigenvalues`

Findings:

- No occurrence of either exact \(g\)-value, tree count, or maximizer prefix was
  located.  Searches returned Freedman--Brown's balanced-family paper but no
  table entry for either unbalanced alphabet.
- The morphism search located the known 85-uniform Ker\"anen construction and
  TheoremDB P2822's dated statement that the unrestricted least uniform modulus
  remains unknown.  It did not locate the explicit unrestricted modulus-2
  census stated here.
- An OpenAlex free-text query for the Freedman--Brown title was dominated by
  biological “sequence” records and did not identify the paper.  A Semantic
  Scholar API query returned HTTP 429.  These failures are recorded and reduce
  novelty confidence; they are not silently treated as negative evidence.

Conclusion: the exact finite values and unrestricted four-state modulus-2
no-go statement were **not located in the recorded pass-2 search**.  No claim
of priority, first discovery, or exhaustive bibliographic coverage is made.
