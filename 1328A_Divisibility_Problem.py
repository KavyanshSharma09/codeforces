def check(a,b):
    t = a%b
    if t == 0:
        return 0
    else:
        return b-t

n = int(input())
res = []
for _ in range(n):
    a,b = map(int,input().split())
    res.append(check(a,b))
print(*res, sep="\n")
