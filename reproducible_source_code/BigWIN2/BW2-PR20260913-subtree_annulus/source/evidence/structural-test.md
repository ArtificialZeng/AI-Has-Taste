# Bounded structural test

Job: primary-20260913-subtree-annulus-triage-1ad02ce248b4.
Status: exact algebra and a proposed analytic proof; no independent referee.

## A failed specific invariant

The proposed rooted bound |1+Phi_{T,v}(z)|<=1 throughout
D={z:|z+1/2|<1/2} is false. For the centre v of K_{1,3},
L=Phi_{T,v}(z)=z(1+z)^3. At z=-1/2+49i/100,

    |z+1/2|^2 = 2401/10000 < 1/4,
    L = -485199/100000000 - 240149i/1000000,
    |1+L|^2 = 10479911040079601/10000000000000000 > 1.

This exact rational witness rejects that particular auxiliary bound. It is
neither a subtree zero nor a counterexample to the original annulus, and it
does not obstruct every possible rooted invariant.

## Double-star formula and inner circle

Let D(a,b) have adjacent centres and a,b>=1 pendant leaves; q=a+b and n=q+2.
Partition connected subsets into single leaves, those containing exactly one
centre, and those containing both. This gives

    Q(z)=Phi_D(z)/z=q+w^a+w^b+z w^q,  w=1+z.

If |z+1/2|<1/2 then |z|<1 and |w|<1. For q>=3,
|w^a+w^b+z w^q|<3<=q, proving Q(z) is nonzero there.
For q=2 one has D(1,1)=P_4 and
Q=4+3z+2z^2+z^3. The transform H from problem.md is
4x^3+9x^2+8x+2. Its Hurwitz determinants are 9, 64, 128,
all positive (leading coefficient 4), so its roots have Re x<0.
Thus this argument excludes even the inner boundary for nonzero P_4 roots;
only open-disk exclusion is required in the general family argument.

## Outer-circle domination: proposed uniform proof

Put c=(q+1)^(1/(q+1))>1 and K=2c^2+2c+1. On
|z+1/2|=c+1/2, set t=|w|. Elementary geometry gives

    c<=t<=c+1,  |z|=sqrt(K-t^2)>0.

Since t>1, convexity of a -> t^a+t^(q-a) for 1<=a<=q-1 gives
t^a+t^b<=t+t^(q-1). Consequently the ratio of the error term
w^a+w^b+q to the main term z w^q is at most

    F(t)=[t^(1-q)+t^(-1)+q t^(-q)] / sqrt(K-t^2).

For each integer k>=1, f_k(t)=t^(-k)/sqrt(K-t^2) is convex on
[c,c+1]:

    (log f_k)'' = k/t^2 + (K+t^2)/(K-t^2)^2 > 0,

and f_k''=f_k[((log f_k)')^2+(log f_k)'']>0.
Thus F=f_{q-1}+f_1+q f_q is convex, and its maximum occurs at an
endpoint. Moreover

    f_k(c+1)/f_k(c) = [c/(c+1)]^(k-1) <= 1,

so F(t)<=F(c). The remaining margin is explicit, using c^(q+1)=q+1:

    1-F(c)
      = [(c+1)c^q-c-c^(q-1)-q]/[(c+1)c^q]
      = (c-1)(q+1-c^2) / [c(c+1)(q+1)] > 0.

The last strict inequality holds for q>=2, since 2/(q+1)<1.
Therefore |w^a+w^b+q|<|z w^q| on the entire shifted outer circle.
Rouche would give q+1 zeros of Q inside: the comparison polynomial
z(z+1)^q has exactly q+1 zeros there, and Q has degree q+1.
The remaining zero of Phi_D is z=0, also inside that circle. Hence this
derivation gives strict outer containment for all genuine double stars.
Every domain, root count, and strict inequality must be checked before
promoting this partial argument to a candidate.

The saved floating screen tested only q in {2,3,4,5,6,8,12,20,40,80,160},
a=1,...,floor(q/2), and 2001 boundary angles in [0,pi]. All sampled
normalized domination gaps were positive, with the smallest anglewise gap
at a=1, theta=pi. These samples suggested the endpoint proof; they do not
certify any continuum or any other parameter values. No tree census was run.

Next discriminator: independently check this uniform scalar domination and
the resulting all-double-star annulus, including denominator positivity,
P_4's inner case, and the exact endpoint factorization; reject or repair the
family claim if any step fails. A targeted literature/value check is still
needed before a result-note candidate is justified.
