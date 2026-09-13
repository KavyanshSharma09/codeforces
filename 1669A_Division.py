n = int(input())
for _ in range(n):
    st = int(input())
    if st < 1400:
        print("Division 4")
    elif st <= 1599:
        print("Division 3")
    elif st <= 1899:
        print("Division 2")
    else:
        print("Division 1")