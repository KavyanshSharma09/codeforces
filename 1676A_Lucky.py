n = int(input())

for _ in range(n):
    st = str(input())
    res = []
    for i in st:
        res.append(int(i))
    if sum(res[:3]) == sum(res[3:]):
        print("YES")
    else:
        print("NO")