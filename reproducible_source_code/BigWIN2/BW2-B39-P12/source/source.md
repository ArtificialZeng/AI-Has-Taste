# A proper Euler magic matrix of order seven

Decide whether there are an integer matrix M=(m_ij) in Z^(7 by 7) and a
nonzero integer gamma such that

\[
MM^{\mathsf T}=\gamma I_7,
\qquad \sum_{i=1}^7m_{ii}^2=\gamma,
\qquad \sum_{i=1}^7m_{i,8-i}^2=\gamma,
\]

and the 49 absolute values |m_ij| are pairwise distinct.

An existence proof is a single explicit matrix together with exact integer
verification of all three identities and distinctness.  A nonexistence proof
must cover every rational matrix satisfying the identities, since clearing
denominators preserves properness and gives the equivalent integer problem.
Near-miss matrices are evidence only and do not resolve the statement.

Primary source: S. D. Kominers, *A proper Euler magic matrix of order 5*,
arXiv:2607.19416v1, Definition 1.1 and Section 5.  Inspected 2026-09-06.  The
paper constructs order 5, states that proper odd orders beyond 5 remain open,
and identifies the three mirror-coordinate pairs for order 7.

Provenance: `batches/inbox/bigWin-39.raw.md`, item DW39-12.
