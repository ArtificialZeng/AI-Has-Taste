# v10 builder report: X16 endpoint and packaged-referee portability

Date: 2026-08-24. Status: **builder candidate only**. This package is
pending a fresh independent v10 final manuscript/archive audit and must not
be called submission-ready.

## Scope

The mathematical change is restricted to the same five-real-parameter
positive-`Z` moving sheet. The exact final closed cell is

```text
1/17 <= X <= 1/16,
0 < S <= 1/10000,
|M| <= 1/1000,
|omega|,|nu| <= 1/100.
```

It extends the displayed moving-sheet theorem only from `X<=1/17` to
`X<=1/16`. It does not prove the full compact-ball quartic, the general
complex Hermitian gate, a common metric for arbitrary data, a fixed-lens or
all-node theorem, or any optimal crossing-lens constant. No Lean result is
claimed for X16.

The final cell crosses the old descriptive locator `Z=1/6`. The source and
referee both reconstruct the actual lossless hypotheses:

```text
0<S<=1, lambda>0, Z>0, x^2+y^2+Z<1.
```

No inverse, rank, gate, or denominator-clearing identity requires `Z<1/6`.
The exact common strict continuum reserve is

```text
141635970781970514779535557286727779805714617592267929266532825868383583
/70448201072640000000000000000000000000000000000000000000000 > 0.
```

The other v10 change is packaging-only. Both canonical and grouped X18
independent-referee copies now accept exactly two explicit `__file__`-based
layouts, resolve the release-local `certificate_workspace`, confine every
dependency beneath that root before hashing, and reject every other layout.

## Root artifact lineage and package adaptations

The corrected root-replayed X16 theorem note was consumed without a divergent
mathematical patch. Its SHA-256 is
`d45e166a16d57ae39e596e023056965ad14c362359f19ceb268216ecce1d640d`.
The v10 source and referee differ from the root scripts only by the explicit
two-layout package resolver, package confinement, and the referee's rebound
source dependency.

The final package hashes are:

```text
X18 source                  dc4d586680587a369478154b5273b43b55e598c5bdb5451578df3592c0cea29b
X18 independent referee     d0d606581ce6cb95b4219d3c0090d3ef0cf07ff3ed138f7e38826449240463bf
X18 source manifest         d50d432faa9c0fcc3f92e8ab9fe7e14ae43fdeaa33f0a47e4b586ad0dba697e9
X18 referee manifest        6a1270de6e1d4161b31e574642daa2eb192ab9cd4baf9d22411ce0ea15f80554
X17 transitive ref manifest 2716855d3de1ccc83816afeef09cec48aff485c8eceea55d927c0c6a4f0aea7c

X16 theorem note            d45e166a16d57ae39e596e023056965ad14c362359f19ceb268216ecce1d640d
X16 source                  6b4835d5c00e56efa90d6451bd789554a0304be9880f45fc739066660d9ac2d4
X16 independent referee     cfb2bd700c68ac9f37cfbe1bf9f87b5d46791dc953d54e33c920929583044d6e
X16 independent audit       c44ac9120edbafa34b5d69677e2d66df85a290900aceaaca3b29bb60d2a66a0b
X16 package test results    b317db5c23d8f8fa0e791fe066a052c5f94353e9b60f067cce20bf8caf974c64
X16 source manifest         de35841d4965ee55fe1afb736dc158dba818dcfa6ad743c1d40284eae7644d68
X16 referee manifest        d34d3edb46eee0f386e757887a4d879bcfa642c7a7e66d584d2dd53b658dcdfa
```

Canonical and grouped copies of every listed script, audit, test record, and
manifest are byte-identical. An abandoned intermediate X16 referee was
dependency-mismatched, failed normal execution, and is not bound anywhere in
the frozen v10 tree.

## Exact replay and attacks

In the builder tree and again in a random fresh extraction, all eight normal
runs exited 0: canonical and grouped X18 source/referee, and canonical and
grouped X16 source/referee. Corresponding copies had byte-identical stdout:

```text
X18 source stdout   07f4bcff9663f701aff86af3605817abaaaefb9f044329e9f223ff1606d2c5c7
X18 referee stdout  0ec65c41b58fbf14cc87cbf02c5c732bf0c7ed8aae17571e959cd079526b75b8
X16 source stdout   0a61a5b061ce12c3287e688adf4fccabbff4815f4e59637e8b27c84c119d5021
X16 referee stdout  01dfa1cebcb0e33ee033c90e3acbb86b6c8704a8f9e97fbaae848db1e843a188
```

All eight distributed scripts rejected optimized Python and a forced bad
dependency. The four unique X18/X16 source/referee scripts rejected an
unknown copied layout. The four independent deleted-term runs were rejected
at the exact `16 higher terms and 947 parameter monomials` or `complete term
set` gates. All eight scripts passed `py_compile` with cache output outside
the extracted release. No verifier accessed a dependency outside the fresh
package's `certificate_workspace`.

## Manifest and host-path gates

All 45 canonical certificate manifests passed, checking 339 direct and
transitive entries. All 43 grouped manifest counterparts were byte-identical
to their canonical copies. One inherited t402 audit manifest bound three
portable checkpoint files omitted from v9; v10 includes exact hash-matched
copies of `AGENTS.md`, `PORTABLE_CHECKPOINT.md`, and `V22_HANDOFF.md` inside
`certificate_workspace`, so that historical manifest is now runnable in a
fresh extraction too.

The entire builder tree and fresh extraction were scanned fail-closed for
builder-specific and generic user-home paths, local-file URI schemes,
Linux/macOS home and volume prefixes, Homebrew/local installation prefixes,
private temporary roots, and Windows drive paths. No host-specific path
remains. Recorder files `main.fls`,
`main.fdb_latexmk`, and `main.log` were excluded after the recorded clean
build because they contain machine build paths.

## LaTeX, bibliography, PDF, fonts, and visual inspection

Two independent builder-tree clean builds under
`SOURCE_DATE_EPOCH=1787539200` produced byte-identical PDFs. A clean
LaTeX/BibTeX build in the random fresh extraction reproduced the packaged
PDF byte for byte. The stable source products are:

```text
main.tex       9df150707c86e332502f2297cf3675817d623813a392cd0996f109896d159ac7
main.pdf       add1fa51a2de24715760d57228023822cb8be28afa4e80f0e67f33cfbde4c63d
main.bbl       3d8e3ac2c999b50e84b126e5f04e108d3e74f0e971aa2ca9f91eaa4742d04f1b
references.bib 989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600
```

The bibliography gate reported 5 cited keys, 5 BibTeX entries, and 5 aux
keys, with no missing, unused, or duplicate key. LaTeX and BibTeX had no
undefined citation/reference, box, or actual warning. The PDF has 20 letter
pages; every font is embedded and subset.

All 20 pages were rendered with Poppler and visually inspected. There was no
clipping, overlap, overflow, broken formula, blank page, or illegible text.
The new X16 proof on page 13 and the exact `m_16`/endpoint data on page 20
received additional full-page inspection. All 20 fresh-rebuild PNG pages were
byte-identical to the inspected builder renders.

## Freeze status and remaining gates

After this report, the release manifest, delivered PDF, source ZIP, and
external sidecars are regenerated. The final ZIP is freshly extracted once
more to recheck its release manifest, forbidden-path scan, packaged/delivered
PDF byte identity, and file/entry counts.

The remaining technical gate is a fresh independent v10 final referee audit.
The remaining nontechnical submission gates are confirmation of author
metadata and the selected venue's AI-disclosure, acknowledgments, funding,
bibliography, source-format, and style requirements.
