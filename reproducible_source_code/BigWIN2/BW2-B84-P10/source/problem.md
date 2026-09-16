# Precise problem reading

Provenance: triage job `win-00084-p10-triage-6ad645323685` (2026-09-09).
The frozen statement is `source.md`, whose SHA-256 at intake was
`4b1056ed0d2c409f9cc07de953b852ea0dea8b612228770e77593f7baa1ebd69`.

## Objects and quantifiers

Fix an integer `n >= 3`. For an integer top row
\(S=(s_1,\ldots,s_n)\in\mathbb Z^n\), define

\[
s_a^0=s_a,\qquad
s_a^b=\lvert s_{a+1}^{b-1}-s_a^{b-1}\rvert
\quad(1\le b\le n-1,\ 1\le a\le n-b).
\]

The sequence is **Gilbreath** precisely when
\(s_1^b=1\) for every \(b=1,\ldots,n-1\). Define

\[
\mathcal G_n=\{S\in\mathbb Z^n:
2=s_1<s_2=3<s_3<\cdots<s_n,
\ s_1^b=1\ (1\le b\le n-1)\}.
\]

For \(S\in\mathcal G_n\), its full two-sided valid-extension set is

\[
K_S=\{k\in\mathbb Z:(s_1,\ldots,s_n,k)\text{ is Gilbreath}\}.
\]

The appended integer is quantified over all of \(\mathbb Z\): it need not be
positive, distinct from an earlier entry, or larger than \(s_n\). In
particular, the target concerns \(|K_S|\), not the increasing-extension subset
\(K_S^+=\{k\in K_S:k>s_n\}\).

The requested classification is therefore a family of explicit finite or
parametric templates \(\mathcal T_n\), valid for every integer \(n\ge3\), with

\[
\forall n\ge3\ \forall S\in\mathbb Z^n:\qquad
S\in\mathcal T_n
\iff
\bigl(S\in\mathcal G_n\ \text{and}\ |K_S|\le9\bigr).
\]

Both implications require proof. A census for finitely many lengths is not a
classification, and translating the top row is outside the normalized family
\(s_1=2,s_2=3\).

## Exact structural language and verifier

For \(S\in\mathcal G_n\), let its ordered right anti-diagonal be

\[
e_i=s_{n-i}^{i}\quad(1\le i\le n-1),\qquad
A(S)=\sum_{i=1}^{n-1}e_i.
\]

Thus \(e_i\ge0\), \(e_{n-1}=1\), and the order \(e_1,e_2,\ldots,e_{n-1}\)
cannot be permuted. Put

\[
F_S(d)=\left|\cdots\left||d-e_1|-e_2\right|\cdots-e_{n-1}\right|.
\]

The primary source's exact criterion is
\(k\in K_S\iff F_S(|k-s_n|)=1\). Equivalently, start with
\(T_{n-1}=\{1\}\) and, for \(i=n-1,n-2,\ldots,1\), set

\[
T_{i-1}=P_{e_i}(T_i),\qquad
P_e(T)=\{e+t:t\in T\}\cup\{e-t:t\in T,\ e\ge t\}.
\]

Then \(D_S=T_0\) and
\(K_S=\{s_n+d:d\in D_S\}\cup\{s_n-d:d\in D_S\}\). The condition
\(e\ge t\) in the second branch is essential; replacing that branch by
\(|e-t|\) changes the set.

The candidate parity interval is

\[
C_S=\{k\in\mathbb Z:|k-s_n|\le A(S)+1,
\ k\equiv s_n\pmod 2\}.
\]

## Literature status and nearest result

Leila Muney, *Holes in Valid-Extension Sets of Finite Gilbreath Sequences*,
[arXiv:2606.23721v2](https://arxiv.org/abs/2606.23721), revised 2026-07-16,
was inspected on 2026-09-09 in its
[v2 HTML text](https://arxiv.org/html/2606.23721v2). Section 16, question (5),
asks exactly for the stability classification of
\(S\in\mathcal G_n\) with \(|K_S|\le9\). Exact-phrase and equivalent-language
web searches located this primary preprint but no later claimed resolution;
that limited search is not proof of priority or continued openness.

The nearest verified results in that source are:

- Proposition 2: the ordered folding criterion above.
- Proposition 18: the exact reverse-tree computation above.
- Theorem 20: \(K_S=C_S\) iff
  \(e_i\le1+\sum_{j>i}e_j\) for every \(1\le i\le n-2\).
- Theorem 25: for every \(n\ge3\), the minimum width is 5, uniquely attained
  by \(L_n=(2,3,5,7,\ldots,2n-1)\).
- Theorem 24 and its exact length-five table: the first non-interval-complete
  sequence is \((2,3,5,9,15)\), and its width is exactly 10. At length five,
  the widths at most nine appearing in the table are 5, 7, and 9.

The paper reports bounded exhaustive data through length 10 (and only the
family count at length 11), which does not settle this all-length question.
Accordingly the source status is **open-supported**, while novelty remains to
be rechecked if a candidate theorem is later obtained.

## Triage target

Nearest prior result X: the minimum-width uniqueness theorem and the exact
interval-completeness criterion. Proposed delta Y: a necessary-and-sufficient,
all-\(n\) classification through width 9. Verification route Z: first try to
falsify the threshold lemma

\[
K_S\ne C_S\quad\Longrightarrow\quad |K_S|\ge10.
\]

The length-five first-hole example makes 10 the sharp possible threshold but
does not prove the lemma. If the lemma survives and is proved, every target
sequence is interval-complete, so \(|K_S|=A(S)+2\le9\); the remaining task is
then a completeness proof for the realizable ordered anti-diagonals with small
sum. If it fails, the least exact counterexample must be incorporated into a
repaired classification.
