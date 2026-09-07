n = int(input())
if n ==1:
    print("I hate it")
if n == 2:
    print("I hate that I love it")
dp = [""]*(n+1)
dp[1] = "I hate"
dp[2] = "I hate that I love"
for i in range(3,n+1):
    dp[i] = dp[i-1]+" "+ "that" + " "+ dp[i-2] + " " + "it"
print(dp[n])