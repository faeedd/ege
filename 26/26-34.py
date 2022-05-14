a = []
with open('26-j6.txt') as F:
    n = int(F.readline()) # количество чисел в файле
    for i in range(n):
        a.append(int(F.readline()))
a.sort()
va = sum(a) * 0.9 #архив
k = m = v = i = 0
while i < n-1 and v+a[i] + sum(a[i+1:n])*0.8 <= va:
    v += a[i]
    m = a[i] # макс. искомое
    k += 1 # количество искомых
    i += 1
delta = va - v
for j in range(i,n):
    if a[j] - m <= delta:
        m = a[j]
print(k,m)
