
def solution(food_times, k):
    # 음식의 총량
    total = sum(food_times)
    # 남은 음식보다 k가 크면 -1을 출력
    if total <= k:
        return -1
    for i, ele in enumerate(food_times):
        food_times[i] = (ele, i)
    food_times.sort(key= lambda x: (x[0],x[1]))
    ft_len = len(food_times)
    idx = 0
    # 연산 전에 빼줘야할 숫자
    discount = 0
    while True:
        # idx번째로 작은 요소의 남은 음식
        temp = food_times[idx][0] - discount
        # 만약 남은 음식의 길이*temp 보다 먹어야될 횟수가 크면 그만큼을 빼준다.
        if temp*ft_len <= k:
            discount += temp
            # 첫번째 값만큼 전체 빼주기 때문에 
            food_times[idx] = (0, food_times[idx][1])
            k -= temp*ft_len
            ft_len -= 1
            idx +=1
        # 만약 모든 요소를 돌 수 없다면
        else:
            r = k%ft_len
            food_times.sort(key=lambda x : x[1])
            for i in range(len(food_times)):
                if food_times[i][0] != 0:
                    r -= 1
                if r == -1:
                    return i+1
            
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