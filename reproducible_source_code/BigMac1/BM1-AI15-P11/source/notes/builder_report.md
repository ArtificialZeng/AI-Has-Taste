# Gate 5 Builder report: rooted gamma cones and a strict infinite subclass

## Scope and epistemic status

This note is an independent positive-route derivation from the formal problem
statement and the rooted recurrence.  It makes **no literature or novelty
claim**.  The full Erdős #993 conjecture is not proved here.  The rigorous
endpoint is a strict-unimodality theorem for a nontrivial infinite subclass,
together with a more general rooted-state closure theorem.  The diagnostic
program is only a cross-check; no finite experiment is used as a premise of
the proof.

Throughout, coefficients are exact nonnegative integers.  A polynomial may be
viewed with leading or trailing zero coefficients when an ambient degree is
specified.  No argument divides by a coefficient or assumes strict positivity
of a rooted state.

## 1. The common-center gamma cone

For an integer \(d\geq 0\), define

\[
 \Gamma_d=\left\{
   \sum_{j=0}^{\lfloor d/2\rfloor}\gamma_j
      x^j(1+x)^{d-2j}:\gamma_j\in\mathbb R_{\geq0}
 \right\}.
\]

The ambient coefficient range is \(0,\ldots,d\).  Thus, for example,
\(x\in\Gamma_2\), with coefficient sequence \((0,1,0)\).  This padding
convention is essential for included-root states, whose constant coefficient
is zero.

### Lemma 1 (exact semiring rules)

