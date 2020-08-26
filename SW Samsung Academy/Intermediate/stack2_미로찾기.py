# 0 통로, 1 벽, 2 출발점, 3 도착점
# 2에서 3으로 도착 가능하면 1, 아니면 0을 출력

# 주변에 3이 있는지 탐색하고, 없으면 0에서 다시 탐색하는 함수

def search(lst, x, y, check):
    global is_check
    # 하, 상, 좌, 우 검색
    dx, dy = [1,-1,0,0], [0,0,-1,1] 
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        # 주변 탐색이 구간을 벗어나지 않을 때 & 방문한 적이 없는 위치일 때
        if 0<=xx<len(lst) and 0<=yy<len(lst) and not check[xx][yy]:
            # 방문 여부를 갱신
            check[xx][yy] = True
            # 만약 도착한 곳이 목적지라면 가능 여부를 True로 바꿔준다.
            if lst[xx][yy] == 3 :
                is_check = True
            # 도착한 곳이 0이라면 갱신된 방문 여부를 가지고 다시 그 부분에서 체크를 진행한다.
            elif lst[xx][yy] == 0 :
                search(lst,xx,yy,check)

T = int(input())
for idx in range(T):
    N = int(input())
    # 미로 입력받기
    maze = [list(map(int, list(input()))) for _ in range(N)]
    # 방문 여부를 확인하는 리스트
    cache = [[False for _ in range(N)] for i in range(N)]
    # 3까지 도달 가능한지 여부 확인
    is_check = False
    for i in range(N):
        for j in range(N):
            # 출발지를 찾는다.
            if maze[i][j] == 2:
                search(maze, i, j, cache)
    if is_check:
        print(f"#{idx+1} 1")
    else:
        print(f"#{idx+1} 0")