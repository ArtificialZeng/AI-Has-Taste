# Supplementary appendix: the alternate one-flip proof

This file is retained only as an independently checked alternative proof and
is not the release manuscript's main proof.  The canonical proof is the
shorter explicit colour-block argument in `proof/builder_notes.md` and
`paper/main.tex`.  Source and novelty audits for the theorem are complete.

## 1. Difference-word reduction

Identify the three colours with \(\mathbb Z/3\mathbb Z\).  For a colouring
\(c_0,\ldots,c_{n-1}\), set
\[
 d_i=c_{i+1}-c_i\pmod 3,
\]
where indices are cyclic, and represent the two nonzero residues by the
integers \(+1\) and \(-1\).  The cycle edges are proper exactly when every
\(d_i\in\{+1,-1\}\), and the colours close exactly when
\(\sum_i d_i\equiv0\pmod3\).

Moreover,
\[
 c_{i+3}-c_i=d_i+d_{i+1}+d_{i+2}.
\]
A sum of three signs is divisible by three exactly when the three signs are
equal.  Thus all offset-three chords are proper exactly when the cyclic sign
word has no three consecutive equal signs.  If \(n=2m\), the diameter from
\(i\) to \(i+m\) is proper exactly when every cyclic length-\(m\) window has
sign sum nonzero modulo three.  These conditions are therefore necessary and
sufficient.

## 2. Odd orders

Let a cyclic sign word contain \(p\) plus signs and \(q\) minus signs.  If
\(p,q>0\) and \(\max(p,q)\le2\min(p,q)\), it can be arranged with no run of
length three.  Explicitly, if \(p\ge q\), put \(r=p-q\) and take
\[
  (++-)^r(+-)^{q-r};
\]
if \(q\ge p\), interchange the signs.  The word also has a safe cyclic seam.

For \(n=6k+1\), \(k\ge2\), take
\((p,q)=(3k+2,3k-1)\).  For \(n=6k+3\), \(k\ge1\), take
\((p,q)=(3k,3k+3)\).  For \(n=6k+5\), \(k\ge1\), take
\((p,q)=(3k+1,3k+4)\).  In every case the displayed inequalities hold and
\(p-q\equiv0\pmod3\), so the resulting sign word gives a proper colouring.
This covers every odd \(n\ge9\).

For \(n=7\), closure forces \(2p-7\equiv0\pmod3\), hence
\(p\in\{2,5\}\).  Five copies of one sign cannot be placed cyclically among
two copies of the other without a run of three (the two minority signs create
only two gaps, each of capacity two).  Hence \(n=7\) is impossible.

## 3. Even-order construction

We use the following elementary one-flip lemma.  Suppose a length-\(m\) word
\(a=(a_0,\ldots,a_{m-1})\) satisfies

1. \(a_0=+1\) and \(\sum a_i\equiv1\pmod3\);
2. it has no three consecutive equal signs internally;
3. \(a_1\ne a_2\), \(a_{m-2}\ne a_{m-1}\), and
   \(a_{m-1}\ne a_1\).

Let \(b=(-a_0,a_1,\ldots,a_{m-1})\) and \(d=ab\).  The endpoint conditions
check directly that \(d\) has no cyclic run of length three, while
\(\sum d=2\sum a-2a_0\equiv0\pmod3\).  Initially a half-window has residue
\(\sum a_i=1\).  During the first half-tour the residue changes only when
the mismatched pair \((a_0,b_0)=(+1,-1)\) crosses an endpoint, at which point
it changes from \(+1\) to \(-1\); during the second half-tour the reverse
crossing changes it from \(-1\) back to \(+1\).  At every other step the
paired signs agree and the residue is unchanged.  Thus it is never zero.
The reduction in Section 1 proves that \(d\) yields a proper colouring of
\(C_{2m}^{(3)}\).

The file `certificates/zero_set_certificate.json` gives literal half-words
satisfying the lemma for
\[
 m\in\{3,5,7,9,11,12,13,\ldots,20\}.
\]
For \(12\le m\le20\), use the certified \(m\)-word unchanged.  For \(m>20\),
choose the unique \(r\in\{12,\ldots,20\}\) with \(m\equiv r\pmod9\), and
prefix the certified \(r\)-word by \((++-)^{3(m-r)/9}\).  This nonempty
prefix has length \(m-r\), sign sum divisible by three, begins \(++-\), ends
in \(-\), and has no run of three.  Its seam with every certified word is
\(-++-\).  Consequently all hypotheses of the one-flip lemma are preserved.
This proves existence for all even orders
except possibly \(2m\) with \(m\in\{4,6,8,10\}\).  The first three will be
excluded below; for \(m=10\), the certificate's literal full length-20
difference word
\[
 ++-++-++-++-++-++-+-
\]
directly satisfies the necessary and sufficient sign conditions.

## 4. The three even exceptions

Let \(n=2m\in\{8,12,16\}\), and let \(p\) be the total number of plus signs
in a hypothetical valid difference word.  The absence of a cyclic run of
three implies \(\lceil n/3\rceil\le p\le\lfloor2n/3\rfloor\).  Combining this
with \(2p-n\equiv0\pmod3\) gives \(p=n/2\) in each of the three cases.

Let \(w_i\) be the number of plus signs in the cyclic length-\(m\) window
starting at \(i\).  Its average over all \(n\) starting positions is
\(mp/n=m/2\), and \(|w_{i+1}-w_i|\le1\).  If no \(w_i\) equalled \(m/2\),
then the cyclic list could not contain values on both sides of \(m/2\), while
its average could not equal \(m/2\) if all values lay strictly on one side.
Thus some \(w_i=m/2\).  That half-window has sign sum
\(2w_i-m=0\), so its diameter endpoints receive the same colour, a
contradiction.  Hence \(n=8,12,16\) are impossible.

Sections 2--4 prove that for every \(n\ge6\), a proper three-colouring exists
if and only if \(n\notin\{7,8,12,16\}\).
