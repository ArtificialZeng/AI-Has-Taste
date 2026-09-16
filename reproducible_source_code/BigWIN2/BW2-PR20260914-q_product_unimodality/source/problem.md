# Precise problem and triage scope

Source: Connelly, Ito, Martinez, Shevchenko, Yang, *Unimodality of q-Fibonomial coefficients for small cases*, arXiv:2605.12822v1, Conjecture 5.4, Section 5.2, printed/PDF page 14. The verbatim source is `source.md`; intake SHA-256: `cbf595d1573adcefa915d3dff46245f4b318bfc3ba73c49912bdc9ca5f7fe8c8`.

For every integer \(r\ge2\), every integer \(k\ge1\), and all positive integers \(a_1,\ldots,a_k,b\), put
\[
[a]_q=\sum_{j=0}^{a-1}q^j,\quad [b]_{q^r}=\sum_{j=0}^{b-1}q^{rj},\quad
P(q)=\prod_{i=1}^k[a_i]_q[b]_{q^r}=\sum_{n=0}^D c_nq^n,
\quad D=\sum_i(a_i-1)+r(b-1).
\]
Here \(q\) is a formal indeterminate. Weak coefficient unimodality means that some integer \(m\in[0,D]\) satisfies \(c_0\le\cdots\le c_m\ge\cdots\ge c_D\). Every integer degree counts, including zero coefficients. Set
\[
C:\quad (\exists i\in\{1,\ldots,k\}:r\mid a_i)\ \lor\ 
\left(b\le1+\sum_i\lfloor a_i/r\rfloor\right).
\]
The original assertion is the conjunction of:

1. For all parameters above, \(C\Rightarrow P\) is unimodal.
2. For all parameters above satisfying \(k\le3\) **or** \(r\le3\), unimodality implies \(C\).

The disjunction is inclusive. Factors \(a_i=1\), and \(b=1\), are allowed. All factors are symmetric, so \(c_n=c_{D-n}\); consequently unimodality is equivalent to \(c_n-c_{n-1}\ge0\) for \(1\le n\le\lfloor D/2\rfloor\). Multiplication by \([1]_q\) does not alter the polynomial, but the original quantifiers remain unchanged.

## Nearest verified prior results

The live [primary paper](https://arxiv.org/html/2605.12822v1#S5.SS2) and saved PDF text were inspected on 2026-09-14. Proposition 5.3 (pp. 13–14) proves the full \(k=1\) case; Corollary 4.3 (p. 10) proves the divisibility branch for every \(k\); Proposition 4.5 (pp. 11–12) proves \(k=2,r=2\). Lemma 4.1 gives the trapezoidal coefficients of two ordinary q-integers. For nondivisible odd factors Proposition 4.5's condition is exactly the floor-sum condition here. The full assertion is labeled a conjecture; the source's finite tests are not a proof.

The source's \([3]_q^4[2]_{q^4}\) example is unimodal while \(C\) fails. Since \(k=r=4\), it violates neither implication. This problem is distinct from the general q-Fibonomial conjecture and the historical fixed \(n=4\) Fibonomial quotient lead.

Source status: **open-supported** by the inspected primary text; no later full resolution found in this bounded search, without a priority guarantee. The observed v1 submission date (2026-05-12), saved PDF date (2026-05-14), and saved/live HTML date (2026-08-24) are distinct metadata fields. The research pass independently checked the date discrepancy and the agreement of the decisive mathematical statements; the immutable source text has not been edited. Historical comparison is limited to supplied `literature/dedup.json` and `literature/screen.md`; full underlying registries and live conversations are unavailable inside this project.

## Proposed contribution and verifier

Nearest prior result: Proposition 4.5 handles two ordinary factors and stretch 2. Research pass 1 submits the following exact restricted theorem for fresh review: for all integers \(r\ge2\) and positive integers \(a,c,b\), \([a]_q[c]_q[b]_{q^r}\) is weakly unimodal if and only if \(r\mid a\), or \(r\mid c\), or \(b\le1+\lfloor a/r\rfloor+\lfloor c/r\rfloor\). This is the full \(k=2\) restriction and does not resolve the original all-parameter conjunction.

The complete proposed proof is `evidence/k2-characterization.md`. The interval inequality left by triage is now proved using floor subadditivity and midpoint constraints, and both sufficiency and the explicit necessity witness are included. The proof also covers divisibility and factor-1 cases without external mathematical assumptions. `evidence/research_verify.py` and `evidence/research-verification.json` give exact finite checks by dense convolution and a separate inclusion-exclusion coefficient formula; computation is not used as an infinite proof. `literature/research-k2-comparison.md` records the bounded current comparison and its limits. No independent mathematical acceptance or priority guarantee is claimed.

The decisive complete primary PDF, text, and HTML are retained as `evidence/external/2605.12822v1.pdf`, `evidence/external/2605.12822v1.txt`, and `evidence/external/2605.12822v1.html`; they agree byte-for-byte with the supplied captures. A fresh PDF extraction was matched exactly to the retained text; details are in `evidence/primary-source-retention.json`. These files are inputs for review, not research manuscripts.
