from sys import stdin

input = stdin.readline
stack = [0]
n = int(input())
result = [-1 for _ in range(n)]
A = list(map(int, input().strip().split()))
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        result[stack.pop()] = A[i]
    stack.append(i)
print(' '.join(map(str, result)))