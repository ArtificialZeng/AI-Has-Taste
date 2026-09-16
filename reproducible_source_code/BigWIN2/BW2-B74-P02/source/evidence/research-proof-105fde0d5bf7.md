# Universal proof dossier

Proposer job: `win-00074-p02-research-105fde0d5bf7`  
Date: 2026-09-09  
Frozen source SHA-256:
`1d3e86e773c0cff8e1d4cf1ab82845ff365401ba6a6d9caf6edc554a7a15af15`

## Theorem proved in this dossier

For every field \(K\) and every integer \(c\geq 2\), in
\(R=K[x,y,z]\), let
\[
 I_c=(x^2,y^2,z^c,xyz).
\]
Then
\[
 v(I_c)=2,
 \qquad
 v(\overline{I_c})=\left\lceil\frac c2\right\rceil.
\]
Consequently
\(v(\overline{I_2})<v(I_2)\), equality holds for \(c=3,4\), and
\(v(I_c)<v(\overline{I_c})\) holds exactly for \(c\geq5\).

The proof below also classifies every socle monomial of both ideals.

## 1. Newton polyhedron and integral closure

Put
\[
 w(a,b,d)=c(a+b)+2d
\]
and let
\[
 H_c=\{(a,b,d)\in\mathbb R_{\geq0}^3:w(a,b,d)\geq2c\}.
\]
The Newton polyhedron of the three pure powers is exactly \(H_c\). Indeed,
all three points
\((2,0,0),(0,2,0),(0,0,c)\) lie on \(w=2c\), so their convex hull plus
the nonnegative orthant is contained in \(H_c\). Conversely, take
\(u=(a,b,d)\in H_c\), write \(S=w(u)\), and put \(t=2c/S\leq1\).
Then \(v=tu\) satisfies
\[
 \frac{v_1}{2}+\frac{v_2}{2}+\frac{v_3}{c}=1,
\]
so \(v\) is in the convex hull of the three pure-power exponent vectors,
while \(u-v=(1-t)u\) is in the nonnegative orthant. Thus \(u\) is in that
Newton polyhedron. Finally
\(w(1,1,1)=2c+2\), so the exponent of \(xyz\) already belongs to \(H_c\).
It follows that
\[
 \operatorname{NP}(I_c)=H_c. \tag{1}
\]

For completeness, the associated lattice-point criterion can be proved
directly, without inferring it from finite data. For a nonzero polynomial
\(f\), let \(\nu(f)\) be the least \(w\)-weight among its monomial terms.
Weighted initial forms in the domain \(K[x,y,z]\) give
\(\nu(fg)=\nu(f)+\nu(g)\) and
\(\nu(f+g)\geq\min(\nu(f),\nu(g))\). Every element of \(I_c^i\) has
\(\nu\geq2ci\). If \(f\) is integral over \(I_c\), an equation
\[
 f^n+a_1f^{n-1}+\cdots+a_n=0,
 \qquad a_i\in I_c^i,
\]
cannot have \(\nu(f)<2c\): in that event \(f^n\) has weight
\(n\nu(f)\), while every other summand has weight at least
\[
 2ci+(n-i)\nu(f)>n\nu(f),
\]
so its lowest-weight initial form cannot cancel. Hence every monomial term
of every \(f\in\overline{I_c}\) has weight at least \(2c\).

Conversely, let \(m=x^ay^bz^d\) have
\(S=w(a,b,d)\geq2c\). The product
\[
 (x^2)^{ca}(y^2)^{cb}(z^c)^{2d}
\]
is a product of \(ca+cb+2d=S\) pure-power generators. It divides
\(m^S\), since the three coordinate differences are respectively
\(a(S-2c),b(S-2c),d(S-2c)\), all nonnegative. Therefore
\(m^S\in(x^2,y^2,z^c)^S\subseteq I_c^S\), and the equation
\(T^S-m^S=0\) shows that \(m\) is integral over \(I_c\).
The integral closure of an ideal is an ideal, so sums of these monomials
are also in \(\overline{I_c}\). The two directions prove the exact,
field-independent description
\[
 \overline{I_c}
 =\bigl(x^ay^bz^d:w(a,b,d)\geq2c\bigr). \tag{2}
\]

## 2. Reduction of the v-number to monomial socles

