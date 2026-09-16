# Mathematical referee report

**Verdict: accept the exact frozen result-note.** Both likelihood-ratio
inequalities, their stated smallest-mode consequence, the two-step localization,
and the sharpness example pass. The original all-parameter unimodality problem
remains unresolved. No replacement or weakening of the frozen candidate is used.

Referee job: `primary-20260914-hypercomb-unimodality-referee-5c0bdc111bea`.
Review date: 2026-09-14.
Snapshot digest:
`88eded2052b0da0653202aa06009643ec703cf1cda57adeec6e653f6fbc9a446`.
Frozen kind: `result-note`. Frozen original status: `unresolved`.

## Inputs and integrity

I read `source.md`, `problem.md`, `claim.json`, `audit/snapshot.json`, and the
listed proof, code, computation record, source-comparison report, capture record,
primary extracts, and relevant portions of the two listed primary PDFs. The
journal statement was also extracted directly from the frozen PDF, independently
of the supplied text extract; arXiv v5 pages 6--8 were checked directly. I consulted
the cited primary sources online for the literature comparison below.

All 12 frozen file hashes and the canonical snapshot digest were recomputed and
matched. The unchanged `source.md` hash is
`66bd66f1a94163be3cb7f8929629c0f122d7f7490759017615c0d690a842773c`.
No checkpoint, scheduling state, prior referee verdict, or earlier job transcript
was read. No agent or other model worker was started. The review is a fresh
reasoning pass, not a claim of statistical independence or external peer review.

## Scope and identification of the counted objects

The claim concerns every integer n >= 2 and ell >= 3, without a cutoff. Write
s=ell-2 >= 1 and t=ell-1=s+1. The initial factors expand as

    z0 = 1+(t+1)x,
    z1 = (1+tx)((1+sx)(1+tx)+2x)
       = 1+(3ell-2)x+3t^2*x^2+s*t^2*x^3.

These are the auxiliary C0 and the actual C1 of the frozen recurrence. Induction
on n in that recurrence gives Cn=z1*Fn+z0*b*F_(n-1), with the two summands exactly
as submitted. This agrees with the journal's equations (28)--(30). No weak
independent sets, graph case ell=2, or general weighted extension are substituted.

I independently checked the combinatorial interpretation by conditioning on the
occupied attachment vertices. An allowed subset A of positions 0,...,n has no
two consecutive positions. If h(A) is the number of spine edges having neither
endpoint in A, its contribution is

    x^|A| (1+t*x)^(n+1-|A|) (1+s*x)^h(A).

The tooth and spine private choices are independent once A is fixed. Summing
these expressions gives the actual strong independent-set polynomial and is
implemented without the proposed polynomial recurrence in the fresh verifier.
It includes the distinct endpoint attachments when n=1. Each spine edge has
s >= 1 private vertices and each tooth has t >= 2, so degree 2n+1 and the
claimed full support are consistent with the hypergraph definition.

## Reconstruction of the infinite proof

**Order and zero coefficients.** For finite nonzero sequences positive on an
integer interval, P <=_lr Q means p_i*q_j >= p_j*q_i for every i<j after zero
extension. It forces both endpoints of the support of P to be no larger than
the corresponding endpoints of Q. Consequently, in a transitivity test
P <=_lr Q <=_lr R, if p_j*r_i>0 with i<j then q_i and q_j are positive:
the left endpoint of Q is at most i and its right endpoint is at least j.
Multiplying the two relevant inequalities is therefore legitimate. If
p_j*r_i=0, the desired minor is already nonnegative. This verifies the stated
transitivity argument, including disjoint supports.

For a log-concave interval-supported R, its Toeplitz minors satisfy

    r_(i-u)*r_(j-v) >= r_(j-u)*r_(i-v)  (i<j, u<v).

If the right side is positive, all four positions lie in the positive support;
the two positions on the left are between the two extreme positions on the
right and have the same sum. The inequality follows from the decreasing
successive ratios. If the right side is zero it is immediate. Expanding the
convolution minor and pairing (u,v) with (v,u) gives precisely equation (3) of
the submitted proof, with the correct sign and no missing factor. Thus
convolution by R preserves the order. Applying this to P <=_lr xP also proves
product closure of log-concavity. This reasoning is not circular: positivity
of the kernel minors is proved directly before using closure. Linearity in
either argument is valid, and all sums used in the induction have interval
support.

