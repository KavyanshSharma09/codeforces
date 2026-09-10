n = int(input())
for i in range(n):
    s1,s2,s3 = map(int,input().split())
    maxx  = max(s1,s2,s3)
    summ = s1+s2+s3
    if summ-maxx == maxx:
        print("YES")
    else:
        print("NO")