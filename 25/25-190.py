def divisors(x):
    dv = set()
    for d in range(2,int(x**0.5) + 1):
        if x % d == 0:
            dv.add(d)
            dv.add(x//d)
    return sorted(dv)
for n in range(10000000,10009000):
    d = divisors(n)
    if len(d) >= 3:
        S = d[len(d) - 1] + d[len(d) - 2] + d[len(d) - 3]
        S1 = str(S**0.5)
        if S1.isdigit():
            print(S1)
