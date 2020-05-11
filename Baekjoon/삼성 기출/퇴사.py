# dp[i]는 i일까지 최대 pay
from sys import stdin
n = int(stdin.readline())
dp = [0 for i in range(n+1)] # 아무생각없이 초기화했다..
tp = [(0,0)]
for _ in range(n):
    tp.append(tuple(map(int, stdin.readline().split())))
for i in range(1,n+1):
    if i + tp[i][0] <= n + 1:
        dp[i] = tp[i][1] # i번째 날에 일한 것으로 초기화
        for j in range(1, i):
            if j + tp[j][0] <= i :
                dp[i] = max(dp[i], dp[j]+tp[i][1])
print(max(dp)) 
