from sys import stdin,setrecursionlimit
setrecursionlimit(100000)
input = stdin.readline
def dfs(x,y):
    dy = [-1,0,1,-1,0,1,-1,0,1]
    dx = [-1,-1,-1,0,0,0,1,1,1]
    for i in range(9):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<h and 0<=yy<w:
            if maps[xx][yy] == 1 and visited[xx][yy]==0:
                visited[xx][yy] = 1
                dfs(xx,yy)
        
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0 : break 
    maps = [list(map(int, input().split())) for _ in range(h)] # 지도
    visited = [[0 for i in range(w)] for j in range(h)] # 방문 여부 표시
    islands = 0  # 섬의 개수
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and visited[i][j] == 0: # 지도에서 땅이고 아직 방문하지 않은 지역이라면
                visited[i][j] = 1
                dfs(i,j)
                islands += 1
    print(islands)
