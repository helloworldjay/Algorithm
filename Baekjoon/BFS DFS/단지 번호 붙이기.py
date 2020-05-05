# 2667번
n = int(input())
a = [list((map(int, list(input())))) for _ in range(n)]

dx = [-1,1,0,0] # 좌, 우, 아래, 위
dy = [0,0,-1,1]
apt = []
cnt = 0

def dfs(x,y):
    global cnt # 바깥의 변수 가져오기
    a[x][y] = 0 # 방문하면 재방문 방지를 위해 0으로 갱신
    cnt += 1 # 단지의 길이
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx>= 0 and nx < n and ny>=0 and ny < n:
            if a[nx][ny] == 1 :
                dfs(nx,ny) 
    return cnt
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            cnt = 0 # 초기화
            apt.append(dfs(i,j))
apt.sort()
print(len(apt))
for i in range(len(apt)):
    print(apt[i])
                