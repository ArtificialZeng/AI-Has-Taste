# King on equal odd-block generalized staircases

Primary original: Eric Gottlieb, Matjaž Krnc and Peter Muršič, *Impartial Chess on Integer Partitions*, arXiv:2501.14640v1 (24 January 2025), Conjecture 5.1, with Definitions 2.1 and 3.1.
https://arxiv.org/html/2501.14640v1

This is a mathematical transcription of that conjecture, not a generated browser batch. The original HTML is preserved without alteration at evidence/external/gkm-2501.14640v1.html (SHA256 4900645fdd94cec1863cc0adfac823a58921b28c6956e57963d9ea1737538ba4). The source's staircase pictogram is written D below solely for legibility.

For a nonempty integer partition lambda, lambda[i,j] deletes its first i rows and its first j columns, omitting nonpositive remaining parts. Legal King moves replace lambda by a NONEMPTY lambda[i,j], for (i,j) in {(0,1),(1,0),(1,1)}. These are unit moves, not arbitrary-length Queen moves. Normal-play Sprague-Grundy values are the mex of legal successor values; a position with no legal move has value zero.

Let D^k_{r,c} be the partition consisting of r copies of kc, then r copies of (k-1)c, ..., then r copies of c, for positive integers r,c,k.

Conjecture 5.1: for every odd positive integer r and every positive integer k, writing q=k mod (r+2) with 0<=q<r+2,
G_King(D^k_{r,r}) = 0 when q is odd;
G_King(D^k_{r,r}) = 1 when q is even and nonzero;
G_King(D^k_{r,r}) = 2 when q=0.

Task: prove or disprove exactly this universal formula. A result restricted to r=1, to finitely many r or k, or to the adjacent unequal-even-block Conjecture 5.2 does not resolve this original.

Source status at intake (13 September 2026): v1 explicitly labels this Conjecture 5.1. The inspected arXiv history has only v1. A later author-posted SSRN record https://ssrn.com/abstract=5649443 (31 pages, posted 23 October 2025) was found, but its full text has NOT been compared. Accordingly current openness and novelty remain qualified, not certified. See literature/outer-intake-screen.md for search coverage, exact finite calibration and semantic-neighbor comparison.
