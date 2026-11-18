#!/bin/bash
# phase.sh TAG NPROC : verify, for each witness9 file, the records not yet
# verified (from the last verified end to the current number of complete
# records); stores the prefix sha256 so later phases can check it is unchanged.
# Works with relative paths from the poison folder (its absolute path has spaces).
cd "$(dirname "$0")/.." || exit 1
TAG=$1; NP=${2:-4}; CH=500000
: > verify/k9/jobs_$TAG.txt
for i in 0 1 2 3 4 5 6 7 8 9; do
  f=witness9/p$i.bin
  sz=$(stat -f %z "$f"); n=$((sz/18))
  start=0; [ -f verify/k9/end_p$i ] && start=$(cat verify/k9/end_p$i)
  [ $n -le $start ] && continue
  sha=$(head -c $((n*18)) "$f" | shasum -a 256 | cut -d' ' -f1)
  echo "$i $n $sha" >> verify/k9/prefix_sha_$TAG.txt
  lo=$start
  while [ $lo -lt $n ]; do hi=$((lo+CH)); [ $hi -gt $n ] && hi=$n
    echo "$f $lo $hi verify/k9/codes_p${i}_${lo}_${hi}.bin verify/k9/out_p${i}_${lo}_${hi}.txt" >> verify/k9/jobs_$TAG.txt; lo=$hi; done
  echo $n > verify/k9/end_p$i
done
xargs -P $NP -L 1 sh -c 'nice -n 5 ./verify/verify 9 $0 $1 $2 $3 > $4' < verify/k9/jobs_$TAG.txt
echo "phase $TAG done $(date)"
