from sys import stdin
input = stdin.readline
N = int(input())
N_list = list(map(int, input().split()))
rev_list = N_list[::-1]
cache = [1] * N
cache2 = [1] * N
for i in range(1, N):
    for j in range(i):
        if N_list[i] > N_list[j]:
            cache[i] = max(cache[i], cache[j]+1)
        if rev_list[i] > rev_list[j]:
            cache2[i] = max(cache2[i], cache2[j]+1)
cache2 = cache2[::-1]
for i in range(N):
    cache[i] += cache2[i]-1
print(max(cache))
