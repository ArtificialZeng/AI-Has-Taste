# Precise statement and triage scope

The frozen original is source.md, unchanged. It reproduces Conjecture 4.6 of
Elizalde–Rivera–Zhuang, *Counting Pattern-Avoiding Permutations by Big Descents*,
Annals of Combinatorics (2026), DOI 10.1007/s00026-026-00805-1.
[Primary journal source](https://link.springer.com/article/10.1007/s00026-026-00805-1).

## Definitions and quantifiers

For every integer n >= 0 let [n]={1,...,n}, and let S_n be its permutations
in one-line notation. S_0 consists of the empty word. Put
S_3={123,132,213,231,312,321}. An occurrence of sigma in S_3 is a triple
of indices i<j<l whose values have relative order sigma; the indices need
not be consecutive. S_n(Pi) consists of permutations avoiding every
sigma in Pi, with Pi a subset of S_3 of cardinality one or two.

For pi in S_n, define

    bdes(pi) = #{i : 1 <= i <= n-1 and pi_i > pi_(i+1)+1},
    b[n,k](Pi) = #{pi in S_n(Pi) : bdes(pi)=k},
    B_n(t;Pi) = sum_{k=0}^n b[n,k](Pi) t^k.

Counts outside the attainable range are zero. The original assertion is:

    For every n in Z_{>=0}, every Pi subset S_3 with |Pi| in {1,2},
    and every integer k with 1 <= k <= n-1,
    b[n,k](Pi)^2 >= b[n,k-1](Pi) b[n,k+1](Pi).

Thus there are 6+15=21 pattern families, with no bound on n. Log-concavity
here means precisely the displayed weak inequalities; it imposes no extra
requirement that every entry or row be positive. The cases n=0,1 are
vacuous, and B_0=1, B_1=1, B_2=2 for every family. For Pi={123,321}, all
rows n>=5 vanish and must remain included. At n=3 and n=4 this family's
nonzero rows are (2,2) and (1,2,1), respectively.

The source claim is unambiguous under these definitions. Real-rootedness,
strict inequalities, right big descents, ordinary descents, larger forbidden
sets, and r-descent refinements are not replacement original targets.

## Source classification and immediate coverage

Theorems 1.1–1.2 identify four singleton and seven doubleton big-descent-Wilf
classes, meaning identical B_n for every n. Here each singleton entry
names the forbidden pattern, and each braced entry a forbidden pair.

| Entire equivalence class | Source result and triage implication |
|---|---|
| 123 | Theorem 2.13: product of two binomial coefficients; LC follows directly |
| 231; 312 | Theorem 4.5: real-rootedness; LC follows |
| 132; 213 | Theorem 2.1: algebraic generating function; LC not settled by this screen |
| 321 | Theorem 2.8: algebraic generating function; LC not settled by this screen |
| {213,231}; {132,312}; {213,312}; {132,231} | Theorems 3.1/3.3: C(n,2k+1); LC follows |
| {123,132}; {123,213}; {132,213} | Theorems 3.5/3.8, Lemmas 3.6/3.9: exceptional binary-word class; LC target |
| {231,321}; {312,321} | Theorem 3.10: rational generating function; LC not settled by this screen |
| {123,231}; {123,312} | Proposition 3.12: degree at most one; LC follows |
| {132,321}; {213,321} | Proposition 3.13: degree at most one; LC follows |
| {231,312} | Proposition 3.14: constant polynomials; LC follows |
| {123,321} | Proposition 3.15: explicit finite polynomial; LC follows |

The exact immediate arguments are in evidence/triage/route.md. They cover
13 families without new research; the other eight occupy four classes.
These implications are prior-result consequences, not new contributions.
In particular, no uninspected claim about 123 real-rootedness is needed.

## Nearest prior result and proposed contribution

For the exceptional class the source proves

    sum_{n>=0} B_n(t) x^n
      = [1-x+(1-t)x^2-(1-t)^2 x^3]
        /[1-2x+(1-t)x^2+t(1-t)x^3].

Its B_n, for n>=1, counts binary words of length n ending in 1, weighted
by the number of consecutive 10 factors plus consecutive 011 factors.
This class is excluded from the source's real-rootedness Conjecture 4.4,
but included in the original log-concavity Conjecture 4.6.

Nearest prior result X: that bijection and rational generating function.
Proposed delta Y: uniform coefficient log-concavity for these three pairs.
Verification route Z: a closed induction for suffix-state coefficient
determinants, with exact falsification of proposed auxiliary inequalities.
A successful theorem in that scope would be only a partial result on the
frozen original; it would require novelty review and a fresh referee.

A run decomposition derived in this triage gives, for n>=1 and k>=0,

    b[n,k] = sum_{r=0}^{n-1} C(r+1,k+1-r) C(n-r-1,k),

where C(a,b)=0 unless 0<=b<=a. Its derivation, positive suffix recurrence,
exact checks, and one failed sufficient condition are in
 evidence/triage/route.md and evidence/triage/positive_formula.json.
This is a reformulation of known enumeration, not itself a novel theorem.

## Research pass 1: changed evidence and route

Job: primary-20260914-bigdescent-logconcavity-research-ff87ce2dd87c.
Workflow: continue; candidate_kind=none; original_status=unresolved.
The full 21-family original is unchanged. No fresh referee or manuscript exists.

The suggested suffix induction has a proved limitation. No cone containing
(1+t,1,1), closed under common positive substitution t -> c t and under the
suffix transfer, can require all C states to be LC. Taking c=5 and two
transfers gives C=(1,2,5), with determinant -1. This is outside the actual
orbit and does not refute original LC. Strong synchronization of C and tB
also fails at actual n=4, k=1. The nine determinant recurrences and exact
witnesses are in evidence/research/suffix-determinants.md,
evidence/research/scale-obstruction.md, and
 evidence/research/suffix_diagnostics.json.

A new route keeps separate variables z_i for events ending at position i.
Let f[n,k](z) sum product_{i in E(w)} z_i over binary words ending in 1
with k factors of type 10 or 011. The working stronger assertion is
coefficientwise nonnegativity of f[n,k](z)^2-f[n,k-1](z)f[n,k+1](z),
for every n and k. It would imply LC for arbitrary nonnegative position
weights in the exceptional class; it leaves the other source classes
as obligations for a complete original resolution.

The no-event matrix P satisfies P^2=P. In the tensor transfer for ordered
word pairs, this lets each nonempty zero block of an exponent profile
be replaced by one zero. A profile of total degree 2k then has length
at most 4k+1. This yields a finite reduction for each fixed k, proved in
 evidence/research/profile-reduction.md. The exact profile_test.py checks
all 2,350,932 compressed profiles for 1<=k<=7, with no negative coefficient.
Together with the reduction, this gives coefficientwise LC at those seven
indices for every n. It is not a proof for arbitrary k or a novelty claim.

A different deterministic implementation compares the tensor coefficients
and compression to direct word-pair enumeration for every n<=9 (9,841
ternary profiles, 83,653 scalar coefficients). A held-out periodic suite
contains 695 profiles of degree >=16, including 268 with nonzero counts;
none violates Schur positivity. These are same-worker cross-checks, not
a fresh referee. Exact scope: evidence/research/profile_audit.json.
Literature comparison and limitations: literature/research-pass-1.md.

One next test: on all compressed profiles of total degree at most 14,
including odd degrees, test the stronger Schur-positivity inequalities
h_j>=h_{j-1} for the pair-profile scalar H_e(x,y), 1<=j<=floor(|e|/2).
If they survive, derive a closed Schur-positive block recurrence from
R_0,R_1,R_2 using P^2=P and the Fibonacci/projector maps on im(P).
An exact failed coefficient rejects that stronger proof premise. Extending
full unweighted rows alone is not the next test.

## Research pass 2: Schur reduction and a sharp two-position theorem

Job: primary-20260914-bigdescent-logconcavity-research-6ff0786c2423.
Workflow: continue; candidate_kind=none; original_status=unresolved.
The original 21-family assertion and the precise interpretation above remain
unchanged. No qualified candidate, fresh referee, or manuscript is claimed.

The requested exhaustive Schur test succeeded for all compressed profiles of
total degree 0..14, including odd degrees: 3,211,434 profiles and 21,122,732
nontrivial inequalities, with exact integer coefficients. The formula counting
the complete finite domain agrees with the enumeration. The code and report
are evidence/research/schur_profiles.py and schur_profiles.json.

There is now an exact contextual block identity. With R=R1, q=xy, s=x+y,
and h2=x^2+xy+y^2,

    R^8=q R^6+q s R^5+5q^2 R^4+2q^2 s R^3+q^2 h2 R^2+q^3 s R.

Every multiplier is Schur-positive. Thus a run of eight 1s reduces to shorter
runs in arbitrary context. The identities R2^3=0 and R2 R1 R2=0 eliminate
profiles containing 222 or 212. All profiles consisting of one run of 1s,
with arbitrary boundary zeros, are Schur-positive at every degree by 32
base cases and the recurrence. The reduced mixed-profile language remains
infinite. Proof and exact certificates: evidence/research/schur-block-reduction.md,
schur_blocks.py, and schur_blocks.json. At profile (1,0,1), CC=x^2+y^2,
whereas H=2(x^2+xy+y^2): statewise Schur positivity and scalar gamma
positivity both fail as proposed stronger premises.

A uniform subsidiary theorem is proved. Let a_n(S) count the binary words
ending in 1 with event set exactly S. For distinct i,j outside S,

    a_n(S) a_n(S union {i,j})
        <= 2 a_n(S union {i}) a_n(S union {j}).

The factor 2 is sharp at n=4, S=empty, {i,j}={2,4}, where the four counts
are (2,1,1,1). The proof reduces arbitrary intervening P,Q products to rank
one or five alternating matrix families. An exact nonnegative coefficient
certificate checks all 1,300 polynomial coefficients in nonnegative boundary
and matrix-family parameters; a separate symbolic expansion agrees.
Consequently every pair profile with at most two entries equal to 1 is
Schur-positive, with arbitrarily many common events (entries equal to 2).
See evidence/research/two-singleton-theorem.md and
two_singleton_certificate.py/.json. This is an unreviewed research theorem,
not a claimed new publication contribution or a resolution of original LC.

A direct binary-word implementation verifies 18,943 conditional configurations
through n=11 and independently matches 3,280 pair profiles / 24,604 scalar
coefficients through n=8. These are same-worker checks, not a fresh referee.
Exact scope: evidence/research/pass2_audit.py and pass2_audit.json.
Bounded primary comparison and unsearched areas: literature/research-pass-2.md.

One next test: extend the separate-family polynomial certificate to three
and four singly occupied positions, testing every Schur coefficient in
nonnegative boundary-ray and gap parameters. Rank-one gaps split into
lower-singleton cases; the remaining gaps use the five alternating families.
A negative parameter coefficient refutes that proof premise, not necessarily
an actual-word inequality. Do not replace the separate families by their
whole positive hull: the latter has an exact counterexample in the theorem
dossier.

## Research pass 3: conditional coefficientwise LC with four free positions

Job: primary-20260914-bigdescent-logconcavity-research-5c6b908e3ed6.
Proposed workflow: candidate for a result-note; original_status=unresolved.
The frozen original and its precise 21-family interpretation are unchanged.
No fresh referee, mathematical acceptance, or manuscript is claimed.

Let a_n(S) count length-n binary words ending in 1 with exact event set S,
where events are the ending positions of factors 10 and 011. For n>=1,
J subset {2,...,n} with |J|=m<=4, and S subset {2,...,n} minus J, define

    H_(S,J)(x,y)=sum_(T subset J) a_n(S union T)
                 a_n(S union (J minus T)) x^|T| y^(m-|T|).

The submitted partial theorem is that H_(S,J) is Schur-positive for every
such choice, with no bound on n, |S|, or spacing. Equivalently, its
coefficients h_j are symmetric and h_j>=h_(j-1) for 1<=j<=floor(m/2).
For fixed S,J, writing

    G(t;z)=sum_(T subset J) a_n(S union T) t^|T| product_(i in T)z_i
           =sum_k g_k(z)t^k,

every g_k^2-g_(k-1)g_(k+1) has nonnegative monomial coefficients. Hence
the conditional count polynomial is LC under arbitrary nonnegative weights
on its <=4 free event positions. The restriction is on binary-word event
positions, not the positions of big descents in the source permutation.

The requested polynomial extension succeeded for all separate gap-family
combinations: 33,800 coefficient positions for m=3 and 659,100 for m=4,
with no negative coefficient. The m=2 case was also recomputed at all
2,600 positions, now including its automatically nonnegative first Schur
row. These are exact coefficient certificates in nonnegative real parameters,
not finite samples of word lengths or gap lengths. Rank-one gaps have the
explicit factorization A Q^2 B=(A e0)(e1^T B); its factors lie in the
required boundary cones, so induction and Schur-positive products handle
every such gap. The proof is evidence/research/four-singleton-theorem.md.

A separate tensor implementation matches all 695,500 certificate positions
and independently checks the cone and alternating-word identities. Direct
binary words check all 72,447 fixed/free configurations with <=4 free sites
through n=11 (152,573 Schur coefficient positions). The scripts and reports
are evidence/research/multi_singleton_certificate.py/.json and
evidence/research/pass3_audit.py/.json. These are same-worker deterministic
cross-checks, not a fresh referee.

The proof also gives Schur positivity at arbitrary singleton count when
rank-one gaps split a profile into components of at most four singletons.
The earlier sharp factor 2 at two positions is included in the theorem.
The extension beyond two positions uses additional word structure: generic
three-coordinate weights 2 on the empty/full sets and 1 elsewhere satisfy
all six factor-two face inequalities but have pair sums (4,3,3,4), which
are not Schur-positive. This generic witness is outside the word model.

Literature comparison is in literature/research-pass-3.md. The source's
decisive primary text is preserved at evidence/external/erz-2026-primary.txt
and included in the candidate evidence. Kahn–Neiman's normalized CAPP
criterion was inspected in the live primary paper; its two-coordinate
hypothesis fails on the actual sharp word example, so it does not directly
prove this result. No priority or exhaustive literature claim is made.

The entire original, and even unrestricted exceptional-class LC, remain
unresolved by this work. The four-position cutoff is not claimed optimal.
One next test: a fresh referee should recompute the finite certificate and
audit the rank-one boundary factorization and coefficientwise-LC corollary,
then assess the precise conditional theorem's contribution against the
primary source and antipodal-pairs literature. Do not widen the candidate
to unrestricted free positions or to all 21 original families.
