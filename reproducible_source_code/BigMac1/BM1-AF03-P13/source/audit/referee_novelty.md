# Independent Referee and Novelty Audit

**Audit cut-off:** 2026-08-29 (Asia/Shanghai)  
**Role:** independent source/novelty referee  
**Isolation rule followed:** this audit was reconstructed from public sources and temporary downloads. I did not read the main research thread's discovery, certificate, formal-statement, status, or manuscript outputs.  
**Scope:** the still-open Ehrhart-root-location part of Lee--Vindas-Meléndez--Wang, Conjecture 5.1, with special attention to the corrected length-10 finite endpoint.

## Referee conclusion

1. The user's correction of the research boundary is source-supported: Braun--Jal, arXiv:2607.00922v1 (2026-07-01), explicitly proves **Conjecture 5.1(1)**, the real-rootedness of the generalized-snake $h^*$-polynomials. It does not state or prove Conjecture 5.1(2), the Ehrhart-root disk assertion.
2. Conjecture 5.1(2), as printed in arXiv v1, arXiv v2, and the journal version, is not internally consistent. There are two substantive errors:
   - the displayed disk “$|z-(n+4)/2|\le (n+2)/2$” has positive center, while the same sentence gives the negative axis $x=-(n+4)/2$ and Theorem 2.9 forces all relevant symmetry into the negative half-plane;
   - it says that the word has length $n+1$, whereas Definition 2.1 and Theorem 2.9 use $n$ for the length. Correcting only the sign would leave the forced root $-(n+4)$ of a length-$(n+1)$ word outside the claimed disk, so the indexing error is mathematically substantive, not cosmetic.
3. The consistent reparameterization is: for a word of actual length $m$, every zero $\rho$ of its Ehrhart polynomial should satisfy
   
   \[
   \boxed{\left|\rho+\frac{m+4}{2}\right|\le \frac{m+2}{2}.}
   \]
   
   Equivalently, if one insists on the printed phrase “length $n+1$,” replace the center/axis by $-(n+5)/2$ and the radius by $(n+3)/2$.
4. Therefore the corrected length-10 endpoint is unambiguous:
   
   \[
   \forall (w_1,\ldots,w_{10})\in\{L,R\}^{10},\quad
   \forall\rho\in\mathbb C,\quad
   L(\varepsilon w_1\cdots w_{10};\rho)=0
   \Longrightarrow |\rho+7|\le 6.
   \]
   
   Here $P(w)$ has $24$ elements, $\mathcal O(P(w))\subset\mathbb R^{24}$, the Ehrhart polynomial has degree $24$, and Theorem 2.9 forces the roots $-1,-2,\ldots,-13$.
5. I found no primary-source proof, counterexample, certified length-10 enumeration, or associated public code resolving this corrected endpoint by the cut-off date. This is a **bounded not-found conclusion**, not a proof of mathematical openness. The corrected length-10 test remains a legitimate research endpoint on the recorded search frontier.

## Primary-source frontier

### Original article and versions

- Eon Lee, Andrés R. Vindas-Meléndez, Zhi Wang, *Generalized snake posets, order polytopes, and lattice-point enumeration*.
  - arXiv abstract/version history: <https://arxiv.org/abs/2411.18695>
  - arXiv v1 HTML: <https://arxiv.org/html/2411.18695v1>
  - arXiv v2 HTML: <https://arxiv.org/html/2411.18695v2>
  - arXiv-issued DOI: <https://doi.org/10.48550/arXiv.2411.18695>
  - journal DOI: <https://doi.org/10.1016/j.disc.2026.115072>
  - publisher PII: `S0012365X26000968`; ScienceDirect landing page: <https://www.sciencedirect.com/science/article/pii/S0012365X26000968>
  - repository version of record: <https://escholarship.org/uc/item/6n85w7mx>
- Version history verified from arXiv/DataCite:
  - v1 submitted 2024-11-27 19:04:01 UTC;
  - v2 submitted 2026-02-27 02:24:52 UTC;
  - no v3 was present at the cut-off.
- Crossref metadata for the journal article records *Discrete Mathematics* **349** (2026), issue **9**, article/page **115072**, Elsevier BV, with print/issue date September 2026. Crossref created the DOI record on 2026-03-10 and records the version-of-record CC BY 4.0 licence as beginning on 2026-02-24, so the version of record was already public before the September issue date and this audit's cut-off. Elsevier metadata marks it open access and gives PII `S0012-365X(26)00096-8`. Crossref records no correction/update relation.
- The printed Conjecture 5.1 defects occur in both arXiv versions and in the publicly indexed journal-version text. Thus this audit does not silently substitute a corrected later author version.

### Braun--Jal

- Benjamin Braun, Aryaman Jal, *Order polytopes of generalized snake posets are $h^*$-real-rooted*.
  - arXiv v1/abstract: <https://arxiv.org/abs/2607.00922>
  - arXiv v1 HTML: <https://arxiv.org/html/2607.00922v1>
  - arXiv-issued DOI: <https://doi.org/10.48550/arXiv.2607.00922>
