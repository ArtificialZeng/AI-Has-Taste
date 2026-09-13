# Proof-builder notes: structural reductions for the \(v_{10}\) interval

Date: 2026-08-29 (Asia/Shanghai)

Role: proof builder. These arguments were developed without importing breaker
output. Claims marked **proved** have complete arguments below. Exact
enumerations and the mask/path statement are explicitly not promoted to a
general theorem.

## 1. Forced normalization and Fibonacci recurrence

Work in \(S_n=\langle s_1,\ldots,s_{n-1}\rangle\), with products acting on the
right, and put

\[
\Omega_n=(s_2s_1)(s_3s_2)\cdots(s_{n-1}s_{n-2}),\qquad
v_n=34\cdots n12.
\]

For \(u\le v\), define

\[
d(u,v)=\ell(v)-\ell(u),\qquad t=q^{-2},\qquad
P_{u,v}(t)=q^{-d(u,v)}\widetilde R_{u,v}(q).
\]

### Lemma 1 (proved)

If \(s\in D_R(v)\), then

\[
P_{u,v}=
\begin{cases}
P_{us,vs},&s\in D_R(u),\\
P_{u,vs}+tP_{us,vs},&s\notin D_R(u),
\end{cases}
\tag{1}
\]

where \(P_{us,vs}=0\) if \(us\not\le vs\). Moreover
\(P_{u,u}=1\), \(P_{u,v}\in\mathbb Z[t]\), and \(P_{u,v}(0)=1\).

**Proof.** The first case is the defining recurrence. In the second case the
ranks of \((u,vs)\) and \((us,vs)\) are \(d-1\) and \(d-2\). Divide

\[
\widetilde R_{u,v}
=\widetilde R_{us,vs}+q\widetilde R_{u,vs}
\]

by \(q^d\). Induction on \(\ell(v)\) proves the remaining assertions.

Every \(F_h(t)\) has constant term \(1\), while the highest \(q\)-term of
\(\widetilde R_{u,v}\) is \(q^{d(u,v)}\) with coefficient \(1\). Hence the
exponent in every valid product formula is forced:

\[
g(u,v)=\ell(v)-\ell(u).
\tag{2}
\]

Thus the real assertion is

\[
P_{u,v}(t)=\prod_iF_{h_i}(t).
\tag{3}
\]

The factors \(F_0=F_1=1\) are noncanonical redundancies and should be omitted
from serialized certificates.

## 2. Exact factorization by Coxeter support

For \(w\in S_n\), let \(\operatorname{Supp}(w)\) be the set of simple
generators occurring in a reduced word. In one-line notation,

\[
i\notin\operatorname{Supp}(w)
\Longleftrightarrow
\{w(1),\ldots,w(i)\}=\{1,\ldots,i\}.
\tag{4}
\]

Let \(I_1,\ldots,I_k\) be the maximal consecutive intervals in
\(\operatorname{Supp}(v)\). Their parabolic subgroups commute.

### Lemma 2 (proved: direct-product multiplicativity)

If \(u\le v\), write uniquely

\[
v=v_1\cdots v_k,\qquad u=u_1\cdots u_k,\qquad
u_j,v_j\in W_{I_j}.
\]

Then \(u_j\le v_j\) and

\[
\widetilde R_{u,v}(q)=
\prod_{j=1}^k\widetilde R_{u_j,v_j}(q),\qquad
P_{u,v}(t)=\prod_{j=1}^kP_{u_j,v_j}(t).
\tag{5}
\]

**Proof.** The subword property gives
\(\operatorname{Supp}(u)\subseteq\operatorname{Supp}(v)\). Bruhat order and
length are coordinatewise in the direct product
\(\prod_jW_{I_j}\). Induct on \(\ell(v)\). Choose a right descent \(s\) in a
nonidentity factor \(v_j\). Since all other factors commute with \(s\),
\(s\in D_R(u)\) exactly when \(s\in D_R(u_j)\). Apply the two cases of the
\(\widetilde R\)-recurrence. The induction hypothesis extracts every
unchanged component; the remaining bracket is the recurrence for
\(\widetilde R_{u_j,v_j}\). Length additivity gives the normalized identity.

This reduces the conjecture exactly to upper endpoints with connected
Coxeter support.

## 3. A proved infinite independent-block class

Call \(b\) boolean if a reduced word for \(b\) contains no repeated simple
generator.

### Lemma 3 (proved: boolean block)

If \(a\le b\) and \(b\) is boolean, then

