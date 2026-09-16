# Exact finite test and structural lead

Job: newwin-00001-p02-triage-ba81b5c3d443. Date: 2026-09-12.

## Complete finite count

Run `python3 evidence/exact_spectrum.py --max-n 10` from the project root. Python 3 and NumPy were available and the run completed. Results are in `exact-spectrum.json`.

For every 1<=n<=10 the program constructs the set F_n of complete truth tables. F_1 contains the identity table (0,1,2). For every root split k and every pair f in F_k, g in F_(n-k), it adds the table (x,y) -> f(x)*g(y). By induction on the number of leaves this covers every bracketing. Conversely each pair is realized by a bracketing, so no extraneous functions are introduced. Using one representative per function is valid because equality is preserved by pointwise composition. Input tuples are in lexicographic order, and table entries are integer bytes. Set membership compares entire byte strings, resolving hash collisions by exact equality. Recorded SHA-256 values are reproducibility fingerprints, not the equality test.

Observed spectrum for n=1,...,10:

    1, 1, 2, 5, 12, 28, 65, 151, 351, 816.

This agrees with the proposed recurrence for all 4<=n<=10. At n=10, all 4862 bracketings are covered through 1688 pairs of lower-arity functions; every function table contains all 59049 assignments. A separate scalar evaluation of every raw tree agrees with the complete sets for 1<=n<=7. It uses the same operation table and is a coding crosscheck, not a fresh mathematical referee. These are finite observations only.

## Semantic pruning

Call a term composite if it contains an operation symbol. All composite term values lie in {0,1}, because this is the image of the operation table. On {0,1} the operation is left projection. Therefore for any two composite terms u,v, the identity u*v=u holds as functions on the union of their variables, with the variables of v ignored on the right-hand side.

Define P recursively on an ordered labeled tree t:

- P(x_i)=x_i.
- If t=(u*v) and both original children are composite, set P(t)=P(u).
- Otherwise set P(t)=(P(u)*P(v)).

Keep original leaf labels; deleted variables are not renumbered. Structural induction gives t^A=P(t)^A on the original ambient A^n. Every pruned composite tree still has at least two leaves and every internal node has at least one leaf child. Thus equal pruned trees imply equal functions for all n. The converse has not been proved.

The pilot `python3 evidence/pruned_forms_pilot.py` enumerates all Catalan trees for 2<=n<=8 and compares full truth tables of their distinct pruned trees. The respective counts are 1,2,5,12,28,65,151, with no collision between different pruned labeled trees. See `pruned-forms-pilot.json`. This pilot shares the scalar evaluator with the preceding script.

For a Boolean-valued composite function f, the table gives useful sections:

    x_i*f = 0 if x_i=0, 1 if x_i=1, and 1-f if x_i=2;
    f*x_j = f if x_j is 0 or 1, and 0 if x_j=2.

These formulas suggest reconstructing a pruned tree from restrictions of its function. Ignored gaps and the location/order of these two operations must be handled explicitly. The pruning lemma alone is elementary and is not proposed as a publishable contribution.

## One next test

Prove or refute the separation claim: for every n>=1 and s,t in B_n, if P(s) and P(t) are different labeled trees, then some assignment in A^n distinguishes s^A from t^A. Use the displayed sections to attempt an inductive reconstruction; if it fails, produce an explicit pair and their exact full truth tables. A successful proof would justify counting attainable pruned trees; a counterexample would invalidate this particular normal-form route without necessarily refuting the original recurrence.
