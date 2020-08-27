from collections import deque
def BFS(x, y):
    # BFS를 위한 큐
    queue = deque([(x,y)])
    # 시작 위치에서는 거리가 0
    distance[x][y] = 0
    # 상하우좌 확인
    dx,dy = [-1,1,0,0], [0,0,1,-1]
    # 큐에 자료가 있는 동안 순회
    while queue:
        row, col = queue.popleft()
        for i in range(4):
            xx, yy = row + dx[i], col + dy[i]
            # 상하좌우가 범위 안에 있으면서 아직 방문한 적이 없을 때
            if 0<=xx<N and 0<=yy<N and distance[xx][yy] == -1:
                # 벽(1)이 아니라면 distance를 갱신해주고 큐에 넣어준다.
                if maze[xx][yy] == 0:
                    distance[xx][yy] = distance[row][col] + 1
                    queue.append((xx,yy))
                elif maze[xx][yy] == 3:
                    distance[xx][yy] = distance[row][col]
                    return

# testcase 입력
T = int(input())
for idx in range(T):
    # 미로의 한 변의 길이를 입력받는다.
    N = int(input())
    # 미로를 입력받는다.
    maze = [list(map(int,list(input()))) for _ in range(N)]
    # 방문 여부를 확인하는 리스트
    distance = [[-1 for _ in range(N)] for i in range(N)]
    # 출발지 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                BFS(i, j)
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                if distance[i][j] == -1 :
                    print(f"#{idx+1} 0")
                else:
                    print(f"#{idx+1} {distance[i][j]}")
               





# # BFS하며 목적지 찾기
# def BFS(lst, x, y, visited, distance):
#     dx,dy = [1,-1,0,0], [0,0,1,-1]
#     for i in range(4):
#         xx = x + dx[i]
#         yy = y + dy[i]
#         # 박스 안에서 벗어나지 않는 범위 내에서
#         if 0<=xx<N and 0<=yy<N and not visited[xx][yy]:
#             # 방문을 표시
#             visited[xx][yy] = True
#             # 목적지를 찾으면 거리를 반환
#             if lst[xx][yy] == 3 :
#                 return distance
#             # 목적지가 아니라 0일 경우
#             elif lst[xx][yy] == 0 :
#                 # 거리가 1 늘어남
#                 distance += 1
#                 print(distance)
#                 BFS(lst, xx, yy, visited, distance)


# # testcase 입력
# T = int(input())
# for idx in range(T):
#     # 미로의 한 변의 길이를 입력받는다.
#     N = int(input())
#     # 미로를 입력받는다.
#     maze = [list(map(int,list(input()))) for _ in range(N)]
#     # 방문 여부를 확인하는 리스트
#     visited = [[False for _ in range(N)] for i in range(N)]
#     # 거리를 담을 변수
#     distance = 0
#     # 출발지 찾기
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2:
#                 result = BFS(maze, i, j, visited, distance)
#                 if result == None :
#                     print(f"#{idx+1} 0")
#                 else:
#                     print(f"#{idx+1} {result}")
                
