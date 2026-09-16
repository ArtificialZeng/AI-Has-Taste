# Root proof audit

The finite-sums definition was reconstructed with four distinct positive
generators and with collisions among subset sums deduplicated.  Positivity
makes eligibility equivalent to the generator sum being at most 201.

On 2026-09-01 both supplied verifiers were executed afresh.  The first uses
`itertools.combinations` for generators and every nonempty subcombination for
the edge; the second uses four explicit ordered loops and iterative sumset
expansion.  Both parsed the same 201-bit word, independently traversed all
2,587,336 eligible generator sets, and returned `PASS`.  They agreed on the
complete edge-size histogram:

`10:20, 11:1585, 12:2952, 13:151189, 14:61964, 15:2369626`.

Every eligible finite-sums edge therefore meets both colour classes.  The
displayed word properly two-colours `H(201,4)`, proving `F(4) >= 202` and
disproving `F(4)=201`.  It does not prove equality at 202.  No proof assistant
was used; the finite result remains subject to ordinary external peer review.
