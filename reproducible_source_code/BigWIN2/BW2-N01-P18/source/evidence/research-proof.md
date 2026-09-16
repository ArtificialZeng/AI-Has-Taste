# Proof candidate: recurrence for the fixed degenerate Laurent polynomial

Research job: `newwin-00001-p18-research-8635786e3d2c`, 2026-09-12.
This is the complete mathematical argument submitted for a fresh referee, not
an acceptance report or publication manuscript. The frozen original is
`source.md`; `problem.md` specifies its quantifiers.

## Statement and dependencies

**Theorem.** For every prime $p$, let $K=\mathbb F_p$ and

    P(x)=x^(p-1)+x^(-1),
    u_n(Q)=[x^0](P(x)^n Q(x))   (n>=0),

where $Q\in K[x,x^{-1}]$. The following conditions are equivalent:

1. Every finite contiguous word occurring in $u(Q)$ occurs arbitrarily far out.
2. $u_n(Q)=0$ for every $n\ge0$.
3. $Q=P F(P)$ for some polynomial $F\in K[t]$.

The third condition denotes $P K[P]$, not the Laurent-ring ideal $P K[x,x^{-1}]$.
The theorem includes $p=2$, $Q=0$, negative exponents, and the initial term
$u_0=[x^0]Q$. It settles the original iff assertion and identifies all recurrent
$Q$. It makes no claim for a different $P$, higher prime powers, or the
whole family in Kohen's Question 20.

Dependencies used below are formal power-series arithmetic, the formal residue
substitution identity (justified below in arbitrary characteristic), division
by a monic polynomial, and the pigeonhole principle. No theorem about automatic
sets, density, generalized polynomials, or recurrence is invoked. Finite
computations are supplementary and are not premises of the proof.

## 1. Recurrent words force translated finite sums

For positive integers $t_1,t_2,\ldots$, write

    FS_0(t_i)={sum_{i in I} t_i : I is a finite subset of the positive integers}.

The empty sum is included. Suppose a word $v=(v_n)_{n\ge0}$ is recurrent and
$v_a=c\ne0$. We construct positive integers $t_i$, with each new one larger
than the sum of its predecessors, such that

    v_(a+s)=c for every s in FS_0(t_i).                         (1)

Start with the position $a$. If $t_1,\ldots,t_m$ have been chosen, put
$T_m=\sum_{i=1}^m t_i$, with $T_0=0$. By recurrence the prefix
$v_0\cdots v_{a+T_m}$ occurs at a starting index $t_{m+1}>T_m$.
For every subset sum $s$ of the first $m$ terms, its occurrence copies
$v_{a+s}$ to $v_{a+s+t_{m+1}}$. These, together with the previous subset
sums, give the induction. Every finite subset is covered at a finite stage,
which proves (1). Only unbounded return of prefixes was used.

## 2. A digit-sum set cannot contain such a translate

For $D\ge0$, let $s_p(m)$ be the sum of the base-$p$ digits of the
nonnegative integer $m$, and put

    S_(p,D)={n>=0 : s_p((p-1)n+r)<=D for at least one r in {0,...,D}}.

**Lemma.** For every $a\ge0$ and every infinite sequence of positive integers
$t_i$, the set $a+FS_0(t_i)$ is not contained in $S_{p,D}$.

First observe that, in any tail of the sequence and for any integer $K\ge0$,
some nonempty consecutive finite block has sum divisible by $p^K$. Among
the initial $p^K+1$ partial sums of that tail (including the empty one), two
coincide modulo $p^K$; subtract them. The resulting block sum is positive.

Choose $K_1\ge0$ so that

    p^K_1 > (p-1)a+D.

Choose a block sum $b_1$ divisible by $p^{K_1}$. After choosing $b_i$,
choose $K_{i+1}\ge0$ so that

    p^K_(i+1) > (p-1)b_i,

