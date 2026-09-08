n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
temp = p[1:]+q[1:]
if len(list(set(temp))) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

