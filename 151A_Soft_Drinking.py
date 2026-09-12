n, k, l, c, d, p, nl, np = map(int,input().split())
t1 = (k*l)//nl
t2 = c*d
t3 = p//np
res = (min(t1,t2,t3))//n
print(res)