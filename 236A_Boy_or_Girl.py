s = str(input())
s = list(set(s))
n = len(s)
if n%2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")