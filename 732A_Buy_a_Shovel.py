n,k = map(int,input().split())
for i in range(1,11):
    if (i*n)%10 == 0 or (i*n)%10 == k:
        print(i)
        break
   