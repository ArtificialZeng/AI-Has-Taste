/* parallel exhaustive poison check: usage pexh nproc pid card1 ... cardK ; splits on the first completion card */
#define LIB
#include "quench2.c"
int K; uint8_t es[20]; int einp[52]; long cnt=0; int win=0;
static void exh(int p){
  if(win) return;
  if(p==18){ cnt++; if(solve_limited(es,18,1L<<40)){ win=1; printf("WIN:"); for(int i=0;i<18;i++) printf(" %d",es[i]); printf("\n"); } return; }
  for(int c=0;c<52 && !win;c++) if(!einp[c]){ einp[c]=1; es[p]=c; exh(p+1); einp[c]=0; }
}
int main(int argc,char**argv){
  init_match(); int np=atoi(argv[1]), pid=atoi(argv[2]); K=argc-3;
  for(int i=0;i<K;i++){ es[i]=atoi(argv[3+i]); einp[es[i]]=1; }
  int idx=0;
  for(int c=0;c<52 && !win;c++) if(!einp[c]){ if(idx++%np!=pid) continue; einp[c]=1; es[K]=c; exh(K+1); einp[c]=0; }
  printf("pid %d/%d: %s, %ld completions checked\n",pid,np,win?"WIN FOUND (not poison)":"all lose",cnt);
  return 0;
}
