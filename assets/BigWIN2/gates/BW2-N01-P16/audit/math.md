# Independent mathematical referee report

**Verdict: accept the exact frozen candidate.**

Job: `newwin-00001-p16-referee-4056b1fc8f93`.
Review date: 2026-09-12 UTC.
Snapshot digest: `9fc8e436106b8c04421db7d93377be9559d2fcb31f8c7e7f46bc8f326c0f9c85`.
Frozen kind: `resolution-paper`. Frozen original status: `proved`.

The submitted argument proves that every odd primitive non-deficient
integer with exactly five distinct prime divisors satisfies
\(\min_i p_i^{a_i+1}<2\prod_i p_i\). All five exponents are arbitrary
positive integers, all primes are unbounded, and equality \(\sigma(n)=2n\)
is included. This is the unchanged original assertion, not a subsidiary
classification accepted in its place. No substantive repair of the
submitted argument was required.

## Inputs and integrity

I read `source.md`, `problem.md`, `claim.json`, `audit/snapshot.json`, and
the evidence files listed in that snapshot. I used the skill's referee
instructions and read the complete release contract before producing the
audit JSON. I did not consult checkpoint/state files, owner verdicts,
earlier job transcripts, or unlisted local research materials. No agents,
other model processes, or background workers were used.

All 12 frozen file digests match. The snapshot digest also matches the
SHA-256 of its sorted-key, compact JSON file mapping; that mapping is
exactly `claim.json` plus the claim's evidence list. The source remains
byte-identical, with SHA-256
`8b4fed18ea31443b084f7ff6a5cca49f4221bce85a82b8c026ce64f0a125e6d2`.
Fresh `pdftotext -layout` extraction from the frozen primary PDF has hash
`36e58e57f90775162d6b175874ad19be6d164b348dd0e07708c360c76c8fa05c`,
exactly the frozen primary text's hash.

The new verification artifacts are `audit/referee_verify.py` and
`audit/referee-checks.json`. The script imports neither submitted program
and does not execute either program or modify any frozen input. Reproduce
its checks from the project root with:

```sh
python3 audit/referee_verify.py
```

## Reconstruction of the universal reduction

For \(h(m)=\sigma(m)/m\), the prime-power geometric series gives

\[
h(n)=\frac{R}{D}\prod_{i=1}^5(1-b_i^{-1}),\qquad
D=\prod_i(p_i-1),\quad b_i=p_i^{a_i+1}.
\]

Every factor is strictly between zero and one. Thus \(h(n)\ge2\)
implies \(R/D>2\), including when \(h(n)=2\). Consequently
\(E=R-2D\) is a positive odd integer. If \(p_1\ge5\), the decreasing
function \(t/(t-1)\) and distinctness give
\(R/D\le85085/46080<2\), using primes \(5,7,11,13,17\).
Hence \(p_1=3\).

Assume the negation of the desired strict bound: \(b_i\ge2R\) for all
five indices. Since \(n/3\) is a positive proper divisor, primitivity gives
\(h(n/3)<2\). Direct expansion, using the same full radical, gives

\[
h(n/3)=\frac RD(1-3/b_1)\prod_{i=2}^5(1-1/b_i).
\]

This identity remains valid for \(a_1=1\): its first local factor is
\((3/2)(1-1/3)=1\). The elementary inequality
\(\prod_i(1-u_i)\ge1-\sum_i u_i\) for \(0\le u_i\le1\) follows by
induction from \(1-P(1-u)=1-P+Pu\le1-P+u\), with \(0\le P\le1\).
Applying it to the losses \(3/b_1,1/b_2,\ldots,1/b_5\) yields

\[
2>h(n/3)\ge\frac{R-7/2}{D}
 =2+\frac{E-7/2}{D}.
\]

As \(D>0\), this forces \(E<7/2\); positivity and parity leave exactly
\(E=1,3\). Modulo 3, either some other prime is 1, giving \(D\equiv0\)
and \(E\equiv0\), or all four other primes are 2, giving \(D\equiv2\)
and \(E\equiv2\). Thus \(E=1\) is impossible. These arguments use no
limit, exponent truncation, classification of perfect numbers, or
unproved external theorem.

## Completeness of the gap-3 certificate

