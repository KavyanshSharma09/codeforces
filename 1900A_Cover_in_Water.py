n = int(input())
for _ in range(n):
    x = int(input())
    st = input()
    if  "..." in st:
        print(2)
    else:
        print(st.count("."))
    