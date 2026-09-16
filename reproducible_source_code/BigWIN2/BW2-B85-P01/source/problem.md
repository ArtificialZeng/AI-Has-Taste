# Precise problem reading

Provenance: triage job `win-00085-p01-triage-310493b59e59` on
2026-09-10. The immutable input is `source.md`, with intake SHA-256
`8bdbd0fa48aea26f73f732eaeb115a15243603a548dc4dabaca4647bf1af6990`.

## Objects and conventions

For \(n\in\{5,6\}\), let \(\mathcal H_n=(\mathbb C^2)^{\otimes n}\).
The symbols \(I,X,Y,Z\) are the usual Hermitian one-qubit Pauli matrices;
a word is their tensor product in the displayed coordinate order. Every
displayed generator has scalar phase \(+1\). For a displayed generator triple
\(G\), let \(S(G)\) be the Pauli subgroup it generates, including the phases
forced by Pauli multiplication, and put

\[
Q(G)=\{v\in\mathcal H_n:gv=v\text{ for every }g\in S(G)\}.
\]

The four ordered triples are

\[
\begin{aligned}
G_A&=(ZZZZI,XXIIX,IIXXX),\\
G_B&=(ZZIZX,XIZXI,IXXYI),\\
G_+&=(XXIIXX,IIXXXX,ZZZZIX),\\
G_-&=(XXZXII,ZZXYII,IZZZXX).
\end{aligned}
\]

Exact symplectic calculation shows that each triple is commuting and binary
independent. Consequently every \(S(G)\) has eight elements, contains no
\(-I\), and \(\dim_{\mathbb C}Q(G)=2^{n-3}\): dimension four for the
five-qubit codes and eight for the six-qubit codes.

For \(\pi\in\operatorname{Sym}(n)\), fix

\[
P_\pi(v_1\otimes\cdots\otimes v_n)
=v_{\pi^{-1}(1)}\otimes\cdots\otimes v_{\pi^{-1}(n)}.
\]

The inverse convention is immaterial to an existential assertion. A
product-local unitary is \(U_1\otimes\cdots\otimes U_n\), where each
\(U_i\in U(2)\) is arbitrary (not necessarily Clifford).

## Two independently quantified assertions

Determine the truth value of each assertion separately:

\[
\begin{aligned}
E_5:\quad&\exists\pi\in\operatorname{Sym}(5)\ \exists U_1,\ldots,U_5\in U(2):
(\bigotimes_{i=1}^5U_i)P_\pi Q(G_A)=Q(G_B),\\
E_6:\quad&\exists\pi\in\operatorname{Sym}(6)\ \exists U_1,\ldots,U_6\in U(2):
(\bigotimes_{i=1}^6U_i)P_\pi Q(G_+)=Q(G_-).
\end{aligned}
\]

Equality is equality of code subspaces, not equality of a chosen generator
list or stabilizer group. An overall scalar phase is irrelevant. Entangling
unitaries and antiunitaries are excluded. Moving \(P_\pi\) to the other side
of the product unitary only relabels the one-qubit factors. The two assertions
do not have to use related permutations or unitaries.

## Prior result, scope, and proposed delta

Mahmoud, arXiv:2607.26214v1, Theorem 5.3(ii),(iii), proves that the displayed
pairs have the stated weight-isometry properties and are not monomially
equivalent. Question 5.4 explicitly asks \(E_5\) and \(E_6\). The arXiv record
still listed only v1 on 2026-09-10; limited exact-assertion searches found no
later primary resolution, so the source status is **open-supported**, not a
certification that the questions remain open.

For \(A\subseteq[n]\), define

\[
d_S(A)=\dim_{\mathbb F_2}\{g\in S:\operatorname{supp}(g)\subseteq A\}.
\]

Van den Nest--Dehaene--De Moor, arXiv:quant-ph/0404106v2, equation (14),
identifies these support-subcode dimensions with degree-two local-unitary
invariants. Equivalently, for the normalized code projector \(\rho_S\),

\[
\operatorname{rank}(\operatorname{Tr}_{A^c}\rho_S)
=2^{|A|-d_S(A)}.
\]

Thus product-local equivalence preserves the indexed function \(d_S\), while
a qubit permutation relabels its arguments. The nearest prior result is this
general invariant. The proposed delta is its explicit application, with small
separating incidence certificates, to Mahmoud's two pairs; no invention of the
invariant is claimed. A research pass should independently derive the reduced
projectors/ranks, verify the full signed Pauli tables, and turn the observed
separators into a self-contained proof that no coordinating permutation exists.
