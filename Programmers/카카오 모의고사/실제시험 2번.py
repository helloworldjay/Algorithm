from itertools import permutations
# expression이 가지고있는 연산자 종류를 구하고 우선순위 정하기
def opers(e):
    op = []
    if "+" in e :
        op.append("+")
    if "-" in e :
        op.append("-")
    if "*" in e :
        op.append("*")
    op = list(permutations(op))
    # index 0이 가장 높은 우선순위, 2가 가장 낮은 우선순위
    return op

def solution(expression):
    priority = opers(expression) # 연산자 우선순위
    mx = 0 # 연산 결과 최대값 저장
    # 연산자 1개 
    if len(priority) == 1:
        mx = eval(expression)
    # 연사자가 2개 
    elif len(priority) == 2:
        for idx in range(2):
            templist = expression.split(priority[idx][-1])
            for i in range(len(templist)):
                templist[i] = str(eval(templist[i]))
            templist = priority[idx][-1].join(templist)
            tempsum = eval(templist)
            if abs(tempsum) > mx :
                mx = abs(tempsum)
    # 연산자가 3개 
    else :
        # 6가지 경우의 수를 각각 계산한다.
        for idx in range(6):
            # 가장 하위 순위 연산으로 string을 split 해준다.
            templist = expression.split(priority[idx][-1])
            first = []
            second = [] # 두번째 연산이 필요한 목록을 저장할 리스트
            for i in range(len(templist)):
                try : # 단일 숫자라면 그냥 최종 계산에 넣어준다.
                    first.append(str(int(templist[i])))
                except : # 아니라면 재검색
                    second.append(templist[i])
            for i in range(len(second)):
                if priority[idx][1] in second[i]: # 연산이 2개 존재하는 항목
                    third = second[i].split(priority[idx][-2])
                    for j in range(len(third)):
                        third[j] = str(eval(third[j])) # 가장 우선순위 연산을 해주어 넣어준다.
                    first.append(str(eval(priority[idx][-2].join(third))))
                else : # 2번째 우선순위 연산이 없다면 그냥 연산해도 무방하다.
                    first.append(str(eval(second[i])))
            if mx < abs(eval(priority[idx][-1].join(first))) :
                mx = abs(eval(priority[idx][-1].join(first))) # 마지막 연산을 수행하여 하나로 합쳐준다.
    return mx


print(solution("100-200*300-500+20"))
