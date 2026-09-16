# A conditional reduction to an odd-degree root statement

Job: primary-20260914-vishnyakova-shifts-research-77f35a690f9a.
This is a proved conditional argument and an explicitly unproved auxiliary
hypothesis. It does not claim equivalence to, or resolution of, the original
conjecture. The original even-degree TP problem remains unchanged.

## Auxiliary hypothesis O

Put b=1-1/sqrt(2). For every odd m>=1 and every -b<t<0, let O assert that
Q_(m,t) has exactly m-1 simple roots in (-1,0) and exactly one simple root
in (0,infinity). This assertion is about a real-rooted polynomial with one
positive root; it does not assert TP of the odd-degree sequence.

A weaker hypothesis sufficient below requires this root configuration only
for m=n-1 at parameters where Q_(n,t) is admissible and has a multiple root.
We do not claim either version follows from known TP multiplication closure.

## Conditional collision lemma

Let n>=4 be even and -1<t<0. Suppose g=Q_(n-1,t) has simple roots

    -1 < beta_1 < ... < beta_(n-2) < 0 < lambda.

If f=Q_(n,t) is admissible and has a multiple root, then it has exactly one
double root r, all its other roots are simple and smaller than r, and

    beta_(n-2) < r < 0,
    partial_z^2 f(r)>0,   partial_t Q_(n,t)(r)=n g(r)<0.

In particular its splitting coefficient is strictly positive; no triple
root or simultaneous second collision is possible.

**Proof.** Set a(z)=z(1+z), and, away from the roots of g, write the recurrence as

    f(z)/(a(z)g(z)) = H(z)
      = sum_(j=1)^(n-2) 1/(z-beta_j) + 1/(z-lambda)
        + t/z + (1-t)/(1+z).

For -1<z<beta_(n-2), excluding its poles,

    H'(z) = -sum_j 1/(z-beta_j)^2 -1/(z-lambda)^2
            -t/z^2 -(1-t)/(1+z)^2 < 0.

Indeed |z-beta_(n-2)|<|z|, and -t<1, so the term from the largest beta
strictly dominates the sole positive term -t/z^2. Every other term is
negative. On each of (-1,beta_1) and (beta_j,beta_(j+1)), H decreases from
positive infinity to negative infinity, since both endpoint pole residues
are positive. Thus these n-2 intervals each contain exactly one simple root
of f. No beta_j is a root of f, because f(beta_j)=a(beta_j)g'(beta_j)!=0.

At an admissible multiple root, f cannot vanish at -1 or 0, since its
endpoint values are (t-1)^n and t^n. It cannot have that root in any of the
preceding intervals. Hence any multiple root lies in (beta_(n-2),0).
The n-2 already counted simple roots leave only two degrees, so there can
be exactly one double root r and no further roots. All other roots are to
its left. The positive leading coefficient gives

    f''(r)=2 n! product_(f(gamma)=0, gamma!=r) (r-gamma)>0.

On (beta_(n-2),0), the polynomial g has positive factors from its interior
roots and a negative factor from lambda, so g(r)<0. The parameter identity
partial_t Q_n=n Q_(n-1) completes the proof. The n=2 case is the explicit
quadratic calibration and needs no beta_j. QED.

## Conditional consequence: interval shape, not nesting

Fix even n. Assume O for degree n-1. Then

    M_n = [-c_n,1+c_n] for some 0<c_n<b.

Here is the complete implication. The known [0,1] result, reflection,
quadratic calibration, and multiplication closure give
M_2 subset M_n and [0,1] subset M_n. The necessary minors already proved
in `triage-exact.md` give M_n subset (-b,1+b). The set M_n is closed by
continuity of roots and the fixed nonzero leading coefficient.

For any t in (-b,0) where admissible f has simple roots, all roots are
strictly inside (-1,0), so admissibility is open near t. At any admissible
multiple-root parameter, the conditional lemma proves there is just one
double root and its splitting coefficient is positive. Taylor expansion
(or the local quadratic factor) then gives admissibility immediately to
the right and nonadmissibility immediately to the left; all other simple
roots persist. This excludes an isolated admissible point or a right
endpoint of an admissible component within (-b,0).

For clarity, there are only finitely many possible collision parameters:
the discriminant in t is a polynomial, nonzero at t=1/2 by the known
simple-root result. Together with the constant endpoint evaluations, this
gives finitely many parameter cells and precludes an accumulation issue.
Consequently there can be only one admissible component on (-b,0], namely
[-c_n,0], and c_n>=c_2>0. Compactness and exclusion of -b give c_n<b.
Reflection and the interior [0,1] result give the displayed equality.

This implication proves neither c_n<=c_(n+2) nor O. The full original
conjunction still has both an unresolved auxiliary hypothesis and a
separate successive-nesting issue. The reduction is not called an
equivalence.

## Exact support and an adversarial boundary check

`python3 evidence/odd-strip.py` generates `odd-strip.json`. For m=1,3,5,
O holds on the larger interval [-1/3,0): in degrees 3 and 5 the exact
discriminants have no root in [-1/3,0], and the sample t=-1/3 has m-1
simple roots in (-1,0) and one positive root. The endpoint evaluations
and fixed leading coefficient prevent a change of root location or count
before t=0. Degree 1 is immediate. Since b<1/3, these results cover O's
whole strip in those three degrees.

The hypothesis was suggested by exact exploratory points in odd degrees
through 21 at t=-1/4,-29/100,-1/3. The saved, separately chosen finite
tests use m=23,25,27,29,31 and t=-183/625=-0.2928 and t=-1/100000.
All ten tests satisfy O, with exact Sturm counts and squarefreeness checks.
They are held-out parameter points, not whole-interval or infinite evidence.

The more permissive extension -1/2<t<0 is false: at m=3,t=-49/100, the
discriminant is strictly negative, and there are no roots in (-1,0), with
one positive root and two nonreal roots. The exact polynomial and
discriminant are recorded in the JSON. This counterexample does not affect
O or the original conjecture.

The next research test is to prove or refute O uniformly for odd m>=7;
a putative counterexample must be converted to an exact root-count
certificate at a rational t in (-b,0), or a certified algebraic t.
The logarithmic-derivative proof above shows precisely what such a result
would change: it would settle, or obstruct this route to, interval shape
and one-direction collision crossing. No conjecture-note candidate is
claimed yet; literature scope and an all-degree structural argument remain
incomplete.