The smallest-mode implication requires no favorable choice among ties. If
i=m(Q)<j=m(P), then p_i<p_j and q_i>=q_j with q_i>0, contradicting the minor
at (i,j). Hence m(P)<=m(Q). This checks the exact convention in `claim.json`.

**Log-concavity inputs.** The factors a, b, z0 and d=a+2x are log-concave with
interval supports; z1=(1+tx)d is therefore log-concave. Independently expanding
(a^2+4yb)/(1+tx) gives the cubic

    R_y = 1+(2s+t+4y)x+(s^2+2st)x^2+s^2*t*x^3.

Its first interior determinant equals

    3s^2+2st+t^2+16sy+8ty+16y^2 > 0.

The second equals s^2*(s^2+2st+3t^2-4ty). It decreases in y; at y=1 and
t=s+1 it is s^2*(6s^2+4s-1)>0. Thus every factor a^2+4yb is log-concave
for the entire required interval 0<=y<=1, including its endpoints.

The submitted Fibonacci factorization has the correct parity and indices:

    Fn = a^(1 if n even else 0)
         product_(j=1)^floor((n-1)/2) (a^2+4b*cos^2(j*pi/n)).

It gives F1=1 and F2=a. Pairing the roots of the standard recurrence solution
establishes the identity. There is no hidden division-by-zero exception: one
may first work at x>0, where a^2+4b>0 and the two characteristic roots differ,
and then extend the polynomial identity identically. Product closure gives
log-concavity of every Fn, and its recurrence gives positivity on [0,2n-2].
The supports of Wn and Yn are therefore [0,2n+1] and [1,2n-1]. F0 is never
used as a nonzero log-concave kernel.

**Simultaneous induction.** The base F1=1 <=_lr F2=a <=_lr b is correct.
The three relevant minors of a versus b are 1, t and t^2. Assume
F_(j-1) <=_lr Fj <=_lr b*F_(j-1). Then

    Fj <=_lr a*Fj,        Fj <=_lr b*F_(j-1),
    a*Fj <=_lr b*Fj,      b*F_(j-1) <=_lr b*Fj.

The first and third comparisons use the log-concave kernel Fj, and the fourth
uses b. Adding upper or lower polynomials as appropriate proves
Fj <=_lr F_(j+1) <=_lr b*Fj. Both induction hypotheses are established together;
neither is assumed from a mode estimate or from the desired conclusion.

**Initial-factor comparisons and conclusion.** For z1 <=_lr x^2*z0 the only
overlap pair needing comparison is (2,3); its determinant is
t^2*(3(t+1)-s)>0. All remaining minors follow from the supports. The minors of
z0 <=_lr d at (0,1), (0,2), (1,2) are respectively s+1, st, (t+1)st.
Multiplying the latter by x(1+tx) gives z0*b <=_lr x*z1. The two valid chains
are then

    Wn <=_lr z1*b*F_(n-1) <=_lr x^2*Yn,
    Yn <=_lr z0*b*Fn      <=_lr x*Wn.

Their kernels are, respectively, z1 and b*F_(n-1), and z0*b and Fn; all have
already been proved log-concave. This includes n=2, where F_(n-1)=1. The
smallest-mode implication and shifts give exactly

    m(Yn)-1 <= m(Wn) <= m(Yn)+2.

Both summands are unimodal. Adding their inequalities proves monotonicity up
to their smaller smallest mode and from their larger smallest mode, whose
distance is at most two. No limit, asymptotic uniformity, or finite enumeration
is being used to prove the all-parameter assertion.

## Independent exact checks

Run from the project directory:

    python3 audit/referee_checks.py

The fresh script uses Python integers and imports no proposer code. It computes
Fn by a binomial tiling expansion, tests its recurrence independently, and checks
every pair of coefficient indices for both invariant inequalities and both final
shifted inequalities. The saved result is `audit/referee-checks.json`.

