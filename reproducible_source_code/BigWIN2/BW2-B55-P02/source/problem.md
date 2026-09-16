# Precise problem interpretation

## Frozen claim

The immutable statement is `source.md` (SHA-256
`66bd29461d230e70ebd25d85636d33bb9132c518790efc445618077a3ba1df4b`).
It is read literally as the following universal assertion.

For every real number \(\delta\) satisfying
\[
0<\delta<\frac16,
\]
fix threshold \(T=1\), Step-2 threshold \(\beta=2/3\), machines
\(\{0,1,2\}\), and jobs \(J=\{q,h,r\}\) with sizes, eligibility sets, and
fractional assignments
\[
\begin{array}{c|c|c}
j & p_j & \{(i,x_{ji}):x_{ji}>0\}\\ \hline
q&1&\{(0,\frac13+\delta),(1,\frac23-\delta)\}\\
h&\frac12&\{(0,\frac23),(2,\frac13)\}\\
r&\frac13-\delta&\{(0,1)\}.
\end{array}
\]
There is no quantification over other feasible fractional points or over an LP
solver's output.

At \(T=1\), a job is big precisely when its size is strictly greater than
\(1/2\). Thus only \(q\) is big. Its two shares are both strictly below
\(\beta\) throughout the stated interval, so Step 2 assigns no job. Equality
at either threshold is interpreted exactly as in the source algorithm; no
endpoint \(\delta=0\) or \(\delta=1/6\) is in scope.

## Slot graph and valid matchings

On each machine \(i\), concatenate its surviving fractional job intervals in
nonincreasing order of \(p_j\). All relevant size inequalities are strict:
\(p_q>p_h>p_r>0\), so no tie-breaking choice occurs. If
\(M_i=\sum_j x_{ji}\), create slots
\[
S_{i,z}=[z-1,\min\{z,M_i\}),\qquad z=1,\ldots,\lceil M_i\rceil.
\]
A job vertex \(j\) is adjacent to \(S_{i,z}\) exactly when its half-open
fraction interval on machine \(i\) has nonempty intersection with
\(S_{i,z}\). Merely sharing an endpoint does not create an edge.

A valid Step-3 matching saturates every surviving job, assigns at most one job
to each slot, and uses only adjacency edges. Slots need not all be matched.
The induced integral schedule assigns each job to the machine containing its
matched slot. Its machine loads and makespan are
\[
L_i=\sum_{j\text{ matched to a slot on }i}p_j,
\qquad C_{\max}=\max_{i\in\{0,1,2\}}L_i.
\]
Distinct slot matchings are counted separately even if they induce the same
machine assignment and makespan. Thus “exactly eight” refers to matchings in
the bipartite job-slot graph, while the requested multiset counts their eight
induced makespans with multiplicity.

The proposition to prove or disprove is simultaneously:

1. for every \(\delta\in(0,1/6)\), the graph has exactly eight valid
   matchings;
2. the minimum of \(C_{\max}\) over those matchings is \(1\);
3. the maximum is \(11/6-\delta\).

The complete makespan multiset is an optional strengthening, not part of the
truth conditions of the three-part claim.

## Symbolic triage normalization

Writing \(A=S_{0,1}\), \(B=S_{0,2}\), \(C=S_{0,3}\),
\(D=S_{1,1}\), and \(E=S_{2,1}\), the intervals are
\[
\begin{array}{c|c|c}
i&\text{job intervals}&\text{slot intervals}\\ \hline
0&q:[0,\frac13+\delta),\ h:[\frac13+\delta,1+\delta),\
r:[1+\delta,2+\delta)&A:[0,1),\ B:[1,2),\ C:[2,2+\delta)\\
1&q:[0,\frac23-\delta)&D:[0,\frac23-\delta)\\
2&h:[0,\frac13)&E:[0,\frac13).
\end{array}
\]
Every displayed interval has positive length throughout the open parameter
range. The resulting candidate edge sets are
\[
N(q)=\{A,D\},\qquad N(h)=\{A,B,E\},\qquad N(r)=\{B,C\}.
\]
There is no interior ordering or contact breakpoint. A triage-level hand
enumeration gives the eight templates
\[
(A,B,C),(A,E,B),(A,E,C),(D,A,B),(D,A,C),(D,B,C),(D,E,B),(D,E,C),
\]
where coordinates list the slots of \((q,h,r)\). This is recorded as a
discriminating sanity check, not as an independently audited resolution.

## Scope exclusions

The claim says nothing about the approximation ratio on arbitrary instances,
which feasible point Step 1 selects, vertex solutions, closed-interval slot
conventions, parameter endpoints, or Step-2 thresholds other than \(2/3\).
It does not assert that the optional multiset has eight distinct values.

## Prior-result check and correction

Primary manuscript inspected on 2026-09-07: arXiv:2609.03890v1,
<https://arxiv.org/abs/2609.03890>, and the local PDF at
`/home/ailab/4math-open-problems/batches/inbox/bigWin-55-materials/2609.03890.pdf`
(verified SHA-256
`889389afa75709325024fa890fb809ad125e09e607517a963e45a4b368de6b05`).
Theorem 2 (PDF pp. 10--11) proves, for every allowed \(\delta\), feasibility,
\(\mathrm{OPT}=1\), and existence of the matching \((A,B,C)\) with makespan
\(11/6-\delta\). Measurement 4 (PDF p. 11) reports eight matchings, best
makespan \(1\), and worst makespan \(11/6-\delta\) only at
\(\delta\in\{10^{-2},10^{-3},10^{-4}\}\), explicitly as measurement. The
inspected manuscript does not state the frozen full-parameter enumeration as a
theorem. A bounded exact-assertion/nearest-result search found this source and
no separate primary theorem settling the symbolic enumeration; that is a
search report, not a priority proof.

