# Fresh mathematical referee report

Referee job: `bigMac-00007-p02-referee-ce689f96df77`  
Frozen snapshot: `eef04bbd239c132e1714ecf5692295d911d0b2fa5fcd1007a1777ad1ad1d7a52`

## Scope reviewed

I reviewed the exact `resolution-paper` statement in `claim.json`, including
all weights \(a,b\geq0\) with \(a+b>0\), the three cut regimes, the complete
projective classification of optimal translation-invariant GL semimetrics,
and the assertion that translation averaging loses no objective value.  I
reconstructed the argument from the definitions in the frozen `source.md` and
`problem.md`; I did not treat a weaker interior-only or value-only statement as
the candidate.

## Reconstruction and checks

1. For a cut of size \(k\), if \(c_1,c_2\) are its crossing counts in the two
   five-edge difference classes, direct counting of directed random-walk
   transitions gives
   \[
   N(A)=\frac{ac_1+bc_2}{5(a+b)},\qquad
   D(A)=\frac{2k(5-k)}{25}.
   \]
   Complementation reduces to \(k=1,2\).  The three dihedral types have
   signatures \((2,2),(2,4),(4,2)\), hence values
   \(5/4\), \(5(a+2b)/(6(a+b))\), and
   \(5(2a+b)/(6(a+b))\).  Pairwise comparison gives exactly the claimed
   strict chambers, and all three coincide only when \(a=b>0\).

2. For arbitrary feasible \(d(x,y)=\|p_x-p_y\|^2\), the average
   \(\bar d(x,y)=5^{-1}\sum_c d(x+c,y+c)\) is realized by
   \(q_x=5^{-1/2}(p_{x+c})_c\) in an orthogonal direct sum.  Averaging each
   translated triangle inequality proves all triangle inequalities for
   \(\bar d\).  Translation invariance of the finite uniform sums gives
   \(N(\bar d)=N(d)\) and \(D(\bar d)=D(d)\); in particular, an admissible
   positive denominator cannot collapse to zero.  Thus both infima are equal,
   with no compactness or limiting interchange involved.

3. An invariant distance matrix has first row \((0,u,v,v,u)\).  On the
   zero-sum Fourier modes its eigenvalues are
   \[
   u/\varphi-\varphi v\quad\text{and}\quad
   -\varphi u+v/\varphi
   \]
   (each twice).  The centered-Gram/CND criterion therefore gives the exact
   squared-Euclidean conditions
   \(u\leq\varphi^2v\) and \(v\leq\varphi^2u\), together with
   nonnegativity.  The two possible three-vertex distance multisets are
   \(\{u,u,v\}\) and \(\{u,v,v\}\), so the triangle inequalities are exactly
   \(v\leq2u\) and \(u\leq2v\).  Since \(2<\varphi^2\), these triangle
   inequalities imply the CND conditions.  Hence the full invariant GL cone
   is precisely the asserted two-ray cone; a nonzero point necessarily has
   \(u,v>0\).

4. On this cone,
   \[
   \frac{N(d)}{D(d)}=
   \frac{5(au+bv)}{2(a+b)(u+v)}.
   \]
   With \(r=u/(u+v)\), the cone is \(1/3\leq r\leq2/3\), and the variable
   part is \(b+(a-b)r\).  It has the unique projective minimizer
   \(r=1/3\) (equivalently \(v=2u\)) when \(a>b\), the unique minimizer
   \(r=2/3\) (equivalently \(u=2v\)) when \(b>a\), and is constant when
   \(a=b>0\).  Averaged adjacent-pair and difference-two cut metrics attain
   the endpoint rays.  Cut metrics are themselves GL-feasible, so this cone
   lower bound and the cut upper bound coincide.

The divisions above are safe because \(a+b>0\), nontrivial cuts have
\(k(5-k)>0\), and SDP competitors have \(D>0\).  The face cases \((a>0,b=0)\)
and \((a=0,b>0)\) give \(5/6\) with the claimed unique cut orbit and metric
ray.  At \(a=b>0\), every nontrivial cut and every nonzero invariant feasible
ray has value \(5/4\).  These checks cover all degenerate regimes allowed by
the statement.

I ran `evidence/check_finite.py`; it exactly verified all 30 nontrivial
subsets, all 10 vertex triples, and both averaged endpoint cut metrics.  I
also performed a separate exact rational enumeration for representatives of
both strict chambers, both coordinate faces, and the tie; it reproduced the
formula and precisely the asserted minimizing signatures.

## Source comparison and contribution

The frozen evidence identifies the nearest source results as the two
one-weight cycle faces and an exactness theorem whose minimizing-character
hypothesis requires image size at most four.  Every nontrivial character of
\(\mathbb Z/5\mathbb Z\) has image size five, so the full interior cone and
its equality classifications are not formal consequences of the cited
hypothesis.  The evidence records a dated, primary-record formula-level
screen and expressly limits it to an absence-of-match report; it makes no
priority claim.  Under that bounded wording, the self-contained interior
argument and complete equality classification constitute the stated exact
resolution.  No external bibliographic assertion is used as a lemma in the
proof.

## Gaps and verdict

I found no mathematical gap, missing equality case, hidden excluded domain,
or mismatch between the proved theorem and the frozen candidate scope.

**Verdict: accept.**
