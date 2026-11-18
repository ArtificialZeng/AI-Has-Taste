#!/bin/bash
# final_check.sh: after all phases. Checks that every prefix verified in an
# earlier phase is byte-identical now (sha256), that file sizes are whole
# records, aggregates the per-chunk SUMMARY lines, checks chunk ranges tile each
# file exactly, and runs the coverage comparison.
cd "$(dirname "$0")/.." || exit 1
echo "== prefix sha256 re-check"
bad=0
for pf in verify/k9/prefix_sha_*.txt; do
  while read i n sha; do
    now=$(head -c $((n*18)) witness9/p$i.bin | shasum -a 256 | cut -d' ' -f1)
    if [ "$now" != "$sha" ]; then echo "CHANGED: $pf p$i first $n records"; bad=1; fi
  done < "$pf"
done
echo "prefix sha mismatches: $bad"
echo "== file sizes"
tot=0
for i in 0 1 2 3 4 5 6 7 8 9; do
  sz=$(stat -f %z witness9/p$i.bin); echo "p$i: $sz bytes, $((sz/18)) records, remainder $((sz%18)), verified up to $(cat verify/k9/end_p$i)"
  tot=$((tot+sz/18))
done
echo "total records: $tot"
echo "== chunk tiling"
for i in 0 1 2 3 4 5 6 7 8 9; do
  ls verify/k9/out_p${i}_*.txt | sed -E 's/.*_p[0-9]+_([0-9]+)_([0-9]+)\.txt/\1 \2/' | sort -n | \
   awk -v i=$i -v end=$(cat verify/k9/end_p$i) 'BEGIN{e=0;ok=1} {if($1!=e) ok=0; e=$2} END{if(e!=end) ok=0; print "p" i ": chunks tile [0," e ") " (ok?"OK":"GAP/OVERLAP")}'
done
echo "== aggregated SUMMARY lines"
cat verify/k9/out_*.txt | grep -v '^SUMMARY' | head -20
cat verify/k9/out_*.txt | grep '^SUMMARY' | awk '{for(i=2;i<=NF;i++){split($i,a,"="); v[a[1]]+=a[2]; if(a[1]=="maxnodes" && a[2]+0>mx) mx=a[2]+0}} END{printf "chunks=%d records=%d sentinel=%d invalid=%d winnable=%d notwinnable=%d prefix_literally_canonical=%d nodes=%.0f maxnodes=%d tablefull=%d cpu=%.0fs\n", NR, v["records"], v["sentinel"], v["invalid"], v["winnable"], v["notwinnable"], v["prefix_literally_canonical"], v["nodes"], mx, v["tablefull"], v["cpu"]}'
echo "== coverage"
./verify/cover 9 verify/k9/codes_*.bin