- At the cut-off, arXiv listed only v1, submitted 2026-07-01 13:24:51 UTC, 11 pages, with no journal DOI located in Crossref or the exact-title web search.
- Their Section 4 explicitly says it proves Lee--Vindas-Meléndez--Wang Conjecture 5.1(1). Theorem 4.1 proves real-rootedness together with prefix interlacing of the non-nesting rook polynomials. The paper contains no occurrence of the Ehrhart root disk, no treatment of Conjecture 5.1(2), and no claim that its interlacing theorem implies that disk bound.
- Notational warning: Braun--Jal use a $2(n+1)$-element width-two poset before adjoining the global minimum and maximum; Lee--Vindas-Meléndez--Wang's $P(w)$ has $2n+4$ elements. Braun--Jal explicitly note the adjoining operation. The $h^*$-result targets the original conjecture because adjoining a global extremum gives a lattice-pyramid operation and preserves $h^*$. It does **not** preserve the Ehrhart polynomial itself; one must not transfer an Ehrhart-root claim by merely identifying the $h^*$-polynomial.

### Other located subsequent work

- Akihiro Higashitani, Koji Matsushita, Koichiro Tani, *Khovanskii bases of subalgebras arising from finite distributive lattices*, arXiv:2501.05720v2: <https://arxiv.org/abs/2501.05720>. It cites arXiv:2411.18695 and uses generalized snake posets for a Khovanskii-basis characterization. It contains no Ehrhart-root-location result.
- Exact-phrase arXiv API search for `"generalized snake posets"` returned four records at the cut-off: the 2022 triangulations paper, the 2024/2026 Lee--Vindas-Meléndez--Wang paper, the 2025 Khovanskii-basis paper, and the 2026 Braun--Jal paper. Of these, only the last two postdate and cite/use the 2024 preprint; neither resolves the Ehrhart disk endpoint.
- Two very recent general $h^*$ papers located during the search—arXiv:2607.15886 and arXiv:2608.03635—contain no occurrence of “snake” and do not address Ehrhart-root location for this family.

## Reconstruction from the definitions

Let $m\in\mathbb Z_{\ge0}$. A generalized snake word is

\[
w=w_0w_1\cdots w_m=\varepsilon w_1\cdots w_m,
\qquad w_i\in\{L,R\}.
\]

Its **length is $m$**, the number of nonempty $L/R$ letters; the initial symbol $w_0=\varepsilon$ is not counted.

The poset is recursively defined as follows.

- $P(\varepsilon)$ has elements $\{0,1,2,3\}$ and cover relations
  
  \[
  1\prec0,\qquad 2\prec0,\qquad 3\prec1,\qquad3\prec2.
  \]
- At step $k\ge1$, obtain $P(w_0\cdots w_k)$ from $P(w_0\cdots w_{k-1})$ by adjoining $2k+2,2k+3$, with covers
  
  \[
  2k+3\prec2k+1,\qquad 2k+3\prec2k+2,
  \]
  
  and one additional cover
  
  \[
  \begin{cases}
  2k+2\prec2k-1,
  &k=1,\ w_k=L,\ \text{or }k\ge2,\ w_{k-1}w_k\in\{RL,LR\},\\
  2k+2\prec2k,
  &k=1,\ w_k=R,\ \text{or }k\ge2,\ w_{k-1}w_k\in\{LL,RR\}.
  \end{cases}
  \]

Consequently $P(w)$ has element set $\{0,1,\ldots,2m+3\}$, hence $2m+4$ elements; its minimum is $2m+3$, maximum is $0$, it is a width-two distributive lattice of rank $m+2$, and its order polytope is full-dimensional in $\mathbb R^{2m+4}$:

\[
\mathcal O(P(w))=
\{x\in[0,1]^{2m+4}:x_i\le x_j\text{ whenever }i<_{P(w)}j\}.
\]

For $q\in\mathbb Z_{\ge0}$, define

\[
L(w;q)=\#\bigl(q\mathcal O(P(w))\cap\mathbb Z^{2m+4}\bigr),
\]

and let $L(w;t)\in\mathbb Q[t]$ denote its unique polynomial continuation. It has degree $2m+4$ and $L(w;0)=1$.

Theorem 2.9, with $m$ denoting the actual word length, gives

\[
\prod_{j=1}^{m+3}(t+j)\mid L(w;t),
\qquad
L(w;t)=L(w;-m-4-t),
\]

and every integer zero lies in $[-m-4,0]$. Since $L$ has real coefficients, the functional identity plus complex conjugation makes the full zero multiset symmetric about

\[
\operatorname{Re}z=-\frac{m+4}{2}.
\]

The corrected disk

\[
D_m=\left\{z\in\mathbb C:
\left|z+\frac{m+4}{2}\right|\le\frac{m+2}{2}\right\}
\]

has real diameter $[-m-3,-1]$, exactly spanning the endpoints of the forced string of roots from Theorem 2.9. This compatibility is an additional internal check on the correction.

## Printed Conjecture 5.1: defect analysis

The source prints, in both v1 and v2 (and the journal text):

