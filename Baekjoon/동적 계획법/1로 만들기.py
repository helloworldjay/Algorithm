# n = int(input()) # 숫자 입력
# dp = [0,0,1,1] # 0과 1은 0번으로, 2와 3은 1번의 연산으로 1 가능
# for i in range(4, n+1):
#     dp.append(dp[i-1]+1)
#     if i%2 ==0 :
#         dp[i] = min(dp[i], dp[(i//2)]+1)
#     if i%3 == 0:
#         dp[i] = min(dp[i], dp[(i//3)]+1)  # 이게 elif면 틀린다.
# print(dp[n])



from sys import stdin
input = stdin.readline
N = int(input())
cache = [0,0,1,1] + [0]*(N-3)
counts = 0    
for i in range(4, N+1):
    if i % 6 == 0 :
        cache[i] = min(cache[i//3], cache[i//2], cache[i-1]) + 1
        continue
    elif i % 3 == 0:
        cache[i] = min(cache[i//3], cache[i-1]) + 1
        continue
    elif i % 2 == 0:
        cache[i] = min(cache[i//2], cache[i-1]) + 1
        continue
    else :
        cache[i] = cache[i-1] + 1
print(cache[N])
    