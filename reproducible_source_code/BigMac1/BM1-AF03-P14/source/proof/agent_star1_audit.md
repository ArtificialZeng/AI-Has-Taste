# Adversarial audit of the `star1` exact certificate

## Verdict

The mathematical certificate in `certificates/star1_exact_certificate.json`
is correct for its stated scope.  An independent reconstruction confirms that
the relative ordered full-support closure

\[
N=\{(0,1)\},\qquad a_0\geq a_1\geq a_2\geq a_3\geq a_4>0
\]

has exactly one critical orbit after scaling:

\[
(\alpha,\alpha,1,1,1),\qquad
\alpha=\frac{24+\sqrt{69}}{13},
\]

and its tangent Hessian has signature \((-,-,-,+)\).  Thus it is a saddle.
No mathematical defect was found in `proof/agent_star1_report.md` or in the
current certificate.

Five fail-closed defects were found in the initial
`src/builder_verify_star1.py`.  They
are JSON typing/canonicalization defects, not defects in the accepted
mathematical instance: the verifier accepts duplicate JSON keys, a reordered
Bernstein table with a refreshed digest, an unreduced resultant content
rational, `False` in place of the integer survivor value zero, and `True` in
place of the integer dimension one.  The independent audit rejects all five.

## Independent method and trust separation

The audit script `src/breaker_star1_audit.py` imports no builder, discovery,
verifier, or other project module.  It uses three deliberately separated
exact paths:

1. a standard-library `Fraction` sparse-polynomial engine for the chamber,
   all 32 subsets, critical numerators, margins, and simplex Bernstein
   conversion;
2. an independently generated Singular program for the residual ideal,
   resultant, irreducibility, and bidirectional ideal inclusion;
3. a small direct implementation of the quadratic field
   \(\mathbb Q[\alpha]/(13\alpha^2-48\alpha+39)\) for the full tangent
   Hessian Gram matrix.

The only serialized data imported from the certificate are treated as
untrusted and compared with independently reconstructed objects.

## Chamber and wall reconstruction

Let

\[
r=1-x-z,
\qquad y=\frac r2+u,
\qquad x,z,r,u,w\geq0,
\]

with

\[
(a_0,a_1,a_2,a_3,a_4)
=(1+w+z+y+x,1+w+z+y,1+w+z,1+w,1).
\]

The independent reconstruction gives the ten signed pair margins

\[
\begin{array}{c|c@{\qquad}c|c}
01&2u&02&r\\
03&r+2z&04&r+2z+2w\\
12&r+2x&13&r+2x+2z\\
14&r+2x+2z+2w&23&2r+2x+2z+2u\\
24&2r+2x+2z+2u+2w&34&2r+2x+4z+2u+2w.
\end{array}
\]

Here 01 is the high margin and the other nine are low margins.  The four
order margins are

\[
x,\qquad r/2+u,\qquad z,\qquad w.
\]

Thus the five advertised inequalities are both necessary and sufficient for
the whole relative chamber closure.  The audit also reconstructed all five
polygon margins in the nonnegative basis \(x,z,r,u,w\):

\[
\begin{array}{c|l}
i&\sum_j a_j-2a_i\\ \hline
0&2x+4z+3r+2w\\
1&4x+4z+3r+2w\\
2&4x+4z+4r+2u+2w\\
3&4x+6z+4r+2u+2w\\
4&4x+6z+4r+2u+4w.
\end{array}
\]

In particular, no dominant-coordinate boundary is hidden in the chart.
Deleting the last pair wall or flipping the 01 sign is rejected by both
verifiers.

The word “closure” here is necessarily relative to \(a_4>0\), because the
gauge is \(a_4=1\).  Support-loss faces \(a_4=0\) are outside this certificate
and must be handled in the separate support-stratum analysis.  The original
report states \(a_4>0\), so this is a scope clarification rather than a flaw.

## Independent numerator and critical equations

At the strict rational sample

\[
(x,y,z,w)=(1/4,3/4,1/4,1/3),
\]

the audit selected the positive parts directly among all 32 subsets.  Exactly
16 subsets are active, and their alternating truncated-power sum agrees
coefficient-by-coefficient with

\[
P=T^4-\sum_i(T-a_i)^4
 +\sum_{i<j}(T-a_i-a_j)^4
 -2(T-a_0-a_1)^4.
\]

Writing \(S=\sum a_i^2\), \(D=\prod a_i\), the four independently
differentiated polynomials are

