from sys import stdin
input = stdin.readline
N = int(input())
N_list = list(map(int, input().split()))
cache = [0]*N # i번째 요소를 포함하는 부분 최대합 
cache[0] = N_list[0] 
max_num = cache[0]
for i in range(1, N):
    # i-1를 포함하는 연속 부분합 중 최대가 음수이면 앞부분은 어차피 버린다.
    cache[i] = max(0, cache[i-1]) + N_list[i]
    max_num = max(max_num, cache[i])
print(max_num)

# cache = [0]*(N+1)
# cache[1] = N_list[0]
# for i in range(1,N):
#     cache[i+1] = cache[i] + N_list[i]
# max_sum = -float('inf')
# for i in range(1,N+1):
#     for j in range(i):
#         if cache[i]-cache[j] > max_sum:
#             max_sum = cache[i]-cache[j]
# print(max_sum)