Bibliographic correction, without changing `source.md`: the cited identifier
and verified local PDF are titled *The 11/6 supremum of the Wang--Sitters
rounding scheme for graph balancing* by Adam Y. Shavit, not *The hidden output
space of a classical rounding scheme*. The stable arXiv identifier and matching
PDF hash make the intended source unambiguous, so the title discrepancy does
not affect the mathematical reading.

## Triage classification and target

Source status: **new-question**. Suitability: **advance**. Nearest prior result
is Theorem 2 plus finite Measurement 4; proposed delta is a uniform symbolic
enumeration on \((0,1/6)\); verification route is an invariant half-open
adjacency calculation, exhaustive matching list, affine load calculation, and
independent exact-rational replay.

## Research-pass resolution of the frozen claim

**Proposition.** For every real \(0<\delta<1/6\), the slot graph has exactly
eight job-saturating matchings.  Their makespan multiset, with slot matchings
counted with multiplicity, is
\[
 \left\{\left(\frac{11}{6}-\delta\right)^1,
 \left(\frac43-\delta\right)^2,1^5\right\}.
\]
Consequently the three assertions in `source.md` hold: the minimum makespan is
\(1\), and the maximum is \(11/6-\delta\).

**Proof.** The strict inequalities
\[
p_q=1>p_h=\frac12>p_r=\frac13-\delta>0
\]
fix the concatenation order on machine 0; the other two machines contain one
fractional job each.  The fractional masses are
\[
M_0=2+\delta,\qquad M_1=\frac23-\delta,\qquad M_2=\frac13.
\]
Thus there are three slots on machine 0 and one on each other machine.  Since
\(0<\delta<1/6\), each displayed slot in the symbolic-normalization table is
nonempty, and no mass crosses an integer inside the parameter interval.

For half-open intervals \([a,b)\) and \([c,e)\), nonempty intersection is
equivalent to the two strict inequalities \(b-c>0\) and \(e-a>0\).  Applying
this test to the intervals in the table gives, uniformly on the entire open
parameter interval,
\[
N(q)=\{A,D\},\qquad N(h)=\{A,B,E\},\qquad N(r)=\{B,C\}.
\]
For example, the contacts that exist only because \(\delta>0\) are \(hB\)
and \(rC\), whose positive overlap lengths are both \(\delta\).  The closest
nonedges remain strict: for \(qB\), the relevant signed gap is
\(-2/3+\delta<0\); for \(rA\), it is \(-\delta<0\).  The full list of exact
signed contact tests is serialized in `evidence/exact_replay_output.json`.

It remains to enumerate injective choices from these three neighborhoods.  If
\(q\) uses \(A\), then \(h\) uses either \(B\) or \(E\); the former forces
\(r\) to \(C\), while the latter allows \(B\) or \(C\).  This gives three
matchings.  If \(q\) uses \(D\), then \(h\) may use \(A,B,E\), yielding,
respectively, two, one, and two choices for \(r\).  This gives five more and
exhausts the Cartesian product of the neighborhoods.  In the coordinate order
\((q,h,r)\), the eight matchings and their exact loads are
\[
\begin{array}{c|c|c}
\text{matching}&(L_0,L_1,L_2)&C_{\max}\\ \hline
(A,B,C)&(11/6-\delta,0,0)&11/6-\delta\\
(A,E,B)&(4/3-\delta,0,1/2)&4/3-\delta\\
(A,E,C)&(4/3-\delta,0,1/2)&4/3-\delta\\
(D,A,B)&(5/6-\delta,1,0)&1\\
(D,A,C)&(5/6-\delta,1,0)&1\\
(D,B,C)&(5/6-\delta,1,0)&1\\
(D,E,B)&(1/3-\delta,1,1/2)&1\\
(D,E,C)&(1/3-\delta,1,1/2)&1.
\end{array}
\]
Here matching different slots on the same machine can yield the same schedule,
which is why rows are not collapsed.  Finally,
\(11/6-\delta>4/3-\delta>1\) throughout the domain, while every non-unit load
in the last five rows is below \(1\).  The table therefore proves the stated
multiset and extrema. \(\square\)

## Exact replay certificate

`evidence/exact_replay.py` independently reconstructs the size order,
fractional intervals, slot counts, and every job-slot contact from the instance
data using only integer and rational arithmetic on affine expressions
\(a+b\delta\).  It verifies constant signs over both endpoints of the open
domain, finds no interior contact or slot-count breakpoint, tests all 12 raw
neighborhood choices for injectivity, and derives the eight load vectors before
comparing them with the templates above.  Its deterministic output is
`evidence/exact_replay_output.json`.

This proves the frozen mathematical claim but does not prove a claim about any
other fractional point or a general behavior of the rounding algorithm.  The
comparison with the primary manuscript remains as stated above: its Theorem 2
contains the first row uniformly, while its Measurement 4 reports the complete
count and extrema only at three sampled parameter values.
