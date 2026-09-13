# Citation audit

Audit date: 2026-08-29 (Asia/Shanghai)

## Result

**PASS: five cited records were individually checked against primary
publisher, DOI, MathNet, or arXiv records.**  Every citation key in
`paper/main.tex` exists exactly once in `paper/references.bib`; every BibTeX
entry is cited; no key was changed after insertion.  Claim support and
metadata were checked separately rather than inferred from key existence.

| Key | Nearby manuscript claim | Primary verification | Metadata/action | Residual uncertainty |
|---|---|---|---|---|
| `HaymanLingham2019` | Problem 4.24 asks for the coefficient-sized image disk and attributes it to Sheil--Small. | Springer chapter DOI `10.1007/978-3-030-25165-9_4`; accessible source arXiv:1809.07200v2, Problem/Update 4.24. | Chapter title, authors, year, book, and pp. 81--95 verified; chapter record used. | The accessible text literally prints \(1/\zeta\), not \(1/\bar\zeta\); the manuscript discloses this. |
| `ClunieHayman1974` | Provenance to the Canterbury problem collection. | Cambridge book DOI `10.1017/CBO9780511662263`; chapter DOI `10.1017/CBO9780511662263.034`. | Clunie and Hayman correctly recorded as editors, not chapter authors. | Paywalled chapter wording was not inspected; the provenance mapping comes from the Hayman--Lingham source table. |
| `LalinSmyth2013` | Standard coefficient definition of self-inversive. | Springer DOI `10.1007/s10474-012-0225-4`; arXiv:1201.0774v1, §1 and equation (1). | Author accent, 2013 journal year, volume 138, combined issue 1--2, pp. 85--101 verified. | The source states the functional/coefficient form, not the zero-multiset wording; the manuscript labels the equivalence elementary. |
| `Solyanik2014` | Binomially weighted covering theorem; endpoint-max branch. | arXiv:1410.6772, Lemma 3 and Corollary 1, pp. 2--3. | Official arXiv metadata used; it is described as a preprint, with no journal/DOI claim. | No journal publication was located. |
| `Dubinin2012` | Broader survey of polynomial covering theorems. | MathNet record and DOI `10.1070/RM2012v067n04ABEH004803`; §2.2, pp. 627--632. | English journal volume/issue/pages and DOI kept separate from the Russian original. | It does not support Solyanik's exact weighted bound; manuscript wording was repaired to cite it only as a broader survey. |

Official URLs:

- `https://doi.org/10.1007/978-3-030-25165-9_4`
- `https://doi.org/10.1017/CBO9780511662263`
- `https://doi.org/10.1007/s10474-012-0225-4`
- `https://arxiv.org/abs/1410.6772`
- `https://doi.org/10.1070/RM2012v067n04ABEH004803`

The 1974 page discrepancy is documented rather than harmonized silently:
the Hayman--Lingham source table lists a wider source interval 143--180,
while Cambridge identifies the chapter `New problems` as pp. 155--180.

## Mechanical checks

Before building, the skill checker reported:

```text
cited_keys: 5
bib_keys: 5
cited_keys_missing_from_bib: 0
bib_keys_not_cited: 0
```

Command:

```bash
python3 /Users/mac/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py paper/main.tex
```

After the converged clean build, the checker additionally reported five
`.aux` bibliography keys with no missing or extra key.  The final `main.log`
and `main.blg` contain no undefined citation/reference, missing database
entry, duplicate entry, BibTeX warning, or LaTeX error.  The exact converged
scan was:

~~~bash
rg -n "Citation .* undefined|There were undefined|I didn't find a database entry|Warning--|Repeated entry|LaTeX Warning|Package .* Warning|LaTeX Error|Fatal error|Emergency stop|Undefined control sequence|Runaway argument|Overfull|Underfull" \
  tmp/pdfs/build/main.log tmp/pdfs/build/main.blg
~~~

It returned no matches.
