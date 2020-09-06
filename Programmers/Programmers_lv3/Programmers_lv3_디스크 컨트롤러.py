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
        # 현재 시간 이전에 들어온 작업들을 모은다
        for i in range(len(jobs)):
            x = heapq.heappop(jobs)
            # 이미 대기열에 있는 작업이면 temp에 넣는다
            if x[0] <= sec:
                temp.append(x)
                continue
            # 현재 시간 이후 작업이라면 아직 대기열에 없으므로 다시 넣어주고 끝낸다.
            else :
                # 이 작업을 하지않아 오류가 발생했다. 아직 대기열에 오지 않은 작업이므로 그냥 
                # break를 하면 작업 자체가 사라져버린다.
                heapq.heappush(jobs,x)
                break
        # 여기서 오류가 발생했다.
        # 반드시 작업들이 연결되어 있는 것이 아니기 때문에 현재 시간 기준으로 작업이 비어있을 수 있다.
        # 그런 경우 시간만 올려주어야한다.
        if len(temp) == 0:
            sec += 1
            continue
        # 작업들이 존재할 경우 완료 시간이 빠른 작업을 우선 꺼낸다.
        temp.sort(key = lambda x : x[1], reverse=True)
        t = temp.pop()
        # 작업 시간만큼 시간을 점프
        sec += t[1]
        # 대기시간을 계산하기 위해 작업 완료된 시점에서 프로세스에 올라온 시간을 뺀다.
        result.append(sec-t[0])
        # 작업의 개수를 한개 줄인다.
        cnt -= 1
        # 진행되지 않은 작업을 다시 heap에 넣는다.
        for i in range(len(temp)):
            heapq.heappush(jobs, temp[i])
    return sum(result)//len(result)

print(solution([[0, 3], [1, 9], [500, 6]]))

