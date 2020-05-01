# dp[i][j] = i행 j열 까지의 합 중 최대가 되는 경우의 합
# a[i][j] = 주어진 삼각형을 담는 리스트
n = int(input())
a = [[0] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split())) 
dp = [[0]*n for _ in range(n)]
dp[0][0] = a[0][0]
for i in range(1, n):
    for j in range(i+1):
        if j < 1 :
            dp[i][j] = dp[i-1][j] + a[i][j]
        elif j > i :
            dp[i][j] = dp[i-1][j-1] + a[i][j]
        else :
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + a[i][j]
print(max(dp[n-1]))