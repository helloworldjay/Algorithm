


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