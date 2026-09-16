# Mathematical referee report

**Verdict: accept the exact frozen result-note scope.**

Job: `primary-20260914-brugidou-positivity-referee-486a48cf24dd`.
Snapshot: `a7e3cb1a0da871d53fdebc1638fdbbcc611f8739bce3289b362822cd5d358427`.
Review date: 2026-09-14 Asia/Shanghai (2026-09-13 UTC).

The candidate kind is `result-note` and its original status is `unresolved`.
Both fields retain exactly the meaning and value in `claim.json`. The accepted
theorem is the integrality and positive coefficient prefix for all hooks
specified there, and full positivity in its stated two-parameter region.
This report does not settle the original all-partition conjecture.

## Inputs and integrity

This is a fresh referee job. I read `source.md`, `problem.md`, `claim.json`,
`audit/snapshot.json`, and the listed proof, computational evidence, literature
comparison and source material. The source's complete 721-line text extraction
was read in consecutive bounded chunks, and the decisive statements were also
checked in the live primary paper. The Qiu--Zhang source was inspected at
Theorem 1.2 and the operator definition in Section 2.2. The proposer checker
was read, and its full JSON was parsed; every one of its 177 per-case records
was independently regenerated and compared, including the coefficient hash.

No checkpoint, scheduling state, earlier job transcript or separate owner
verdict was read. No other agents or model processes were used. The proposal's
confidence language has no role in this decision. The skill, referee reference,
and release contract were each read completely in a separate tool result.

All eleven frozen file hashes match. The SHA-256 of the sorted-key compact
JSON file mapping is the stated snapshot digest. The immutable source hash is
`41514463fec1850514a2d7e769680ea0403b78bc8ec786ce51eef70271847b1d`.
The verifier checks these bindings before and after its computations. No frozen
input was edited; this job adds only referee artifacts under `audit/`.

## Exact statement checked

Write

\[
 K_{a,b}=J_{(a,1^b)}/b!,\qquad
 d_{a,b}=\binom{a-1}{2}+(a-1)b,\qquad
 D_a=\binom{a-2}{2},\qquad
 F(a)=\max\left(0,\left\lceil\frac{D_a-4}{2}\right\rceil\right).
\]

For every pair of integers \(a\ge2,b\ge0\), the submitted claims are
\(K_{a,b}\in\mathbb Z[q]\), positivity at every integer degree
\(0\le k\le\min(d_{a,b},2b+3)\), and positivity throughout
\(0\le k\le d_{a,b}\) if \(b\ge F(a)\). The additional conclusion covering
all hooks with \(2\le a\le6\) uses established positive rows when \(b=0\).
No optimal cutoff, log-concavity or non-hook assertion is included.

The frozen original statement agrees with Brugidou's Conjecture 4.1 and its
normalization. Indices outside a polynomial's constant-to-leading range are
excluded. The empty partition is excluded; the original one-row and one-column
cases remain included. All cancellations below are polynomial identities, with
no division at a numerical value \(q=0\) or \(q=1\).

## Reconstruction of the decisive argument

For a hook, the multiplicity product is \(b!\), its size is \(a+b\), its
length is \(b+1\), and its valuation is \(\binom{b+1}{2}\). Consequently

\[
 \phi_q(m_{(a,1^b)})=
 \frac{(1-q)^{a-1}q^{\binom{b+1}{2}}}{(a+b-1)!}K_{a,b}.
\]

For \(a\ge3\), split the distinguished variable of \(p_{a-1}\) according to
whether it occurs in a monomial of \(e_{b+1}\). The two disjoint outcomes give

\[
 p_{a-1}e_{b+1}=m_{(a,1^b)}+m_{(a-1,1^{b+1})}.
\]

Each monomial occurs once because \(a-1\ge2\); the multiplicity would change
at \(a=2\), where this identity is not used. Substitution gives exactly

\[
 (1-q)K_{a,b}=\binom{a+b-1}{a-2}J_{a-1}
                  -q^{b+1}K_{a-1,b+1}. \tag{H}
\]

The source gives \(K_{2,b}=1+q+\cdots+q^b\) and rational polynomiality of
\(K_{a,b}\). Induction on \(a\), simultaneously for all \(b\ge0\), proves
integrality: division of an integral numerator by \(1-q\), when the quotient
is already known to be a polynomial, gives integral coefficient prefixes.
This does not assume the additional divisibility of \(J_{(a,1^b)}\) by \(b!\).
The source degree formula simplifies to \(d_{a,b}\). The constant term of
(H), including its base case, is

\[
 K_{u,v}(0)=\frac{(u+v-1)!}{(v+1)!}>0\quad(u\ge2,v\ge0).
\]

For \(a=3\), (H) gives the coefficient list consisting of \(b+1\) copies of
\(b+2\), followed by \(b+1,b,\ldots,1\). This proves the full positive base
case, also when \(b=0\).

The source's aggregate recurrence, at \(r=1\), is

