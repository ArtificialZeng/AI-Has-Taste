# Definition-first transfer-automaton equivalence audit

## Verdict

**PASS.**  Starting only from the graph in
problem/formal_statement.md (SHA-256
0796f4e5af9890b77240d3f281f9ae149edaac7576b259ba096468b487b59db4),
I independently derived exact transfer automata for odd and even orders.
For even \(n=2m\), the construction has 54 states and a mandatory
component-swap closure.  I prove a bijection in both directions between
proper labelled three-colourings and accepted based walks.

The exact counting formulas are

\[
 a(n)=\operatorname{tr}(U^n)\quad(n\ {\rm odd}),
 \qquad
 a(2m)=\operatorname{tr}(T^mJ)\quad(m\ge3),
\]

where \(U,T,J\) are defined below.  In particular, replacing the second
formula by the ordinary trace \(\operatorname{tr}(T^m)\) is false: it loses
the half-cycle swap at both the middle and cyclic seams.

## 1. Odd-order automaton

Let \(K=\{0,1,2\}\).  Define the 12-state set

\[
 {\cal O}=\{(x_0,x_1,x_2)\in K^3:
             x_0\ne x_1,\ x_1\ne x_2\}.
\]

Use lexicographic order on \(K^3\) to index the states.  Define the
\(12\times12\) zero-one matrix \(U\) by

\[
 U_{(x_0,x_1,x_2),(y_0,y_1,y_2)}=1
\]

if and only if there is a \(z\in K\) such that

\[
 (y_0,y_1,y_2)=(x_1,x_2,z),\qquad
 x_2\ne z,\qquad x_0\ne z. \tag{1}
\]

The two inequalities in (1) are exactly the new offset-one and
offset-three conditions when \(z\) is appended.

An accepted word of order \(n\) is a length-\(n\) based closed walk

\[
 s_0\longrightarrow s_1\longrightarrow\cdots
 \longrightarrow s_n=s_0
\]

in this automaton.

### Colouring implies accepted walk

Given a proper colouring \(c:\mathbb Z/n\mathbb Z\to K\), extend \(c_i\)
periodically to all \(i\in\mathbb Z\), and set

\[
 s_i=(c_i,c_{i+1},c_{i+2}).
\]

The offset-one edges put every \(s_i\) in \({\cal O}\).  The offset-one
edge \(c_{i+2}c_{i+3}\) and offset-three edge \(c_ic_{i+3}\) give (1), so
\(s_i\to s_{i+1}\).  Periodicity gives \(s_n=s_0\).

### Accepted walk implies colouring

Conversely, overlap in (1) forces any walk to have a unique symbol sequence
\(c_0,c_1,\ldots,c_{n+2}\) with
\(s_i=(c_i,c_{i+1},c_{i+2})\).  The equality \(s_n=s_0\) gives

\[
 c_n=c_0,\qquad c_{n+1}=c_1,\qquad c_{n+2}=c_2.
\]

State membership and (1) give \(c_i\ne c_{i+1}\) and
\(c_i\ne c_{i+3}\) for every cyclic \(i\).  Thus \(c_0,\ldots,c_{n-1}\)
is a proper colouring.  The two maps are inverse and preserve the actual
colour labels and the distinguished vertex \(0\); no rotation or colour
permutation is factored out.  Therefore \(a(n)=\operatorname{tr}(U^n)\)
for odd \(n\).

## 2. Even orders: paired columns and the twist

Let \(n=2m\), with \(m\ge3\), and write

\[
 q_i=(x_i,y_i):=(c_i,c_{i+m})\qquad(0\le i<m).
\]

Let

\[
 Q=\{(x,y)\in K^2:x\ne y\},\qquad
 \sigma(x,y)=(y,x).
\]

The six elements of \(Q\) are precisely the possible properly coloured
diameter pairs.  Extend the column word to every integer index by the
twisted rule

\[
 q_{i+m}=\sigma(q_i). \tag{2}
\]

It then has ordinary period \(2m\).  If \(\pi_1,\pi_2\) denote the two
coordinates, (2) gives, for every \(i\in\mathbb Z\),

\[
 \pi_1(q_i)=c_i,\qquad
 \pi_2(q_i)=c_{i+m}, \tag{3}
\]

