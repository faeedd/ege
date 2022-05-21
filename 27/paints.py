f = open('27a.txt')
N = int(f.readline())
m = []
for i in range(N):
    a,b = map(int, f.readline().split())
    s = [a,b]
    m.append(s)
res = sorted(m, key=lambda x: x[1])
lastP = -1
k = 0
for i in range(len(res)):
    currfP = res[i][0]
    if currfP > lastP:
        k += 1
        lastP = res[i][1]
print(k)
