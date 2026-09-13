# Independent proof audit

## Verdict

**PASS.**  Starting only from the graph definition in
`problem/formal_statement.md`, I reconstructed the claimed zero set and then
audited `proof/builder_notes.md` and `proof/main_proof.md` line by line.  I
found no fatal or major mathematical gap and no counterexample.  In
particular, `proof/builder_notes.md` is a complete, computation-free proof of

\[
 a(n)=0\quad\Longleftrightarrow\quad n\in\{7,8,12,16\}
 \qquad(n\geq 6).
\]

`proof/main_proof.md` gives a second valid route once its finite seed data are
read from `certificates/zero_set_certificate.json`.  It has two local
traceability/exposition defects recorded below, neither of which changes the
theorem or requires a new idea.

This audit addresses mathematical correctness under the graph definition as
stated.  It does not certify the separate literature/novelty claim in lines
42--46 of the formal statement.

Audited versions (SHA-256):

| File | SHA-256 |
|---|---|
| `problem/formal_statement.md` | `0796f4e5af9890b77240d3f281f9ae149edaac7576b259ba096468b487b59db4` |
| `proof/builder_notes.md` | `30a2851abecfe04fc7722e6a8022ac93ac1630bc8f4c2845516d4ce197b2146c` |
| `proof/main_proof.md` | `30f939212492eebdee5a176f0e4ec4d3c64838b5d3d3c153641c1055d41c0b69` |
| `certificates/zero_set_certificate.json` | `ff2d77c2e21b883c6588036137c5482f72a2bbfff3723151d8ab5b72f66a677c` |

## 1. Definition-first reconstruction

Identify the colours with \(\mathbb Z/3\mathbb Z\).  For a proper colouring
of the cycle edges, define

\[
 d_i=c_{i+1}-c_i\in\{+1,-1\},
\]

where residue \(2\) is represented by the integer \(-1\).  Conversely,
choosing \(c_0\) and successively adding the signs reconstructs a colouring
on the cyclic vertex set exactly when

\[
 \sum_{i=0}^{n-1}d_i\equiv0\pmod 3. \tag{A}
\]

The offset-three edge at \(i\) is proper exactly when

\[
 c_{i+3}-c_i=d_i+d_{i+1}+d_{i+2}\not\equiv0\pmod3.
\]

A sum of three signs is \(0\bmod3\) exactly for \(+3\) or \(-3\), hence
exactly when the three signs are equal.  Thus the offset-one and offset-three
conditions are equivalent, in both directions, to (A) and the absence of a
cyclic run of three equal signs.

If \(n=2m\), then

\[
 c_{i+m}-c_i=\sum_{j=0}^{m-1}d_{i+j}.
\]

Consequently all diameter edges are proper exactly when every cyclic
length-\(m\) window has sum nonzero modulo three.  This proves the full
colour/sign-word equivalence, including windows and triples crossing the
cyclic seam.  It also shows that checking all \(i\) merely checks each
undirected diameter twice; this is harmless.

At \(n=6\), the offset-three and diameter edges coincide.  Both translate to
the same length-three-window condition.  After identifying repeated edges,
the graph has the nine distinct edges

\[
 01,03,05,12,14,23,25,34,45,
\]

and the colouring word \(010101\) is proper.  Thus the endpoint and the
simple-graph collision do not create an omitted condition.

## 2. Audit of the positive constructions

### 2.1 `proof/builder_notes.md`

Put \(A=01\) and \(B=21202\).

- Within an \(A\)-block, offsets one and three reverse parity.  Within \(B\),
  all adjacent pairs and the two internal offset-three pairs are proper.
- Across an \(A\mid B\) seam, the three offset-three comparisons are, up to
  order, \((1,2),(0,1),(1,2)\).  Across a \(B\mid A\) seam they are
  \((2,0),(0,1),(2,0)\).  Both adjacent seam pairs are also proper.  Hence a
  cyclic word whose \(B\)'s are separated by \(A^r\), \(r\ge2\), has every
  offset-one and offset-three edge proper, including the closing seam.
- For odd \(n\ge9\), the word \(A^{(n-5)/2}B\) has length \(n\), and its sole
  \(A\)-separation has exponent at least two.
- For \(n\equiv2\pmod4\), \(A^{n/2}\) is a well-defined alternating cyclic
  word of even length.  Offsets one and three are odd, and the diameter
  \(n/2\) is odd.  This includes \(n=6\).
- For \(n=20\), the two halves printed in builder lines 99--100 are
  \(X=0101012120\) and \(Y=2010121202\); their ten coordinates differ.
- For \(n=4k\), \(k\ge6\), the split
  \(X=A^{k-1}21\), \(Y=202A^{k-4}B\) has two halves of length \(2k\).
  Coordinates \(0,1,2\) compare \(010\) with \(202\); coordinates
  \(3\le j\le2k-6\) lie in opposite-parity alternating strings; and the final
  five coordinates compare \(10121\) with \(21202\).  These ranges are
  disjoint and exhaustive even at the endpoint \(k=6\) (\(n=24\)).  The
  lower endpoint \(k=5\) is exactly the separately handled word for \(n=20\).

