/* fast 3-colorability test by backtracking (small graphs). Library-style: reads graph from stdin:
   nv ne, then ne pairs; then queries: k e1..ek  (edges removed); prints 1 if colorable else 0. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int nv, ne, eu[4096], ev[4096], adjn[512], adj[512][16], adje[512][16], removed[4096], col[512], order[512];
static int bt(int p){ if(p==nv) return 1; int v=order[p];
  for(int c=0;c<3;c++){ int ok=1; for(int t=0;t<adjn[v];t++){ int w=adj[v][t]; if(removed[adje[v][t]]) continue; if(col[w]==c){ok=0;break;} }
    if(ok){ col[v]=c; if(bt(p+1)) return 1; col[v]=-1; } if(p==0) break; }
  return 0; }
int main(){ if(scanf("%d %d",&nv,&ne)!=2) return 1;
  for(int i=0;i<ne;i++){ scanf("%d %d",&eu[i],&ev[i]); int u=eu[i],v=ev[i]; adj[u][adjn[u]]=v; adje[u][adjn[u]++]=i; adj[v][adjn[v]]=u; adje[v][adjn[v]++]=i; }
  /* BFS order from 0 */ int seen[512]={0}; int h=0,t=0; order[t++]=0; seen[0]=1; while(h<t){ int v=order[h++]; for(int k=0;k<adjn[v];k++){ int w=adj[v][k]; if(!seen[w]){seen[w]=1;order[t++]=w;} } }
  int k; while(scanf("%d",&k)==1){ memset(removed,0,sizeof removed); for(int i=0;i<k;i++){ int e; scanf("%d",&e); removed[e]=1; }
    for(int i=0;i<nv;i++) col[i]=-1; printf("%d\n", bt(0)); fflush(stdout); }
}