Both \(I_c\) and \(\overline{I_c}\) contain \(x^2,y^2,z^c\), hence are
\(\mathfrak m=(x,y,z)\)-primary. Their only associated prime is therefore
\(\mathfrak m\). For an \(\mathfrak m\)-primary homogeneous ideal \(J\),
the condition \((J:f)=\mathfrak m\) says exactly that the nonzero class of
\(f\) lies in \(\operatorname{Soc}(R/J)=(J:\mathfrak m)/J\).
For a monomial ideal, the standard monomials form a \(K\)-basis and the
socle is spanned by those standard monomials whose products by each of
\(x,y,z\) lie in the ideal. Thus \(v(J)\) is the least total degree among
its socle monomials. This also rules out a lower-degree cancellation from a
non-monomial homogeneous \(f\).

## 3. Complete socle of the original ideal

A standard monomial \(u=x^ay^bz^d\) for \(I_c\) has
\(a,b\leq1\), \(d\leq c-1\), and it cannot have simultaneously
\(a=b=1\) and \(d\geq1\). For such a standard monomial, direct divisibility
by the four generators gives
\[
\begin{aligned}
 xu\in I_c&\iff a=1\ \text{or}\ (b=1\text{ and }d\geq1),\\
 yu\in I_c&\iff b=1\ \text{or}\ (a=1\text{ and }d\geq1),\\
 zu\in I_c&\iff d=c-1\ \text{or}\ a=b=1.
\end{aligned} \tag{3}
\]
Solving (3) is exhaustive. The case \(a=b=0\) fails. If
\((a,b)=(1,0)\), all three conditions force \(d=c-1\), which also has
\(d\geq1\) because \(c\geq2\); the case \((0,1)\) is symmetric. If
\(a=b=1\), standardness forces \(d=0\), and this monomial satisfies all
three conditions. Hence the complete exponent list is
\[
 \operatorname{SocMon}(R/I_c)
 =\{(1,1,0),(1,0,c-1),(0,1,c-1)\}. \tag{4}
\]
Their degrees are \(2,c,c\), so \(v(I_c)=2\).

## 4. Complete socle of the integral closure

By (2), a monomial of weight \(W\) is standard for \(\overline{I_c}\)
exactly when \(W<2c\). Its products by \(x,y,z\) have weights
\(W+c,W+c,W+2\). Thus a standard monomial is a socle monomial exactly when
\[
 2c-2\leq W<2c, \tag{5}
\]
because \(2c-2\geq c\) for \(c\geq2\).

Write \(s=a+b\). The upper inequality in (5) forces \(s\leq1\). If
\(s=0\), then (5) becomes
\(2c-2\leq2d<2c\), whose unique integral solution is \(d=c-1\). If
\(s=1\), then
\[
 c-2\leq2d<c.
\]
For \(c=2q\) the unique solution is \(d=q-1\); for \(c=2q+1\) it is
\(d=q\). In both cases
\(d=\lceil c/2\rceil-1\), and there are the two choices
\((a,b)=(1,0),(0,1)\). Consequently the complete exponent list is
\[
 \operatorname{SocMon}(R/\overline{I_c})
 =\{(0,0,c-1),(1,0,\lceil c/2\rceil-1),
       (0,1,\lceil c/2\rceil-1)\}. \tag{6}
\]
The three degrees are \(c-1,\lceil c/2\rceil,\lceil c/2\rceil\).
Since \(c-1\geq\lceil c/2\rceil\) for \(c\geq2\), (6) proves
\[
 v(\overline{I_c})=\left\lceil\frac c2\right\rceil.
\]

At \(c=2\) this is \(1<2\); it equals \(2\) precisely for \(c=3,4\);
and it exceeds \(2\) precisely for \(c\geq5\), proving every endpoint in
the frozen statement.

## 5. Exact computational cross-check and gap list

On 2026-09-09, rerunning
`python3 evidence/triage_enumerate.py` produced SHA-256
`5f877d2dad81d01b3fbb99f8174566f337069e2c7bdceac3260f193cae11d7ee`,
byte-for-byte equal to `evidence/triage-enumeration.txt`. The script
exhausts the complete standard-monomial box and reproduces (4) and (6) for
every \(2\leq c\leq20\), including the three exceptional endpoint regimes.
This finite check is corroboration only; Sections 1--4 are the universal
proof.

Known mathematical gaps in the argument above: none identified. Independent
referee verification is still required before the result can be accepted.
