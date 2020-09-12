import copy
# 90도 회전
def rotate(ndarray):
    result = [[0 for _ in range(len(ndarray))] for _ in range(len(ndarray))]
    for i in range(len(ndarray)):
        for j in range(len(ndarray)):
            result[j][len(ndarray)-1-i] = ndarray[i][j]
    return result 

# 해당 key로 board를 돌았을 때 열리면 True, 아니면 False를 반환한다.
def check(key, board, N, M, i, j):
    # key를 기준으로 움직이며 board와 겹치는 부분을 갱신해준다.
    for x in range(N):
        for y in range(N):
            board[x+i][y+j] = (board[x+i][y+j]^key[x][y])
    # 결과 보기
    for x in range(N-1,N+M-1):
        for y in range(N-1,N+M-1):
            if board[x][y] == 0:
                return False
    return True

def solution(key, lock):
    # lock을 더 넓은 판으로 만들어준다. 
    N, M = len(key), len(lock)
    origin_board = [[0 for i in range(2*N+M-2)] for j in range(2*N+M-2)]
    # board의 가운데를 lock으로 만들어준다.
    for i in range(M):
        for j in range(M):
            origin_board[i+N-1][j+N-1] = lock[i][j]
    cnt = 3
    board = copy.deepcopy(origin_board)
    while cnt >= 0:
        # i,j는 각각 row와 col 방향으로 키가 board에서 얼만큼 움직였는지를 의미한다.    
        for i in range(N+M-1):
            for j in range(N+M-1):
                # board에서 key가 i, j 만큼 움직였을 때 board의 가운데 요소가 모두 1이면 열린다.
                if check(key,board,N,M,i,j): return True
                board = copy.deepcopy(origin_board)
        # 만약 안되면 키를 총 3번 회전시켜 다시 해본다.
        key = rotate(key)
        cnt -= 1        
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

