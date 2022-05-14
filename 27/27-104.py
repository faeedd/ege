f = open("filename.txt")
M = 4043520
N = int(f.readline())
a = [int(i) for i in f]
all_count = N * (N+1) // 2
pr = 1
count = left = 0
for i in range(N):
    pr *= a[i]
    while 4043520 % pr != 0:
        count += N - i
        pr //= a[left]
        left += 1
print(all_count - count)