with colour indices read modulo \(2m\).

For columns \(q=(x,y)\) and \(r=(x',y')\), write

\[
 q\perp r\quad\Longleftrightarrow\quad
 x\ne x'\ \hbox{ and }\ y\ne y'. \tag{4}
\]

Equations (2)--(4) give the definition-first equivalence

\[
\begin{split}
c\text{ is proper on }C_{2m}^{(3)}
\quad\Longleftrightarrow\quad&
q_i\in Q\quad(0\le i<m),\\
&q_i\perp q_{i+1},\quad q_i\perp q_{i+3}
       \quad(0\le i<m),
\end{split} \tag{5}
\]

where indices outside \(0,\ldots,m-1\) are evaluated using (2).

Indeed, \(q_i\in Q\) is exactly the diameter constraint.  For
\(h\in\{1,3\}\), the two coordinate inequalities in
\(q_i\perp q_{i+h}\) are

\[
 c_i\ne c_{i+h},\qquad
 c_{i+m}\ne c_{i+m+h}.
\]

As \(i\) runs from \(0\) to \(m-1\), these are exactly all offset-\(h\)
edges with starting vertex in \(\mathbb Z/2m\mathbb Z\).  This proves both
implications in (5), rather than only necessity.

## 3. The exact 54-state matrix

Define

\[
 {\cal E}=\{(q_0,q_1,q_2)\in Q^3:
             q_0\perp q_1,\ q_1\perp q_2\}. \tag{6}
\]

For any fixed \(q\in Q\), exactly three \(r\in Q\) obey \(q\perp r\).
For example, for \(q=(0,1)\) they are

\[
 (1,0),\ (1,2),\ (2,0).
\]

Consequently

\[
 |{\cal E}|=6\cdot3\cdot3=54. \tag{7}
\]

Thus the 54-state size is derived from the formal graph; it is not assumed
from an external transfer matrix.

Index \({\cal E}\) lexicographically by its six ordered column symbols.
Define the \(54\times54\) zero-one matrix \(T\) by

\[
 T_{(q_0,q_1,q_2),(r_0,r_1,r_2)}=1 \tag{8}
\]

if and only if there is a \(q_3\in Q\) such that

\[
 (r_0,r_1,r_2)=(q_1,q_2,q_3),\qquad
 q_2\perp q_3,\qquad q_0\perp q_3. \tag{9}
\]

The last two conditions in (9) are the newly completed offset-one and
offset-three column constraints.

Define an involution on states by

\[
 \tau(q_0,q_1,q_2)
   =(\sigma q_0,\sigma q_1,\sigma q_2),
\]

and let \(J\) be its permutation matrix:

\[
 J_{s,t}=1\quad\Longleftrightarrow\quad t=\tau(s). \tag{10}
\]

An accepted even word is a length-\(m\) based twisted closed walk

\[
 s_0\longrightarrow s_1\longrightarrow\cdots
 \longrightarrow s_m=\tau(s_0). \tag{11}
\]

With the row-to-column convention in (8), the number of these walks is

\[
 \sum_{s\in{\cal E}}(T^m)_{s,\tau(s)}
   =\operatorname{tr}(T^mJ). \tag{12}
\]

## 4. Bijection for the even automaton

### Proper colouring implies accepted twisted walk

Given a proper \(c\), form the columns \(q_i\) and extend them by (2).
By (5), all columns lie in \(Q\), and the distance-one and distance-three
column constraints hold.  Put

\[
 s_i=(q_i,q_{i+1},q_{i+2})\qquad(0\le i\le m).
\]

Then (6) makes every \(s_i\) a state, (9) gives every transition, and

\[
 s_m=(\sigma q_0,\sigma q_1,\sigma q_2)=\tau(s_0).
\]

Thus every graph colouring produces an accepted twisted walk.

### Accepted twisted walk implies proper colouring

Conversely, the exact overlap required by (9) makes a walk (11) determine
unique columns \(q_0,q_1,\ldots,q_{m+2}\) with

\[
 s_i=(q_i,q_{i+1},q_{i+2}).
\]

The endpoint equality in (11) is the three-coordinate closure

\[
 q_m=\sigma q_0,\qquad
 q_{m+1}=\sigma q_1,\qquad
 q_{m+2}=\sigma q_2. \tag{13}
\]

