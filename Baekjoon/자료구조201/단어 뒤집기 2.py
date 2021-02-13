from sys import stdin
from collections import deque
input = stdin.readline
s = input().strip()
queue = deque()
stack = []
result = ""
isCheck = True
for c in s:
    if c == "<":
        isCheck = False
        queue.append(c)
        while stack:
            result += stack.pop()
    elif c == ">":
        isCheck = True
        queue.append(c)
        while queue:
            result += queue.popleft()
    elif c == " ":
        if isCheck:
            while stack:
                result += stack.pop()
            result += c
        else:
            queue.append(c)
    else:
        if isCheck:
            stack.append(c)
        else:
            queue.append(c)
while stack:
    result += stack.pop()
print(result)