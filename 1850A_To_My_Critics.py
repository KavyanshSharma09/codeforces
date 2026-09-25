def check(ar):
    for i in range(len(ar)):
        for j in range(i + 1, len(ar)):
            if ar[i] + ar[j] >= 10:
                return "YES"

    return "NO"


n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    print(check(arr))