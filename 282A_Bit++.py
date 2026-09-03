def check(arr):
    n = 0
    for i in arr:
        if "+" in i:
            n += 1
        else:
            n -=1
    return n

x = int(input())
ar = []
for i in range(x):
    st = str(input())
    ar.append(st)
print(check(ar)) 

