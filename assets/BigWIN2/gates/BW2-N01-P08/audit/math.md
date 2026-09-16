# Mathematical referee report

**Verdict: accept the exact frozen candidate.**

Job: `newwin-00001-p08-referee-c2ead421b155`.
Date: 2026-09-12 UTC.
Snapshot digest:
`c96c6b7b2814f0a2007caa6a6a99496edbecadac9ef9bc71fe55d3ecd76309f0`.
Frozen kind: `resolution-paper`. Frozen original status: `proved`.

The submitted coefficient formula and the stronger conclusion of one
simple zero at zero and k-1 distinct strictly negative zeros are correct
for every integer m>=2, n>=1, 1<=k<=n. They resolve source.md with its
original path orientation and consecutive-factor conventions. No part of
the candidate has been weakened, replaced, or repaired for this decision.

## Scope, integrity and review independence

I read source.md, problem.md, claim.json, audit/snapshot.json and the
snapshot's listed evidence, including the actual cited theorem statements.
I reconstructed the decisive argument rather than treating owner-side
assertions or successful computations as certification. No checkpoint.md,
state.json, earlier job transcripts or earlier referee verdicts were
consulted. No subagent, other Codex process or background worker was used.
This is a fresh model review pass, not external human peer review or a
claim of statistical independence.

All eleven listed file hashes and the canonical hash of their mapping were
verified. source.md retains SHA-256
`e6b61e96d2298cfd85d301038ae9142fc908f4efaee7c7ab1638993c5cbf7696`.
The frozen evidence and claim were not edited. New review artifacts are
confined to audit/.

The path height is h=#N-m#E. There are mn north letters and n east letters;
every prefix has h>=0. Peaks and NNE occurrences are literal consecutive
factors, without cyclic counting. Each maximal north run contributes one
peak, and contributes one NNE precisely when its length is at least two.
The claim includes every permitted m,n,k, not just the computed examples.

## Reconstructed counting argument

For a nonempty excursion, take the first return to height zero. Its final
letter is E, starting at height m. Before that letter, mark the last
upward departure from each of heights 0,...,m-1. These steps exist because
upward increments have size one. They occur in increasing height order:
after any such departure the path still has to reach height m, so it has
to depart from every higher marked level later.

The resulting factorization is

    D = N P1 N P2 ... N Pm E P_(m+1).

Each intermediate Pi starts and ends at its displayed base height. If it
dropped below that base, returning to the base would require another
departure from the previous level, contradicting the marked step's last
occurrence. This argument also applies when a down-step skips several
levels. The final suffix is an excursion at zero. Conversely, inserting
any m+1 excursions in this form gives a valid path; the displayed E is
its first return and the marked departures are recovered. Thus the map
is a bijection, including empty components.

Every nonempty component begins with at least m north letters and ends
in E. Since m>=2, a factor ending at an E inside a component cannot acquire
a new preceding N or NN across its beginning: the first component E
already has its two preceding N letters internally. All cross-component
statistic changes therefore occur at the single displayed E. The exhaustive
cases, written as (extra peaks, extra NNE), are:

| Component condition | Increment | Contribution to F-1 |
| --- | --- | --- |
| Pm nonempty | (0,0) | z F^m(F-1) |
| Pm empty, P_(m-1) nonempty | (1,0) | zu F^(m-1)(F-1) |
| Pm and P_(m-1) empty | (1,1) | zut F^(m-1) |

Here F includes the empty path, z counts E letters, u counts peaks and t
counts NNE occurrences. The resulting equation is exactly

    F = 1 + z F^(m-1) [F(F-1)+u(F-1)+ut].

For m=2 the last case still has the two displayed N letters required for
NNE. The argument correctly refrains from substituting m=1 into this
equation, where the component-boundary analysis would change.

Set Y=F-1. The equation Y=z phi(Y), with

    phi(v)=(1+v)^(m-1)[v(1+v)+u(v+t)],

has a unique zero-constant-term formal solution. Lagrange inversion in
Q(u,t)[[z]] is legitimate, and the recursive coefficients are polynomials
in u,t. No analytic limit, convergence assertion, or division by a
specialized value of u or t occurs. Extracting u^k from phi(v)^n gives

    [z^n u^k]F
      = C(n,k)/n * [v^(k-1)] (1+v)^(mn-k)(v+t)^k
      = C(n,k)/n * sum_(j=1)^k C(k,j) C(mn-k,j-1)t^j.

The j=0 contribution would require exponent -1 in the remaining factor
and vanishes. All j=1,...,k coefficients are positive because mn-k>=k.
This proves the claimed formula directly from the frozen definitions.

## Root location and simplicity

The scalar reduction to the ordinary-Dyck family is algebraically exact:

    W^(m)_(n,k)(t)
      = C(n-1,k-1)/C(mn+1,k-1) * V_(mn+1,k)(t).

