def fibo(n):
    dp = [0]*(n+1)
    if n < 3:
        return 1
    if dp[n] != 0:
        return dp[n]
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

print(fibo(5))