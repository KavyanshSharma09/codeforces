arr = list(map(int,input().split()))
arr.sort()
for i in range(len(arr)-1):
    a = max(arr) -arr[i]
    print(a,end=" ")    
