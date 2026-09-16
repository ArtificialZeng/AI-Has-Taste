# Independent mathematical referee report

**Verdict: accept the exact frozen candidate.** The proof establishes both
clauses of the original statement, together with the asserted endpoint identity
and elementary coefficient properties. There is no mathematical scope reduction
or substantive correction. The contribution is a uniform proof of the
higher-index statement posed in the inspected arXiv source. The candidate's
explicitly bounded literature claim is retained; this report does not certify
absolute priority or the contents of the unavailable later journal body.

## Review identity and frozen inputs

- Job: `primary-20260913-chen-ulc-failure-referee-c4f4e634158a`.
- Review date: 2026-09-13 Asia/Shanghai (2026-09-12 UTC).
- Snapshot: `4556257bb02194676513831cafeed05699982a8fd956a67820a92eda025f8ae5`.
- Frozen kind: `resolution-paper`; frozen original status: `proved`.
- Original `source.md` SHA256:
  `35bf7999e659653cddadf84048b691931a7e0d0d3064a2f0020c7603c780731b`.

I read `source.md`, `problem.md`, `claim.json`, `audit/snapshot.json`, and the
eight evidence files enumerated by the claim (including the two original
statement files). All nine snapshot file hashes, including `claim.json`, match.
I independently recomputed the digest of the sorted, compact JSON file mapping.
The original source and every frozen input were left unchanged.

This was a fresh referee context. I did not read `checkpoint.md`, `state.json`,
earlier job transcripts, earlier audit verdicts, or progress summaries. Assertions
of correctness within the authorized proof dossier and problem interpretation
were not used as evidence. No agents, other Codex processes, or background
workers were started. The mathematical assessment below is based on reconstructed
arguments and a separately written exact verifier.

## Exact scope and reconstruction

Write \(d=m-1\) and

\[
D_{m,j}=j(m-1-j)a_j^2-(j+1)(m-j)a_{j-1}a_{j+1}.
\]

The claim requires strict negativity for both polynomial families at every
integer \(4\le j\le m-2\), and a failing internal index for each \(m\ge4\).
It additionally asserts \(D_{m,m-2}=-m\), nonnegative integer coefficients, and
monicity of degree \(m-1\). These are exactly the properties verified below.

**Polynomial facts and the small cases.** With \(z=s+1\), the proposed geometric
sums give

\[
f_{2r}=s\sum_{\ell=0}^{r-1}(s+1)^{2\ell},\qquad
f_{2r+1}=1+s(s+1)\sum_{\ell=0}^{r-1}(s+1)^{2\ell}.
\]

Multiplying each expression by \(s+2=z+1\) recovers the original numerator.
The expressions establish integrality, nonnegativity and a leading coefficient
of one. Direct subtraction gives \(h_m=f_m+(-1)^m\). For odd \(m\), this only
removes the constant 1; for even \(m\), it adds a constant 1 to a polynomial
with zero constant coefficient. Hence all asserted elementary properties hold
for both families, and their \(D_{m,j}\) agree whenever \(j\ge2\).

Descending comparison in the original quotient identity gives the top three
coefficients

\[
(a_{m-3},a_{m-2},a_{m-1})=
\left(\frac{m^2-5m+8}{2},m-2,1\right).
\]

All three indices are positive for \(m\ge4\), so this holds for \(h_m\) too.
Substitution yields

\[
D_{m,m-2}=(m-2)^3-(m-1)(m^2-5m+8)=-m.
\]

In particular, the internal indices \(j=2\) at \(m=4\) and \(j=3\) at \(m=5\)
have differences \(-4\) and \(-5\). The empty higher-index range in these two
cases leaves no gap in the non-ULC existence assertion.

**Normalization and coefficient extraction.** Put

\[
b_j=\frac{a_j}{\binom{m-1}{j}}.
\]

The binomial ratios imply exactly

\[
D_{m,j}=j(m-1-j)\binom{m-1}{j}^{2}
              (b_j^2-b_{j-1}b_{j+1}).
\]

This is normalization by the actual degree, including when \(a_0=0\).
The fundamental theorem of calculus gives the polynomial identity

\[
f_m(s)=m\int_0^1[-1+(s+2)t]^{m-1}\,dt.
\]

Division by \(s+2\) initially verifies it for \(s\ne-2\); polynomial identity
then includes \(s=-2\). Expanding the finite binomial sum and substituting
\(x=2t-1\) gives

\[
b_j=\frac{m}{2^{j+1}}\int_{-1}^1(1+x)^j x^{m-1-j}\,dx.
\]

