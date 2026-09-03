def check(arr):
    
    res = []
    for i in arr:
        count = 0
        for w in i:
            if w == "1":
                count +=1
        if count == 2 or count > 2:
            res.append(w)
    return len(res)

                    


n = int(input())
temp = []
for i in range(n):
    st = str(input())
    temp.append(st)
print(check(temp))