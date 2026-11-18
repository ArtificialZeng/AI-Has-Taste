/* For every canonical prefix pattern of length K, find a completion to 18 cards that wins.
   usage: lbsearch K nproc procid seed     (patterns are split by their index at depth SPLIT)
   prints HARD lines for patterns where no witness was found, and a summary. */
#define LIB
#include "quench2.c"
static uint64_t rs;
static inline uint64_t rnd(){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
static FILE* WF=NULL; static uint8_t lastwin[20];
int K, NP, PID, SPLIT=4; long patidx=0, done=0, hard=0, tries_total=0;
int su[20], ra[20], rcnt[20], usedc[4][13];
uint8_t pre[20];
static int witness(){
  int avail[52], m=0, inp[52]={0};
  for(int i=0;i<K;i++) inp[pre[i]]=1;
  for(int c=0;c<52;c++) if(!inp[c]) avail[m++]=c;
  uint8_t s[20]; memcpy(s,pre,K);
  long lims[]={3000,3000,3000,3000,20000,20000,200000,5000000};
  for(int t=0;t<400;t++){
    if(t%2==0){ for(int i=0;i<18-K;i++){ int j=i+rnd()%(m-i); int x=avail[i]; avail[i]=avail[j]; avail[j]=x; s[K+i]=avail[i]; } }
    else {  /* greedy-matching completion: prefer cards that match the card 1 or 3 positions to the left */
      for(int i=0;i<18-K;i++){
        int p=K+i, cand[52], nc=0;
        for(int a=i;a<m;a++){ int c=avail[a]; if(M[c][s[p-1]] || (p>=3 && M[c][s[p-3]])) cand[nc++]=a; }
        int a = nc? cand[rnd()%nc] : i+rnd()%(m-i);
        int x=avail[i]; avail[i]=avail[a]; avail[a]=x; s[p]=avail[i];
      }
    }
    tries_total++;
    long lim = t<8? lims[t] : (t<100? 50000 : 5000000);
    if(solve_limited(s,18,lim)){ memcpy(lastwin,s,18); return 1; }
  }
  return 0;
}
void rec(int p,int ns,int nr){
  if(p==SPLIT && K>SPLIT){ long id=patidx++; if(id%NP!=PID) return; }
  if(p==K){
    if(K<=SPLIT){ long id=patidx++; if(id%NP!=PID) return; }
    done++;
    int w_=witness(); if(w_ && WF) fwrite(lastwin,1,18,WF);
    if(!w_){ hard++; if(WF){ uint8_t z[20]; memset(z,255,sizeof z); fwrite(z,1,18,WF);}  printf("HARD"); for(int i=0;i<K;i++) printf(" %d",pre[i]); printf("\n"); fflush(stdout); }
    return;
  }
  for(int s=0;s<=ns && s<4;s++) for(int r=0;r<=nr && r<13;r++){
    if(usedc[s][r]||rcnt[r]>=4) continue;
    usedc[s][r]=1; rcnt[r]++; pre[p]=13*s+r;
    rec(p+1, ns+(s==ns), nr+(r==nr));
    usedc[s][r]=0; rcnt[r]--;
  }
}
int main(int argc,char**argv){
  init_match(); K=atoi(argv[1]); NP=atoi(argv[2]); PID=atoi(argv[3]); rs=atoll(argv[4])*2654435761ULL+PID*97+1;
  if(argc>5) WF=fopen(argv[5],"wb");
  rec(0,0,0);
  if(WF) fclose(WF);
  printf("K=%d proc %d/%d: patterns %ld, hard %ld, completions tried %ld\n",K,PID,NP,done,hard,tries_total);
  return 0;
}
