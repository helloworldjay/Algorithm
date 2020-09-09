
def check(stones,k,mid):
    # 연속으로 0의 개수가 얼마인지 확인
    cnt = 0
    for stone in stones:
        stone -= (mid-1)
        if stone <= 0: 
            cnt += 1
            if cnt == k:
                return False
        else:
            cnt = 0
    return True

def solution(stones, k):
    start = 0
    end = max(stones)
    while True:
        mid = (start+end)//2
        # 만약 mid만큼의 사람수가 건널 수 있다고 하면
        if check(stones, k, mid):
            start = mid
        else:
            end = mid
        if end-start <= 1:
            return start if not check(stones,k,end) else end

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))

# 정확도만 통과

# def check(stones, k):
#     num = 0
#     for i in range(len(stones)):
#         if stones[i] == 0 :
#             num += 1
#             if num == k:
#                 return True
#         else:
#             num = 0
#     return False

    
# def solution(stones, k):
#     cnt = 0
#     while True:
#         # 0이 존재하는지 확인
#         # 0*k가 stones에 존재하면 종료
#         if check(stones,k,0,len(stones)-1):
#             return cnt
#         # 존재 안하면 한번씩 더 빼주기
#         for i in range(len(stones)):
#             if stones[i] != 0: stones[i] -= 1
#         cnt += 1
