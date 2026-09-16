# Inspected primary source extract

Huang–Lehtonen, Associative-commutative Spectra for Some Varieties of Groupoids, ECA 4:4 (2024), Article S2R29.
URL: https://ecajournal.haifa.ac.il/Volume2024/ECA2024_S2A29.pdf
Read 2026-09-12 from supervisor-cached primary PDF text; journal web open returned an internal error.

## PDF page 1

                       pplications
 numerative
                  A
       ombinatorics

ecajournal.haifa.ac.il
                                     Enumerative Combinatorics and Applications                ECA 4:4 (2024) Article #S2R29
                                                                                               https://doi.org/10.54550/ECA2024V4S3R29




                      Associative-commutative Spectra for Some Varieties of Groupoids

                                                               Jia Huang: and Erkko Lehtonen;

                               : Department of Mathematics and Statistics, University of Nebraska, Kearney, NE 68849, USA

                                                                      Email: huangj2@unk.edu

   ; Department of Mathematics, Khalifa University of Science and Technology, P.O. Box 127788, Abu Dhabi, United Arab Emirates

                                                                 Email: erkko.lehtonen@ku.ac.ae

                                        Received: June 18, 2024, Accepted: July 31, 2024, Published: August 9, 2024
                                            The authors: Released under the CC BY-ND license (International 4.0)

   Abstract: The associative spectrum of a groupoid (i.e., a set with a binary operation) measures its nonas-
   sociativity while the associative-commutative spectrum measures both nonassociativity and noncommutativity
   of the groupoid. The two spectra are also the coefficients of the Hilbert series of certain operads. We establish
   upper bounds for the two spectra of various varieties of groupoids defined by different sets of identities and
   provide examples (often groupoids with three elements) for which the upper bounds are achieved. Our results
   have connections to many interesting combinatorial objects and integer sequences and naturally lead to some
   questions for future studies.

   Keywords: Associative-commutative spectrum; Associative spectrum; Binary operation; Tree; 3-element
   groupoid
   2020 Mathematics Subject Classification: 05A15; 20N02; 08B05


   1.          Introduction
   A groupoid pG, ˚q is a basic algebraic structure that consists of a set G together with a binary operation ˚
   defined on G. Associativity and commutativity are common properties that could be satisfied by a groupoid.
   Csákány and Waldhauser [3] defined the associative spectrum (also called the subassociativity type by Braitt
   and Silberger [2]) to measure the failure of a groupoid to be associative, and we introduced the associative-
   commutative spectrum, or simply ac-spectrum, to measure both nonassociativity and noncommutativity of a
   groupoid in earlier work [6]; see the definition below.

   Definition 1.1. Fix a countable list of distinct variables x1 , x2 , . . .. Let Bn denote the set of all bracketings of
   x1 , . . . , xn , which are terms in the language of groupoids obtained by inserting pairs of parentheses into the word
   x1 x2 ¨ ¨ ¨ xn in all valid ways. Let Fn denote the set of full linear terms over x1 , . . . , xn , which are obtained by
   permuting the variables in the bracketings of x1 , . . . , xn . We can view Bn as a subset of Fn . Every term t P Fn
   induces an n-ary operation t˚ on a groupoid pG, ˚q. It is often convenient to think about the terms in Fn or
   the n-ary operations induced by them in terms of the corresponding (ordered, full) binary trees with n labeled
   leaves; see the example below for B4 , which can give F4 if the variables are permuted in all possible ways.

                               4                                                        4       1                     1
                                                 1    2    3    4
                 1 2 3                                                    1    2 3                   2 3      4            2    3 4
               ppx1 ˚x2 q˚x3 q˚x4               px1 ˚x2 q˚px3 ˚x4 q      px1 ˚px2 ˚x3 qq˚x4    x1 ˚ppx2 ˚x3 q˚x4 q   x1 ˚px2 ˚px3 ˚x4 qq

   The associative spectrum (resp., ac-spectrum) of a groupoid pG, ˚q, or of its binary operation ˚, is a sequence
   whose nth term is san p˚q :“ |Pn p˚q| (resp., sac                                        ˚                                ˚
                                                     n p˚q :“ |P n p˚q|), where Pn p˚q :“ tt : t P Bn u (resp., P n p˚q :“ tt :
   t P Fn u), for n “ 1, 2, . . .. It turns out that tPn p˚quně1 (resp., tP n p˚quně1 ) together with a composition function
   becomes a nonsymmetric operad (resp., symmetric operad) that satisfies certain coherence axioms [11], and the
   Hilbert series of this operad is the generating function (resp., exponential generating function) of the associative
   spectrum (resp., ac-spectrum) of pG, ˚q.
      By the above definition, we have (1) san p˚q “ 1 for n “ 1, 2, (2) sac                  ac
                                                                          1 p˚q “ 1, and (3) s2 p˚q is either 1 or 2,
   depending on whether ˚ is commutative. Thus we may assume n ě 3 when necessary. It is easy to see that

