def solution(bridge_length, weight, truck_weights):
    passing_truck = []
    passed_truck = []
    ingappend = passing_truck.append
    edappend = passed_truck.append
    sec = 0
    while True :
        if len(passing_truck) == 0 and len(truck_weights) == 0 :
            return sec
        sec += 1
        for i in range(len(passing_truck)):
            passing_truck[i][0] += 1
        if truck_weights[0] + sum(passing_truck) <= weight :    
            ingappend([sec, truck_weights.leftpop()])
        if passing_truck[0][0]
    while passing_truck :
        
    return

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