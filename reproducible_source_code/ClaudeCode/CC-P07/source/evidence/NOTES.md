# Ross's poison cards in Late Binding solitaire (TAOCP 7.2.2.2-486; Ross & Knuth STAN-CS-89-1269, 1989)
Question (answer 486, "still unsolved"): is there a sequence of (say) nine poison cards, i.e. a 9-card prefix such
that every 18-card game starting with it is lost? KAR (1989) asked for the minimum length n; the seminar believed
n <= 17 and that n <= 15 might be provable.

## Tools
- quench.c / quench2.c: memoized DFS solver (quench2 adds suit-rank connectivity pruning: a disconnected
  suit/rank graph of the current tops can never be reduced). Checks: Knuth's example deal is winnable, and not after
  A-clubs x J-clubs or A-clubs xx 10-clubs (as in answer 486); 9279/20000 = 46.4% random deals winnable
  (Gent et al. 2024: 47.0%, Knuth 1989/2015: 44.3% of 10000). SAT encoding (lb.py, Knuth's ex. 484 clauses) agrees
  with DFS on 60/60 random deals.
- patcount.c: canonical prefix patterns (suits and ranks relabelled in order of first appearance):
  k=1..10: 1, 3, 15, 113, 1101, 12657, 162863, 2281239, 34260563, 546727587.
- lbsearch.c: for every pattern of length K, random and greedy-matching completions with node-limited search until
  a win; prints HARD patterns. lbsearch_w.c also writes the winning 18-card deals (witnesses).
- penum.c: exhaustive poison test for long prefixes (all ordered completions).

## Results
- 2026-11-18: K=9, seed 2026, 10 processes: all 34,260,563 patterns have a winning completion (HARD = 0).
  => NO 9-card poison sequence exists (answers Ross's question as posed in answer 486). So 10 <= n.
- Poison prefixes of length 16 exist (random sampling: ~0.5% of random 16-prefixes; each checked against all
  36*35 = 1260 completions), e.g. 33 8 34 17 46 9 41 40 37 29 24 22 44 11 12 26. So n <= 16.
- Rerun with witnesses: K=9, seed 7, witness9/p*.bin (18-byte deals); independent verifier being written by a
  separate agent in verify/.
- 2026-11-18 ~23:00: hill climbing (hc.c: minimize wins over 200 random completions, then 2000, then exhaustive over
  all ordered completions) found two 15-card poison prefixes within a minute (46,620 completions each lose):
  8D 6S 9D 5H 8C TS 3C KD 7H 4D QH KS JH 4C AS   and   3H 4S 9C QS 7C JH 9D TS 4D 3C 2H KC 6D 5D JS. So n <= 15.
- 2026-11-18 ~23:15: a 14-card poison prefix (all 1,771,560 ordered completions lose):
  card numbers 45 2 42 15 46 11 39 8 22 27 43 12 23 31 (see poison_found.txt). So n <= 14.
- 2026-11-19 ~00:40: witness rerun (seed 7) complete: 34,260,563 patterns, HARD 0, deals stored in witness9/ (617 MB).
  Independent verifier (separate agent, own solver) running in verify/.
- 13-card search: random-start climbs plateau at ~1e-3 win rate; climbs restricted to "frozen" prefixes (no internal
  capture at distance 1 or 3, like the 14-card poison) started (hc4.c). Two 13-card candidates passed a 20000-sample
  screen but exhaustive checks found wins (612,807th and 151,826th completions).
- 2026-11-19 ~01:05: K=10 lower-bound run with witnesses started (6 procs, nice 10, seed 101, witness10/).
- Novelty: Blake & Gent (JAIR 85, 2026; arXiv:1906.12314) treat Late Binding (47.021%) but not poison cards; no
  other source found.
- 2026-11-19 ~01:40: 13-card POISON prefix (all 69,090,840 completions lose, pexh on 6 procs):
  30 19 28 18 3 39 8 50 12 49 14 33 22 = 5D 7H 3D 6H 4S AC 9S QC KS JC 2H 8D TH (frozen; found by hc4 frozen climb,
  200000-sample screen 0 wins). So 10 <= n* <= 13. Sent to the independent verifier for confirmation.
  Independent verifier (verify/report.txt): k=9 evidence fully confirmed; 14- and 15-card prefixes confirmed poison.
  Verifier remark: Knuth's "4432 of 10000" (answer 486) is ~5 sigma below the true ~47% win rate.
