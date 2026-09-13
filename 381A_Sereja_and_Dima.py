n = int(input())
arr = list(map(int, input().split()))
s = 0
d = 0
for i in range(len(arr)):
    x = max(arr[0],arr[-1])
    if i % 2 == 0:
        s += x
    else:
        d += x
    arr.remove(x)
print(s)
print(d)