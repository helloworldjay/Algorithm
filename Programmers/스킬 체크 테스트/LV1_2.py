def solution(answers):
    # 수포자 3명의 정답 방식을 기록
    n1 = [1,2,3,4,5] # 5개
    n2 = [2,1,2,3,2,4,2,5] # 8개
    n3 = [3,3,1,1,2,2,4,4,5,5] # 10개
    sc = [0,0,0] # 점수
    for i in range(len(answers)) :
        if answers[i] == n1[i%5] :
            sc[0] += 1
        if answers[i] == n2[i%8] :
            sc[1] += 1
        if answers[i] == n3[i%10] :
            sc[2] += 1
    ans = [1,2,3]
    if sc.count(max(sc)) == 3:
        return ans
    elif sc.count(max(sc)) == 2:
        temp = []
        for i in range(len(sc)):
            if max(sc) != sc[i]:
                ans.remove(i+1)
                return ans    
    elif sc.count(max(sc)) == 1:
        return [sc.index(max(sc))+1]
print(solution([1,2,3,4,5]))