import heapq

def solution(food_times, k):
    # 0이 아닌 최소값
    m = 100000000
    # 0이 아닌 요소의 길이
    N = 0
    for i in range(len(food_times)):
        if food_times[i] != 0:
            N += 1
            if food_times[i] < m:
                m = food_times[i]
    q, r = divmod(k, N)
    idx = 0
    # 최소값이 몫보다 크면 나머지만 생각하면 된다.
    if m >= q:
        for i in range(len(food_times)):
            food_times[i] -= q
            if food_times[i] != 0:
                r -= 1
                if r == 0:
                    return i + 1
    else :
        q -= m
        r += q*N
        while True:
            food_times[idx] -= m
            if food_times[idx] == 0:
                N -= 1
            elif food_times[idx] != 0:
                idx + 1
                r -= 1
            if r == 0:
                return (idx%len(N)) + 1
            
print(solution([3,1,2], 5))




# 정확도

# def solution(food_times, k):
#     total = sum(food_times)
#     idx = 0
#     while True:
#         if food_times[idx%(len(food_times))] != 0:
#             if k == 0:
#                 return (idx%len(food_times)) + 1
#             else:
#                 k -=1
#                 food_times[idx%(len(food_times))] -= 1
#                 total -= 1
#         if total == 0:
#             return -1
#         idx += 1
            

# print(solution([3,1,2], 5))

