from sys import stdin
from collections import deque

input = stdin.readline
isCheck = True
queue = deque()
stack = []
result = ''
s = input().strip()
for i in s:
    if i == "<":
        while stack:
            result += stack.pop()
        queue.append(i)
        isCheck = False

    elif i == ">":
        queue.append(i)
        isCheck = True
        while queue:
            result += queue.popleft()

    elif i == " ":
        if isCheck:
            while stack:
                result += stack.pop()
            result += i
        else:
            queue.append(i)
            while queue:
                result += queue.popleft()

    else:
        if isCheck:
            stack.append(i)
        else:
            queue.append(i)
while stack:
    result += stack.pop()
print(result)
