
# 실패한 코드
# def solution(n):
#     arr = []
#     for i in range(n//2):
#         arr.append("수박")
#         if n % 2 == 1:
#             arr.append("수")
#     return ''.join(arr)

# print(solution(4))

def solution(n):
    wm =''
    for i in range(n//2):
        wm += "수박"
    if n % 2 == 1 :
        wm += "수"
    return wm    
print(solution(5))