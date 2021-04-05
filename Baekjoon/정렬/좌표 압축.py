from sys import stdin

input = stdin.readline
N = int(input())
x_list = list(map(int, input().split()))
sorted_list = sorted(x_list)
result = [0 for _ in range(N)]
for i in range(N):
    result[i] = sorted_list.index(x_list[i])
print(' '.join(map(str, result)))
