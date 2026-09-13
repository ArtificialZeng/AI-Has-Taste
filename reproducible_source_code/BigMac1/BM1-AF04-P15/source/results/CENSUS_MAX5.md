# Certified four-letter census through maximum 5

## Exact result

For every four-element integer alphabet, translate its minimum to zero, divide
by the gcd of the translated letters, sort, and identify the result with its
reflection.  Among the primitive normalized representatives
\(A=\{0<a<b<c\}\) with \(c\le5\), the complete list and exact ASF maxima are:

| \(A\) | \(g(A)\) | tree nodes | leaves | maximizers |
|---|---:|---:|---:|---:|
| \(\{0,1,2,3\}\) | 50 | 187,789 | 50,136 | 16 |
| \(\{0,1,2,4\}\) | 62 | 19,097,778 | 5,350,440 | 2 |
| \(\{0,1,3,4\}\) | 55 | 659,727 | 183,150 | 4 |
| \(\{0,1,2,5\}\) | **86** | 299,596,819 | 83,646,960 | 8 |
| \(\{0,1,3,5\}\) | **88** | 234,485,149 | 66,026,525 | 2 |
| \(\{0,1,4,5\}\) | 55 | 1,137,005 | 322,450 | 4 |
| \(\{0,2,3,5\}\) | 55 | 850,735 | 241,212 | 4 |

The two bold values were not located in the dated literature search.  This is
a bounded novelty statement, not a priority claim.

## Why the certificate is complete

There is one representative at maximum 3, two at maximum 4, and four at
maximum 5.  `src/list_normalized_alphabets.py` reconstructs this list directly
from gcd and reflection normalization.

Each DFS vertex is one ASF prefix, including the empty root.  When one letter
is appended, every old factor is unchanged; hence the only newly possible
additive square ends at the new final position.  Checking every suffix
half-length therefore accepts exactly the children in the ASF prefix tree.  A
closed traversal supplies the upper bound, and a regenerated maximum-depth
word supplies the matching lower bound.

The discovery program stores left-to-right prefix sums.  The independent
verifier instead rebuilds right-tail cumulative sums from the current word,
enumerates every tree again, and compares node counts, leaf counts, maximum
depth, maximizer count, a canonical digest of all maximizers, and an explicit
witness.  It imports no discovery output.

## Reproduction

Fast discovery, one alphabet at a time:

```sh
clang++ -O3 -std=c++20 -Wall -Wextra -pedantic \
  src/exact_prefix_dfs.cpp -o experiments/exact_prefix_dfs
./experiments/exact_prefix_dfs 0 1 2 5 --node-limit 1000000000
./experiments/exact_prefix_dfs 0 1 3 5 --node-limit 1000000000
```

Independent full verification:

```sh
python3 certificates/verify_finite_census.py certificates/census_max5.json
```

Verified terminal record:

```text
{"certificate_sha256": "ebeb72ca4f04e377de266f4c403f6e2480bed3232feabb923d1436685057ce19", "records": 7, "status": "VERIFIED", "verifier_cpp_sha256": "dc8c5e25393fd58456ab72178b79cd636ec6f4006ccdfd80a4b363e1c766ef19"}
```

This census proves nothing about normalized alphabets with maximum at least 6,
alphabets with five or more letters, or the full infinite existence problem.
