# v12 builder test report

Date: 2026-08-25 (Asia/Shanghai)  
Status: **technical builder candidate; pending a fresh independent v12 final
referee audit.**  This report is builder evidence, not the independent audit
and not an unconditional claim that the archive is ready for journal upload.

## 1. Frozen mathematical scope

The manuscript and package make two separate, connected partial-theorem
claims.

1. On the original centered five-real-parameter moving sheet, the scalar
   gate is nonnegative on the closed interval
   `0 <= X <= 428905727/1858957100`.  Uniform strict danger holds only on the
   half-open interval `0 <= X < 428905727/1858957100`.  The right endpoint is
   sharp only for uniform legality of the fixed centered box.  The formal
   point `X=1/4` is nonlegal and is not a gate counterexample.
2. On the distinct affine-omega chart
   `omega_phys = omega - (10636/275)(X-1/5)`, the exact source and independent
   referee prove the closed interval `1/5 <= X <= 3/13`, both signs of `z`,
   rank two, and `D >= S/100 > 0`.  All 48 exact Bernstein controls are
   strictly positive, with reserve

       2564950982194530478444050838857341987999
       ----------------------------------------------------- .
                31850496000000000000000000000

At `X=1/5` the tilt vanishes, so the two charts meet exactly and their union
is connected.  They are not identified as a single enlarged sheet.  The
paper does **not** claim a full compact-ball theorem, a general common-metric
theorem, an optimal fixed-lens constant, or an arbitrary-node theorem.

## 2. Root-promoted artifacts and package adaptation

The following hashes identify the root-promoted theorem/source/referee/audit
chain consumed by v12.  The theorem notes and audits are copied without
mathematical alteration.  Each executable verifier is adapted mechanically
to a two-layout, `__file__`-based, package-confined resolver; therefore its
package hash is deliberately different from the root hash.  Canonical and
grouped package copies are byte-identical.

