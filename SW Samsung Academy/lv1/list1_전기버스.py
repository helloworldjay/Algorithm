T = int(input())
# 결과를 담을 리스트
result = []
for _ in range(T):
    # K = 한번 충전으로 움직일 수 있는 최대 거리, N = 정류장 수, M = 충전기가 설치된 정류장 수
    K,N,M = map(int, input().split())
    # 충전기가 설치된 정류장
    charger_stop = list(map(int, input().split()))
    # 충전 횟수를 담을 변수
    time = 0
    # 반복을 통해 충전 횟수 찾기
    idx = 0
    while True:
        # 탈출 조건 형성(idx가 N보다 크거나 같으면 종료)
        if idx + K >= N:
            break
        # idx부터 idx + K 사이에 충전기가 있는 정류장 찾기
        is_Check = False
        for charger in range(idx+K, idx, -1):
            # charger가 주어진 정류장 안에 있을 경우
            if charger in charger_stop:
                idx = charger
                time += 1
                is_Check = True
                break
        # charger가 정류장에 없을 경우 -1을 결과로 하고 반복을 종료한다.
        
        if not is_Check:
            result.append(0)
            break
    if is_Check:
        result.append(time)

for i in range(T):
    print(f"#{i+1} {result[i]}")

