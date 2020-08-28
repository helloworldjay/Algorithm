# 90도 회전
def rotate(lst):
    # N = 행, M = 열
    N = len(lst)
    M = len(lst[0])
    # 회전 된 후의 배열이므로 행과 열이 바뀐다.
    ret = [[0]*N for _ in range(M)]
    # 기존 열 번호가 행 번호가 되고, (행길이-1)에서 기존 행 번호를 빼준 값이 열 번호가 된다.
    for r in range(N):
        for c in range(M):
            ret[c][N-1-r] = lst[r][c]
    return ret

# 4개가 모두 같은 모양이면 위치를 저장한다.
def check(maze):
    # 행의 길이
    row = len(maze)
    # 열의 길이
    col = len(maze[0])
    # 위치를 저장
    result = []
    # 총 4방향을 체크한다.
    for i in range(row):
        for j in range(col):
            # 비교 대상 설정
            center = maze[i][j]
            # 2번째 이상 시행에서 빈칸을 제외하고 검색해야하므로 조건을 넣어준다.
            # 위치가 0이 아닌 곳에서 탐색
            if center != 0:
                # 상 좌
                # 상 좌가 가능하면
                if i > 0 and j > 0:
                    if center == maze[i][j-1] and center == maze[i-1][j] and center == maze[i-1][j-1]:
                        result.extend([(i,j), (i,j-1),(i-1,j),(i-1,j-1)])
                # 상 우
                if i > 0 and j < col-1:
                    if center == maze[i][j+1] and center == maze[i-1][j] and center == maze[i-1][j+1]:
                        result.extend([(i,j), (i,j+1),(i-1,j),(i-1,j+1)])
                # 하 좌
                if i < row-1 and j > 0:
                    if center == maze[i][j-1] and center == maze[i+1][j] and center == maze[i+1][j-1]:
                        result.extend([(i,j), (i,j-1),(i+1,j),(i+1,j-1)])
                # 하 우
                if i < row-1 and j < col-1:
                    if center == maze[i][j+1] and center == maze[i+1][j] and center == maze[i+1][j+1]:
                        result.extend([(i,j), (i,j+1),(i+1,j),(i+1,j+1)])
    return list(set(result))

def solution(m, n, board):
    board = rotate(board)
    # 전체 순회하며 범위 내에서 기준값을 잡고, 그 주변에 3쌍씩을 확인한다.
    # n이 행이되고 m이 열로 바뀐다. 
    # 0의 개수
    cnt = 0
    while True :
        result = check(board)
        # 0의 개수를 추가한다.
        cnt += len(result)
        # 겹치는 곳이 없다면 반복을 종료한다.
        if len(result) == 0:
            break
        # 전체 순회로 모두 저장한 뒤 해당값을 한번에 제거해준다.
        # 저장된 위치의 빈 칸에 구별 가능한 다른 요소를 채워준다.(예를 들어 0) 
        for result_idx in range(len(result)):
            row, col = result[result_idx]
            board[row][col] = 0
        # 제거하며 뒷부분의 요소들을 앞으로 당겨준다.
        for i in range(n):
            temp = []
            for j in range(m):
                if board[i][j] != 0:
                    # 아래와 같이 처리하면 안된다.. 0이 연속으로 올 경우 한칸 앞으로 당겨지면서
                    # 당겨진 0이 처리되지 못한다.
                    # board[i] = board[i][:j] + board[i][j+1:] + [0]
                    # 이것도 안된다.
                    # 그 이후를 순회하며 위치를 바꿔준다.
                    # for idx in range(j+1, m):
                    #     if board[i][idx] != 0:
                    #         board[i][j], board[i][idx] = board[i][idx], board[i][j]
                    temp.append(board[i][j])
            board[i] = temp + [0]*(n-len(temp))
    # (0의 개수) 출력
    return cnt
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))