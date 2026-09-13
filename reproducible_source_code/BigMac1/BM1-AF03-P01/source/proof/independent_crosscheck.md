# Independent structural cross-check for the \(n=9\) proof

This route is not needed by `main_proof.md`; it was developed independently
and checks the delicate five-point structure by a different decomposition.

Fix \(E\in\mathcal F\), put \(X=[9]\setminus E\), and define \(C(T)\) as
in the main proof.  For each \(e\in E\), let
\[
 A_e=\{x\in X:(E\setminus\{e\})\cup\{x\}\in\mathcal F\}.
\]
Every \(A_e\) is nonempty.  Intersectingness gives
\(e\in C(T)\Rightarrow A_e\subseteq T\).  Hence every triple of the
five-set \(X\) wholly contains at least two of the four sets \(A_e\).
Choosing one transversal point from each \(A_e\) and applying the complement
pair argument from the main proof shows that every transversal is injective.
Thus the four \(A_e\) are pairwise disjoint.  Since they are nonempty subsets
of a five-set, the sum of the sizes of any two is at most three.

For each two-set \(I\subset E\), define a graph \(G_I\) on \(X\) by
\[
 xy\in G_I \quad\Longleftrightarrow\quad I\cup\{x,y\}\in\mathcal F.
\]
These six graphs are edge-disjoint.  Indeed, if \(P=\{x,y\}\in G_I\) and
\(T=X\setminus P\), every \(e\in C(T)\) must lie in \(I\), or else
\(T\cup\{e\}\) and \(I\cup P\) would be disjoint.  Since \(|C(T)|\ge2\),
we obtain \(C(T)=I\), uniquely determining \(I\) from \(P\).

For \(I\in\binom E2\), \(x\in X\), and \(J=E\setminus I\), direct
classification of the fourth vertex gives the exact identity
\[
 d_{\mathcal F}(I\cup\{x\})
 =\deg_{G_I}(x)+\sum_{e\in J}\mathbf 1_{x\in A_e}.
\]
Summing over the five vertices and using the pairwise-disjoint size bound,
\[
 10\le2|G_I|+\sum_{e\in J}|A_e|\le2|G_I|+3,
\]
so every \(G_I\) has at least four edges.  Six edge-disjoint graphs would
then require at least 24 distinct edges on a five-vertex set, which has only
10.  This is a second contradiction.

As an adversarial finite check of only the auxiliary forcing-set lemma, all
\(31^4\) ordered quadruples of nonempty subsets of a five-set were enumerated.
Exactly 360 satisfy the triple-containment premise; every survivor is
pairwise disjoint and has size pattern \((1,1,1,1)\) or \((1,1,1,2)\).
This enumeration is diagnostic support, not a dependency of either proof.
