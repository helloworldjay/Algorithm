# # baseball game 구현
# def baseballgame(candi,target):
#     s = 0
#     b = 0
#     for i in range(3):
#         if candi[i] == target[i]:
#             s += 1
#         else :
#             if candi[i] == candi[(i+1)%3] or candi[i] == candi[(i+2)%3]:
#                 b += 1
#     return [str(s), str(b)]


# def solution(baseball):
#     # 모든 경우의 수 탐색해서 불가능한 것 제거하는 구조
#     from itertools import permutations
#     # 1 ~ 9 까지 계산을 위한 리스트 생성
#     base = [str(i) for i in range(1,10)]
#     # test case 설정
#     tc = list(permutations(base,3))
#     for i in range(len(tc)):
#         tc[i] = ''.join(tc[i])
#     # baseball 요소마다 testcase와 비교하여 제거
#     result = tc[:]
#     for i in range(len(baseball)):
#         for j in range(len(tc)):
#             game = baseballgame(tc[j],str(baseball[i][0]))
#             if game != baseball[i][1:]:
#                 try :
#                     result.remove(tc[j])
#                 except:
#                     pass
#     return len(result)




def solution(progresses, speeds):
    # 걸리는 시간 리스트를 새로 생성한다.
    days = []
    import math
    for i in range(len(speeds)):
        days.append(math.ceil((100 - progresses[i])/speeds[i]))    
    
    # 항을 하나씩 꺼내 기준보다 작은경우 cnt를 증가시키며 다음으로 가고 더 크면 result에 cnt를 넣고 초기화한다. 
    result = []
    cnt = 1
    if days:
        mark = days[0] 
    for i in range(1, len(days)):
        if mark >= days[i]:
            cnt += 1
             
        else :
            result.append(cnt)
            cnt = 1 
            mark = days[i]
        if i == len(days)-1:
            result.append(cnt)   
        
    return result