\[
H_q=S_qPD+2SP_qD-2SPD_q.
\]

For every \(q\), the audit also verified the separate quotient-rule identity

\[
D\,\partial_q(SP^2)-2SP^2D_q=P H_q,
\]

which reconstructs the critical numerator from
\(F^2=SP^2/(24^2D^2)\) without reusing the displayed derivative formula.

On a subset-sum wall the adjacent numerator differs by \(L^4\).  Its first
three derivatives vanish at \(L=0\), so the same first-derivative equations
are valid throughout the chamber closure.  This also suffices for the
candidate Hessian, which lies strictly away from every subset-sum wall.

## Bernstein identity and zero set

The audit recomputed

\[
K=-6H_x+7H_y-8H_z+4H_w
\]

after substituting the chart.  If

\[
K=\sum_{p,q}c_{pq}(u,w)x^pz^q,
\]

the independent power-to-Bernstein formula used was

\[
b_{ij}(u,w)=
\sum_{p\leq i,\ q\leq j}
c_{pq}(u,w)\frac{(i)_p(j)_q}{(9)_{p+q}}.
\]

Expanding the resulting 55 degree-nine simplex basis terms reconstructs
\(K\) exactly.  The independently obtained canonical table has:

- 55 rows;
- \(b_{00}=0\);
- 1620 strictly positive parameter-monomial coefficients among the other
  rows;
- minimum positive coefficient 2;
- a positive constant term in each of the 54 nonzero \(b_{ij}\);
- positive endpoint witnesses \(b_{9,0}\) and \(b_{0,9}\);
- canonical row digest
  `d47de13461dbd9d8d06ff8a896b0986ede3410a448f1da3722a74250610015b3`.

Consequently \(K\geq0\) on the closed simplex.  If \(x>0\), the
\((9,0)\) basis term is positive; if \(z>0\), the \((0,9)\) term is
positive.  Hence

\[
K=0\quad\Longleftrightarrow\quad x=z=0.
\]

This includes the face \(x+z=1\), its endpoints, \(u=0\), and all compatible
coordinate-order intersections.  Sixty-four seeded exact rational points,
plus the simplex vertices and the face \(x+z=1\), were used only as
adversarial consistency checks; the positivity table, not these samples, is
the proof.

## Residual ideal and real branches

On \(x=z=0\), the independently reconstructed equations satisfy the exact
identities

\[
16H_x=(w+1)^2(2u+2w+3)A,
\qquad
-16H_z=(w+1)(2u+2w+3)B,
\]

with exactly the serialized polynomials \(A,B\).  Since the displayed
factors are positive on \(u,w\geq0\), every critical point lies in
\(V(A,B)\).

Singular 4.4.1 independently returned:

- `vdim(std(A,B)) = 15`;
- zero normal forms for every generator of \(\langle A,B\rangle\) modulo
  the claimed five-component intersection;
- zero normal forms in the reverse direction;
- exact equality of the computed resultant with the serialized factorization;
- irreducibility over \(\mathbb Q\) of all five univariate component
  polynomials.

Each component is a graph \(c w+g(u)=0\) over an irreducible univariate
factor.  It is therefore prime over \(\mathbb Q\).  The bidirectional ideal
containment proves the stated equality with their intersection, and hence
also proves radicality and completeness; this is stronger than merely
checking that the listed points vanish.

The exact semialgebraic rejection is:

1. \(4u^2+4u+3\) has discriminant \(-32\).
2. The component with \(84u^2-52u+1\) forces \(w=-2/3\).
3. The cubic component forces \(2w+2u+3=0\).
4. All seven coefficients of the sixth-degree component polynomial are
   positive.
5. The remaining component is
   \(w=0,\ 52u^2-36u-15=0\).  Its constant and leading coefficients have
   opposite signs, so it has one positive and one negative root.

The positive root gives

\[
u=\frac{9+2\sqrt{69}}{26},\qquad
\alpha=u+\frac32=\frac{24+\sqrt{69}}{13}.
\]

All four original \(H_q\), not just \(H_x,H_z\), reduce to zero modulo
\(52u^2-36u-15\).  Substitution \(u=\alpha-3/2\) gives

\[
52u^2-36u-15=4(13\alpha^2-48\alpha+39).
\]

