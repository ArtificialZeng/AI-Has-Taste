# Full-scope proof proposed for fresh review

Proposer: primary-20260914-comb-inverse-research-b437f7246570.
Date: 2026-09-14 Asia/Shanghai. This is a research proof dossier, not an
accepted audit or a publication manuscript.

## Statement and dependencies

For the recursively defined comb posets and raw lattice-point support
polynomials in `source.md` and `problem.md`, the two series specified there
satisfy

\[
 R(t,F(t,x))=x=F(t,R(t,x))\qquad\text{in }\mathbb Q(t)[[x]].
\]

In particular, the assertion concerns every coefficient and the full
indeterminate support parameter, not only its specialization at one.
We prove it directly from the ideal inequalities, with no support-duality
theorem or experimentally inferred recurrence as a dependency. The tree
decomposition used below is classical; its needed formal and bijective
details are included here. The source proposal is in Section 9.6 of the
primary text archived as `evidence/external/2605.26916.html`.

Write \(K=\mathbb Q(t)\) and \(q=1+t\). All series substitutions below have
zero constant term. Every rational-series denominator used has an invertible
constant coefficient in \(K\). The letter \(c\) denotes a nonnegative
integer cost, not the parameter \(q\).

## 1. All lower ideals give precisely prefix constraints

The recursion defining \(\tau_n\) gives a spine
\(r_1<\cdots<r_n\), indexed from the minimum, and one leaf \(s_i\) above
\(r_i\) for each \(i\). Its covering relations are
\(r_i<r_{i+1}\) and \(r_i<s_i\). This follows by induction: the newly
adjoined minimum and singleton are \(r_1,s_1\), and the old labels shift
by one.

Every nonempty lower ideal is uniquely of the form

\[
 I_{k,S}=\{r_1,\ldots,r_k\}\cup\{s_i:i\in S\},
 \quad 1\le k\le n,\quad S\subseteq\{1,\ldots,k\}.
\]

Indeed, the spine part is an initial segment; a leaf requires its parent
and that parent's predecessors, and no other predecessor. Every displayed
set is conversely a lower ideal. The empty ideal contributes a vacuous
inequality.

For a nonnegative integer vector let \(a_i=x_{r_i}\), \(b_i=x_{s_i}\).
The inequality for \(I_{k,S}\) is

\[
 \sum_{i=1}^k a_i+\sum_{i\in S}(b_i-1)\le k.
\]

Maximizing independently over the choices of membership in \(S\) shows
that *all* these inequalities are equivalent to

\[
 \sum_{i=1}^k c_i\le k\quad(1\le k\le n),\qquad
 c_i=a_i+\max(b_i-1,0).                                      \tag{1}
\]

The maximization argument also applies to nonnegative real coordinates,
although only integer coordinates are counted here. No ideal inequality
has been discarded without this equivalence.

## 2. Local support weights

For an integer \(c\ge0\) define

\[
 w_c(t)=\sum_{\substack{a,b\in\mathbb Z_{\ge0}\\a+\max(b-1,0)=c}}
             t^{\mathbf1_{a>0}+\mathbf1_{b>0}}.
\]

For \(c=0\) the two pairs are \((0,0),(0,1)\). For \(c\ge1\) there are
two pairs of support one, \((c,0),(0,c+1)\), and exactly \(c\) pairs of
support two: \((c,1)\), and \((c-b+1,b)\) for \(2\le b\le c\).
These lists exhaust the possibilities by separating \(b=0,1\) and
\(b\ge2\). Thus

\[
 w_0=q,\qquad w_c=2t+ct^2\ (c\ge1),
\]
\[
 W(t,u):=\sum_{c\ge0}w_c(t)u^c
   =q+\frac{2tu}{1-u}+\frac{t^2u}{(1-u)^2}
   =\frac{(1+(t-1)u)(q-u)}{(1-u)^2}.                         \tag{2}
\]

The choices of each pair are independent once the costs are fixed, and
support adds across pairs. Hence, writing \(\mathcal C_n\) for the
sequences of nonnegative integers satisfying (1),

