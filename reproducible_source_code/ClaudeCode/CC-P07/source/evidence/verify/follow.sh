#!/bin/bash
# follow.sh: verify new records in rounds (4 procs) while the witness run is in
# progress; once all ten lbw9 logs report completion, verify the rest (6 procs)
# and run final_check.sh.
cd "$(dirname "$0")/.." || exit 1
r=1
while true; do
  c=0; for i in 0 1 2 3 4 5 6 7 8 9; do grep -q '^K=9 proc' logs/lbw9_p$i.log 2>/dev/null && c=$((c+1)); done
  [ $c -eq 10 ] && break
  t0=$(date +%s)
  ./verify/phase.sh R$r 4; r=$((r+1))
  el=$(( $(date +%s) - t0 )); [ $el -lt 300 ] && sleep $((300-el))
done
sleep 5
./verify/phase.sh FINAL 6
./verify/final_check.sh
