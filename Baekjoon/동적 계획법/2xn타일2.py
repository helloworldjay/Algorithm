from sys import stdin
N = int(stdin.readline())
cache = [0,1,3] + [0]*(N-2)
for i in range(3, N+1):
    cache[i] = (cache[i-2]*2 + cache[i-1])%10007
print(cache[N])
