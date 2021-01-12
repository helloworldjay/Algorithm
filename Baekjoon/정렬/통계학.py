from collections import Counter
from sys import stdin

input = stdin.readline
n = int(input())
n_list = [0 for _ in range(n)]
for i in range(n):
    n_list[i] = int(input())
n_list.sort()
# 산술평균
print(round(sum(n_list) / n))
# 중앙값
print(n_list[n // 2])
# 최빈값
n_counter = Counter(n_list)
sorted_list = sorted(n_counter.most_common(), key=lambda x: (-x[1], x[0]))
if len(sorted_list) == 1:
    print(sorted_list[0][0])
else:
    if sorted_list[0][1] == sorted_list[1][1]:
        print(sorted_list[1][0])
    else:
        print(sorted_list[0][0])
# 범위
print(n_list[-1] - n_list[0])
