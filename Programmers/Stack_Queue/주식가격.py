

# 효율성 실패, 시간 초과
# def solution(prices):
#     from collections import deque
#     result = [] # 기록 입력
#     ra = result.append
#     for i in range(len(prices)-1):
#         sec = 0
#         temp = deque(prices[i+1:])
#         while temp:
#             sec += 1
#             if temp.popleft() < prices[i]:
#                 break
#         ra(sec)
#     ra(0)
#     return result



# 속도 이슈 발생 O(n^2) 라서
def solution(prices):
    result = [[0 for i in range(len(prices))]] # 결과물 input
    for i in range(len(prices)-1): # 마지막 항 제거
        for j in prices[i+1:]:
            result[i] += 1
            if j < prices[i]:
                break
        
    
    return result