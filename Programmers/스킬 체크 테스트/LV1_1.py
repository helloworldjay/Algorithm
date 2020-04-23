def solution(N, stages):
    # 스테이지별 실패율 리스트 만들기
    fail = [0]
    # 1번부터 N까지 한칸씩 올라가며 실패율을 계산해 리스트에 넣기
    total = len(stages)
    for i in range(1, N+1):
        # 실패율 계산
        temp = stages.count(i)
        fail.append(temp/total)
        total -= temp
        if total <= 0:
            break
    # index와 함께 저장
    fail = [(idx, val) for idx, val in enumerate(fail)]
    # 실패율 기준으로 정렬
    fail.sort(key= lambda x : -x[1])
    # 0을 제외한 값 순서대로 뽑기
    ans = [fail[i][0] for i in range(len(fail)) if fail[i][0] != 0]    

    return ans
