# win-00070-p04 — Certified zero count in a finite Fibonacci-zeta rectangle

## Immutable primary-source record

- Primary source: Marco Mantovanelli, *The Right Edge of the Zero Set of the Fibonacci Zeta Function*, arXiv:2609.04993v1 [math.NT], 4 September 2026.
- Official abstract: <https://arxiv.org/abs/2609.04993v1>.
- Official HTML: <https://arxiv.org/html/2609.04993v1>.
- Definition and Theorem 1.1: HTML 61–116; Diophantine cusp: Proposition 7.3, HTML 633–668; heuristic and exploratory zeros: HTML 669–709.
- Access record: official arXiv HTML was read directly on 2026-09-08. The official PDF is archived as batch material.

## Frozen assertion

Let \(F_1=F_2=1\), \(F_{n+2}=F_{n+1}+F_n\), and for \(\Re s>0\) let
\[
Z_F(s)=\sum_{n\ge1}F_n^{-s}.
\]
Zeros are counted with analytic multiplicity. Determine the exact integer
\[
N_{0.73}(8596696)
=\#\{\rho:Z_F(\rho)=0,\ \Re\rho\ge0.73,\ 0<\Im\rho\le8596696\}.
\]
In addition, determine whether the closed disk
\[
\left|s-(0.730178633163+8596695.206382i)\right|\le10^{-6}
\]
contains exactly one zero and whether that zero is simple.

An acceptable resolution must certify completeness of the rectangle, not merely refine the displayed approximate zero.

## Nearest result and precise delta

Theorem 1.1 proves that \(Z_F\) has no zeros for \(\Re s\ge\sigma_F\), where \(\sigma_F\approx0.7431633987\), and Proposition 7.3 supplies a Diophantine zero-free cusp near that edge. Section 7 lists eight exploratory near-edge zeros, ending with the center frozen above, but explicitly says the search was targeted rather than exhaustive and that the negative search up to height \(10^8\) is not used in any proof.

The delta is a complete finite zero count with existence, uniqueness, multiplicity, and exclusion certificates in the region naturally singled out by the final table entry. It does not assert the source's shrinking-target prediction or the global value of a first-hitting function.

## Cheapest decisive attack

Apply the source's phase-lock inequalities to \(\Re s\ge0.73\), keeping all constants explicit, to reduce possible ordinates to intervals in which \(t\log2\) and \(t\log3\) are simultaneously close to odd multiples of \(\pi\). Enumerate those intervals completely up to height 8596696 using continued fractions or exact lattice reduction, and record the enumeration certificate.

On each remaining complex box, evaluate a finite truncation of \(Z_F\) and its derivative with directed-rounding complex balls. Prove a uniform tail bound from explicit Fibonacci growth. Use interval Newton or Krawczyk operators to isolate each simple zero. Use a certified argument-principle winding number on the rectangle boundary and/or a complete zero-exclusion cover for all other boxes to establish completeness and multiplicity.

The first go/no-go test is the size of the rigorously phase-locked candidate family. If it remains too large for a complete cover within one research pass, park with the exact reduction instead of presenting a targeted search as exhaustive.

## Failure risks

- A high-precision residual at the listed point proves neither existence nor uniqueness.
- The infinite Dirichlet-series tail must be bounded uniformly over every complex box.
- Argument-principle use requires a certified nonzero boundary and correct winding computation.
- Phase-lock inequalities are necessary conditions only unless the later analytic verification is complete.
- The vertical boundary at \(\Re s=0.73\), horizontal boundaries, conjugation symmetry, and zeros on boundaries must be handled explicitly.

## Semantic boundary

No registry entry was found for arXiv:2609.04993 or Fibonacci zeta zeros. Existing Fibonacci-related combinatorics projects concern finite words or recurrences, not zeros of this Dirichlet series.
