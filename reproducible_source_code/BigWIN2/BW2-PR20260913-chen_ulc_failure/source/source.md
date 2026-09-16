# Higher-degree ULC failure for Chen's recursion polynomials

Source-supported mathematical transcription, not a browser-generated batch.
Stephanie Chen, *Log-Concavity of the Grothendieck Classes of Banana Graphs
and Clasped Necklaces*, arXiv:2503.16296v2, Conjecture3.9, printed p16.
Definitions: equations(3.1),(3.3),printed p10; ULC normalization:
Definition2.4,equations(2.14)–(2.15),printed pp8–9.

For every integer m>=4 define polynomials
f_m(s)=((s+1)^m-(-1)^m)/(s+2) and
h_m(s)=((s+1)^m+(-1)^m(s+1))/(s+2).
Both have degree d=m-1. If p(s)=sum_{j=0}^d a_j s^j is either one,
ordinary ULC means that a_j/binom(d,j) is log-concave.

The original claim consists of both:
1. Neither f_m nor h_m is ordinary ULC, for every m>=4.
2. At each integer index 4<=j<=m-2, both coefficient sequences strictly
   fail the ordinary ULC inequality; explicitly,
   j*(m-1-j)*a_j^2 < (j+1)*(m-j)*a_{j-1}*a_{j+1}.

The second range is empty for m=4,5. The first statement is not empty.
The normalization is order m-1, not ULC(m); this distinction is essential.
No subcase, equality, or endpoint convention has been silently changed.

Original primary PDF:
https://arxiv.org/pdf/2503.16296v2
SHA256 0a673529c79637037b46b00444ff34f5af961c0957cd00c5dc022f7dee94260a.
Complete bytes retained; the above is a faithful explicit mathematical
transcription, not a claim that a browser generator supplied it.
