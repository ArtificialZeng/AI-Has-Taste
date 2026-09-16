/* Exhaustive individualization/refinement canonizer for simple graphs n<=18.
 * Independent of nauty; no automorphism or branch pruning is used.
 * Output: canonical graph6, search-node count, leaf count, automorphism
 * group order (number of leaves attaining the minimum; tab separated).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#define MAXN 18
static int n, adj[MAXN][MAXN], bestset;
static unsigned long long nodes, leaves, automorphisms;
static char best[40];
static int less(int a,int b,int *part,int sig[MAXN][MAXN],int k) {
    if(part[a]!=part[b]) return part[a]<part[b];
    for(int i=0;i<k;i++) if(sig[a][i]!=sig[b][i]) return sig[a][i]<sig[b][i];
    return 0;
}
static int refine(int *part,int k) {
    for(;;) {
        int sig[MAXN][MAXN]={{0}}, order[MAXN], next[MAXN];
        for(int a=0;a<n;a++) {
            order[a]=a;
            for(int b=0;b<n;b++) sig[a][part[b]]+=adj[a][b];
        }
        for(int i=1;i<n;i++) {
            int a=order[i],j=i;
            while(j && less(a,order[j-1],part,sig,k)) {order[j]=order[j-1];j--;}
            order[j]=a;
        }
        int nk=1; next[order[0]]=0;
        for(int i=1;i<n;i++) {
            if(less(order[i-1],order[i],part,sig,k)) nk++;
            next[order[i]]=nk-1;
        }
        memcpy(part,next,n*sizeof(int));
        if(nk==k) return k;
        k=nk;
    }
}
static void search(int *part,int k) {
    nodes++; k=refine(part,k);
    if(k==n) {
        int order[MAXN], t=0,value=0,pos=1;
        char code[40];code[0]=(char)(n+63);
        for(int a=0;a<n;a++) order[part[a]]=a;
        for(int j=1;j<n;j++) for(int i=0;i<j;i++) {
            value=(value<<1)|adj[order[i]][order[j]];t++;
            if(t==6) {code[pos++]=(char)(value+63);t=0;value=0;}
        }
        if(t) code[pos++]=(char)((value<<(6-t))+63);
        code[pos]=0;leaves++;
        if(!bestset || strcmp(code,best)<0) {strcpy(best,code);bestset=1;automorphisms=1;}
        else if(strcmp(code,best)==0) automorphisms++;
        return;
    }
    int size[MAXN]={0},cell=-1;
    for(int a=0;a<n;a++) size[part[a]]++;
    for(int i=0;i<k;i++) if(size[i]>1 && (cell<0 || size[i]<size[cell])) cell=i;
    for(int a=0;a<n;a++) if(part[a]==cell) {
        int child[MAXN];
        for(int b=0;b<n;b++) child[b]=part[b]+(part[b]>cell || (part[b]==cell && b!=a));
        search(child,k+1);
    }
}
int main(void) {
    char line[100];
    while(fgets(line,sizeof line,stdin)) {
        size_t len=strcspn(line,"\r\n");line[len]=0;
        n=(unsigned char)line[0]-63;
        if(n<1 || n>MAXN || len!=(size_t)(1+(n*(n-1)/2+5)/6)) return 2;
        for(size_t i=1;i<len;i++) if(line[i]<63 || line[i]>126) return 3;
        memset(adj,0,sizeof adj);int bit=0;
        for(int j=1;j<n;j++) for(int i=0;i<j;i++,bit++)
            adj[i][j]=adj[j][i]=((line[1+bit/6]-63)>>(5-bit%6))&1;
        if(bit%6 && ((line[len-1]-63)&((1<<(6-bit%6))-1))) return 4;
        int part[MAXN]={0};bestset=0;nodes=leaves=automorphisms=0;search(part,1);
        printf("%s\t%llu\t%llu\t%llu\n",best,nodes,leaves,automorphisms);
    }
    return ferror(stdin)?5:0;
}
