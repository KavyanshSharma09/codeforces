t = int(input())
for _ in range(t):
    a = list(map(int,input().split()))
    count = 0
    for i in range(1,len(a)):
        if a[i] >a[0]:
            count += 1  
    print(count)

