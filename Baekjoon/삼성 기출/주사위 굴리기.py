n, m, x, y, k = map(int, input().split())
B = []
for i in range(n):
    B.append(list(map(int,input().split())))
dice = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]] # 주사위 [1][1] 이 바닥
def roll(k): # 주사위의 바닥은 1행 1열에 고정하고 전체를 이동시킴
    global dice
    if k == 1:
        dice[1][0], dice[1][1], dice[1][2] = dice[1][1], dice[1][2], dice[1][0]    
    elif k == 2:
        dice[1][0], dice[1][1], dice[1][2] = dice[1][1], dice[1][2], dice[1][0]
    elif k == 3:
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]
    elif k == 4:
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]
    
order = list(map(int,input().split()))
for o in order:
    if o == 1:
        y += 1
        if y >= m:
            continue
        if B[x][y] != 0:
            roll(o)
            dice[1][1] = B[x][y]
        else :
            roll(o)
            B[x][y] = dice[1][1]
    elif o == 2:
        y -= 1
        if y < 0:
            continue
        if B[x][y] != 0:
            roll(o)
            dice[1][1] = B[x][y]
        else :
            roll(o)
            B[x][y] = dice[1][1]
    elif o == 3:
        x -= 1
        if x < 0:
            continue
        if B[x][y] != 0:
            roll(o)
            dice[1][1] = B[x][y]
        else :
            roll(o)
            B[x][y] = dice[1][1]
    elif o == 4:
        x += 1
        if x >= n:
            continue
        if B[x][y] != 0:
            roll(o)
            dice[1][1] = B[x][y]
        else :
            roll(o)
            B[x][y] = dice[1][1]
    print(dice[3][1])