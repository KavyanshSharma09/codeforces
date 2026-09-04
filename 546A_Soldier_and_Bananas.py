k,n,w = map(int,input().split())
summ = 0
l = []
for i in range(1,w+1):
    l.append(i*k)
if (sum(l)-n) < 0:
    print(0)
else:
    print(sum(l)-n)
