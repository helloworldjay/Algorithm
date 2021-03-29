from sys import stdin
from collections import deque
input = stdin.readline
N, M = map(int, input().strip().split())
circle = deque([i for i in range(1, N+1)])
check_list = deque(list(map(int, input().strip().split())))
cnt = 0
while check_list:
    check_target = check_list.popleft()
    target_index = circle.index(check_target)
    if len(circle)//2 >= target_index:
        for _ in range(target_index):
            circle.append(circle.popleft())
            cnt += 1
    else:
        for _ in range(len(circle) - target_index):
            circle.appendleft(circle.pop())
            cnt += 1
    circle.popleft()
print(cnt)