For a prime prefix define \(A=\prod p\), \(B=\prod(p-1)\), and
\(g=A-2B\). Adding a prime \(q\) changes the gap to \(qg+2B\).
If a proper nonempty prefix had positive gap, then \(g\ge1\), \(B\ge2\),
and its next extension would have gap greater than 3. Subsequent
extensions increase a positive gap. Zero gap is impossible because
\(A\) is odd. Therefore every proper prefix of a gap-3 radical is
strictly negative. This validates all submitted sign pruning, including
discarding the three-prime gap 3 at \((3,5,13)\).

The inequality \(R/D>2\) forces \(p_1=3\) as above. If \(p_2\ge15\),
then \(R/D\le(3/2)(15/14)^4<2\), since
\(151875<153664\). Thus \(p_2\in\{5,7,11,13\}\). For fixed
\(p_2=p\), the bound
\(R/D\le[3p/(2(p-1))][t/(t-1)]^3\) when \(p_3\ge t\)
gives the following checked endpoints:

| \(p\) | Excluded \(p_3\ge t\) | Endpoint comparison \(3pt^3\le4(p-1)(t-1)^3\) | Retained \(p_3\) |
|---:|---:|---|---|
| 5 | 47 | 1557345 < 1557376 | 17,19,23,29,31,37,41,43 |
| 7 | 23 | 255507 < 255552 | 11,13,17,19 |
| 11 | 17 | 162129 < 163840 | 13 |
| 13 | 15 | 131625 < 131712 | none |

Every prime between the lower and upper endpoints was checked. For
\(p=5\), the excluded values \(7,11,13\) have positive prefix gaps
\(9,5,3\). This leaves exactly the submitted 13 triples. The bounds are
mathematical consequences, not chosen search cutoffs.

For any retained triple, put \(c=2B-A>0\), \(x=p_4\), \(y=p_5\).
Expanding the radical equation verifies the exact equivalence

\[
Axy-2B(x-1)(y-1)=3
\quad\Longleftrightarrow\quad
(cx-2B)(cy-2B)=2AB-3c=N.
\]

The four-prime prefix has gap \(2B-cx<0\). Hence
\(u=cx-2B>0\), and \(v=cy-2B>u\). Every solution therefore arises
from a positive divisor \(u\mid N\) with \(u^2<N\), via
\(x=(u+2B)/c\), \(y=(N/u+2B)/c\). Conversely, integral prime outputs
with \(p_3<x<y\) solve the original equation. Negative and zero factor
branches cannot hide a solution; a square-factor case would give
\(x=y\) and is rejected.

I independently recomputed every \(A,B,c,N\), tested every displayed
prime factor by trial division, multiplied each factorization back to
\(N\), and scanned every integer \(u\le\lfloor\sqrt N\rfloor\) for
divisibility. All 95 small-divisor entries and both congruence remainders
per entry agree with the frozen certificate. There are precisely six
integral ordered pairs in the allowed range:

| Prefix | \((x,y)\) | Exact reason it is not a prime pair |
|---|---|---|
| 3,5,17 | (257,65533) | \(65533=13\cdot5041\) |
| 3,5,17 | (259,22015) | \(259=7\cdot37\) |
| 3,5,17 | (265,7509) | \(265=5\cdot53\) |
| 3,5,19 | (97,9215) | \(9215=5\cdot1843\) |
| 3,5,19 | (107,925) | \(925=5\cdot185\) |
| 3,7,11 | (27,2079) | \(27=3\cdot9\) |

The further integral pair \((25,5375)\) at prefix \((3,5,43)\) fails
\(x>43\). No other integral pair occurs. The earlier certificate's
26 tables for gaps 1 and 3 were also checked entry by entry, including
all 147 divisor checks. The submitted gap-3 exclusion is complete.

## Independent attacks and boundary checks

The fresh verifier additionally uses a recursive search that starts with
the empty prefix and does not assume the submitted list of 13 triples
or factor any \(N\). At a negative-gap prefix with \(m\) places left,
the first integer \(t\) satisfying
\(At^m\le2B(t-1)^m\) excludes every next prime at least \(t\), by
monotonicity. Such a \(t\) exists since \(A<2B\). If only one place
remains, its unique possible value is
\(y=(2B-E)/(2B-A)\); divisibility, primality, and ordering are then
checked exactly. Thus this search has a proved stopping rule on every
branch, not a fixed maximum prime.

