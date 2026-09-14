x = int(input())
for _ in range(x):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    if arr == sorted(arr) or k >1:
        print("YES")
    else:
        print("NO")
        
             

                