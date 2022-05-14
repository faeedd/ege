f = open("filename.txt")
M = 8023320
N = int(f.readline())
a = [int(i) for i in f]
ml = 0
elpm = 0
left = 0
right = 1
pr = a[0]
while left < N and right < N:
    if M % pr == 0:
        if right - left > ml:
            ml = right - left
            elpm = left + 1
        pr *= a[right]
        right += 1
    else:
        pr //= a[left]
        left += 1
print(elpm)