| cell | root theorem | root source | root referee | root audit |
|---|---|---|---|---|
| X13 | `bc28de7eb9fb5f107414eac91f03a296271b3ca42086324c0bb9981051cef302` | `00fa00540037ae711ee014983884c4b95bcacfe7c39d586f4cbae7ec3cc80971` | `05fd9905720283dea7a9e25707940217e66de2e381595d6061af7782bff6671e` | `5a73fd66241648074155ac60acf1fac29e0f377a470428e5961c3865565b2c26` |
| X12 | `114cd2645ebd383a1a98ab35e102f517a090d7c99f9fc1b73abe2807ead5b81b` | `f85f292a5a6dab1091f5f0fa344e474b8da87a47ce7deccb0dc990f26025dd55` | `4b84c66582fe995cf88dce7534435a32183bc00bcbfd95276a6c4177635721c7` | `de9df71062bd8bf208ebc36f1fbfdd3746d993b917f141a5ff7a5e70ff7633e0` |
| X11 | `d426d2517cfbe5cb04b0680b481ca2d7921875665cd1758eb2c08675ba69b123` | `e824428e6d0c72a49a580c1c53dc0366a37800b2e74934898d334bba56565d46` | `a1241f4be0184ee030f1558502812ea3eefefa0376528316dc8512fefcbf95b0` | `cdae4f788e653ea149ba88ebf089511246e9de074e05eeb306d8f73aa47c7e35` |
| X10 | `1d5139b283f50bbcb1ad4b49e6f47b5a8a85ccc730ace19c4d3f09a33dc32b83` | `dd65ae3e8a2891b13f0fa3991dbe35057dd8c04480eee3b1528c9ce9cd4dcd5c` | `b33291f23537e5e23ae04d02a83e0f4373ec0f9fd8dd2fb33589a15ce7004364` | `8dd6a192c185e3c56192a089d3fd48870e681d1707e96340c46c835196824a00` |
| X9 | `a159ddf16593fe599b7d40adbceeb5e760965796582d8c4a6cee62e89f6dbeab` | `8c668472aee9fe42bb740d1c4fe0671396140c379f189e45c41df4e94f2aa076` | `fd076079aeee4c7d4dbb443156680f91182ca4c686be5dc6218dadae40da93f0` | `609d22fae7547fcdc68830298ec87c16e71b3f66a50979856f69d49680d9c007` |
| X8 | `98d896613808cf42eb7f80c36dfeee39e3c1bc36d0de81718ca66b21bcdc3067` | `6a68e71a059bf8ff867e51529a08130b295773a6a50cf5e3c092c935cfb1f8c1` | `17cbf3b55c7f0cd9898d5bea8cce0bcdd6b2cb15fface8eff8bba62b44cf7af7` | `55819c95c2b54b6dc2ffbfdf78eae54f980b780c6feeb7c541ea6a35b09fc519` |
| X7 | `76622dab1b117189e333db6b382b0c745a6586ea20ad9f6a85f0c43c788576c0` | `05e480e1b0228a1101306374da2d0563766c4fa522725c1df380dd3f6661113d` | `6d1b3a03a71118bb581eaface4da231e9b5bbbcc2217b8e63da188fa26f91339` | `9ec6de24510b8bc27113dab2b971bcc8da8fe3bdbf5861d884763ef2a2137749` |
| X6 | `db209c6987f806e90a5e521bee887a82b0394a8bb7090107ef1a4143e8ae0bfa` | `997d20985aa98a09518a75eaf385bab41b5f0911953fda6ebc356f6088eb264d` | `2f184c99b44cd0d85ca01a250f0d9e0514354c93d289d27a5ab0bcd747846110` | `7c69fa457a343fcf12748bc5ead3a788b94f38cf7859a13bb8063cb601c4ae72` |
| X5 | `a86dbe3eea4d9bfaf2772383407e65a5960e6941344713377068ff048ffc5f4d` | `60d7d2bc3c79d9261bd0d85917c488950a55aa9d941cea2e3101a475a594cad4` | `a4738635fd660ec5bf2003a9b56f2a680ce327059d87f89d2c903ff2da923cf7` | `d2283df6f7414580764f2572167441bc8ff3026fae8ad1882a0960312764d078` |
| X4 breakpoint | `e3f37ef598110eaad6c96a45eabff1e6313256923950057e8145568dbde865e0` | `e6190b282d16b837adf22c252bb9dd82308ddcc2c3b34806ccae445d365a7b5d` | `39c053b869f0b8a6a4af23873d9be4342517220f0a93aa777ffc89112d158873` | `01a8ba94013601bc2d71e4616f3af84763d345bb0169fb5f2c5c47bef04a9b03` |
| affine tilt | `bd127112e0cd59e9f0ed8c565480a612c2c75ba83edd979c3552896b18395067` | `50c81b2ce85f5d162844a477e329d79301b1e54facbddd9f4b6506446a00992f` | `becc0405facab40e95aac34e718453010bb18fea29c8ab73e69657157d9a1acd` | `33452bd574d47968fbbc599d6017806c47e672ef9e9ab86a5a2473e1a223a1b2` |

The affine discovery lineage is also present in both layouts:

- discovery source: `51d51d98f8e49a286aeedca1d3fed510024421d4b58d6c967ec6ea1aac42075a`;
- discovery note: `a0007fd1a788afcb0669dc95e165c4f45fa8bd641fe4436f1e3823e2e9010670`;
- split-comparison source: `06ff590d9fcf2b45aefcaf19a76f39c42fe73851231df5a3c113ef3e49d018fb`;
- root test results: `33d54c33e3252bc214fc49e8ede69cd2b3c0a2e823bba64d56c4763be8aa7966`;
- root theorem/source-freeze/referee manifests:
  `e501a790677564c2617631b91a30a34459443c0b8371a0a8266a5f5e3316d003`,
  `715ceebfe6f70c8db3620991a1185e24f46406f04e3defc3720544be77db4ac3`,
  `a656b6f1b0f7979b2b81bd584103de6a369b102636ad877598f4e156e395427a`.