There are no infinite series or limiting interchanges in this step.

For \(p=j-1, k=m-j-2\), let

\[
M_r=\int_{-1}^1x^{k+r}(1+x)^p\,dx,
\qquad H(p,k)=M_0M_2-M_1^2.
\]

The full nonempty target domain is in bijection with the integer pairs
\(p\ge3, k\ge0\), by \(j=p+1, m=p+k+3\). Extracting the adjacent normalized
coefficients from the same four moments gives

\[
b_{j-1}=\frac{m}{2^j}M_2,\quad
b_j=\frac{m}{2^{j+1}}(M_1+M_2),\quad
b_{j+1}=\frac{m}{2^{j+2}}(M_0+2M_1+M_2).
\]

Consequently

\[
b_{j-1}b_{j+1}-b_j^2=\frac{m^2}{2^{2j+2}}H(p,k).
\]

All prefactors used to transfer strict positivity to \(D_{m,j}<0\) are
strictly positive on the target domain.

**Uniform positivity, including odd \(k\).** If \(k\) is even,
\(x^k(1+x)^p\,dx\) is a finite nonnegative measure, with positive density on
\((0,1)\). Strict Cauchy–Schwarz for \(1,x\) gives \(H(p,k)>0\): equality would
require \(x\) to be constant almost everywhere on an interval of positive
density.

Fix instead an odd \(k\ge1\). For every integer \(p\ge1\), each of
\(M_0,M_1,M_2,M_3\) is positive. When \(k+r\) is even, its integrand is
nonnegative with positive density on \((0,1)\). When \(k+r\) is odd, reflection
gives

\[
M_r=\int_0^1x^{k+r}\big((1+x)^p-(1-x)^p\big)\,dx>0.
\]

In particular, division by \(B=M_1\) in the induction is legitimate.
For \(A=M_0, B=M_1, C=M_2, D=M_3\), set \(E=BD-C^2\).
The measure \(x^{k+1}(1+x)^p\,dx\) is nonnegative and has moments \(B,C,D\),
so the same strict Cauchy–Schwarz argument proves \(E>0\). This is an
auxiliary nonnegative measure; no Cauchy–Schwarz inequality is applied to the
signed density \(x^k(1+x)^p\).

At the base \(p=3\), direct integration gives

\[
A=\frac6{k+2}+\frac2{k+4},\quad
B=\frac2{k+2}+\frac6{k+4},\quad
C=\frac6{k+4}+\frac2{k+6},
\]

and hence

\[
H(3,k)=\frac{64(k+1)}{(k+2)^2(k+4)^2(k+6)}>0.
\]

I checked its common numerator independently as
\(16[(2k+7)(2k+11)(k+2)-(2k+5)^2(k+6)]=64(k+1)\).
Every denominator is positive for odd \(k\ge1\).

Multiplication of the integrand by \(1+x\) gives
\(M_r(p+1,k)=M_r(p,k)+M_{r+1}(p,k)\). Therefore

\[
\begin{aligned}
H(p+1,k)&=(A+B)(C+D)-(B+C)^2\\
        &=H+(AD-BC)+E\\
        &=\left(1+\frac CB\right)H+
          \left(1+\frac AB\right)E.
\end{aligned}
\]

The final equality is the algebraic identity
\(B(AD-BC)=CH+AE\). Both coefficients are positive, and \(E>0\) at every
step independently of the induction hypothesis. Starting at \(p=3\) proves
\(H(p,k)>0\) for every integer \(p\ge3\), at each fixed odd \(k\ge1\).
Together with the even case, this covers all target pairs. The moment
reduction, equality of positive-degree coefficients, and endpoint calculation
prove every assertion in the frozen claim.

## Independent exact checks actually run

I wrote and ran `python3 audit/referee-verify.py`; its serialized output is
`audit/referee-verify.json`. This standard-library verifier does not import or
execute `evidence/research-verify.py`, and does not overwrite frozen evidence.
It divides each original numerator separately by \(s+2\), and evaluates moments
using a different finite expansion:

\[
M(p,q)=2^{p+1}\sum_{\ell=0}^{q}
 \frac{\binom q\ell2^\ell(-1)^{q-\ell}}{p+\ell+1}.
\]

All arithmetic is exact integers or rational `Fraction` arithmetic. Results:

- Both families for every \(4\le m\le512\): 1,018 polynomial checks,
  257,556 strict-negative target-minor checks, and 1,018 endpoint checks passed.
