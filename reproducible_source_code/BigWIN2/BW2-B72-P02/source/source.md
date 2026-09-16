# win-00072-p02 — Reversible Gray representatives in the Gamma_34 orbit of an explicit qLP

## Immutable primary-source record

- Main source: Nikita Lebedev, *Quaternary Legendre Pairs of Lengths 42, 46, 52, 58, 66, 72, and 80*, arXiv:2609.04589v1 [math.CO], 4 September 2026.
- Official abstract: <https://arxiv.org/abs/2609.04589v1>.
- Official PDF: <https://arxiv.org/pdf/2609.04589v1>.
- Main-source locations: qLP definition in equation (1), printed p.1; Gray map, Lemma 3, Proposition 4, and reversibility in printed p.4; the length-34 discussion and explicit disclaimer of a full-orbit argument in printed p.8; literal words in Appendix A, printed p.12.
- Supporting primary definitions: I. S. Kotsireas and A. Winterhof, *Quaternary Legendre Pairs*, arXiv:2212.10953v1, printed p.4; D. Bulutoglu, D. Baczkowski, and J. Yauney, *Determining the group that sends each Legendre pair to an equivalent Legendre pair*, arXiv:2604.22423v1, printed pp.2–3, equations (1.2)–(1.5).
- Access record: official PDFs were inspected on 2026-09-08 and archived as bigWin-72-materials/2609.04589.pdf (SHA-256 e19270a04161256be4763baddcac7e8f61aa10a7c9a192bb5de73e958512ca51), 2212.10953.pdf (SHA-256 1f35e045dff6686322595a440a4e523073bbc5d50c3424e6ccfdc9a3554f5067), and 2604.22423.pdf (SHA-256 62090f618bfcfa9d005fa3ab9507b0bbd4a11bd8b2e3812d4fd1f7b5f67280bb).

## Fixed words and conventions

Map Appendix-A digits \(0,1,2,3\) to \(1,i,-1,-i\), respectively. Fix the length-34 pair
\[
A=2202202000022020222202000220200020,
\qquad
B=1133303133112311101113211331303331.
\]
All indices below lie in \(\mathbb Z_{34}\). For a sequence \(x\), set
\[
(c_rx)_j=x_{j-r},\qquad (d_kx)_j=x_{jk^{-1}}
\]
for \(r\in\mathbb Z_{34}\) and \(k\in\mathbb Z_{34}^{\times}\).

Define \(\Gamma_{34}(A,B)\) to be the finite set of all pairs
\[
s^e\!\left(\alpha\,c_r d_k(A^\varepsilon),
            \beta\,c_t d_k(B^\varepsilon)\right),
\]
where
\[
\alpha,\beta\in\{1,i,-1,-i\},\quad
r,t\in\mathbb Z_{34},\quad
k\in\mathbb Z_{34}^{\times},\quad
\varepsilon,e\in\{0,1\}.
\]
Here \(A^0=A\), \(A^1=\overline A\), likewise for \(B\), and \(s\) exchanges the two sequences.

Independent phases and shifts, common decimation, simultaneous conjugation, and pair exchange each preserve the qLP equations by direct calculation. This definition deliberately does not claim to be the largest possible equivalence group. In particular, the asynchronous binary-LP decimation alternative in arXiv:2604.22423 equation (1.5) is not imported without a qLP proof.

For \(p,q,r',s'\in\{\pm1\}^{34}\), the Gray decoding is
\[
A'=\frac{p+q}{2}+i\frac{p-q}{2},
\qquad
B'=\frac{r'+s'}{2}+i\frac{r'-s'}{2}.
\]
A decoded binary row \(x\) is reversible when \(x_j=x_{-j}\) for every
\(j\in\mathbb Z_{34}\).

## Frozen assertion

Decide whether \(\Gamma_{34}(A,B)\) contains a pair whose four Gray rows are all reversible.

Both answers must be literal finite-orbit statements under the displayed definition. A negative answer must not be described as proving non-reversibility under every conceivable qLP equivalence.

## Nearest result and precise delta

The main source verifies that the printed orientation of \((A,B)\) is not reversible. It explicitly says that concluding the pair lies outside the reversible equivalence class would require an orbit argument that it does not carry out.

The proposed delta is the complete yes/no decision for the explicitly frozen
\(\Gamma_{34}\) orbit. There are at most
\[
2\cdot16\cdot34^2\cdot16\cdot2=1{,}183{,}744
\]
parameter images before deduplication.

This differs from win-00063-p11, which asks unrestricted qLP existence at length 64 and was parked because the full space is far larger than the source's reversible search queue.

## Cheapest decisive attack and certificate contract

Enumerate every displayed parameter tuple, decode the resulting pair into four Gray rows, and test all reflection identities exactly.

- A positive certificate is the concrete reversible pair, its seven parameters
  \((\alpha,\beta,r,t,k,\varepsilon,e)\), and a dependency-free checker of the qLP and reflection equations.
- A negative certificate needs the complete parameter-domain count, a canonical deduplication rule and orbit digest, and for every canonical image a deterministic witness consisting of a Gray-row label and the least index \(j\) where \(x_j\ne x_{-j}\). An independent verifier must reconstruct the full domain and digest.
- The worker must also prove on paper that every generator in the frozen definition preserves the qLP equations and that its enumeration covers the entire displayed parameter set.

## Novelty and value risks

- The result concerns presentation/reversibility of one known qLP, not qLP existence.
- The author used the phrase “full equivalence group” informally, while the present project freezes a named safe group. The manuscript must state this distinction prominently.
- If \(\Gamma_{34}\) omits a field-standard operation essential to the mathematical question, or if the orbit decision reduces to an immediate invariant already in the literature, fresh referee should reject publication and retain only the exact audit asset.

## Semantic boundary

No registered project concerns the length-34 witness orbit, its Gray-row reversibility, or the displayed \(\Gamma_{34}\). The only same-source neighbor is win-00063-p11 at length 64 with different object and quantifier.
