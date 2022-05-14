f = open('26-k2.txt')
N,k = map(int, f.readline().split())
a = [int(i) for i in f]
a.sort(reverse = True)
a = a[k:(N-k)]
print(a[0])
print(sum(a)/len(a))
