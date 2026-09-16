# Precise problem reading

## Frozen lead

The original lead is: “Determine the first unresolved unbalanced complete-multipartite value in the source: `eta(K_{1,1,5})`.” The full frozen statement remains in `source.md`; this file interprets it without altering it.

## Objects and quantifiers

Let
\[
G=K_{1,1,5}=K_2\vee \overline{K_5}.
\]
Write its three parts as \(A=\{a\}\), \(B=\{b\}\), and \(C=\{c_0,\ldots,c_4\}\). Thus the edges are \(ab\), every \(ac_i\), and every \(bc_i\); the ten pairs \(c_ic_j\) with \(i\ne j\) are precisely the nonedges.

For a finite abelian group \(\Gamma\), written additively, and a symmetric set \(S=-S\subseteq\Gamma\setminus\{0\}\), the simple undirected Cayley graph \(\operatorname{Cay}(\Gamma,S)\) has distinct \(x,y\) adjacent exactly when \(y-x\in S\). An induced abelian Cayley embedding of \(G\) is an injection \(f:V(G)\to\Gamma\) such that, for every unordered pair of distinct vertices \(u,v\),
\[
uv\in E(G)\quad\Longleftrightarrow\quad f(v)-f(u)\in S.
\]
Define \(\eta(G)\) as the minimum of \(|\Gamma|\) over **all** finite abelian groups and all such \((f,S)\). The problem is to determine the single integer \(\eta(K_{1,1,5})\) exactly; it does not ask for a classification of all unbalanced complete multipartite graphs or only cyclic hosts.

Equivalently, for a proposed injection let \(D_E\) contain both orientations of all edge differences and let \(D_N\) contain both orientations of all nonedge differences. A suitable \(S\) exists exactly when \(D_E\cap D_N=\varnothing\), in which case \(S=D_E\) works. Translation permits the normalization \(f(a)=0\). This gives an exact finite verifier, not merely a numerical test.

## Established bracket and boundary cases

The seven labels force \(|\Gamma|\ge 7\). More strongly, the neighborhood of \(a\) contains the independent set \(C\) of size five, so the local order floor in Theorem 6 of the cited source gives
\[
\eta(K_{1,1,5})\ge \max(7,2\cdot5)=10.
\]

There is an explicit order-15 embedding. In \(\Gamma=\mathbb Z_{15}\), take
\[
f(C)=\{0,3,6,9,12\},\qquad f(a)=1,\qquad f(b)=2,
\]
and
\[
S=\{x\in\mathbb Z_{15}:x\not\equiv0\pmod3\}.
\]
Internal differences in \(C\) are nonzero multiples of three, while every edge difference is nonzero modulo three. Hence the all-pairs condition holds and
\[
10\le \eta(K_{1,1,5})\le15.
\]

To certify the value 15 by exhaustion, the unresolved lower search has only these abelian group types: \(\mathbb Z_{10}\), \(\mathbb Z_{11}\), \(\mathbb Z_{12}\), \(\mathbb Z_2\times\mathbb Z_6\), \(\mathbb Z_{13}\), and \(\mathbb Z_{14}\). Orders below 10 are excluded by the proved local floor. If an embedding occurs earlier, its group, seven labels, and an exact all-pairs check certify the corresponding upper bound, but all smaller orders still require exclusion.

## Source status and correction

The relevant primary source is R. Fokam Souop and L. Bitjoka, *Induced Embeddings of Graphs into Abelian Cayley Graphs*, arXiv:2609.01486v1 (2026), Definition 1, Theorem 6, and Remark 12, <https://arxiv.org/abs/2609.01486v1>, inspected 2026-09-07. Remark 12 gives the floor 10, the residue-class construction of order 15, explains only why one obvious \(\mathbb Z_{10}\) refinement fails, and states that determining \(\eta\) for unbalanced complete multipartite graphs is open.

The frozen `source.md` incorrectly attributes this arXiv identifier and title to J. A. Noel and J. A. Scott. The official arXiv record and the local PDF metadata both name Rigobert Fokam Souop and Laurent Bitjoka; the local PDF SHA-256 agrees with the hash frozen in `source.md`. This bibliographic correction does not change the mathematical question.

A targeted search for the exact value and equivalent terminology on 2026-09-07 found no separate primary source resolving this fixed instance. This is a limited literature screen, not proof of novelty or priority. Triage therefore records the source status as **open-supported**, subject to a broader literature check before any novelty claim.

## Triage target

Nearest prior result: the certified bracket \(10\le\eta\le15\) above. Proposed delta: determine the exact value for this fixed seven-vertex graph. Verification route: exhaustive exact enumeration, normalized by translation, over every abelian group type at orders 10 through 14, plus independent all-pairs verification of any returned labeling and the explicit order-15 certificate. The search space and verifier are bounded, so the lead is suitable to advance.
