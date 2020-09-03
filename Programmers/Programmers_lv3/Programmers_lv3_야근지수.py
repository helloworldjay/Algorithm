def solution(n,works):
    # 요소를 다 합친 값보다 줄일 수 있는 값이 더크면 결국 모두 0이 된다.
    if sum(works) <= n:
        return 0
    works.sort(reverse = True)
    for i in range(len(works)-1):
        # 같은 값들과 안같은 값의 경계 차이
        diff = works[i] - works[i+1]
        # n이 i+1개 요소를 바꾸는 것보다 더 크면 i+1개의 요소를 
        # i+2 요소와 같은 숫자로 전부 바꿔준다.
        if diff*(i+1) < n:
            works[:i+1] = [works[i+1] for _ in range(i+1)]
            n -= diff*(i+1)
        # 만약 i+1개의 요소를 다 바꿀만큼 n이 남지 않았다면
        else :
            q, r = divmod(n, (i+1))
            # 뺄 수 있는 만큼 최대한 똑같이 뺀다.
            works[:i+1] = [works[j]-q for j in range(i+1)]
            # 남은 숫자만큼 빼는데 어차피 이 때에는 정렬상태가 중요하지 않으므로 
            # 그냥 r개를 뺀다.
            works[:r] = [works[j]-1 for j in range(r)]
            # n만큼 다 뺐으므로 n을 초기화
            n = 0
            break
    # 모든 요소가 같을 경우 위를 돌아도 n이 제거되지 않는다(차이를 기반으로 하므로)    
    if n != 0:
        # 공평하게 다 빼주고 남은 요소를 제거한다.
        q2, r2 = divmod(n, len(works))
        works = [works[idx]-q2 for idx in range(len(works))]
        works[:r2] = [works[j]-1 for j in range(r2)]
    result = 0
    for i in range(len(works)):
        result += (works[i])**2
    return result



# def binary_search(ele, lst, start, end):
#     mid = (start+end)//2
#     if lst[mid] == ele:
#         return mid
#     if end-start == 1 and lst[start] < ele:
#         return end 
#     if end == start:
#         return end    
#     elif ele > lst[mid]:
#         return binary_search(ele, lst, mid, end)
#     elif ele < lst[mid]:
#         return binary_search(ele, lst, start, mid)    
    


# def solution(n,works):
#     works.sort()
#     while n > 0:
#         if sum(works) == 0:
#             return 0
#         temp = works.pop() - 1
#         print(temp, works)
#         # temp값을 이진탐색으로 정렬을 해치지 않는 순서에 넣는다.
#         # temp값과 같거나 or temp보다 큰요소, 작은요소 사이 인덱스를 구한다.
#         idx = binary_search(temp, works,0,len(works)-1)
#         # 그 요소에 temp를 넣는다.
#         works.insert(idx, temp)
#         n -=1
#     late_work = 0
#     for i in range(len(works)):
#         late_work += (works[i])**2
#     return late_work




# import heapq
# def solution(n,works):
#     # 최소힙을 활용하여 최대값을 출력하기위해 -1을 곱하였다.
#     for i in range(len(works)):
#         works[i] *= -1
#     # works를 heap 구조로 만든다.
#     heapq.heapify(works)
#     while True:
#         if sum(works) == 0:
#             return 0
#         temp = heapq.heappop(works)
#         heapq.heappush(works, temp+1)
#         n -=1
#         if n == 0:
#             break
#     print(works)
#     late_work = 0
#     for i in range(len(works)):
#         late_work += (works[i])**2
#     return late_work





# 문제를 잘못 해석

# def solution(n, works):
#     # 주어진 works의 총합
#     total = sum(works)
#     if n > total:
#         return 0
#     # 위 조건이 아니므로 total은 무조건 양수
#     total -= n
#     # 몫을 먼저 배치해주고 나머지를 추가해준다.
#     q, r = divmod(total, len(works))
#     works = [q] * len(works)
#     result = 0
#     for i in range(len(works)):
#         if r != 0:
#             result += ((works[i]+1)**2)
#             r -= 1
#         else:
#             result += ((works[i])**2)
#     return result
print(solution(1, [2, 1, 2]))

