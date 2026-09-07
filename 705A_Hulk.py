n = int(input())
dp = [""] *(n+1)
dp[1] = "I hate"
if n>= 2:
    dp[2] = "I hate that I love"

for i in range(3,n+1):
    if i%2 == 0:
        dp[i] = dp[i-1] + " that I love"
    else:
        dp[i] = dp[i-1] + " that I hate"
print(dp[n] + " it")