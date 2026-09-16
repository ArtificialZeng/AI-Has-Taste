# Full-scope proof proposed for fresh review

Job: newwin-00001-p08-research-23519ac79811. Date: 2026-09-12.
Status: researcher argument; no independent referee acceptance is asserted.
The immutable statement is in source.md and its precise reading is in problem.md.

## Statement

For integers m>=2, n>=1 and 1<=k<=n, count the words with mn letters N and
n letters E, all prefixes satisfying #N>=m#E, by their consecutive NE and
NNE factors as in source.md. Then

    W^(m)_(n,k)(t)
      = C(n,k)/n * sum_(j=1)^k C(k,j) C(mn-k,j-1) t^j.       (1)

In particular the polynomial has degree k, has a simple zero at 0, and
has k-1 distinct strictly negative zeros. Thus it satisfies the entire
original real-rootedness assertion, with no change of orientation or statistic.

## 1. Unique excursion decomposition

Give N height increment +1 and E increment -m. Every nonempty valid word
has a first return to height 0, necessarily by an E from height m.
Before that E, for each i=0,...,m-1, mark the last N from height i to i+1.
Such a step exists since the path starts at 0 and reaches m, and an upward
crossing of an integer height can only use N. These marked steps occur in
increasing order of i: after the last departure from i, the path must still
reach height m, and hence must subsequently depart from each larger i.
This yields

    D = N P1 N P2 ... N Pm E P_(m+1).                       (2)

For i<m, Pi begins and ends at height i, between the departure from i-1
and that from i. It cannot visit a height below i: to return to i would
then require another departure from i-1, contradicting the marked step's
being last. The same argument applies to Pm, which starts and ends at m
before the distinguished E. The suffix P_(m+1) starts and ends at 0 and
stays nonnegative. Translating each starting height to 0 therefore makes
every Pi a valid excursion. Empty components are allowed.

Conversely, any ordered tuple of m+1 such excursions, inserted in (2),
gives a valid word. Before the displayed E its height is at least 1, so
this E is its first return. No component after the displayed N from i to
i+1 falls to i, and later displayed levels are larger; thus the marked
departures are exactly recovered. This proves both uniqueness and the inverse.

Every nonempty excursion starts with at least m north steps: before its
first E it must accumulate height at least m. It ends in E, since a final
N would require height -1 immediately beforehand. In particular, for m>=2
it starts NN.

## 2. Exhaustive audit of factor boundaries

Every counted factor ends at an E. If this E belongs to a component Pi,
its preceding one or two letters are within that component: even its first
E is preceded there by at least two N's. Therefore all such NE and NNE
occurrences have already been counted internally. Only the displayed E in
(2) can contribute a new factor.

* If Pm is nonempty, it ends E. The displayed E contributes neither factor.
* If Pm is empty and P_(m-1) is nonempty, the last two letters before the
  displayed E are EN. It contributes one NE and no NNE.
* If Pm and P_(m-1) are empty, those last two letters are NN. It contributes
  one NE and one NNE.

This includes m=2, where the last case leaves only P3 unrestricted. It
does not extend to m=1: a nonempty component may then begin NE, and a new
NNE occurrence can cross its beginning. No m=1 substitution is used.