- “Let $w$ be a generalized snake word of length $n+1$”;
- all roots of $L(w;t)$ are in $|z-(n+4)/2|\le(n+2)/2$;
- “with axis of symmetry $x=(-n-4)/2$”;
- verified for words of length up to 9.

There are three notation observations:

1. **Wrong sign in the disk center (fatal if literal).** The disk as typeset is centered at $+(n+4)/2$, not at the negative axis named in the same sentence. It also cannot contain the already-proved negative integer roots.
2. **Off-by-one length (fatal if literal).** If the actual length is $n+1$, Theorem 2.9 forces $-1,\ldots,-(n+4)$ and gives center $-(n+5)/2$. Even after changing the minus sign in the disk to a plus sign, the printed disk would have real interval $[-n-3,-1]$, excluding the forced root $-(n+4)$. Thus the only coherent readings are:
   - change “length $n+1$” to “length $n$”; or
   - retain “length $n+1$” and change all disk/axis parameters by the same shift.
3. **Root-variable switch $t\to z$ (harmless).** The polynomial is written as $L(w;t)$, but a generic root is denoted $z$. This is ordinary bound-variable reuse, unlike the preceding two defects. In v1 there is also a parenthesis typo in $h^*(w;z)$, corrected in v2.

## Symmetry quotient warning

Remark 2.8 in the original article explicitly supports **letter complement**:

\[
\bar w:\ L\leftrightarrow R,
\qquad L(w;t)=L(\bar w;t).
\]

Thus complement quotienting is source-locked. The audited clauses do not explicitly establish the proposed **word reversal** quotient for Ehrhart polynomials. It may be true via an additional poset-duality/isomorphism or skew-board argument, but a finite exhaustive certificate must either:

- prove and independently verify $L(w;t)=L(w^{\mathrm{rev}};t)$, or
- avoid quotienting by reversal.

This warning does not affect the statement of the length-10 endpoint; it affects only whether an enumeration is complete.

## Public-code audit

- The arXiv v1 and v2 source bundles for 2411.18695 contain LaTeX, bibliography, and figures only. The paper says that examples/computations were done with Sage, but supplies no Sage script, repository URL, archive DOI, or code-availability statement.
- The arXiv source bundle for 2607.00922v1 contains `main.tex`, `bibliography.bib`, and arXiv metadata only; no computation code or Ehrhart-root verifier is included.
- GitHub repository searches for `generalized snake posets`, `2411.18695`, `2607.00922`, and `snake poset Ehrhart` returned zero repositories. General web searches restricted to GitHub also found no associated project. GitHub's unauthenticated **code** search endpoint returned HTTP 401, so private repositories and unindexed code, and code discoverable only through authenticated GitHub code search, were outside the audit.
- Web searches of Zenodo, OSF, and Figshare for the exact phrase found no record. No supplement link containing code was located on arXiv, the DOI record, or the repository record.
- A third-party generic `polynomial-tools` repository appeared in a broad search because it has an $h^*\leftrightarrow$ Ehrhart converter; it was not associated with either paper and did not constitute a published length-10 result.

Accordingly: **no associated public enumeration/certificate code was found within the recorded sources and query boundaries**.

## Novelty-lock decision

The frontier supported by primary sources at 2026-08-29 is:

- Conjecture 5.1(1): **solved** by Braun--Jal; out of scope for novelty claims.
- Conjecture 5.1(2), interpreted literally as printed: **malformed/trivially incompatible with Theorem 2.9**, so it must not be quoted without correction.
- Corrected all-length root-disk statement: no public proof or counterexample found.
- Corrected length-10 exhaustive statement $|\rho+7|\le6$: no public certified result found; it is the first length after the authors' reported verification through 9.

**Referee verdict:** proceed with exact length-10 research only under the corrected $m$-parameter statement above. Any eventual novelty claim must be re-searched immediately before release and must say “not found in the recorded searches” rather than claim absolute priority from database silence.

## Evidence integrity

Temporary source artifacts used in this audit had the following SHA-256 hashes:

- arXiv 2411.18695v1 PDF: `77549ea9d5a5d4a5424b8a6249605a8f0011d0f9e1d5ee3d5305b22829dfecb3`
- arXiv 2411.18695v2 PDF: `86defc823e76cc8b850a5bedef94e2012bd32ca3cbc1fd1b2c31918a09f04f53`
- arXiv 2411.18695v1 source: `a30646be5376bdb6e7f110d4b4c07d42ea5965140fdc438f7019abde347db30e`
- arXiv 2411.18695v2 source: `70f8c81c921f5c2534caf83fc9653e1d50306cb54b56abb227281d2b9054a2e5`
- arXiv 2607.00922v1 source: `eea3b6fcd050dbd765ba9df7f4ad98ae596953b664cb2a8e96034691658b199a`
- arXiv 2102.11306v2 source: `b6a836efbb5006272f1e4dc691360920aa82dd891e0f923b997f14f0c161ed69`

The detailed query record, failures, and not-found boundary are in `literature/referee_search_raw.md`.
