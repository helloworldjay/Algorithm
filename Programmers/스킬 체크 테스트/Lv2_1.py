# def solution(record):
#     # record의 기록을 하나씩 탐색
#     result = []
#     idnick = {} #id nickname 딕셔너리 
#     temp = []
#     for i in range(len(record)):
#         try :
#             order, userid, nickname = record[i].split()
#         except :
#             order, userid = record[i].split()
#         # nickname을 업데이트
#         if order == "Enter" or order == "Change":
#             idnick[userid] = nickname
#         temp.append([order,userid])
#     # 저장된 명령 리스트를 기준으로 문자열 반환
#     for i in range(len(temp)):
#         if temp[i][0] == "Enter":
#             result.append("{}님이 들어왔습니다.".format(idnick[temp[i][1]]))
#         elif temp[i][0] == "Leave":
#             result.append("{}님이 나갔습니다.".format(idnick[temp[i][1]]))
#     return result


#여러개의 최소공배수는 두 수의 최소공배수와 다른 수의 최소공배수를 반복하여 얻은 겨로가와 같다.
# 2개의 수의 최소공배수를 구하는 함수 만들기
def lcm(n1, n2):
    # gcd 부터 구하기
    # b에 큰 수 넣기
    a, b = n1, n2
    gcd = 0
    if a > b:
        a, b = b, a
    while True:
        if b % a != 0 :
            b, a = a, b%a
        else :
            gcd = a
            break
    return (n1*n2)//gcd    

def solution(arr):
    l = arr.pop() # 처음 값
    while arr :
        cur = arr.pop()
        l = lcm(cur, l)

    return l

print(lcm(12,7))