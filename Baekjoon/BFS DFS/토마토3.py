from sys import stdin
from collections import deque
input = stdin.readline
m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
days = 0
max_day = 0
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
def bfs():
    global max_day
    while visiting:
        x, y, z, day = visiting.popleft()
        for i in range(6):
            xx, yy, zz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= xx < m and 0 <= yy < n and 0 <= zz < h:
                if not visited[zz][yy][xx] and tomato[zz][yy][xx] == 0:
                    visited[zz][yy][xx] = True
                    tomato[zz][yy][xx] = 1
                    visiting.append((xx, yy, zz, day+1))
                    if day + 1 > max_day:
                        max_day = day + 1
def is_all_riped(tomato):
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomato[i][j][k] == 0:
                    return False
    return True
visiting = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                visiting.append((k, j, i, days))
bfs()
if is_all_riped(tomato):
    print(max_day)
else:
    print(-1)


