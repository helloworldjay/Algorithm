import sys

input = sys.stdin.readline
n = int(input())
tower_list = list(map(int, input().split()))
stack = []
result = [0] * n
for i in range(n):
    tower = tower_list[i]
    while stack and tower_list[stack[-1]] < tower:
        stack.pop()
    if stack:
        result[i] = stack[-1] + 1
    stack.append(i)
print(' '.join(map(str, result)))
