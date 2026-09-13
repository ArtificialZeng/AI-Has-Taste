# Certified finite result for the first previously unverified relation

## Result

Let `s=s_{123,132}` and let `M_N` be defined as in
`problem/formal_statement.md`.  Complete exact enumeration gives

\[
 |M_{13}|=47\,265\,120,
 \qquad
 |M_{14}|=378\,120\,960.
\]

Consequently,

\[
 \boxed{|M_{14}|=8|M_{13}|}.
\]

This is a certified finite result for the parameter `n=7`.  It is not a
proof of Conjecture 4.4 for all positive integers.

## 1. Exact local form of the stack map

The current stack avoids both `123` and `132`.  If the next input is `x`, a
new forbidden triple must use `x` as its first (topmost) entry.  The two
forbidden patterns cover the two possible relative orders of the later two
entries.  Thus pushing `x` is illegal if and only if at least two current
stack entries exceed `x`.  This proves the evaluator used in Enumerator A.

## 2. Large-label factorization

Fix `N` and a threshold `m`.  Define the skeleton `kappa_m(pi)` by retaining
the entries `1,...,m` with their labels and replacing every entry greater
than `m` by a common symbol `L`.

Define a symbolic map `F_m` on skeletons as follows.  Read the skeleton from
left to right.  Always push an `L`.  For a small token `x`, pop while at least
two current stack tokens belong to

\[
 \{x+1,x+2,\ldots,m,L\},
\]

then push `x`.  Flush the stack after the input is exhausted.

### Lemma (factorization)

For every permutation `pi`,

\[
 \kappa_m(s(\pi))=F_m(\kappa_m(\pi)).
\]

### Proof

A forced pop caused by an input value `y>m` can only pop another value
greater than `m`.  Indeed, if the stack top were `z<=m<y`, illegality of the
push would require two entries below `z` that exceed `y`; then `z` together
with those two entries would already form `123` or `132` in the current
stack, a contradiction.

Collapse all values greater than `m` to `L`.  A pop caused by a large input
may now be delayed: it moves a top `L` to the output and cannot cross a small
stack entry.  If another large input arrives first, only the order among
indistinguishable `L` tokens changes.  If a small input arrives first, every
delayed `L` exceeds it.  The actual execution retains at least the most
recently pushed large entry, so the delayed execution has at least two large
tokens precisely until the delayed extras have been popped; those extras
therefore leave before any small token can cross them.  If no small input
remains, the final flush has the same effect after projection.

Commuting every large-caused pop in this way makes every large input an
immediate push.  When a small input `x` is processed, the actual legality
test depends only on the number of current entries exceeding `x`, which
after projection is exactly the number of tokens in
`{x+1,...,m,L}`.  The projected execution is therefore `F_m`.  This proves
the identity.  Applying it inductively proves
`kappa_m(s^r(pi))=F_m^r(kappa_m(pi))` for all `r>=0`.  QED.

For the minimally-sorted problem take

\[
 m=\left\lfloor\frac{N-1}{2}\right\rfloor.
\]

Berlow's theorem says periodicity is exactly the half-decreasing condition,
which refers only to the labelled small entries `1,...,m`.  Hence the
transient length, and therefore membership in `M_N`, depends only on the
skeleton.  Every skeleton has exactly `(N-m)!` lifts to `S_N`, obtained by
arbitrarily assigning the large labels.  If `Q_N` is the set of qualifying
skeletons, then

\[
 |M_N|=|Q_N|(N-m)!.
\]

## 3. Complete skeleton enumeration

A skeleton is specified by choosing the `m` positions of the small labels
and ordering those labels.  Therefore the exact search size is

\[
 \binom Nm m!=\frac{N!}{(N-m)!}.
\]

For `N=13,14`, `m=6`.  The verifier enumerated respectively

\[
 \frac{13!}{7!}=1\,235\,520,
 \qquad
 \frac{14!}{8!}=2\,162\,160
\]

skeletons.  Starting from each skeleton it repeatedly applied `F_6` and
recorded the first half-decreasing iterate.  Zhang's theorem bounds that
iterate by `12`.  Exactly `9,378` skeletons attain `12` at each length.
Thus

\[
 |M_{13}|=9\,378\cdot7!=47\,265\,120,
\]

\[
 |M_{14}|=9\,378\cdot8!=378\,120\,960.
\]

All arithmetic is integer arithmetic.

## 4. The requested natural 8-to-1 map

The full verifier checked the stronger finite identity

\[
 Q_{14}=\{wL:w\in Q_{13}\}.
\]

Thus define

\[
 D:M_{14}\longrightarrow M_{13},\qquad
 D(\pi)=\operatorname{std}(\pi_1\cdots\pi_{13}).
\]

Every qualifying length-14 skeleton ends in `L`, so `pi_14` lies in
`{7,...,14}` and `D(pi)` has a qualifying length-13 skeleton.  Conversely,
for `q in M_13` and each `j in {7,...,14}`, the terminal insertion

\[
 E_j(q)=(q_1+1_{q_1\ge j})\cdots(q_{13}+1_{q_{13}\ge j})j
\]

has skeleton `kappa_6(q)L` and lies in `M_14`.  These eight insertions are
distinct, exhaust the fiber of `D`, and satisfy `D(E_j(q))=q`.  Hence `D` is
exactly 8-to-1.

The certificate proves this statement only for the finite pair `(13,14)`;
the analogous all-`n` skeleton-extension statement remains a conjectural
proof route.

## 5. Independent verification

The machine-readable certificate is
`certificates/n1_to_n7_counts.json`.  The no-import verifier
`code/verify_certificate.py` reconstructs every skeleton rather than reading
the C++ discovery outputs.  It rejects malformed schemas, missing or
duplicate records, boolean-as-integer fields, altered counts, source hash
mismatches, and unexpected keys.

Reproduction command:

```sh
code/verify_certificate.py certificates/n1_to_n7_counts.json
```
