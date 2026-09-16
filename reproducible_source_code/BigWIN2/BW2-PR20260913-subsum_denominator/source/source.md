# Ordinary reciprocal-subsum denominator log-concavity

Source: Cristina Ballantine, George Beck, Brooke Feigon and Kathrin Maurischat, Reciprocals of subsum polynomials, The Ramanujan Journal70:46(2026), DOIhttps://doi.org/10.1007/s11139-026-01419-0, Conjecture4, p18.

Original statement (mathematical notation normalized; words preserved):

> The sequence of coefficients of den(n,x) is log-concave except for n=3,5,6,7.

Definitions: n is apositiveinteger. Let sp(lambda,x)=product_(parts a of lambda)(1+x^a). For each partitionlambda ofn set h_lambda=product_(i=1)^n(1+x^i)^(floor(n/i)-m_lambda(i)), G_n=gcd_lambda h_lambda, and den(n,x)=product_(i=1)^n(1+x^i)^floor(n/i)/G_n. Proposition3.8 identifies this exact polynomial with D_n=product_(i=1)^n(1+x^i)^(1+floor(log2(n/i))).

Exact target: for every integern>=1 outside{3,5,6,7}, writingD_n=sum_j d_(n,j)x^j, prove ordisprove d_(n,j)^2>=d_(n,j-1)d_(n,j+1) for every1<=j<degreeD_n. Thefourlistedexceptions areknown failures, notnewcontributions. Coefficientsincludeall integerdegrees, notsubsequences. No upperboundonn is substituted.

Knownboundary: Prop3.9p11 givespalindromicity andunimodality; thosealone arenotlogconcavity. Chen-Ono-Zhang2605.21718v2 lists thisshapeclaim asremainingopen. Retrieved2026-09-13local/2026-09-12UTC. CompletejournalPDFSHAa0da6b8f736e5fc66084d2fa6913d89bce77254d7e9e4e5a5a2acce9b4a4ff31.
