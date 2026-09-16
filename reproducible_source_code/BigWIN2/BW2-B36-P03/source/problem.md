# Precise problem statement

## Frozen source and status

The original wording is preserved verbatim in `source.md` (SHA-256
`377a023c95e7cab2168d3560250420b87ae89ebd1e1c8f0bfe0ec83831669a09`).
Nothing in this file changes that wording.

The supplied nearest-prior-result lead is Zijian Zeng, *The Exact Two-Row
Pairwise-Coprime Grid Threshold Is L 41 = 529*, DOI
`10.2139/ssrn.7395519`, claiming \(L_{41}=529\). The local record
`literature/user-library-record.md` contains only workbook metadata and an
abstract, not the paper or its certificates. Exact-title, exact-DOI, and SSRN
site searches on 2026-09-06 did not expose the target record; direct retrieval
also failed. Thus the current source status is **status-uncertain**: the cited
theorem and any auxiliary data are leads, not yet verified facts. This is an
access/verification limitation, not evidence that the citation or theorem is
false.

## Definitions and quantifiers

For integers \(n\geq 1\), \(x\), and \(d>0\), and a finite set
\(V\subset\mathbb Z\), put

\[
S(d,V):=\bigcup_{v\in V}\{v,v+d\}.
\]

Call \((x,d,V)\) an \(n\)-column, two-row witness when

1. \(d\in\mathbb Z_{>0}\);
2. \(V\subseteq[2,x-d]\cap\mathbb Z\) and \(|V|=n\);
3. \(|S(d,V)|=2n\) (all displayed entries are distinct); and
4. for every two distinct \(a,b\in S(d,V)\), \(\gcd(a,b)=1\).

Then the intended definition is

\[
L_n=\min\{x\in\mathbb Z:\exists d\in\mathbb Z_{>0}\ \,
\exists V\subset\mathbb Z\text{ such that }(x,d,V)
\text{ is an }n\text{-column, two-row witness}\}.
\]

This minimum exists. For example, fix \(d=2\). Given finitely many already
chosen odd starts whose pairs are pairwise coprime, let \(P\) be the product of
the odd primes dividing the existing entries. For each \(p\mid P\), choose a
residue for the next start avoiding \(0\) and \(-2\pmod p\); at least one exists
even for \(p=3\). The Chinese remainder theorem, together with the odd-parity
condition, supplies arbitrarily large such starts. The new pair is coprime
internally and to every old entry. Induction gives a witness for every \(n\) at
some finite \(x\).

The precise claim to decide is

\[
\boxed{L_{42}=529}.
\]

Equivalently, once the claimed lower bound \(L_{42}\geq L_{41}=529\) is
independently validated, decide whether

\[
\exists d\in\mathbb Z_{>0}\ \,\exists V\subseteq[2,529-d]\cap\mathbb Z,
\quad |V|=42,
\]

such that the 84 members of \(S(d,V)\) are distinct and pairwise coprime. A
yes-instance, together with the validated lower bound, proves equality. A
complete no-instance at \(x=529\), together with that lower bound and the
integrality of \(L_{42}\), proves \(L_{42}\geq530\).

## Boundary reductions

- Feasibility at size \(n\) implies feasibility at every smaller size by
  deleting starts. Hence \(L_n\) is nondecreasing in \(n\), and verified
  \(L_{41}=529\) would imply \(L_{42}\geq529\).
- At \(x=529\), nonempty \(V\subseteq[2,529-d]\) forces
  \(1\leq d\leq527\).
- For \(n\geq2\), \(d\) cannot be odd: every pair would contribute one even
  entry, producing two distinct even entries with gcd at least 2. Thus only
  the 263 gaps
  \[
  d\in\{2,4,\ldots,526\}
  \]
  are admissible at \(x=529\).
- For even \(d\), every admissible start \(v\) is odd and satisfies
  \(\gcd(v,d)=1\), since
  \(\gcd(v,v+d)=\gcd(v,d)\).

## Exact finite formulation and scope

For fixed \(x,d\), define a graph \(G_{x,d}\). Its vertices are

\[
C_{x,d}:=\{v\in[2,x-d]\cap\mathbb Z:\gcd(v,v+d)=1\}.
\]

Distinct vertices \(v,w\) are adjacent exactly when the four entries in
\(\{v,v+d,w,w+d\}\) are distinct and every cross-pair has gcd 1. Then an
\(n\)-column, two-row witness with fixed \(x,d\) is exactly an \(n\)-clique in
\(G_{x,d}\). Consequently the unresolved finite assertion is

\[
\max_{d\in\{2,4,\ldots,526\}}\omega(G_{529,d})\ \mathrel{?}\ \geq42.
\]

The first research computation must use exact integer gcd predicates. A
positive answer must output an explicit \((d,V)\) certificate and directly
check all 84 entries. A negative answer must cover all 263 even gaps with a
reproducible completeness certificate; timeout or solver failure is not an
exclusion. The paper's \(L_{41}\) theorem and auxiliary data must be obtained
and checked before they are used as mathematical evidence.