The four construction rows cover, without a quantifier gap,

| Class | Covered orders |
|---|---|
| odd | every odd \(n\ge9\) |
| \(2\bmod4\) | \(6,10,14,18,\ldots\) |
| \(0\bmod4\), positive | \(20\) and every \(n\ge24\) divisible by four |

Their complement among integers \(n\ge6\) is precisely
\(\{7,8,12,16\}\).

### 2.2 `proof/main_proof.md`

The odd-order count construction is correct.  If \(p\ge q>0\), set
\(r=p-q\).  The run bound \(p\le2q\) is exactly what makes
\(0\le r\le q\), and

\[
 (++-)^r(+-)^{q-r}
\]

has \(p\) plus signs, \(q\) minus signs, and a safe cyclic seam.  The three
parameter pairs in main-proof lines 40--43 have total length \(n\), difference
\(p-q=\pm3\), and obey the run bound at their stated endpoints.  They cover
all odd \(n\ge9\).

The one-flip lemma is also correct.  Let \(A_0=\sum_j a_j\), let \(b\) be
\(a\) with only \(a_0=+1\) flipped, and put \(d=ab\).  The endpoint
hypotheses exclude every triple internal to \(b\) and every triple across
both seams.  Also

\[
 \sum d=2A_0-2\equiv0\pmod3.
\]

For the cyclic half-window residues, the precise full-tour statement is

\[
 S_0\equiv1,\qquad
 S_i\equiv-1\ (1\le i\le m),\qquad
 S_i\equiv1\ (m+1\le i\le2m-1).
\]

Thus every diameter is proper.  The finite half-word seeds stored in
`certificates/zero_set_certificate.json` for

\[
 m\in\{3,5,7,9,11,12,13,\ldots,20\}
\]

all satisfy the six stated seed conditions.  For \(m>20\), the selected
\(r\in[12,20]\) is unique, \(m-r\) is a positive multiple of nine, and the
prefix \((++-)^{(m-r)/3}\) has length \(m-r\) and sign sum divisible by
three.  It starts \(++-\), ends in \(-\), and meets every seed in the safe
context \(-++-\); its beginning and the seed's unchanged ending preserve the
endpoint conditions.  The separately printed length-20 sign word for
\(m=10\) also passes all necessary and sufficient conditions.  Therefore the
even construction covers all half-lengths \(m\ge3\) except \(m=4,6,8\),
which are exactly the three even exceptions.

## 3. Audit of nonexistence

Let \(p\) be the total number of plus signs.  Closure gives

\[
 2p-n\equiv0\pmod3. \tag{B}
\]

In a cyclic sign word with no equal-sign triple and with both signs present,
each sign occurs at most twice as often as the other: every run has length at
most two.

- For \(n=7\), (B) gives \(p=2\) or \(p=5\).  The majority count five cannot
  fit in the two cyclic gaps made by the minority signs, whose combined
  capacity is four.
- For \(n=8,12,16\), closure plus the run restriction gives respectively
  \(p=4,6,8\), hence in each case \(p=n/2=m\).  The all-one-sign candidates
  \(p=0,n\), relevant only in the intermediate \(n=12\) congruence list, are
  excluded directly by the no-three rule.

For the latter three orders let \(q_i\) count plus signs in the length-\(m\)
window starting at \(i\).  The opposite window is its complement, so

\[
 q_{i+m}=m-q_i,
 \qquad |q_{i+1}-q_i|\le1.
\]

Since \(m=4,6,8\) is even, the integer path from \(q_i\) to \(m-q_i\) must
hit \(m/2\).  That window has integer sign sum \(2q_i-m=0\), contradicting
the diameter condition.  This is an existence contradiction, not an
inference from a finite calculation, and covers all four claimed zeros.

## 4. Independent checks

I did not import, modify, or call either existing verifier.  I wrote ephemeral
minimal Python checks directly from the graph definition.

1. A direct unordered-edge constructor generated offsets one and three and,
   for even \(n\), the diameter, identifying repeated pairs in a set.  It
   generated the four builder colour families literally and compared colours
   on every edge.  Raw result:

   ```text
   PASS direct graph-edge check n=6..500 plus 1000,1002,10000,10002
   n=6 simple edge count 9 edges [(0, 1), (0, 3), (0, 5), (1, 2),
   (1, 4), (2, 3), (2, 5), (3, 4), (4, 5)]
   ```

2. A separately coded sign-word checker tested total closure, every cyclic
   equal-sign triple, and every cyclic half-window.  It checked each of the 14
   literal half-word seeds, independently applied the one-flip construction,
   checked the extension rule for every \(12\le m\le1000\), and checked the
   special length-20 word.  Raw result:

   ```text
   PASS all 14 seed half-words, extended m=12..1000, and special n=20
   ```

3. A third routine reconstructed the graph itself and exhausted colourings in
   vertex order, pruning only against already coloured graph neighbours.  It
   fixed \(c(0)=0\), which is lossless under global colour permutation.  Raw
   result:

   ```text
   7 0
   8 0
   12 0
   16 0
   PASS independent direct graph-colouring exhaustion with c(0)=0
   ```

