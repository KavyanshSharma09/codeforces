n = int(input())
res = list(map(int,input().split()))

un = 0
po = 0
for i in res:
    if i >0:
        po+=i
    else:
        if po>0:
            po -= 1
        else:
            un += 1
print(un)
