time = int(input())
for t in range(time):
    k, n, m = map(int, input().split()) # 1회 충전 후 최대 이동 가능 거리, 총 정류장 개수, 충전 가능 정류장 개수
    chargelist = list(map(int, input().split())) # 충전 가능 정류장 위치
    start = 0 # 충전후 시작지점
    cnt = 0 # 충전 횟수
    i = 0 
    while True :
        if start + k < chargelist[i] :
            break
        elif start + k > chargelist[i] : # 다음 정류소로 간다
            i += 1
            continue
        elif start + k == chargelist[i] : # 여기서 충전
            start += k
            cnt += 1
            i += 1
            continue
        else : # 여기 하나 전 정류소에서 충전
            start += k
            cnt += 1
            continue
        if i > m - 1 :
            break
    print("#{} {}".format(t+1, cnt))
    

     