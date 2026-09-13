# bigMac-00014-p01 — Exact invertibility probability in `M_(N,2)`

## Immutable source statement

For each integer `N>=2`, let

`M_(N,2)={A in {0,1}^{N x N}: A 1=2 1 and A^T 1=2 1}`

and let `A_N` be uniform on this finite set. Determine the exact probability
that `det(A_N) != 0` and its complete first-order asymptotic as `N→infinity`.

The proposed route must prove, not assume, the coefficient identity obtained
from Lemma 6.2's representation `A=P(I+Q)`, with `Q~Ewens_N(1/2)` conditioned
to have no fixed points. It must check that invertibility is equivalent to every
cycle of `Q` having odd length, account for all small `N` and any contribution
from the second singularity at `z=-1`, and give the leading constant exactly.

## Primary boundary

He and Huang, *The Oriented Kesten--McKay Law for Random Regular Digraphs*,
arXiv:2609.05297v1, model definition p. 5 and Lemma 6.2 pp. 35--36.

Primary PDF: `batches/literature/bigMac-14/2609.05297v1.pdf`.

The source proves a global limiting spectral law and the Ewens representation;
it does not state the requested exact unshifted determinant probability in the
portion checked at intake. The loops-allowed model is intentional. No claim is
made here for the zero-diagonal model `M^0_(N,2)`.

## Permitted contribution boundary

An exact all-`N` coefficient formula plus a rigorously derived asymptotic with
constant, or an exact counterexample to the proposed cycle reduction. A weak
spectral limit or numerical frequencies are not a proof of invertibility.