\[
\widetilde R_{a,b}(q)=q^{\ell(b)-\ell(a)},\qquad P_{a,b}(t)=1.
\tag{6}
\]

**Proof.** Fix a reduced word \(b=s_{i_1}\cdots s_{i_r}\) with distinct
letters. Every \(a\le b\) is represented by a unique subset of its positions:
existence is the subword property, and different subsets have different
Coxeter support. Induct on \(r\), using \(s=s_{i_r}\). If the final position
is selected for \(a\), it is a common right descent and is removed. If it is
not selected, \(s\notin D_R(a)\) and \(as\not\le bs\), because
\(\operatorname{Supp}(as)\) contains \(s\) while
\(\operatorname{Supp}(bs)\) does not. Only
\(q\widetilde R_{a,bs}\) remains. Induction proves (6).

For \(A\in\mathbb Z\) and \(m\ge3\), define a shifted full block

\[
\nu_{A,m}=(s_{A+1}s_A)(s_{A+2}s_{A+1})\cdots
(s_{A+m-2}s_{A+m-3})\in W_{[A,A+m-2]}.
\tag{7}
\]

This is an index shift of \(v_m\). The published Chen--Fan--Guo--Zhong
endpoint theorem says that for \(a\le\nu_{A,m}\),

\[
P_{a,\nu_{A,m}}(t)
=F_{m-\ell(a)+d(\omega)-2}(t),
\tag{8}
\]

where \(\omega\) is a reduced subword of the shifted \(\Omega_m\), and
\(d(\omega)\) counts adjacent selected letters whose indices decrease by one.

### Theorem 4 (proved from Lemmas 2--3 and the published theorem)

Suppose every connected support component of \(v\le v_n\) is either boolean
or a shifted full block \(\nu_{A,m}\). Then (3) holds for every \(u\le v\).
Boolean components contribute no nonconstant factor; each full block
contributes the factor in (8).

For example, in \(S_{10}\),

\[
v=(3,4,5,1,2,\ 8,9,10,6,7)=\nu_{1,5}\nu_{6,5}.
\]

The supports \([1,4]\) and \([6,9]\) commute. At \(u=e\),

\[
\widetilde R_{e,v}(q)
=q^{12}F_3(q^{-2})^2
=q^{12}+4q^{10}+4q^8.
\tag{9}
\]

### Corollary 4.1 (proved: index-sum bound on this class)

If \(H_j\) is the actual Fibonacci index in (8), then

\[
H_j=m_j-\ell(a_j)+d(\omega_j)-2\le m_j-2,
\]

because \(d(\omega_j)\le\ell(a_j)\). The block uses \(m_j-1\) generators.
Consequently every interval in Theorem 4 satisfies

\[
\sum_j H_j\le n-2.
\tag{10}
\]

If at least one nonconstant block occurs, the sum is at most the number of
used generators minus the number of such blocks, hence at most
\((n-1)-1\); otherwise the sum is zero. This proves the observed bound on a
nontrivial infinite class, but not for every connected capped-ladder interval.

## 4. Capped-ladder reduction: the genuinely new \(n=10\) boundary

Let \(I=[a,b]\) be a connected component of
\(\operatorname{Supp}(v)\), for \(v\le v_n\). Put

\[
r=b-a+1,\qquad c_L=\mathbf1_{a>1},\qquad c_R=\mathbf1_{b<n-1}.
\]

Project a reduced subword of \(\Omega_n\) representing \(v\) onto \(I\).
Letters from other components commute. Length additivity shows that the
projected expression is reduced and represents the component \(v_I\).
The available local word is exactly

\[
\Lambda_{a,b}^{(n)}
=(s_a)^{c_L}
\left(\prod_{j=a+1}^{b}s_js_{j-1}\right)
(s_b)^{c_R},
\tag{11}
\]

where the exponents mean presence or absence, not group powers.

### Lemma 5 (proved: minimal ambient rank)

Every local interval \([u_I,v_I]\) in (11), after shifting indices, is an
interval in \([e,v_N]\subset S_N\), where

\[
N=N(I)=r+1+c_L+c_R.
\tag{12}
\]

**Proof.** In \(S_N\), place the \(r\)-generator support at \([1,r]\) when
\(c_L=0\), and at \([2,r+1]\) when \(c_L=1\). Restricting \(\Omega_N\) to
that support gives (11): a left cap occurs exactly when the support begins at
2, and a right cap exactly when it ends one generator before \(N-1\). The
subword property proves the assertion.

