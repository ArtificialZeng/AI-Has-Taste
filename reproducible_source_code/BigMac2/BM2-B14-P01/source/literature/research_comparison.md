# Bounded primary-literature comparison

Checked 2026-09-08 by research job
`bigMac-00014-p01-research-09c4ecbfdfab`. This is a search and attribution
record, not a mathematical referee report or proof of priority.

## Primary sources inspected and precise boundaries

1. Yukun He and Jiaoyang Huang, *The oriented Kesten--McKay law for random
   regular digraphs*, arXiv:2609.05297v1, submitted 2026-09-04.
   [Version record](https://arxiv.org/abs/2609.05297v1);
   [primary PDF](https://arxiv.org/pdf/2609.05297v1).
   The web reader exposed the 44-page paper. The model definition is on
   one-based PDF page 6 (web page index 5): it expressly distinguishes
   the loops-allowed binary model from the zero-diagonal model.
   Lemma 6.2 and the uniformity portion of its proof are on one-based PDF
   page 36 (index 35). The proof counts 2^c ordered matching decompositions
   and compensates by weight 2^(-c). This is exactly the representation
   reproduced in Section 1 of `evidence/proof.md`; it is not new here.
   The checked lemma/proof and model definition do not state the requested
   unshifted determinant probability or its coefficient asymptotic.
   The model's source page numbers in immutable `source.md` are off by one;
   this note corrects navigation only, without changing that source.

2. Chi-Kwong Li, Julia Shih-Jung Lin, and Leiba Rodman, *Determinants of
   Certain Classes of Zero-One Matrices with Equal Line Sums*,
   Rocky Mountain Journal of Mathematics 29 (1999), 1363--1385.
   [Author-hosted primary preprint](https://cklixx.people.wm.edu/llr.pdf);
   [author's publication record](https://people.wm.edu/~cklixx/ilasreu.htm).
   The 18-page preprint was read at Section 3, Theorem 3.1 and its proof
   (PDF pages 5--6). It explicitly reduces matrices with line sums two
   to relative permutation cycles, gives determinant zero for an even
   cycle and magnitude two for an odd cycle, and classifies all possible
   absolute determinant values. It also records the exceptional singular
   case (n,k)=(4,2), and general existence statements in Section 2.
   Therefore our cycle criterion, determinant magnitudes, and exceptional
   existence cases are known facts. The checked material classifies values
   rather than their multiplicities under the uniform matrix law. Searches
   for probability and number-of-matrices terminology did not identify
   the coefficient ratio or the two-singularity probability expansion.

3. David J. Houck and Michael E. Paul, *Non-singular 0-1 matrices with
   constant row and column sums*, Linear Algebra and its Applications
   22 (1978), 263--266, DOI 10.1016/0024-3795(78)90076-9.
   [Publisher record](https://www.sciencedirect.com/science/article/pii/0024379578900769).
   The indexed publisher abstract states a construction for 0<k<n apart
   from (k,n)=(2,4). This corroborates that existence is old. Only publisher
   metadata and abstract were available in this pass; the direct page
   open failed. No assertion is made about the uninspected full text.

4. Philippe Flajolet and Andrew Odlyzko, *Singularity Analysis of Generating
   Functions*, SIAM Journal on Discrete Mathematics 3(2) (1990), 216--240,
   DOI 10.1137/0403019.
   [Author-hosted primary paper](https://algo.inria.fr/flajolet/Publications/FlOd90b.pdf).
   Its introduction describes extension to finitely many dominant
   singularities. Section 5.1 (printed page 234) states the classical
   Fourier/Darboux smooth-remainder coefficient principle. Our proof
   supplies the elementary integration-by-parts argument and checks the
   specific fractional powers, so this is methodological attribution,
   not an appeal to an unspecified analytic transfer.

## Searched scope and contribution assessment

Search queries included combinations of binary matrices, two ones in each
row and column, nonsingular probability, 2-regular bipartite matrices,
Ewens invertibility, degree-two singularity, and exact Gamma(1/4)
constants. Targeted title searches led from the determinant-classification
paper to its author-hosted version. General fixed-degree invertibility
literature, including arXiv:1806.01382, was also screened; it did not
supply the requested degree-two coefficient formula in the inspected
introductory results. Searches are discovery tools, not evidence that an
unreturned result does not exist.

The proposed contribution for fresh review is the exact all-N probability
in this particular uniform loops-allowed model, including the exact
leading constant, the parity term from -1, and the cancellation of the
ordinary first correction. It combines the known representation and
known determinant criterion with an explicit counting and asymptotic
calculation. No equivalent probability/asymptotic result was found in
the checked portions of these primary sources on this date. This is
not a claim of first discovery, nor a claim that a famous open problem
has been settled. The referee should assess whether the explicit
probability and remainder constitute sufficient mathematical value.

Unsearched regions include non-English combinatorial enumeration sources,
older tables of regular-matrix counts, full citation trees, and possible
equivalent formulas phrased solely as weighted restricted permutations.
The probability might be an unstated consequence of older enumerative
results; the current pass does not exclude that possibility.

## Access and supplied-bibliography limitations

The local primary PDF path from `source.md` is absent. A direct `curl`
download failed with DNS resolution error; the arXiv web text reader
worked, while its screenshot endpoint returned an internal error. No
local PDF is represented as downloaded. These are operational facts,
not mathematical evidence. All needed mathematics is reproduced in
`evidence/proof.md`.

`literature/user_bibliography_check.md` supplies a separate workbook-based
record for Zijian Zeng, *The Distinct-Cycle-Length Probability is Strictly
Decreasing after 30*, DOI 10.2139/ssrn.7380519. That supplied record has
been preserved. Its allowed role is comparison with permutation-cycle
probabilities; it is not used to establish the present representation,
determinant criterion, asymptotic, or novelty. This pass did not refresh
that metadata or inspect its full text and does not call it nonexistent.
