
def solution(food_times, k):
    # 길이, 최소값 정의
    while True:
        N, m = 0, 100000001
        for i in range(len(food_times)):
            if food_times[i] != 0:
                N += 1
                if food_times[i] < m:
                    m = food_times[i]
        if N*m <= k and k >0 :
            k -= N*m
            for i in range(len(food_times)):
                if food_times[i] != 0:
                    food_times[i] -= m
                    if food_times[i] == 0:
                        N -= 1
        else:
            if N == 0:
                return -1
            q, r = divmod(k, N)
            for i in range(len(food_times)):
                if food_times[i] != 0:
                    if r == 0:
                        return i + 1
                    else:
                        r -= 1
            
            
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

