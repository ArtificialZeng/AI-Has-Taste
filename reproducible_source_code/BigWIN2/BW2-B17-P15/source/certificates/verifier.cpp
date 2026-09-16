#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;
using u64 = std::uint64_t;
using u128 = __uint128_t;

struct Prime { u64 p, root; };
static const Prime PRIMES[] = {
    {998244353ULL,3ULL}, {1004535809ULL,3ULL}, {469762049ULL,3ULL},
    {167772161ULL,3ULL}, {754974721ULL,11ULL}
};

static u64 modpow(u64 a, u64 e, u64 p) {
    u64 r=1;
    while(e){ if(e&1) r=(u128)r*a%p; a=(u128)a*a%p; e>>=1; }
    return r;
}

static void ntt(std::vector<u64>& a, bool inv, Prime z) {
    const size_t n=a.size();
    for(size_t i=1,j=0;i<n;i++){
        size_t bit=n>>1; for(;j&bit;bit>>=1) j^=bit; j^=bit;
        if(i<j) std::swap(a[i],a[j]);
    }
    for(size_t len=2;len<=n;len<<=1){
        u64 wlen=modpow(z.root,(z.p-1)/len,z.p);
        if(inv) wlen=modpow(wlen,z.p-2,z.p);
        for(size_t i=0;i<n;i+=len){
            u64 w=1;
            for(size_t j=0;j<len/2;j++){
                u64 x=a[i+j], y=(u128)a[i+j+len/2]*w%z.p;
                a[i+j]=x+y<z.p?x+y:x+y-z.p;
                a[i+j+len/2]=x>=y?x-y:x+z.p-y;
                w=(u128)w*wlen%z.p;
            }
        }
    }
    if(inv){ u64 ni=modpow(n,z.p-2,z.p); for(u64& x:a)x=(u128)x*ni%z.p; }
}

static std::vector<u64> convolution_mod(const std::vector<u64>& w, Prime z, size_t sz) {
    std::vector<u64> a(sz);
    for(size_t i=0;i<w.size();i++) a[i]=w[i]%z.p;
    ntt(a,false,z); for(u64& x:a)x=(u128)x*x%z.p; ntt(a,true,z);
    a.resize(2*w.size()-1); return a;
}

static u64 parse_u64(const std::string& s, bool positive=false) {
    if(s.empty() || (s.size()>1 && s[0]=='0')) throw std::runtime_error("non-canonical unsigned integer");
    u64 x=0;
    for(char c:s){
        if(c<'0'||c>'9') throw std::runtime_error("invalid unsigned integer");
        unsigned d=c-'0';
        if(x>(std::numeric_limits<u64>::max()-d)/10) throw std::runtime_error("uint64 overflow");
        x=x*10+d;
    }
    if(positive && x==0) throw std::runtime_error("integer must be positive");
    return x;
}

static std::vector<u64> read_certificate(const std::string& path) {
    std::ifstream f(path); if(!f) throw std::runtime_error("cannot open input");
    std::string s;
    if(!(f>>s)||s!="AUTOCONV_CERT_V1") throw std::runtime_error("bad magic/version");
    if(!(f>>s)||s!="n") throw std::runtime_error("missing n field");
    std::string ns; if(!(f>>ns)) throw std::runtime_error("missing n value");
    u64 n=parse_u64(ns,true); if(n>500000) throw std::runtime_error("n exceeds verifier limit");
    if(!(f>>s)||s!="weights") throw std::runtime_error("missing weights field");
    std::vector<u64> w; w.reserve(n);
    for(u64 i=0;i<n;i++){ if(!(f>>s))throw std::runtime_error("too few weights"); w.push_back(parse_u64(s)); }
    if(!(f>>s)||s!="end") throw std::runtime_error("missing end marker or too many weights");
    if(f>>s) throw std::runtime_error("trailing token after end marker");
    return w;
}

static std::vector<cpp_int> exact_convolution(const std::vector<u64>& w) {
    size_t sz=1; while(sz<2*w.size()-1)sz<<=1;
    for(const auto& z:PRIMES) if((z.p-1)%sz) throw std::runtime_error("transform length unsupported");
    cpp_int maxw=*std::max_element(w.begin(),w.end());
    cpp_int bound=cpp_int(w.size())*maxw*maxw;
    cpp_int modulus=1; for(const auto& z:PRIMES)modulus*=z.p;
    if(bound>=modulus) throw std::runtime_error("CRT modulus insufficient for proven coefficient bound");
    std::vector<std::vector<u64>> r;
    for(const auto& z:PRIMES)r.push_back(convolution_mod(w,z,sz));
    const size_t m=2*w.size()-1; std::vector<cpp_int> out(m);
    for(size_t k=0;k<m;k++){
        cpp_int x=r[0][k], M=PRIMES[0].p;
        for(size_t j=1;j<std::size(PRIMES);j++){
            u64 p=PRIMES[j].p, xm=(x%p).convert_to<u64>(), Mm=(M%p).convert_to<u64>();
            u64 delta=(r[j][k]+p-xm)%p;
            u64 t=(u128)delta*modpow(Mm,p-2,p)%p;
            x += M*t; M*=p;
        }
        if(x>bound) throw std::runtime_error("reconstructed coefficient exceeds bound");
        out[k]=x;
    }
    if(w.size()<=2048){
        std::vector<cpp_int> slow(m);
        for(size_t i=0;i<w.size();i++)for(size_t j=0;j<w.size();j++)slow[i+j]+=cpp_int(w[i])*w[j];
        if(slow!=out)throw std::runtime_error("naive convolution cross-check failed");
    }
    return out;
}

static void self_test(){
    std::vector<std::vector<u64>> cases={{1},{1,2,3},{0,7,0,11},{1000000000ULL,999999999ULL}};
    for(const auto& w:cases)(void)exact_convolution(w);
    std::cout<<"SELF_TEST_PASS cases="<<cases.size()<<"\n";
}

int main(int argc,char**argv){
    try{
        if(argc==2 && std::string(argv[1])=="--self-test"){self_test();return 0;}
        if(argc!=2)throw std::runtime_error("usage: verifier CERTIFICATE | --self-test");
        auto w=read_certificate(argv[1]);
        cpp_int A=0; for(u64 x:w)A+=x; if(A==0)throw std::runtime_error("all-zero vector is inadmissible");
        auto c=exact_convolution(w); cpp_int mx=*std::max_element(c.begin(),c.end());
        size_t arg=std::max_element(c.begin(),c.end())-c.begin();
        cpp_int lhs=cpp_int(2)*w.size()*mx*100000000;
        cpp_int rhs=A*A*150274365;
        cpp_int margin=rhs-lhs;
        std::cout<<"CERTIFICATE_PARSED n="<<w.size()<<"\nSUM "<<A<<"\nMAX_COEFFICIENT "<<mx
                 <<"\nARGMAX_FIRST "<<arg<<"\nLHS "<<lhs<<"\nRHS "<<rhs<<"\nMARGIN "<<margin<<"\n";
        if(!(lhs<rhs)){std::cout<<"VERDICT FAIL_TARGET\n";return 2;}
        std::cout<<"VERDICT PASS_STRICT_TARGET\n"; return 0;
    }catch(const std::exception& e){std::cerr<<"VERDICT INVALID: "<<e.what()<<"\n";return 1;}
}
