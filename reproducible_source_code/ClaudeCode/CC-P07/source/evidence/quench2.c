/* improved solver: connectivity pruning + move ordering option */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef struct { uint64_t a,b; } key;
#define HB 22
#define HS (1u<<HB)
static key tab[HS]; static uint32_t stamp=1; static uint32_t ust[HS];
static int M[64][64];
static inline key mk(const uint8_t*s,int n){ key k={0,0}; for(int i=0;i<n;i++){ if(i<10) k.a|=(uint64_t)(s[i]+1)<<(6*i); else k.b|=(uint64_t)(s[i]+1)<<(6*(i-10)); } k.b|=(uint64_t)n<<58; return k; }
static inline uint32_t hh(key k){ uint64_t h=k.a*0x9E3779B97F4A7C15ULL ^ (k.b+0x632BE59BD9B4E019ULL)*0xC2B2AE3D27D4EB4FULL; return (uint32_t)(h>>(64-HB)); }
static int seen(key k){ uint32_t h=hh(k); while(ust[h]==stamp){ if(tab[h].a==k.a&&tab[h].b==k.b) return 1; h=(h+1)&(HS-1);} return 0; }
static void add(key k){ uint32_t h=hh(k); while(ust[h]==stamp){ if(tab[h].a==k.a&&tab[h].b==k.b) return; h=(h+1)&(HS-1);} ust[h]=stamp; tab[h]=k; }
static long nodes, limit_nodes; static int aborted; int ORDER=0;
static inline int connected(const uint8_t*s,int n){
  /* union-find on 17 nodes: suits 0..3, ranks 4..16 */
  int p[17]; for(int i=0;i<17;i++) p[i]=i;
  #define F(x) ({int _x=(x); while(p[_x]!=_x) _x=p[_x]=p[p[_x]]; _x;})
  int present=0;
  for(int i=0;i<n;i++){ int a=s[i]/13, b=4+s[i]%13; present|=1<<a|1<<b; int ra=F(a), rb=F(b); if(ra!=rb) p[ra]=rb; }
  int root=-1;
  for(int i=0;i<17;i++) if(present>>i&1){ int r=F(i); if(root<0) root=r; else if(r!=root) return 0; }
  return 1;
}
static int ql(uint8_t*s,int n){
  if(n==1) return 1;
  if(nodes>limit_nodes){ aborted=1; return 0; }
  key k=mk(s,n); if(seen(k)) return 0;
  nodes++;
  if(!connected(s,n)){ add(k); return 0; }
  uint8_t t[20];
  if(ORDER==0){
    for(int i=0;i+1<n;i++) if(M[s[i]][s[i+1]]){ memcpy(t,s,i); memcpy(t+i,s+i+1,n-i-1); if(ql(t,n-1)) return 1; if(aborted) return 0; }
    for(int l=0;l+3<n;l++) if(M[s[l]][s[l+3]]){ memcpy(t,s,n); t[l]=s[l+3]; memmove(t+l+3,s+l+4,n-l-4); if(ql(t,n-1)) return 1; if(aborted) return 0; }
  } else {
    for(int i=n-2;i>=0;i--){
      if(M[s[i]][s[i+1]]){ memcpy(t,s,i); memcpy(t+i,s+i+1,n-i-1); if(ql(t,n-1)) return 1; if(aborted) return 0; }
      if(i+3<n && M[s[i]][s[i+3]]){ memcpy(t,s,n); t[i]=s[i+3]; memmove(t+i+3,s+i+4,n-i-4); if(ql(t,n-1)) return 1; if(aborted) return 0; }
    }
  }
  add(k); return 0;
}
int solve_limited(uint8_t*s,int n,long lim){ stamp++; if(stamp==0){memset(ust,0,sizeof ust);stamp=1;} nodes=0; limit_nodes=lim; aborted=0; return ql(s,n); }
void init_match(){ for(int a=0;a<52;a++) for(int b=0;b<52;b++) M[a][b]=(a/13==b/13)||(a%13==b%13); }
#ifndef LIB
static uint64_t rs=88172645463325252ULL;
static inline uint64_t rnd(){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
int main(int argc,char**argv){ init_match(); ORDER=atoi(argv[1]); long hist[12]={0}; int wins=0,N=20000; long totn=0;
  for(int d=0;d<N;d++){ int deck[52]; for(int i=0;i<52;i++) deck[i]=i;
    for(int i=0;i<18;i++){ int j=i+rnd()%(52-i); int x=deck[i]; deck[i]=deck[j]; deck[j]=x; }
    uint8_t s[20]; for(int i=0;i<18;i++) s[i]=deck[i];
    int w=solve_limited(s,18,1L<<40); totn+=nodes;
    if(w){ wins++; int b=0; long x=nodes; while(x>1){x/=4;b++;} if(b>11)b=11; hist[b]++; } }
  printf("order %d: wins %d/%d, avg nodes %.0f |",ORDER,wins,N,(double)totn/N);
  for(int b=0;b<12;b++) printf(" %ld",hist[b]); printf("\n");
}
#endif
