n = int(input())

dp = [-1 for _ in range(91)]
dp[1] = 1
dp[2] = 1

def fibo(n):
    if dp[n] == -1:
        dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

print(fibo(n))