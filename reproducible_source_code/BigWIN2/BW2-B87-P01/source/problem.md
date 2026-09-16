# Precise reading and triage target

## Frozen statement

The immutable statement is `source.md` (SHA-256
`6d335fd74e75e87e406c31cfb1f57cc3d41eb9ac2e22eaab0b8cae79449a4858`).
It is read as follows.

- A **tournament** on a finite set \(V\) is a loopless orientation of every
  two-element subset of \(V\). Write \(x\to_i y\) when the arc is directed
  from \(x\) to \(y\) in \(T_i\).
- A vertex \(x\) **dominates** \(U\subseteq V\) in \(T_i\) when
  \(x\to_i u\) for every \(u\in U\). Looplessness forces \(x\notin U\); in
  particular, the witness is one common outside vertex in one common
  tournament.
- For integers \(m,k\geq1\), \(f(m,k)\) is the least integer \(n\geq k+1\)
  such that some indexed family \((T_1,\ldots,T_m)\) of tournaments on the
  same \(n\)-element set \(V\) satisfies
  \[
    (\forall U\in {V\choose k})(\exists i\in\{1,\ldots,m\})
    (\exists x\in V\setminus U)(\forall u\in U)\;x\to_i u.
  \]
  Repeated tournaments are allowed by this reading but never help.
- The claim is
  \[
      (\forall k\in\mathbb Z,\ k\geq3)\qquad f(k-1,k)=k+3.
  \]
  Thus both an order-\(k+3\) construction and nonexistence at every order
  below \(k+3\) are required. Since \(n\geq k+1\), the latter has exactly the
  two boundary cases \(n=k+1\) and \(n=k+2\). The case \(k=2\) is excluded.

For a tournament \(T\) of order \(n\), define the auxiliary simple graph
\(H_T\) on \(V(T)\) by
\[
  ab\in E(H_T)\quad\Longleftrightarrow\quad
  a\to V\setminus\{a,b\}\text{ or }b\to V\setminus\{a,b\}.
\]
Equivalently, \(ab\) records that the \((n-2)\)-set complementary to
\(\{a,b\}\) has a valid witness. The structural subclaim to verify is: for
every \(n\geq3\), \(H_T\) is contained in a star, or \(H_T\) is exactly a
triangle.

## Source status and nearest result

Primary source inspected on 2026-09-11:
[Joel Jeffries, arXiv:2604.08790v1](https://arxiv.org/abs/2604.08790), PDF
pp. 4--10. The arXiv history listed only v1, submitted 2026-04-09.
Definitions 2.1--2.2 give the common-vertex/common-tournament quantifiers.
Proposition 2.3 and Theorem 2.2 give a gluing construction which specializes
to the upper bound \(f(k-1,k)\leq k+3\). Figure 7 reports SAT-confirmed
equalities for this slice at \(k=3,4,5,6\). The conclusion says the paper has
no nontrivial general lower bound for \(f(m,k)\); it does not explicitly state
the present all-parameter slice as an open problem.

Exact-assertion and equivalent-language web searches on 2026-09-11 located no
primary source beyond Jeffries's paper that states or settles this slice.
This is only a limited negative search, not evidence of priority. Accordingly
the source status is **new-question / status-uncertain**, not a verified listed
open problem.

## Proposed contribution and verification route

Nearest prior result: the order-\(k+3\) gluing upper bound and exact SAT values
for \(3\leq k\leq6\). Proposed delta: a uniform lower bound for all \(k\geq3\),
plus an independent explicit validation of the construction. Verification
route: prove the stated classification of \(H_T\), turn order \(k+2\) into an
edge-cover obstruction, check order \(k+1\) separately, and directly verify
the block construction. `evidence/triage_check.py` supplies a small exact
sanity check; it is not a proof of the quantified claim.

## Research-pass status

Research job `win-00087-p01-research-981c2d1e0004` has written a complete
proof candidate at `evidence/research_proof.md`; it is not yet referee
certified. One counting detail is made explicit there: if there are \(a\)
star-type auxiliary graphs but only \(r\le a\) distinct chosen centers, then
after deleting those centers the number of triangle-type graphs is at most
\(n-3-a\le n-3-r=q-3\). Thus repeated star centers cannot invalidate the
edge-cover obstruction. The proof treats \(n=k+1\), \(n=k+2\), \(q=3\), and
the construction at \(k=3\) without exceptions. Publication priority remains
uncertain and is not part of the submitted mathematical claim.
