# Precise problem statement

## Frozen source and status

The immutable statement is `source.md` (SHA-256
`a4e8a9bb1fdaa7a9e9b0266a518a1ee0d134f343adf5c7f056e20034d68aa67e`).
The definitions below make its intended finite problem explicit; they do not
alter the source statement.

The motivating asymptotic question

\[
  \frac{E(n)}{N(n)}\longrightarrow 0\qquad(n\to\infty)
\]

is **not** part of the finite target and remains unresolved here. A finite
determination of the first incompatibility layer would not resolve that limit.

## Objects and conventions

All indices and elements below are integers. For every \(n\geq 1\), let

\[
 X_n=\{2,3,\ldots,n+1\},\qquad
 R_n=\prod_{k=2}^{n}\mathbb Z/k\mathbb Z.
\]

For \(n=1\), the product is empty and \(R_1\) contains one empty profile.
For a profile \(r=(r_2,\ldots,r_n)\in R_n\), define

\[
 S_n(r)=\bigl\{m\in X_n:
 [m]_k\ne r_k\text{ for every }k\text{ with }2\leq k<m\bigr\}.
\]

The survivor family and its size are

\[
 \mathcal F_n=\{S_n(r):r\in R_n\},\qquad N(n)=|\mathcal F_n|.
\]

Thus membership in \(\mathcal F_n\) means realizability by at least one full
profile; different profiles may yield the same set. Define the extendible
family by

\[
 \mathcal E_n=\left\{A\in\mathcal F_n:
 \begin{array}{l}
 \text{there is }r\in R_n\text{ with }S_n(r)=A,\text{ and}\\
 r_k\ne[n+2]_k\text{ for every }2\leq k\leq n
 \end{array}\right\},
 \qquad E(n)=|\mathcal E_n|.
\]

Equivalently, \(A\in\mathcal E_n\) if and only if
\(A\cup\{n+2\}\in\mathcal F_{n+1}\). Empty universal quantifiers have their
usual vacuous meaning, so these definitions also cover \(n=1\).

For any \(A\subseteq X_n\) and each \(2\leq k\leq n\), set

\[
 \Omega_k^+(A)=\mathbb Z/k\mathbb Z\setminus
 \left(\{[x]_k:x\in A,\ x>k\}\cup\{[n+2]_k\}\right).
\]

For every omitted point \(m\in X_n\setminus A\), set

\[
 W_A(m)=\{k\in\{2,\ldots,m-1\}:[m]_k\in\Omega_k^+(A)\}.
\]

Define \(L_n(A)\) to be the conjunction

\[
 \bigl(\forall k\in\{2,\ldots,n\},\ \Omega_k^+(A)\ne\varnothing\bigr)
 \quad\text{and}\quad
 \bigl(\forall m\in X_n\setminus A,\ W_A(m)\ne\varnothing\bigr).
\]

## Exact CSP interpretation

For \(A\subseteq X_n\), introduce one variable \(a_k\) for every
\(2\leq k\leq n\), with domain \(a_k\in\Omega_k^+(A)\). For every omitted
point \(m\in X_n\setminus A\), impose the clause

\[
 \bigvee_{k\in W_A(m)}\bigl(a_k=[m]_k\bigr).
\]

Equivalently, if

\[
 C_{k,a}(A)=\{m\in X_n\setminus A:m>k,\ [m]_k=a\},
\]

the selected blocks must cover \(X_n\setminus A\). Theorem 30 of the cited
source says, for the essential hypothesis \(A\in\mathcal F_n\),

\[
 A\in\mathcal E_n
 \quad\Longleftrightarrow\quad
 \text{this finite CSP is satisfiable}.
\]

Hence \(L_n(A)\) says that every variable domain and every individual omitted
point has a local witness. It does not require those witnesses to be mutually
compatible.

## Quantity to determine and classification required

Let

\[
 \mathcal G_n=\{A\in\mathcal F_n\setminus\mathcal E_n:L_n(A)\}.
\]

The target is to prove that \(\{n\geq1:\mathcal G_n\ne\varnothing\}\) is
nonempty, determine

\[
 n_*=\min\{n\geq1:\mathcal G_n\ne\varnothing\},
\]

and give a complete literal list of all subsets in \(\mathcal G_{n_*}\).
No equivalence relation “up to symmetry” is specified, so classification means
equality with the full set \(\mathcal G_{n_*}\), not representatives. The
displayed minimum is undefined if the indexing set is empty; therefore
existence of an incompatibility is part of what must be proved. If instead one
proved \(\mathcal G_n=\varnothing\) for every \(n\), the correct conclusion
would be that \(n_*\) does not exist, not a numerical value. A bounded search
alone cannot establish that global alternative.

A complete claimed value and classification must include:

1. an exact, reproducible exhaustive generation certificate for
   \(\mathcal F_n\) through the first layer, in particular proving
   \(\mathcal G_n=\varnothing\) for every \(1\leq n<n_*\) and completeness of
   the candidates at \(n_*\);
2. a separate implementation of the Theorem 30 CSP test, based directly on
   the domains and coverage clauses above rather than inferring extendibility
   from the generation recurrence; and
3. for each \(A\in\mathcal G_{n_*}\), an explicit human-readable unsatisfiable
   conflict core: a displayed finite collection of omitted-point clauses and
   residue-domain restrictions whose incompatibility is proved, while the
   nonemptiness assertions in \(L_{n_*}(A)\) are also exhibited. Minimality of
   a core is not required unless separately claimed.

All computations must be exact (integer/residue or bit-set operations, not
floating-point or heuristic solver output), and their coverage ranges must be
stated.

## Nearest source result, proposed delta, and scope

The inspected primary source is Raso--Venturi, *Counting Survivor Sets:
Exponential Equivalence with Prime-Admissible Sets*, arXiv:2609.08528v1,
8 September 2026 (local PDF SHA-256
`87fcffe17bb2ab225420b76944a4979e0de5aced59e3ca529f886e78af05cb96`,
inspected 2026-09-09). Definitions 26 and 28--29 define extendibility and the
residue domains/blocks; Theorem 30 gives the exact CSP criterion; Corollaries
31 and 33 give the two kinds of necessary local conditions; Remark 34 points
to incompatible residue choices; and Proposition 36 gives an exact dynamic
enumeration of \(\mathcal F_n\) (printed pages 26--30). The paper does not give
the first genuine layer or classify it in those inspected passages.

The proposed delta is therefore: nearest result = the exact criterion and
dynamic recurrence; new finite target = the least layer and complete exception
set; verification route = exact layer-by-layer generation, a separately coded
CSP decision procedure, and replayable conflict cores. This is a
source-derived finite question. Its publication novelty is **status-uncertain**
because only the recent v1 and its indicated passages have been inspected in
this triage; no priority claim is made.
