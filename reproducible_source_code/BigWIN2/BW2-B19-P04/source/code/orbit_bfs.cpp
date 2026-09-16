#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <unordered_set>
#include <vector>

using U = std::uint64_t;
static std::vector<std::array<int,4>> fs;
static std::vector<U> vm;
static std::vector<std::array<unsigned char,35>> actions;

static bool appendable(U s, int j) {
    U f=vm[j], ridges[4]={0,0,0,0}; int nr=0;
    for(int i=0;i<35;i++) if((s>>i)&1) {
        U h=f&vm[i];
        if(__builtin_popcountll(h)==3) {
            bool seen=false; for(int q=0;q<nr;q++) seen |= ridges[q]==h;
            if(!seen) ridges[nr++]=h;
        }
    }
    if(!nr) return false;
    for(int i=0;i<35;i++) if((s>>i)&1) {
        U h=f&vm[i]; bool covered=false;
        for(int q=0;q<nr;q++) covered |= (h & ~ridges[q])==0;
        if(!covered) return false;
    }
    return true;
}

static U canon(U s) {
    U best=~U(0);
    for(auto const& a:actions) {
        U t=0, x=s;
        while(x) { int i=__builtin_ctzll(x); x&=x-1; t |= U(1)<<a[i]; }
        if(t<best) best=t;
    }
    return best;
}

int main(int argc,char**argv){
    int maxdepth=argc>1?std::atoi(argv[1]):35;
    for(int a=0;a<7;a++)for(int b=a+1;b<7;b++)for(int c=b+1;c<7;c++)for(int d=c+1;d<7;d++){
        fs.push_back({a,b,c,d}); vm.push_back((U(1)<<a)|(U(1)<<b)|(U(1)<<c)|(U(1)<<d));
    }
    std::array<int,128> idx; idx.fill(-1); for(int i=0;i<35;i++)idx[vm[i]]=i;
    std::array<int,7> p={0,1,2,3,4,5,6};
    do {
        std::array<unsigned char,35>a{};
        for(int i=0;i<35;i++) { U z=0; for(int v:fs[i])z|=U(1)<<p[v]; a[i]=idx[z]; }
        actions.push_back(a);
    } while(std::next_permutation(p.begin(),p.end()));
    std::unordered_set<U> layer,next; layer.insert(1); // singleton orbit
    std::cout<<"depth,orbits,transitions,dead\n";
    for(int depth=1;depth<=maxdepth;depth++) {
        std::uint64_t trans=0,dead=0;
        if(depth<35) {
            for(U s:layer) {
                bool any=false;
                for(int j=0;j<35;j++) if(!((s>>j)&1) && appendable(s,j)) {
                    any=true; trans++; next.insert(canon(s|(U(1)<<j)));
                }
                if(!any) dead++;
            }
        }
        std::cout<<depth<<","<<layer.size()<<","<<trans<<","<<dead<<"\n"<<std::flush;
        if(dead || depth==maxdepth || layer.empty()) return dead?2:0;
        layer.swap(next); next.clear();
    }
}
