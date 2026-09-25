x = int(input())
for _ in range(x):
    n = int(input())
    st = str(input())
    lo,hi = 0,len(st)-1
    while lo<hi and st[lo] !=st[hi]:
        lo += 1
        hi -= 1
    print(hi-lo+1)