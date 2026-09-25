n = int(input())
arr = list(map(int, input().split()))
maxx = max(arr)
total = 0
for i in arr:
    temp = maxx-i
    total += temp
print(total)