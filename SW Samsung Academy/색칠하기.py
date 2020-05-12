T = int(input()) # testcase
result = []
for _ in range(T):
    board = [[0 for i in range(10)] for j in range(10)] # 색칠할 판 초기화
    N = int(input()) # 칠할 횟수
    ctype = [[[] for i in range(10)] for j in range(10)] # 색칠된 색의 종류 
    mxlen = 0 # 색깔 최대 개수 저장
    for i in range(N):
        x1, y1, x2, y2, c = map(int, input().split()) # (x1, y1), (x2, y2) c 색 종류
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if c not in ctype[x][y] : # 색칠이 되어있지 않을 경우에만 색칠
                    board[x][y] += c
                    ctype[x][y].append(c)
                    if len(ctype[x][y]) > mxlen :
                        mxlen = len(ctype[x][y])
    ck = mxlen*(mxlen+1)//2 # 색 종류의 합
    rlist = [(i,j) for i in range(10) for j in range(10) if board[i][j] == ck]
    result.append(len(rlist))
for i in range(T):
    print("#{} {}".format(i+1, result[i]))
