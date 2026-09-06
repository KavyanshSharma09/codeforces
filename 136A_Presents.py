n = int(input())
arr = list(map(int, input().split()))
res = [0]*(n)
for i in range(n):
    res[arr[i]-1] = i+1
print(*res)