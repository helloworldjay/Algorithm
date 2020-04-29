t = int(input()) # testcase
tc = []
def p123(n):
    dp = [0,1,2,4]
    for i in range(4,n+1):
        dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    return dp[n] 
for _ in range(t):
    tc.append(int(input()))
for i in range(t):
    print(p123(tc[i]))