t = int(input())
for _ in range(t):
    ans = 0
    a = list(map(int,input().split()))
    for i in a:
        ans ^= i
    print(ans)
    
        