## PDF page 17

                                          Jia Huang and Erkko Lehtonen


To generalize the above theorem, one could use a primitive root of unity ω :“ e2πi{k to define an operation
a ˚ b :“ ωa ` ωb on the field of complex numbers, which reduces to the double minus operation when k “ 2; for
k ě 3, the n-th term of the associative spectrum was shown in [10] to coincide with the number of equivalence
classes of the equivalence relation on n-leaf binary trees that relates two trees if the depths of corresponding
leaves are congruent modulo k. Closed formulas for the associative spectrum and the ac-spectrum of this
operation are yet to be determined.


7.      Questions and remarks
We have some more questions other than those in the last section. Our computations suggest that a majority
of the 3330 non-isomorphic 3-element groupoids have their ac-spectrum reaching the upper bound n!Cn´1 and
thus have their associative spectrum reaching the upper bound Cn´1 . Some other 3-element groupoids have
smaller spectra, including those given earlier in this paper as examples for various upper bounds to be sharp.
We also have computational data on the spectra of several other 3-element groupoids but do not have any
general result on them.
    For instance, our computations show that the first several terms of the associative spectrum and ac-spectrum
of each of the following groupoids are 1, 1, 2, 5, 12, 28, 65, 151, 351 and 1, 2, 12, 96, 880, respectively; the former
agrees with the initial terms of a trisection of the Padovan sequence [13, A034943].
                      ˚   0 1      2      ˚   0 1      2      ˚    0 1     2      ˚    0 1     2
                      0   0 0      0      0   0 0      1      0    0 1     1      0    0 1     1
                      1   1 1      0      1   1 1      0      1    0 1     0      1    0 1     0
                      2   1 0      1      2   1 0      0      2    0 0     1      2    1 0     0
                          SC258               SC685               SC1594              SC1600
It is clear that SC258 and SC685 are anti-isomorphic to SC1594, SC1600, respectively. One can check that
SC258 and SC685 both satisfy at least the following identities.
  pwxqpyzq « pwxqpzyq,      ppwxqyqz « ppwxqzqy,       pvwqpxpyzqq « pvwqppxyqzq,      vppwxqpyzqq « pvpwxqqpyzq
   Next, consider the following 3-element groupoids.
                      ˚    0 1     2      ˚    0 1     2      ˚    0 1     2      ˚    0 1     2
                      0    0 0     2      0    0 0     2      0    0 1     1      0    0 1     1
                      1    2 0     2      1    2 2     0      1    1 0     0      1    1 0     1
                      2    2 2     0      2    2 0     0      2    0 0     1      2    0 1     0
                          SC1414              SC1477              SC1693              SC1717
There is an anti-isomorphism between SC1414 and SC1717 and between SC1477 and SC1693 by swapping 1
and 2. It is routine to check that SC1414 and SC1693 both satisfy the identities pwxqpyzq « pyzqpwxq and
ppwxqyqz « ppwxqzqy. Computations show that the first several terms of its associative spectrum and ac-
spectrum are 1, 1, 2, 5, 13, 35, 97, 275, 794, 2327 and 1, 2, 12, 96, 980; the former matches with the initial terms of
a generalized Catalan number [13, A025242], which counts Dyck paths of length 2n avoiding U U DD.
   Computations also show that the first several terms of the associative spectrum and ac-spectrum of the fol-
lowing two anti-isomorphic groupoids are 1, 1, 2, 5, 14, 42, 132, 429, 1430 and 1, 2, 12, 108, 1340; the former agrees
with Cn´1 while the latter is less than n!Cn´1 .
                                          ˚   0 1      2      ˚    0 1     2
                                          0   0 0      0      0    0 1     1
                                          1   1 0      1      1    0 0     1
                                          2   1 1      1      2    0 1     1
                                              SC229               SC1553
One can check that SC229 satisfies the identity ppwxqyqz « ppwxqzqy.
    It would be nice if the associative spectra and ac-spectra of the above 3-element groupoids (or even better,
groupoids satisfying the same identities as the above groupoids) could be determined.
    Another question is about the arithmetic mean on R. Csákány and Waldhauser [3] showed that its associative
spectrum is Cn´1 . In previous work [6], we showed that its ac-spectrum is the number of ways to write 1 as
an ordered sum of n powers of 2 [13, A007178]. It would be interesting to find the identities that could be
used to characterize all the groupoids whose associative spectra and ac-spectra are bounded by the above and
if possible, find a 3-element groupoid to achieve the upper bounds.
    Lastly, we provide a generalization of a result in our earlier work [6], which asserts that an associative
groupoid pG, ˚q must have sac n p˚q ď n! and this upper bound holds as an equality if pG, ˚q is noncommutative
and has an identity element.


ECA 4:4 (2024) Article #S2R29                                                                                       17