\[
 h_n(t)=\sum_{(c_1,\ldots,c_n)\in\mathcal C_n}
                   \prod_{i=1}^n w_{c_i}(t).                \tag{3}
\]

For \(n=0\) the unique empty sequence has weight one. Each set
\(\mathcal C_n\) is finite because its entries sum to at most \(n\).

## 3. Bijection with nonempty ordered forests

An ordered rooted tree has an ordered list of children at each vertex.
An ordered forest is an ordered list of such trees. Postorder visits the
children in their specified order before their parent, and visits the
trees of a forest in their specified order.

We claim that nonempty ordered forests on \(n+1\) vertices correspond
bijectively to \(\mathcal C_n\), with postorder outdegrees

\[
 (d_0,d_1,\ldots,d_n)=(0,c_1,\ldots,c_n).                    \tag{4}
\]

Here vertices are unlabelled; their positions in this deterministic
traversal specify the correspondence without a labelling multiplicity.

**Construction.** Process (4) from left to right, maintaining a stack
that is an ordered list of completed trees. For the entry \(d_i\), take
the last \(d_i\) trees, in their existing left-to-right order, as the
children of a new root, and replace them by the newly rooted tree. For
degree zero this means appending a leaf; no tree is removed. Start with
the empty stack. The first degree zero therefore creates one leaf.
Before processing \(c_i\), exactly \(i\) vertices and
\(\sum_{j<i}c_j\) edges have been created, so the stack has
\(i-\sum_{j<i}c_j\) trees. It contains enough children if and only if
\(\sum_{j\le i}c_j\le i\), precisely (1). Its size after that step is
\(i+1-\sum_{j\le i}c_j\ge1\); the final forest is nonempty.

An induction on processed entries shows that concatenating the postorder
degree words of the trees on the current stack gives exactly the processed
word. Replacing its final trees by their new parent appends that parent's
degree and does not reorder any earlier vertex. The produced forest thus
has exactly (4) as its postorder word.

**Inverse.** A nonempty forest starts its postorder traversal at a leaf,
so its first degree is zero. Apply the same stack procedure to its actual
postorder word. At a parent of degree \(d\), the last \(d\) completed
trees on the stack are precisely that parent's children in order. This
can be verified recursively within each subtree: processing a subtree
leaves any earlier stack entries in place and appends exactly that
subtree. Processing the component trees successively therefore recovers
the original forest. In particular every stack operation is allowed,
which gives (1). This proves both existence and uniqueness in (4), in
both directions.

Give a vertex of outdegree \(c\) weight \(z w_c(t)\), and let \(T(z)\)
enumerate nonempty ordered rooted trees with the product of these weights.
Root decomposition gives

\[
 T(z)=z\sum_{c\ge0}w_c(t)T(z)^c=zW(t,T(z)).                  \tag{5}
\]

This equation defines a unique series \(T\in zK[[z]]\) by induction on
degree. Combinatorially, for each fixed size there are finitely many
ordered rooted trees; their outdegrees are at most size minus one, and
each local weight is a polynomial. Thus the infinite sum in (5) is
coefficientwise finite. In particular \(T=qz+O(z^2)\).

All nonempty ordered forests have generating series
\(T+T^2+\cdots=T/(1-T)\). Under (4), their weight is

\[
 z^{n+1}w_0(t)\prod_{i=1}^n w_{c_i}(t)
      =qz\,z^n\prod_{i=1}^n w_{c_i}(t).
\]

The extra factor comes from the *first* postorder vertex, a uniquely
specified leaf, not an arbitrarily chosen or marked leaf. More explicitly,
one may decorate each other vertex by one of the pairs counted by its
\(w_c\); these are exactly the original coordinates. The first vertex
may independently carry either of the two decorations of cost zero,
of weights 1 and \(t\). This supplies precisely \(q\), with no factor
equal to the number of leaves.

Consequently, with \(H(z)=\sum_{n\ge0}h_n(t)z^n\),

\[
 qzH(z)=\frac{T(z)}{1-T(z)},\qquad
 H(z)=\frac{T(z)}{qz(1-T(z))}.                              \tag{6}
\]