## 3. Package replay matrix

All commands below use exact rational arithmetic.  No sampled grid or
floating-point positivity test is counted as proof.

- Normal runs: `11 chains x 2 roles x 2 layouts = 44/44`, all exit `0`.
- For every chain and role, canonical and grouped stdout are byte-identical.
- Fail-closed quick matrix: `110/110` expected nonzero exits, covering
  `python -O`, bad dependency, and unsupported-layout attacks.
- Deleted-control attacks: `22/22` expected exit `1`.
- External-cache `py_compile`: `44/44` exit `0`; no `__pycache__` or `.pyc`
  entered the release tree.

Package hashes appear in the order source, referee, source manifest, referee
manifest, source stdout, referee stdout:

```text
X13 9c2fe18283463edbc004d5f75273f8931bab6b3e2b28e17cb8a4759c23c6e570 67233d8cd9a4850d176746e8be7881bd007fbcbec4f903a16a5714aba8a5ebbb e184c75443a7cd1c37409f03dbee808c740caf796fdc956e6a71ee0c41eb768c 345eeba7c98e49b607978e4f1cafe0c1799ab686a6a8492ae5748c6efb481682 165cbb2cd3a3ec272a258c8df6bea89d4eab930dd7838113279d358513b4b026 2c9e873fc6a2110179d50d8d57cbc24787e7c181164317d5a76b1048c322a721
X12 b1204f1ba159cbf22c95fbd4e767b13fb1b30f534082cb5eb2db6a3f10422dbf 362233e082e9d7f871dea9f44a3ba292e812c607ccb2dbe42546cf005d902d05 548cbd9d3f1c710eeece3db30f909d8c2e6dc7e9c20224d1ad5b32a3924c2f55 84550386c8a0bac7161a7aa771a22bf8a8e22748489052885c17e261eacbe5f3 58cfcd6c73c3098e0ee104c01caee5ac4815438d787de6e0e7108177f8bba96f 2bdfd5fe38a777c5df90599a8c1ae7fdde380330c25790930f79f70637a31369
X11 4344f5b17c6910472f99c9f0565ad394657105019e7a5cd1fae0bf6497c31ba1 34a518c73f11d936de16e97f7580f5e6118002f2a9927dc6337bd91b499720bd 8c230ca77e8edc7d7ba6e3385806271fb5a86952765c98076e2d4ad932e858d6 09b517802a748ecb60607736d9a7b8e09f36364bce70c03777e8abda456c2422 8995433be9866e36496e6c395f9f46987b199e369e4ad1f4f8e2315ee7233154 163219b335e8f93731774878d33500fbffffb40b166a67d84b5a58f55e6ba35c
X10 2abd097ad86565645a4b89b7a239a9d6f97b2e355f3f8e2f64bf89b9832fbc62 0ab79bbc6f754c23085586d8f508b16b00f567551e3d9f5cb6c8d248f09a55ac 504deba75c5f02b0dbfaf6dd8f86406609a5195560497fe1b783167314af7854 87b44ad720ba40abb72a14b3268bad38667b3ca39fc1e6a4478450de7dd0b416 0ce1c5ddbd3f23f0864472ed4fb2fa56a0a8fba9c132c26cfef24934f934381d 20b0a7ff8fa72ae5f617178bab5766e22b122408da5e47bc0513a890ac7851fb
X9  afaca6c51cb389272292fa8c61ede272582720732bd3fefe821fcc2cbc06d1d5 6c10f2fd8a25f202ba9255067a67422821d0c0a41fac82543cce944a2e599f38 c451e52c6fe9f4e60efb79f4694b2447befa39042de6bd0f186e7671676ce7b4 50592afa640ab8d6a0d792da23251bcc5b4e25a2a4863147d042e2e377aaa9dd b1c504d96db1696a1feb0d2b84169797acee631334b5be0fd008753087ca8b8d afbab5d2dd644327ea69ce9e26cd97c432d6f268e89cedf0c2040f5025c2d4c9
X8  ac43a2b1b82a521378066f2b4162d0134bd19cccd0f9e49900702652930458bc 021226c2d4809b8e5131726b03d58fc5f89a566bbeaa50949b5cce27f95943c8 7032ab2a165116f1eea1ff86a701a675200b46701c6c6f2bd15a00ad3667f39b ad48331c56031f9a1683d46857115d612135deed8835f07aae20daaed6b3ae8b 8bb69574e4baea8fde3307df16bfdd6b1855d9084a0073c2f4601ca46e93dfa4 785f8fd8d77d5f99a2c8afab78e0ae0a866996140265c9b2836e520f005ac25f
X7  bd253e74b1ec9e03e1f2350f1b1428a447555f24e5b1c4eeb01ded0c36c7d880 8b2f21c103525a9889e8f25b2c30e1d2bd6e116e96b44c835db315efb2d6ad56 d8755ca47000080c48e505d1db018f60ef3f51db5f974414b77d6fbd7fa05918 94a9b68526cb7738b9348012c6cf84f40d0dad4eb171c5bcfb63ea27caed8ddf 7dd3d7e31d1e6244b408a0f6455ca05a2b352fcb384b3cb06c35e5634d3bfcae b75923cf2359cc8c1c848c70fddca1115e5c79c7e24df9bc92a2ac85d2635c01
X6  6d9f63d0a8e41b710eb2e4970bd405e2052ec0beb92b60bfc32568137e7ffc7e 8b0cac85ca318f4acdd9d759ceba13b13e559fa0c011e7048e6a8b6b318bfa3c f1b6c1eb258328cc70af866752b0b0ba2fffc7ac8a1ca3d9076b58420bb99b8a 0fa17c2c00173c5703d57a08ed0e6720a227cfba19bd32806ee77d6ba9bcfe5e acf3fefa793821600ab325d27160615d3fccb37d7d85b242ae80e47b505ce313 0b611043ac01060c49ed512dae7896a63c0acbf085ea612f8d235a86c4e2dcb9
X5  222f6aefe1efba50a214a96cfb3e611a26ad08a7b79e7e2cd3997bffcbee391b 1d6b218e94a3d5c46312d955b51c451cb0e3b1a6463418d56b22ff086c30dc0f 451e3b58706f442429f863d22b7591002cabd2bee7a737b4212e050938f1c549 768292a5c1508de27f99449144c1dc38ec8fc1b861f7473df59d36d84b73eb6a 40faca7963c7af3f16d4ebdb7ff08e16ff930d0e74ab9047d29086daa4dc6d0d f55ad314da8a8513d037ce440b7b4e3852dadc8ead6463f804ef91dcde9fb21b
X4  137765b9fe8afe9feaf51b8a71caa069908fc04ffd1eee4fac48b4b15da77289 73db20a9473e7c2e4806c21ecf547eee8e2a7e34007d27cd1acaa90d5ae41ebc ba0d212b34a7a33a890879444abaa7866304c6bd6725b9126b0d181acf830f93 d48dc0dd2b724c993ef733b8dccca7db42e1f767dac9184eb1781e38ea953bca 4bf789904bb186265b53273a85cafc1c7f08ba007de262d14b834b4242c9c191 784c42fe3568bdeba764a5b960cf0ea41eb7fef5899082435fd8d852d2832451
tilt 84587eef3507682eab241256444b559d3f800836001627d95831b10d4bb72cb8 89f3ed3778a3bb66db65f6f94448cc27b5cafd0cfa6839adc448c95fb7614516 17db0760acab91c4964ccfd1e5bfa320bce9a743f97e95c94498686c19ec1737 81bfa9207ec89bb3549e6e5a6f47f2cd8995fa40f4869869aba68fdad04bbb1b 92444120df7d6cb48c7a0d66424a31c97dc48b9766d2bba97e78fa8907ed600e d56fbc3541ce9ff6bd03a0ceb07b53ab1f1ce063db2ed7b3bb9430a05b873535
```

