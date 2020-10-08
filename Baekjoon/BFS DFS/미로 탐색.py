from sys import stdin
from collections import deque
input = stdin.readline
N, M = map(int, input().split())
maze = [list(map(int, list(input().strip()))) for _ in range(N)]
visiting = deque([(0,0)])
visited = [[False for i in range(M)] for j in range(N)]
dx, dy = [0,0,-1,1], [1,-1,0,0]
while visiting:
    x, y = visiting.popleft()
    visited[x][y] = True
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if 0<=xx<N and 0<=yy<M:
            if maze[xx][yy] == 1 and visited[xx][yy] == False:
                visiting.append((xx,yy))
                maze[xx][yy] += maze[x][y]
print(maze[N-1][M-1])
    







# def main():
#     n, m = map(int, stdin.readline().strip().split()) # n행 m열
#     miro = []
#     ck = [[0]*m for _ in range(n)]
#     # 미로 입력받기
#     for i in range(n):
#         miro.append(list(map(int,list(stdin.readline().strip()))))
#     # bfs
#     searching = deque([[0,0]])
#     dx = [-1,1,0,0]
#     dy = [0,0,1,-1]
#     ck[0][0] = 1
#     while searching:
#         temp = searching.popleft()
#         x, y  = temp[0], temp[1]
#         if x == n-1 and y == m-1:
#             break
#         for i in range(4):
#             xx = x + dx[i]
#             yy = y + dy[i]
#             if xx>= 0 and xx<n and yy>=0 and yy<m:
#                 if ck[xx][yy] == 0 and miro[xx][yy] == 1:
#                     ck[xx][yy] = ck[x][y] + 1
#                     searching.append([xx,yy])
#     print(ck[n-1][m-1])        





# if __name__ == "__main__":
#     main()