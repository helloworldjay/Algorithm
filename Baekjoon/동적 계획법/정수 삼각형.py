# dp[i][j]는 i행 j 열 까지 합의 최대값
# dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])

n = int(input()) # 삼각형의 변의 길이
dp = [[0]*n for _ in range(n+1)]
for i in range(n+1):
    temp = list(map(int, input().split()))
    for j in range(1, i+1):
        dp[i][j] = tmp[j-1]
for i in range(1, n+1):
    for j in range(0, i+1):
        if j == 0 :
            dp[i][j] = dp[i-1][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1]
        else :    
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[n-1])) 