n = int(input())
for _ in range(n):
    l = int(input())
    x = list(map(int,input().split()))
    
    for i in x:
        count = 0
        temp = 0
        if i == 0:
            count+=1
            temp = max(temp, count)
        else: 
            count = 0
            
    print(temp)