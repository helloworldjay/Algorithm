from sys import stdin
input = stdin.readline
div = 1000000000
N = int(input())
cache = [0, [0,1,1,1,1,1,1,1,1,1]] + [[0 for i in range(10)] for j in range(N-1)]
for i in range(2, N+1):
    for j in range(11):
        if j>0 and j<9:
            cache[i][j] = (cache[i-1][j-1] + cache[i-1][j+1])%div
        elif j == 0: cache[i][j] = cache[i-1][1]
        elif j == 9: cache[i][j] = cache[i-1][8]
print((sum(cache[N]))%div)