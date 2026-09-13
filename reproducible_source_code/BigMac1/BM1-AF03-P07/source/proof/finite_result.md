# Certified finite result for alphabet size eight

## Theorem

For every \(0\leq n\leq8\), let \(\mathcal C\) be a K-Knuth equivalence
class of initial straight increasing tableaux on \([n]\), and let
\(\Sigma(\mathcal C)\) be its set of shapes. If
\(\lambda,\nu\in\Sigma(\mathcal C)\) and \(\lambda\subseteq\nu\), then every
partition \(\mu\) satisfying \(\lambda\subseteq\mu\subseteq\nu\) belongs to
\(\Sigma(\mathcal C)\).

In particular, the first endpoint not verified in the 2016 source paper,
\(n=8\), satisfies Conjecture 7.6. This is a finite theorem and does not prove
Conjecture 7.6 for unbounded alphabets.

## Exact finite proof

### 1. Exhaustive state space

For a tableau on \([n]\), the entry in position \((i,j)\) is at least
\(i+j-1\). Hence its shape lies in the finite staircase
\(\delta_n=(n,n-1,\ldots,1)\).

The independent verifier enumerates every partition \(\lambda\subseteq
\delta_n\). For each such shape, it visits the boxes in row-major order. At a
box \((i,j)\), it tries every integer from

\[
 \max\{i+j-1,\ T(i,j-1)+1,\ T(i-1,j)+1\}
 \quad\text{through}\quad n,
\]

omitting a nonexistent left or upper neighbor. Every generated filling is
strictly increasing. Conversely, every increasing tableau has exactly one
shape in this list and its entry at each visited box occurs among exactly these
choices. Thus the enumeration is exhaustive and duplicate-free.

The verifier encodes the result cell-by-cell in an 80-bit exact integer code.
For a box on diagonal \(d=i+j-1\), digit zero means absent and digits
\(1,\ldots,9-d\) represent entries \(d,\ldots,8\). Decoding and tableau
validity are rechecked before transitions are used.

### 2. Exact K-Knuth components

For each enumerated tableau \(T\) and each \(a\in[n]\), the verifier performs
the four-case Hecke row-insertion rule using an explicit integer grid and stores
the exact state \(T\leftarrow a\). It then instantiates at every state all
primitive pairs

\[
 p\leftrightarrow pp,\qquad
 pqp\leftrightarrow qpq\ (p<q),\qquad
 xzy\leftrightarrow zxy,\qquad
 yxz\leftrightarrow yzx\ (x<y<z).
\]

There are
\(n+\binom n2+2\binom n3\) such unordered primitive pairs. The verifier
merges their image states and applies the same right insertion by every letter
to each newly merged pair until the queue is empty. This is precisely the
finite congruence closure in Algorithm 1 of Gaetz et al.; their Theorem 3.1
proves that its components are exactly the tableau K-Knuth classes.

The alphabet of a word is invariant under each primitive relation. Therefore a
component containing an initial tableau on \([n]\) contains only initial
tableaux on \([n]\), and the exact alphabet-bitset filter selects complete
components rather than component fragments.

### 3. Exact interval predicate

For every initial component, let \(S\) be its deduplicated shape set. In any
poset,

\[
 S\text{ is order-convex}
 \quad\Longleftrightarrow\quad
 (\uparrow S)\cap(\downarrow S)\subseteq S.
\]

Indeed, a point in the left-hand intersection has some element of \(S\) below
it and some element of \(S\) above it, so it lies in an interval with endpoints
in \(S\); the converse is immediate. The verifier represents all staircase
shapes by bit positions, constructs exact upward and downward closure bitsets,
and checks that
\((\uparrow S)\cap(\downarrow S)\setminus S\) is empty for every component.
No floating-point or probabilistic operation occurs.

### 4. Certified totals

| \(n\) | all tableaux on \([n]\) | initial tableaux | initial classes | URTs | interval complete |
|---:|---:|---:|---:|---:|:---:|
| 0 | 1 | 1 | 1 | 1 | yes |
| 1 | 2 | 1 | 1 | 1 | yes |
| 2 | 6 | 3 | 3 | 3 | yes |
| 3 | 26 | 13 | 13 | 13 | yes |
| 4 | 162 | 87 | 79 | 71 | yes |
| 5 | 1,450 | 849 | 620 | 459 | yes |
| 6 | 18,626 | 11,915 | 6,036 | 3,313 | yes |
| 7 | 343,210 | 238,405 | 70,963 | 25,904 | yes |
| 8 | 9,069,306 | 6,773,991 | 988,384 | 215,295 | yes |

For \(n=8\), the closure used 148 primitive rules at each of the 9,069,306
states, hence exactly 1,342,257,288 primitive tests. It performed 7,303,139
successful component merges and exactly 58,425,112 right-closure tests. All are
integer loop counts checked against the serialized certificate.

The rows \(n\leq7\) reproduce the source paper's reported initial-tableau,
class, and URT counts. The \(n=8\) row is the new finite endpoint.

## Independence and reproducibility

The discovery program adds equal-letter rook strips and encodes each tableau by
row bitsets. The verifier instead enumerates shape-first, fills cell-by-cell,
uses an 80-bit cell code, performs insertion on explicit grids, and checks
order-convexity by closure bitsets. It reads only
`certificates/n8_certificate.json`; it does not read discovery states,
transitions, components, or interval answers.

Run:

```sh
sh scripts/verify_n8.sh
python3 tests/test_fail_closed.py
```

The first command rebuilds every endpoint \(0\leq n\leq8\) and prints SHA-256
hashes of the certificate, driver, verifier source, and verifier binary. The
second command checks rejection of missing fields, extra trusted fields,
boolean/integer confusion, duplicate JSON keys, and an altered exact count, and
also confirms acceptance of an intact small endpoint.

## Limitation

The computation settles only alphabet cardinalities at most eight. The
prescribed-cover lemma in `proof/structural_reduction.md` is supported at those
finite endpoints but remains unproved in general. No Lean, Coq, Isabelle, or
other proof assistant was used.
