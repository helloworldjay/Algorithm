from sys import stdin
input = stdin.readline
N = int(input())
cache = [[0], [1 for _ in range(10)]] + [[0 for i in range(10)] for j in range(N-1)]
for i in range(2, N+1):
    for j in range(10):
        cache[i][j] = (sum([cache[i-1][k] for k in range(j+1)]))%10007
print(sum(cache[N])%10007)