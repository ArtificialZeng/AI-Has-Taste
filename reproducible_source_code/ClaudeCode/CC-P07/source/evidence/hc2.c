/* Hill climbing for poison prefixes of length K, followed by an exhaustive check.
   usage: hc K seed iters [start cards...] */
#define LIB
#include "quench2.c"
static uint64_t rs;
static inline uint64_t rnd(){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
int K;
static int sample_wins(uint8_t*P,int N,long lim,uint64_t seed){
  uint64_t save=rs; rs=seed; int inp[52]={0}; for(int i=0;i<K;i++) inp[P[i]]=1;
  int avail[52],m=0; for(int c=0;c<52;c++) if(!inp[c]) avail[m++]=c;
  int wins=0; uint8_t s[20]; memcpy(s,P,K);
  for(int t=0;t<N;t++){
    for(int i=0;i<18-K;i++){ int j=i+rnd()%(m-i); int x=avail[i]; avail[i]=avail[j]; avail[j]=x; s[K+i]=avail[i]; }
    if(solve_limited(s,18,lim)) wins++;
  }
  rs=save; return wins;
}
static long exh_count; static int exh_win;
static uint8_t es[20]; static int einp[52];
static void exh(int p){
  if(exh_win) return;
  if(p==18){ exh_count++; if(solve_limited(es,18,1L<<40)) exh_win=1; return; }
  for(int c=0;c<52 && !exh_win;c++) if(!einp[c]){ einp[c]=1; es[p]=c; exh(p+1); einp[c]=0; }
}
static int exhaustive(uint8_t*P){ memset(einp,0,sizeof einp); for(int i=0;i<K;i++){ es[i]=P[i]; einp[P[i]]=1; } exh_count=0; exh_win=0; exh(K); return !exh_win; }
int main(int argc,char**argv){
  init_match(); K=atoi(argv[1]); rs=atoll(argv[2])*2654435761ULL+11; long iters=atol(argv[3]);
  uint8_t P[20]; int inp[52]={0};
  if(argc>4+K-1){ for(int i=0;i<K;i++){ P[i]=atoi(argv[4+i]); inp[P[i]]=1; } }
  else { for(int i=0;i<K;i++){ int c; do c=rnd()%52; while(inp[c]); inp[c]=1; P[i]=c; } }
  int N=200; uint64_t sseed=12345;
  int cur=sample_wins(P,N,20000,sseed);
  for(long it=0;it<iters;it++){
    int i=rnd()%K, old=P[i], c; do c=rnd()%52; while(inp[c]);
    P[i]=c; inp[old]=0; inp[c]=1;
    int sc=sample_wins(P,N,20000,sseed);
    if(sc<=cur || rnd()%100==0){ cur=sc; } else { P[i]=old; inp[c]=0; inp[old]=1; }
    if(it%200==0){ printf("it %ld score %d/%d :",it,cur,N); for(int j=0;j<K;j++) printf(" %d",P[j]); printf("\n"); fflush(stdout); }
    if(cur==0){
      int big=sample_wins(P,2000,200000,sseed^0xabcdef);
      printf("candidate (2000-sample wins %d):",big); for(int j=0;j<K;j++) printf(" %d",P[j]); printf("\n"); fflush(stdout);
      if(big==0 && K<=13){ int huge=sample_wins(P,20000,2000000,sseed^0x5555); printf("CANDIDATE13 (20000-sample wins %d):",huge); for(int j=0;j<K;j++) printf(" %d",P[j]); printf("\n"); fflush(stdout); if(huge==0) return 0; }
      else if(big==0){
        int pz=exhaustive(P);
        printf("EXHAUSTIVE %s after %ld completions:",pz?"POISON":"not poison",exh_count); for(int j=0;j<K;j++) printf(" %d",P[j]); printf("\n"); fflush(stdout);
        if(pz) return 0;
      }
      sseed=rnd(); cur=sample_wins(P,N,20000,sseed);
    }
  }
  return 0;
}
