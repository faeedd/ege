f = open('26-files/26-5-1.txt')
nechet = []
all = set()
k = m = 0
N = int(f.readline())
for _ in range(N):
    x = int(f.readline())
    if x % 2 != 0:
        nechet.append(x)
        all.add(x)
    else:
        all.add(x)
for i in range(len(nechet)):
    for j in range(i+1,len(nechet)):
        s = (nechet[i]+nechet[j]) // 2
        if s in all:
            k += 1
            m = max(s,m)
print(k,m)