The canonical certificate workspace contains 76 nested manifests with 593
entries; all validate after the resolver adaptation and transitive hash
refresh.  Grouped copies of the new chains are byte mirrors of the canonical
files.

Two integrity events are disclosed rather than hidden: the root X5 chain
underwent a stale-results integrity repair before promotion, and the X4
referee underwent two pre-freeze SymPy normalization repairs replacing
uncancelled `(M+1)/(M+1)` assertions by exact factored zero checks.  Neither
event changes a mathematical constant, interval, or theorem statement.

## 4. Bibliography

The citation surface is unchanged from the independently accepted v11:
five cited keys, five BibTeX entries, and five auxiliary citations.  The
v12 `references.bib` and converged `main.bbl` are byte-identical to v11.
The citation checker reports no missing, unused, or duplicate key, and the
LaTeX/BibTeX logs contain no undefined citation or reference.  No citation
subagents were started because the project imposed a hard two-local-task
limit and the already verified citation set did not change.

## 5. Deterministic build, PDF, archive, and visual gates

Two independent clean builds with `SOURCE_DATE_EPOCH=1787539200` and
`FORCE_SOURCE_DATE=1` produced byte-identical PDFs:

- deterministic build A SHA-256:
  `1359a72329ef81a8c9e1c23eac680d157439c7f1ba8bbd06f04f19a4d643c70a`;
