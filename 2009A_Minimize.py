n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    if a ==b:
        print(0)
    else:
        finn = float('inf')
        for i in range(a,b):
            temp = (i-a)+(b-i)
            finn = min(finn, temp)
        print(finn)