def num0(lst):
    l = 1
    for i in range(1,len(lst)):
        if lst[i] == 0 :
            l += 1
        else :
            return l
    return l 
def solution(stones,k):
    
        
    
    return

# # 정확성 실패
# def solution(stones, k):
#     n0 = "0"*k
#     cnt = 0
#     while True:
#         temp = ''.join(list(map(str,stones)))
#         print(temp)
#         if n0 in temp:
#             return cnt
#         cnt += 1
#         for i in range(len(stones)):
#             if stones[i] > 0:
#                 stones[i] -= 1
             

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))