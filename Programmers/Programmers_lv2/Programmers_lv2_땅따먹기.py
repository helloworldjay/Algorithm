# # 1차 실패
# def solution(land):
#     temp = land[:]
#     firstidx = land[0].index(max(temp[0]))
#     temp[0].remove(max(temp[0]))
#     secondidx = land[0].index(max(temp[0]))
#     sum = land[0][firstidx]
#     for i in range(1, len(land)):
#         sum += max(temp[i].remove(firstidx))
#         firstidx = temp[i].remove(firstidx).index(max(temp[i].remove(firstidx)))
#     planA = sum
#     sum = land[0][secondidx]
#     for i in range(1, len(land)):
#         sum += max(temp[i].remove(secondidx))
#         secondidx = temp[i].remove(secondidx).index(max(temp[i].remove(secondidx)))
#     planB = sum
#     return planA if planA >= planB else planB

# def solution(land):
#     temp = land[:]
#     firstidx = land[0].index(max(temp[0]))
#     temp[0].remove(max(temp[0]))
#     secondidx = land[0].index(max(temp[0]))
#     planA = land[0][0]
#     # for i in range(1, len(land)):

#     return planA

def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][:j]+ land[i-1][j+1:])
            # max(land[i][(j+1)%4],land[i][(j+2)%4],land[i][(j+3)%4])
            # 도 가능한 표현이지만 j의 범위가 커지면 힘들어진다.
    return max(land[len(land)-1])
print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))


