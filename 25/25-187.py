def divisors(x):
    dv = set()
    for d in range(2,int(x**0.5) + 1):
        if x % d == 0:
            dv.add(d)
            dv.add(x//d)
    return sorted(dv)
for n in range(10000000,10005000):
    d = divisors(n)
    if len(d) >= 2:
        S = d[len(d) - 1] + d[len(d) - 2]
        if S < 100000 and S % 31 == 0:
            print(S,n)
