# Precise problem: a monomial basis for a fixed involution class

## Frozen original and scope

The exact original remains in immutable `source.md`:

> Problem 29. Find an explicit monomial basis of \(R(M_{n,a})\).

Source: Hai Zhu, *Positive combinatorial formulae for involution matrix loci and
orbit harmonics*, EJC 33(2) (2026), P2.54, printed p. 21,
[DOI 10.37236/14808](https://doi.org/10.37236/14808).
This is a construction problem, not a single prespecified basis assertion.

For every integer \(n>0\) and every integer \(a\) with \(0\le a\le n\) and
\(a\equiv n\pmod2\), put \(k=(n-a)/2\) and
\[
M_{n,a}=\{P_w:w\in S_n,\ w^2=1,\ |\{i:w(i)=i\}|=a\}\subset\mathbb C^{n\times n},
\qquad (P_w)_{ij}=\mathbf1_{w(i)=j}.
\]
Write \(A=\mathbb C[x_{ij}:1\le i,j\le n]\), with total degree grading,
\(I(M)=\{f\in A:f(P)=0\text{ for all }P\in M\}\), and
\(\operatorname{gr}I(M)=\langle\tau(f):0\ne f\in I(M)\rangle\), where
\(\tau(f)\) is the highest nonzero homogeneous part of \(f\). Thus
\(R(M)=A/\operatorname{gr}I(M)\). The ideal uses all vanishing polynomials,
not just leading parts of an arbitrary chosen generating set.

Seek a uniform explicit combinatorial description of monomials
\(\mathcal B_{n,a}\subset A\) whose residue classes form a complex vector-space
basis. This means spanning and linear independence, and hence unique finite
linear expansion of every quotient element. They need not form an equivariant
basis or a Groebner standard basis. The source's intended contribution is a
combinatorial basis rule; generic Groebner elimination or finite greedy selection
already gives algorithmic existence and does not address that research aim.
No claim that “explicit” specifies a formal complexity bound is made.

The total required cardinality is \(n!/(a!2^k k!)\). For \(a=n\), the locus is
one point and \(R(M_{n,n})=\mathbb C\), with basis \(\{1\}\). Invalid parity,
\(a<0\), \(a>n\), and \(n=0\) are outside the source's quantified range.
Degrees greater than \(k\) vanish by the known ideal presentation (journal
Section 2.5); the actual top nonzero degree can be smaller.

## Precisely identified subsidiary candidate

For each integer \(0\le d\le k\), consider partitions \(\lambda\vdash n\),
\(\mu\vdash2d\), such that \(\lambda_1\le n-2d+a\), all parts of \(\mu\)
are even, \(\mu\subseteq\lambda\), and \(\lambda/\mu\) is a horizontal
strip (at most one removed box in each column). The empty partition is allowed.
Use English Young diagrams. Reading columns from left to right, start at height
zero and add +1 for a column meeting the strip and -1 otherwise. Require every
height through column \(\lambda_1\) to be nonnegative. This is exactly
\(\lambda/\mu\in\operatorname{PHS}(d,\lambda)\), Definition 5 and Equation (4).
“Even” refers to row lengths of \(\mu\), not its column lengths.

For each standard Young tableau \(P\) of shape \(\lambda\), with entries
\(1,\ldots,n\) increasing along rows and columns, reverse the row insertions
specified by the strip. Remove its boxes from rightmost column to leftmost;
at each removed corner, reverse bump through each preceding row by exchanging
with its rightmost smaller entry. The surviving tableau \(Q\) has shape
\(\mu\) and distinct entries drawn from \([n]\). This reverses insertion of
the removed labels in increasing order. Transpose \(Q\) before applying the
ordinary row-insertion RSK inverse:
\[
M=\operatorname{RSK}^{-1}(Q^{\mathsf t},Q^{\mathsf t}),\qquad
m(P,\lambda/\mu)=\prod_{i<j:\ M_{ij}=1}x_{ij}.
\]
Embed unused labels as zero rows and columns in the \(n\times n\) matrix.
The matrix is symmetric, has zero diagonal, and is a partial permutation with
\(2d\) ones. Thus each monomial is the squarefree edge product of a
\(d\)-edge matching. For \(d=0\), it is 1.

The subsidiary assertion is: **for every admissible \(n,a,d\), all these
monomials descend to a basis of \(R(M_{n,a})_d\)**. The source establishes the
index-set cardinality via Proposition 17 and states injectivity via Pieri.
It conjectures linear independence and reports computer verification for
\(a=0,n\le8\). A dependence would refute this candidate, not the original
problem of finding some explicit basis. A uniform proof would answer the original.

## Nearest prior results and proposed contribution

Liu--Ma--Rhoades--Zhu, *Involution matrix loci and orbit harmonics*,
[arXiv:2409.06175v1](https://arxiv.org/html/2409.06175v1), Theorem 3.3,
provides matching monomials for the locus of **all** involutions; Theorem 5.21
provides fixed-class graded characters. Zhu's journal Proposition 17 makes the
latter formula positive and supplies the above cardinality-matched candidate.
The journal also supplies a statistic answering its broad Problem 28, which is
not an alternative unsolved target here.

Nearest prior result X: these character, ideal, and counting results.
Proposed delta Y: a uniform proof of the candidate's basis property, or a
nontrivial structural straightening result / exact counterexample to that
specifically identified subsidiary assertion. Verification route Z: exact
filtered evaluation first, then a complete argument or dependence certificate
with a fresh mathematical audit. Small successful tables alone are not a paper.

## Exact finite verifier and triage evidence

Let \(F_{\le d}\subseteq\mathbb C^{M_{n,a}}\) be evaluations of all polynomials
of total degree at most \(d\), and \(F_{\le-1}=0\). The associated graded
construction identifies \(R(M_{n,a})_d\) with
\(F_{\le d}/F_{\le d-1}\). For candidate evaluation columns \(C_d\), check
\[
\operatorname{rank}[F_{\le d-1},C_d]-\dim F_{\le d-1}
=|C_d|=\dim F_{\le d}-\dim F_{\le d-1}.
\]
All matching monomials of sizes at most \(d\) span \(F_{\le d}\): on the locus,
\(x_{ji}=x_{ij}\), \(x_{ii}=1-\sum_{j\ne i}x_{ij}\), each off-diagonal
coordinate is idempotent, and two different edges sharing a vertex have zero
product. These identities reduce every coordinate monomial without increasing
degree. This is a computational spanning reduction, not the missing candidate
straightening theorem.

`evidence/triage_rank.py` tests exactly (3,1), (4,0), (5,1), (6,2), all allowed
degrees, with rational arithmetic. Every inverse Pieri and RSK instance checks
against its forward operation. All pass, with graded dimensions respectively
(1,2), (1,2,0), (1,9,5), and (1,14,30). A separate script enumerates permutation
matrices directly and uses SymPy QQ ranks of all original-coordinate monomials;
it reproduces every rank. Candidate generation is shared data, not independently
rederived by that verifier. These are finite observations, not a universal proof.

Source status: **open-supported, with bounded literature coverage** as of
2026-09-14. The live publisher and arXiv pages and inspected journal text support
this reading; no later equivalent solution was found in the recorded queries.
No exhaustive priority guarantee or completed local historical-registry audit
is claimed; see `literature/triage-screen.md`.

## Research pass 1: strictly scoped partial result

The assigned (7,1) test passes in every degree, with graded dimensions
(1,20,70,14). Forward and inverse tableau constructions agree, and separate
QQ arithmetic reproduces the ranks. Additional exact cases and their scope
are indexed in checkpoint.md. None refutes the source's candidate.

A proposed partial theorem, with a complete argument in
`evidence/quadratic-proof.md`, concerns a>=2 and k=(n-a)/2>=2 only.
Let H_n be all two-edge matching monomials and set

T_n = {x_12 x_ij:3<=i<j<=n}
    union {x_13 x_2j:4<=j<=n}
    union {x_1j x_23:4<=j<=n}
    union {x_15 x_24,x_15 x_34,x_25 x_34}.

The theorem identifies the literal degree-2 candidate with H_n minus T_n
and proves it is a basis. In the off-diagonal presentation it is also the
degree-2 standard monomial set for every monomial order refining the positive
weight w(x_ij)=n^2-ij. Together with {1} and all degree-1 edges except 12,
this gives a complete explicit standard monomial basis of R(M_(n,n-4))
for every n>=6, since higher degrees then vanish. This leaves the original
uniform all-n,a problem unresolved.

The elementary incidence/Lefschetz method is known: Dao--Nair,
*On the Lefschetz property for quotients by monomial ideals containing
squares of variables*, arXiv:2112.09434v4, Proposition 3.1, Lemma 3.2,
Theorem 3.3. The proposed contribution is the tableau identification and
specific uniform weight comparison, not the incidence-rank criterion or
known Hilbert dimensions. See `literature/research-screen.md` for the primary
comparison and its limits. Fresh mathematical and significance review is
required; no acceptance or manuscript has been created.
