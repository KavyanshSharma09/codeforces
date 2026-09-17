t = int(input())
for _ in range(t):
    a = list(map(int,input().split()))
    a.remove(max(a))
    a.remove(min(a))
    print(*a)