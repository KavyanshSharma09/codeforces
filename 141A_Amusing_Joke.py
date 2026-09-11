s1 = str(input())
s2 = str(input())
s3 = str(input())

if sorted(list(s1+s2)) == sorted(list(s3)):
    print("YES")
else:
    print("NO")

