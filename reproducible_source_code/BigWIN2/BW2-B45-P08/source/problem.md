# Precise reading

## Objects and notation

Let \(V\) be a finite set. A **tournament** \(T=(V,A)\) has, for every
unordered pair \(\{x,y\}\), exactly one of \(x\to y\) and \(y\to x\) in
\(A\). A **linear order** is a strict total order on \(V\), written as a
permutation from earliest to latest. An \(m\)-profile
\(P=(\pi_1,\ldots,\pi_m)\) is an ordered list of \(m\) linear orders;
repetitions are allowed (so it represents a multiset of voters).

For an arc \(x\to y\) of \(T\), put

\[
s_P(x,y)=|\{r:x\text{ precedes }y\text{ in }\pi_r\}|,
\qquad \mu_P(x,y)=2s_P(x,y)-m.
\]

For odd \(m\), \(P\) **induces** \(T\) when \(s_P(x,y)\ge (m+1)/2\) for
every \(x\to y\in A\). Its majority margin on that arc is then the positive
odd integer \(\mu_P(x,y)\). For odd \(m\) and odd \(t\) with \(1\le t\le m\),

\[
I_{m,t}=\{T:\exists P\text{ of size }m\text{ inducing }T
\text{ and }\mu_P(x,y)\le t\text{ for every }x\to y\in A\}.
\]

Membership is a property of an isomorphism class. It is also invariant under
converse/reversal: reverse every voter order to turn a profile for \(T\) into
one for the tournament \(T^{\mathrm{op}}\) with every arc reversed.

## Frozen finite claim

Define

\[
\mathcal F_9=\{[T]: |V(T)|=9,\ T\in I_{3,3}\setminus I_{3,1}\},
\]

where \([T]\) denotes tournament isomorphism class. The cited primary paper
reports exactly 254 such non-isomorphic classes. The question is the universal
finite assertion

\[
\boxed{\mathcal F_9\subseteq I_{5,1}.}
\]

Expanded without class notation, the quantifiers are:

> For every tournament \(T\) on nine vertices, if some three-order profile
> induces \(T\), but no three-order inducing profile has margin \(1\) on every
> arc, then there exist five linear orders of \(V(T)\) such that, for every
> arc \(x\to y\) of \(T\), exactly three of the five orders put \(x\) before
> \(y\).

For \(m=3\), \(I_{3,3}\) is simply the class of 3-inducible tournaments;
failure of \(I_{3,1}\) means that every inducing three-profile has at least one
unanimous \(3{:}0\) arc. For \(m=5\), membership in \(I_{5,1}\) is exactly a
\(3{:}2\) split on all 36 pairs. Membership in \(I_{5,3}\) allows \(3{:}2\)
and \(4{:}1\), but excludes \(5{:}0\).

The phrase “254 isomorphism/reversal classes” in source.md is normalized
here to the paper's count of 254 isomorphism classes. Passing instead to
orbits under isomorphism and converse could reduce the number of
representatives, but cannot change the truth of the universal assertion,
because \(I_{5,1}\) and the boundary family are both converse-invariant.

## Immediate inclusion and logical outcomes

Every \(T\in\mathcal F_9\) is in \(I_{5,3}\): take a three-profile inducing
\(T\) and append a linear order \(\sigma\) and its reverse. On every pair the
new voters contribute one vote in each direction, so the old margin is
unchanged. Hence old \(2{:}1\) and \(3{:}0\) arcs become respectively
\(3{:}2\) and \(4{:}1\).

Thus one class \(T\in\mathcal F_9\setminus I_{5,1}\) would disprove the boxed
claim and prove \(I_{5,1}\subsetneq I_{5,3}\). A verified \(I_{5,1}\) profile
for every one of the 254 classes would prove the boxed claim only; it would
not prove equality of the global layers, nor is it a lower bound for \(N(5)\),
which concerns non-5-inducibility.

## Certificate scope

For a positive census, retain the canonical adjacency data and five explicit
permutations for every class, and independently recount all 36 pairs per
class. For a negative class, retain canonical adjacency data, an explicit
five-order \(I_{5,3}\) profile (the construction above suffices when its
three-profile is included), a transparent CNF encoding five strict total
orders with exact \(3{:}2\) arc support, and a DRAT or preferably LRAT proof
verified by an independent checker. A solver's unsupported UNSAT line is
not evidence.

## Primary-source status (retrieved 2026-09-06)

The primary paper is Leonid Chindelevitch and Ararat Harutyunyan,
*Tournaments determined by three and five voters*, arXiv:2607.26690v1.
Its pp. 2–3 define \(I_{m,t}\); p. 12 reports the 254-class boundary; pp.
17–18 state Conjecture 8.1 and identify \(I_{5,1}\subsetneq I_{5,3}\) as an
open first case; pp. 25–27 give the census and reproducibility location.
Official sources inspected:

- https://arxiv.org/abs/2607.26690
- https://arxiv.org/pdf/2607.26690
- https://github.com/Leonardini/Tournaments

This finite 254-class assertion is a new derived question, not a theorem or
explicit open problem located in the paper. The nearest prior result is the
reported \(I_{3,3}\setminus I_{3,1}\) census plus Conjecture 8.1. The paper's
claim that every tournament on at most 11 vertices is 5-inducible gives only
\(I_{5,5}\), not \(I_{5,1}\), for this 3-inducible family; its stronger
margin-1 statement there concerns the complementary non-3-inducible classes.
No proof or disproof of the boxed finite claim was found in the inspected
primary paper or its repository overview.
