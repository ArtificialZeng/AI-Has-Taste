# v11 builder report: X15/X14 moving-sheet extension

Date: 2026-08-24. Status: **builder candidate only**. This package is
pending a fresh independent v11 final manuscript/archive audit and must not
be called submission-ready.

## Scope

The mathematical change is restricted to the same five-real-parameter
positive-`Z` moving sheet. The two new exact closed cells are

```text
1/16 <= X <= 1/15,
1/15 <= X <= 1/14,
0 < S <= 1/10000,
|M| <= 1/1000,
|omega|,|nu| <= 1/100.
```

Together with the frozen predecessor chain they extend only the displayed
moving-sheet theorem from `X<=1/16` to `X<=1/14`. They do not prove the full
compact-ball quartic, the general complex Hermitian gate, a common metric for
arbitrary data, a fixed-lens or all-node theorem, or any optimal crossing-lens
constant. No Lean result is claimed for X15 or X14.

Both new cells lie beyond the old descriptive locator `Z=1/6`. The source
and referee verifiers reconstruct the actual lossless hypotheses

```text
0<S<=1, lambda>0, Z>0, x^2+y^2+Z<1.
```

No inverse, rank, gate, or denominator-clearing identity requires `Z<1/6`.
The X15 and X14 exact strict continuum reserves are respectively

```text
12366382505636800388307905057490747689083041004726403513462638991
/6150937500000000000000000000000000000000000000000000 > 0,

53550029757865949037427029808183214063735927456893583920630862251
/26635508121600000000000000000000000000000000000000000 > 0.
```

An X13 artifact was root-promoted after the v11 scope was frozen. It is
explicitly a post-v11 input and is not integrated or claimed here.

## PDF operation gate

Before the v11 tree was cloned or edited, the PDF skill's create-operation
marker was run exactly once with one expected PDF. It was not rerun after the
later X14 integration instruction.

## Root lineage and portable package adaptations

The X15 and X14 theorem notes and root-replayed source/referee/audit/test
records were consumed without a divergent mathematical patch. The package
source and referee scripts differ only by explicit two-layout `__file__`
resolvers, package confinement, and each referee's rebound source dependency.
Canonical and grouped copies are byte-identical.

Final package hashes are:

```text
X18 source                  dc4d586680587a369478154b5273b43b55e598c5bdb5451578df3592c0cea29b
X18 independent referee     d0d606581ce6cb95b4219d3c0090d3ef0cf07ff3ed138f7e38826449240463bf
X18 source manifest         d50d432faa9c0fcc3f92e8ab9fe7e14ae43fdeaa33f0a47e4b586ad0dba697e9
X18 referee manifest        6a1270de6e1d4161b31e574642daa2eb192ab9cd4baf9d22411ce0ea15f80554

X16 theorem note            d45e166a16d57ae39e596e023056965ad14c362359f19ceb268216ecce1d640d
X16 source                  6b4835d5c00e56efa90d6451bd789554a0304be9880f45fc739066660d9ac2d4
X16 independent referee     cfb2bd700c68ac9f37cfbe1bf9f87b5d46791dc953d54e33c920929583044d6e
X16 source manifest         de35841d4965ee55fe1afb736dc158dba818dcfa6ad743c1d40284eae7644d68
X16 referee manifest        d34d3edb46eee0f386e757887a4d879bcfa642c7a7e66d584d2dd53b658dcdfa

X15 theorem note            3bf5600929c88308f9bb3cb6ce4bfbfe3b1fa9dc4632cdf49ef4ca0d3954adfb
X15 source                  3b1e78e4117c34dcc04500b845fa52896308d2e815ed25df5bb4d83b9e312c27
X15 independent referee     7982c8475f04bea59ce438c88bdae65f131fe3752327635ab3fa69b750889f9d
X15 independent audit       f72655ebd904a761577e74f65a48e4ac50b2946777cc9504b17d2a2643a72e9c
X15 package test results    c6e900a4042aa57540898dc2b6f3eca180d4215516a02e2515a5fedc093ad405
X15 source manifest         ef4926cced7ccf1f1178ba0a2c3f598968e1e363a5c8b1b309aac67607c2e2ff
X15 referee manifest        19f3cd4aba6794a0fd4e4cbbafee447670a3fd78f7d5482a4fac8631f93776d5

X14 theorem note            676435f4c4626a827e86a1d63161a459155e26e5f69773ae7e07b412ce0d5384
X14 source                  da695b3f2620861e82a14d1e4d037e3dbf7fb7d1170389ac0950fc86f59c3b73
X14 independent referee     e7d785924e4b6e3039dcdff731a834ccd81346302b6dea017c93df843b5881d1
X14 independent audit       020800b2a0318760f5549cea94e5bee6c13e25607d8e3a6496df1eb1dd13b33d
X14 package test results    83134e5046f4680c37f3d65d3d76b9e4a5c942c98d778c6e18a53d9dbfeef73b
X14 source manifest         8da486a36d0be8aa2ce9b59d7996b4b00d163c0cd72afcba85fa06c0ae347bf5
X14 referee manifest        24dc513420bdba90f35b01d45fc5b5521cc4926c52417baebdf6055a14f34e38
```

