# Ehrhart–word identity for arbor polytopes

For every integer n >= 1, let tau be a rooted tree whose vertices are the nonempty blocks of a partition of [n]={1,...,n}. For a vertex v let D(v) be the union of its descendant blocks, including v itself. Define
Q_tau = {x in R^n : x_i >= 0 for every i, and sum_(i in D(v)) x_i <= |D(v)| for every vertex v}.
Define h*(Q_tau,t) by
sum_(m>=0) |m Q_tau intersect Z^n| t^m = h*(Q_tau,t)/(1-t)^(n+1).

Let W_tau consist of all length-n words over [n] for which, for every vertex v, the total number of occurrences of letters from D(v) is at least |D(v)|. Repetitions are allowed. Let des(w)=|{i:1<=i<n, w_i>w_(i+1)}| with the usual total order on [n].

Prove or disprove, for every such n and tau, the polynomial identity
h*(Q_tau,t) = sum_(w in W_tau) t^(n-1-des(w)).

Primary source: C. A. Athanasiadis, Q. Xiao and X. Yan, Lattice point enumeration of some arbor polytopes, arXiv:2603.11654v1, Conjecture 5.2, printed page 13.
https://arxiv.org/html/2603.11654v1
https://arxiv.org/pdf/2603.11654v1

This is a faithful mathematical transcription with explicit definitions, not a browser-generated batch and not a claim of worldwide current open status. The full PDF/HTML is preserved separately. The original asks for all arbors, not just chains, stars, a bounded size range, or a support-polynomial property.
