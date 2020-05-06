T = int(input())
F, ck = [], []
dx, dy = [-1,1,0,0], [0,0,1,-1]
def bfs(x,y):
    for i in range(4):
        ck[x][y] = 1
        xx = x + dx[i]
        yy = y + dy[i]
        if F[xx][yy] == 0 or ck[xx][yy]:
            continue
        bfs(xx,yy)


def process():
    m,n,k = map(int, input().split())
    F = [[0]*(m+2) for _ in range(n+2)] # 양쪽으로 1씩 채워서 2를 더해주면 벗어나는 조건을 추가할 필요가 없다.
    ck = [[0]*(m+2) for _ in range(n+2)]
    for _ in range(k):
        a, b = map(int, input().split())
        F[a+1][b+1] = 1
        ans = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if F[i][j] ==0  or ck[i][j]:
                continue
            bfs(i,j)
            ans += 1
    print(ans)
                    
                
for _ in range(T):
    process()
      