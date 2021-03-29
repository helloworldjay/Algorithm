from sys import stdin
from collections import deque
input = stdin.readline
N, K = map(int, input().strip().split())
josephus = deque([str(i) for i in range(1, N+1)])
result = []
while josephus:
    for _ in range(K-1):
        josephus.append(josephus.popleft())
    result.append(josephus.popleft())
print('<'+', '.join(result)+'>')