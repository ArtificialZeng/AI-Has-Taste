# Search log

Search date: 2026-08-22 (Asia/Shanghai).

## Frozen questions

1. Is the global conjecture still open in current primary sources?
2. What is the strongest safe universal frequency constant, and which decimal
   improvements rely on numerical hypotheses?
3. What finite ground-set and family-size ranges are already known?
4. What is the exact Poonen LP/Farkas criterion?
5. Which \(FC(k,n)\) values and upper bounds are published?
6. Are the candidate sharpenings \(FC(4,9)\le20\) or
   \(FC(5,8)\le35\) already stated?

## Primary-source queries and records

- arXiv title/phrase searches for “union-closed sets conjecture”,
  “0.38234”, “0.38271”, and 2024--2026 successor papers.
- Justin Gilmer, arXiv:2211.09055.
- Ryan Alweiss, Brice Huang, and Mark Sellke, EJC 31(3) (2024), P3.35,
  DOI 10.37236/12232.
- Zachary Chase and Shachar Lovett, arXiv:2211.11689.
- Lei Yu, *Entropy* 25 (2023), 767, DOI 10.3390/e25050767; full text at
  PubMed Central.
- Jingbo Liu, arXiv:2306.08824.
- Boon Suan Ho, arXiv:2601.19327 (used only as dated evidence of continuing
  work, not as a status authority by itself).
- Bjorn Poonen, *Journal of Combinatorial Theory, Series A* 59 (1992),
  253--268, DOI 10.1016/0097-3165(92)90068-6.
- Jonad Pulaj and Kenan Wood, arXiv:2301.01331v2; related journal DOI
  10.1080/10586458.2024.2410964.
- Bojan Vučković and Miodrag Živković, *The 12-Element Case of Frankl's
  Conjecture*, journal PDF from IPSI Transactions (2017).

## Exact novelty searches

The following quoted searches returned no mathematical source asserting the
candidate values:

- `"FC(4,9)" 20 union-closed`
- `"FC(5,8)" 35 union-closed`
- `"FC(4, 9)" "20" Frankl`
- `"FC(5, 8)" "35" Frankl`

This is only a bounded web/arXiv/publisher search.  It does not exclude
unindexed notes, code output, theses, or private computations.

## Corrections to the source formulation

- “About 0.38” is accurate at the requested precision.  The safest exact
  closed-form theorem is \((3-\sqrt5)/2\); Yu reports 0.38234, and Liu's
  0.382709 evaluation is tied to numerically verified structural hypotheses.
- “Frankl 1979” is an attribution date.  The project has not located an
  original 1979 paper containing the conjecture.

## Recursive-lift priority audit

After deriving the deletion recurrence, the search was repeated with:

- `"FC(4,n)" "1/7" union-closed`
- `"binom{n}{4}" "FC(4" union-closed`
- `union-closed FC family point deletion recurrence FC(k,n)`
- `site:arxiv.org union-closed "FC(4,9)" "20"`
- `site:github.com union-closed "FC(4,9)"`
- `site:arxiv.org union-closed "FC(5,8)" "35"`
- `"floor" "FC(k,n)" union-closed`

No indexed mathematical source stating
\[
 FC(4,n)\le1+\left\lfloor\frac{\binom n4+n}{7}\right\rfloor
\]
or its first consequence \(FC(4,9)\le20\) was located.  Pulaj--Wood's
Theorem 2.7 was re-read as the closest predecessor: it gives the one-shot
ceiling bound and explicitly records \(FC(4,9)\le21\).  Their proof uses the
same underlying averaging principle without iterating the intervening integer
floors.  Accordingly, this project describes the recurrence as a tightening
of that theorem and makes no absolute priority claim.

Exact and phrase searches for a pre-existing fixed-frequency-power no-go
result, including `union-closed sum frequencies squared inequality Frankl`
and `union-closed power set chain weighted frequency Frankl`, did not locate
the construction recorded here.  Because the construction is elementary, it
is treated primarily as an adversarial methodological observation, not as a
standalone priority claim.
