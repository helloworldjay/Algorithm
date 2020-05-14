def dfs(x, y):
    
    if miro[x][y] == 3:
        return 1
    else:
        dx, dy = [0,0,1,-1],[1,-1,0,0]
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<n and 0<=yy<n:
                if miro[xx][yy] == 0:
                    dfs(xx,yy)
    return 0
T = int(input()) # testcase
for i in range(T):
    n = int(input())
    miro = [list(map(int, input().split())) for _ in range(n)]
    start = []
    for j in range(n):
        for k in range(n):
            if miro[j][k] == 2:
                start = (j, k)
    dfs(start[0], start[1])