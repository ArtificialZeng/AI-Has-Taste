# The growth of directional nondeterministic word separation

Primary-literature intake, 2026-09-13. Not a browser-generated 大WIN batch;
no batch number consumed and no target-conversation comparison claimed.

## Frozen original source

John W. Nicol, Further Remarks on Separating Words, arXiv:2608.30928v1,
31 August 2026, Section 4.1, physical pages 3–4:
https://arxiv.org/html/2608.30928v1
https://arxiv.org/pdf/2608.30928v1

The displayed definition and bounds, transcribed mathematically:

    A(q) = max{ nsep(w,x) : |w|=|x|, w!=x, nsep(x,w)<=q }.
    (q-1)^2+1 <= A(q) <= 2^q, for q>=3.

The source's exact remaining question is:

> The exact growth of A(q) remains open.

Here w,x are finite binary words. The NFA convention has one initial state,
an arbitrary accepting subset and possibly missing transitions; no epsilon
transitions are needed. nsep(w,x) minimizes the state count over automata
accepting w and rejecting x, with no restrictions on other words.

This is the entire A(q) problem, not just its one-marker subclass and not
the already resolved question of whether a directional difference or ratio
can be unbounded. Precise interpretation and proposed research route are
separate in problem.md and literature/outer-intake-handoff.md.

The original v1 PDF and HTML are saved unchanged in literature/ before
dispatch. PDF SHA25661f478189b3ee63c8b2e0d36f1d70cb738a1bf4796d5efd595b203c122b77f42;
HTML SHA25606589f3087746fa3e5f057dda290fcaec281c24317588756bf599f7a631505d4.
Read the short handoff before triage. No manuscript or acceptance at triage.
