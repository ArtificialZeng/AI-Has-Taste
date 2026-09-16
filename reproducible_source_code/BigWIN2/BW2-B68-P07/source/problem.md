# Precise problem statement

## Frozen source and convention

`source.md` is the immutable source record (SHA-256
`fd372110ceb5d92c5c134bc70354af09f46731ff1e3866c04dfe2edbb257e7bf`).
The convention below is the literal **independent-row** convention in Remark 3.2
and Open Problem 5.1 of arXiv:2609.05010v1; it is not the repeated-part
diagonal convention of Definition 3.3 in arXiv:2604.10336v1.

Let \(n\geq 1\), and let \(\alpha=(a_1,\ldots,a_k)\vdash n\). Put
\(s_i=a_1+\cdots+a_{i-1}\) and let
\(c_i=(s_i+1\;s_i+2\;\cdots\;s_i+a_i)\in S_n\), with a 1-cycle
understood as the identity. Define
\[
  G_\alpha=\langle c_1\rangle\times\cdots\times\langle c_k\rangle
  \leq S_n.
\]
The factors have disjoint supports, so this is an internal direct product (trivial
factors are harmless). In particular,
\(G_{(2,2)}=\langle(12),(34)\rangle\), not
\(\langle(12)(34)\rangle\).

For \(H\leq S_n\), write \(X^n/H\) for the molecular species whose structures
on an \(n\)-element set are the corresponding cosets, with transport by
relabeling. Set \(\mathbf K_\alpha=X^n/G_\alpha\). The Hadamard product is
pointwise Cartesian product:
\((F\times G)[U]=F[U]\times G[U]\), with the diagonal transport action.
Its cycle index satisfies
\[
 Z_{X^n/H}=\frac1{|H|}\sum_{h\in H}p_{\operatorname{type}(h)},
 \qquad Z_{F\times G}=Z_F\star Z_G,
\]
where \(p_\lambda\star p_\mu=\delta_{\lambda\mu}z_\lambda p_\lambda\).

## Quantified assertions to decide

The degree-four claim is that there do **not** exist coefficients
\(m_\lambda\in\mathbb Z_{\geq0}\), indexed by \(\lambda\vdash4\), such that
\[
 \mathbf K_{(2,2)}\times\mathbf K_{(4)}
 \cong \coprod_{\lambda\vdash4}m_\lambda\mathbf K_\lambda.
\]
Equivalently for the intended proof route, once
\(\{Z_{\mathbf K_\lambda}:\lambda\vdash4\}\) is proved linearly independent,
the unique expansion of
\(Z_{\mathbf K_{(2,2)}}\star Z_{\mathbf K_{(4)}}\) in that basis has a
negative coefficient. The proposed, presently unaudited identity is
\[
 Z_{\mathbf K_{(2,2)}}\star Z_{\mathbf K_{(4)}}
 =2Z_{\mathbf K_{(2,2)}}-2Z_{\mathbf K_{(2,1,1)}}
  +2Z_{\mathbf K_{(1,1,1,1)}}.
\]

"Degree four is first" means both: (i) for every \(n\in\{1,2,3\}\) and every
\(\alpha,\beta\vdash n\), the species
\(\mathbf K_\alpha\times\mathbf K_\beta\) is a nonnegative integral sum of the
\(\mathbf K_\lambda\); and (ii) the displayed degree-four pair fails this
property. No statement is made about a closed formula in a larger molecular
species basis, nor about every aspect of Open Problem 5.1.

## Prior-results boundary (checked 2026-09-09)

- Baolahy--Randrianirina, arXiv:2609.05010v1, Remark 3.2 and Open Problem 5.1,
  explicitly give the independent-row group and ask for a closed-form expansion
  for its products. This supports the convention and motivates the question, but
  does not prove the degree-four obstruction.
- Baolahy--Benjamin, arXiv:2604.10336v1, Definition 3.3, Proposition 4.2,
  Proposition 5.7 and Corollary 5.5, prove basis/closure statements for a group
  with one diagonal cyclic factor for each *distinct* part size. For repeated
  parts that group differs from the one above, so those conclusions cannot be
  transferred to \(G_{(2,2)}\) without a new argument.
- Primary-source URLs inspected: <https://arxiv.org/html/2609.05010v1> and
  <https://arxiv.org/abs/2604.10336>. The two cited local PDFs match the hashes
  frozen in `source.md`. A narrow exact/equivalent-phrase search found no primary
  source already stating this degree-four calculation; this is only a limited
  search result, not a priority or openness claim. Source status is therefore
  `new-question` / literature status uncertain, rather than a verified open
  theorem.

## Proposed contribution and verification route

Nearest prior result: positive closure for the distinct-part diagonal convention.
Proposed delta: an exact smallest-degree obstruction for the newer independent-row
convention. Verification route: exhaustive exact permutation arithmetic through
degree four, double-coset/intersection certificates, exact cycle-index linear
algebra, and an independent replay.
