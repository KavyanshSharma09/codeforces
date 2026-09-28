from math import gcd
a, b = map(int, input().split())
temp = max(a, b)
res = 6 - temp + 1
g = gcd(res, 6)
print(f"{res // g}/{6 // g}")