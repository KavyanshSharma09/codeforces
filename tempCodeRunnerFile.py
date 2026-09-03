
n,x = map(int,input().split())
arr = list(map(int, input().split()))

if list(set(arr))[0] == x:
    print(n)
else:
    count = 0
    for i in arr:
        
        if i >x:
            count+=1
    print(count)