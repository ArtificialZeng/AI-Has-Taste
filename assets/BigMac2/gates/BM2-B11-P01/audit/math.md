# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the exact frozen `result-note` claim in `claim.json`, not a weakened
version of the original problem.  The original problem remains unresolved: the
candidate proves an exclusion through active grade six and concludes only
\(7\le n_{\min}(4)\le 8\); it does not claim to decide dimension seven.  I
recomputed the SHA-256 hashes of `claim.json`, `source.md`, `problem.md`, and all
four files under `evidence/` listed in `claim.json`.  Every hash agrees with
`audit/snapshot.json`, whose digest is
`29258eb36e7e703e2b489996282ae99cc7e049febb6d67fd89adb45f5582213d`.
The immutable `source.md` also has its recorded hash
`5fcdf705252e8804eb53fdd3c5e490cbf2ddb4af6e976c28d00544df0a32de26`.

## Imported results checked in the primary source

I inspected the actual frozen PDF, not only the dependency summary.  Physical
pages 6--9 define the active spectral reduction, the monic degree-four
orthogonal polynomial \(P_k\), and \(H_k>0\); equation (G.5) gives the signed
one-block map (with sign \(+1\) at even restart length); (G.7) is the signed
two-block recurrence; (G.8)--(G.10) give monotone bounded energy and vanishing
same-parity chords; and Proposition 1.4 gives parity factor convergence,
fixedness of every omega-limit state, and resonant support of size between five
and eight.  These hypotheses apply to every nonterminating orbit after active
spectral reduction.  Thus the dossier's imported dynamics package has the
right normalization and scope.

Physical pages 103--104 state the exact eight-dimensional counterexample at
restart length four.  Physical page 143 explicitly leaves the smallest
counterexample dimension as a natural question.  Hence the cited nearest
result supplies the upper bound but not the candidate's grade-six exclusion.
The available comparison supports only this bounded statement; it is not a
general priority certification.

## Reconstruction of the six-node argument

