n = int(input())
res = []
for i in range(n):
    st,sf = map(int,input().split())
    res.append(sf-st)
count= 0
for i in res:
    if i >= 2:
        count+=1
print(count)
