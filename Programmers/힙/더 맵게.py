import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while True:
        # 가장 작은 요소가 K보다 크면 끝난 것
        notspicy1 = heapq.heappop(scoville)
        if notspicy1 > K:
            return cnt
        # 가장 작은 요소가 K보다 작은 경우
        else :
            # 그런데 한개만 남고 더 섞을 수 없는 경우는 -1을 반환
            if len(scoville) == 0:
                return -1
            # 섞을 소스가 존재
            else :
                # 두번째로 안매운 소스를 뺀다
                notspicy2 = heapq.heappop(scoville)
                # 새로운 소스를 만든다
                newsauce = notspicy1 + (notspicy2*2)
                # 새로운 소스를 넣는다
                heapq.heappush(scoville, newsauce)
                # 횟수 추가
                cnt += 1

# 효율성 통과 못함
# def mix(a, b):
#     return a + b*2
# def solution(scoville, K):
#     cnt = 0 
#     while min(scoville) < K :
#         scoville.sort()
#         temp = mix(scoville[0],scoville[1])
#         del scoville[0:2]
#         scoville.insert(0, temp)
#         cnt += 1
#     return cnt