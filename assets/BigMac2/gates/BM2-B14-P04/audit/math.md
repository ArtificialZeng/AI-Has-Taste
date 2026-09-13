# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the exact `resolution-paper` claim frozen by snapshot digest
`b351e94f1f6cf09be64035e87dd55329cfebe1ebaade24939abc0aa76f1c9837`:
the minimum total element-occurrence cost of a local realizer of
\(B_3=(2^{[3]},\subseteq)\) is 16, and hence
\(\operatorname{rdim}(B_3)=2\). I recomputed the canonical snapshot digest
and the SHA-256 digest of every listed file; all agree with
`audit/snapshot.json`. In particular, the immutable `source.md` has digest
`a91b0542ab546f82a1c5bdfa5d81d1b62f0c112ef70504ffa677a98f556a98e8`.

The interpretation in `problem.md` matches the full original scope. A local
realizer must cover every element and every unordered comparable pair, and it
must realize both orientations of every unordered incomparable pair. Thus the
problem is exactly a weighted set-cover problem whose columns are all PLEs and
whose column cost is the PLE's cardinality. No proper-part, fractional, or
asymptotic variant has been substituted.

## Upper bound reconstructed

Using the integer encoding in the certificate, consider

```text
M1 = 0 1 2 3 4 5 6 7
M2 = 4 2 6 1 5 3
M3 = 5 2
```

`M1` is a full linear extension. In `M2`, the required rank-one-to-rank-two
relations are
\(1<3,5\), \(2<3,6\), and \(4<5,6\), all of which hold; `M3` contains two
incomparable elements and is therefore a PLE. The full extension covers every
element and comparable pair. It orders the singleton antichain as
\(1<2<4\) and the doubleton antichain as \(3<5<6\), while `M2` gives the
reverse order on each antichain. For the three complementary incomparable
pairs, `M2` supplies the orientation opposite to `M1` for \(\{1,6\}\) and
\(\{4,3\}\); `M3` supplies it for \(\{2,5\}\). Hence all nine incomparable
pairs occur in both orientations. The cost is \(8+6+2=16\).

## Lower bound reconstructed

I independently checked the proposed nonnegative covering-dual weights. They
are:

- weight \(1/3\) on each of \((0,D)\) and \((D,7)\), for the three
  doubletons \(D\);
- weight \(2/3\) on both orientations of every pair of singletons and both
  orientations of every pair of doubletons; and
- weight \(2\) on the three orientations \(6<1\), \(5<2\), and \(3<4\).

Their sum is
\(6/3+12(2/3)+3(2)=16\). It remains to check every PLE-column inequality.
For an arbitrary PLE \(M\), let \(s,d,e\) count respectively its singleton
elements, doubleton elements, and endpoint elements among \(\{0,7\}\). Let
\(q\) count the three weight-2 orientations covered by \(M\). Directly from
the listed weights, its dual load is

\[
 W(M)=\frac{ed}{3}+\frac23\binom{s}{2}
      +\frac23\binom{d}{2}+2q.
\]

There cannot be two heavy orientations in a PLE. Writing
\(D_i=[3]\setminus\{i\}\), if distinct heavy orientations
\(D_i<i\) and \(D_j<j\) both held, the inclusion relations
\(i<D_j\) and \(j<D_i\) would force the strict cycle
\(D_i<i<D_j<j<D_i\). Therefore \(q\leq1\).

Since \(d\leq3\), the endpoint contribution satisfies \(ed/3\leq e\). If
\(q=0\), then for each \(u\in\{s,d\}\subseteq\{0,1,2,3\}\),
\(u(u-1)/3\leq u\), so \(W(M)\leq e+s+d=|M|\). If \(q=1\), then
\(s,d\geq1\), and

\[
 s(4-s)+d(4-d)\geq 3+3=6.
\]

After rearrangement this is exactly
\[
 \frac23\binom{s}{2}+\frac23\binom{d}{2}+2\leq s+d,
\]
so again \(W(M)\leq|M|\). The empty PLE has load and cost zero. Thus every
possible PLE satisfies the dual constraint, without reliance on a solver or
on finite enumeration.

Every local realizer covers each requirement at least once. Summing the
nonnegative requirement weights and then applying the column inequalities
gives
\[
 16\leq\sum_M W(M)\leq\sum_M |M|.
\]
This proves the required universal lower bound, including families with any
finite number of PLEs. Together with the upper witness it proves optimum cost
16 and relative dimension \(16/8=2\).

## Exact replay and adversarial checks

I ran `python3 evidence/verify_certificate.py` afresh. It exited successfully
using exact rational arithmetic, regenerated all 1,323 nonempty PLEs by
minimal-element recursion, independently matched them against the PLEs among
all 109,600 nonempty partial permutations, checked all 1,324 column
inequalities including the empty PLE, and directly checked the upper witness
against all 45 coverage requirements. Its output agrees with the frozen
`evidence/verification.json`.

The proof handles the potentially troublesome cases explicitly: diagonal
pairs force element occurrence; comparable pairs require co-occurrence;
incomparable pairs require both orientations; empty PLEs have no effect; and
no division, limiting argument, compactness assertion, or unverified solver
status is used. The dual is rational and its universal feasibility proof is
self-contained.

## Prior-result comparison and limitation

The frozen literature record identifies arXiv:2609.05166v1 as the nearest
result: it supplies the same cost-16 upper witness and, in the inspected text,
states only \(\operatorname{rdim}(B_3)\leq2\). The candidate's precise delta
is the explicit value-16 rational lower certificate above. The supplied
search was bounded and does not prove global priority or open status; the
claim and contribution appropriately limit the comparison to the inspected
v1 text. This disclosed literature limitation does not create a gap in the
mathematical resolution of the frozen original statement.

## Verdict

**Accept.** The candidate proves the original claim at its exact frozen scope,
the upper and lower certificates are independently checkable, and the stated
contribution is precise and conservatively bounded. I found no mathematical
gap requiring revision.