- Every target index for \(6\le m\le42\): all 703 coefficient-to-moment and
  determinant-normalization checks passed.
- The rectangle \(3\le p\le25, 0\le k\le39\): all 920 positivity checks,
  460 odd-\(k\) induction checks, and 20 odd-\(k\) base checks passed.
- Formal multiplication of univariate polynomials verified the base's
  numerator coefficients \([64,64,0,0]\) in ascending powers of \(k\).
- The outside-domain negative control \(p=2,k=1\) gave
  \(H=-16/225\) and \(D_{6,3}=6\). Thus the implementation detects the opposite
  sign below the cutoff; extending the uniform target to \(j=3\) would fail.

Fresh `pdftotext -layout` extraction of the frozen primary PDF is saved as
`audit/referee-source-extraction.txt`. Its bytes equal the frozen extraction.
I read the defining equations and the relevant statements from that fresh
extraction as well as the listed source text.

These finite checks support the formulas, independently of the proposer code.
The infinite conclusion rests on the proof above. No floating-point sign test,
formal proof assistant, or machine-checked infinite theorem is claimed.

## Source comparison and contribution assessment

The decisive primary is Stephanie Chen,
[arXiv:2503.16296v2](https://arxiv.org/pdf/2503.16296v2), whose frozen PDF hash
matches `source.md`. Definition 2.4 and equations (2.14)–(2.15), pp.8–9,
give the degree-based normalization. Equations (3.1),(3.3), p.10, define the
same polynomials. Proposition 3.8, p.16, already establishes failure of ULC
somewhere. Conjecture 3.9 on that page asks for failure throughout
\(4\le j\le m-2\), after computation through \(m=100\). Proposition 3.10,
pp.18–19, addresses order \(m\), a different inequality. Its positive
order-\(m\) statements do not imply the required negative order-\((m-1)\)
minors. The contradictory low-index phrase concerning even \(h_m\) in
Proposition 3.8 is immaterial: the present proof does not use it.

The precise contribution is the all-parameter higher-index theorem. It is
neither a repetition of the already-known existence clause nor a finite
extension of the original computations. The signed-moment argument supplies
a self-contained way to prove the prescribed strict reverse inequalities
where a direct positive-measure argument would be invalid. It resolves a
specific source conjecture for the original two recursion families, with no
arbitrary restriction. This is a coherent, nontrivial contribution at the
frozen scope.

I performed a fresh bounded web comparison. The
[live arXiv record](https://arxiv.org/abs/2503.16296) still displayed v2 dated
4 April 2025. Queries used the exact title and identifier, author with
`Conjecture 3.9`, author with `105666`, the PII with `Conjecture` and
`coefficients`, the title with `3.10`, and the family names with proof,
conjecture, ULC and signed moments. No primary resolution of the exact
uniform statement was located. Secondary summaries and problem registries
were not used to establish correctness or present open status.

The [publisher's indexed article preview](https://www.sciencedirect.com/science/article/abs/pii/S0393044025002517)
for DOI 10.1016/j.geomphys.2025.105666 displays the same polynomial families
and the known non-ULC classification in Proposition 1.2, referring to
Proposition 3.9. It does not expose the higher-index conjecture's disposition.
Direct opens of the article, its abstract page and the Elsevier article XML
endpoint returned tool access errors; the full journal body was not inspected.
This is an access limitation, not evidence that the journal lacks the theorem
or that the mathematical problem remains open today.

The bounded contribution claim in `claim.json` is supportable: an elementary
full proof of the statement conjectured in the inspected arXiv version, with
no equivalent proof located in the sources searched. Absolute priority and
the later journal body's treatment remain unverified, as the frozen candidate
already states. The acceptance does not remove that qualification. Any later
discovery of an equivalent prior theorem must trigger contribution reassessment,
rather than being hidden behind this audit.

## Gaps, disposition and next step

No mathematical gap, missing case, invalid theorem hypothesis, or unsupported
infinite extrapolation was found. In particular, the argument treats the
empty target ranges, the actual polynomial degree, the signed density, strict
inequalities, nonzero divisors and both parities. No substantive revision is
requested.

**Accept** the unchanged `resolution-paper` / `proved` candidate under the
given snapshot. The runner may next perform `check-math` and proceed to its
authorized writing phase if that provenance/integrity gate passes. The report
does not itself claim the runner's gate passed. Publication wording must
retain the bounded literature statement; inspecting the complete journal
version is the specific remaining source-comparison test that could change
the contribution assessment. No manuscript or research PDF was created in
this referee job.
