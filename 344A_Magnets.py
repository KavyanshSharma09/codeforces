n = int(input())
res = []
for _ in range(n):
    mg = str(input())
    res.append(mg)
g = 1
for i in range(n-1):
    if res[i]!=res[i+1]:
        g+=1
print(g)