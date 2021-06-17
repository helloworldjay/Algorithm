from sys import stdin
from bisect import bisect_left
input = stdin.readline
N = int(input())
A = list(map(int, input().split()))
ascending_partial_sequence = [A[0]] # 1< N 이므로 오류 발생 안함
for element in A:
    if ascending_partial_sequence[-1] < element:
        ascending_partial_sequence.append(element)
        continue
    index = bisect_left(ascending_partial_sequence, element)
    ascending_partial_sequence[index] = element
print(len(ascending_partial_sequence))







# dp = [1 for _ in range(N)]
# for i in range(1, N):
#     for j in range(i):
#         if A[j] < A[i]:
#             dp[i] = max(dp[j]+1, dp[i])
# print(max(dp))
