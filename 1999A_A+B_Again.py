n = int(input())
for _ in range(n):
    st = str(input())
    if len(st) >1:
        print(int(st[0])+int(st[1]))
    else:
        print(int(st))