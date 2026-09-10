n = int(input())
for _ in range(n):
    st = str(input())
    l = len(st)
    res = []
    for i in range(l):
        t = int(st[i]) * (10 ** ((l - 1) - i))
        if t > 0:
            res.append(t)
    print(len(res))
    print(*res)
