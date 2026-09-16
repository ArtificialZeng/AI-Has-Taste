# Final independent proof and statement audit

Audit date: 2026-08-31  
Audited source: `paper/main.tex`, current lines 1--175  

## Verdict: **PASS**

The mathematical proof, scope, authorship information, and manuscript-content constraints all pass. The previous proof gaps and policy issue have been repaired.

## Mathematical proof: PASS

- **Lines 46--50:** the theorem correctly quantifies over every characteristic-zero field and every finite simple graph on eight vertices.
- **Lines 58--91:** the algebra, monomial basis, Hilbert formula, multiplication incidence matrix, and reduction to the variable sum \(L\) are correct.
- **Lines 99--100:** Holleben--Nicklasson Corollary 3.12 correctly covers \(\alpha\ge5\), since \(8/3+2=14/3\).
- **Lines 102--111:** Theorem 3.10 is now explicitly cited and correctly gives non-surjectivity of \(M_5:A_5\to A_6\) for an independent four-set. The formula
  \[
  h_6-h_5=-140-5i_2+2i_4
  \]
  remains correct. The bounds \(i_2\ge6\) and \(i_4\le70\) imply \(h_6-h_5\le-30\), so non-surjectivity contradicts maximal rank.
- **Lines 114--117:** the formerly omitted strict-positivity reason is now present: an independent triple gives \(i_2\ge3\), \(i_3\ge1\), hence \(h_5-h_4=5i_2+5i_3-14\ge6>0\).
- **Lines 138--149:** every \(\alpha=3\) class is assigned a nonzero exact integer right-kernel vector for \(M_4\). The independent certificate audit verified all 6,021 records exactly.
- **Lines 159--165:** the conclusion correctly covers labelled graphs by relabelling and every characteristic-zero field by scalar extension/rational-minor invariance.
- The strata \(\alpha=3\), \(\alpha=4\), and \(\alpha\ge5\) exhaust the hypothesis. No rank direction, endpoint, or equality case is missing.

## Scope, authorship, and overclaim: PASS

- **Lines 18--26, 41--55, 159--172:** the claims are bounded to the eight-vertex characteristic-zero result. The paper does not claim the full conjecture or positive characteristic.
- **Lines 12--14:** the author, affiliation, and both email addresses exactly match the required information.
- The previous forbidden wording about commands, software versions, checksums, run logs, and unused proof assistants has been removed from lines 168--172.
- **Lines 171--172:** “the supplementary archive distributed with this article” is an adequate named supplement locator for a submission package, assuming that archive is actually included in the ZIP/submission.

## Final policy check: PASS

The former internal workflow paragraph has been removed. No model/vendor description, prompt text, checksum, proof-assistant workflow statement, or comparable internal pipeline trace remains in the manuscript body. No proof or release blocker remains in this audit.
