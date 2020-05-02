t = int(input())
result = []
# 이동 가능한 거리내에 주유소가 있는지 확인
def isCheck(s):
    for i in range(len(s)-1, -1, -1):
        # 가장 먼 주유소 탐색
        if s[i] :
            return i
        return -1
for _ in range(t):
    # k = 한번 충전 최대 이동 거리, n = 총 정류장 개수, m = 충전기가 설치된 정류장 개수
    k, n, m = map(int, input().split())
    # 충전기가 설치된 정류장 받기
    temp = list(map(int, input().split()))
    mlist = [1 if i in temp else 0 for i in range(n+1)]
    i = 0 # 출발점
    cnt = 0 # 주유 횟수
    while True:
        if i+k+1 <= n+1:
            if 1 in mlist[i:i+k+1]:
                i += isCheck(mlist[i:i+k+1])
                cnt += 1