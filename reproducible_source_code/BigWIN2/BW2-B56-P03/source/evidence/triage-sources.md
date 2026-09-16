# Triage literature record

Retrieval date: 2026-09-07.

## Primary conjecture and the length-15 candidate

Fatemeh Rezaee, *Conjectural Criteria for the Most Singular Points of the
Hilbert Schemes of Points*, Experimental Mathematics 34 (2025), no. 4,
668--683, DOI 10.1080/10586458.2024.2400181.

- Authoritative repository PDF:
  https://api.repository.cam.ac.uk/server/api/core/bitstreams/dc53dacc-fca2-40af-af4b-82cefc4ff37e/content
- Conjecture B: printed pp. 5--6.
- Conjecture F and its tangent formula: printed p. 9.
- Table entry for colength 15 and \(I_*\): printed p. 10.
- Inspected content: the paper describes its sufficient conditions and
  explicit non-tetrahedral families as conjectural. For \(j=1\), Conjecture F
  specializes to
  \(I_*=(x^3,y^3,z^6,x^2y,x^2z,xy^2,xyz,y^2z,xz^3,yz^3)\), of colength 15.
  Its displayed formula yields
  \(3\cdot15+(T(\mathfrak m^3)-3\cdot10)+6=45+(60-30)+6=81\).

## Exact computational table by the smallest pure exponent

Alexia Ascott, Fatemeh Rezaee, and Zhichen Zhou, *A monotonicity conjecture
for the local maximal singularity of the Hilbert scheme of points*,
arXiv:2506.17704v2 (7 Feb 2026).

- Abstract page: https://arxiv.org/abs/2506.17704
- PDF: https://arxiv.org/pdf/2506.17704
- Definition 0.1 and Conjecture C: printed pp. 2--3.
- Exact table and Macaulay2 snippet: printed p. 4.
- Inspected content: the text gives \(T_{\max,1}(l)=3l\), and the table
  explicitly reports, for \(l=15,k=3\), \(T_{\max,2}=69\) and
  \(T_{\max,3}=81\). Thus the three length-15 values are \(45,69,81\).
  The authors state that the table
  confirms their monotonicity conjecture for \(N=3\), \(10\le l\le35\).
  Appendix A says the method lists strongly stable ideals and computes
  `degree Hom(I,(ring I)/I)`, but only prints an illustrative length-35,
  fixed-generator-count call rather than a full length-15 transcript or
  maximizer list.

## Nearest theorem and the uncovered degree

Fatemeh Rezaee and Parsa Saberi, *An obstruction to the maximal singularity
of the Hilbert scheme of points on threefolds*, arXiv:2609.04054v1
(3 Sep 2026).

- Abstract page: https://arxiv.org/abs/2609.04054
- PDF: https://arxiv.org/pdf/2609.04054
- Conjecture B and degree families (0.1)--(0.3): printed p. 2.
- Theorem B: printed pp. 2--3; Theorem 5.1: printed p. 17.
- Inspected content: for \(k=3\), family (0.1) is \(10,11,12,13\), family
  (0.2) is \(16,17,18,19\), and family (0.3) is \(10,14,17,19\) after
  removing duplicates. Therefore 15 is the only integer in
  \(10\le l<20\) not covered by Theorem B.

## Search boundary

Searches used the exact assertion, the candidate generators, “colength 15,”
“maximum dimension tangent space,” and the terminology
\(T_{\max,m_1}(l)\). No primary source found in this bounded search supplied a
complete length-15 atlas and all equality cases. This is not a claim of
priority or proof that no such source exists.
