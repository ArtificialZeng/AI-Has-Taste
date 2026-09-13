# Fresh mathematical referee report

## Frozen scope

I reviewed the exact `resolution-paper` claim frozen by snapshot digest
`ab3e4198491bf587813a4e9409d5ead91b272ae82481f039447827d825db8405`.
It quantifies over every integer (n\ge 2), every monic irreducible degree-
(n) modulus over \(\mathbb F_2\), the polynomial coordinate basis, and the
full Boolean matrix space including singular matrices.  I recomputed every
file hash in the snapshot and the canonical snapshot digest before assessing
the proof.

## Reconstruction of the proof

Let (c_A=\bigoplus_{C\subseteq A}G(1_C)) be the vector ANF coefficient.
If an input assignment has Hamming weight below (n), then its value under
(G) is zero.  Indeed, when (u=0), the inversion factor is zero.  When
(u\ne0), the matrix has at most (n-2) nonzero entries, hence rank at most
(n-2), so all ((n-1))-minors and therefore its adjugate vanish.  Thus every
term in the subset sum defining (c_A) is zero when (|A|<n).  Since
(G(I,u)=J_{n,p}(u)) is nonzero, the support is nonempty, and the first set in
any support ordering has size at least (n).  This proves (L(G)\ge n).

For the upper bound, put \(\alpha=t\bmod p\) and take (i=1).  Irreducibility
and (n\ge2) imply that the constant coefficient of (p) is one, and

\[
 \alpha^{-1}=\alpha^{n-1}+a_{n-1}\alpha^{n-2}+\cdots+a_2\alpha+a_1.
\]

Let (v=J_{n,p}(e_i)).  For (n\ge3), choose (r=n-1), so (v_r=1) and
(r\ne i).  For (n=2), the only allowed modulus is
(t^2+t+1); choosing (r=0) again gives (v_r=1) and (r\ne i).

For (k=0,\ldots,n-1), define \(\sigma_k(h)=h+k\pmod n\),
(c_k=\sigma_k(r)), and

\[
 A_k=\{p_{h,\sigma_k(h)}:h\ne r\}\cup\{u_{\sigma_k(i)}\}.
\]

At (1_{A_k}), the matrix is a rank-((n-1)) partial permutation matrix
with zero row (r) and missing column (c_k), while multiplication by the
operand gives (e_i).  Directly checking the cofactor orientation specified
in the frozen problem gives

\[
 \operatorname{adj}(P^{(k)})=e_{c_k}e_r^{\mathsf T}.
\]

Every proper subset of (A_k) has weight below (n), so all its evaluations
vanish.  Consequently

\[
 c_{A_k}=G(1_{A_k})=e_{c_k}e_r^{\mathsf T}v=e_{c_k}\ne0.
\]

Hence all (A_k) are in the joint support.  They are pairwise disjoint:
for each row (h\ne r), the cyclic shifts use every column exactly once,
and the operand indices also run through all coordinates exactly once.  Their
union contains all operand variables and all matrix variables outside row
(r).  Order these (n) supports first.  Each introduces exactly (n)
variables, and only the (n) entries of row (r) remain unseen afterward.
Appending every other supported monomial in any order can therefore introduce
at most (n) new variables at any step.  Thus (L(G)\le n), completing the
universal equality.

## Adversarial checks

- The proof uses the full Boolean domain and, essentially, singular rank-
  ((n-1)) matrices; it does not replace the domain by \(GL_n\).
- The coefficient calculation respects the transposed row/column placement in
  the frozen adjugate convention.  Cofactor signs cause no issue over
  \(\mathbb F_2\).
- The special case (n=2) is valid and is not covered by the (r=n-1)
  choice; the separate (r=0) argument closes it.
- No division by zero occurs: the displayed inverse is taken only for the
  nonzero element \(\alpha\), and (J(0)=0) is used elsewhere.
- The upper-bound ordering need not enumerate or characterize the remaining
  support.  Once the prefix leaves only one row unseen, the definition itself
  bounds every later increment by (n).
- `audit/referee_verify.py` independently uses list-of-lists matrices and a
  separately implemented exact field-arithmetic path.  It rechecked the
  snapshot, all 230 proposed prefix coefficients for every irreducible modulus
  in degrees (2\) through (7), and the complete ANFs for (n=2,3).  The
  complete support sizes, degree extrema, and coordinate-monomial counts match
  the frozen exact data.  This finite computation is corroboration, not a
  premise of the proof.

## Source comparison and contribution

I inspected the cited primary PDF directly.  Its Definition 11 and
Definitions 13--14 define the same full-space raw map and joint-support leap.
Its Theorem 17 proves only the universal lower bound (L(G)\ge n).  Table 1
and Appendix A.3 give exact values and finite support-prefix certificates only
for (n=3,4), and the conclusion lists exact general raw ANF values as a
future direction.  The reviewed cyclic family supplies the missing uniform
upper bound for every allowed modulus and therefore settles the frozen claim,
rather than merely treating a fixed modulus or finite dimension.  The bounded
literature record does not establish priority, and the candidate correctly
does not assert priority beyond that screen.

## Verdict

**Accept.**  The proof is complete at the exact frozen scope, its edge cases
and quantifiers check out, and the explicit cyclic prefix is a substantive
full resolution relative to the nearest cited result.  I found no unresolved
mathematical gap requiring revision.
