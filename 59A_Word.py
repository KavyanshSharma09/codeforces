s = str(input())
lc ="abcdefghijklmnopqrstuvwxz"
uc = "ABCDEFGHIJKLMNOPQRSTUVW"
lcc = 0
for i in s:
    if i in lc:
        lcc += 1
hcc = len(s)-lcc
if hcc > lcc:
    s = s.upper()
    print(s)
else:
    s = s.lower()
    print(s)
