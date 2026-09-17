t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        if arr.count(arr[i]) == 1:
            print(i + 1)
            break