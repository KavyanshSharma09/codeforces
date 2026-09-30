# solvable but it is an unoptimized solution. It is a brute force solution 
n = int(input())
memo = set()
for i in range(2,n+1):
    if i < 2 or any(i % j == 0 for j in range(2, int(i ** 0.5) + 1)):
        memo.add(i)
for i in memo:
    if n - i in memo:
        print(i, n - i)
        break
            

            
                
    