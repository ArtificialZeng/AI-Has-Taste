# Gate 5 referee audit: low-degree builder argument

**Audit scope.** I used only the definitions in problem/formal_statement.md and the assertions in proof/builder_notes.md. I did not use the breaker notes or the builder's symbolic-checking code. Exact identities were reconstructed independently with a sparse Laurent-polynomial verifier:

    python3 tests/referee_low_degree_identities.py

The verifier uses rational coefficients and formal independent conjugate symbols; it is not a floating-point test or a proof assistant.

## Verdict

| Degree | Referee verdict | What is actually established |
|---|---|---|
| \(n=2\) | **PROVED** | Theorem 3 is valid for every exact self-inversive quadratic, including ties and repeated/unit-circle roots. |
| \(n=3\) | **PROVED** | Theorem 4 is valid for every exact self-inversive cubic. The endpoint case follows from (1.4), and the non-endpoint case follows from the audited boundary and isolated-zero argument. |
| \(n=4\) | **PARTIAL ONLY** | Theorem 5 is valid, but \(\mathsf C_4\) is not proved on the all-unimodular, non-endpoint stratum \(2\lvert a_4\rvert<A\). |
| \(n=5\) | **PARTIAL ONLY** | Theorem 6 is valid, but \(\mathsf C_5\) is not proved on the all-unimodular, non-endpoint stratum \(2\lvert a_5\rvert<A\). |

No fatal defect was found in the proofs of \(n=2\) or \(n=3\). There are two major incompletenesses, namely Q4-U and Q5-U, and several local or expository repairs listed below.

## 1. Foundational reductions

### 1.1 Phase and scale normalizations

The Hermitian convention (1.1) is valid. If initially

\[
a_k=\omega\overline{a_{n-k}},\qquad |\omega|=1,
\]

then multiplication by a scalar phase \(\lambda\) satisfying
\(\lambda/\overline\lambda=\omega^{-1}\) gives
\(\lambda a_k=\overline{\lambda a_{n-k}}\). Scaling preserves the ratio
\(\rho(P(\mathbb D))/A(P)\), and input rotations preserve the image.

The specific normal forms used later were checked:

- For \(n=2\), Hermitian coefficients can be changed to
  \(r+bz+rz^2\), with \(r>0\) and \(b\in\mathbb R\).
- For \(n=3\), once the middle pair has modulus \(A\), the stated input
  rotation \(z=e^{2i\phi}u\) and output phase \(e^{-3i\phi}\) send that pair
  to \(1,1\), leaving endpoints \(\overline d,d\).
- The forms (4.1) and (5.1) are exactly the even/odd Hermitian forms.

The sentence at lines 17--20 that a conjugate pair can be assigned “any
convenient common phase” is broader than needed and is not literally
compatible with retaining (1.1) for an arbitrary common non-real phase.
The actual normal forms are nevertheless valid. This is **expository**, not
a mathematical gap in the subsequent proofs.

### 1.2 Lemma 1

Lemma 1 is correct.

