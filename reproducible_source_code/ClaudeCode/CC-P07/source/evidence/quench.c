/* Late Binding solitaire solver (graph quenching), memoized DFS.
   stdin: lines of 18 (or n) card numbers 0..51 (suit=c/13, rank=c%13); output: 1/0 per line. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef struct { uint64_t a,b; } key;
#define HB 22
#define HS (1u<<HB)
static key tab[HS]; static uint8_t used[HS]; static uint32_t stamp=1; static uint32_t ust[HS];
static int M[64][64];
static inline key mk(const uint8_t*s,int n){ key k={0,0}; for(int i=0;i<n;i++){ if(i<10) k.a|=(uint64_t)(s[i]+1)<<(6*i); else k.b|=(uint64_t)(s[i]+1)<<(6*(i-10)); } k.b|=(uint64_t)n<<58; return k; }
static inline uint32_t hh(key k){ uint64_t h=k.a*0x9E3779B97F4A7C15ULL ^ (k.b+0x632BE59BD9B4E019ULL)*0xC2B2AE3D27D4EB4FULL; return (uint32_t)(h>>(64-HB)); }
static int seen(key k){ uint32_t h=hh(k); while(ust[h]==stamp){ if(tab[h].a==k.a&&tab[h].b==k.b) return 1; h=(h+1)&(HS-1);} return 0; }
static void add(key k){ uint32_t h=hh(k); while(ust[h]==stamp){ if(tab[h].a==k.a&&tab[h].b==k.b) return; h=(h+1)&(HS-1);} ust[h]=stamp; tab[h]=k; }
static long nodes;
static int q(uint8_t*s,int n){
  if(n==1) return 1;
  key k=mk(s,n); if(seen(k)) return 0;
  nodes++;
  uint8_t t[20];
  for(int i=0;i+1<n;i++) if(M[s[i]][s[i+1]]){
    memcpy(t,s,i); memcpy(t+i,s+i+1,n-i-1); if(q(t,n-1)) return 1; }
  for(int l=0;l+3<n;l++) if(M[s[l]][s[l+3]]){
    memcpy(t,s,n); t[l]=s[l+3]; memmove(t+l+3,s+l+4,n-l-4); if(q(t,n-1)) return 1; }
  add(k); return 0;
}
int quench_seq(uint8_t*s,int n){ stamp++; if(stamp==0){memset(ust,0,sizeof ust);stamp=1;} return q(s,n); }
void init_match(){ for(int a=0;a<52;a++) for(int b=0;b<52;b++) M[a][b]=(a/13==b/13)||(a%13==b%13); }
#ifndef LIB
int main(){ init_match(); uint8_t s[20]; int n=0; int x; char line[512];
  while(fgets(line,sizeof line,stdin)){ n=0; char*p=line; int off; while(sscanf(p,"%d%n",&x,&off)==1){ s[n++]=x; p+=off; }
    if(n==0) continue; printf("%d\n",quench_seq(s,n)); }
  return 0; }
#endif
