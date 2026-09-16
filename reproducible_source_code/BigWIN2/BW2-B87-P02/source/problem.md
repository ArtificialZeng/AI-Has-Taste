# Precise interpreted problem

## Ambient objects and equivalence

Let $p\ge 11$ be prime and let

\[
3\le \ell\le (p-3)/2
\]

be an integer (equivalently, $2\ell\le p-3$). All displayed elements and
set operations below are in the prime field $\mathbb F_p=\mathbb Z/p\mathbb
Z$. For subsets $A,B\subseteq\mathbb F_p$, define the asymmetric
restricted sumset

\[
A\mathbin{\dotplus}B=\{x+y:x\in A,\ y\in B,\ x\ne y\}.
\]

The pair $(A,B)$ is ordered: interchanging $A$ and $B$ is not part of the
equivalence.  Two ordered pairs are *simultaneously affinely equivalent* when
there are $u\in\mathbb F_p^\times$ and $v\in\mathbb F_p$ such that

\[
(A',B')=(uA+v,uB+v).
\]

Under this action the restricted sumset is sent to
$u(A\mathbin{\dotplus}B)+2v$.

## Claim to prove or refute

Classify every ordered pair $(A,B)$ satisfying

\[
|B|=\ell,\qquad |A|=p-\ell,\qquad
|A\mathbin{\dotplus}B|=p-2.
\]

Writing $C=\mathbb F_p\setminus A$, the proposed classification is as
follows. For every pair of nonnegative integers $a,b$ with $a+b=\ell$,
put

\[
\begin{aligned}
B_{a,b}&=\{-2j:0\le j<a\}\ \cup\
          \{1+2j:0\le j<b\},\\
C_{a,b}&=\{2+2j:0\le j<a\}\ \cup\
          \{-1-2j:0\le j<b\},\\
A_{a,b}&=\mathbb F_p\setminus C_{a,b}.
\end{aligned}
\]

An index range with upper endpoint below its lower endpoint is empty.  The
integer expressions in these sets are reduced modulo $p$.

The assertion has three quantified parts:

1. Every pair $(A,B)$ satisfying the three cardinality conditions is
   simultaneously affinely equivalent to $(A_{a,b},B_{a,b})$ for some
   $a,b\ge0$ with $a+b=\ell$.
2. Two displayed representatives are affinely equivalent exactly when their
   parameters agree up to $(a,b)\leftrightarrow(b,a)$. Thus the number of
   affine classes is $\lfloor\ell/2\rfloor+1$.
3. Conversely, every displayed pair has the required sizes and restricted
   sumset of size $p-2$; in the displayed normalization its two missing sums
   are exactly $0$ and $2$.

For a normalized pair whose missing sums are $\{0,2\}$, the necessary
missing-sum constraint to be used (and proved) is

\[
U(B):=((-B)\setminus\{0\})\cup((2-B)\setminus\{1\})
\subseteq C.
\]

Normalization itself must be justified for an unordered two-element missing
set. After normalization, the only simultaneous affine maps preserving the
set of missing sums $\{0,2\}$ are the identity and $z\mapsto1-z$; the latter
corresponds to swapping $a$ and $b$. The universal argument must also
prove the step-two cyclic run count, both exceptional endpoint corrections,
absence of unintended modular wrap-around in $2\ell\le p-3$, the converse,
and uniqueness.  Integer order or maximum/minimum arguments are not valid in
$\mathbb F_p$ without a separate rectification argument.

No assertion is made for composite moduli, $p<11$, $\ell<3$,
$2\ell>p-3$, unordered pairs, or critical pairs with different cardinalities.

## Nearest located prior work and source status

The nearest primary source is Jiantao Li and Xinyi Liang,
*A Counterexample to a Conjecture of Liu and Qian and a Refined Inverse
Theorem for Restricted Sumsets in* $\mathbb Z_p$, arXiv:2609.10148v1
(submitted 2026-09-09), inspected 2026-09-11.  Its Theorems 1.1--1.2 on PDF
pp. 1--2 state the lower bound and Liu--Qian arithmetic-progression case;
Example 2.1 on pp. 2--3 gives one $p=11,\ell=3$ boundary counterexample; and
Theorem 3.1 on p. 3 treats only $|A|+|B|\le p-1$. It says the general
asymmetric inverse problem remains open, but it does not state the present
all-parameter boundary classification.

Peidong Liu and Guoyou Qian, *On the critical pairs of restricted sumsets in
Z/pZ*, Finite Fields and Their Applications 116 (2026), 102867,
doi:10.1016/j.ffa.2026.102867, is the other nearest work.  Its publisher page
and indexed text were inspected 2026-09-11 and state a classification when at
least one set is an arithmetic progression and Conjecture 1.7 for the general
case.  Full-text retrieval was blocked by the publisher (HTTP 403/closed
access), so overlap and novelty remain unverified.  Accordingly the source
status for this exact classification is **new-question / status-uncertain**,
not a literature-certified open problem.