Let F=1+sum_D z^(#E(D)) u^(pk(D)) t^(nne(D)), summing nonempty words of
all sizes in addition to the empty word. The three cases contribute,
respectively, z F^m(F-1), zu F^(m-1)(F-1), and zut F^(m-1). Hence

    F = 1 + z F^(m-1) [F(F-1)+u(F-1)+ut].                  (3)

The z records the distinguished E. The remaining E's are counted by the
components, so this is the intended size parameter, not the total word length.

## 3. Formal coefficient extraction

Set Y=F-1. It is the unique formal series with zero constant term solving

    Y = z phi(Y),
    phi(v)=(1+v)^(m-1)[v(1+v)+u(v+t)].

Formal Lagrange inversion gives [z^n]Y=(1/n)[v^(n-1)]phi(v)^n.
It may be applied in Q(u,t)[[z]], where phi(0)=ut is invertible; uniqueness
and the recursion show all coefficients actually lie in Q[u,t]. Thus no
analytic convergence or specialization to u=t=0 is required.

Extracting u^k selects exactly k of the n factors u(v+t), giving

    [z^n u^k]Y
      = C(n,k)/n * [v^(n-1)]
          (1+v)^((m-1)n) v^(n-k)(1+v)^(n-k)(v+t)^k
      = C(n,k)/n * [v^(k-1)](1+v)^(mn-k)(v+t)^k.

The t^j coefficient of (v+t)^k is C(k,j)v^(k-j). The remaining v exponent
is j-1. The j=0 term vanishes and j=1,...,k give (1). The inequalities

    mn-k >= k >= 1

ensure that all coefficients displayed in (1) are positive. In particular
[t]W=C(n-1,k-1)>0, and its leading coefficient is positive. For n=k=1,
(1) gives W=t, as required by the single word N^m E.

As consistency checks derived from (1), Vandermonde gives

    W^(m)_(n,k)(1)=C(n,k) C(mn,k-1)/n,

and summing over k gives C((m+1)n,n)/(mn+1). These checks are consequences,
not substitutes for the coefficient proof.

## 4. Reduction to the ordinary theorem

Write V_(r,k) for the ordinary Dyck polynomial with NE peaks and NNE
factors. Wang--Zhang, arXiv:2309.05903v1, Theorems 1.1 and 1.2, reproduce
the ordinary coefficient formula and real-rootedness theorem due to Bóna
et al. The source is copied verbatim to
evidence/external/wang-zhang-2309.05903v1.html. Its ordinary U,D words
translate to our N,E letters when m=1, without reversing factors.

For r=mn+1, one has r>=2k+1, so their nonexceptional formula gives

    V_(mn+1,k)(t)
      = C(mn+1,k-1)/k * sum_(j=1)^k C(k,j)C(mn-k,j-1)t^j.

Comparison with (1), using (k/n)C(n,k)=C(n-1,k-1), proves

    W^(m)_(n,k)(t)
      = C(n-1,k-1)/C(mn+1,k-1) * V_(mn+1,k)(t).             (4)

The scalar is strictly positive for the full stated range. Real-rootedness
therefore follows from the cited ordinary theorem. This use of the known
theorem is correctly attributed; the proposed contribution is the Fuss
enumeration and the resulting resolution, not a new ordinary theorem.

## 5. A self-contained root argument, also proving simplicity

This is a second justification of the root step in Section 4. Put
d=k-1, A=mn-k, and b=A-d=mn-2k+1>=1. Define the degree-d polynomial

    J(x)=sum_(l=0)^d C(d+1,d-l) C(d+b,l)
                       ((x-1)/2)^l ((x+1)/2)^(d-l).

It is the Jacobi polynomial P_d^(1,b). Its positive leading coefficient
is apparent from this sum, so it has degree exactly d. The product rule
proves the Rodrigues identity

    J(x)=(-1)^d/[2^d d! (1-x)(1+x)^b]
           * (d/dx)^d [(1-x)^(d+1)(1+x)^(d+b)].             (5)

For explicit verification, differentiate the first factor d-l times and
the second l times. After division the resulting term is

    2^(-d) (-1)^l C(d+1,d-l) C(d+b,l)
                         (1-x)^l(1+x)^(d-l),

which is the l-th term above. This also shows cancellation of the
denominator in (5), with no singularities in the polynomial J.

For any polynomial q of degree below d, integrate (5) against
q(x)(1-x)(1+x)^b over [-1,1] and integrate by parts d times. Every boundary
term vanishes: derivatives of order at most d-1 of
(1-x)^(d+1)(1+x)^(d+b) vanish at both endpoints. The resulting integral
contains q^(d)=0. Thus J is orthogonal to every lower-degree polynomial
for the strictly positive weight (1-x)(1+x)^b on (-1,1).

For completeness, let x_1,...,x_s be all distinct roots of J in (-1,1)
where J changes sign. If s<d, the polynomial q=product_i(x-x_i) has degree
below d and Jq has one nonzero constant sign on that interval apart from
its finitely many zeros. Its weighted integral is therefore nonzero,
contradicting orthogonality. Consequently s>=d. Since deg J=d, all its
roots are distinct and lie in (-1,1). The d=0 case is J=1.

The defining sum for J gives the polynomial identity

    (1-t)^d J((1+t)/(1-t))
      = sum_(l=0)^d C(k,l+1) C(A,l)t^l
      = (1/t) sum_(j=1)^k C(k,j)C(A,j-1)t^j.               (6)

The identity is initially a rational substitution for t!=1, with all
denominators canceled, so it is a polynomial identity. Its value at t=1
is a sum of positive coefficients, hence is nonzero. Each root x_i of J
maps to t_i=(x_i-1)/(x_i+1) in (-infinity,0). The map is injective, and
these d roots exhaust the degree-d polynomial in (6). Its constant term
is k>0. Multiplication by t and the positive scalar C(n,k)/n proves the
simple zero at 0 and the k-1 distinct strictly negative zeros asserted.

## Dependencies, contribution, and gaps

The counting proof uses finite word decompositions, binomial expansion,
and formal Lagrange inversion. The root proof may use either the explicitly
cited ordinary theorem or the elementary Rodrigues/orthogonality argument.
No computations are logically required by these arguments. The numerical
checks in the accompanying exact-integer script are finite corroboration.

No mathematical gap is known to this researcher. A fresh referee must
still assess all steps, especially the last-departure inverse, factors
crossing component boundaries, and the parameters in (6). Primary-source
comparison and search limits are documented separately; priority is not
claimed beyond the sources actually checked. This is not an acceptance
report and no research manuscript or PDF is produced in this phase.
