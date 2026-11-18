/* count canonical prefix patterns (suit classes and rank classes in restricted-growth order, no repeated card) */
#include <stdio.h>
#include <stdlib.h>
int K; long cnt[20]; int su[20], ra[20], rcnt[20], used[4][13];
void rec(int p,int ns,int nr){
  cnt[p]++;
  if(p==K) return;
  for(int s=0;s<=ns && s<4;s++) for(int r=0;r<=nr && r<13;r++){
    if(used[s][r]) continue; if(rcnt[r]>=4) continue;
    used[s][r]=1; rcnt[r]++; rec(p+1, ns+(s==ns), nr+(r==nr)); used[s][r]=0; rcnt[r]--;
  }
}
int main(int argc,char**argv){ K=atoi(argv[1]); rec(0,0,0); for(int k=1;k<=K;k++) printf("k=%d: %ld patterns\n",k,cnt[k]); }
