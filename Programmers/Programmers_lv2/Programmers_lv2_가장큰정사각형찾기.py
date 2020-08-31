def solution(board):
    row = len(board)
    col = len(board[0])
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1],min(board[i-1][j],board[i][j-1])) + 1
    return max([board[x][y] for x in range(row) for y in range(col)])**2




# # # 모든 요소가 1인지 확인하는 함수
# def is_check(arry):
#     for i in range(len(arry)):
#         for j in range(len(arry[0])):
#             # 하나라도 0이면 False
#             if arry[i][j] == 0:
#                 return False
#     return True

# def partial(board, row, col, testside):
#     new_board = [[0 for i in range(testside)] for j in range(testside)]
#     for i in range(0, testside):
#         for j in range(0, testside):
#             new_board[i][j] = board[row+i][col+j]
#     return new_board

# def solution(board):
#     side = 0
#     N, M = len(board), len(board[0])
#     # 잘라서 정사각형인지 체크하는 isCheck 함수 만들기
#     for i in range(N):
#         for j in range(M):
#             test_side = min(N-i, M-j)
#             if side > test_side:
#                     break
#             while test_side > 0:
#                 partial_board = partial(board,i,j,test_side)
#                 if is_check(partial_board) and test_side > side:
#                     side = test_side
#                     break
#                 test_side -= 1
#     return side**2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