and choose $b_{i+1}$ divisible by $p^{K_{i+1}}$ using a tail strictly after
the indices used by $b_i$. Do this through $b_{D+1}$. All blocks use
disjoint sets of indices, so their total is a finite subset sum of the $t_i$.

Because $b_i\ge p^{K_i}>0$, the displayed strict inequality implies
$K_{i+1}>K_i$. The nonzero base-$p$ digits of $(p-1)b_i$ occur only at
positions at least $K_i$, and, for $i\le D$, strictly below $K_{i+1}$.
Every $(p-1)a+r$, $0\le r\le D$, has all digits strictly below $K_1$.
Consequently these nonnegative summands have disjoint digit positions and
produce no carries when added. For

    n=a+b_1+...+b_(D+1)

and **each** allowed $r$, we have

    s_p((p-1)n+r)
      =s_p((p-1)a+r)+sum_{i=1}^{D+1}s_p((p-1)b_i)
      >=D+1.

Here every $b_i$ contributes at least one because it is positive. This $n$
belongs to $a+FS_0(t_i)$ and not to $S_{p,D}$, proving the lemma. The
argument includes $D=0$ and all possible offsets simultaneously.

It follows from Section 1 that a recurrent word supported in $S_{p,D}$
must be the zero word.

## 3. The lacunary series and the constant-term map

Define

    a_j=(p^j-1)/(p-1) (j>=1),
    Y(z)=sum_{j>=1} z^(a_j) in K[[z]],
    Phi(Q)=sum_{n>=0} u_n(Q) z^n.

The exponent identity $a_{j+1}=p a_j+1$ and Frobenius give

    Y=z(1+Y^p),       Y=z+O(z^2).                             (2)

The series $f(x)=x/(1+x^p)=x+O(x^2)$ satisfies $f(Y)=z$, so $Y$ is
its compositional inverse and $Y(f(x))=x$.

For completeness, if $f=x+O(x^2)$ over $K$ and $G(z)\in K((z))$, then

    Res_z G(z) dz = Res_x G(f(x)) f'(x) dx.                   (3)

Here $\operatorname{Res}$ extracts the coefficient of exponent $-1$.
One may lift all coefficients of $f$ and $G$ to integers; the linear
coefficient of the lift of $f$ is 1. Over the rationals, (3) follows
term by term: $f^m f'$ is a formal derivative divided by $m+1$ when
$m\ne-1$, hence has zero residue; $f'/f=x^{-1}+h'/h$, where $f=xh$
and $h\in1+x\mathbb Z[[x]]$, has residue 1. Both sides of (3) are integer
expressions involving only finitely many relevant coefficients, so the
identity reduces modulo $p$. Thus (3) does not assume invertibility of
$n$, $r$, or $m+1$ in $K$.

In characteristic $p$, $f'(x)=(1+x^p)^{-1}$. For $r,n\ge0$, (3) now
gives

    [z^n]Y^r
      =Res_z Y(z)^r z^(-n-1) dz
      =Res_x x^r (x/(1+x^p))^(-n-1)/(1+x^p) dx
      =[x^(n-r)](1+x^p)^n
      =[x^0](P(x)^n x^r).

Therefore

    Phi(x^r)=Y^r for every r>=0.                             (4)

This also proves $\Phi(1)=1$, so $[x^0]P^n=0$ for all $n>0$, with
the initial coefficient equal to 1.

## 4. All Laurent polynomials and the exact kernel

Let

    R=K[t,X]/(X^p-tX+1).

Division by the monic polynomial in $X$ makes $R$ a free $K[t]$-module
with basis $1,X,\ldots,X^{p-1}$. In this quotient, $X(t-X^{p-1})=1$.
Consequently the maps

    R -> K[x,x^(-1)]:   X -> x, t -> P;
    K[x,x^(-1)] -> R:   x -> X, x^(-1) -> t-X^(p-1)

