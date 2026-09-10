nu = int(input())
for _ in range(nu):
    st = int(input())
    if st<=2:
        print(0)
    else:
        temp = st - (st//2)
        if st%2 == 0:
            print((st-temp)-1)
        else:
            print(st-temp)
            