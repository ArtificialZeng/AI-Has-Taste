# Search log

## NOVELTY_LOCK — 2026-08-29 (Asia/Shanghai)

Claims C01--C12 were frozen in `claim_ledger.md` before running any new large
candidate search.  Initial web queries (2026-08-29) were:

- `Erdos problem 647 tau(n) n+d(n) 24`
- `site:erdosproblems.com 647 divisor function tau`
- `"max" "m+d(m)" "n+2" divisors`
- `OEIS n + number of divisors record`

Initial hits requiring primary-source verification:

- Erdős Problems #647 (page says open; last edited 2026-04-07; lists original
  references and OEIS A062249/A087280).
- I. Mian and S. Siddique, *A Kernel-Checked Exclusion Certificate for Erdős
  Problem 647*, arXiv:2608.17880 (submitted 2026-08-18).
- Repository/artifact links associated with finite and claimed global
  domination certificates.
- Erdős Problems discussion thread recording a challenged January 2026 global
  claim.

## Primary-source checks — 2026-08-29

- Paul Erdős, “Some Unconventional Problems in Number Theory,” *Mathematics
  Magazine* 52(2) (1979), 67--70, DOI 10.1080/0025570X.1979.11976756.
  Inspected the original scan at p. 68 (Problem 4), SHA-256
  `772e2f84dff324b363dc6fbb74a9449f36c42569027b29efb3b71af84ff18964`.
  It attributes the investigation to Erdős and Selfridge, records \(n=24\),
  expresses extreme doubt about infinitely many solutions, and suggests the
  prefix gap may tend to infinity.
- Paul Erdős, “Some Unconventional Problems in Number Theory,” *Acta
  Mathematica Academiae Scientiarum Hungaricae* 33 (1979), 71--80, DOI
  10.1007/BF01903382.  Inspected the original passage at p. 72: it states the
  fixed-window conjecture and that Schinzel's Hypothesis H would imply it.
- I. Mian and S. Siddique, arXiv:2608.17880v1 (submitted 2026-08-18).
  Inspected PDF SHA-256
  `ac5b24d675ac9cee85ccbfaeeae39fa7313fbf58db3304cbad9c174e1667ea49`.
  Exact endpoint: kernel-checked exclusion \(24<n\le10^9\); separately labels
  \(10^{12}\) and \(9.17\times10^{18}\) as cited computations outside the
  proof kernel.
- Patrik Idén, Zenodo 10.5281/zenodo.21084248 (record date 2026-06-30).
  API metadata and file checksums inspected; it reports the direct sieve to
  \(10^{12}\).  This project did not rerun that full scan.
- OEIS A087280 (last modified 2026-08-25) defines the equality solutions and
  lists \(5,8,10,12,24\), with no further terms through \(10^{12}\).  OEIS
  A062249 (last modified 2026-08-28) defines \(n+\tau(n)\).
- `bentrd/erdos647-frontier-extension`, commit
  `f727ab831abd533d36260f36f0b3433d8db0715e`: inspected scanner source, pair
  list, both 15,140-line full-run logs, validation slices, and exact depth
  exceptions.  The repository reports the prior endpoint
  \(9{,}174{,}471{,}185{,}880{,}000{,}000\).  The complete prior scan was not
  rerun locally; this limitation remains explicit.
- `scottdhughes/erdos647-proof-chain`: inspected the reduction theorem surface,
  axiom boundary, 41-residue set, 6,549 universal closures, and finite-prefix
  package.  Its dependency-free frontier verifier passed 30/30 local checks,
  including partition reconstruction and exact closure arithmetic.

## First-pass later-work queries

- `"Erdős Problem 647" August 2026 solution`
- `"Erdos problem 647" after:2026-08-18`
- `site:arxiv.org "Problem 647" divisor August 2026`
- `site:doi.org "Erdős problem 647"`

The only mathematical paper found after the prior computational artifacts was
arXiv:2608.17880v1, which explicitly says the global problem remains open.  A
second, result-specific pass is required before release.

## Result-specific second pass — 2026-08-29

After the exact endpoint was known, the following additional queries were run:

- `"9,180,628,549,092,000,000" Erdős 647`
- `"9180628549092000000" divisor`
- `"Erdős Problem 647" "9.18"`
- `"Erdos 647" "149100000"`
- `Erdős problem 647 new bound divisor record August 29 2026`
- `Erdos problem 647 solved divisor function 2026`
- `site:arxiv.org/abs/2608 "Erdős problem 647"`
- `site:oeis.org/A087280 Erdős 647 10^18`

No source was found stating the exact new endpoint or a larger one.  The current
Erdős Problems discussion, MathDB status, OEIS A087280, and arXiv search still
lead to the same frontier literature and explicitly describe the global problem
as open.  Therefore the novelty claim is deliberately bounded: “not found in
the recorded sources and queries through 2026-08-29,” not “certainly never
obtained elsewhere.”

## Release-time second pass — 2026-08-29

Immediately before the release audit, the exact decimal endpoints and the
problem name were searched again with these queries:

- `"9,180,628,549,092,000,000" "Erdős"`
- `"9180628549092000000" divisor tau`
- `"Erdős Problem 647" computational frontier`
- `site:arxiv.org "Erdős Problem 647"`
- `"9,174,471,185,880,000,000" "Erdős 647"`
- `"9174471185880000000" Erdős`
- `"149100000" "erdos647"`
- `site:github.com erdos647 frontier extension 2026`

The exact new endpoint again produced no mathematical source.  The maintained
[Erdős Problems page](https://www.erdosproblems.com/647),
[arXiv:2608.17880](https://arxiv.org/abs/2608.17880),
[OEIS A087280](https://oeis.org/A087280), and
[MathDB record](https://mathdb.com/p/383289/erdos-problem-647) continued to
describe the global problem as open.  The exact fixed commit of the public
[frontier-extension artifact](https://github.com/bentrd/erdos647-frontier-extension/tree/f727ab831abd533d36260f36f0b3433d8db0715e)
still reports the previous endpoint
\(9{,}174{,}471{,}185{,}880{,}000{,}000\).  No exact or larger bound was found
in these listed sources and queries through 2026-08-29.  This is the complete
release-time scope of C12; it is not a universal statement about unpublished
work.
