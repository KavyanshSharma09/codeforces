t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    stk = []
    printed = set()
    for i in range(n):
        if s[i] == '1':
            stk.append(i)
        elif s[i] == '2':
            if stk:
                printed.add(stk.pop())
            else:
                printed.add(i)
        else:  
            printed.add(i)
    ans = []
    for i in range(n):
        if i not in printed:
            ans.append(i + 1)
    print(len(ans))
    print(*ans)