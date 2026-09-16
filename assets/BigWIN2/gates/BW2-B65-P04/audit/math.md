# Fresh mathematical referee report

## Frozen scope and source check

I reviewed the claim frozen by snapshot
af2adbacd1e5aa8b5c28901066e152027aaf75c09dab1693cf4ebcbe472474f4.
The SHA-256 digests of claim.json, source.md, problem.md, and every listed
evidence file agree with audit/snapshot.json. The submitted claim is the full
assertion from source.md, under the precise conventions in problem.md: for
every $s,t\geq0$ with $N=3s+4t\geq4$, the complement of
$sC_3\sqcup tC_4$ has rigidity dimension equal to its Maxwell dimension.

I checked the hash-fixed primary paper itself. Its Theorem 1.4 proves
Maxwell-sharpness only when the maximum-degree-two complement has no
$C_3$- or $C_4$-component, and the paragraph immediately following the
theorem explicitly identifies those exclusions as limitations of that
argument. Corollary 1.5 gives the stated lower bound involving $\sigma$.
Thus the submitted family is outside Theorem 1.4. The source comparison does
not make a priority claim, and none is needed for this full resolution of the
frozen problem.

## Reconstructed decisive argument

The edge count is

\[
 |E(G)|=\binom N2-N=\frac{N(N-3)}2.
\]

Writing $d=N-1-a$, direct substitution shows that the Maxwell inequality in
dimension $d$ is equivalent to $a(a+1)/2\geq N$. Hence, for the least $a$
satisfying that inequality,

\[
 M(G)=N-1-a.
\]

It remains to prove rigidity in this dimension. I reconstructed the central
symmetric-product lemma as follows. For an $N\times a$ row matrix $Z$, a
linear relation among the tensors $z_i\odot z_j$, over the edges of
$D=sC_3\sqcup tC_4$, is equivalent, up to nonzero factors of two, to

\[
 Z^{\mathsf T} C Z=0
\]

for a nonzero symmetric matrix $C$ supported on the edges of $D$. If
$\operatorname{rank}(C)=r$, congruence reduces the fiber calculation to
$X^{\mathsf T}X=0$ for an $r\times a$ matrix $X$. On the rank-$k$ locus,
the column space is a totally isotropic $k$-plane. Its dimension is

\[
 k(r-k)-\frac{k(k+1)}2,
\]

and the matrices spanning a fixed such plane contribute $ak$ dimensions.
The maximum occurs at $k=\min(a,\lfloor r/2\rfloor)$. Consequently the
codimension of the compression fiber is exactly

\[
c_a(r)=
\begin{cases}
h(2a-h+1)/2,&r=2h<2a,\\
a+h(2a-h-1)/2,&r=2h+1<2a,\\
a(a+1)/2,&r\geq2a.
\end{cases}
\]

I independently checked the rank-stratum accounting. A nonzero weighted
triangle block has rank/dimension $(2,2)$ or $(3,3)$, while a weighted
four-cycle block, written as
$\left(\begin{smallmatrix}0&B\\B^{\mathsf T}&0\end{smallmatrix}\right)$,
has rank/dimension $(2,3)$ or $(4,4)$. If $u,v,x,y$ count active blocks of
these four types, then

\[
r=2u+3v+2x+4y,\qquad \ell=2u+3v+3x+4y=r+x.
\]

For $r\geq2a$, one has $\ell\leq N\leq a(a+1)/2=c_a(r)$. For
$r=2h<2a$, $x\leq h$, so $\ell\leq3h$, and

\[
c_a(2h)-(3h-1)=\frac{h(2a-h-5)+2}{2}\geq0.
\]

The only arithmetic equalities are $(a,h)=(2,1)$ and $(3,2)$. Equality in
the preceding stratum bound would respectively require one or two active
four-cycle blocks, contradicting $N\leq3$ or $N\leq6$. For
$r=2h+1<2a$, odd rank forces an active rank-three triangle block, hence
$x\leq h-1$ and $\ell\leq3h$. Then

\[
c_a(2h+1)-(3h-1)
=\frac{2a+h(2a-h-7)+2}{2}>0.
\]

Thus every projectivized nonzero rank stratum has dimension $\ell-1$
strictly less than its compression codimension. The corresponding incidence
variety has dimension less than $aN$, so its projection cannot cover the
space of $Z$. Therefore the $N$ cycle-edge tensors are independent for
generic rows whenever $N\leq a(a+1)/2$. I also exhaustively enumerated all
active rank patterns satisfying the edge budget for $1\leq a\leq30$; all
57,274,123 patterns satisfy the same strict inequality. This enumeration is
a check on, not a substitute for, the uniform inequalities above.

The passage to rigidity is valid. The independence locus is a nonempty
Zariski-open set defined over $\mathbb Q$. Since $N-1\geq a$, it meets the
open set where deleting any row of $Z$ leaves rank $a$. The kernel of
$Z^{\mathsf T}$ is then contained in no coordinate hyperplane, so it
contains a rational vector with all coordinates nonzero. Scaling the rows by
that vector preserves tensor independence and makes their sum zero. Extending
the all-ones vector to a basis $[\mathbf1\ P]$ of
$\ker Z^{\mathsf T}$ produces an affinely spanning realization in
$d=N-a-1$ dimensions.

For this realization, the complete-framework stress matrices are precisely
$Z\Psi Z^{\mathsf T}$, with $\Psi\in\operatorname{Sym}_a$. Restriction to a
deleted edge $ij$ is the functional $z_i^{\mathsf T}\Psi z_j$.
Independence of the deleted edge tensors makes this restriction map onto.
By elementary row-space/kernel duality, surjectivity is equivalent to every
deleted rigidity row lying in the span of the undeleted rows. Deleting $D$
therefore preserves the complete graph's full rigidity rank. A full-rank
rational specialization makes the relevant rigidity minor a nonzero
polynomial, so the generic rank is full. This proves generic $d=M(G)$
rigidity. Maxwell's necessary count supplies the reverse bound on
$\operatorname{rig}$. The $N=4,d=0$ boundary case is compatible with the
same argument and with the stated zero-dimensional convention.

## Ancillary exact checks

I ran all three supplied verifiers with Python 3. The perturbative exchange
check reproduced $2q(27q+10)$, the old determinant $-1$, the exchange minor
20, and the nonzero zero-sum-scaled determinant 383616. The separate
Gale-extension check reproduced determinants $-1$ and $-3,616,140$. The
rigidity-certificate verifier independently reconstructed all graphs and
deterministic integer placements and verified 41 affine-span and nonzero
maximal-minor certificates modulo 65521, covering every feasible pair through
28 vertices. These checks support the setup and boundary behavior; the
universal conclusion rests on the uniform incidence argument, not on finite
computation.

## Verdict

**Accept.** The proof settles the exact frozen universal claim. I found no
unresolved mathematical gap, hidden weakening, unsupported limiting step, or
degenerate exception. The full-scope resolution-paper classification and
original_status: proved are justified.