### Corollary 6 (proved: three new connected families)

Assume the \(n\le9\) baseline has been independently reproduced. Lemmas 2
and 5 settle every \(n=10\) interval except connected full-support endpoints
in these local ambient words:

| type | global support | shifted ambient word | caps |
|---|---|---|---|
| A | \([1,9]\) | \(\Omega_{10}\) | none |
| B | \([1,8]\) or \([2,9]\) | \(\Omega_9s_8\) or \(s_1\Omega_9\) | one |
| C | \([2,8]\) | \(s_1\Omega_8s_7\) | two |

Indeed \(N(I)\le10\), and \(N(I)=10\) gives only

\[
(r,c_L+c_R)=(9,0),(8,1),(7,2).
\]

Each listed support leaves no nonadjacent generator for another support
component. Therefore every disconnected-support \(n=10\) interval reduces
entirely to \(n\le9\) component intervals.

The one-cap cases are equivalent. If
\(\delta(s_i)=s_{r+1-i}\) is the type-\(A_r\) diagram involution, then
\(w\mapsto\delta(w^{-1})\) maps
\(\Omega_{r+1}s_r\) to \(s_1\Omega_{r+1}\). Inversion and Coxeter-system
automorphisms preserve \(\widetilde R\).

The bound \(\sum H_i\le n-2\) is inherited by this reduction. Suppose the
local theorem in minimal rank \(N(I)\) gives factor-index sum at most
\(N(I)-2\). Let support-component lengths be \(r_1,\ldots,r_k\), and let
\(e\in\{0,1,2\}\) count nonempty left/right exterior gaps. The total cap count
is \(2(k-1)+e\), so

\[
\sum_j(N(I_j)-2)=\sum_jr_j+k-2+e\le n-2.
\tag{13}
\]

The inequality holds because the \(n-1\) generator positions contain the
component supports, at least \(k-1\) internal gaps, and the \(e\) nonempty
exterior gaps. Thus both factorization and the index-sum assertion reduce to
the connected A--C families.

### Diagnostic workload counts (not certificates)

An exact-integer enumeration of subword products, full supports via (4), and
principal ideals gave:

| type | all local elements | full-support uppers | comparable pairs |
|---|---:|---:|---:|
| A | 12,866 | 1,137 | 2,221,410 |
| B | 4,374 | 577 | 519,212 |
| C | 1,458 | 239 | 89,780 |

Counting both mirror copies of B gives 3,349,614 genuinely new connected
pairs. The full \(n=10\) ideal has 12,866 elements and 6,229,297 comparable
pairs by the same diagnostic. These counts require independent reproduction
before use in a certified finite theorem.

## 5. Distinguished masks and the missing general lemma

Fix a reduced word \(\mathbf v=s_{i_1}\cdots s_{i_m}\). A mask
\(\epsilon\in\{0,1\}^m\) defines

\[
x_0=e,\qquad x_j=x_{j-1}s_{i_j}^{\epsilon_j}.
\]

Call it right-distinguished if

\[
\epsilon_j=0\Longrightarrow
\ell(x_{j-1}s_{i_j})>\ell(x_{j-1});
\tag{14}
\]

a descent cannot be skipped. Define its defect set by

\[
D(\epsilon)=
\{j:\epsilon_j=1,\ \ell(x_j)<\ell(x_{j-1})\}.
\tag{15}
\]

### Lemma 7 (proved: exact mask generating function)

\[
P_{u,v}(t)=
\sum_{\substack{\epsilon\text{ satisfies }(14)\\x_m=u}}
t^{|D(\epsilon)|}.
\tag{16}
\]

**Proof.** Read \(\mathbf v\) from right to left. A current right descent is
forced to be selected; at an ascent, selection and skipping are precisely the
two recurrence branches. Thus recurrence leaves and masks are in
weight-preserving bijection. If a mask has \(A\) selected descents, it has
\(\ell(u)+2A\) selected positions, hence
\(m-\ell(u)-2A=d(u,v)-2A\) skips. Its contribution
\(q^{d-2A}\) normalizes to \(t^A\).

### Candidate P-MASK (open, not a theorem)

For a suitable canonical reduced word of every upper endpoint below \(v_n\),
the map

\[
\epsilon\longmapsto D(\epsilon)
\tag{17}
\]

should be a bijection from masks ending at fixed \(u\) to independent sets of
a graph \(G(u,v)\), with every component of \(G(u,v)\) a path.

If proved, (16) gives the product formula because the independence polynomial
of a path on \(r\) vertices is \(F_{r+1}(t)\). A proof must establish:

