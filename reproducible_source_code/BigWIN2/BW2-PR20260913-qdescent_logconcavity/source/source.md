# Gaetz–Gao q-descent coefficient log-concavity
Primary: Christian Gaetz and Yibo Gao, On q-analogs of descent and peak polynomials, arXiv:1912.04933v2 (8 January2020), §1.2 and §2, Theorem5, Theorem6, Conjecture7 and following Remark; European Journal of Combinatorics97(2021),103397, DOI10.1016/j.ejc.2021.103397.
https://arxiv.org/html/1912.04933v2
Raw original HTML is preserved at evidence/external/gaetz-gao-1912.04933v2.html, SHA256 aac7bacf054929a792ad5cf9422c2902249bb636eec8fdc6ab11a6957fa7d6aa. The HTML rendering's dynamic Date is not its submission/version date.

Conjecture7's original sentence, formula rendered in plain text:
“The coefficients (a_k(S;q))_{k>=1} (defined in Theorem5) form a strongly q-log concave sequence.”

Precise transcription of the definitions:
S is a finite nonempty subset of positive integers, m=max(S). Des(pi)={i:pi_i>pi_(i+1)}; inv(pi)=#{i<j:pi_i>pi_j}.
For1<=k<=m,
a_k(S;q)=sum q^inv(pi),
where the sum runs over pi in Sym(m+k) with Des(pi)=S and {m+1,...,m+k} contained in {pi_1,...,pi_m}. Set a_0=a_(m+1)=0.
The literal printed §1.2 condition is no internal zero polynomials and
a_i(S;q)*a_j(S;q)-a_(i-1)(S;q)*a_(j+1)(S;q) in Z_{>=0}[q]
for every1<=i<j<=m, for every such S.

Important source ambiguity: the printed definition says i<j, but nearby discussion treats diagonal i=j inequalities as part of strong q-log-concavity. Preserve this discrepancy. The frozen literal original target above uses i<j. Test/report the conventional strengthened target i<=j separately. A diagonal-only failure does not refute the frozen literal target. A proof including the diagonal is a disclosed stronger result, not a silent change of original. Do not manufacture a counterexample from the source's wording alone.

This is primary-literature fallback, not a browser-generated batch. Source v2 and the publisher excerpt explicitly retain Conjecture7. Bounded follow-up searches on13September2026 found no inspected primary resolution; this does not certify global priority/current openness. Full designated-conversation history is unavailable. See literature/outer-intake-screen.md.