For five primes it recorded 22 nonterminal branches and 108 final-prefix
checks. It found no solution for either target gap 1 or target gap 3.
The same implementation recovered exactly \((3,7,13,19)\) at gap 3
with four primes and exactly \((3,5,13)\) with three primes. Their
respective products and totients are \((5187,2592)\) and \((195,96)\).
These controls check that gap-3 solutions outside the claimed scope are
not incorrectly removed.

A second exact cross-check solves
\(y=[2B(x-1)-3]/(cx-2B)\) over all integers in
\(p_3<x<4B/c\). The upper bound follows from \(y>x\) and the positive
denominator: \(cx^2<4Bx-2B-3<4Bx\). All 937 possible fourth values
give the same six ordered integral pairs. Separately, 243 exact rational
identity checks used exponents in \(\{1,2,3\}^5\), including removal of
the prime 3 at exponent one, and all 16 modulo-3 residue patterns were
checked. These finite sanity checks supplement the universal proof;
they are not its justification for arbitrary exponents.

The original domain is nonempty: \(15015=3\cdot5\cdot7\cdot11\cdot13\)
has \(\sigma(15015)=32256>30030\), while
\(h(15015/13)=2304/1155<2\). Removing any smaller prime reduces
abundancy further. Every proper divisor divides one of these prime
quotients, and \(h\) is increasing under divisibility, so this example
is primitive non-deficient.

## Source comparison and contribution

The nearest inspected primary result is Joshua Zelinsky, *Must a
Primitive Non-Deficient Number Always Have a Small Component?*,
J. Integer Sequences 29 (2026), Article 26.4.3. The live publisher PDF
agrees with the frozen text: Conjecture 1, p. 2, asks for \(2R\);
Lemma 4, p. 4, proves the odd cases with three or four prime divisors;
Theorem 2 gives \(2kR\) generally. Its Lemma 9 already uses a product-loss
inequality, and Proposition 16 is an alternative involving the largest
prime. Their statements do not provide the submitted unconditional
five-prime bound. See the
[primary paper](https://cs.uwaterloo.ca/journals/JIS/VOL29/Zelinsky/zel14.pdf).

The [publisher record](https://cs.uwaterloo.ca/journals/JIS/VOL29/Zelinsky/zel14.html)
gives publication on July 3, 2026. The
[current arXiv record](https://arxiv.org/abs/2005.12115), opened during this
review, lists v5 dated July 3, 2026 and the revised \(2R\) conjecture;
no later version is displayed. The version-specific v5 URL itself failed
to fetch, but the current record supplied the version information.

Fresh bounded searches included the exact title; “primitive non-deficient”
with “five”, “five prime factors”, and “component”; “primitive abundant”
with “five” and “component”; and affine-totient variants including
“n-2phi(n)”, “2phi” with “5187”, and “totient” with “n-3” and “squarefree”.
Equation searches produced many irrelevant results. I found no verified
covering result. The January 1977 AMS Notices lead in the frozen screen
was encountered again, but opening its PDF failed. The Cohen DOI also
failed to open in this review. Neither failure supplies evidence of
novelty or mathematical truth, and neither source is a proof dependency.
The proposer's historical registry comparison was not revalidated.

The accepted contribution is the full odd five-prime case, extending the
nearest inspected three/four-prime result. The specific advance is the
exponent-uniform reduction to two radical gaps together with a complete,
small exclusion certificate, avoiding classification of all primitive
non-deficient integers in this domain. This is a substantive resolution
of the frozen question. The elementary inequality and factorization are
not separately claimed to be new. The bounded literature wording is
appropriate: global priority and exhaustive historical coverage are not
certified.

## Decision and remaining scope

No mathematical gap was found in the submitted scope. The quotient
estimate, signs, congruence, complete cutoffs, factor equivalence, and
finite arithmetic collectively prove the original strict inequality.
The conclusion is a proof in the frozen full scope, not an inference
from passing tests or from a workflow flag.

Accept `resolution-paper` with frozen original status `proved`. The
general conjecture for six or more primes and the stronger \(R\) bound
are outside this audit. This fresh context provides a separate review
pass, not a claim of statistically independent evidence or journal peer
review. No manuscript or PDF was produced. After saving the verdict,
`release_gate.py check-math` exited zero with `ok: true`, confirming the
current snapshot and referee provenance. This is a structural check only.
The next workflow step is manuscript preparation at exactly the accepted
scope while preserving the stated literature limits.
