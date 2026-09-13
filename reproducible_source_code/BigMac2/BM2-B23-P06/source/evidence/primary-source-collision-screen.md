# Primary-source collision screen

Date: 2026-09-09  
Research job: `bigMac-00023-p06-research-9fc8d354b118`

## Frozen source verification

The paper named in `source.md` is locally present at
`literature/2609.03184v1.pdf` (not at the `batches/literature/...` path named
there). Its SHA-256 is

```text
eec197e27fcab9602c1cd8b033dd84a45d4401abcbdbe225db3de9d6afb9acf2
```

which exactly matches the frozen digest in `source.md`. `pdfinfo` reports the
title *On uniquely colorable Cayley graphs*, author Milan Basic (Bašić), eight
pages, and an unencrypted PDF. `pdftotext -layout` was used for the checks
below.

- Section 2, printed p. 2, defines `D_n` as the divisors of `n` strictly less
  than `n`, states that an integral circulant is determined by
  `D subseteq D_n`, denotes it `ICG_n(D)`, and gives the equivalent union of
  gcd classes. This agrees with the reading in `problem.md`.
- Section 5, printed p. 7, distinguishes unitary Cayley graphs from the broader
  integral-circulant class and explicitly says that a full classification of
  perfect integral circulant graphs remains an open problem. It does not state
  or supply a finite census through 64.

## Nearest primary sources and collision assessment

1. W. Klotz and T. Sander, *Some Properties of Unitary Cayley Graphs*,
   Electronic Journal of Combinatorics 14 (2007), R45,
   <https://doi.org/10.37236/963>. Section 3 proves that
   `ICG_n({1})` is perfect exactly when `n` is even or `n` is odd with at most
   two distinct prime divisors. The paper later extends the notation to
   arbitrary divisor sets but proves integrality/eigenvalue formulas there,
   not perfectness for arbitrary `D`. This is a strict subfamily of the frozen
   task.

2. W. So, *Integral circulant graphs*, Discrete Mathematics 306 (2006),
   153--158, <https://doi.org/10.1016/j.disc.2005.11.006>. The paper reports
   computing spectra for all possible integral-circulant symbols on fewer than
   100 vertices. Thus a finite all-symbol generation below 100 is prior work
   and any future contribution must not be described as the first enumeration
   of the underlying ICG inputs. The reported output concerns spectra and
   isospectrality; it gives neither perfectness labels nor odd-hole/antihole or
   positive perfectness certificates, so it is not the requested census.

3. W. Klotz and T. Sander, *GCD-Graphs and NEPS of Complete Graphs*, Ars
   Mathematica Contemporanea 6 (2013), 289--299,
   <https://doi.org/10.26493/1855-3974.309.129>, identifies gcd-graphs with
   NEPS of complete graphs and studies eigenspaces. Searches for a perfectness
   classification of these NEPS found only work on perfect **state transfer**,
   not perfect graphs. The NEPS representation is relevant structure, but the
   cited paper is not a perfectness census.

4. X. Liu and S. Zhou, *Eigenvalues of Cayley Graphs*, Electronic Journal of
   Combinatorics 29(2) (2022), P2.9,
   <https://www.combinatorics.org/ojs/index.php/eljc/article/view/v29i2p9>.
   Its survey section on integral circulants records Klotz--Sander's
   perfectness result only for the unitary graph, then treats general
   `ICG(n,D)` through integrality and Ramanujan-sum eigenvalues. No finite
   general-`D` perfectness table is recorded there. Absence from a survey is
   not a priority proof.

5. J. Minac, T. T. Nguyen, and N. D. Tan, *On the gcd-graphs over polynomial
   rings*, Canadian Journal of Mathematics, published online 2025,
   <https://doi.org/10.4153/S0008414X25101673>. Section 7 advertises and proves
   sufficient conditions for perfectness/non-perfectness over polynomial
   quotient rings and recovers the unitary classification. It is neither a
   classification over `Z/nZ` for arbitrary divisor sets nor a finite census
   through 64.

6. J. Minac, T. T. Nguyen, and N. D. Tan, *A complete classification of
   perfect unitary Cayley graphs*, arXiv:2409.01922 and Galois Journal of
   Algebra 2 (2026), 50--58, classifies the unitary construction over finite
   rings. For `Z/nZ` this again concerns `D={1}`, not arbitrary `D`.

The bounded searches included exact and synonymous combinations of
`perfect integral circulant`, `perfect ICG(n,D)`, `perfect gcd-graph`, `odd
hole`, `odd antihole`, `census`, `n <= 64`, and `perfect NEPS of complete
graphs`, as well as the reference chains of the papers above. No primary source
located in this screen gives an equivalent finite perfectness classification
or census. This is a bounded negative search result, not proof of novelty or
priority.

## Consequence for scope

The literature collision test does not settle the frozen classification and
does not justify a candidate. It narrows the possible increment: a result may
claim only perfectness labels/certificates and a genuine compression of them,
not first enumeration of all ICG symbols. The fastest next falsifier is the
frozen `n<=32` census: cover all 539 pairs, serialize exact odd-hole or
odd-antihole witnesses for every imperfect case, and require a replayable
positive certificate or proved structural cover for every perfect case.
