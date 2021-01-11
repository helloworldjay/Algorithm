from sys import stdin, maxsize

input = stdin.readline
row, col = map(int, input().split())
chess_board = [[] for _ in range(row)]
for i in range(row):
    chess_board[i] = list(input().strip())


def check_board(word: str, row: int, col: int, chess_board) -> int:
    cnt = 0
    for i in range(row, row + 8):
        for j in range(col, col + 8):
            if i % 2 == 0:
                if j % 2 == 0 and chess_board[i][j] != word:
                    cnt += 1
                if j % 2 == 1 and chess_board[i][j] == word:
                    cnt += 1
            else:
                if j % 2 == 0 and chess_board[i][j] == word:
                    cnt += 1
                if j % 2 == 1 and chess_board[i][j] != word:
                    cnt += 1
    return cnt


cnt = maxsize
for i in range(0, row - 7):
    for j in range(0, col - 7):
        cnt = min(cnt, check_board("W", i, j, chess_board))
        cnt = min(cnt, check_board("B", i, j, chess_board))
print(cnt)