# Simultaneous 0120/0121 avoidance in ascent sequences

Source-derived problem, frozen by the outer supervisor on 2026-09-13; not a browser-generated batch or a quotation of a user problem.

For n>=1 let A_n consist of nonnegative integer words x_1...x_n with x_1=0 and x_i<=1+asc(x_1...x_(i-1)), where asc counts strict adjacent increases. Retain exactly those words having no four positions whose entries reduce to 0120 or to 0121; reduction preserves both order and equality of entries. Determine their all-length enumeration, equivalently a proved explicit ordinary generating function F(z)=1+sum_(n>=1)|A_n|z^n, or a comparably informative uniform structural enumeration beyond exhaustive word generation.

Primary source: Qi Liu, Sergey Kitaev, Philip B. Zhang, Simultaneous avoidance of length-4 patterns in ascent sequences, arXiv:2604.06735v1 (8 April 2026), definitions in Section 1, Table 1, and Section 6. https://arxiv.org/html/2604.06735v1

The source explicitly leaves this simultaneous-avoidance class unenumerated. Its initial counts for n=1..9 are 1,2,5,13,34,90,244,683,1980. These are calibration data, not a conjectured formula.

