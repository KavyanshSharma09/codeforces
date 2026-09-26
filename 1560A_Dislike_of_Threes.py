t = int(input())
for _ in range(t):
    k = int(input())
    count = 0
    num = 0
    while count < k:
        num += 1
        if num % 3 != 0 and num % 10 != 3:
            count += 1
    print(num)