The interval \(12/5<\alpha<5/2\) isolates the larger root exactly.  At the
candidate the high margin is \(2u>0\), every top-small low margin is 1, and
every small-small low margin is \(2(u+1)>0\); it lies on no subset-sum wall.

## Full Hessian audit

The ambient numerator \(P\), all five first derivatives, and all 25 second
derivatives were rebuilt before evaluation in
\(\mathbb Q[\alpha]/(13\alpha^2-48\alpha+39)\).  The audit did not rely only
on one vector from the two-dimensional small-block representation.  It used
the full tangent basis

\[
\begin{aligned}
L&=(1,-1,0,0,0),\\
S_1&=(0,0,1,-1,0),\\
S_2&=(0,0,1,1,-2),\\
C&=(3,3,-2\alpha,-2\alpha,-2\alpha).
\end{aligned}
\]

Every vector has zero dot product with
\((\alpha,\alpha,1,1,1)\).  For the reconstructed logarithmic Hessian
\(M\), all six off-diagonal Gram entries vanish exactly and the diagonal is

\[
\operatorname{diag}\left(
\frac{-54388-71136\alpha}{864435},
\frac{-5468+1664\alpha}{66495},
3\frac{-5468+1664\alpha}{66495},
\frac{-2580+1248\alpha}{169}
\right).
\]

The isolating interval makes the first three entries negative and the fourth
positive.  The audit also obtained

\[
P(\alpha,\alpha,1,1,1)=\frac{3(32\alpha-13)}4>0.
\]

At a critical point, the Hessian of the section volume is the positive
factor \(F\) times this logarithmic Hessian on the sphere tangent space.
Therefore the signature is exactly \((-,-,-,+)\).

## Fail-closed audit and mutations

`src/breaker_star1_audit_tests.py` ran eleven cases against both the original
builder verifier and the independent audit.  Six ordinary mathematical/wall
mutations behaved correctly: the valid certificate was accepted, while a
deleted wall, flipped high-pair sign, changed Bernstein coefficient with a
refreshed digest, changed residual polynomial, and changed Hessian form were
rejected.

The following five malformed but semantically equivalent encodings were
accepted by the initial verifier and rejected by the independent audit:

| mutation | original verifier | independent audit | cause |
|---|---:|---:|---|
| duplicate top-level `schema` key with the same value | accept | reject | standard `json.loads` silently keeps the last duplicate |
| swap two Bernstein rows and refresh digest | accept | reject | row index set is checked, canonical row order is not |
| change resultant content `[1024,1]` to `[2048,2]` | accept | reject | content rational lacks a gcd/canonical check |
| change survivor `w: 0` to `w: false` | accept | reject | Python has `False == 0` |
| change a symmetry dimension `1` to `true` | accept | reject | Python has `True == 1` in dictionary equality |

These are genuine defects relative to the user-required fail-closed and
canonical-input contract.  They do not furnish a counterexample to the
mathematical theorem and do not change the meaning of the current untouched
certificate.  The release verifier was subsequently repaired to reject
duplicate object keys while parsing JSON, require the explicit `(i,j)` row
sequence, reduce the resultant content rational, and apply a strict
non-boolean integer decoder to `w` and all dimension values.  The same
eleven-case suite now requires both the release verifier and the independent
audit to reject all ten corruptions; the repaired record is
`audit/star1_audit_mutations.json`.

## Artifacts and reproduction

Artifacts produced by this audit:

- `src/breaker_star1_audit.py`;
- `src/breaker_star1_audit_tests.py`;
- `experiments/breaker_star1_independent_audit.json`;
- `experiments/breaker_star1_audit_mutation_tests.json`.

Reproduction:

```bash
python src/breaker_star1_audit.py \
  certificates/star1_exact_certificate.json \
  --output experiments/breaker_star1_independent_audit.json \
  --seed 140120260829 --random-checks 64

python src/breaker_star1_audit_tests.py \
  --output experiments/breaker_star1_audit_mutation_tests.json
```

The audited certificate SHA-256 is
`70cf7f980c89ff36e6b07ccecde268bcde6d8cf5f9da171759b5d8ba5c0e3fa7`.
The main audit used Python 3.13.5 and Singular 4.4.1 on arm64 macOS.  The
seed was `140120260829`; all 64 sampled checks were rational and secondary
to the exact certificates.

No Lean, Coq, Isabelle, or other proof assistant was used.  The conclusion
is limited to the stated positive-support ordered `star1` chamber closure;
it makes no claim about other chambers or support-loss strata.
