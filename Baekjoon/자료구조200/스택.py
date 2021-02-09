from sys import stdin

input = stdin.readline
n = int(input())
stack = []
for _ in range(n):
    check = input().strip()
    if check == "top":
        print(stack[-1] if stack else -1)
    elif check == "empty":
        print(0 if stack else 1)
    elif check == "size":
        print(len(stack))
    elif check == "pop":
        print(stack.pop() if stack else -1)
    else:
        stack.append(check.split()[1])