n,h = map(int,input().split())
ar = list(map(int,input().split()))
w = 0
for i in ar:
    if i > h:
        w+=2
    else:
        w += 1   
print(w)

