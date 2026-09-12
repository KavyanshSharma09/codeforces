n,k = map(int,input().split())
total = k
count = 0
for i in range(1,n+1):
    total += i*5
    if total >240:
        break
    count += 1
print(count)

        