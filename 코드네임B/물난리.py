import copy
# 물의 위치를 한 칸 이동시키는 함수
def water(origin, pos):
    lst = copy.deepcopy(origin)
    dx, dy = [0,0,-1,1], [1,-1,0,0]
    # 다음 이동할 위치를 저장
    new_pos = []
    # 물이 고여있는 위치를 탐색
    for p in range(len(pos)):
        x, y = pos[p]
        # 사방 탐색
        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            # 물이 이동할 수 있으며 집 안의 범위이면 물이 한칸 이동
            # 새롭개 물이 고인 위치를 갱신
            if 0<=xx<N and 0<=yy<N and lst[xx][yy] == 0:
                lst[xx][yy] = 3
                new_pos.append((xx,yy))
    return lst, new_pos

# 안전지대 체크(물을 다 채우고 0의 개수를 확인하는 함수)
def check(origin):
    global max_safe
    lst = copy.deepcopy(origin)
    temp_safe = 0
    dx, dy = [0,0,-1,1], [-1,1,0,0]
    for x in range(len(lst)):
        for y in range(len(lst[0])):
            if lst[x][y] == 3:
                for i in range(4):
                    xx, yy = x + dx[i], y+dy[i]
                    if 0<=xx<len(lst) and 0<=yy<len(lst[0]) and lst[xx][yy]==0:
                        lst[xx][yy] = 3
    # 전체 0의 개수 계산
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == 0:
                temp_safe += 1
    if temp_safe > max_safe:
        max_safe = temp_safe 

# 홍현을 이동시키는 함수
def Hong(lst,xy):
    # xy는 홍현이 존재할 수 있는 위치의 후보군
    di, dj = [0,0,-1,1], [1,-1,0,0]
    # pos는 홍현이가 위치할 수 있는 후보군 
    pos = []
    for x in range(len(xy)):
        i, j = xy[x]    
        # 홍현이의 현재 위치
        visited[i][j] = 1
        # 사방 체크
        for d in range(4):
            ii, jj = i + di[d], j + dj[d]
            if 0<=ii<len(lst) and 0<=jj<len(lst[0]) and lst[ii][jj] == 0 and visited[ii][jj] == 0:
                # 위치 이동
                lst[i][j] = 0
                lst[ii][jj] = 2
                # 안전지대 체크(물을 다 채우고 0의 개수를 확인하는 함수)
                check(lst)
                pos.append((ii,jj))
                lst[ii][jj] = 0
    return lst, pos
N = int(input())
# 집 상태를 입력 받음
house = [list(map(int, input().split())) for _ in range(N)]
# 물의 위치는 3, 홍현의 위치는 2로 표현한다.
house[0][0], house[N-1][N-1] = 3, 2
pos = [(0,0)]
hong_pos = [(N-1,N-1)]
visited = [[0 for i in range(N)] for j in range(N)]
cnt = 0
# 안전한 위치의 최대값을 저장할 변수1
max_safe = -1
# 조건이 완성될 때까지 물을 한칸씩 이동
while True :
    # 물이 한번 이동한 후 집 상태와 새롭게 물이 샌 위치를 출력
    flooded_house, pos = water(house,pos)
    # 종료 조건 : 물이 더이상 움직일 수 없을 때
    if house == flooded_house or cnt > (N**2):
        break
    # 홍현을 이동시키는 함수
    # 홍현을 한번 이동시킬 때마다 물을 다 채우고 max_safe를 갱신하고 다시 이동시킨다.
    house,hong_pos = Hong(flooded_house,hong_pos)
    cnt += 1
print(max_safe)