Use \(q_0,\ldots,q_{m-1}\) as the fundamental columns and extend them by
(2).  State membership and the transitions give

\[
 q_i\perp q_{i+1},\qquad q_i\perp q_{i+3}
 \qquad(0\le i<m);
\]

the cases that cross \(m\) are valid precisely because of (13).  Write
\(q_i=(x_i,y_i)\), and define

\[
 c_i=x_i,\qquad c_{i+m}=y_i\qquad(0\le i<m).
\]

Now (5) proves that every graph edge is proper.  This construction recovers
the original columns from a colouring-derived walk, and the preceding map
recovers the same walk from these columns.  Hence the maps are inverse:
there is a bijection, not merely equality of experimental counts.

The full state closure in (13) matters.  Requiring only
\(q_m=\sigma q_0\), without the next two memory coordinates, would leave
the offset-three seam unchecked.

## 5. Explicit seam audit

The swap in (2) simultaneously represents the middle seam and the cyclic
seam of the original \(2m\)-vertex order.

For offset one,

\[
 q_{m-1}\perp q_m=q_{m-1}\perp\sigma q_0
\]

is exactly the pair of original constraints

\[
 c_{m-1}\ne c_m,\qquad c_{2m-1}\ne c_0.
\]

For offset three, the last three fundamental starting columns give

\[
\begin{array}{c|cc}
i & \text{first coordinate} & \text{second coordinate}\\ \hline
m-3 & c_{m-3}\ne c_m & c_{2m-3}\ne c_0\\
m-2 & c_{m-2}\ne c_{m+1} & c_{2m-2}\ne c_1\\
m-1 & c_{m-1}\ne c_{m+2} & c_{2m-1}\ne c_2.
\end{array}
\]

These are all six offset-three edges crossing the two seams.  There is no
unstated ordinary periodicity of the two halves.

This audit also locates the exact failure of an untwisted trace.  Ordinary
closure \(s_m=s_0\) imposes \(q_{i+m}=q_i\), whereas the original vertex
order requires \(q_{i+m}=\sigma q_i\).  Independent exact counts are:

\[
\begin{array}{c|rrrrrr}
n&6&8&10&12&14&16\\ \hline
\operatorname{tr}(T^{n/2})&0&114&0&522&0&2130\\
\operatorname{tr}(T^{n/2}J)&42&0&186&0&930&0.
\end{array}
\]

Thus the permutation matrix \(J\) is logically indispensable.

## 6. Boundary \(n=6\)

Here \(m=3\), and

\[
 q_0=(c_0,c_3),\quad q_1=(c_1,c_4),\quad
 q_2=(c_2,c_5).
\]

The offset-three edges coincide with the diameter edges.  In the automaton,
their column conditions are

\[
 q_i\perp q_{i+3}=q_i\perp\sigma q_i.
\]

For \(q_i=(x,y)\in Q\), this says \(x\ne y\) twice, so it is exactly the
already imposed simple diameter edge and adds no spurious restriction.

The distance-one conditions

\[
 q_0\perp q_1,\qquad q_1\perp q_2,\qquad
 q_2\perp\sigma q_0
\]

encode the six cycle edges, including \(c_2c_3\) and \(c_5c_0\).  Therefore
the same 54-state construction is valid without an exceptional convention
at \(n=6\).  It gives

\[
 \operatorname{tr}(T^3J)=42,
\]

which agrees with direct enumeration of the nine distinct simple edges.

## 7. Independent executable cross-check

I wrote an ephemeral checker without importing or calling any project
verifier and without reading a published matrix.  It constructed \(U,T,J\)
from (1), (6), and (8)--(10), separately constructed the unordered graph edge
set from offsets \(1,3,n/2\), and exhaustively coloured that graph.

Raw output:

    state_sizes 12 6 54
    6 42 42
    7 0 0
    8 0 0
    9 18 18
    10 186 186
    11 66 66
    12 0 0
    13 234 234
    14 930 930
    15 750 750
    16 0 0
    PASS automaton counts equal direct graph-coloring counts for n=6..16

In each numeric row, the first number after \(n\) is the relevant automaton
trace and the second is the direct graph-colouring count.  These finite
checks are diagnostic only; the two inverse constructions in Sections 1 and
4 prove the equivalence for every quantified order.

