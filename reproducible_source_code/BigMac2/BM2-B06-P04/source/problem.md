# Precise problem statement

Provenance: `bigMac-00006-p04-triage-104c376d6da8`.

The immutable wording is in `source.md`.  The mathematical reading below uses
Gerber--Norton's conventions in arXiv:2609.03738v1.

## Definitions

- A partition is a weakly decreasing sequence
  \(\lambda=(\lambda_1,\lambda_2,\ldots)\) of nonnegative integers with finite
  support.  A bipartition is an ordered pair
  \(\boldsymbol\lambda=(\lambda^{1},\lambda^{2})\), with
  \(|\boldsymbol\lambda|=|\lambda^{1}|+|\lambda^{2}|\).
- A charge is an ordered pair \(\mathbf s=(s_1,s_2)\in\mathbb Z^2\).  For a
  partition \(\lambda\) and \(s\in\mathbb Z\), define its shifted symbol (beta
  set)
  \[
    S(\lambda,s)=\{\lambda_k-k+1+s:k\geq1\}\subset\mathbb Z.
  \]
- For the charges occurring here, the source's Definition 2.14 and Lemma 2.11
  give the following equivalent, self-contained criterion: a bipartition
  \(\boldsymbol\lambda\) is an \((e,\mathbf s)\)-core exactly when
  \[
    S(\lambda^{1},s_1)\subseteq S(\lambda^{2},s_2)
    \subseteq S(\lambda^{1},s_1+e).
  \]
  Let \(\mathcal C^2_{e,\mathbf s}\) denote the set of all such bipartitions.
- With \(q\) a formal indeterminate, define
  \[
    \mathsf c_{e,\mathbf s}(q)
      =\sum_{\boldsymbol\lambda\in\mathcal C^2_{e,\mathbf s}}
        q^{|\boldsymbol\lambda|}
      =\sum_{n\geq0}c_{e,\mathbf s}(n)q^n.
  \]
  Thus \(c_{e,\mathbf s}(n)\) is the finite, nonnegative integer counting
  \((e,\mathbf s)\)-core bipartitions of size \(n\), and
  \([q^n]\mathsf c_{e,\mathbf s}(q)=c_{e,\mathbf s}(n)\).

## Frozen claim, made explicit

Prove or disprove the conjunction
\[
 \forall n\in\mathbb Z_{\geq0}:\quad
 \left(\exists\boldsymbol\lambda\in\mathcal C^2_{6,(0,1)},
              |\boldsymbol\lambda|=n\right)
 \ \land\ 
 \left(\exists\boldsymbol\mu\in\mathcal C^2_{6,(0,3)},
              |\boldsymbol\mu|=n\right).
\]
Equivalently, both \(c_{6,(0,1)}(n)>0\) and
\(c_{6,(0,3)}(n)>0\) must hold for every integer \(n\geq0\).  The witnesses
for the two charges need not be the same bipartition.  A disproof needs one
exact \(n\) for which either count is zero; proving only one branch does not
resolve the conjunction.

The boundary case \(n=0\) is included.  The empty bipartition is the unique
bipartition of size zero and satisfies both nesting criteria, so both constant
coefficients equal \(1\).

## Source validation and known scope

The primary source was inspected on 2026-09-06 in both its v1 PDF and arXiv
HTML: <https://arxiv.org/abs/2609.03738> and
<https://arxiv.org/html/2609.03738v1>.  It was submitted on 2026-09-03.

- Section 5 defines the generating series exactly as above.  Table 2 labels
  each of the two \(e=6\), level-two branches "conjecturally yes."
- The calculation leading to equation (5.3) was checked directly.  It first
  gives
  \[
    \mathsf z^2_{3,0}(q)
     =q\mathsf c_{6,(-1,4)}(q)+\mathsf c_{6,(0,3)}(q)
       +q\mathsf c_{6,(1,2)}(q)
     =\mathsf c_{6,(0,3)}(q)+2q\mathsf c_{6,(0,1)}(q),
  \]
  and hence
  \[
    \tag{5.3}
    \phi(q)\mathsf c_3(q)^2
      =\mathsf c_{6,(0,3)}(q)+2q\mathsf c_{6,(0,1)}(q),
  \]
  where \(\phi(q)=\sum_{a\in\mathbb Z}q^{a^2}\) and \(\mathsf c_3(q)\) is
  the ordinary 3-core partition generating function.  This identity proves
  positivity of the weighted sum, not of either summand separately.
- Immediately after (5.3), the authors say that separate positivity is
  equivalent to the \(e=6\) case of their Conjecture 3.10.  Near that
  conjecture they report computer support only.  Exact-assertion and equivalent
  arXiv searches on 2026-09-06 found no separate resolution.  This supports the
  triage label `open-supported`; it is not a priority claim.

Nearest prior result: equation (5.3) controls the sum of the two unknown
series, while the neighboring charge \((0,2)\) is proved coefficient-positive
in the same paper.  Proposed delta: separate the two summands and prove a
positive all-degree representation for each, or produce an exact missing
coefficient.  A suitable verifier is exact enumeration using the displayed
nested-symbol criterion, followed by coefficientwise verification of (5.3).

