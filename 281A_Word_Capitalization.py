s = str(input())
if s[0] == s[0].upper():
    print(s)
else:
    res = ""
    res = s[0].upper()+s[1:]
    print(res)