from collections import deque
from sys import stdin

input = stdin.readline
queue = deque()
n = int(input())
for _ in range(n):
    order = input().strip()
    if order == "size":
        print(len(queue))
    elif order == "empty":
        print(0 if queue else 1)
    elif order == "front":
        print(queue[0] if queue else -1)
    elif order == "back":
        print(queue[-1] if queue else -1)
    elif order.startswith("push_front"):
        main, num = order.split()
        queue.appendleft(num)
    elif order.startswith("push_back"):
        main, num = order.split()
        queue.append(num)
    elif order.startswith("pop_front"):
        print(queue.popleft() if queue else -1)
    elif order.startswith("pop_back"):
        print(queue.pop() if queue else -1)