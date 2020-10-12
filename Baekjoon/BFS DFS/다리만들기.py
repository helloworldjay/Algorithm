from sys import stdin,setrecursionlimit
from collections import deque
input = stdin.readline
setrecursionlimit(100000)
N = int(input())
maps = [ list(map(int, input().split())) for _ in range(N) ]
visited = [ [0 for i in range(N)] for j in range(N) ] # 방문 체크
islands = [ [0 for i in range(N)] for j in range(N) ] # 섬 번호
island_num = 0 # 섬 번호
def bfs(i,j,island_num):
    global border
    visited[i][j] = 1
    islands[i][j] = island_num # 섬 번호 배정
    di, dj = [1,-1,0,0], [0,0,1,-1]
    if maps[i][j] == 1 :
        for k in range(4):
            ii, jj = i+di[k], j+dj[k]
            if 0<=ii<N and 0<=jj<N and maps[ii][jj] == 0 :
                border[island_num] = border.get(island_num, deque()) + deque([(i,j)])
                break
    for k in range(4):
        ii, jj = i+di[k], j+dj[k]
        if 0<=ii<N and 0<=jj<N and maps[ii][jj] == 1 and visited[ii][jj]==0:
            bfs(ii,jj,island_num)
border = {}
for i in range(N):
    for j in range(N):
        if visited[i][j] != 1 and maps[i][j] == 1: # 방문을 안했고 섬이면
            island_num += 1 # 섬 번호 증가
            bfs(i,j,island_num)
min_len = 201
def bfs2(visiting):
    visited = [ [0 for i in range(N)] for j in range(N) ] # 방문 체크
    dx, dy = [-1,1,0,0],[0,0,1,-1]
    color = islands[visiting[0][0]][visiting[0][1]]
    distance = 0
    while True:
        temp = deque()
        while visiting:    
            x,y = visiting.popleft()
            visited[x][y] = 1
            for i in range(4):
                xx, yy = x + dx[i], y + dy[i]
                if 0<=xx<N and 0<=yy<N and visited[xx][yy] == 0:
                    if islands[xx][yy] !=0 and islands[xx][yy] != color:
                        return distance
                    elif islands[xx][yy] == 0:
                        temp.append((xx,yy))
        visiting = temp
        distance += 1
for i in range(1,island_num+1):
    border_list = border[i]
    distance = bfs2(border_list)
    if distance < min_len : min_len = distance
print(min_len)




# from sys import stdin
# from collections import deque
# input = stdin.readline
# N = int(input())
# maps = [list(map(int, input().split())) for _ in range(N)]
# island = [[0 for i in range(N)] for j in range(N)]
# visited = [[0 for i in range(N)] for j in range(N)]
# island_num = 1
# def bfs1(x,y,island_num):
#     visited[x][y] = 1
#     island[x][y] = island_num
#     dx,dy = [1,-1,0,0], [0,0,-1,1]
#     for i in range(4):
#         xx,yy = x+dx[i], y+dy[i]
#         if 0<=xx<N and 0<=yy<N:
#             if maps[xx][yy] == 1 and visited[xx][yy] == 0:
#                 island[xx][yy] = island_num
#                 bfs1(xx,yy,island_num)
# for i in range(N):
#     for j in range(N):
#         if maps[i][j] == 1 and visited[i][j] == 0:
#             bfs1(i,j,island_num)
#             island_num += 1
# min_len_bridge = 201 # 다리의 최대 길이

# def bfs2(visiting, color):
#     visited = [[0 for i in range(N)] for j in range(N)]
#     distance = 0
#     while visiting:
#         check_islands = visiting.popleft()
#         temp = []
#         for i in range(len(check_islands)):
#             x, y = check_islands[i]
#             visited[x][y] = 1
#             if island[x][y] != 0 and island[x][y] != color: # 다른 섬에 도달
#                 return distance
#             elif island[x][y] == 0: #섬이 아니라 바다
#                 dx,dy = [1,-1,0,0], [0,0,-1,1]
#                 for j in range(4):
#                     xx, yy = x+dx[j], y+dy[j]
#                     if 0<=xx<N and 0<=yy<N and visited[xx][yy]==0:
#                         temp.append((xx,yy))
#         if len(temp) != 0 : visiting.append(temp)
#         distance += 1
#     return -1
# check_border = []
# for check_num in range(1, island_num):
#     temp = []
#     for i in range(N):
#         for j in range(N):
#             if island[i][j] == check_num:
#                 di, dj = [1,-1,0,0], [0,0,-1,1]
#                 for k in range(4):
#                     ii ,jj = i+di[k], j+dj[k]
#                     if 0<=ii<N and 0<=jj<N and island[ii][jj] == 0:
#                         temp.append((i,j))
#     check_border.append(temp)

# for x in range(len(check_border)): # 섬 번호
#     for y in range(len(check_border[x])): # 특정 섬 번호에서 검색해봐야할 좌표
#         i, j = check_border[x][y]
#         visiting = deque()
#         di,dj = [1,-1,0,0], [0,0,-1,1]
#         temp = []
#         for k in range(4):
#             ii,jj = i+di[k], j+dj[k]
#             if 0<=ii<N and 0<=jj<N and maps[ii][jj] == 0:
#                 temp.append((ii,jj))
#         visiting.append(temp)
#         color = island[i][j]
#         distance = bfs2(visiting,color)
#         if distance != -1 and min_len_bridge > distance : min_len_bridge = distance
# print(min_len_bridge)
            
