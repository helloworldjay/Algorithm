from sys import stdin
input = stdin.readline
N = int(input())
cache = [[0,0] for _ in range(N+1)] # 0번째 인덱스 = i-1을 마셨을 때, 1번째 인덱스 = i-1을 안 마셨을 때
wine = [0]*(N+1)
for i in range(1,N+1):
    wine[i] = int(input())
cache[1][0],cache[1][1] = wine[1], wine[1]
if N >= 2: cache[2][0], cache[2][1] = wine[2] + wine[1], wine[2]
for i in range(3, N+1):
    cache[i] = [cache[i-1][1] + wine[i], max(cache[i-2]) + wine[i]] 
max_wine = 0
for i in range(N+1):
    if max_wine < max(cache[i]):
        max_wine = max(cache[i])
print(cache)
