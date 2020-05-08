from sys import stdin
from collections import deque
T = int(stdin.readline()) # 테스트 케이스
result = [] # 개수 입력
def bfs(graph,x,y):
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    cnt = 0
    searching = deque()
    searching.append([x,y])
    while searching:
        temp = searching.popleft() # 검색 큐에서 검색 요소 추출
        [a, b] = temp
        for i in range(4):
            xx = a + dx[i]
            yy = b + dy[i]
            if xx>=0 and xx <N and yy >= 0 and yy<M:
                if graph[xx][yy] == 1 and ck[xx][yy] == 0:
                    searching.append([xx,yy])
                    ck[xx][yy] = 1
                    cnt += 1
    if cnt != 0 :
        return cnt    

for _ in range(T):
    M, N, K = map(int, stdin.readline().strip().split()) # 열, 행, 배추의 개수
    farm = [[0]*M for _ in range(N)] # 배추밭을 테스트 케이스마다 초기화
    ck = [[0]*M for _ in range(N)] # 위치를 방문했는지 여부 확인
    for i in range(K):
        tmpx, tmpy = map(int, stdin.readline().strip().split())
        farm[tmpy][tmpx] = 1  # 배추의 위치 1로 세팅
    tmplist = []
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1 and ck[i][j] == 0 :
                tmplist.append(bfs(farm,i,j))
    result.append(len(tmplist))
print('\n'.join(map(str,result)))
