def solution(heights):
    answerlist = [0]*len(heights) # list의 값을 0으로 초기화
    for i in range(len(heights)-1,0,-1): # 가장 오른쪽 값부터 체크
        for j in range(1, i+1): # 한칸 왼쪽부터 더 큰값이 나올때까지 비교
            if heights[i] < heights[i-j]:
                answerlist[i] = i-j+1
                break # 처음으로 나온 것을 저장하기 위해 비교를 멈추어야 한다.
    return answerlist
print(solution([6,9,5,7,4]))
        