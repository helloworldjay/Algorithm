import math
def solution(n,k):
    # n명의 사람 리스트
    lst = [i for i in range(1,n+1)]
    result = []
    # 조건을 만족할 때까지 순회
    while True:
        quo = math.factorial(len(lst)-1)
        # 몫, 나머지
        q, r = divmod(k, quo)
        # 나머지가 0이면 lst의 남은 값들을 역순으로 result에 붙인다.
        if r == 0:
            result.append(lst[q-1])
            lst = lst[:q-1] + lst[q:]    
            result += lst[::-1]
            break
        result.append(lst[q])
        # lst의 q 인덱스 요소를 삭제하고 result에 삽입
        lst = lst[:q] + lst[q+1:]
        k = r
    return result

print(solution(3,5))