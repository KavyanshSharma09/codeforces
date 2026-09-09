s = str(input())
s = s[1:-1]
res = []
for i in s:
    if i == "{" or i == "}" or i == "," or i == " " or i == "":
        continue
    else:
        res.append(i)
print(len(list(set(res))))