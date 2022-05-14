itog = set()
for i in range(1,100000):
    n = bin(i)[2:]
    n = n + str(sum([int(i) for i in n])%2)
    n = n + str(sum([int(i) for i in n]) % 2)
    itog.add(int(n,2))
print (len(list(filter(lambda x: x<50,sorted(itog)))))
