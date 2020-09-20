from sys import stdin
input = stdin.readline
N = int(input())
wine = [int(input()) for _ in range(N)]
# cache[i] = i번째 와인을 마시는 경우 최대의 와인 합
# cache[i] = (i-2번째 와인까지 마신 최대의 합 and i-1 안마시기) or (i-3번째 최대 마신것 and wine[i-1]) + wine[i]
cache = [0 for _ in range(N)]
cache[0] = wine[0]
if N > 1: cache[1] = wine[0] + wine[1]
if N > 2 : cache[2] = max(wine[0]+ wine[2],wine[1]+ wine[2], wine[0]+wine[1]) 
for i in range(3, N):
    cache[i] = max(cache[i-2]+wine[i], cache[i-3]+wine[i-1]+ wine[i], cache[i-1]) 
print(cache[N-1])

# 틀린 코드
# 아래처럼 작성하면 100 100 10 10 100 100 의 경우 원래는 400이 되어야 최대인데
# 100 200 110 210 310 310이 된다. 즉 두번을 점프 뛰어야 하는 상황을 고려하지 못했다.
# from sys import stdin
# input = stdin.readline
# N = int(input())
# wine = [int(input()) for _ in range(N)]
# # cache[i] = i번째 와인을 마시는 경우 최대의 와인 합
# # cache[i] = (i-2번째 와인까지 마신 최대의 합 and i-1 안마시기) or (i-3번째 최대 마신것 and wine[i-1]) + wine[i]
# cache = [0 for _ in range(N)]
# cache[0] = wine[0]
# if N > 1: cache[1] = wine[0] + wine[1]
# if N > 2 : cache[2] = max(wine[0],wine[1]) + wine[2]
# for i in range(3, N):
#     cache[i] = max(cache[i-2], cache[i-3]+wine[i-1]) + wine[i]
# print(max(cache))