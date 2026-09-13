# Precise problem reading

Provenance: `bigMac-00011-p02-triage-72084db0453e` (triage, 2026-09-07).
This file interprets the immutable statement in `source.md`; it does not amend it.

## Objects and map

Let \(\Sigma=\{U,D\}\).  For \(n\ge 0\), let
\[
\mathcal D_n=\{w\in\Sigma^{2n}:h_w(k)\ge0\ (0\le k\le2n),\ h_w(2n)=0\},
\qquad
h_w(k)=\#_U(w_1\cdots w_k)-\#_D(w_1\cdots w_k),
\]
and put \(\mathcal D=\bigcup_{n\ge0}\mathcal D_n\).  Input and output use this
step-word encoding.

An admissible weight pair is
\[
(u,d)\in\mathbb Z^2,\qquad |u|,|d|\le2,\qquad \gcd(|u|,|d|)=1,
\]
with the convention \(\gcd(a,0)=a\).  Thus \((0,0)\) is excluded and the
admissible pairs are exactly
\[
\begin{split}
W=\{&(1,1),(1,-1),(-1,1),(-1,-1),\\
&(1,2),(1,-2),(-1,2),(-1,-2),\\
&(2,1),(2,-1),(-2,1),(-2,-1),\\
&(1,0),(-1,0),(0,1),(0,-1)\}.
\end{split}
\]

Fix \((u,d)\in W\), write \(\nu(U)=u\) and \(\nu(D)=d\), and let
\(w=w_1\cdots w_N\in\Sigma^*\).  Position \(i\) has starting level
\[
\ell_{u,d}^w(i)=\sum_{1\le j<i}\nu(w_j).
\]
There are two tie orders.  For \(t=L\), order positions by the lexicographic
key \((\ell(i),i)\); for \(t=R\), order them by \((\ell(i),-i)\).  If
\(i_1,\ldots,i_N\) is the resulting increasing order, define
\[
\Phi_{u,d}^{t}(w)=w_{i_1}\cdots w_{i_N},
\qquad \Phi_{u,d}^{t}(\varepsilon)=\varepsilon.
\]
Thus levels increase first, and an equal-level block is read left-to-right
for \(L\) or right-to-left for \(R\).  This is Definition 5.2 of the primary
source with its “scan direction” made explicit.

## Quantified classification target

For every one of the \(16\cdot2=32\) labeled triples \((u,d,t)\in
W\times\{L,R\}\), decide whether the restriction
\(\Phi_{u,d}^t\!\upharpoonright_{\mathcal D}:\mathcal D\to\Sigma^*\) is
polyregular in the source's realization sense:

* **positive** means that there is a partial polyregular map
  \(T:\Sigma^*\rightharpoonup\Sigma^*\) with
  \(\mathcal D\subseteq\operatorname{dom}(T)\) and
  \(T(P)=\Phi_{u,d}^t(P)\) for every \(P\in\mathcal D\);
* **negative** means that no such \(T\) exists.

The quantifier ranges over all semilengths, including \(n=0\).  Behavior of a
realizing transducer away from \(\mathcal D\) is unconstrained.  The output is
not required to be a Dyck word, and injectivity, surjectivity, and preservation
of any Catalan statistic are not part of the target.

Every positive entry must include a finite explicit polyregular presentation
(an equivalent explicit 2DFT/MSO transduction is sufficient) and a proof of
agreement on every Dyck input.  Every negative entry must include a complete
lower bound, such as a regular-language pumping obstruction after the
linear-growth collapse or a rigorously applicable semilinearity obstruction.
Finite testing, or failure of a proposed transducer, settles no entry.  A
complete deliverable is a table covering all 32 labeled triples; a reduced
table is acceptable only when every omitted entry is recovered by a proved
conjugacy identity.

## Symmetry convention

Let \(\bar L=R\), \(\bar R=L\), and let
\(\operatorname{rev}(a_1\cdots a_N)=a_N\cdots a_1\).  Directly from the two
sorting orders, on every word
\[
\Phi_{-u,-d}^{t}=\operatorname{rev}\circ
\Phi_{u,d}^{\,\bar t}.
\]
Since output reversal is an invertible regular transduction, the two sides
have the same polyregular-realizability status.  Consequently the proved
negation reduction acts on labeled cases as
\((u,d,t)\mapsto(-u,-d,\bar t)\), not merely on the weight pair while silently
holding the tie order fixed.

The phrase “the evident word-reversal symmetry” in `source.md` does not specify
an action on \((u,d,t)\).  Plain reversal does not preserve the Dyck language;
reverse-complement does preserve it but changes starting levels into
suffix/ending-level expressions.  To avoid guessing a materially different
claim, the frozen reading above requires all 32 labeled cases.  Any further
symmetry reduction must first state and prove an exact identity using regular
input/output bijections that preserve the Dyck domain.

## Nearest prior result and proposed delta

The inspected primary PDF is arXiv:2609.05005v1 (4 September 2026), SHA-256
`b55c4a261469e318c2058e0461ef2440a012243800b16ac07077e420c1067a66`.
Its Definition 5.2 is the map above; Proposition 5.3 places every additive
level sort in \(\mathrm{sRR}_1\subseteq\mathrm{WRP}\); Open Problem 11(4) asks
which are polyregular.  It records \((u,d)=(1,1)\) as the identity and Theorem
6.5 proves the right-to-left height sort \(\Phi_{1,-1}^{R}\) non-polyregular on
the Dyck domain.  The proposed delta is the complete bounded-weight table,
not a claim that this broader open problem has been classified.

There is a bibliographic error in the immutable source: the inspected PDF's
first page names Jineon Baek, Byung-Hak Hwang, Joonhyun La, and Hongseok Yang,
not “Zeng and Kim.”  The title, arXiv identifier, hash, definitions, and open
problem otherwise identify the intended primary document.  This correction is
bibliographic and does not alter the mathematical statement.
