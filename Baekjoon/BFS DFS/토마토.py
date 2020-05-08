# 0을 기준으로 사방이 전부 -1이면 결과는 -1이 나와야한다. -> 이렇게 할 필요 없이 모든 연산 후 0 이 있나를 보면 된다..
from sys import stdin
from collections import deque
def bfs():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    sec = 0 
    while queue :
        sec += 1
        # 여기에서 그냥 큐를 꺼내는 것이 아니라 for문으로 주어진 큐만큼 반복을해서 sec를 고정시킨다..
        for _ in range(len(queue)): # 이렇게 되면 sec 기준으로 그당시에 존재하는 큐는 모두 같은 sec를 갖는다.
            [x,y] = queue.popleft()
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0<=xx and xx<n and 0<=yy and yy<m:
                    if farm[xx][yy] == 0 :
                        queue.append([xx,yy]) # 큐에 추가
                        farm[xx][yy] = 1 # 다시 계산하는 걸 방지하기위해 익은 것을 표현
    return sec
m, n = map(int, stdin.readline().strip().split()) # n 행, m 열
farm, queue = [], deque()
for i in range(n):
    temp = list(map(int, stdin.readline().strip().split()))
    for j in range(m):
        if temp[j] == 1:
            queue.append([i,j]) # 우선적으로 1인 값을 큐에 넣는다
result = bfs()
for i in range(n):
    for j in range(m):
        if farm[i][j] == 0 :
            print(-1)
            exit()
print(result)
