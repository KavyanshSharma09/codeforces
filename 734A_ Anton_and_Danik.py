n = int(input())
s = str(input())
c = 0
for i in s:
    if i == "D":
        c +=1
if (n-c) > c:
    print("Anton") 
elif (n-c) == c:
    print("Friendship")
else:
    print("Danik")