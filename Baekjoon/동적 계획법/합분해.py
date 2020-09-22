from sys import stdin
input = stdin.readline
N, K = map(int, input().split())
div = 1000000000
cache = [[0 for i in range(N+1)] for j in range(K+1)]
cache[1] = [1] * (N+1)
for i in range(K+1):
    cache[i][0] = 1
for i in range(1,K+1):
    for j in range(1,N+1):
        cache[i][j] = (cache[i-1][j] + cache[i][j-1])%div
print(cache[K][N])
    