If \(P(\xi)=w\) for \(|\xi|<1\), the nonconstant holomorphic map \(P\) is open
at \(\xi\), so \(w\) is interior to \(P(\mathbb D)\). Hence a boundary value
has no preimage in \(\mathbb D\). If all roots of \(P-w\) had modulus
strictly greater than one, the positive separation of this finite root
multiset from the unit circle and continuity of polynomial roots would
persist for all nearby values \(w'\); that would put \(w\) in the interior
of the complement. Thus at least one root is unimodular. Dividing out one
such root leaves precisely the other roots, all of modulus at least one.

The proof's “continuity of roots” sentence is adequate for notes, although a
submission should state the positive separation argument or invoke
Rouché on \(|z|=1\). Classification: **expository**.

The zero-value consequence is also correct. For a self-inversive polynomial,
any root outside the unit circle has a reciprocal-conjugate root inside.
Therefore \(0\in\partial P(\mathbb D)\) forces all roots to be unimodular.
Conversely, when all roots are unimodular, \(0\notin P(\mathbb D)\) and is a
boundary value because radial approaches to any unit-circle root map to
zero. The converse is used implicitly in the puncture discussion and should
be stated. Classification: **local**.

### 1.3 Lemma 2

Lemma 2 is correct, including \(h_0=0\) and the equal-product case.

On \(|y|=1\), \(|H^\#(y)|=|H(y)|\). In the strict case
\(|h_0|<|h_m|\), Rouché gives the numerator in (1.3) the same number of
zeros in the disk as \(H\); the numerator has zero constant term and
leading coefficient \(|h_m|^2-|h_0|^2\ne0\), so division by \(y\) leaves
a degree-\((m-1)\) polynomial with all roots in the closed disk. If \(H\)
has unit-circle roots, they are common to \(H\) and \(H^\#\) with the same
multiplicities; one may factor them first, or contract the roots radially and
pass to the limit. If \(|h_0|=|h_m|\), the root-product formula and
\(|\zeta_j|\le1\) force every \(|\zeta_j|=1\), and then
\(h_0H^\#=\overline{h_m}H\).

The phrase “radial limiting argument” does not specify the approximating
polynomials or the preservation of multiplicities. The repair is standard
but should be written out in a submission. Classification: **local**, not
fatal.

### 1.4 Endpoint disk (1.4)

This argument is exact. For

\[
P(z)-w=a_n\prod_{j=1}^n(z-\zeta_j),
\]

the product of root moduli is
\(|a_0-w|/|a_n|<1\), so at least one root lies in \(\mathbb D\).
Thus every \(w\in B(a_0,|a_n|)\) belongs to \(P(\mathbb D)\). All cases in
which an endpoint realizes \(A\) are genuinely complete.

## 2. Degree two

The quadratic normal form (2.1) is valid, and replacing \(z\) by \(-z\)
changes only the sign of \(b\). If \(r\ge b\), (1.4) gives the target
radius. If \(b\ge r\), (2.2) gives

\[
|P(e^{it})-2r|^2=b^2+4r^2\sin^2t\ge b^2.
\]

For \(b>0\), the real roots of \(rz^2+bz-r\) have product \(-1\).
They cannot both be unimodular unless they are \(1,-1\), whose sum is zero;
therefore exactly one root is in \(\mathbb D\). For
\(|w-2r|<b\), Rouché on the unit circle preserves this one interior root,
so \(w\in P(\mathbb D)\). The \(b=0\) case belongs to the endpoint branch.

**Conclusion:** \(\mathsf C_2\) is actually proved. No genericity,
simplicity, or strict coefficient ordering was assumed.

## 3. Degree three

### 3.1 Boundary Schur identity

For (3.1), division gives

\[
\frac{P(x)-P(z)}{x-z}
 =(1+z+dz^2)+(1+dz)x+dx^2.
\]

Reversing its coefficients gives exactly (3.2). Lemma 1 puts its roots in
\(\overline{\mathbb D}\). Its nominal leading coefficient
\(1+z+dz^2\) cannot vanish: otherwise the quotient would have the root
\(x=0\in\mathbb D\), contrary to Lemma 1. This small justification is
omitted in the notes. Classification: **local**.

Independent formal expansion gives

\[
{\cal S}H_z=\frac{P(z)}{z^2}\,[1+(1+z)y],
\]

so (3.3) is correct. Because the boundary value \(P(z)\ne0\), the
equal-product branch of Lemma 2 would make the nonzero right-hand side
identically zero and is impossible. The reduced linear polynomial is stable,
and its root \(-1/(1+z)\) has modulus at most one. Hence
\(|1+z|\ge1\), exactly (3.4).

### 3.2 Inequality (3.6)

For \(z=e^{it}\), with the principal \(t\in[-\pi,\pi]\),
\(|1+z|=2\cos(t/2)\). Thus (3.4) is equivalent to
\(x=\cos(t/2)\in[1/2,1]\). Directly,

\[
\operatorname{Re}\!\left[
 z^{-3/2}(P(z)-C)\right]
=2\cos(t/2)-\frac12\cos(3t/2)
=\frac72x-2x^3.
\]

The remaining terms are purely imaginary. The displayed real part is
positive on the interval. Its second derivative is \(-12x<0\), so the
minimum is attained at an endpoint; both endpoint values are \(3/2\).
Thus (3.6) is valid.

The equality statement at lines 377--378 is too strong if read as equality
in the modulus inequality. The scalar lower bound equals \(3/2\) at
\(t=0,\pm2\pi/3\), but equality
\(|P(z)-C|=3/2\) additionally requires the discarded imaginary part to
vanish. At those three points this requires \(\operatorname{Im}d=0\).
For non-real \(d\), the modulus is strictly larger. This is **expository**
and has no effect on the lower bound.

### 3.3 Isolated value \(w=0\)

This part is valid. If \(0\) is a boundary value, all roots of \(P\) are
unimodular. Gauss--Lucas puts both roots of
\(P'(z)=1+2z+3dz^2\) in the closed disk. The first Schur transform has
coefficients

\[
(6\overline d-2)+(9|d|^2-1)y.
\]

The product condition gives \(|d|\ge1/3\); stability of the transform gives

\[
|6\overline d-2|\le 9|d|^2-1.
\]

In the equality case \(|d|=1/3\), Lemma 2 makes both displayed coefficients
zero, so the same inequality remains valid. Squaring yields (3.9), and
substitution into \(|C|^2\) yields

\[
|C|^2\ge
\frac12+\frac{17}{2}r^2-\frac{27}{4}r^4.
\]

As a concave function of \(r^2\in[1/9,1]\), its minimum is at an endpoint;
the two values are \(49/36\) and \(9/4\). Hence
\(|C|\ge7/6\), and equality is indeed attained by
\((1+z)^3/3\).

### 3.4 Homotopy and disk containment

Let

\[
P_s(z)=s\overline d+z+z^2+sdz^3,\qquad
C_s=\frac12+2s\overline d.
\]

At \(s=0\), \(P_0(z)=C_0\) has the stated interior root. A fully formal
version of the “first loss” argument uses the integer number of roots of
\(P_s-C_s\) in \(\mathbb D\): it is locally constant whenever there is no
unit-circle root, including for small positive \(s\) where the third root
comes from infinity. If membership failed at \(s=1\), the last interior root
would cross the unit circle at a parameter \(s_*\), making \(C_{s_*}\) a
boundary value.

If \(C_{s_*}\ne0\), (3.6) applied to \(P_{s_*}\) would say
\(0=|C_{s_*}-C_{s_*}|\ge3/2\). If \(C_{s_*}=0\), all roots would be
unimodular and the isolated-zero estimate applied to \(sd\) would give
\(|C_{s_*}|\ge7/6\). Both are impossible. Thus \(C\in P(\mathbb D)\).

The notes' first-loss sentence is therefore repairable exactly as above.
Classification: **local**.

Every nonzero boundary point is at distance at least \(3/2\) from \(C\);
the only possible zero boundary point is at distance at least \(7/6\).
Since \(C\) is in the image, a segment from \(C\) to any allegedly omitted
point of \(B(C,1)\) would meet the boundary inside that disk, a
contradiction. In fact the same argument proves the stronger
\(B(C,7/6)\subset P(\mathbb D)\) in the all-unimodular non-endpoint case,
and \(B(C,3/2)\subset P(\mathbb D)\) when not all roots are unimodular.
The line saying that the “proved covering radius is only one” understates
what the preceding estimates prove. Classification: **expository**.

**Conclusion:** \(\mathsf C_3\) is actually proved.

## 4. Degree four

The exact algebra through (4.9) is correct.

For a boundary value \(w\ne0\), reversing the quotient gives (4.3).
The leading coefficient of this reciprocal is nonzero by Lemma 1, and the
strict Schur branch applies: equality would force its Schur transform to
vanish, whereas (4.4) is a nonzero scalar times a nonzero \(K_z\).
Independent expansion confirms (4.4).

With \(u=bz\) and \(S=c+u+\overline u\), the leading coefficient of \(K_z\)
is \(zS\). Exact degree gives \(S\ne0\), while its root product gives
\(|S|\ge|b|\). The next Schur transform has, after multiplication of its
constant term by the unit \(z\),

\[
cS+u^2,\qquad S^2-|b|^2
\]

as constant and leading coefficients. This remains valid in the
equal-product case, where both coefficients vanish. Hence (4.6) holds.
The reverse triangle inequality gives

\[
|c|\,|S|-|b|^2\le |cS+u^2|
\le S^2-|b|^2,
\]

and \(S\ne0\) gives \(|S|\ge|c|\). Thus
\(|S|\ge\max(|b|,|c|)=A\), and the purely imaginary decomposition (4.8)
proves (4.9).

For completeness, the center homotopy is

\[
P_s(z)=s\overline d+\overline bz+cz^2+bz^3+sdz^4,\qquad
C_s=2s\overline d.
\]

At \(s=0\), \(z=0\) maps to \(C_0=0\). Since exact degree gives \(d\ne0\),
\(C_s\ne0\) for \(s>0\), and the nonzero-boundary estimate prevents a first
loss. Therefore \(2\overline d\in P(\mathbb D)\). This fills the local detail
at lines 277--278.

If any root is off the unit circle, reciprocal-conjugate symmetry supplies
an interior root, so \(0\in P(\mathbb D)\); all boundary points are then
nonzero and (4.10) follows. If all roots are unimodular, \(0\) is a boundary
point and the relative set

\[
B(2\overline d,A)\setminus\{0\}
\]

is path connected and contains the nonzero center. It contains no boundary
point by (4.9), hence lies entirely in the image. Thus (4.11) is valid.
When \(2|d|\ge A\), the open disk does not contain zero and the full radius
\(A\) disk follows.

The exact remaining stratum is therefore

\[
\boxed{\text{all four roots unimodular},\quad |a_4|<A,\quad
       2|a_4|<A.}
\]

On this stratum the argument proves only the punctured inclusion, not an
inball of radius \(A\). Q4-U is a **major gap** relative to proving
\(\mathsf C_4\); it is not a defect in the stated partial theorem.

The example \(P=(1+z)^4/6\) has \(A=1\), \(d=1/6\), and zero lies strictly
inside \(B(1/3,1)\). The additional assertion that \(B(1,1)\) is contained
in the image is correct. Indeed, writing \(P=u^4/6\) with
\(|u-1|<1\), and choosing the fourth-root argument in
\([-\pi/8,\pi/8]\) for \(w\in B(1,1)\), the needed radial inequality reduces
to

\[
\frac83\cos^4(\phi/4)-2\cos\phi\ge\frac23
\qquad (|\phi|\le\pi/2).
\]

## 5. Degree five

The exact algebra through (5.6) is also correct. Reconstructing the omitted
degree-four reciprocal quotient and applying Lemma 2 gives (5.2).
For a chosen square root \(q=z^{1/2}\), substitution
\(y\mapsto q^{-2}y\) followed by multiplication by \(q^3\) sends \(K_z\)
exactly to (5.4):

\[
B=bq^3,\quad C=cq,\quad
S=B+C+\overline C+\overline B.
\]

Changing the square-root branch only applies unit changes and does not
affect stability or any modulus inequality.

The first Schur transform of \(L\) has constant and leading coefficients

\[
SC+B^2,\qquad S^2-|B|^2.
\]

Root-product stability, including its equal-product case, gives (5.5), hence
\(|S|\ge\max(|b|,|c|)=A\). The identity (5.6) is exact and its last
parenthesis is purely imaginary.

The same explicit homotopy is

\[
P_s(z)=s\overline d+\overline bz+\overline cz^2
       +cz^3+bz^4+sdz^5,\qquad C_s=2s\overline d.
\]

It starts with the interior preimage \(z=0\), and \(C_s\ne0\) for \(s>0\).
Thus the nonzero-boundary inequality proves \(2\overline d\in P(\mathbb D)\).
The zero-value and punctured-disk topology are identical to degree four.

Consequently the precise remaining stratum is

\[
\boxed{\text{all five roots unimodular},\quad |a_5|<A,\quad
       2|a_5|<A.}
\]

On it, the proof establishes

\[
B(2\overline{a_5},A)\setminus\{0\}\subset P(\mathbb D)
\]

after the Hermitian phase convention, but it does not establish any
radius-\(A\) inball. Q5-U is a **major gap** relative to proving
\(\mathsf C_5\). The phrase “(4.11) remains valid verbatim” should be
replaced by the displayed quintic statement above; this is otherwise only
an **expository** cross-reference issue.

## 6. Gap classification

| ID | Location | Classification | Effect |
|---|---|---|---|
| R1 | Lines 17--20, generic phase wording | Expository | Specific normal forms remain valid. |
| R2 | Lemma 1 root-continuity sentence | Expository | A positive root-separation/Rouché sentence makes it formal. |
| R3 | Converse characterization of zero as boundary | Local | Needed explicitly for the puncture narrative; follows immediately by radial approach. |
| R4 | Lemma 2 with unit-circle roots | Local | Factor common boundary roots or give the radial contraction; statement is correct. |
| R5 | Reciprocal quotient's nominal leading coefficient | Local | It cannot vanish because that would give quotient root \(0\), contradicting Lemma 1. |
| R6 | Degree-three and endpoint homotopies | Local | Root-count continuity supplies a rigorous first-loss argument. |
| R7 | Lines 377--378 equality wording | Expository | The cubic lower bound, not necessarily the modulus, attains \(3/2\) at the listed \(t\). |
| R8 | “proved covering radius is only one” | Expository | The proof actually yields \(7/6\) in the all-unimodular cubic subcase. |
| R9 | Q4-U | **Major** | Prevents a proof or disproof of \(\mathsf C_4\). |
| R10 | Q5-U | **Major** | Prevents a proof or disproof of \(\mathsf C_5\). |
| R11 | Quintic reference to (4.11) | Expository | The analogous punctured inclusion is valid but should be restated. |

There are **no fatal gaps** in the asserted degree-two theorem, degree-three
theorem, or the precisely worded partial degree-four and degree-five
theorems. The builder notes must not, however, be summarized as having solved
the requested frontier \(n=2,3,4,5\): only \(n=2,3\) are complete.

## 7. Proof-assistant disclosure

No proof assistant was used in this referee audit. The independent verifier
is a small exact algebra script using Python integers/Fractions and sparse
Laurent monomials; it checks identities but does not formalize the analytic
or topological arguments.
