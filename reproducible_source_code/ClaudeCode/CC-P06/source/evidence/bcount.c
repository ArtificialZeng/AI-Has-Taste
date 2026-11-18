/* Independent brute-force counter for fully clued slitherlink: plain backtracking over edges (no SAT, no theory).
   usage: bcount file   (file: rows of digits, top row first). Prints each solution as an ASCII picture and the count. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int R,C;               /* cells: R rows, C cols; vertices (R+1)x(C+1) */
int clue[64][64];
int NE; int eu[8192],ev[8192]; /* edge endpoints (vertex ids) */
int ecells[8192][2], nec[8192];
int val[8192];
int cellcnt[64*64], cellrem[64*64], vdeg[8192], vrem[8192];
int vid(int r,int c){ return r*(C+1)+c; }
long sols=0; int printsol=1;
int par[8192]; int fnd(int x){ while(par[x]!=x){ par[x]=par[par[x]]; x=par[x];} return x; }
void check(){
  int nv=(R+1)*(C+1); for(int i=0;i<nv;i++) par[i]=i;
  int any=-1;
  for(int e=0;e<NE;e++) if(val[e]){ int a=fnd(eu[e]),b=fnd(ev[e]); if(a!=b) par[a]=b; any=eu[e]; }
  if(any<0) return;
  int root=fnd(any);
  for(int e=0;e<NE;e++) if(val[e] && fnd(eu[e])!=root) return;
  sols++;
  if(printsol){
    printf("solution %ld:\n",sols);
    for(int r=0;r<=R;r++){
      for(int c=0;c<=C;c++){ printf("+"); if(c<C){ int e=-1; for(int k=0;k<NE;k++) if(eu[k]==vid(r,c)&&ev[k]==vid(r,c+1)) e=k; printf(val[e]?"--":"  "); } }
      printf("\n"); if(r==R) break;
      for(int c=0;c<=C;c++){ int e=-1; for(int k=0;k<NE;k++) if(eu[k]==vid(r,c)&&ev[k]==vid(r+1,c)) e=k; printf(val[e]?"|":" "); if(c<C) printf("%d ",clue[r][c]); }
      printf("\n");
    }
  }
}
int ok_cell(int cl){ int r=cl/C,c=cl%C; int s=cellcnt[cl], rem=cellrem[cl]; return s<=clue[r][c] && s+rem>=clue[r][c]; }
int ok_v(int v){ int d=vdeg[v], rem=vrem[v]; if(d>2) return 0; if(rem==0 && d==1) return 0; if(d==1 && rem==0) return 0; return !(d==1 && rem==0); }
void rec(int e){
  if(e==NE){ check(); return; }
  for(int x=0;x<2;x++){
    val[e]=x; int ok=1;
    for(int k=0;k<nec[e];k++){ int cl=ecells[e][k]; cellcnt[cl]+=x; cellrem[cl]--; }
    vdeg[eu[e]]+=x; vdeg[ev[e]]+=x; vrem[eu[e]]--; vrem[ev[e]]--;
    for(int k=0;k<nec[e]&&ok;k++) if(!ok_cell(ecells[e][k])) ok=0;
    int vs[2]={eu[e],ev[e]};
    for(int k=0;k<2&&ok;k++){ int v=vs[k]; if(vdeg[v]>2 || (vrem[v]==0 && vdeg[v]==1) || (vdeg[v]==1 && vrem[v]==0)) ok=0; if(vrem[v]==0 && vdeg[v]!=0 && vdeg[v]!=2) ok=0; }
    if(ok) rec(e+1);
    for(int k=0;k<nec[e];k++){ int cl=ecells[e][k]; cellcnt[cl]-=x; cellrem[cl]++; }
    vdeg[eu[e]]-=x; vdeg[ev[e]]-=x; vrem[eu[e]]++; vrem[ev[e]]++;
  }
  val[e]=0;
}
int main(int argc,char**argv){
  FILE*f=fopen(argv[1],"r"); char line[256]; R=0;
  while(fgets(line,sizeof line,f)){ int n=0; for(char*p=line;*p;p++) if(*p>='0'&&*p<='4') clue[R][n++]=*p-'0'; if(n){C=n;R++;} }
  if(argc>2) printsol=atoi(argv[2]);
  /* edge order: for each vertex row r: horizontal edges of row r, then vertical edges from row r to r+1 */
  NE=0;
  for(int r=0;r<=R;r++){
    for(int c=0;c<C;c++){ eu[NE]=vid(r,c); ev[NE]=vid(r,c+1); nec[NE]=0; if(r>0) ecells[NE][nec[NE]++]=(r-1)*C+c; if(r<R) ecells[NE][nec[NE]++]=r*C+c; NE++; }
    if(r<R) for(int c=0;c<=C;c++){ eu[NE]=vid(r,c); ev[NE]=vid(r+1,c); nec[NE]=0; if(c>0) ecells[NE][nec[NE]++]=r*C+c-1; if(c<C) ecells[NE][nec[NE]++]=r*C+c; NE++; }
  }
  for(int cl=0;cl<R*C;cl++){ cellcnt[cl]=0; cellrem[cl]=4; }
  for(int e=0;e<NE;e++){ vrem[eu[e]]++; vrem[ev[e]]++; }
  rec(0);
  printf("%d x %d cells: %ld single-loop solutions\n",R,C,sols);
  return 0;
}
