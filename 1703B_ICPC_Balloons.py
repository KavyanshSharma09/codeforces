n = int(input())
for _ in range(n):
    l = int(input())
    st = input()
    s = set()
    count = 0
    for i in st:
        if i in s:
            count += 1
        else:
            s.add(i)
            count +=2
    print(count)