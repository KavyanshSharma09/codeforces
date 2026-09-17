n = int(input())
for _ in range(n):
    l = int(input())
    st = list(map(int,input().split()))
    st.sort()
    pos = True
    for i in range(n - 1):
        if st[i + 1] - st[i] > 1:
            pos = False
            break
    if pos:
        print("YES")
    else:
        print("NO")
