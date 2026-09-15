n = int(input())
for _ in range(n):
    x,k = map(int,input().split())
    arr= list(map(int,input().split()))
    if k in arr:
        print("YES")
    else:
        print("NO")
    