## Exact replay and attacks

In a random fresh extraction, all sixteen normal runs exited 0: canonical
and grouped source/referee copies for X18, X16, X15, and X14. Corresponding
copies had byte-identical stdout:

```text
X18 source stdout   07f4bcff9663f701aff86af3605817abaaaefb9f044329e9f223ff1606d2c5c7
X18 referee stdout  0ec65c41b58fbf14cc87cbf02c5c732bf0c7ed8aae17571e959cd079526b75b8
X16 source stdout   0a61a5b061ce12c3287e688adf4fccabbff4815f4e59637e8b27c84c119d5021
X16 referee stdout  01dfa1cebcb0e33ee033c90e3acbb86b6c8704a8f9e97fbaae848db1e843a188
X15 source stdout   0cd6a38926684f01428b8eaeb95e5a8c8036163d0e496a4d473a5d6b72eea1c0
X15 referee stdout  b25dfc9b448c58f5dd684b33b4d9919744d83add0853aff20d371c11e1596701
X14 source stdout   38af5e27923e84b4dc5dabb8e0577f16c9de6b6512fdfa1fae41eaf04622fad9
X14 referee stdout  d244cde029f4b614c6bfe709131c9aaf025b78cca046ee7f7cb94a2d023efe74
```

All sixteen distributed scripts rejected optimized Python and a forced bad
dependency. All eight unique source/referee scripts rejected an unknown
copied layout. All eight deleted-term attacks were rejected at the exact
`16 higher terms and 947 parameter monomials` or `complete term set` gates.
All sixteen scripts passed `py_compile` with cache output outside the release.
No verifier accessed a dependency outside the fresh package's
`certificate_workspace`, and no cache or late file appeared in the package.

## Manifest and host-path gates

All 49 canonical certificate manifests passed in the builder and fresh trees,
checking 375 direct and transitive entries. All 47 grouped manifest
counterparts were byte-identical to their canonical copies. This includes the
inherited t402 audit manifest and its portable checkpoint dependencies.

The builder tree and fresh extraction were scanned fail-closed for
builder-specific and generic user-home paths, local-file URI schemes,
Linux/macOS home and volume prefixes, package-manager installation prefixes,
private temporary roots, and Windows drive paths. No host-specific path
remains. Recorder files `main.fls`, `main.fdb_latexmk`, and `main.log` are
excluded from the frozen package.

## LaTeX, bibliography, PDF, fonts, and visual inspection

Two independent builder-tree clean builds under
`SOURCE_DATE_EPOCH=1787539200` produced byte-identical PDFs. A clean
LaTeX/BibTeX build in the random fresh extraction reproduced the PDF byte for
byte. Stable source products are:

```text
main.tex       2b23ad3ee50540e6f811284785b2da7c68226d606ab72d9fe63dffaae4c2ed8e
main.pdf       91794e054228d51cabbe5afb735bb52a0aec890e7633c582c25e7176695db641
main.bbl       3d8e3ac2c999b50e84b126e5f04e108d3e74f0e971aa2ca9f91eaa4742d04f1b
references.bib 989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600
```

The unchanged bibliography gate reported 5 cited keys, 5 BibTeX entries,
and 5 auxiliary keys, with no missing, unused, or duplicate key. The frozen
official-record audit remains the v8 bibliography audit; no citation or BibTeX
record changed in v11. Final LaTeX and BibTeX logs had no undefined citation,
undefined reference, box, repeated, or other warning. The PDF has 21 letter
pages; all 29 fonts are embedded and subset.

All 21 pages were rendered with Poppler and visually inspected. There was no
clipping, overlap, overflow, broken formula, blank page, or illegible text.
The new X15/X14 proof on page 13 and exact reserve/endpoint data on pages
20--21 received additional full-page inspection. All 21 fresh-rebuild PNG
pages were byte-identical to the inspected builder renders.

## Freeze status and remaining gates

After this report, the release manifest, delivered PDF, source ZIP, and
external sidecars are regenerated. The final ZIP is freshly extracted once
more to recheck its release manifest, forbidden-path scan, packaged/delivered
PDF byte identity, and file/entry counts.

The remaining technical gate is a fresh independent v11 final referee audit.
The remaining nontechnical submission gates are confirmation of author
metadata and the selected venue's AI-disclosure, acknowledgments, funding,
bibliography, source-format, and style requirements.
