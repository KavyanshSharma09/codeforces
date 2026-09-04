s = list(map(str,input().split("+")))
s.sort()
res = ""
for i in s:
    res = res+ str(i)+"+"
    
print(res[:len(res)-1])