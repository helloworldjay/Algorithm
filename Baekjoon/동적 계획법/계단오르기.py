import sys
input = sys.stdin.readline

N = int(input())
# 각 계단의 점수
stairs = [int(input()) for _ in range(N)]
def stair(N, stairs):
    stairs = [0] + stairs
    if N == 1:
        return stairs[1]
    elif N == 2:
        return stairs[2]+stairs[1]
    elif N == 3:
        return stairs[3]+max(stairs[1],stairs[2])
    # i번째 계단을 밟았을 때 그 때까지의 최고 점수
    score = [0 for i in range(N+1)]
    score[1], score[2], score[3] = stairs[1], stairs[2]+stairs[1], stairs[3]+max(stairs[1],stairs[2])
    # 연속된 세개의 계단을 모두 밟아선 안된다
    for i in range(4, N+1):
        score[i] = max(stairs[i-1]+score[i-3],score[i-2]) + stairs[i]
    return score[-1]    

print(stair(N,stairs))