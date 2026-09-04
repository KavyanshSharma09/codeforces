n = int(input())

rim = n%5
if rim > 0:
    print((n//5)+1)
else:
    print(n//5)