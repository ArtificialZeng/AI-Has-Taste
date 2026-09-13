# Preliminary novelty audit: two exact positivity islands

Date: 2026-08-23

## Scope and status

This is a focused, preliminary literature audit for the proposed short paper
tentatively titled *Two exact positivity islands for a complex Hermitian
rank-two scalar gate arising in a common-metric problem*.  It is not evidence
that the full fixed-crossing-lens constant has been determined, and it is not
a claim of priority.  The safe novelty wording at this stage is:

> We give two explicit, independently checkable positivity families for a
> scalar gate that arises in one common-metric reduction of the fixed-lens
> problem.

The focused search did not locate the two exact parameter families or their
certificate architecture in the sources below.  Absence from this search is
not proof that no equivalent result exists.

## Claim-level findings

### N01 — The individual crossing-lens optimum remains open

**Status: directly verified in a current primary source.**

Shanmu Jin's version 4 preprint, Section 7.6, explicitly lists the optimal
constant for an individual crossing lens among the open problems.  The same
preprint's Corollary 6 gives the uniform constant two for all pairs of
spherical disks; these are different quantifiers.

- Shanmu Jin, *The Numerical Range Is a 2-Spectral Set*, v4, Section 7.6:
  <https://www.preprints.org/manuscript/202607.1919>

The classical lenticular paper establishes a lens-shaped von Neumann
inequality framework and is essential background, but its existence does not
identify the unrestricted optimum for each fixed crossing lens.

- Bernhard Beckermann and Michel Crouzeix, *A lenticular version of a von
  Neumann inequality*, Archiv der Mathematik 86 (2006), 352--355,
  DOI 10.1007/s00013-005-1533-5:
  <https://doi.org/10.1007/s00013-005-1533-5>
- Author manuscript:
  <https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/bernhard_beckermann/abs/becrv4.pdf>

### N02 — The universal constant two does not settle the fixed-lens optimum

**Status: verified; manuscript wording must keep the quantifiers separate.**

Lorist and Schwenninger announced a proof of the universal Crouzeix constant
two.  Jin's Corollary 6 likewise states the least constant valid uniformly over
all pairs of spherical disks is two.  Neither statement supplies the optimal
constant for every individual crossing lens; Jin explicitly separates that
question in Section 7.6.

- Emiel Lorist and Felix Schwenninger, *A solution to Crouzeix's conjecture*,
  arXiv:2608.03841 (2026): <https://arxiv.org/abs/2608.03841>
- Shanmu Jin, *The Numerical Range Is a 2-Spectral Set*, v4, Corollary 6 and
  Section 7.6: <https://www.preprints.org/manuscript/202607.1919>

### N03 — General intersections-of-disks bounds are established background

**Status: verified.**

Badea, Beckermann and Crouzeix prove that an intersection of `n` spherical
disks that are spectral sets for an operator is a complete `K`-spectral set
with `K <= n + n(n-1)/sqrt(3)`.  This supports the general spectral-set
background, not the new local common-metric positivity families.

- Catalin Badea, Bernhard Beckermann and Michel Crouzeix, *Intersections of
  several disks of the Riemann sphere as K-spectral sets*, Communications on
  Pure and Applied Analysis 8 (2009), 37--54,
  DOI 10.3934/cpaa.2009.8.37:
  <https://doi.org/10.3934/cpaa.2009.8.37>
- Preprint: <https://arxiv.org/abs/0807.3136>

### N04 — Related common-quadratic-metric criteria already exist

**Status: verified as adjacent literature; no exact duplicate located.**

King and Nathanson treat real Hurwitz matrices whose difference has rank one,
proving a common quadratic Lyapunov function criterion in terms of the product
having no negative real eigenvalue.  This is mathematically adjacent to a
common-metric problem, but it is not the same Hermitian interval gate, complex
rank-two compression, or polynomial family used here.  The proposed paper
must not imply that common quadratic metrics themselves are new.

- Christopher King and Michael Nathanson, *On the existence of a common
  quadratic Lyapunov function for a rank one difference*, Linear Algebra and
  its Applications 419 (2006), 400--416,
  DOI 10.1016/j.laa.2006.05.010:
  <https://doi.org/10.1016/j.laa.2006.05.010>
- Preprint: <https://arxiv.org/abs/math/0403467>

### N05 — Bernstein certificates are an established exact method

**Status: verified.**

Exact sign certification through Bernstein coefficients and de Casteljau
subdivision is established prior methodology.  Accordingly, the paper may
claim an explicit exact certificate and reproducible implementation, but not
novelty of the Bernstein technique itself.

- Yves Bertot, Frederique Guilhot and Assia Mahboubi, *A formal study of
  Bernstein coefficients and polynomials*, Mathematical Structures in
  Computer Science 21 (2011), 731--761,
  DOI 10.1017/S0960129511000090:
  <https://doi.org/10.1017/S0960129511000090>

### N06 — Exact scale-cubic and moving-sheet families

**Status: novelty candidates, not priority claims.**

The focused searches used combinations of the following concepts: fixed
crossing lens, common metric, complex Hermitian rank-two gate, scale cubic,
compact-ball quartic, moving-sheet parametrization, and Bernstein exact
certificate.  No source located in this pass states either audited family in
the project's parameterization or an evidently equivalent one.

Safe language:

- "We establish the following two explicit positivity families."
- "To our knowledge, these particular exact families have not previously
  been recorded," only after a broader citation audit and with a qualifier.

Unsafe language at the current gate:

- "We solve the fixed-lens problem."
- "This is the first exact common-metric result."
- "The scale-cubic/moving-sheet method is new" without a broader search and
  comparison.

## Consequences for the manuscript

1. Lead with the two local theorem statements, not the original fixed-lens
   conjecture.
2. State that the universal constant two and the individual fixed-domain
   optimum have different quantifiers.
3. Cite the classical lenticular and intersections-of-disks papers for the
   spectral-set context.
4. Cite prior common-quadratic-Lyapunov and Bernstein work as adjacent method
   background.
5. Put a prominent scope paragraph after the main theorems: the results do not
   cover the full compact ball, arbitrary normalized scale, the complete
   common-metric theorem, or the optimal constant for a fixed crossing lens.
6. Treat all novelty wording as provisional until the completed manuscript
   undergoes a claim-by-claim citation audit.

## Audit boundary

This pass verified bibliographic existence and the specific statements listed
above using primary or publisher/author sources.  It did not yet perform a
systematic citation graph search, MathSciNet/Zentralblatt review search, or a
claim-by-claim two-pass audit of the finished manuscript.  Those remain release
gates.
