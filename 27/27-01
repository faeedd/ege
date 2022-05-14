f = open("filename.txt")
M = 345600
N = int(f.readline())
a = [int(i) for i in f]
left = 0
right = 1
count = 0
pr = a[0]
kp = N * (N+1) // 2
while left < N and right < N:
    if pr % M == 0:
        count += N - right + 1
        pr //= a[left]
        left += 1
    else:
        pr *= a[right]
        right += 1
print(kp - count)
