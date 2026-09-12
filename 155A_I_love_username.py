n = int(input())
arr = list(map(int,input().split()))
best = arr[0]
worst = arr[0]
count = 0
for i in range(1,len(arr)):
    if arr[i] > best:   
        count +=1
        best = arr[i]
    elif arr[i] < worst:
        count += 1
        worst = arr[i]
print(count)
        