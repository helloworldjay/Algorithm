import heapq
def solution(jobs):
    heapq.heapify(jobs)
    # 작업의 수
    cnt = len(jobs)
    # 시간을 나타내는 변수
    sec = 0
    # 결과를 담을 변수
    result = []
    while cnt > 0:
        # 후보군에서 제외될 때에 담겨질 변수
        temp = []
        for i in range(len(jobs)):
            x = heapq.heappop(jobs)
            if x[0] <= sec:
                temp.append(x)
                continue
            else :
                break
        temp.sort(key = lambda x : x[1],reverse=True)
        x = temp.pop()
        sec += x[1]
        result.append(sec-x[0])
        cnt -= 1
        for i in range(len(temp)):
            heapq.heappush(jobs, temp[i])                
    return result

print(solution([[0, 3], [1, 9], [2, 6]]))