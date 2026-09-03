def check(s):
    temp = ""
    n = len(s)
    a = n-2
    if n>10:
        a = str(a)
        temp = s[0]+a+s[-1]
        return temp
    else:
        return s
t = int(input())
for i in range(t):
    stt = str(input())
    print(check(stt))