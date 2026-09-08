n = int(input())

count = 0

for x in [100, 20, 10, 5, 1]:
    count += n // x
    n %= x

print(count)