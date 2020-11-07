def solution(n, board):
    position = {} # position of nums by row, col
    for i in range(len(board)):
        for j in range(len(board)):
            position[board[i][j]] = (i,j)
    move = 0 # times of movement
    target = 1 # heading to
    row, col = 0, 0 # start point
    while target <= n*n: # till visit everywhere
        x,y = position[target]
        move += (min(abs(row-x), n-abs(row-x)) + min(abs(col-y), n-abs(col-y))) + 1 # take minimum between (upside arrow, downside arrow), (rightside arrow, leftside arrow)
        row, col = x, y # repositioning start point
        target += 1 # head to next target
    return move

print(solution(4, [[11, 9, 8, 12], [2, 15, 4, 14], [1, 10, 16, 3], [13, 7, 5, 6]]))