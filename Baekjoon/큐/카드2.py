from sys import stdin
input = stdin.readline
from collections import deque
dequeue = deque([i for i in range(1, int(input())+1)])
while len(dequeue) != 1:
    dequeue.popleft()
    dequeue.append(dequeue.popleft())
print(dequeue[0])
