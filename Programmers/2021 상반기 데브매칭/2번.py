# def solution(rows, columns, queries):
#     import copy
#     board = [[0 for i in range(columns)] for j in range(rows)]
#     for i in range(rows):
#         for j in range(columns):
#             board[i][j] = i * columns + j + 1
#     result = []
#     for x1, y1, x2, y2 in queries:
#         testboard = [[0 for i in range(columns)] for j in range(rows)]
#         min_value = board[x1 - 1][y1 - 1]
#         for i in range(y1 - 1, y2 - 1):
#             testboard[x1 - 1][i + 1] = board[x1 - 1][i]
#             min_value = min(min_value, board[x1 - 1][i])
#         for i in range(y1, y2):
#             testboard[x2 - 1][i - 1] = board[x2 - 1][i]
#             min_value = min(min_value, board[x2 - 1][i])
#         for i in range(x1 - 1, x2 - 1):
#             testboard[i + 1][y2 - 1] = board[i][y2 - 1]
#             min_value = min(min_value, board[i][y2 - 1])
#         for i in range(x1, x2):
#             testboard[i - 1][y1 - 1] = board[i][y1 - 1]
#             min_value = min(min_value, board[i][y1 - 1])
#         result.append(min_value)
#         for i in range(0, rows):
#             for j in range(0,columns):
#                 if testboard[i][j] == 0:
#                     testboard[i][j] = board[i][j]
#         board = copy.deepcopy(testboard)
#     return result


def solution(rows, columns, queries):
    board = [[0 for i in range(columns)] for j in range(rows)]
    for i in range(rows):
        for j in range(columns):
            board[i][j] = i * columns + j + 1
    result = []
    for x1, y1, x2, y2 in queries:
        temp = [board[x1 - 1][y1 - 1], board[x1 - 1][y2 - 1], board[x2 - 1][y1 - 1], board[x2 - 1][y2 - 1]]
        min_value = min(temp)
        for i in range(y2-2, y1-1, -1):
            board[x1 - 1][i + 1] = board[x1 - 1][i]
            min_value = min(min_value, board[x1 - 1][i])
        for i in range(y1, y2 - 1):
            board[x2 - 1][i - 1] = board[x2 - 1][i]
            min_value = min(min_value, board[x2 - 1][i])
        for i in range(x2-2, x1-1, -1):
            board[i + 1][y2 - 1] = board[i][y2 - 1]
            min_value = min(min_value, board[i][y2 - 1])
        for i in range(x1, x2 - 1):
            board[i - 1][y1 - 1] = board[i][y1 - 1]
            min_value = min(min_value, board[i][y1 - 1])
        board[x1 - 1][y1], board[x1][y2 - 1], board[x2 - 2][y1 - 1], board[x2 - 1][y2 - 2] = temp[0], temp[1], temp[2], temp[3]
        result.append(min_value)
    return result


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100, 97, [[1,1,100,97]]))
