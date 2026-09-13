# Precise reading of bigMac-00011-p03

## Frozen source and provenance

- Job: `bigMac-00011-p03-triage-a8d466ebee0b`.
- The immutable statement is `source.md` (SHA-256
  `c1b138ca46b1461350f7d08629d515228c1181f53fc0c7a54349d60ef6bb06a5`).
- The primary input is Baolahy--Randrianirina, arXiv:2609.05010v1,
  especially Remark 3.2 and Open Problem 5.1. The inspected PDF has SHA-256
  `8e4ec54dde6f55666109cc6e4a0323ea8a548115eaa459306c229bb5fb43676e`.
  Record: <https://arxiv.org/abs/2609.05010> (retrieved 2026-09-07).

## Objects and conventions

Let \(S_4\) act on \([4]=\{1,2,3,4\}\). For a partition
\(\lambda=(\lambda_1,\ldots,\lambda_k)\vdash4\), put
\(s_i=\lambda_1+\cdots+\lambda_i\) and take the disjoint standard cycles

\[
c_i=(s_{i-1}+1\;s_{i-1}+2\;\cdots\;s_i),
\]

with a one-cycle contributing the trivial group. The convention frozen by
`source.md` is the **independent-row convention**

\[
G_\lambda=\langle c_1\rangle\times\cdots\times\langle c_k\rangle\le S_4,
\qquad K_\lambda=X^4/G_\lambda.
\]

Thus each cyclic factor may rotate its block independently. In particular,

\[
H:=G_{(2,2)}=\langle(12)\rangle\times\langle(34)\rangle
=\{e,(12),(34),(12)(34)\}\cong C_2^2.
\]

For a four-element set \(U\),

\[
(X^4/L)[U]=\{fL:f:[4]\overset{\sim}{\longrightarrow}U\},
\]

with bijections of label sets acting by postcomposition. The product \(\times\)
is the Hadamard (Cartesian) product of species, evaluated pointwise.

The five requested indices are

\[
\lambda\in\{(4),(3,1),(2,2),(2,1,1),(1,1,1,1)\}.
\]

## Exact question and quantifiers

Determine the unique multiplicity, if it exists, for every \(\lambda\vdash4\),

\[
j^{\lambda}_{(2,2),(2,2)}\in\mathbb Z,
\]

such that the following is an equality (natural isomorphism) of species:

\[
K_{(2,2)}\times K_{(2,2)}
\cong\coprod_{\lambda\vdash4}
j^{\lambda}_{(2,2),(2,2)}K_\lambda.
\]

For an actual coproduct decomposition the nonzero coefficients must in fact be
nonnegative integers. Allowing integers means passage to the Grothendieck group;
it must not be used to hide a molecular summand whose stabilizer is not conjugate
to any \(G_\lambda\).

The decisive form of the question is the transitive-orbit decomposition

\[
X^4/H\times X^4/H
\cong\coprod_{HgH\in H\backslash S_4/H}
X^4/(H\cap gHg^{-1}).
\]

Accordingly, one must enumerate **all** double cosets, certify their completeness,
and determine the conjugacy class in \(S_4\) of every intersection
\(H\cap gHg^{-1}\). An expansion in the displayed five species exists exactly
when every resulting stabilizer is conjugate to some \(G_\lambda\).

Equality of species is the primary reading. Applying cycle indices gives a
necessary symmetric-function identity
\(Z_{K_{(2,2)}}\star Z_{K_{(2,2)}}=\sum j^\lambda Z_{K_\lambda}\),
which is an independent arithmetic check, not a substitute for the subgroup
certificate. If closure fails, the “correct minimal basis” means the distinct
transitive molecular species \(X^4/L\) for the stabilizer conjugacy classes that
actually occur. Any integral relations at cycle-index level must be stated
separately from species isomorphisms.

## Convention audit and nearest prior result

There is a material notation conflict. In the earlier paper *Species, Symmetric
Functions, and Kronecker Product* (arXiv:2604.10336v1; ECA 6:3 (2026), S2R19),
equal-length cycles are rotated diagonally: its definition gives
\(G_{(2,2)}=\langle(12)(34)\rangle\cong C_2\), not \(C_2^2\). Its basis and
closure statements therefore do not directly settle the frozen problem. The
later arXiv:2609.05010v1 explicitly uses independent shifts in Remark 3.2 and
Open Problem 5.1, and `source.md` removes the ambiguity by explicitly requiring
\(C_2^2\). Records inspected 2026-09-07:
<https://arxiv.org/html/2604.10336v1>, Definition 3.3 and Proposition 5.7, and
<https://ecajournal.kms-ks.org/Volumes.html>, volume 6 issue 3.

Nearest prior machinery: the standard molecular-species/Mackey double-coset
formula above (also Proposition 2.2 of arXiv:2604.10336v1). Proposed delta: the
complete first independent-row noncyclic case \(H=C_2^2\). Verification route:
exact enumeration in \(S_4\), an elementary normalizer/conjugate-subgroup proof,
and an exact power-sum cycle-index check.

No general formula for arbitrary \(\alpha,\beta\), no numerical-only character
calculation, and no claim of novelty or priority is within this job's scope.