## Final Gate 5 decision

- Odd accepted closed walks \(\leftrightarrow\) odd graph colourings:
  **proved bijection**.
- Even swap-twisted accepted walks \(\leftrightarrow\) even graph colourings:
  **proved bijection**.
- Diameter constraints, offset-three constraints, both seams, and
  \(n=6\): **all represented exactly**.
- Ordinary untwisted trace for even orders: **rejected**, with the exact
  \(n=6\) discrepancy \(0\ne42\).
- Proof-assistant use: **none**.

**Overall verdict: PASS.  Failed implication or unresolved item: none for
the automata defined in this report.**

## Implementation/cone recheck

### Scope and version binding

This follow-up audits the implemented cone certificate and verifier, rather
than reusing the earlier definition-level bijection as evidence.  I read the
following current files in full and bind this recheck to their SHA-256
digests:

| File | SHA-256 |
|---|---|
| proof/transfer_automaton.md | ff87d9c0060f6e499f1fda395c928a9a6080b72a0560de5d441bd61ff75d37f8 |
| certificates/transfer_automata_certificate.json | 3d805efc718fbbd507aabe3cf7e9595e4dfe9f51f4b9f54d6c73cb3885650774 |
| verification/verify_transfer_automata.py | 73fd784626dd01a8749be6ac1cade2cf18c07c6b01c98185a6757f2562d871f2 |
| results/transfer_automata_verification.json | 355ebdb410400c3cee15178da0b630a9532e39ce0e609ac03aab14966ccebd58 |

The verifier changed during the beginning of this audit to validate the
literal state, transition, closure, and acceptance descriptions as well as
their data.  All tests and the verdict below were rerun against the final
73fd7846...871f2 version shown in the table.

### Independent reconstruction of the serialized invariants

I independently rebuilt the state lists and matrices without importing the
project verifier.  States were ordered lexicographically exactly as specified,
and a matrix was serialized as compact JSON with separators comma and colon
before hashing.  The reconstructed results are:

| Object | States | Nonzero entries | Nonzero columns | Minimum | Maximum | Entry sum | SHA-256 |
|---|---:|---:|---:|---:|---:|---:|---|
| \(O\) | 12 | 18 | 12 | — | — | — | 015de555faf78002f4a295aafb8db08d814956af339c6f2ef16916723baab2a9 |
| \(O^{10}\) | — | — | — | 1 | 26 | 1398 | 60c37736e05a71a2d58e40979685e037485f9c2193cc5c3eaa9b0227362a003e |
| \(E\) | 54 | 114 | 54 | — | — | — | fbbf93271d70402aca563534f82ba99ef73c6f6dcc60f78b580e35a24d58ce7d |
| \(E^{13}\) | — | — | — | 20 | 4097 | 2750778 | cfcbabfd011035603fd011e34e8447ab3f98085424ac9b19669ae63d95ad82b7 |

Every value and digest equals the serialized certificate.  I also recomputed
the certificate and verifier file hashes from their actual bytes; both equal
the hashes stored in results/transfer_automata_verification.json.

The saved result was compared field by field with a fresh verifier run.  Every
field emitted by the current verifier is identical.  The sole additional
saved field is

    interpreter_modes_passed = ["python3 -I", "python3 -O -I"],

which accurately records the two separately rerun modes.

### Cone-propagation logic

The propagation argument uses the correct multiplication side.  Let \(A\) be
either \(O\) or \(E\), suppose \(A^r>0\) entrywise, and fix \(i,j\).  Because
column \(j\) of \(A\) is nonzero, some \(k\) has \(A_{kj}>0\).  Hence

\[
 (A^{r+1})_{ij}
   =\sum_\ell (A^r)_{i\ell}A_{\ell j}
   \ge (A^r)_{ik}A_{kj}>0.
\]

Induction proves \(A^{r+t}>0\) for every \(t\ge0\).  The verifier checks the
needed nonzero-column premise for all 12 columns of \(O\) and all 54 columns
of \(E\), before using the positive powers.

It follows exactly that:

- \(O^n>0\) for every \(n\ge10\), so
  \(\operatorname{tr}(O^n)>0\) for every relevant odd \(n\ge11\);
  the remaining positive odd base order is separately checked by
  \(\operatorname{tr}(O^9)=18\).
