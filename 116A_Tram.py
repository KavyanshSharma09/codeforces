def check(arr):
    curr_sum = float('-inf')
    for i in range(len(arr)):
        summ = 0
        for j in range(i,len(arr)):
            if (j-i)%2 == 0:
                summ += arr[j]
            else:
                summ -= arr[j]
        curr_sum = max(curr_sum,summ)
    return curr_sum

n = int(input())
ar = []
for i in range(n):
    s1,s2 = map(int,input().split())
    ar.append(s1)
    ar.append(s2)
print(check(ar))