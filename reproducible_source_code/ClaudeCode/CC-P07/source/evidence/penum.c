/* Exhaustive poison test for long prefixes: try every ordered completion to 18 cards; stop at the first win.
   usage: penum k nsamples seed  -> samples random prefixes of length k taken from random deals */
#define LIB
#include "quench.c"
static uint64_t rs;
static inline uint64_t rnd(){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
static uint8_t seq[20]; static int inuse[52]; static long tried;
static int K;
static int rec(int p){
  if(p==18){ tried++; uint8_t t[20]; memcpy(t,seq,18); return quench_seq(t,18); }
  int order[52],m=0; for(int c=0;c<52;c++) if(!inuse[c]) order[m++]=c;
  for(int i=m-1;i>0;i--){ int j=rnd()%(i+1); int x=order[i]; order[i]=order[j]; order[j]=x; }
  for(int i=0;i<m;i++){ int c=order[i]; inuse[c]=1; seq[p]=c; int w=rec(p+1); inuse[c]=0; if(w) return 1; }
  return 0;
}
int main(int argc,char**argv){
  init_match(); K=atoi(argv[1]); int ns=atoi(argv[2]); rs=atoll(argv[3])*7919+17;
  int poison=0;
  for(int s=0;s<ns;s++){
    int deck[52]; for(int i=0;i<52;i++) deck[i]=i;
    for(int i=51;i>0;i--){ int j=rnd()%(i+1); int x=deck[i]; deck[i]=deck[j]; deck[j]=x; }
    memset(inuse,0,sizeof inuse); for(int i=0;i<K;i++){ seq[i]=deck[i]; inuse[deck[i]]=1; }
    tried=0; int w=rec(K);
    if(!w){ poison++; printf("POISON k=%d:",K); for(int i=0;i<K;i++) printf(" %d",seq[i]); printf("  (completions %ld)\n",tried); fflush(stdout); }
  }
  printf("k=%d: %d poison of %d random prefixes\n",K,poison,ns);
  return 0;
}
