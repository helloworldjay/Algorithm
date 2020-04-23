def solution(bridge_length, weight, truck_weights):
    from collections import deque
    passed = []
    passing = deque()
    truck_weights = deque([[0, i] for i in truck_weights]) # truck weights에 시간 요소 추가
    sec = 0 # 초기 시간
    while True: # 주어진 트럭의 수와 지나간 트럭 목록의 수가 같을 때 stop
        sec += 1 # 현재 시간을 추가
        if passing:
            if sec - passing[0][0] == bridge_length: # 차가 진입한 순간 시간보다 현재 시간이 bridge_length 만큼 지났을 때
                passed.append(passing.popleft()) # 지나간 차 목록에 옮긴다.
        total = sum([passing[i][1] for i in range(len(passing))])
        if truck_weights: # 대기중인 트럭이 있다면
            if total + truck_weights[0][1] <= weight: # 다리가 무게를 버틸 수 있으면
                truck_weights[0][0] = sec # 현재 시간을 입력한다
                passing.append(truck_weights.popleft()) # 대기 트럭 목록에서 지나가는 트럭 목록으로 옮긴다.
        if not passing:
            break        
    return sec

print(solution(2, 10, [7, 4, 5, 6]))
# 속도 이슈 발생
# def solution(bridge_length, weight, truck_weights):
#     truck_weights = truck_weights[::-1]
#     bridge_list = [0]*bridge_length
#     sec = 0
#     while bridge_list :
#         sec += 1
#         bridge_list.pop()
#         insert = bridge_list.insert
#         if truck_weights :
#             if sum(bridge_list) + truck_weights[-1] <= weight :
#                 insert(0,truck_weights.pop())
#             else : 
#                 insert(0,0)
#     return sec