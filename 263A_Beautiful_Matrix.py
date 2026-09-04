a = []
for i in range(5):
    row = list(map(int, input().split()))
    a.append(row)

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == 1:
            res = [i+1,j+1]
            temp = [abs(res[0]-3),abs(res[1]-3)]
            
print(sum(temp))