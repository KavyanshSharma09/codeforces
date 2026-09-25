n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    finn = float('inf')
    for i in range(a,b):
        temp = (i-a)+(b-i)
        finn = min(finn, temp)
    print(finn)