n = int(input())
for _ in range(n):
    st = input()
    if len(st) <= 2:
        print(st)
        continue
    memo = [st[0]]
    for i in range(1, len(st), 2):
        memo.append(st[i])
    print(''.join(memo))