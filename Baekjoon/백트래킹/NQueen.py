from sys import stdin

input = stdin.readline
N = int(input())
cnt = 0
placed = [-1 for i in range(N)]  # which col

def is_possible(i, j):
    for x in range(i):
        if j == placed[x] or (abs(i - x) == abs(j - placed[x])):
            return False
    return True

def backtracking(row):
    global cnt
    if row == N:
        cnt += 1
    else:
        for col in range(N):
            if is_possible(row, col):
                placed[row] = col
                backtracking(row+1)
                placed[row] = -1
backtracking(0)
print(cnt)