In the ordinary formula of Wang–Zhang, Theorem 1.1, use semilength
r=mn+1. Then r>=2k+1, so every 1<=j<=k satisfies k+j<=r and the constant
exception is absent. The scalar is positive. Theorem 1.2 therefore yields
real-rootedness, with the underlying ordinary theorem credited to Bóna
et al. The actual hypotheses and pattern definitions were checked in the
[primary text](https://arxiv.org/html/2309.05903v1).

The candidate's second root argument also proves the stronger frozen
claim without relying on that theorem. Put d=k-1, A=mn-k, b=A-d>=1 and
define

    J(x)=sum_(ell=0)^d C(d+1,d-ell) C(d+b,ell)
                      ((x-1)/2)^ell ((x+1)/2)^(d-ell).

Every leading contribution is positive, so deg J=d. Expanding the d-th
derivative of H=(1-x)^(d+1)(1+x)^(d+b) by the product rule verifies

    (1-x)(1+x)^b J(x) = (-1)^d H^(d)(x)/(2^d d!).

For deg q<d, integrate against q and integrate by parts d times. At x=1
and x=-1, H has zeros of orders d+1 and d+b, respectively. Both are at
least d+1, so every boundary term vanishes. Since q^(d)=0, J is orthogonal
to all such q for the strictly positive weight (1-x)(1+x)^b on (-1,1).

If J had fewer than d sign-changing roots there, multiply it by the product
of the corresponding distinct linear factors. The product has one fixed
nonzero sign away from finitely many zeros, so its weighted integral cannot
vanish, contradicting orthogonality. Hence all d roots are distinct and
inside (-1,1); for d=0, J=1. This also excludes repeated, endpoint and
nonreal roots of J.

Termwise substitution gives the polynomial identity

    (1-t)^d J((1+t)/(1-t))
      = sum_(ell=0)^d C(k,ell+1) C(A,ell)t^ell.

The substitution's denominators cancel. t=1 is not a root, since the right
side is positive there. Each root x of J maps injectively to
t=(x-1)/(x+1)<0. These d distinct roots exhaust the degree-d right side,
whose constant term is k. Multiplying by t C(n,k)/n proves exactly one
simple zero at zero and k-1 distinct strictly negative zeros of W.

Degenerate cases were checked explicitly: n=k=1 and all k=1 give W=t;
m=2,k=n gives b=1, still within the positive-weight range. n=0 is only
the auxiliary empty object in F and is not asserted in the source.

## Independent finite checks actually performed

`python3 audit/referee-check.py > audit/referee-check.log` completed
successfully. The new verifier imports no project counting code and uses
only the Python standard library. It appends individual N/E letters,
enforces the prefix inequality after each step, and recognizes NE/NNE
with the literal last two letters. This differs from the submitted
north-run-slot enumeration.

It checked all k=1,...,n at 49 pairs, for 303 polynomials:

- m in {2,3,4,7}, n=1,...,10;
- (2,16), (3,13), (6,11), (11,8), (31,5), (100,3);
- all pairs in the submitted 66-row research-check table, omitting
  duplicate pairs from the preceding lists.

All integer coefficients, peak totals and Fuss total counts match. All
66 serialized submitted coefficient rows were independently recomputed.
Coverage outside that particular submitted table is labeled as such;
it is not asserted to be outside every earlier exploratory computation.

A separately implemented rational Sturm chain, using polynomial division
and positive primitive rescaling, counted exactly k-1 roots of W/t on
(-infinity,0), with gcd(W/t,(W/t)') of degree zero, in all 303 cases.
The chain was also checked on simple known polynomials with two negative
roots, a positive root, a nonreal pair, and a repeated negative root.
Eleven integer-polynomial checks verified the Rodrigues identity and
the denominator-cleared change of variable, including d=0, b=1,
d=15, and b=100. Full inputs, coefficient rows and Sturm signs are in
audit/referee-check.json; the source is audit/referee-check.py.

These are exact finite corroborations. The general word decomposition,
coefficient extraction and orthogonality argument establish the universal
claim. No proof-assistant formalization or floating-point root fit was used.
The submitted 3176-word decomposition run was inspected as owner-side
evidence, but was not rerun or represented as a fresh referee computation.

## Contribution, limitations and final decision

The nearest proved result is the ordinary joint UD/UUD distribution and
real-rootedness due to Bóna et al., reproduced by Wang–Zhang. The present
delta is the enumeration on the specified Fuss family and its exact
positive-scalar identification with that ordinary family. It answers the
whole frozen question and provides exact coefficients and simple-root
information; it is not an arbitrary finite restriction or a claim that
classical Jacobi theory is new.

The [maintained source page](https://www.symmetricfunctions.com/realRootedCatalan.htm)
still states the Fuss conjecture on the review date. In
[Bóna et al. v2](https://arxiv.org/html/2212.10586v2), the multi-pattern
Theorem 1.5 remains about ordinary paths. The nearby augmented-path
enumeration of
[Zhang–Zhuang](https://cs.uwaterloo.ca/journals/JIS/VOL27/Zhuang/zhuang2.pdf),
Lemma 12, counts a different statistic after augmentation. Its use of the
same standard decomposition does not supply the claimed joint Fuss formula.
Details, exact source locations, search queries and limitations are recorded
in audit/referee-sources.md.

No equivalent Fuss identification or resolution was found in the primary
sources inspected. This bounded comparison is not a global priority proof,
and no such priority claim is accepted. The frozen contribution already
states that limitation honestly. There is no unresolved mathematical gap
in the submitted scope and no required substantive revision.

**Final decision: accept**, keeping `resolution-paper` and `proved`
exactly as frozen. The next workflow check is the runner's `check-math`
integrity/provenance gate, followed by manuscript preparation with the
same statement, attribution and bounded novelty language. This report
does not certify a manuscript, bibliography build, PDF or publication.
