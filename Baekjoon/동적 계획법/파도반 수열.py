def p(n):
    dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] # 파도반 수열
    dp.extend([0]*(n-10))
    if n <= 10:
        return dp[n]
    else :
        for i in range(11, n+1):
            dp[i] = dp[i-1] + dp[i-5]
    return dp[n]

k = int(input())
tc = []
for i in range(k):
    tc.append(int(input()))
for i in range(k):
    print(p(tc[i]))