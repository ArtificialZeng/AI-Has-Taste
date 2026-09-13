# Checkpoint

Job provenance: `bigMac-00005-p02-research-50bd812e77fa` (research pass 1).
`source.md` remains unchanged at SHA-256
`0dcd3cbf037a1923284cfaaead3837a1dd6d1fa6853d2d5de2ed64cd83cb954d`.

## New proved result

The complete branch \(\ell=1\) is now solved:
\[
\operatorname{OPT}_{m,1}=\max\{2m+2,5m/2\}
=\begin{cases}2m+2&m=2,3,\\5m/2&m\ge4.\end{cases}
\]
Hence \(J_{m,1}\) is fractionally Hamiltonian iff \(2\le m\le4\).
The proof and exact certificates are in `evidence/l1_theorem.md`. The lower
bounds are the singleton-cut dual and a second explicit dual supported on
\(\{b_i\},\{x_i\},\{b_i,x_i\}\). For \(m\ge4\), an orbit-constant primal
weighting is verified for every cut by a symbolic two-case argument. Explicit
Hamiltonian cycles settle \(m=2,3\).

The requested boundary LPs are therefore exactly
\(\operatorname{OPT}_{5,1}=25/2>12\) and
\(\operatorname{OPT}_{6,1}=15>14\). In particular, \(J_{5,1}\) disproves the
natural sharpness guess for the known sufficient boundary \(m\ge2\ell+4\),
already at \(m=2\ell+3\).

## Reproducible evidence and limits

`evidence/cut_lp_certify.py` checks compact rational data in
`evidence/J_m_1_certificates.json` using exact `Fraction` arithmetic. Its
captured output `evidence/J_m_1_verification.json` exhausts all 2047 distinct
cuts of \(J_{5,1}\), all 8191 of \(J_{6,1}\), and all cuts for \(m=2,3,4\),
while also checking the matching dual constraints and objectives. The symbolic
proof, rather than finite extrapolation, establishes all \(m\ge4\).

The original all-\((m,\ell)\) problem remains unresolved. The prior literature
screen in `problem.md` found no inspected primary source with this
classification; that limited search is not a priority or novelty proof.

## Next test

Compute and rationally certify the symmetry-reduced and complete cut LPs for
\(J_{6,2},J_{7,2},J_{8,2}\). These are respectively \(m=2\ell+2\),
\(2\ell+3\), and the known-negative boundary \(2\ell+4\); they directly test
the named candidate threshold “non-FH iff \(m\ge2\ell+3\)” suggested by the
new \(\ell=1\) theorem before attempting an all-parameter symbolic formula.
