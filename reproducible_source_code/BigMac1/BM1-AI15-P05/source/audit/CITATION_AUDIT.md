# Citation audit

Audit date: 2026-08-29.  Status: **PASS**.

The audit was performed serially because the active execution policy did not
authorize sub-agent delegation.  Every citation key in the manuscript was
checked against the source named below; no key migration was required.

| Key | Verification source | Result |
|---|---|---|
| `Erdos1979Magazine` | Crossref DOI `10.1080/0025570X.1979.11976756` and original scan, Problem 4, p. 68 | title, journal, volume, issue, pages, year, and historical claim verified |
| `Erdos1979Acta` | Crossref DOI `10.1007/BF01903382` and original scan, p. 72 | title, journal, volume, issue, pages, year, and Hypothesis H context verified |
| `Bloom2026` | [Erdős Problems #647](https://www.erdosproblems.com/647) | problem statement, open status, and attribution verified |
| `Iden2026` | [Zenodo DOI 10.5281/zenodo.21084248](https://doi.org/10.5281/zenodo.21084248) | creator, title, date, and reported \(10^{12}\) computation verified |
| `MianSiddique2026` | [arXiv:2608.17880v1](https://arxiv.org/abs/2608.17880) | authors, title, date, subject, DOI, and \(10^9\) theorem scope verified |
| `Hughes2026` | repository CFF/release and [fixed commit](https://github.com/scottdhughes/erdos647-proof-chain/tree/be657cf1b89aebb98bbb8117f29c0456a8435ac6) | author, title, version, commit, and imported theorem surface verified |
| `Tordjman2026` | repository CFF/release and [fixed commit](https://github.com/bentrd/erdos647-frontier-extension/tree/f727ab831abd533d36260f36f0b3433d8db0715e) | author, title, version, commit, and prior endpoint claim verified |

Claim-to-source checks passed: the two Erdős articles support only historical
statements; the maintained database supports current open status; the finite
computations are not cited as global proofs; Hughes supports only the modular
prerequisite; Tordjman supports only the inherited reported prefix.

The final `.aux`/bibliography key checker and the clean-build undefined-citation
scan are recorded with the release build.  The bibliography has no missing or
duplicate keys, and every bibliography entry is cited in the text.
