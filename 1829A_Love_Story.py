n = int(input())
check = "codeforces"
for _ in range(n):
    st = input()
    count = 0
    for i in range(len(st)):
        if st[i] != check[i]:
            count+= 1
    print(count)