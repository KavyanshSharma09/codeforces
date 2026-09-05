y = int(input())
i = y+1
while i >y:
    if len(str(i)) == len(set(str(i))):
        print(i)
        break
    else:
        i +=1