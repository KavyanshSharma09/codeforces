n = int(input())
for _ in range(n):
    st = str(input())
    if st == "abc":
        print("YES")
    elif st[1] + st[0] + st[2] == "abc":
        print("YES")
    elif st[2] + st[1] + st[0] == "abc":
        print("YES")
    elif st[0] + st[2] + st[1] == "abc":
        print("YES")
    else:
        print("NO")