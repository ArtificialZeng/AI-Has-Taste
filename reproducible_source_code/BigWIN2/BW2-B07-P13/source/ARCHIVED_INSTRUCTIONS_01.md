# Upstream Mordell tables

The exact filter uses the two complete tables linked from Michael A. Bennett
and Amir Ghadermarzi's data page:

- Data page: https://personal.math.ubc.ca/~bennett/BeGa-data.html
- Negative k, 0 < |k| <= 10^6:
  https://personal.math.ubc.ca/~bennett/0-10%5E6.pdf
- Positive k, 0 < k <= 10^6:
  https://personal.math.ubc.ca/~bennett/0-10%5E6n.pdf

Their accompanying paper is “Mordell's equation: a classical approach,”
LMS Journal of Computation and Mathematics 18 (2015), 633--646,
DOI 10.1112/S1461157015000182.

Expected file digests are embedded in `fetch_upstream.py` and in the derived
filter certificate.  The upstream PDFs are not redistributed in the LaTeX
source ZIP; the downloader retrieves the author-hosted copies and refuses a
digest mismatch.
