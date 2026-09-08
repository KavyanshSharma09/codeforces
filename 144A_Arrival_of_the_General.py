n = int(input())
arr = list(map(int,input().split()))
maxx = arr.index(max(arr))
minn = n - 1 - arr[::-1].index(min(arr))

ans = maxx+(n-1-minn)
if maxx > minn:
    ans -= 1
print(ans)
        
