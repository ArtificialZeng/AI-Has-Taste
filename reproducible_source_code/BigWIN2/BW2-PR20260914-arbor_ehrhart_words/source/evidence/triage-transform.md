# Subtree transformation: triage derivation requiring audit

Date: 2026-09-14. Job:
`primary-20260914-arbor-ehrhart-words-triage-5bfaab9809a5`.
This is a mathematical evidence note, not an accepted result or manuscript.
The following derivation appears to cover the frozen all-arbor statement;
research must check it before freezing a resolution candidate.

Fix an integer \(m\ge0\). Let \(T_{\le k}\) retain degrees at most \(k\)
and \(T_{\ge k}\) retain degrees at least \(k\). Define at every vertex
\[
F_v(x)=T_{\le mN_v}\left((1-x)^{-b_v}\prod_{c\text{ child of }v}F_c(x)\right).
\tag{1}
\]
Its coefficient of \(x^s\) counts nonnegative integer vectors on \(D_v\)
of total \(s\), satisfying every subtree upper bound \(mN_u\) below \(v\).
This follows from stars and bars on \(B_v\), independent child subtrees,
and truncation at the constraint for \(v\). Thus \(L_\tau(m)=F_r(1)\).

Independently define
\[
G_v(y)=T_{\ge N_v}\left((1+y)^{(m+1)b_v}
                         \prod_{c\text{ child of }v}G_c(y)\right).
\tag{2}
\]
Each coordinate contributes \((1+y)^{m+1}\), so coefficients count vectors
\(a\) with weight \(\prod_i\binom{m+1}{a_i}\) and the lower subtree
bounds. In particular,
\[
[y^n]G_r(y)=\sum_{a\in A_\tau}\prod_i\binom{m+1}{a_i}.
\tag{3}
\]
No preorder-dual theorem is needed to justify this interpretation.

## Local identity

For integers \(b\ge1\) and \(K\ge0\),
\[
y^b\sum_{q=0}^K\binom{q+b-1}{b-1}(1+y)^{K-q}
   =T_{\ge b}(1+y)^{K+b}.
\tag{4}
\]
Indeed, after dividing by \(y^b\), the coefficient of \(y^j\),
\(0\le j\le K\), on the left is
\[
\sum_{q=0}^{K-j}\binom{q+b-1}{b-1}\binom{K-q}{j}
=\binom{K+b}{b+j}.
\]
For a direct proof of the last equality, put \(r=K-j-q\) and take the
coefficient of \(z^{K-j}\) in
\((1-z)^{-b}(1-z)^{-j-1}\). These are exactly the coefficients of the
right side of (4).

## Proposed induction for every subtree

Claim:
\[
G_v(y)=y^{N_v}(1+y)^{mN_v}F_v\bigl((1+y)^{-1}\bigr).
\tag{5}
\]
The right side is a polynomial since \(\deg F_v\le mN_v\).
Suppose (5) holds for the children; the empty product handles leaves.
Write \(b=b_v\), \(N=N_v\), and
\(R(x)=\prod_cF_c(x)=\sum_s r_sx^s\).
Then \(\deg R\le m(N-b)\), so \(K=mN-s\ge0\) for every contributing
\(s\). Equation (1) gives
\[
F_v(x)=\sum_s r_sx^s\sum_{q=0}^{mN-s}
                                  \binom{q+b-1}{b-1}x^q.
\]
Apply (4) to each summand after substituting \(x=(1+y)^{-1}\):
\[
\begin{aligned}
y^N(1+y)^{mN}F_v((1+y)^{-1})
 &=y^{N-b}T_{\ge b}\left((1+y)^{mN+b}R((1+y)^{-1})\right). \tag{6}
\end{aligned}
\]
On the other hand, the child instances of (5) imply
\[
(1+y)^{(m+1)b}\prod_cG_c(y)
 =y^{N-b}(1+y)^{mN+b}R((1+y)^{-1}).
\]
Here each summand inside parentheses has exponent \(mN+b-s\ge0\), so
ordinary polynomial truncation is legitimate. Applying \(T_{\ge N}\)
changes this expression to (6), which is exactly (2). This proves the
induction step. Consequently (5) at the root gives
\([y^n]G_r(y)=F_r(1)\), the desired binomial-sum equality for all \(m\ge0\).

## Word conversion, including ties and empty runs

For fixed content \(a\) with \(|a|=n\), the product
\(\prod_i\binom{m+1}{a_i}\) counts choices of which of \(m+1\) ordered
boxes contain each letter; no box contains a repeated letter. Reading each
box in strictly decreasing order, allowing empty boxes, produces a word
of content \(a\) with \(m\) bars. For a given word \(w\), every position
\(j\) with \(w_j\le w_{j+1}\) requires a bar; descents do not. There
are \(d=n-1-\operatorname{des}(w)\) required gaps. After placing these
bars, the remaining \(m-d\) bars are distributed among \(n+1\) gaps,
including the ends. Thus the number is \(\binom{m-d+n}{n}\) for
\(m\ge d\) and zero otherwise. Summing in \(m\) gives
\[
\sum_{m\ge0}\left(\prod_i\binom{m+1}{a_i}\right)t^m
=\frac{\sum_{w\text{ of content }a}t^{n-1-\operatorname{des}(w)}}{(1-t)^{n+1}}.
\]
Summing over \(A_\tau\) gives exactly the frozen target, conditional on
verification of the preceding derivation.

## Exact checks and limitations

Run from the project root: `python3 evidence/triage_recursion.py`.
The saved output `evidence/triage_recursion.json` contains nine cases,
55 case/dilation pairs, and 191 coefficientwise subtree identities.
Seven supplied cases (sizes 1, 4, 5) were freshly recomputed by direct
lattice-point and word enumeration; their Ehrhart samples and numerators
match the independent recurrences. The two added branching cases have
sizes 8 and 9; only recurrence checks were made for them, at all integer
\(m=0,\ldots,n\). This is sparse finite evidence, not exhaustive coverage,
independent mathematical review, or proof by computation.

The recurrence alone is elementary enumeration; any substantive contribution
would be the verified intertwining identity and its full-scope consequence.
Do not extend (1) to arbitrary preorders: overlapping ideals destroy the
independence of child subtrees. No such extension is established here.
The next test is to attack (4)–(6) and the box/word bijection directly,
especially degree bounds and zero/empty cases, before any candidate gate.
