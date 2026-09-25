
st = str(input())
res = ""
i = 0
while i < len(st):
    if st[i]  == ".":
        res += "0"
        i += 1
    else:
        if st[i:i+2] == "-.":
            res += "1"
            
        else:
            res += "2"
        i += 2
           
print(res)       