Assume a nonterminating orbit with six distinct active nodes
\(\lambda_1<\cdots<\lambda_6\), all positive, and put
\(\Delta(t)=\prod_i(t-\lambda_i)\), \(D_i=\Delta'(\lambda_i)\).  For
\(x_i=w_{k,i}P_k(\lambda_i)\), orthogonality gives four Vandermonde equations.
Their two-dimensional nullspace is
\(x_i=(c_0+c_1\lambda_i)/D_i\).  Since
\(\langle P_k,t^4\rangle=H_k\), while
\(\sum_i\lambda_i^j/D_i=0\) for \(j\le4\) and equals one for \(j=5\),
\(c_1=H_k\).  Consequently a unique real \(a_k\) satisfies
\[
 w_{k,i}P_k(\lambda_i)=H_k\frac{\lambda_i-a_k}{D_i},
 \qquad
 w_{k+1,i}=\frac{(\lambda_i-a_k)P_k(\lambda_i)}{D_i}.
\]
When support remains full, the monic quintic \((t-a_k)P_k(t)\) alternates
sign at the six nodes.  It therefore has one simple zero in each node gap;
\(a_k\) occupies exactly the gap omitted by the four zeros of \(P_k\).

Applying the annihilator identity at consecutive times makes
\((t-a_k)P_kP_{k+1}-H_{k+1}(t-a_{k+1})\) divisible by \(\Delta\), with a
monic cubic quotient \(B_k=(t-a_k)L_k+u_k\).  Evaluating at \(a_k\) and then
dividing by \(t-a_k\) gives, without an unrecorded division assumption,
\[
 a_{k+1}-a_k=\frac{\Delta(a_k)}{H_{k+1}}u_k,
 \qquad
 P_kP_{k+1}=H_{k+1}+\Delta L_k+u_kK_{a_k},
\]
where \(K_a=(\Delta-\Delta(a))/(t-a)\) is a polynomial even at the formal
level.  Substitution at the nodes in (G.8) gives the stated nonnegative energy
identity for \(u_k^2\).

At a full-support omega-limit point, resonance at all six nodes gives
\(P_eP_o=h+\Delta L\), with monic quadratic \(L\).  The one-block weight
formula and \(P_eP_o=h\) on the nodes show that the two limiting phases have
the same parameter \(a\) and omit the same node gap \(I\).  Factor convergence
then keeps every sufficiently late \(a_k\) in that fixed gap.

For either limiting quartic \(P\), the two equations defining the monic
quadratic \(J_P\) are nonsingular.  Indeed, a homogeneous solution would give
\(P\mid d\Delta-e\), with \(d,e\) linear; multiplying by \(L\) and reducing
with \(P_eP_o=h+\Delta L\) yields the polynomial identity
\(eL+hd=0\), which forces \(d=e=0\).  Thus \(J_P\) and
\(\mathcal L_P(f)=[t^3]\operatorname{rem}_P(J_Pf)\) vary continuously near
both limits.  The functional kills constants, \(P\mathbb P_3\), and
\(\Delta\mathbb P_1\).  Applying it to the difference of two consecutive
product identities gives exactly
\[
 u_{k+1}\mathcal L_{P_{k+1}}(K_{a_{k+1}})
 =u_k\mathcal L_{P_{k+1}}(K_{a_k}).
\]
At a limiting factor, Lagrange interpolation at its four simple roots gives
\(\mathcal L_P(K_a)=Q(a)\), where \(Q\) is the opposite limiting factor.
Neither limiting factor has a zero on the closed omitted gap.  Compactness and
continuity therefore make the two functional values nonzero and of the same
sign for all late \(k\).  The case \(u_k=0\) propagates as zero; otherwise
\(u_k\) has an eventual fixed sign.  Since \(\Delta\) also has a fixed sign
on \(I\), the drift formula makes \(a_k\) eventually monotone and bounded.
Its convergence, together with the weight formula and parity factor
convergence, proves convergence of both parity weight vectors.

## Boundary, signs, and quantifiers

If no omega-limit point has all six nodes, Proposition 1.4 makes every
omega-limit support a five-node set.  On a fixed five-node support \(S\), the
one-dimensional Vandermonde annihilator gives
\(w_iP(\lambda_i)=h/(\Delta_S'(\lambda_i))\), so the limiting factor and
support determine at most one weight vector.  Only six supports exist.  A
same-parity sequence has step size tending to zero, so its compact omega-limit
set is connected; a connected subset of this finite set is a singleton.
Thus both parity weight sequences converge also in the boundary case.

If a coordinate vanishes at a finite block, active grade drops.  Grade at most
four terminates.  At grade five the same annihilator calculation gives
\(P_k(\lambda_i)P_{k+1}(\lambda_i)=H_{k+1}\) on every active node.  Equation
(G.8) then forces \(H_{k+1}=H_k\), and (G.7) makes the signed two-block
multiplier exactly one.  Repeated eigenvalues and initially zero coordinates
reduce to these active-grade cases, so no simplicity or full-support
hypothesis is lost.

Finally, after parity weights converge, every coordinate with positive limiting
weight is resonant and has signed two-block multiplier tending to
\(q_\infty(\lambda_i)/h=1\); that multiplier is eventually positive.  Its sign
therefore stabilizes, while coordinates of zero limiting weight vanish.  This
upgrades squared-weight convergence to convergence of the signed normalized
residual directions, exactly as required by the frozen claim.

I specifically checked the empty/lower-grade cases, finite support loss,
repeated eigenvalues, possible zero denominators, the \(u_k=0\) equality case,
root-gap stability, and the compactness/uniformity used in sign transport.  I
also ran the supplied standard-library exact-rational verifier successfully;
it reported all four division/drift/energy checks, all three transport checks,
and all four limiting-functional checks as passing.  This computation is
regression evidence only; the reconstruction above is the correctness basis.

## Contribution and verdict

The exclusion is not a routine consequence of Proposition 1.4: that proposition
permits resonant omega-limit supports through eight nodes, whereas the new
six-node annihilator, completion functional, and sign-transport invariant rule
out nonconvergent motion at active grade six.  It closes one of the three
dimensions left between elementary termination and the cited construction and
has the direct use of narrowing the frozen minimum to \(7\) or \(8\).  The
claim honestly leaves dimension seven and the original problem unresolved.

**Verdict: accept.**  The frozen scope, mathematical correctness/evidence, and
partial-result contribution all pass.  I found no required revision to the
candidate claim or decisive evidence.
