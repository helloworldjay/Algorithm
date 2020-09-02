def solution(people, limit):
    # 횟수를 카운트할 변수 생성
    cnt = 0
    # NlogN으로 people을 역순으로 정렬
    people.sort(reverse = True)
    # 50000명이 제한이므로 N^2는 2,500,000,000(25억)
    # N^2를 하면 속도 이슈 발생 확률이 높다.
    start, end = 0, len(people)-1
    while start <= end:
        # start위치에 있는 사람을 태우고 여분의 무게를 구한다.
        extra_weight = limit - people[start]
        # start를 한 칸 앞으로 이동
        start += 1
        # 뒤에 있는 사람이 탈 수 있으면 태운다.
        if people[end] <= extra_weight:
            end -= 1
        cnt += 1
    return cnt

## 틀린 풀이
## 너무 복잡하게 생각했다.


# def binary_search(lst, weight,start,end):
#     mid = (start+end)//2
#     if lst[mid] == weight :
#         return mid
#     elif start==end:
#         if lst[start] <= weight:
#             return start
#         else:
#             return -1
#     elif end - start == 1 :
#         if lst[start] > weight and lst[end] < weight:
#             return end
#     elif lst[mid] < weight:
#         binary_search(lst, weight, start, mid)
#     else:
#         binary_search(lst, weight, mid, end)
#     return -1

# def solution(people, limit):
#     # 횟수를 카운트할 변수 생성
#     cnt = 0
#     # NlogN으로 people을 역순으로 정렬
#     people.sort(reverse = True)
#     # 50000명이 제한이므로 N^2는 2,500,000,000(25억)
#     # N^2를 하면 속도 이슈 발생 확률이 높다.
#     # 모든 사람을 태웠는지 확인 할 리스트 생성
#     is_check = [False] * len(people)
#     # 첫번째 요소부터 꺼내오며 반복
#     for person in range(len(people)):
#         # (limit - 요소) 이하의 값이 리스트에 존재하는지 binary search로 탐색(logN)하여 인덱스 찾고 
#         # 이미 구한 사람이면 넘어간다.
#         if is_check[person]:
#             continue
#         # 사람 확인 리스트가 False인 경우만 넣고 아니면 다음값 
#         idx = binary_search(people, limit - people[person],person+1,len(people)-1)
#         second = -1
#         # limit - person보다 작은 값이 존재 한다면
#         if idx != -1 :
#             while True:
#                 # 마지막까지 다 구해졌다면
#                 if idx > len(is_check) -1:
#                     break
#                 # 아직 구해지지 않은 사람이라면
#                 if not is_check[idx]:
#                     second = idx
#                     break
#                 idx += 1
#         # 작은 값이 없다면 그냥 second = -1이므로 특별히 해줄 것이 없다.
#     # 먼저 태운 사람의 인덱스와 두번째가 존재 가능할 경우 태운 사람 리스트를 갱신(True)
#         is_check[person] = True
#         if second != -1:
#             is_check[second] = True
#         # 횟수를 1개 증가   
#         cnt += 1
#     return cnt

print(solution(	[70, 80, 50], 100))