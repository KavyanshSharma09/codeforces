n = int(input())
arr = list(map(int, input().split()))
one = []
two = []
three = []
for i in range(n):
    if arr[i] == 1:
        one.append(i + 1)
    elif arr[i] == 2:
        two.append(i + 1)
    else:
        three.append(i + 1)
minn = min(len(one), len(two), len(three))
print(minn)
for i in range(minn):
    print(one[i], two[i], three[i])