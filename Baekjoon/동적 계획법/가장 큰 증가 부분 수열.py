n, a = int(input()), list(map(int, input().split()))
dp = a[:]
for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[j]+a[i], dp[i])
print(max(dp))