- \(E^m>0\) for every \(m\ge13\).  In particular every selected twisted
  entry \((E^m)_{s,\tau(s)}\) is positive, so
  \(\operatorname{tr}(E^mP)>0\) for every even \(n=2m\ge26\).

Thus the threshold 26 follows from the exact cone certificate, while the
definition-level recursion through 25 covers every lower order.  There is no
numerical limiting argument or unchecked gap between the finite and cone
ranges.

### Direct-recursion completeness and independent check

The implemented graph constructor takes the set of unordered pairs generated
by offsets one and three and, at even orders, \(n/2\).  Consequently duplicate
diameter pairs are identified, and at \(n=6\) the repeated offset-three and
diameter edges are also identified exactly as required by the formal simple
graph.

The recursion fixes \(c_0=0\).  At any partial proper colouring it selects one
uncoloured vertex and branches over every colour not used by an already
coloured neighbour.  Every proper completion chooses exactly one of those
branches, and no such branch is discarded.  When the second endpoint of an
edge is coloured that edge is checked; therefore every leaf is proper.
Induction on the number of uncoloured vertices proves that every proper
colouring with \(c_0=0\) reaches exactly one leaf.  Adding a constant modulo
three is a bijection between the three possible values of \(c_0\), so
multiplication by three gives the labelled count \(a(n)\).

As an independent implementation check, I used a fixed vertex order
\(1,2,\ldots,n-1\), rather than the verifier's dynamic
most-constrained-vertex choice.  It reproduced every one of the 20 serialized
fixed-\(c_0\) counts:

    6:14, 7:0, 8:0, 9:6, 10:62, 11:22, 12:0, 13:78,
    14:310, 15:250, 16:0, 17:748, 18:1526, 19:2166,
    20:40, 21:6118, 22:7438, 23:16974, 24:832, 25:46500.
    PASS independent fixed-order recursion equals all serialized
    c0=0 counts for n=6..25

At the boundary \(n=6\), this gives 14 colourings with \(c_0=0\), hence
\(a(6)=42\).  Independently, the twist computation gives
\(\operatorname{tr}(E^3P)=42\), while the deliberately rejected ordinary
trace is zero.  The direct, twisted-automaton, and simple-edge conventions
therefore agree at the fragile endpoint.

### Normal and optimized execution; fail-closed tamper tests

The verifier contains no Python correctness assert and uses explicit
require/fail calls.  Fresh runs in both modes

    python3 -I verification/verify_transfer_automata.py CERTIFICATE
    python3 -O -I verification/verify_transfer_automata.py CERTIFICATE

returned exit status zero and byte-identical PASS JSON.  Their reported
certificate and verifier hashes are the current hashes in the scope table.

I copied the certificate to a temporary directory and performed three
one-field tamper tests.  Each test was run in both normal and optimized mode:

| Tamper | Normal mode | \(-O\) mode |
|---|---|---|
| odd full_positive_power: \(10\to11\) | exit 1, FAIL: odd positive-power hash mismatch | exit 1, same failure |
| eventual threshold: \(26\to28\) | exit 1, FAIL: eventual threshold mismatch | exit 1, same failure |
| odd acceptance text: odd \(n\ge7\to n\ge9\) | exit 1, FAIL: odd automaton definition text mismatch | exit 1, same failure |

The temporary tamper files were deleted after the runs.  These are decisive
mutations: they alter the asserted positive-power endpoint, theorem
threshold, or serialized acceptance rule.  None can pass through an
optimization-disabled check, and the hardening also prevents unused
definition text from silently drifting.

### Final implementation/cone decision

- Automaton and positive-power hashes: **PASS**.
- \(O^{10}\) and \(E^{13}\) invariants: **PASS**.
- Nonzero-column premise and all-later-power cone propagation: **PASS**.
- Direct recursion, finite range, and \(c_0\) normalization: **PASS**.
- \(n=6\) repeated-edge and twist boundary: **PASS**.
- Normal and \(-O\) fail-closed behaviour: **PASS**.
- Saved result binding to current certificate/verifier: **PASS**.
- Fatal, major, local, or unresolved mathematical/implementation items:
  **none**.

**Final follow-up verdict: PASS.**
