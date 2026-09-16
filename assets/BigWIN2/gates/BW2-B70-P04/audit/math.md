# Fresh mathematical referee report

## Scope and verdict

I reviewed the exact frozen `resolution-paper` claim bound to snapshot
`f2fe0048732affad34e18fc192abb34ea9864f6299cf6bf655ee47934ff9386e`.
The claim is that the multiplicity-weighted count in
\(\operatorname{Re}s\ge 0.73\), \(0<\operatorname{Im}s\le 8596696\) is one,
and that the specified closed radius-\(10^{-6}\) disk contains one simple
zero. I accept that claim. The argument covers the full frozen scope; it does
not rely on treating the source paper's targeted numerical search as
exhaustive.

I recomputed all hashes in `audit/snapshot.json`; `claim.json` and every listed
evidence file matched the frozen digest mapping. The review used the frozen
source, interpretation, claim, snapshot, and only the evidence enumerated by
the claim.

## Source result and reduction of the domain

The archived Mantovanelli preprint proves in Theorem 1.1/Proposition 3.1 that
\(Z_F(s)\ne0\) for \(\operatorname{Re}s\ge\sigma_F\), including the edge,
and that \(\sigma_F<0.75\). Proposition 7.1 gives the necessary phase-lock
inequalities (17)--(20) for a zero with
\(1/2\le\sigma<\sigma_F\). Thus every zero relevant to the count but not
already excluded by the source theorem lies in
\[
  0.73\le\sigma<\sigma_F<0.75,
  \qquad 0<t\le8596696.
\]
The paper's final displayed zero is explicitly the product of a targeted,
nonexhaustive search. Consequently the exact census certified here is a real
delta from the cited source rather than a restatement of its numerical table.

## Reconstruction and check of the ordinate cover

On the above strip, monotonicity from Lemma 2.1 and direct rigorous bounds
give
\[
 H(\sigma)<0.045602822,\quad K(\sigma)<0.402314890,
\]
as well as
\(2^{-\sigma}>0.594603557\),
\(3^{-\sigma}>0.438691337\), and
\[
 R(\sigma)>\sum_{\substack{5\le n\le90\\n\ne6,12}}F_n^{-3/4}
 >0.75746608.
\]
I independently reevaluated these inequalities with 384-bit Arb balls. The
corresponding angular bounds in `phase_cover.py` are outward bounds for (17)
at bases 2 and 3 and for every nonvacuous instance of (20), namely
\(F_n=5,13,21,34,55,89\). The next free value, \(F_{13}=233\), already gives
a chord bound greater than 2, after which the individual bound is vacuous.

The decimal enclosures of \(\pi\) and the required logarithms were checked by
Arb, and the conversion of each odd-\(\pi\) phase window to the \(10^{-9}\)
grid rounds the lower endpoint down and the upper endpoint up. Intersecting
these periodic closed covers is therefore a necessary-condition cover, not a
sampling procedure.

For the joint pruning, put
\(w_n=F_n^{-3/4}\),
\(S(t)=\sum_{5\le n\le30,\ n\ne6,12}w_nF_n^{-it}\), and
\(W=\sum w_n\). Since \(w_n\le F_n^{-\sigma}\), (18) implies
\[
 W-\operatorname{Re}(\overline\omega S(t))\le H(\sigma)<H_{\rm up}.
\]
Hence either necessary consequence
\(W-|S(t)|\le H_{\rm up}\), together with the restriction from (19)
\(\omega=-e^{i\alpha}\),
\(|\alpha|\le0.348764756\), may safely exclude an ordinate box. The code uses
interval upper bounds for the maximum projection over 24 covering alpha
subarcs; an inconclusive terminal box is retained whole. This establishes the
direction of every pruning implication and rules out false exclusion through
rounding.

The resulting closed necessary cover consists of exactly these eight
intervals:

1. [893451.166593898, 893451.296590004]
2. [1045810.765660011, 1045810.914566694]
3. [1292959.408434021, 1292959.524502041]
4. [1431405.026953860, 1431405.066784306]
5. [2302570.625261012, 2302570.893936211]
6. [2396445.266260887, 2396445.372661887]
7. [2688164.836889199, 2688164.901257748]
8. [8596695.022433829, 8596695.288582920].

