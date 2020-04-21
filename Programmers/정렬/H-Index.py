def solution(citations):
    citations.sort()
    h_index = 0 # h index를 초기화
    for i in range(len(citations)):
        if citations[i] <= len(citations)-i: # 요소 값이 남은 자리 개수보다 작을 때 성립
            h_index = citations[i]
    return h_index

print(solution([3,0,6,1,5]))