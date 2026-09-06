n1 = str(input())
n2 = str(input())
res = ""
for i in range(len(n1)):
    if n1[i] == "1" and n2[i] == "1":
        res = res+"0"
    elif n1[i] == "0" and n2[i] == "0":
        res = res+"0"
    else:
        res = res+"1"
print(res)