I reran the constant certification, exact periodic intersections, and 59,741
joint interval tests; the independently produced interval bytes had SHA-256
`9f574a6d680d682f931d6f1e09580815e693a7e6b70760563da2020df01f3c70`,
matching the frozen cover. This rerun supplements, but does not replace, the
implication and rounding audit above.

## Uniform analytic exclusion of all other boxes

Let \(P_{140}(s)=\sum_{n=1}^{140}F_n^{-s}\) and
\(q=\varphi^{-0.73}\). The elementary bounds
\(F_n\ge\varphi^{n-2}\) and \(F_n\le\varphi^{n-1}\) give, uniformly for
\(\operatorname{Re}s\ge0.73\),
\[
 |Z_F-P_{140}|<10^{-20},\qquad
 |Z_F'-P_{140}'|<10^{-18}.
\]
Direct finite summation plus the derivative tail gives
\(|Z_F'|<3.79\). The geometric majorant
\[
 (\log\varphi)^2\sum_{k\ge1}(k+1)^2q^k
 =(\log\varphi)^2\frac{q(4-3q+q^2)}{(1-q)^3}
\]
is less than 16 and bounds \(|Z_F''|\). I rederived and reevaluated all four
bounds at 384-bit precision; their respective upper values were approximately
\(2.101\times10^{-21}\), \(1.440\times10^{-19}\),
\(3.789075\), and \(14.947983\).

For a closed box \(B\), center \(m\), and half-sum of side lengths \(r_1(B)\),
integration along a line segment gives
\[
 |Z_F(s)-P_{140}(m)|
 \le10^{-20}+3.79r_1(B),\qquad s\in B.
\]
Thus the strict lower-modulus comparisons in the certificate prove
nonvanishing on the corresponding entire closed boxes, rather than only at
their centers.

I parsed the serialized rational endpoints independently and reconstructed
the deterministic bisection tree from each of the eight initial closed
rectangles. The 127 leaves form the exact recursive cover: 122 have a strict
nonvanishing inequality and five are wholly contained in the frozen disk.
At fresh 384-bit precision I recomputed all 122 partial sums and every one of
the strict inequalities passed. Exact corner-distance calculations also
confirmed the five disk containments. This checks both the analytic labels and
the absence of a gap in the box cover.

## Disk count and multiplicity

Let \(c=0.730178633163+8596695.206382i\), \(r=10^{-6}\), and
\[
 L(s)=P_{140}(c)+P_{140}'(c)(s-c).
\]
The recomputed enclosures give
\[
 |P_{140}(c)|<1.500649\times10^{-6},\qquad
 |P_{140}'(c)|>3.272560,
\]
so the unique zero of the linear function is at distance less than
\(4.58555\times10^{-7}<r\) from \(c\). On \(|s-c|=r\),
\[
 |L(s)|>1.7719116\times10^{-6}.
\]
The value tail, derivative-tail allowance, and Taylor remainder are bounded
by
\[
 10^{-20}+10^{-18}r+\tfrac12(16)r^2
 <8.000000011\times10^{-12}.
\]
The strict Rouché margin is therefore greater than
\(1.7719036\times10^{-6}\). Rouché's theorem gives exactly one zero counted
with multiplicity in the disk and also excludes a boundary zero. Total
multiplicity one implies one distinct zero and simplicity.

The disk lies strictly above the bottom boundary, inside the eighth phase
interval, to the right of \(0.73\), and below \(t=8596696\). The source theorem
handles the unbounded right side and the line \(\sigma=\sigma_F\); the closed
box certificates include \(\sigma=0.73\), phase endpoints, and any possible top
boundary point. Hence no counted boundary or omitted part of the quantified
region remains untreated.

## Final decision

The phase cover is a rigorous necessary cover, the box certificates exclude
its complement to the frozen disk, and the strict Rouché calculation gives
one simple disk zero. Therefore
\[
 N_{0.73}(8596696)=1,
\]
and both requested disk assertions are true. Verdict: **accept**.
