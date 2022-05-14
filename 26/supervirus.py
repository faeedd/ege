with open('26-files/26-8.txt') as F:
    N, T = map(int, F.readline().split())
    vse = [list(map(int, F.readline().split())) for j in range(N)]
    Ur = 0
    for x in vse:
        Ur += x[0]
    Ur = Ur / N
    slab = []
    silen = []
    for x in vse:
        if x[0] <= Ur:
            slab.append(x)
        elif x[0] > Ur:
            silen.append(x)
k = Tslab = Tsilen = 0
slab = sorted(slab)
silen = sorted(silen)
for i in range(len(slab)):
    if silen[i][1] + Tslab + Tsilen < T:
        k += 1
        Tsilen += silen[i][1]
    if slab[i][1] + Tslab + Tsilen < T:
        k += 1
        Tslab += slab[i][1]
    f = i
for i in range(f,len(slab)):
    print(slab[i])
    if Tslab + Tsilen + slab[i][1] < T:
        k += 1
        Tslab += slab[i][1]
print(k,Tsilen)
