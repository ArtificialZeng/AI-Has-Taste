# Precise reading and triage target

Provenance: `bigMac-00014-p01-triage-528e5256d151`.  The immutable
statement is `source.md`; this file fixes its mathematical reading and does
not replace or amend it.

## Objects, quantifiers, and probability

For every integer \(N\ge 2\), write \([N]=\{1,\ldots,N\}\) and let
\(\mathbf 1_N\in\mathbb R^N\) be the all-ones vector.  Define
\[
 \mathcal M_{N,2}=\{A\in\{0,1\}^{N\times N}:
 A\mathbf 1_N=2\mathbf 1_N,\ A^{\mathsf T}\mathbf 1_N=2\mathbf 1_N\}.
\]
Thus every row and every column contains exactly two ones.  Binary entries
exclude multiple edges.  Diagonal ones are permitted (self-loops in the
directed-graph interpretation); no conditioning on a zero diagonal is made.
Let \(A_N\) have the uniform law on this finite nonempty set, and put
\[
 p_N:=\mathbb P(\det A_N\ne0)
     =\frac{|\{A\in\mathcal M_{N,2}:\det_{\mathbb Z}A\ne0\}|}
            {|\mathcal M_{N,2}|}.
\]
The exact part of the problem asks for \(p_N\) for every \(N\ge2\), including
all exceptional small values, not merely an eventual or numerical formula.

## Permutation formulation that must be justified

For \(q\in S_N\), let \(c_k(q)\) be its number of \(k\)-cycles and
\(c(q)=\sum_kc_k(q)\).  Under the Ewens law with parameter \(1/2\),
\[
 \mathbb P(q)=\frac{(1/2)^{c(q)}}{(1/2)(3/2)\cdots(N-1/2)}.
\]
Let
\[
 \mathcal D_N=\{q\in S_N:c_1(q)=0\},\qquad
 \mathcal O_N=\{q\in\mathcal D_N:c_{2j}(q)=0\text{ for every }j\ge1\}.
\]
Thus \(\mathcal O_N\) consists exactly of permutations whose cycles all have
odd length at least three.

He--Huang, arXiv:2609.05297v1, Lemma 6.2 (one-based PDF p. 36), proves that if \(P\)
is a uniform permutation matrix and the independent permutation matrix \(Q\)
has Ewens\(_N(1/2)\) law conditioned on \(c_1(Q)=0\), then
\(P(I+Q)\) is uniform on \(\mathcal M_{N,2}\).  Application to the present
problem still has to prove explicitly that
\[
 \det(P(I+Q))\ne0\quad\Longleftrightarrow\quad Q\in\mathcal O_N.
\]
Equivalently, one must decompose the permutation matrix into cycle blocks and
show that \(-1\) is an eigenvalue of a cycle block exactly when that cycle has
even length.  This reduction is a required claim, not an assumption.

## Exact coefficient identity to be proved

For a formal power series, let \([z^N]\) denote coefficient extraction.  Set
\[
 D(z):=\exp\!\left(\frac12\sum_{k\ge2}\frac{z^k}{k}\right)
      =e^{-z/2}(1-z)^{-1/2},
\]
\[
 H(z):=\exp\!\left(\frac12
             \sum_{\substack{k\ge3\\k\ \mathrm{odd}}}\frac{z^k}{k}\right)
      =e^{-z/2}\left(\frac{1+z}{1-z}\right)^{1/4},
\]
where the fractional powers are the branches represented by their formal
series at \(z=0\).  The precise candidate exact answer is
\[
 \boxed{\displaystyle p_N=\frac{[z^N]H(z)}{[z^N]D(z)}}\qquad(N\ge2). \tag{*}
\]
The exponential-formula weights are \((1/2)^{c(q)}\), and the common factor
\(N!\) cancels in the ratio.  Both this weighted enumeration and its link to
the uniform matrix law must be proved; formula (*) is presently the research
target, not a triage-certified theorem.

## Asymptotic deliverable

The phrase “complete first-order asymptotic” is read as requiring an exact
leading equivalent and a rigorous error estimate.  In addition, the source
explicitly requires the singularity at \(z=-1\) to be analyzed rather than
discarded.  The two-singularity calculation suggested by (*) gives the
specific target
\[
 p_N=\frac{2^{1/4}\sqrt\pi}{\Gamma(1/4)}N^{-1/4}
 +(-1)^N\frac{e\sqrt\pi\,2^{-1/4}}{\Gamma(-1/4)}N^{-3/4}
 +O(N^{-5/4}). \tag{**}
\]
In particular, the requested leading constant would be
\(2^{1/4}\sqrt\pi/\Gamma(1/4)\).  Equation (**) is a candidate to prove, not
an established result: a valid solution must derive the \(z=1\) term, derive
and sign-check the oscillatory \(z=-1\) term, control the remainder, and
justify division by \([z^N]D(z)\).

## Scope and triage status

The target is solely the unshifted determinant in the loops-allowed model
\(\mathcal M_{N,2}\).  It makes no claim about the zero-diagonal model
\(\mathcal M^0_{N,2}\), shifted determinants, smallest singular values, or a
spectral limiting law.  The nearest verified prior result is the model
definition on one-based PDF p. 6 and the Ewens representation in Lemma 6.2 on one-based PDF p. 36 of
arXiv:2609.05297v1 (retrieved 2026-09-07 from
`https://arxiv.org/pdf/2609.05297`).  The inspected portion does not state (*)
or (**).  The exact-result/open/novelty status remains **status-uncertain**;
the limited triage search is not evidence of priority.

Triage target: nearest result = He--Huang Lemma 6.2; proposed delta = prove
(*) for every \(N\ge2\) and (**) with exact constants; verification route =
exact small-\(N\) enumeration followed by a cycle-block determinant proof,
the weighted permutation exponential formula, and singularity analysis at
both \(1\) and \(-1\).


## Research-pass clarification (2026-09-08)

The preceding target formulas preserve the original interpretation. A complete
proposed proof is now in `evidence/proof.md`, pending fresh mathematical review.
It proves the exact ratio (*) and the stronger expansion
\[
 p_N=C_0N^{-1/4}+(-1)^{N+1}C_1(N^{-3/4}+N^{-7/4})+O(N^{-9/4}),
\]
where \(C_0=2^{1/4}\sqrt\pi/\Gamma(1/4)\) and
\(C_1=e\sqrt\pi/(2^{9/4}\Gamma(3/4))\). This implies (**), because
\(\Gamma(-1/4)=-4\Gamma(3/4)\). The exact small cases are p_2=p_4=0,
p_3=1, and 0<p_N<1 for every N>=5. No scope change is made.

The He--Huang page numbers above are now corrected to one-based PDF pages
6 and 36; the page-number errors in immutable `source.md` remain untouched.
The determinant cycle criterion itself is already explicit in Li--Lin--Rodman,
*Determinants of Certain Classes of Zero-One Matrices with Equal Line Sums*
(1999), Theorem 3.1 and its proof. The nearest primary boundaries are therefore
that older determinant classification and He--Huang's conditional Ewens law.
The proposed delta is the uniform probability count and its parity-sensitive
asymptotic, not a new cycle determinant criterion. See
`literature/research_comparison.md` for current primary-source checks and
bounded novelty language. The historical triage status above does not certify
or reject the new research candidate.
