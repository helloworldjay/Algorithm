def solution(A):
    cars_to_east = 0 # 동쪽으로 가는 차의 수
    num_cross = 0 # 마주치는 횟수
    max_cross = 1000000000
    for i in range(len(A)):
        if A[i] == 0 : cars_to_east += 1
        else: num_cross += cars_to_east
    return num_cross if num_cross <= max_cross else -1
