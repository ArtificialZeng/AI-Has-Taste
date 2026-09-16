# Fresh mathematical referee report

## Frozen scope and verdict

I reviewed the exact `resolution-paper` claim frozen by snapshot digest
`97a8fec3482eede8fdc9f545e6d76765b8211128fcf3f75f3eba34adedd11a4f`.
All six hashes in `audit/snapshot.json` agree with the files reviewed, including
the primary PDF hash
`0b2d8edbed7c6b69ef0f9edd7e106e919c7a2f5976f845e16b3758528a32fe2c`.
The mathematical verdict is **accept**. The candidate correctly disproves the
source theorem's general order-six assertion and proves the stronger claimed
Q-order-four statement for the specified diagonal family. It does not silently
replace that scope by a weaker one.

## Reconstruction of the decisive argument

Let (R=I-AX), (Y=X(2I-AX)), and (Z=AY=I-R^2). Direct expansion of the
source's equation (1.4), without changing the residual convention, gives

\[
 I-Z\bigl((2+\nu)I-(1+\nu)Z\bigr)
   =-\nu R^2+(1+\nu)R^4. \tag{1}
\]

For (A=I_3), (R=t\operatorname{diag}(1,2,3)), and the Frobenius norm,

\[
 \nu=\frac{(1+16+81)t^4}{(1+4+9)t^2}=7t^2,
\]

so (1) gives exactly

\[
 R_+=t^4\operatorname{diag}(-6,-12,18)
      +7t^6\operatorname{diag}(1,16,81). \tag{2}
\]

The quartic coefficient is nonzero. Hence

\[
 \frac{\|R_+\|_F}{\|R\|_F^6}
 =\frac{\|(-6+7t^2,-12+112t^2,18+567t^2)\|_2}
        {14^3t^2}\longrightarrow\infty.
\]

This already rules out a uniform sixth-order local estimate. More decisively,
the candidate establishes the order along each fixed orbit, rather than relying
only on this one-step family.

After the first step write

\[
 R_k=c_k\operatorname{diag}(-a_k,-b_k,1),\qquad q_k=c_k^2,
\]

and put

\[
 m=\frac{a^4+b^4+1}{a^2+b^2+1},\qquad d=1-m+qm.
\]

Coordinatewise substitution in (1) gives

\[
 a^+=\frac{a^2(m-a^2-qma^2)}d,\quad
 b^+=\frac{b^2(m-b^2-qmb^2)}d,\quad
 q^+=q^4d^2. \tag{3}
\]

At (q=0), the first two components (P_1,P_2) satisfy the exact identities
(P_1+P_2=1) and (P(a,b)=(a,b)) on (a+b=1). The exact defect identity is

\[
 1-a^+-b^+
 =\frac{q(a^4+b^4+1)^2}
 {a^2-a^4+b^2-b^4+q(a^4+b^4+1)}. \tag{4}
\]

I separately checked the no-exit estimates on the claimed box. On that box,
(L=a^2-a^4+b^2-b^4\ge3123/10000>153/500),
(1+a^2+b^2\le689/400), and therefore (d>1/6). Also
(a^4+b^4+1<27/20), (m<1), and both sign-preserving numerators in (3)
are positive. The supplied factorizations yield

\[
 |P_1-a|\le  e,\qquad |P_2-b|\le3e,
 \quad e=1-a-b,
\]

using only rational endpoint bounds; the respective crude coefficient bounds
are already (<1) and (<3). Differentiating (3) in (q) gives the displayed
bounds (6) and (21) (the latter is substantially loose). Consequently

\[
 e^+\le6q,quad q^+\le2q^4,quad
 |a^+-a|\le e+6q,quad |b^+-b|\le3e+21q. \tag{5}
\]

For (u=t^2\le10^{-4}), the exact first-step parameters are

\[
 a_1=\frac{6-7u}{18+567u},\quad
 b_1=\frac{12-112u}{18+567u},\quad
 e_1=\frac{686u}{18+567u},\quad
 q_1=u^4(18+567u)^2.
\]

Direct rational cross-multiplication verifies the claimed entry bounds;
indeed (q_1<4\cdot10^{-14}<10^{-12}). Summing (5), up to any hypothetical
first exit, gives total variations (<1/200) for (a) and (<13/1000)
for (b). These are smaller than the initial margins to every ratio face.
Equation (4) and (q^+\le2q^4) exclude the remaining faces. Thus the
first-exit argument is noncircular and the whole nonterminating orbit stays in
the box.

With (S_k=(1+a_k^2+b_k^2)^{1/2}), the invariant bounds give

\[
 c_{k+1}=c_k^4d_k,\qquad \frac16<d_k<1,qquad
 1<S_k<\frac43.
\]

It follows exactly that, for every (k\ge1),

\[
 \frac{27}{512}\|R_k\|_F^4
 <\|R_{k+1}\|_F
 <\frac43\|R_k\|_F^4. \tag{6}
\]

The summable variations make ((a_k,b_k)) Cauchy, while (4) forces its
limit to satisfy (a_\infty+b_\infty=1). The box keeps both limiting
coordinates positive. Passing to the limit in

\[
 \frac{\|R_{k+1}\|_F}{\|R_k\|_F^4}
 =\frac{d_kS_{k+1}}{S_k^4}
\]

therefore gives

\[
 \frac{1-m_\infty}{S_\infty^3}\in(0,\infty).
\]

This proves Q-order exactly four for every fixed (0<t\le10^{-2}), and
establishes that the quartic behavior is persistent.

## Source comparison and proof defect

The hash-verified primary PDF states in Theorem 2.1 that CTM has order six
for a nonsingular complex matrix whenever the initial residual satisfies its
stated hypothesis. Its equations (1.4), (2.1), and (2.4) agree with the update
and residual used above. Thus (2) is a counterexample under the source's own
convention, not an adapted algorithm.

In equation (2.7), the source treats a term known only to be quartic in the
error as ϵ_k times the fourth power with ϵ_k tending to zero. The preceding
estimate supplies only a bounded normalized coefficient. Equations (2) and
(6) show that this coefficient stays nonzero on the audited family. The next
sentence makes an independent quantifier error: from “for every fixed
ϵ>0, eventually ϵ_k\leϵ” it substitutes the moving value
ϵ=\|e_k\|^2. That does not produce a single eventual index and would require
the additional estimate ϵ_k=O(\|e_k\|^2)), which is false here.

The result refutes the general sixth-order conclusion. It does not claim
nonconvergence and does not classify other CTM orbits. The source proof also
uses the stronger residual restriction (\sigma<3^{-1/3}) for its convergence
argument, but that separate scope discrepancy is not needed for this
counterexample; the audited initial interval satisfies even that stronger
restriction.

## Checks performed, contribution, and remaining gaps

I inspected the actual source update and theorem in PDF pages 2--4, recomputed
the residual map and diagonal recurrence, ran the frozen symbolic verifier
(all identities returned zero), and independently checked the rational bounds
used for box entry, invariance, derivative control, and the two-sided quartic
estimate. The source PDF and every decisive evidence file match the frozen
snapshot.

The contribution is nontrivial: it combines an exact counterexample to a newly
stated general theorem with a complete invariant-region and Q-order analysis
of an explicit interval of initial data. The frozen dossier reports only a
limited literature search and makes no priority claim; I do not elevate that
search to proof of novelty. No unresolved mathematical gap remains within the
exact frozen claim.
