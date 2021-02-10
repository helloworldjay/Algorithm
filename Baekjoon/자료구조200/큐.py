from sys import stdin
from collections import deque

input = stdin.readline
queue = deque()
n = int(input())
for _ in range(n):
    order = input().strip()
    if order == "pop":
        print(queue.popleft() if queue else -1)
    elif order == "size":
        print(len(queue))
    elif order == "empty":
        print(0 if queue else 1)
    elif order == "front":
        print(queue[0] if queue else -1)
    elif order == "back":
        print(queue[-1] if queue else -1)
    else:
        queue.append(int(order[5:]))