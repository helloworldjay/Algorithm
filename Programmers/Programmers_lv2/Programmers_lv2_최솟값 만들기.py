# 1차 실패
# def solution(A,B):
#     sum = 0
#     testnum = len(A)
#     for i in range(testnum):
#         sum += A.pop(A.index(max(A)))*B.pop(B.index(min(B)))
#     return sum

# # 2차 실패
# def solution(A,B):
#     sum = 0
#     testnum = len(A)
#     for i in range(testnum):
#         sum += max(A)*min(B)
#         A.remove(max(A))
#         B.remove(min(B)) 
#     return sum


def solution(A,B):
    sum = 0
    A.sort()
    B.sort(reverse = True)
    for i in range(len(A)):
        sum += A[i]*B[i] 
    return sum