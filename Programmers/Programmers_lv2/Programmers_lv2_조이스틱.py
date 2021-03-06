def solution(name):
    letter = "A" * len(name)
    # 움직여야하는 횟수
    cnt = 0
    # 관찰할 위치 인덱스
    idx = 0
    while True:
        change = ord(name[idx]) - ord("A")
        # 반대로 돌 수 있다.
        if change > 13 : change = 26 - change
        # 글자를 변경해준다.
        cnt += change
        name = name[:idx] + "A" + name[idx+1:]
        # print(cnt)
        # 같아졌으면 종료
        if letter == name:
            return cnt
        # 안 같기 때문에 좌 우를 결정해주어야 한다. 
        left, right = 0, 0
        ischeck_left, ischeck_right = True, True
        for i in range(1, len(name)):
            if name[(idx+i)%len(name)] != "A" and ischeck_right:
                right = i
                ischeck_right = False
            if name[(idx-i)] != "A" and ischeck_left:
                left = i
                ischeck_left = False
            if not ischeck_left and not ischeck_right:
                break
        # 오른쪽으로 더 많이 가야되면 왼쪽으로 가야한다.
        if right > left:
            idx = idx-left
            cnt += left
            if idx < 0: idx += len(name) 
        # 왼쪽으로 더 많이 가야되면 오른쪽으로 가야한다.
        else:
            cnt += right
            idx = (idx+right)%len(name)

print(solution("JEROEN"))

# 런타임에러 발생

# # 움직여야되는 횟수 찾는 함수
# def find_cnt(target):
#     return 26 - (ord(target) - 65) if ord(target) - 65 > 13 else (ord(target) - 65)

# def direction(idx, lst):
#     left = 0
#     right = 0
#     for i in range(1, len(lst)):
#         if lst[idx+i] != 0:
#             right = i
#             break
#     for i in range(1,len(lst)):
#         if lst[idx-i] != 0:
#             left = i
#             break
#     return -left if left < right else right

# def solution(name):
#     cnt = [0] * len(name)
#     for i in range(len(name)):
#         cnt[i] = find_cnt(name[i])
#     # 커서가 움직일 필요가 있는지 확인하기 위한 변수
#     total = sum(cnt)
#     # 커서의 위치 index
#     idx = 0
#     # 총 커서의 횟수를 담을 변수
#     result = 0
#     while True:
#         result += cnt[idx]
#         total -= cnt[idx]
#         cnt[idx] = 0
#         if total <= 0:
#             break
#         # 커서를 얼마만큼 움직여야 하는지 정해주는 함수
#         move = direction(idx, cnt)
#         idx = (idx+move)+len(cnt) if (idx+move)<0 else ((idx+move)%(len(cnt)))
#         result += abs(move)
#     return result






















# def direction(lst, idx):
#     right = 0
#     left = 0
#     # 움직여야 하는 방향을 출력해주는 함수
#     # idx를 기준으로 lst를 양쪽으로 정확히 절반으로 바꿔야할 개수를 count해준다   
#     for i in range(1, len(lst)-1):
#         if lst[(i+idx)%len(lst)] != 0 :        
#             right = i
#             break
#     for i in range(1, len(lst)-1):
#         if lst[idx-i] != 0 :
#             left = i
#             break
#     return left, right

# def solution(name):
#     # 전체 횟수
#     total_cnt = 0
#     # 처음에는 A로만 이루어져있다.
#     target = "A" * len(name)
#     # 아스키코드 65 ~ 90
#     # 각 자리수별로 움직여야되는 횟수를 저장
#     cnt = [0]*len(name)
#     for i in range(len(name)):
#         # cnt의 i번째 요소는 name의 i번째 요소를 만들기 위한 횟수
#         cnt[i] = find_cnt(name[i])
#     # 이동할 인덱스
#     idx = 0
#     while True:
#         # idx 위치의 알파벳을 바꿔준다
#         total_cnt += cnt[idx]
#         # 변경되었으므로 cnt를 초기화
#         cnt[idx] = 0
#         # 모든 요소가 0이면 반환하고 함수 종료
#         if sum(cnt) == 0:
#             return total_cnt
#         # idx에서 어느 방향으로 움직여야할지 결정해주는 함수
#         left, right = direction(cnt,idx)
#         if left > right:
#             idx += right
#             total_cnt += right
#         else :
#             idx -= left
#             total_cnt += left
#     return total_cnt
# print(solution("BBBAAAB"))
# # 0000000    9


# def direction(lst, idx):
#     right = 0
#     left = 0
#     # 움직여야 하는 방향을 출력해주는 함수
#     # idx를 기준으로 lst를 양쪽으로 정확히 절반으로 바꿔야할 개수를 count해준다
#     for i in range(idx+1, idx+(len(lst)//2)+1):
#         if lst[i%len(lst)] != 0 :
#             right += 1
#     for i in range(idx-1, idx-1-(len(lst)//2),-1):
#         if lst[i%len(lst)] != 0 :
#             left += 1
#     # 오른쪽으로 바꿔야될 수가 더 많으면 오른쪽으로 이동
#     if right >= left :
#         return True
#     # 왼쪽으로 바꿔야될 수가 더 많으면 왼쪽으로 이동 
#     else :
#         return False