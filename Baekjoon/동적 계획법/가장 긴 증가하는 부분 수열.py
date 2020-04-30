# n, seq = int(input()), list(map(int, input().split())) # 개수, 수열
# dp = [1] * n # 최소 부분 수열의 길이가 1이므로 1로 초기화
# for i in range(1, n):
#     for j in range(0, i):
#         if dp[j] < dp[i] :
#             dp[i] = max(dp[i-1], dp[j]+1)
    
# print(max(dp))


n, seq = int(input()), list(map(int, input().split()))
dp = [1 for _ in range(n)] # 최소 길이가 1이므로
for i in range(1, n):
    for j in range(i):
        if seq[i] > seq[j] :
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
