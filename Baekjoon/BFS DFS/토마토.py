from sys import stdin
from collections import deque
input = stdin.readline
M, N = map(int, input().split())
farm = [ list(map(int, input().split())) for _ in range(N) ]
visited = [[-1 for i in range(M)] for j in range(N)]
cnt = 0 # 0의 개수
sec = 0 # 익는데 걸리는 시간
riping = deque()
temp = [] # 같은 시간안에 처리되어야할 목록
for i in range(N): # 0의 개수 구하기
    for j in range(M):
        if farm[i][j] == 0 : 
            cnt += 1
            visited[i][j] = 0
        if farm[i][j] == 1 : temp.append((i,j))
riping.append(temp)
def bfs(x,y):
    global cnt
    dx, dy = [-1,1,0,0], [0,0,1,-1]
    temp = []
    for i in range(4):
        xx,yy = x+dx[i], y+dy[i]
        if 0<=xx<N and 0<=yy<M:
            if visited[xx][yy] == 0 and farm[xx][yy] == 0:
                visited[xx][yy] = 1
                farm[xx][yy] = 1
                temp.append((xx,yy))
                cnt -= 1
    return temp    
while riping and cnt != 0:
    check = riping.popleft()
    sec += 1
    temp = []
    for i in range(len(check)):
        x, y = check[i]
        temp.extend(bfs(x,y))
    if len(temp) !=0 : riping.append(temp)
print(sec if cnt == 0 else -1)


