def solution(N, A):
    counters = [0 for _ in range(N+1)]
    # 임시 최대값
    temp_mx = 0
    # 저장될 최대값
    mx = 0
    
    for x in A:
        # N+1 일 땐 저장될 최대값을 갱신해준다.
        if x == N+1 :
            mx = temp_mx
        # N+1보다 작을 경우 
        else :
            # x 이전의 경우에 N+1이 나왓다면 mx가 갱신되었을 것이고 아니면 0이므로 1만 증가시켜준다.
            if counters[x] < mx :
                counters[x] = mx + 1
            # counters[x]가 mx보다 크다면 1만큼만 올려야한다. 이미 최대값인데 mx+1 만큼 증가될 수 있다. 
            else:
                counters[x] += 1
            # counters[x] 가 부분 최대값보다 크다면 갱신해준다.
            if counters[x] > temp_mx :
                temp_mx = counters[x]
            
    # 만약 N+1 이 나온 이후에 증가된 부분이 있다면 위에 if문에서 이미 mx + 1 로 처리가 되었다. 
    # 즉 mx보다 작은 모든 값은 N+1이 나온 이후에 갱신된 적이 없다는 뜻이므로 전체를 += mx가 아니라 = mx로 갱신하면 된다.
    for i in range(1, len(counters)):
        if counters[i] < mx :
            counters[i] = mx
    return counters[1:]