are well-defined inverse ring homomorphisms. For the second composition,
$X^{p-1}+X^{-1}=t$; the first composition fixes $x$ and $x^{-1}$.
Thus every Laurent polynomial has a unique expression

    Q=sum_{r=0}^{p-1} f_r(P)x^r,     f_r in K[t].             (5)

The map $\Phi$ is linear; it is not asserted to be multiplicative. Direct
index shifting instead gives

    Phi(PQ)=(Phi(Q)-[x^0]Q)/z.                               (6)

If $\Phi(Q)=H(Y)$ for a polynomial $H\in K[y]$, then
$[x^0]Q=H(0)$, by setting $z=0$. From (2), $1/z=Y^{-1}+Y^{p-1}$ in
$K((z))$, so (6) becomes

    Phi(PQ)=L(H)(Y),
    L(H)(y)=(H(y)-H(0))(y^(-1)+y^(p-1)).                   (7)

This is a polynomial since $y\mid H(y)-H(0)$. It vanishes on constants;
on a nonconstant polynomial of degree $d$ it preserves the leading
coefficient and has degree $d+p-1$. Equations (4), (5), (7), and linearity
show that every $\Phi(Q)$ equals $H(Y)$ for some polynomial $H$.

The vector-space basis arising from (5) consists of $P^k x^r$ for $k\ge0$
and $0\le r\le p-1$. Its members $P^k$, $k\ge1$, map to zero. The
remaining members have polynomial images

    1, and L^k(y^r) for k>=0 and 1<=r<=p-1.

These are monic, with distinct degrees $0$ and $r+k(p-1)$, respectively;
each nonnegative integer occurs exactly once. They are therefore linearly
independent and span $K[y]$, by elimination of the leading term. Finally,
substitution $H\mapsto H(Y)$ is injective: for nonzero $H$, its lowest
nonzero monomial has the same degree and coefficient after $Y=z+O(z^2)$.
It follows that

    Phi(Q)=0  iff  f_r=0 for 1<=r<=p-1 and f_0(0)=0
              iff Q belongs to P K[P].                     (8)

## 5. Support, cancellation, and conclusion

Let $H\ne0$ have degree $D$. If the coefficient of $z^n$ in $H(Y)$
is nonzero, some term $Y^r$ with $0\le r\le D$ has a nonzero coefficient
there. For $r>0$, expanding that product means that at least one ordered
tuple $j_1,\ldots,j_r\ge1$ satisfies

    n=a_(j_1)+...+a_(j_r).

Only finitely many tuples can contribute to a fixed coefficient. Then

    (p-1)n+r=p^(j_1)+...+p^(j_r),
    s_p((p-1)n+r)<=r<=D.                                   (9)

The digit inequality follows by carrying: replacing $p$ units at a digit
position by one at the next lowers the sum by $p-1$. When $r=0$, the
only possible index is $n=0$, and the same containment holds. Coefficient
cancellation can only remove support points. Thus all support of $H(Y)$
is in $S_{p,D}$. Sections 1 and 2 exclude recurrence of its nonzero
coefficient word.

If $u(Q)$ is recurrent, this forces $H=0$, equivalently $u(Q)=0$.
Conversely, the zero word is recurrent. Equation (8) gives the asserted
algebraic classification. This proves all three equivalences.

## Gap list and scope of verification

Known mathematical gaps in this argument: none identified in this research
pass. A separate fresh referee has not yet reviewed it. In particular, the
residue identity, freeness in (5), finite-sums induction, and simultaneous
carry separation are explicit arguments here, not assumptions inherited
from the triage checkpoint.

`check-research.py` and `research-check.json` supplement the proof with exact
finite tests. They cannot certify infinite recurrence or nonrecurrence.
The closest primary-source comparison, including its limits, is recorded in
`literature/research-live-screen.md`. No priority is claimed for the elementary
component lemmas; the proposed contribution is their complete application to
the fixed-$P$, all-$Q$ recurrence problem.