\[
 J_m=\sum_{j=1}^{m-1}\binom{m-1}{j}q^{\binom j2}J_{m-1}^{(j)}.
\]

Its aggregate factors have nonnegative integer coefficients and constant term
\((m-1-j)!\). Thus, for \(m\ge3\),

\[
 R_m=J_m-(m-1)J_{m-1}\in\mathbb N[q],\qquad
 R_m(0)=0,\qquad [q]R_m=\binom{m-1}{2}(m-3)!=\frac{(m-1)!}{2}.
\]

The degree-one assertion uses only the \(j=2\) summand: every \(j\ge3\)
is shifted by at least three. The boundary \(m=3\) is legitimate and uses
\(J_2^{(2)}(0)=0!=1\). Individual non-row positivity is never presumed.

Now fix \(a\ge4\), put \(s=b+1\), \(N=a+b-1\), and set

\[
 A=\binom N{a-2}J_{a-1},\quad B=K_{a-1,b+1},\quad
 P=\binom N{a-3}J_{a-2},\quad C=K_{a-2,b+2}.
\]

Two applications of (H) give \((1-q)K=A-q^sB\) and
\((1-q)B=P-q^{s+1}C\). The binomial identity
\(\binom N{a-2}(a-2)=(s+1)\binom N{a-3}\) implies

\[
 \Delta=A-(s+1)P=\binom N{a-2}R_{a-1}\in\mathbb N[q],\qquad
 \Delta_1=(s+1)p_0/2>0,
\]

where \(p_i=[q^i]P\), with zero extension outside its support. For \(k<s\),
\([q^k]K\) is a positive prefix of \(A\). For \(k=s+t\), \(0\le t\le s\),
directly taking both prefixes gives

\[
 [q^k]K=\sum_{i=0}^{k}\Delta_i
       +\sum_{i=0}^{t}(s-t+i)p_i
       +(s+1)\sum_{i=t+1}^{k}p_i. \tag{P}
\]

Every term is nonnegative. If \(t<s\), the contribution \((s-t)p_0\)
is positive; if \(t=s\), the first sum contains \(\Delta_1>0\).
This proves positivity through \(k=2s\) without any positivity assumption
on \(B\) or nonconstant coefficients of \(C\).

At \(k=2s+1\), the shifted \(C\) term contributes for the first time, and
its contribution is exactly \(C_0\), with coefficient one. Hence

\[
 [q^{2s+1}]K=\sum_{i=0}^{2s+1}\Delta_i
  +\sum_{i=0}^{s+1}(i-1)p_i
  +(s+1)\sum_{i=s+2}^{2s+1}p_i+C_0
 \ge\Delta_1-p_0+C_0=\frac{s-1}{2}p_0+C_0>0. \tag{E}
\]

Here \(s\ge1\); in particular, the endpoint is still strict at \(s=1\).
For \(a=4\), \(C\) is the established \(a=2\) base, so \(C_0=1\).
Since \(d_{a,b}\ge3s\ge2s+1\) for \(a\ge4\), this index belongs to the
polynomial. Formula (E) is precisely the claimed endpoint \(2b+3\).
The smaller \(a\) cases were handled separately. This proves the full prefix
claim in its frozen range.

For full positivity, induct on \(a\) in the region \(b\ge F(a)\).
The function \(F\) is nondecreasing, so \(b+1\ge F(a-1)\); therefore the
induction hypothesis supplies positivity of all coefficients of \(B\).
Let \(D=\deg A=D_a\) and \(L=\deg B\). Polynomiality in (H), evaluated
after the identity is established, gives \(A(1)=B(1)\). For \(k\ge D\),

\[
 [q^k]K=A(1)-\sum_{j=0}^{k-s}B_j
        =\sum_{j>k-s}B_j.
\]

The prefix is empty when its upper limit is negative. The last sum contains
a positive coefficient for every \(k\le s+L-1=d_{a,b}\), including the
leading coefficient. The prefix result covers all remaining indices because

\[
 b\ge F(a)\quad\Longrightarrow\quad D-1\le2b+3.
\]

When \(D=2b+4\), the positive prefix ends at \(D-1\) and the tail begins
at \(D\), so the critical boundary has no gap. All small negative-ceiling
values are handled by the maximum with zero. Finally
\(F(2),F(3),F(4),F(5),F(6)=0,0,0,0,1\); established positive rows supply
the sole missing leg value \(b=0\) for \(a=6\).

This reconstructs all three assertions and the stated consequence. There are
no limiting exchanges, compactness assumptions, numerical sign inferences or
circular positivity lemmas in the argument.

## Independent exact checks

Run from the project directory:

```sh
python3 audit/referee-check.py
```

The completed output is `audit/referee-check.json`. This fresh script imports
no proposer implementation. It obtains specialized power sums from the finite
partition expansion of \(\log E(t)\), computes small hooks using the general
injective-assignment recurrence for augmented monomials, and compares them
against a fully unrolled hook numerator divided by polynomial long division
from the leading term. Thus it does not merely rerun the submitted recursive
hook/prefix computation.

