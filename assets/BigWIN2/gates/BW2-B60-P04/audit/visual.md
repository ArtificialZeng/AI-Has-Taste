# Rendered-page visual audit

The current four-page PDF was rendered afresh at 170 dpi to a digest-specific
temporary directory. I opened and visually inspected pages 1, 2, 3, and 4 at
original image detail, exactly once each.

- Page 1: title, author block, abstract, contextual citations, notation, and
  equation (1) are complete, aligned, and inside the margins.
- Page 2: the theorem, equations (2)--(7), scope paragraph, and beginning of
  the proof are fully visible with no clipping or symbol loss.
- Page 3: the graph-kernel argument, six coefficient list, specialization,
  support inequalities, proof ending, and Remark 2 are legible; the end-of-proof
  mark and footer do not overlap text.
- Page 4: limitations, assistance disclosure, and all five bibliography items
  render cleanly and remain inside the page.

There are no figures, charts, or tables requiring value-by-value visual-data
checking. Mathematical primes, transposes, subscripts, Greek symbols, set
braces, inequalities, equation numbers, and citation numbers render distinctly.
No page has clipped text, overlap, orphaned headings, illegible fonts, or
distorted graphics. Cross-references and citations resolve to numbers, and the
bibliography is complete.

`pdfinfo` reports a valid unencrypted four-page letter-size PDF produced by
pdfTeX with hyperref. The optional metadata title/author fields are empty, while
the title and full author identity are visibly typeset on page 1; this causes no
ambiguity in the artifact and is not a rendering or release blocker.

The authored scope matches the accepted mathematical statement: the paper is
limited to the two-state affine-linear characteristic-zero row and explicitly
disclaims nonlinear, sparse, time-varying-coefficient, positive-characteristic,
and broader sharp-support conclusions. No unsupported strengthening was found.
