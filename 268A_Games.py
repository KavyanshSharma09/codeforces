n = int(input())
home = []
away = []
for _ in range(n):
    h,a = map(int,input().split())
    home.append(h)
    away.append(a)
i = 0
count = 0
while i <len(home):
    for j in range(len(away)):
        if home[i] ==away[j]:
            count += 1
    i += 1
print(count)