The exact integer/rational checks all passed:

- 120 direct defining-specialization comparisons: every hook of size 2 through
  16, including all rows and \(a=2\) cases in that range.
- All 177 submitted per-case records and full coefficient hashes reproduced,
  including every recorded degree, cutoff, support index and minimum.
- 28 additional cases: \(17\le a\le20\), with
  \(b\in\{0,1,2,5,F(a)-1,F(a),F(a)+1\}\). Here the four cutoff values are
  51, 58, 66 and 75. These were absent from the submitted dataset.
- Row excess nonnegativity, zero constant and exact degree-one coefficient for
  \(3\le m\le20\); 3,243 prefix identities and 37,827 tail coefficient
  identities across the 205 computed hook cases.
- Threshold adjacency and induction-domain arithmetic for \(2\le a\le1000\).
  The universally quantified inequalities also have the algebraic proof above.
- The explicit \(K_{5,1}\) coefficient list agrees with the submission, in
  particular \([q^2]K_{5,1}=130\).

These are finite validation results. The universal theorem is justified by the
reconstruction above. The submitted labeled-tree enumeration was inspected
but was not independently rerun; the source's all-partition computation through
size 43 was not rerun either. No formal proof-assistant certificate is claimed.

## Source comparison and contribution

[Brugidou, arXiv:2306.15300v7](https://arxiv.org/html/2306.15300v7) supplies
polynomiality, degree and normalization in Corollary 3.5; the positive aggregate
polynomials and constants in the introduction; the recurrence used above in
Corollary 3.4's proof; and the \(a=2\) formula in (3.22). Its Corollary 5.2
establishes a terminal block of coefficients, while Section 4 records finite
all-partition checks. Its full text does not state the submitted hook prefix or
threshold theorem. The live abstract record still lists v7, revised 4 June 2025;
its stale abstract computation range is superseded by the size-43 statement in
the actual v7 text and version comments.

The later [Brugidou Tutte recurrence paper,
v2](https://arxiv.org/html/2509.20959v2), independently opened at Theorem 1.1
and Section 4, extends the aggregate recurrence to two variables. It does not
identify the individual hooks in this claim. The live record lists v2, revised
18 November 2025. The removed conjecture mentioned in that record belongs to
that paper's earlier version and is not the positivity conjecture under review.

The saved [Qiu--Zhang paper,
v2](https://arxiv.org/html/2607.00940v2) states signed Schur positivity of
iterates of \(\nabla\), a different operation. Its Section 2.2 gives
\(C_2(1)=-h_2/u\), writing \(u\) for the operator parameter. Independently,
\(\phi_q(h_2)=\phi_q(s_2)=1-q/2\), so at \(u=q\) its image is
\(1/2-q^{-1}\). This confirms the submitted objection to naive termwise
positivity transfer. It does not rule out more subtle consequences of that
paper, and none is asserted here.

Independent live queries included `"Brugidou" "hook" positivity`,
`"2306.15300" proof positivity`,
`"specialization of monomial symmetric functions" coefficients hook`, and
`"Brugidou" positivity conjecture 2026`. No equivalent theorem was found in
the inspected primary content. This is a bounded literature comparison, not
an exhaustive priority or current-open-status certificate.

The mathematical delta is substantive enough for one concise result note.
The low-degree excess comparison controls a genuinely subtractive overlapping
coefficient window; the aggregate positivity theorem alone does not isolate
individual hooks. It supplies both an initial range for every hook and an
infinite region of complete positivity. The elementary recurrence, integrality
observation, known rows and the local support-separation cutoff should not be
presented as separate new contributions. The frozen note already combines them.

For a concrete use, \((a,b)=(14,31)\) gives a hook of size 45, degree 481,
and \(F(14)=31\). The theorem proves its entire coefficient range, whereas
the source's specified terminal block covers degrees 438 through 481 and its
reported finite census stops at size 43. More generally the coefficient-window
comparison offers a usable starting point for extending the remaining hook
region. This is not merely a new finite check or an arbitrary isolated example.

## Gaps, limits and decision

No mathematical gap was found at the exact frozen scope. Both sensitive
boundaries, \(k=2b+3\) and \(D_a=2b+4\), are justified above and passed the
independent finite checks. The contribution is supported relative to the
inspected primary sources, with the stated literature limits.

Accept this snapshot as a `result-note`, with original status `unresolved`.
No claim revision is required. A manuscript should retain precisely this scope
and attribution, keep computational evidence separate from proof, and preserve
the bounded novelty language. This review does not authorize a stronger hook
theorem, optimality, log-concavity or resolution of the original conjecture.
The next workflow test is the runner's `check-math` provenance/integrity gate
before manuscript preparation; manuscript, citation, build and visual review
remain later jobs.
