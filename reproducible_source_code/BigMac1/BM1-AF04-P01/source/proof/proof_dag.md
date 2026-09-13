# Proof dependency graph

```text
Krasko--Omelchenko EGF + branch s(0)=1
                  |
                  v
   X=(E,E/s,G), exact state system X'=AX  ---->  piece annihilators (2),(3)
                  |
                  v
 row identity p3 r3+p2 r2+p1 r1+p0 r0=0
                  |
                  v
              L3(F)=0
                  |
       Ore identity M o L3 = L5
                  |
                  v
              L5(F)=0
                  |
 EGF rule [t^m/m!] t^j F^(k)=(m)_j a_(m-j+k)
                  |
                  v
      target recurrence for every n>=4

formal expansion F(t) --> a0=0,a1=0,a2=1,a3=1 --> uniqueness/initial data
```

Decisive identities are certified independently in
`certificates/verify_certificate.py`; direct differentiation and finite
combinatorial checks are separate audit routes.
