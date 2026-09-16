# Precise reading

## Frozen input and status

The original task is frozen verbatim in `source.md` (SHA-256
`b7785e0011f4ce3924d7dc440dcc38190302db050ffe19c18159e3ca45076baf`).
This file interprets it without altering it.

The primary paper is Huibo Xu, Shi Fu, Youming Qiao, and Dacheng Tao,
*Synchronization Strings over the Optimal Alphabet*, arXiv:2609.04122v1
(submitted 2026-09-03), <https://arxiv.org/abs/2609.04122>. It was inspected
on 2026-09-07. Theorem 1.5 and Proposition D.7 (pp. 4 and 34--35) prove the
denominator `D=227`; Appendices D--E give the construction and its exact
finite/analytic certificates. The paper says that optimizing the
synchronization parameter remains open (p. 5), but it does not state the
present fixed-framework `D=226` refinement as an established open problem.
Accordingly, the source status of this refinement is **new-question**, not a
verified literature-open problem.

## Definitions

Let `Sigma={0,1,2}`. Words use half-open interval notation: for a word `S` of
length `n`, `S[i,j)` is the factor in positions `i,...,j-1`. (The paper uses
one-based endpoints `1 <= i < j < k <= n+1`; shifting all endpoints by one is
immaterial.) For finite words `X,Y`, let

`ED(X,Y) = |X|+|Y|-2 LCS(X,Y)`

be insertion/deletion edit distance; substitutions are not primitive and cost
two operations. Two nonempty factors `A=S[i,j)` and `B=S[j,k)` are adjacent
when they share the boundary `j`. Their total length is `s=k-i=|A|+|B|`.
The non-strict normalized adjacent-interval gap of `S` is

`g(S) = min_{1 <= i < j < k <= n+1} ED(S[i,j),S[j,k))/(k-i)`.

Thus `g(S) >= 1/D` means

`ED(S[i,j),S[j,k)) >= (k-i)/D`

for every adjacent nonempty interval pair. Because `ED` is integral, this is
equivalent to `ED >= ceil((k-i)/D)`. It implies the paper's strict
epsilon-synchronization inequality for every `epsilon > 1-1/D`, but not
automatically at equality `epsilon=1-1/D`.

## Fixed construction and what may vary

Fix the special 54-uniform Brinkhuis 952-triple from Proposition D.1 and the
artifact at commit `5e9e0c05fca32a5d5735cab9914626ffe667c53c`. Concretely, there
are 952 distinct length-54 codewords in each `D_a` (`a in Sigma`); `D_1` and
`D_2` are obtained from `D_0` by cyclic alphabet shifts, and `D_0` is closed
under reversal. For a ternary square-free outer word
`T=T_1...T_N`, choose independently an index `R_q in {1,...,952}` at each
occurrence and form

`W(T,R)=D_{T_1,R_1} ... D_{T_N,R_N}`.

Every such output is square-free. For a requested `n`, the framework takes
`N=ceil(n/54)`, obtains an admissible occurrence-choice vector by the asymmetric
Lovasz Local Lemma, and returns the length-`n` prefix.

The following ingredients are fixed: the codebooks and square-free outer-word
setup; the fragment-aware exact conditional masses `P_l` of (33); the exact
left/right deletion-event volumes of (34); the dependency count with additive
constant 109; and the charge parameters

`alpha=51/100000`, `beta=3/10`.

For a candidate denominator `D`, lengths `a,b>=1`, and `s=a+b`, a direct bad
event is relevant only when `s>=D+1` and `D|a-b|<s`, and is

`E_{t,a,b}(D) = { ED(W[t,t+a),W[t+a,t+a+b)) < s/D }`.

Writing `u=a-LCS` and `v=b-LCS`, its exact raw volume sums over integer pairs
with `v-u=b-a`, `(u,v)!=(0,0)`, and `D(u+v)<s`. The two orientations weight
each pair respectively by

`binom(a,u) binom(b,v) 3^u` and
`binom(a,u) binom(b,v) 3^v`.

Multiplication by the corresponding `P_a` or `P_b` and taking the smaller
orientation gives the exact probability upper bound `p_D(a,b)`. A retained
event has the fixed charge

`x_D(a,b)=p_D(a,b) exp(alpha*s+beta)`.

The exact charge-envelope test must be recomputed with the `D`-dependent event
set and volumes. In the notation of Lemma D.6 this includes verifying every
charge is below the required range and the two sufficient inequalities

`R_0(D)<alpha`, `109 R_0(D)+R_1(D)<beta`,

where `R_0` and `R_1` sum `x_D/(1-x_D)` and
`s*x_D/(1-x_D)`, respectively, over all retained ordered length types. Any
types removed from the raw event calculation must instead be covered by exact
enumeration, an analytic proof, or a separately checked structural certificate.
For `D=227` the published exceptional totals are
`{229,231,...,463} union {456,462,464}`; these exclusions are
denominator-specific and are not a certificate for `D=226`.

## Quantified target

For an integer `D>=1`, let `C(D)` mean that the fixed construction and fixed
charge rule above, together with a complete newly valid exact treatment of all
`D`-relevant finite shells, certify

`for every n>=1, there exists S in Sigma^n such that g(S)>=1/D`.

Determine the least `D` for which `C(D)` holds, testing `C(226)` before any
smaller denominator. `C(227)` is the nearest prior certified result. Therefore:

- success at 226 is an explicit-parameter improvement but does not by itself
  establish minimality; smaller denominators would still have to be tested;
- failure at 226 must be reported as the first exact failed framework
  inequality or an explicit newly relevant shell witness;
- such failure is an obstruction only to this fixed certificate framework and
  does not prove that ternary words with gap `1/226` do not exist, nor that 227
  is globally optimal.

## Admissibility and first decisive test

Nearest prior result: `C(227)` (Xu--Fu--Qiao--Tao, Proposition D.7).
Proposed delta: certify `C(226)`, or obtain a reproducible exact obstruction to
that fixed method. Verification route: verify the frozen artifact/commit and
the default 227 certificate, then run its exact-rational denominator diagnostic
at 226 without importing the 227 shell exclusions; list every newly relevant
total and audit precisely the raw-bound failures. This is a precise,
nontrivial target with a bounded first test, so it is suitable to advance to
research.