These computations are diagnostics.  Infinite quantifiers and nonexistence
are established by the symbolic arguments above.

## 5. Issue ledger

### Fatal

None.

### Major

None.

### Local

1. **Unidentified finite dependency in `proof/main_proof.md`, lines 70--85.**
   The phrase "the certificate" does not identify a file, and the repository
   contains multiple files named as certificates.  The required half-word
   list is in `certificates/zero_set_certificate.json`, not
   `verifier/certificate.json`.  The data are present and independently pass,
   so this is not a mathematical gap in the project artifact.  Repair: name
   the exact file (and preferably print the 14 short seeds in an appendix).

2. **Incomplete description of the cyclic window transitions in
   `proof/main_proof.md`, lines 65--67.**  During a full cyclic tour there are
   two nontrivial transitions, \(+1\to-1\) and later \(-1\to+1\), not just the
   one transition described in the prose.  The piecewise formula in Section
   2.2 above supplies the missing sentence and proves that neither transition
   hits zero.  No hypothesis or conclusion changes.

### Expository

1. In `proof/builder_notes.md`, lines 137--159, the stated ratio bound assumes
   both signs occur, while the \(n=12\) intermediate congruence list also
   contains \(p=0,12\).  Those two cases are immediately excluded by the
   no-three rule, but the table transition should say this explicitly.

2. In `proof/main_proof.md`, lines 74--78, the claimed beginning, ending, and
   seam of the prefix apply only when \(m>20\).  For \(12\le m\le20\) the
   prefix is empty and the certified seed is used unchanged.  Splitting those
   two cases would remove the harmless empty-prefix ambiguity.

3. The word in `proof/main_proof.md`, line 83, is the full length-20
   difference word for \(n=20\), not a half-word for \(m=10\).  Its length and
   role are correct; labelling it explicitly would make the exception easier
   to parse.

## Final certification statement

Under the exact graph definition in `problem/formal_statement.md`, the proof
of the zero set is mathematically complete.  No proof assistant was used in
this referee audit.  The verdict is **PASS with local edits recommended**.

## Remediation recheck

The builder and main proofs were revised after the preceding audit.  I read
both revised files in full and rechecked every requested repair against the
difference-word reduction, the one-flip lemma, and the endpoint coverage.
This section supersedes the earlier recommendation status.

Rechecked versions (SHA-256):

| File | SHA-256 |
|---|---|
| `problem/formal_statement.md` | `0796f4e5af9890b77240d3f281f9ae149edaac7576b259ba096468b487b59db4` |
| `proof/builder_notes.md` | `d01158e7a473289615d5156503c0f7f36afa260e753b5620cdba90f51b94b114` |
| `proof/main_proof.md` | `15c726c86dc70e3a72ab6ec8976db5daee8b9a82bcfd8eff79a573d2d36cf672` |
| `certificates/zero_set_certificate.json` | `ff2d77c2e21b883c6588036137c5482f72a2bbfff3723151d8ab5b72f66a677c` |

Remediation results:

1. **Prior local issue 1 — resolved.**  Main-proof lines 73--76 now name
   `certificates/zero_set_certificate.json` explicitly and state exactly the
   set of supplied half-lengths.  This is the correct artifact, and its seed
   data remain unchanged.
2. **Prior local issue 2 — resolved.**  Main-proof lines 64--69 now describe
   both nontrivial half-window transitions: \(+1\to-1\) in the first
   half-tour and \(-1\to+1\) in the second.  At all other paired indices the
   signs agree, so the residue stays fixed.  This is the exact cyclic window
   profile and proves that zero is never reached.
3. **Prior expository issue 1 — resolved.**  Builder lines 142--143 explicitly
   exclude the one-sign words before applying the ratio bound.  The
   \(p=0,12\) entries in the intermediate \(n=12\) congruence list therefore
   cause no logical ambiguity.
4. **Prior expository issue 2 — resolved.**  Main-proof lines 78--83 separate
   the unchanged seeds for \(12\le m\le20\) from the genuinely nonempty
   prefix construction for \(m>20\).  For \(m>20\), the selected
   \(r\in\{12,\ldots,20\}\) satisfies \(m-r\ge9\), so the stated prefix is
   indeed nonempty; its length, residue, seam, and endpoint claims remain
   correct.
5. **Prior expository issue 3 — resolved.**  Main-proof lines 85--91 now call
   the \(m=10\) witness a full length-20 difference word.  Its role and order
   are unambiguous.

As a fresh diagnostic, an independent in-memory check computed every cyclic
half-window residue for all 14 literal one-flip seeds and checked the
nonempty-prefix rule for every \(21\le m\le100\).  It returned:

```text
PASS remediation smoke: exact two-flip window profile for 14 seeds; nonempty-prefix rule m=21..100
```

No repair changed the colour constructions, the \(n=6\) collision handling,
the \(n=4k\) endpoint ranges, or the four nonexistence arguments.  No new
fatal, major, local, or expository issue was introduced.

**Final remediation verdict: PASS.  Unresolved items: none.**
