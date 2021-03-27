from sys import stdin
input = stdin.readline
K = int(input())
stack = []
for _ in range(K):
    num = int(input())
    if num:
        stack.append(num)
    else:
        stack.pop()
result = 0
while stack:
    result += stack.pop()
print(result)