1. defect positions determine the whole mask;
2. defect sets are hereditary;
3. every minimal forbidden set has size two;
4. the conflict graph has maximum degree two;
5. the conflict graph has no cycle;
6. one explicit reduced-word choice works for every upper endpoint.

To also prove \(\sum_i h_i\le n-2\), one needs a further **disjoint
footprints lemma**: a path on \(r\) defect vertices must occupy \(r+1\)
distinct slots in the \(n-2\) column spine of \(\Omega_n\), and footprints of
different components must be disjoint. Then \(h_i=r_i+1\) and the bound
follows. Polynomial factorization alone cannot prove this: degree controls
only \(\sum_i\lfloor h_i/2\rfloor\), not \(\sum_i h_i\).

### Exact falsification evidence

Using only integer permutation arithmetic, every upper and lower endpoint for
\(3\le n\le9\) was tested for properties 1--5, with each upper reduced word
chosen independently by deterministic leftmost-adjacent-inversion sorting.
No failure occurred.

| \(n\) | upper endpoints | valid masks over all pairs |
|---:|---:|---:|
| 3 | 4 | 9 |
| 4 | 14 | 72 |
| 5 | 46 | 545 |
| 6 | 146 | 3,990 |
| 7 | 454 | 28,561 |
| 8 | 1,394 | 201,176 |
| 9 | 4,246 | 1,400,177 |

With deterministic seed 829, 200 full-support type-A \(n=10\) uppers and all
their lower endpoints also passed. This is discovery evidence, not proof.

The discriminating test is to exhaust A--C and, on failure, serialize
\((u,v,\mathbf v)\) together with either two masks having one defect set, a
minimal nonface of size at least three, a degree-three vertex, or a cycle.
Such a witness refutes P-MASK but does not itself refute the product formula.

## 6. Fail-closed Fibonacci recurrence certificate

Equation (1) gives a proof-certificate calculus independent of final
polynomial factorization. For each interval node store endpoints, rank,
chosen right descent, and child hashes. Accept only:

1. **base:** \(u=v\), factor multiset empty;
2. **common descent:** replace \((u,v)\) by \((us,vs)\);
3. **zero branch:** if \(s\notin D_R(u)\) and \(us\not\le vs\), replace
   \((u,v)\) by \((u,vs)\);
4. **Fibonacci join:** if the children certify
   \[
   P_{us,vs}=C(t)F_{h-2}(t),\qquad
   P_{u,vs}=C(t)F_{h-1}(t),
   \]
   certify the parent as \(C(t)F_h(t)\);
5. **support product:** apply Lemma 2 after recomputing support components.

Rule 4 is exact because \(F_h=F_{h-1}+tF_{h-2}\). A verifier must reject:

- a wrong/absent upper right descent;
- a claimed zero branch with \(us\le vs\);
- wrong ranks or multiplication convention;
- a base node with \(u\ne v\);
- a tampered \(h\) or unequal common factor multisets;
- noncanonical \(F_0,F_1\) factors;
- a product split across adjacent supports;
- missing child hashes or cycles in the certificate DAG;
- endpoints outside \(S_{10}\) or failing exact Bruhat order.

Bruhat order must be recomputed by an independent rank-matrix criterion, not
by importing a discovery subword table.

## 7. Route status and honest endpoint

| ID | Route | Status | Result / gap |
|---|---|---|---|
| P-B1 | support direct product | **proved** | Lemma 2 and Theorem 4 |
| R-B2 | minimal capped-ladder ambient | **proved** | Lemma 5 and Corollary 6 |
| P-B3 | distinguished-mask sum | **proved** | Lemma 7 |
| P-B4 | defect graph is a path forest | **candidate** | properties 1--6 unproved |
| P-B5 | recurrence DAG calculus | **proved as a rule** | existence of a DAG for every root is not proved structurally |

The exhaustive \(n=10\) result reported by the certifier, once its serialized
no-import verifier passes, is a **certified finite result**. It proves
factorization and the finite classification of observed factor multisets at
\(n=10\). In particular, if its factor list directly checks that precisely
the partitions with \(\sum h_i\le8\) occur, that statement is rigorous for
\(n=10\).

It is not an all-\(n\) proof. The occurrence of every such partition does not
by itself imply P-MASK, the disjoint-footprints lemma, or an inductive
construction. Those are the named fatal gaps for a general theorem.

No Lean, Coq, Isabelle, or other proof assistant was used in these notes.
