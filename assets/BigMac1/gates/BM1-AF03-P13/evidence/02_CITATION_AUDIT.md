# Citation audit — pass 2

Audit date: 2026-08-29 (Asia/Shanghai).  Scope: every cited or externally
checkable claim frozen in `citation_claims_pass1.md`.  Primary sources were
preferred; search-engine results and secondary databases were used only to
locate them.

## Bibliographic identity

| Key | Identity check | Primary evidence | Verdict |
|---|---|---|---|
| `LeeVindasWang2026` | Eon Lee; Andrés R. Vindas-Meléndez; Zhi Wang; exact title; *Discrete Mathematics* 349(9), Paper 115072 (2026); DOI `10.1016/j.disc.2026.115072`; arXiv `2411.18695` | [publisher record](https://www.sciencedirect.com/science/article/pii/S0012365X26000968), [arXiv v2](https://arxiv.org/abs/2411.18695), [repository record](https://escholarship.org/uc/item/6n85w7mx), local Crossref response | PASS |
| `BraunJal2026` | Benjamin Braun; Aryaman Jal; exact title; arXiv `2607.00922v1` (2026); arXiv DOI `10.48550/arXiv.2607.00922` | [arXiv record](https://arxiv.org/abs/2607.00922), [arXiv v1 full text](https://arxiv.org/html/2607.00922v1) | PASS |
| `Stanley1986` | Richard P. Stanley; “Two poset polytopes”; *Discrete & Computational Geometry* 1 (1986), 9--23; DOI `10.1007/BF02187680` | [author-hosted article PDF](https://math.mit.edu/~rstan/pubs/pubfiles/66.pdf), [author publication list](https://klein.mit.edu/~rstan/pubs/index.html) | PASS |

The required author-title, exact-title/Semantic-Scholar, author-venue-year,
and DOI/arXiv query families were run for each item.  Semantic Scholar did not
return a useful exact-title page for every item; this does not weaken the
primary DOI/arXiv/full-text matches.

## Claim-by-claim verification

| Pass-1 claim | Evidence comparison | Verdict |
|---:|---|---|
| 1 | The original abstract and introduction explicitly say the paper studies Ehrhart theory/lattice-point enumeration of order polytopes of generalized snake posets. | PASS |
| 2 | arXiv v2, Conjecture 5.1, items (1) and (2), contains exactly the (h^*)-root and Ehrhart-disk assertions. | PASS |
| 3 | arXiv v2 Definition 2.1 says length (n), the number of (L/R) letters; Conjecture 5.1 says length (n+1). | PASS |
| 4 | Conjecture 5.1(2) prints `|z-(n+4)/2|` and in the same sentence prints axis `x=(-n-4)/2`. | PASS |
| 5 | arXiv v2 Theorem 2.9 gives both ((t+1)\cdots(t+n+3)\mid L) and (L(t)=L(-n-4-t)). | PASS |
| 6 | The sentence immediately after Conjecture 5.1 says it was verified for snake words of length up to 9. | PASS as an author report only; it is not accepted as a proved baseline |
| 7 | Braun--Jal Section 4 says it proves Lee et al. Conjecture 5.1(1), and Theorem 4.1 proves real-rootedness/interlacing.  No disk theorem or Conjecture 5.1(2) treatment occurs. | PASS |
| 8 | Stanley's article supplies the canonical triangulation by linear extensions.  Braun--Jal Theorem 2.1, explicitly attributed to Stanley, states (h^*(\mathcal O(P);t)=W_P(t)) for a naturally labelled finite poset. | PASS |
| 9 | Lee--Vindas-Meléndez--Wang Theorem 4.8 states \(h^*(\mathbf w;z)=\sum_iD(n-i,i)z^i\) for a regular word of actual length \(n-1\). Substitution \(n=11\) and \(n=10\) matches the manuscript's two cross-checks. | PASS |
| 10 | Both downloaded arXiv source archives contain TeX/bibliography/figures but no Sage program, repository, or certificate; the public article record says data are available on request. | PASS within the inspected public artifacts |
| 11 | The pre-result and fingerprint searches in `search_log.md` plus the isolated referee search in `referee_search_raw.md` found no prior resolution. | PASS only as the stated bounded not-found report |
| 12 | arXiv v2 full text still contains Section 5 and the defective formula; the publisher/repository records expose the same article/version. | PASS |
| 13 | New exact calculations were routed to proof/certificate audit rather than attributed to literature. | PASS |

## Placement, direction, and completeness

- Every cited sentence in `paper/main.tex` is supported by the cited item and
  the citation appears immediately after the relevant claim.
- No citation is reversed: Braun--Jal is cited only for the solved (h^*)
  half, not for the Ehrhart disk.
- The author's length-9 statement is described as a report, not upgraded to a
  theorem.
- The negative novelty and code claims explicitly retain their search
  boundaries.
- The paper's new counterexample, Rouché, and Routh claims cite certificates
  and verifiers rather than unrelated external literature.

## Final citation verdict

`CITATION_AUDIT = PASS`.  Citation count: 3 unique bibliography entries; 3/3
existence and metadata verified; all 13 frozen claims classified; no unsupported
external factual claim requiring manuscript correction remains.

Post-edit check: the final clean build retained the same three cited works and
the same citation directions.  The added exact-scan paragraph refers only to
serialized project evidence and introduces no new external citation claim.
