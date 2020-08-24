# 새로운 코드
# 범위가 매우 작으므로 for문을 여러번 중첩할 수 있었다.
# 기존에 비해 조건을 쉽게 정해 쉽게 구현할 수 있었다.
# SWEA 사이트에서는 stack overflow 문제가 발생한다.
# board를 선언할 때에 board = [[0]*10]*10 으로 설정하면 오류가 발생한다.

T = int(input()) #testcase의 수
for idx in range(T):
    n = int(input()) #색칠할 수 
    board = [[0]*10 for _ in range(10)]
    # 보라색 칸의 수
    cnt = 0
    # 색칠을 실행
    for c in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if board[i][j] != color and board[i][j] < 3:
                    board[i][j] += color
                    if board[i][j] == 3:
                        cnt += 1
    print(f"#{idx+1} {cnt}")
    

# 예전 코드

# T = int(input()) # testcase
# result = []
# for _ in range(T):
#     board = [[0 for i in range(10)] for j in range(10)] # 색칠할 판 초기화
#     N = int(input()) # 칠할 횟수
#     ctype = [[[] for i in range(10)] for j in range(10)] # 색칠된 색의 종류 
#     mxlen = 0 # 색깔 최대 개수 저장
#     for i in range(N):
#         x1, y1, x2, y2, c = map(int, input().split()) # (x1, y1), (x2, y2) c 색 종류
#         for x in range(x1, x2+1):
#             for y in range(y1, y2+1):
#                 if c not in ctype[x][y] : # 색칠이 되어있지 않을 경우에만 색칠
#                     board[x][y] += c
#                     ctype[x][y].append(c)
#                     if len(ctype[x][y]) > mxlen :
#                         mxlen = len(ctype[x][y])
#     ck = mxlen*(mxlen+1)//2 # 색 종류의 합
#     rlist = [(i,j) for i in range(10) for j in range(10) if board[i][j] == ck]
#     result.append(len(rlist))
# for i in range(T):
#     print("#{} {}".format(i+1, result[i]))
