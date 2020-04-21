# enumerate 학습 
def solution(answers):
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    list1 = [1,2,3,4,5]
    list2 = [2,1,2,3,2,4,2,5]
    list3 = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)) :
        if list1[i%5] == answers[i] :
            cnt1 += 1
        if list2[i%8] == answers[i] :
            cnt2 += 1
        if list3[i%10] == answers[i] :
            cnt3 += 1
    cnt = [cnt1, cnt2, cnt3]
    maxnum = cnt.count(max(cnt))
    if maxnum == 1 :
        answer = [cnt.index(max(cnt))+1]
        return answer
    elif maxnum == 2 :
        for i in range(3):
            if cnt[i] != max(cnt) :
                answer = [1,2,3]
                del answer[i]
                return answer
    else :
        answer = [1,2,3]
        return answer

print(solution([1,3,2,4,2]))
    

#enumerate 사용
def solution(answers):
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    list1 = [1,2,3,4,5]
    list2 = [2,1,2,3,2,4,2,5]
    list3 = [3,3,1,1,2,2,4,4,5,5]
    answer =[]
    for i in range(len(answers)) :
        if list1[i%5] == answers[i] :
            cnt1 += 1
        if list2[i%8] == answers[i] :
            cnt2 += 1
        if list3[i%10] == answers[i] :
            cnt3 += 1
    cnt = [cnt1, cnt2, cnt3]
    for i, value in enumerate(cnt):
        if value == max(cnt):
            answer.append(i+1)
            
    return answer