- deterministic build B SHA-256:
  `1359a72329ef81a8c9e1c23eac680d157439c7f1ba8bbd06f04f19a4d643c70a`;
- final PDF: 26 US-letter pages, with the same SHA-256;
- converged `main.bbl`:
  `3d8e3ac2c999b50e84b126e5f04e108d3e74f0e971aa2ca9f91eaa4742d04f1b`;
- unchanged `references.bib`:
  `989cbb89877e9af6649de49818bf9db5fc83b29f8fa96319fe22242784ade600`.

PDF metadata is deterministic, all fonts are embedded and subset, and the
extracted text contains the exact breakpoint, affine slope, closed `3/13`
endpoint, and scope exclusions.  All 26 final pages were rendered with
Poppler and visually inspected; no clipping, overlap, overflow, broken
formula, blank page, or illegible text was found.  The new tilted theorem on
page 16 and the dense exact-data pages 24--26 received additional full-page
inspection.

The release-manifest and ZIP hashes are intentionally not embedded in this
file because doing so would make the archive self-referential.  They are
recorded in the external SHA-256 sidecars and in the builder handoff.  A
fresh-extract manifest/build/PDF-identity gate is run after the archive is
created and is the final acceptance step below.

Fresh-extract acceptance: **PASS**.  A random-directory extraction validated
all 569 release-manifest entries, contained no forbidden host path, rebuilt
the PDF byte-for-byte, and matched the packaged and delivered PDF bytes.
The affine-omega tilted source and referee were additionally rerun in both
canonical and grouped layouts in that extraction: `4/4` exited `0`, and the
two source outputs and two referee outputs were respectively byte-identical
to the builder-tree outputs.  After this status line was frozen, the release
manifest and archive were regenerated once and the final archive was freshly
extracted again to recheck its manifest, host-path scan, clean rebuild, and
PDF byte identity.

The remaining nontechnical submission gates are intentionally unresolved:
author identity/affiliation/email confirmation, target-venue style and
disclosure policy, acknowledgements, and funding declarations.  No value is
invented for those fields.
