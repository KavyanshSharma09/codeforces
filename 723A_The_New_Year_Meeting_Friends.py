a,b,c = map(int,input().split())
temp = min(a-b,a-c,b-c,b-a,c-b,c-a)
print(abs(temp))
