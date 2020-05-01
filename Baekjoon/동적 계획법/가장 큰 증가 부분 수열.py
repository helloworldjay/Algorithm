n, a = int(input()), list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = a[0]
for i in range(n):
    for j in range(0, i):
        if a[i] > a[j]:
            dp[i] = max(dp[j]+a[i], dp[i]) #i번째가 j번째보다 클 때에만 부분 수열에 포함한다. 
print(max(dp))