The division by \(z\) removes a known factor, and \(q\) is a unit in
\(K\). When \(n=0\), the one-vertex forest has weight \(qz\), so (6)
has the required constant coefficient one.

## 4. Formal elimination

The original shifted series is \(F(t,x)=xH(x/t)\). Put \(U=T(x/t)\).
Equations (5)--(6) give

\[
 F=\frac{tU}{q(1-U)},\qquad
 U=\frac{qF}{t+qF},\qquad U=\frac{x}{t}W(t,U).              \tag{7}
\]

In (2), substitute this value of \(U\). The three factors become

\[
 1-U=\frac{t}{t+qF},\quad
 1+(t-1)U=\frac{t(1+qF)}{t+qF},\quad
 q-U=\frac{qt(1+F)}{t+qF}.
\]

Thus \(W(t,U)=q(1+F)(1+qF)\). Since its constant coefficient is \(q\),
we may rearrange (7) to obtain

\[
 x=\frac{tU}{W(t,U)}
   =\frac{F}{(1+F)(1+qF)(1+qF/t)}.                         \tag{8}
\]

This is an identity of full formal series obtained from the bijection.

## 5. Sum exactly the proposed inverse

For an auxiliary variable \(y\), the contribution of the initial 1 in
each coefficient of the original \(R(t,y)\) is \(y/(1+y)\). Its remaining
contribution is, on setting \(m=k+2\),

\[
 -\frac{q^2y^2}{t}\sum_{k\ge0}(-qy)^k\sum_{j=0}^k t^{j-k}
 =-\frac{q^2y^2}{t}\sum_{a,b\ge0}(-qy)^a(-qy/t)^b
 =-\frac{q^2y^2}{(1+qy)(t+qy)}.
\]

Here \(a=j\), \(b=k-j\); at each degree there are only finitely many
terms, so the rearrangement is valid formally. In particular no division
by \(1-t\) is needed. Therefore

\[
 \begin{aligned}
 R(t,y)&=\frac{y}{1+y}-\frac{q^2y^2}{(1+qy)(t+qy)}\\
 &=\frac{ty}{(1+y)(1+qy)(t+qy)}
  =\frac{y}{(1+y)(1+qy)(1+qy/t)}.                           \tag{9}
 \end{aligned}
\]

The numerator simplification uses \(q=1+t\):
\((1+qy)(t+qy)-q^2y(1+y)=t\). Equations (8)--(9) prove \(R(t,F)=x\).
Both \(F\) and \(R\) have constant coefficient zero and linear
coefficient one. Formal series with this property have a unique
compositional inverse, as follows by recursively solving its coefficients;
hence also \(F(t,R)=x\). This settles the frozen identity at its full scope.

For an additional check free of negative powers of \(t\), put \(x=tz\)
in (8) and cancel the factor \(tz\) from the equality after clearing
denominators. Since \(F(t,tz)=tzH(z)\), the same conclusion reads

\[
 H=(1+tzH)(1+tqzH)(1+qzH)
   =1+(1+3t+t^2)zH+2t(1+t)^2z^2H^2+t^2(1+t)^2z^3H^3.     \tag{10}
\]

This equation has a unique constant-one solution in \(\mathbb Z[t][[z]]\)
by coefficient recursion. It is a consequence of the proof, not a
recurrence inferred from initial numerical values.

## Scope, checks, and gaps

The argument uses all lower ideals and the actual support weights. It
proves the original inverse identity for all \(n\) with \(t\)
indeterminate. Specializing the intermediate forest quotient at \(t=-1\)
is not permitted; no such specialization is used. The polynomial equation
(10) remains valid at all scalar values, including zero and minus one.

The accompanying `research-forest-check.py` independently constructs forest
shapes, compares them with all bounded cost words, and checks local weights
and polynomial identities. Its finite output is supplementary evidence,
not a substitute for this uniform argument or a fresh referee pass.

Known mathematical gaps in this proposed proof: **none identified**.
Fresh mathematical review has **not** occurred. Novelty is only screened
against the primary sources documented in `literature/research-screen.md`;
global priority is not certified. In particular the recent general support
duality result must be acknowledged, although it is not used by this proof.