- All n=2,...,24 and ell=3,...,18, plus n in {25,32,47,64} and ell in
  {3,4,5,31,1000003}: 388 parameter pairs and 958,808 directly tested minors.
- Log-concavity, interval support, smallest modes, and the two monotone tails
  passed in all those cases.
- The attachment-subset count above agreed with Cn=Wn+Yn for all n=1,...,10
  and ell=3,...,8: 60 direct hypergraph comparisons.
- At n=3, ell=5 the exact arrays are

      W = [1,28,320,1937,6744,13632,14976,6912],
      Y = [0,1,16,95,248,240],
      C = [1,29,336,2032,6992,13872,14976,6912].

  The modes of W and Y are uniquely 6 and 4. The total C is log-concave.
  Thus separation two is attained for the specified summands; this example
  does not show any failure of unimodality of C.

These checks are finite corroboration and implementation checks. The proof of
the infinite statement is the argument reviewed above. The proposer's script
and its 1,431-case record were inspected, but were not imported or rerun, and
their counts are not represented as independently reproduced.

## Source comparison and contribution

The nearest journal baseline is Galvin and Sharpe, *Independent set sequence of
some linear hypertrees*, Australasian Journal of Combinatorics 94(1) (2026),
93--121. Theorem 1.7, Corollary 1.8, Note 1.9 and Section 2.5 were checked.
The recurrence, factorization and summand log-concavity are prior results. Their
mode comparison leaves an O(sqrt(n)) interval for each fixed ell; the withdrawn
v3 proof is not a theorem or a counterexample.
[Primary journal PDF](https://academicweb.nd.edu/~dgalvin1/pdf/journal/linear-hyperpaths_J.pdf).
The current arXiv record confirms version 5 dated 30 January 2026.
[Version record](https://arxiv.org/abs/2409.15555).

The overlapping September preprint, *Eventual Strict Log-Concavity of Weighted
Linear Hypercombs*, aiXiv aixiv.260910.000002v1.0, was checked in the actual
primary PDF: equation (1), Theorem 1, Corollary 2 and Section 9. Its recurrence
specializes correctly at s=ell-2,t=ell-1. It asserts eventual strict
log-concavity at fixed positive weights and retains the all-length unweighted
question. It does not supply the submitted all-length shifted likelihood-ratio
comparisons or two-step mode bound. Its analytic proof and claimed Lean
development were not audited here and are not premises of this candidate.
[Primary preprint](https://aixiv.science/pdf/aixiv.260910.000002v1.0.pdf).
An initial direct-open error was resolved by following the primary landing
page's download link.

Fresh searches included hypercomb with likelihood, unimodality and mode;
hypercombs with likelihood ratio; hypercomb with two-step and mode separation;
and Fibonacci with likelihood-ratio and polynomials. The precise title of the
September preprint was searched as well. Most narrower queries returned no
relevant additional source. No equivalent was found in the inspected primary
sources or the relevant returned leads as of the review date. This is a bounded
screen, not a guarantee of worldwide priority; unrelated search hits were not
used as evidence.

The contribution is the simultaneous recurrence order invariant and its
initial-factor application, yielding a universal constant bound for the full
stated uniform family. The elementary order calculus is standard and should
not be presented as newly invented. The application is a substantive
strengthening of the journal mode comparison, not a restatement of its
factorization or a finite toy restriction. It also gives useful information
at lengths not covered by the eventual statement. A credible further use is
to reduce the original unimodality question to excluding a strict valley at
the single intermediate index when the summand modes differ by two.

## Limits and handoff

No substantive gap was found in the frozen partial theorem. The accepted
localization interval is specified by the summand modes; it is not a claimed
constant-width interval around an explicit affine function of n. Sharpness is
only for separation of these summands. Neither the example nor the theorem
resolves full unimodality or all-parameter log-concavity of Cn.

No manuscript or PDF was created in this referee job. The next workflow test is
the runner's `check-math` integrity/provenance gate, followed by drafting at this
accepted scope. That gate is not additional mathematical evidence. Any
substantive revision to the claim or decisive evidence requires a new snapshot
and fresh review.
