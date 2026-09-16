# Fresh mathematical referee report

**Job:** `win-00063-p02-referee-edd8a170acfc`  
**Frozen snapshot:** `6c1265a85e773577b5043ae72f2a6374f20d3259fcde2383b7e1cf384d12240f`  
**Verdict:** **accept**

## Scope reviewed

The frozen candidate is the full-scope statement that, for every integer
\(r\ge 2\), the unique minimizing Johnson-scheme index is \(2\). This implies
the least allowed threshold \(r_0=2\), with an empty exception range. I checked
the SHA-256 digest of every frozen file against `audit/snapshot.json`; all
matched. In particular, the attached primary-source PDF matched its recorded
digest.

The candidate addresses the original question without weakening its domain or
changing the definition of the graph. The index range checked is the complete
range \(0\le j\le 2r\), and the claim of uniqueness is material because the
problem asks for all ties.

## Reconstruction of the decisive proof

Put

\[
\Delta=\binom{2r}{r}\binom{2r+2}{r},\qquad
\theta_j=E_r(j)/\Delta,
\]

and \(m_j=\binom{4r+2}{j}-\binom{4r+2}{j-1}\). Direct evaluation of the
given Eberlein sum gives

\[
\theta_0=1,\quad \theta_1=\frac1{2r+2},\quad
\theta_2=-\frac{2r^2+1}{(2r-1)(2r+2)(2r+1)},
\]

and

\[
\theta_3-\theta_2=\frac{r-1}{2(r+1)(2r+1)}>0.
\]

Thus indices \(0,1,3\) are strictly above index \(2\) for every \(r\ge2\).

For the remaining indices, cancellation in the multiplicities gives

\[
\frac{m_{j+1}}{m_j}=
\frac{(4r+1-2j)(4r+3-j)}{(j+1)(4r+3-2j)}.
\]

On the relevant range its denominator is positive, and the sign after
subtracting one is the sign of
\(g_r(j)=j^2-(4r+2)j+4r^2+3r\). Since
\(g_r(j+1)-g_r(j)=2j-4r-1<0\), the multiplicity sequence on
\(4\le j\le2r\) is single-peaked, so its minimum occurs at an endpoint.
For \(r\ge3\), binomial unimodality and \(2r\ge6\) reduce
\(m_{2r}\ge m_4\) to

\[
\frac{3(4r-2)}{5(2r+3)}\ge\frac{4r-5}{4r-1}.
\]

The cross-multiplied difference is \(8r^2-46r+81\), whose leading
coefficient is positive and whose discriminant is \(-476\). Hence
\(m_j\ge m_4\) for every \(4\le j\le2r\).

Because the graph is simple and \(\Delta\)-regular on
\(v=\binom{4r+2}{2r}\) vertices, its exact spectral trace identity is

\[
\sum_{j=0}^{2r}m_j\theta_j^2=\frac v\Delta.
\]

For
\(Q(r)=(v/\Delta)/(m_4\theta_2^2)\), exact cancellation gives
\(Q(3)=330/361<1\). The displayed ratio for \(Q(r+1)/Q(r)\) in the
candidate has positive denominator, and one minus that ratio has numerator

\[
384r^8+2032r^7+1276r^6+76r^5-236r^4+136r^3+439r^2+87r-18.
\]

This is positive for \(r\ge1\): the only negative terms are already dominated
by \(384r^8-236r^4-18\ge148r^4-18>0\), while all omitted terms are positive.
Therefore \(Q(r)<1\) for all \(r\ge3\).

If some \(j\ge4\) had \(\theta_j\le\theta_2<0\), then
\(\theta_j^2\ge\theta_2^2\), and the trace identity together with
\(m_j\ge m_4\) would imply

\[
\frac v\Delta\ge m_j\theta_j^2\ge m_4\theta_2^2,
\]

contradicting \(Q(r)<1\). Hence every index \(j\ge4\) is strictly above
index \(2\) for \(r\ge3\). At the only residual value \(r=2\), direct exact
evaluation yields \((90,15,-9,-6,6)\), again with unique minimizer \(2\).
This proves the full frozen statement and rules out all ties.

## Checks performed

- Recomputed all frozen-file SHA-256 values and confirmed the snapshot binding.
- Ran `evidence/tail_exact_audit.py`; all symbolic identities and the exact
  \(r=2\) spectrum passed.
- Ran `evidence/triage_exact_spectrum.py`; it found the unique minimizer \(2\)
  for every \(2\le r\le60\), and found the trace ratio below one for every
  tested \(r\ge3\).
- Wrote and ran a separate standard-library verifier,
  `audit/referee_exact_check.py`. It independently recomputed the Eberlein sums,
  multiplicities, explicit low-index formulas, and the full trace identity for
  every \(2\le r\le80\); it also checked the unique minimizer on that range and
  exact monotonic decrease of \(Q\) through \(r=250\). These finite checks are
  corroboration; the infinite conclusion rests on the algebraic proof above.
- Checked all relevant denominator signs and the boundary cases \(r=2\),
  \(j=0\), and \(j=2r\). No empty-domain, division-by-zero, limiting-exchange,
  or equality-case gap remains.

## Source comparison and contribution

The attached Luo--Cao--Li--Li PDF states the Eberlein formula and multiplicities
in equations (2.1) and (2.2). Its Proposition 12 says that under
\(t^2-t<4r-2\), \(E_r(2)\) is smallest for `J(4r+t,2r,r)` only for all
sufficiently large \(r\). At \(t=2\), this does not supply an explicit
threshold or classify the residual values. Theorem 13 is a consequence for a
quantum-chromatic lower bound and does not strengthen that threshold statement.

The candidate's exact monotone trace ratio makes the tail bound effective from
\(r=3\), and the exact \(r=2\) spectrum closes the sole residual case. Thus its
precise delta over the cited result is the sharp threshold and complete
exception/tie classification requested by the frozen problem. This comparison
is limited to the frozen primary source; the report makes no broader priority
claim.

## Verdict

**Accept.** The resolution-paper candidate proves the original claim in its
entire frozen scope, with exact comparisons, an infinite-tail argument, the
least allowed threshold, and a complete (empty) exception classification. I
found no mathematical or scope gap requiring revision.
