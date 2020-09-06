def solution(number, k):
    stack = ["0"]
    # 처음 빈문자를 넣었으므로 0을 지우기 위해 k를 하나 증가시킨다.
    k += 1
    for i in range(len(number)):
        if k == 0:
            stack.append(number[i])
            continue
        while k > 0:
            # 비어있지 않으면 number[i]로 계속 비교해 나간다. stack의 마지막 값보다
            # number[i]가 더 크면 stack[-1]을 제거해 나간다.
            if number[i] > stack[-1]:
                stack.pop()
                k -= 1
            if len(stack) == 0 or number[i] <= stack[-1] or k==0 :
                stack.append(number[i])
                break
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
print(solution("999", 2))



# # 왜 에러가 나는지 모르겠다.
# def solution(number, k):
#     result_len = len(number) - k
#     max_idx = 0
#     result = []
#     # 과정을 반복한다.
#     # 커서의 위치 인덱스
#     idx = 0
#     while True :
#         # number[idx:idx+k] 중에서 최대값 인덱스 찾기
#         # 부분 최대값의 인덱스는 max_idx
#         max_idx = number[idx:idx+k+1].find(max(number[idx:idx+k+1]))
#         # idx += (max_idx + 1)
#         idx += max_idx + 1
#         if idx == len(number) - k:
#             return number[:idx]
#         # 최대값만 result에 담는다.
#         result += number[idx-1]
#         # k -= max_idx
#         k -= max_idx if max_idx != 0 else 1
#         # k == 0 이면 result += number[idx:]
#         if k <= 0:
#             result += number[idx:]
#             break
#     return ''.join(result) if len(result) == result_len else ''.join(result[:-(len(result)-result_len)])

#지원
# def solution(number, k):

#     max_num =[]

#     for idx,num in enumerate(number):
#         #                          이전 숫자    현재 숫자 제거된 숫자 카운트 용
#         while len(max_num) >0 and max_num[-1] < num and k >0:
#             max_num.pop()
#             k-=1 # 숫자 카운트
#         if k==0: #제거된 횟수를 다 썻댜
#             max_num+= list(number[idx:])
#             break
#         max_num.append(num)
#     print(max_num)
#     # 이 조건 이해가 안감
#     # 숫자가 내림차순
#     #9876
#     if k>0:
#         max_num = max_num[:-k] 
#     # k가 0 이면 빈 리스트가 되기 때문에 if를 이용해서 조건을 걸어준다.
#     answer = ''.join(max_num)



# 용철
# def solution(number, k):
#     start = 1
#     while k != 0:
#         check = True
#         for i in range(start,len(number)):
#             if number[i-1] < number[i]:
#                 number = number[:i-1] + number[i:]
#                 k -= 1
#                 if i-1 <= 0:
#                     start = 1
#                 else:
#                     start = i - 1
#                 check = False
#                 break
#         if check == True:
#             number = number[:len(number)-k]
#             break
#     return number






# def find_max(string):
#     max_num = "0"
#     max_idx = 0
#     for i in range(len(string)):
#         if string[i] > max_num :
#             max_num = string[i]
#             max_idx = i
#     return max_idx

# # 왜 에러가 나는지 모르겠다.
# def solution(number, k):
#     max_idx = 0
#     result = []
#     # 과정을 반복한다.
#     # 커서의 위치 인덱스
#     idx = 0
#     while True :
#         # number[idx:idx+k] 중에서 최대값 인덱스 찾기
#         # 부분 최대값의 인덱스는 max_idx
#         max_idx = find_max(number[idx:idx+k+1])
#         # idx += (max_idx + 1)
#         idx += (max_idx + 1)
#         # 최대값만 result에 담는다.
#         result += number[idx-1]
#         # k -= max_idx
#         k -= max_idx
#         # k == 0 이면 result += number[idx:]
#         if k == 0:
#             result += number[idx:]
#             break
#     return ''.join(result)