For \(p,p'\in\Gamma_d\) and \(q\in\Gamma_e\),

\[
 p+p'\in\Gamma_d,\qquad pq\in\Gamma_{d+e},\qquad
 (1+x)p\in\Gamma_{d+1},\qquad xp\in\Gamma_{d+2}.
\]

**Proof.** Addition adds gamma coefficients.  On basis elements,

\[
 [x^a(1+x)^{d-2a}]
 [x^b(1+x)^{e-2b}]
 =x^{a+b}(1+x)^{d+e-2(a+b)}.
\]

The last two statements are the same identity with the indicated extra
factor.  All new gamma coefficients remain nonnegative.  \(\square\)

### Lemma 2 (shape, including plateaux and zeros)

Every polynomial in \(\Gamma_d\) has a coefficient sequence symmetric about
\(d/2\) and weakly unimodal with a mode at the central index or indices.  If
its gamma coefficient \(\gamma_0\) is positive, every inequality away from
the central position(s) is strict.  In detail, for \(d=2n\),

\[
 [x^0]p<[x^1]p<\cdots<[x^n]p>\cdots>[x^{2n}]p.
\]

For \(d=2n+1\), the only plateau is the forced central one:

\[
 [x^0]p<\cdots<[x^n]p=[x^{n+1}]p>\cdots>[x^{2n+1}]p.
\]

**Proof.** A basis sequence
\(x^j(1+x)^{d-2j}\), padded by zeros, is symmetric about \(d/2\), weakly
increasing up to the center, and weakly decreasing after it.  Nonnegative
sums preserve all of these coefficientwise inequalities.  The \(j=0\)
summand is \(\gamma_0(1+x)^d\).  Its binomial coefficients are strictly
increasing before the center and, for odd \(d\), equal only at the two central
indices.  It makes every noncentral inequality strict; symmetry supplies the
right half and forces the stated odd-degree plateau.  \(\square\)

## 2. A rooted-pair invariant that is genuinely closed

For a rooted tree \((R,r)\), let \(A_R\) count independent sets excluding
\(r\), and let \(B_R\) count those including \(r\).  Call \((R,r)\)
**gamma-balanced of darga \(d\)** when

\[
 A_R\in\Gamma_d\quad\hbox{and}\quad B_R\in\Gamma_d.
\]

The word "balanced" refers to the common ambient center \(d/2\), not to equal
polynomials.  In particular, zeros at the ends of \(B_R\) are allowed.

### Lemma 3 (rooted grammar)

The rooted cherry (a root with two leaf children) is gamma-balanced of darga
\(2\).  More generally, take any finite list of gamma-balanced rooted trees
\((R_j,r_j)\) of dargas \(d_j\), make their roots children of a new root, and
also give the new root exactly two new leaf children.  The resulting rooted
tree is gamma-balanced of darga \(2+\sum_jd_j\).

**Proof from the rooted recurrence.** For the rooted cherry,

\[
 A=(1+x)^2\in\Gamma_2,\qquad B=x\in\Gamma_2.
\]

For the general construction, the two new leaf children have total excluded-
root factor \((1+x)^2\) in \(A\) and factor \(1\) in \(B\).  Hence

\[
 A=(1+x)^2\prod_j(A_{R_j}+B_{R_j}),\qquad
 B=x\prod_j A_{R_j}.
\]

For every \(j\), common darga makes
\(A_{R_j}+B_{R_j}\in\Gamma_{d_j}\).  Lemma 1 now puts both displayed
polynomials in \(\Gamma_{2+\sum_jd_j}\).  The empty list is allowed and
recovers the cherry, so the empty-product boundary is covered.  \(\square\)

### Theorem 4 (balanced-cell gluing)

Let \(H\) be a finite graph.  For each \(v\in V(H)\), take a vertex-disjoint
gamma-balanced rooted tree \((R_v,r_v)\) of darga \(d_v\), and add the edge
\(r_ur_v\) for every \(uv\in E(H)\).  Then the resulting graph \(G\) has

\[
 I_G(x)\in\Gamma_D,\qquad D=\sum_{v\in V(H)}d_v,
\]

and its zeroth gamma coefficient is one.  It is therefore strictly unimodal
with a unique central peak when \(D\) is even; when \(D\) is odd, it is
strictly increasing and then strictly decreasing except for equality of the
two central coefficients.

If \(H\) is a tree, then \(G\) is a tree.

**Proof.** Partition independent sets of \(G\) according to the set \(S\) of
cell roots that they contain.  The allowed root sets are exactly the
independent sets of \(H\), and therefore

\[
 I_G(x)=\sum_{S\in\operatorname{Ind}(H)}
   \left(\prod_{v\in S}B_{R_v}\right)
   \left(\prod_{v\notin S}A_{R_v}\right).                 \tag{1}
\]

Every summand belongs to \(\Gamma_D\) by Lemma 1, and their sum remains in
\(\Gamma_D\).  The constant coefficient of every \(A_{R_v}\) is one and that
of every \(B_{R_v}\) is zero.  Since the zeroth gamma coefficient equals the
constant coefficient, exactly the \(S=\varnothing\) summand contributes to
\(\gamma_0\), and it contributes one.  Lemma 2 gives the claimed strictness
and complete plateau classification.  If the core is a tree, joining distinct
tree pieces by the \(|V(H)|-1\) core edges preserves connectedness and creates
no cycle.
\(\square\)

This is the exact rooted-composition invariant: closure depends on the two
states having the **same** darga.  It does not rely merely on each state being
unimodal.

## 3. Rigorous infinite tree subclass

For a graph \(H\), write \(L_2(H)\) for the graph obtained by attaching two
new private leaves to every vertex of \(H\).

### Theorem 5 (strict unimodality of double-leafy trees)

Let \(H\) be any nonempty \(n\)-vertex tree, and let \(T=L_2(H)\).  Then \(T\)
is a \(3n\)-vertex tree, \(\alpha(T)=2n\), and

\[
 I_T(x)=\sum_{j=0}^{\alpha(H)}i_j(H)
             x^j(1+x)^{2n-2j}\in\Gamma_{2n}.              \tag{2}
\]

Consequently its independence sequence is symmetric and strictly unimodal:

\[
 i_0(T)<i_1(T)<\cdots<i_n(T)>\cdots>i_{2n}(T),
 \qquad i_k(T)=i_{2n-k}(T).
\]

**First proof (direct exact decomposition).** Given an independent set \(S\)
of core vertices, every selected core vertex contributes \(x\) and forces its
two private leaves out.  At each of the other \(n-|S|\) core vertices, its two
private leaves are chosen freely and contribute \((1+x)^2\).  Summing first
over all core independent sets of size \(j\) gives (2).  The term with
\(j=0\) is \((1+x)^{2n}\), so the polynomial has degree exactly \(2n\), and
the set of all \(2n\) new leaves confirms \(\alpha(T)=2n\).  Equation (2)
places the polynomial in \(\Gamma_{2n}\) with \(\gamma_0=i_0(H)=1\).
Lemma 2 gives strict unimodality and symmetry.  Attaching leaves to a tree
preserves connectedness and acyclicity.

**Second proof (rooted-pair recurrence).** Root \(H\), orient its edges away
from the root, and regard each core vertex together with its two new leaves as
one application of Lemma 3.  Induction from the core leaves upward proves that
the rooted subtree over any core vertex \(v\) is gamma-balanced of darga
twice the number of core vertices below \(v\).  At the core root this gives
\(A_T,B_T\in\Gamma_{2n}\), hence
\(I_T=A_T+B_T\in\Gamma_{2n}\).  Tracking whether each core root is included
recovers the gamma coefficients \(i_j(H)\), agreeing with (2).  Thus the
direct decomposition and rooted recurrence independently yield the same
identity.  \(\square\)

### Boundary audit for Theorem 5

- **Smallest core:** \(n=1\) gives the cherry with
  \(I_T=1+3x+x^2\), so the asserted strict pattern is \(1<3>1\).
- **Empty graph:** excluded because the formal problem requires a nonempty
  tree.  Algebraically it would give the harmless empty product \(I=1\).
- **Zero state coefficients:** included-root polynomials have constant term
  zero; the ambient gamma-cone convention explicitly permits this.
- **Top degree:** all \(2n\) private leaves form an independent set, while
  every core vertex together with its two private leaves is a three-vertex
  star of independence number two, so no set exceeds \(2n\).
- **Plateaux:** Lemma 2 allows them in the general cone, but
  \(\gamma_0=1\) rules them out here by a strict binomial contribution.
- **No hidden cancellation:** all identities and cone operations have
  nonnegative coefficients.

## 4. Exact obstruction to extending the invariant to arbitrary roots

The common-darga condition is special rather than automatic.  Root the star
\(K_{1,m}\) at its center.  Its states are

\[
 A=(1+x)^m,\qquad B=x.
\]

If \((1+x)^m\in\Gamma_d\), its constant coefficient forces
\(\gamma_0=1\); nonnegativity then forces a nonzero \(x^d\) coefficient, so
its degree gives \(d=m\).  If \(x\in\Gamma_d\), let \(j\) be the least index
with positive gamma coefficient.  The corresponding basis term has support
endpoints \(j\) and \(d-j\).  A polynomial supported only at exponent one
therefore requires \(j=d-j=1\), hence \(d=2\).  Thus the two root states have
a common gamma darga **if and only if \(m=2\)**.

The same obstruction appears for the \(q\)-leaf cell:

\[
 A=(1+x)^q\in\Gamma_q,\qquad B=x\in\Gamma_2;
\]

the local common-center charge balances exactly at \(q=2\).  For example,
the perfectly unimodal star with three leaves has
\(I=1+4x+3x^2+x^3\), which is not symmetric and hence cannot lie in a single
gamma cone.  Therefore this invariant is sufficient but not necessary for
tree unimodality, and a proof of the full conjecture needs an invariant that
can transport or compare unequal centers.

There is also no purely algebraic rule saying that the sum of two unimodal
state sequences is unimodal.  For instance, padded coefficient sequences

\[
 (1,10,1,1,1),\qquad (0,1,1,10,0)
\]

are individually weakly unimodal, but their sum
\((1,11,2,11,1)\) is not.  This pair is **not asserted to be realizable by a
rooted tree**; it kills only the state-free lemma.  The tree-specific common-
center invariant in Theorem 4 is precisely the additional structure that
repairs the sum step on the proved subclass.

Another tempting induction—"the two rooted states always have a common
mode"—already fails for the center-rooted star when \(m\ge4\): \(B=x\) has
its only mode at one, while \((1+x)^m\) has its mode(s) at the middle.  This
failure occurs even though the resulting star polynomial itself is unimodal.

## 5. Dependency DAG and exact endpoint

The proof dependencies are

\[
 \text{gamma basis}
 \longrightarrow
 \begin{cases}
   \text{semiring closure (Lemma 1)},\\
   \text{coefficient shape (Lemma 2)}
 \end{cases}
 \longrightarrow
 \begin{cases}
   \text{rooted grammar (Lemma 3)},\\
   \text{balanced gluing (Theorem 4)}
 \end{cases}
 \longrightarrow
 \text{double-leafy strict theorem (Theorem 5)}.
\]

The strongest unconditional tree endpoint in this report is Theorem 5:
all double-leafy extensions of arbitrary finite nonempty core trees have a
symmetric, strictly unimodal independent-set sequence.  Theorem 4 is the more
general exact closure statement, conditional only on each supplied rooted
cell satisfying the explicitly checkable common-darga property.  Nothing in
this report resolves trees outside that closure.

## 6. Independent exact diagnostic

Run from the project root:

```bash
python3 experiments/builder_gamma_verify.py --max-n 7
```

The program uses no randomness and only Python integer arithmetic.  For every
labelled base tree of orders \(1\) through \(7\), it:

1. reconstructs the base independence polynomial by brute-force subsets;
2. independently reconstructs it by rooted-pair dynamic programming;
3. constructs the double-leafy edge list and evaluates it by rooted DP;
4. reconstructs (2) directly from the base coefficients and binomial
   coefficients;
5. checks exact equality, degree \(2n\), symmetry, and every strict
   consecutive inequality.

The Prüfer-word enumeration count is also checked against Cayley's exact
\(n^{n-2}\) count.  This diagnostic attacks implementation and indexing
errors only; the symbolic proofs above remain the certificate.

Observed compact success record (Python 3.14.7):

```text
status=PASS; total_labelled_trees=18249;
counts={1:1,2:1,3:3,4:16,5:125,6:1296,7:16807};
code_sha256=7e14a070def0c07b87bb582cc92d123e4d67b31f064448fa5fd24b4e27c77000
```

## 7. Proof-assistant disclosure

No proof assistant was used.  The proof is an exact elementary polynomial and
combinatorial argument, with a separate exact-integer diagnostic program.
