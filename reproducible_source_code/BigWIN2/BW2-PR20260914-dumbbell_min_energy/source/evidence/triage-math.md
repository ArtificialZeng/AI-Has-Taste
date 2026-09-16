# Exact triage evidence: a singular minimizer and the stationarity claim

Job: primary-20260914-dumbbell-min-energy-triage-f6149d7dafbe.
These are inspectable mathematical arguments from triage, not independently
refereed results. The original all-odd family remains unresolved.

## 1. Formula and switching check

Expand det(xI-A) by permutations. A nontrivial permutation component is either
an edge transposition (contributing -1, since opposite gains multiply to 1)
or an oriented simple cycle. The two orientations of a graph cycle contribute
-gamma-conjugate(gamma) = -2 Re(gamma). The only simple cycles in D are
C_r and C_s; they are disjoint. Summing the remaining transpositions gives
exactly the four matching-polynomial terms in problem.md, including the
+4ab term on the remaining path P_(ell-1). This also proves spectral
dependence only on the two real parts. Tree switching and lifting the two
cycle products give the stated equivalence of optimization problems.

The script independently constructs Hermitian matrices with rational complex
unit gains and counts graph matchings by vertex deletion. Four exact matrix
characteristic-polynomial comparisons pass, including cycle lengths in both
odd residue classes modulo 4 and connectors of lengths 1 and 3. This finite
check supplements the determinant proof, not a substitute for it.

## 2. The zero-eigenvalue locus for the full all-odd family

D has exactly one perfect matching: each odd cycle forces its designated
vertex to be matched along the connector. The connector then has its unique
alternating perfect matching, and each remaining even path from a cycle has
its unique perfect matching. D-C_r and D-C_s have odd orders, so their
matching polynomials vanish at zero. The even path P_(ell-1) also has one
perfect matching. Consequently, with N=r+s+ell-1,

P_(a,b)(0) = (-1)^(N/2) + 4ab (-1)^((ell-1)/2)
           = (-1)^(N/2) (1-4 alpha beta).

Thus zero eigenvalues occur exactly on alpha beta=1/4. This is a direct
structural consequence, with no novelty claim. Twenty-seven exact matching
checks, r,s in {3,5,7} and ell in {1,3,5}, also verify the identity.

## 3. Complete D_(3,3,1) minimization as a discriminating test

Here alpha=a and beta=b. Direct matching enumeration gives

P_(a,b)(x)=x^6-7x^4+11x^2-1-2(a+b)(x^3-3x)+4ab.

For the Coulson kernel write, with t>0,

Z=1+7t^2+11t^4+t^6, X=Y=2t^3(1+3t^2), W=4t^6,
K=(Z-abW)^2+X^2(a+b)^2,
E(a,b)=(1/pi) integral_0^infinity log(K)/t^2 dt.

For ab<=0 and (a,b)!=(0,0), K>Z^2: expand the difference and use
ZW-X^2=4t^8(1+t^2)^2>0. For ab>0 set c=sqrt(ab). Then

K(t;a,b)-K(t;c,c)=X^2(a-b)^2.

The energy is unchanged by simultaneous negation. Hence every nonzero
minimizer must be on the same-sign diagonal, including the boundary, and
the problem reduces to c in [0,1]. These kernel reductions are elementary
consequences of the source's existing Lemma 4.5 and Theorem 4.6, not new
contributions by themselves.

On that diagonal an exact factorization is

P_(c,c)(x)=F_+(x,c) F_-(x,c),
F_+(x,c)=x^3-x^2-3x+1-2c,
F_-(x,c)=x^3+x^2-3x-1-2c.

All roots are real, since their product is the characteristic polynomial of
a Hermitian gain matrix. Put h(z)=z^3+z^2-3z, strictly increasing for z>=1.
For 0<=c<1/2 let -U be the negative root of F_+ and v the positive root of
F_-. Each satisfies U,v>1 and

h(U)=1-2c, h(v)=1+2c.

F_+ has two positive roots and one negative root; F_- has two negative
roots and one positive root. These sign counts follow from the constant
terms, the traces (+1,-1), and real-rootedness. Therefore

E(c,c)=2+2(U+v),
dE(c,c)/dc=4(1/h'(v)-1/h'(U))<0 for 0<c<1/2,

because v>U>1 and h' is strictly increasing there. The extreme roots are
simple since h'>0. At c=1/2 continuity gives the same limiting formula.

For 1/2<c<=1, both cubics have exactly one positive root, respectively
w>2 and v>1. For F_+, three positive roots are excluded by its negative
pairwise-root sum -3; F_- cannot have three positive roots since its trace
is -1. Thus E(c,c)=2(w+v). Implicit differentiation gives

w'=2/(3w^2-2w-3)>0, v'=2/(3v^2+2v-3)>0.

The energy is strictly increasing on this interval. Hence its global minimum
over the full square is attained exactly at

(a,b)=(1/2,1/2) and (-1/2,-1/2),

and equals 2+sqrt(13)+sqrt(5). At the positive point,

P=x(x+2)(x^2-x-3)(x^2-x-1).

There are four lifts of each real-part pair to oriented cycle-gain switching
classes (eight total on a fixed labelled graph). Only this one graph is
classified here. The displayed minimum value and its strict improvement
over E(0,0) are already source Proposition 4.9; the proof of global minimality
is what makes it a valid test of the source's minimizer stationarity claim.

The script reproduces Proposition 4.9's root isolation exactly: the three
positive roots of y^3-7y^2+11y-1 have the cited rational isolating intervals.
Rational square comparisons imply E(0,0)>7.92477719 and
2+sqrt(13)+sqrt(5)<7.841619254. No floating comparison is used as a proof.

## 4. Exact failure of the unqualified stationarity equations

Source Theorem 4.7, printed pp.13-14, equation (117), asserts zero values
for two integrals at every interior minimizer. At the proven D_(3,3,1)
minimizer a=b=1/2, its notation gives

A=Z-W/4=1+7t^2+11t^4, B=X, C=A^2+B^2,
-bWA+XB=2t^6(1+5t^2+7t^4)>0.

The other numerator is identical. Thus both integrals in (117) are strictly
positive, not zero. They converge: after division by t^2 C the integrands
are O(t^4) at zero and O(t^-2) at infinity. Equation (119) fails as well.
The diagonal conclusion does survive by the preceding kernel inequality.

Explicit one-sided derivatives of the diagonal energy at c=1/2 further
locate the defect. Set U=(sqrt(13)-1)/2, v=(1+sqrt(5))/2,
w=(1+sqrt(13))/2. The left and right derivatives are respectively

L=4(1/(5v)-1/(6-U))<0,
R=4(1/(6+w)+1/(5v))>0,
R-L=4/3.

The simple zero eigenvalue crosses with derivative -2/3 in c; its absolute
value causes the cusp. Polynomial dependence of K on parameters does not
justify interchanging differentiation with this improper integral at the
singular minimizer. This is an exact subsidiary counterexample to (117),
not a disproof or resolution of the original classification problem.

## Next discriminating test

Derive a uniform replacement for Theorem 4.7 on alpha beta=1/4: prove the
zero eigenvalue is simple in the interior, isolate its absolute-value term,
and obtain necessary directional optimality conditions for arbitrary all-odd
triples. Require those conditions to recover the D_(3,3,1) cusp exactly.
This could support a meaningful correction with equality analysis; neither
publishability nor novelty is certified by the present triage.
