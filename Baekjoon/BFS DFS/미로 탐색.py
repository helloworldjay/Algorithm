import sys
sys.setrecursionlimit(1000)
n, m = map(int, input().split()) # n행 m열
A = []
for _ in range(n):
    A.append(list(map(int,list(input()))))
ck = [[0]*m for _ in range(n)]
cnt = 0
def bfs(graph, x, y):
    global cnt
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    if graph[x][y] == 1 and ck[x][y] == 0:
        cnt += 1
        ck[x][y] += cnt
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx>= 0 and xx <n and yy >= 0 and yy < m:
            if graph[xx][yy] == 1:
                bfs(graph,xx,yy)
             
bfs(A,0,0)
print(ck[n-1][m-1])
