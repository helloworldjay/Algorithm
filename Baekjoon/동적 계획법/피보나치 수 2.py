# 성공
from sys import stdin
n = int(stdin.readline())
dp = [0 for _ in range(n+1)]
dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])
# 이유는 모르겠는데 dp[2] = 1을 추가하면 런타임에러가 난다..

# 실패 1
# n = int(input())
# def fibo(k):
#     dp = [0 for _ in range(k+1)]
#     dp[1] = 1
#     dp[2] = 1
#     for i in range(3, k+1):
#         dp[i] = dp[i-1] + dp[i-2]
#     return dp[k]
# print(fibo(n))


# 실패 2
# n = int(input())
# dp = [0 for _ in range(n+1)] 
# dp[1], dp[2] = 1, 1
# def fibo(k):
#     if dp[k] != 0:
#         return dp[k] 
#     else :
#         return fibo(k-1)+ fibo(k-2)
# print(fibo(n))
