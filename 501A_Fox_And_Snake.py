m, n = map(int, input().split())
for row in range(m):
    if row%2 == 0:
        print("#"*n)
    elif row%4 == 1:
        print("."*(n-1)+"#")
    else:
        print("#"+"." *(n-1))
        
        
    