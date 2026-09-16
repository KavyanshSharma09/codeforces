n = int(input())
for _ in range(n):
    x = int(input())
    arr = list(map(int,input().split()))
    if sum(arr)%2 ==0:
        print("YES")
    else:
        print("NO")