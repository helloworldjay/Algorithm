def solution(expression):
    from itertools import permutations
    operations = [1, 2, 3]
    operation_priorities = list(permutations(operations, 3))
    priority_dict = {}
    result = 0
    for priority in operation_priorities:
        priority_dict["+"] = priority[0]
        priority_dict["-"] = priority[1]
        priority_dict["*"] = priority[2]
        oper_result = int(calculate_with_suffix(infix_to_suffix(expression, priority_dict)))
        result = max(abs(oper_result), result)
    return result

def infix_to_suffix(infix, priority):
    suffix = []
    stack = []
    temp = ""
    for token in infix:
        if token.isnumeric():
            temp += token
        else:
            suffix.append(temp)
            temp = ""
            if not stack or priority[stack[-1]] < priority[token]:
                stack.append(token)
            else:
                while stack:
                    if priority[stack[-1]] >= priority[token]:
                        suffix.append(stack.pop())
                    else:
                        break
                stack.append(token)
    suffix.append(temp)
    suffix.extend(stack[::-1])
    return suffix
def calculate_with_suffix(suffixes):
    stack = []
    for suffix in suffixes:
        if suffix.isdecimal():
            stack.append(suffix)
        else:
            latter = stack.pop()
            former = stack.pop()
            stack.append(str(eval(former+suffix+latter)))
    return stack[-1]

print(infix_to_suffix("50*6-3*2", {"+":0, "-":0, "*":1}))
print(calculate_with_suffix(infix_to_suffix("50*6-3*2", {"+":0, "-":0, "*":1})))

# 예전 풀이
from itertools import permutations
import math

# 리스트의 내용물을 편집할 때 길이가 바뀔 때에는 직접 리스트를 편집하는 것은 좋지 않다.

def solution2(expression):
    # 연산자의 우선 순위 정하기
    # expression을 순회하며 존재하는 연산자를 확인한다.
    opers = []
    for i in range(len(expression)):
        # 만약 i번째 요소가 연산자이면 연산자를 opers에 저장한다.
        if not expression[i].isdecimal() and expression[i] not in opers:
            opers.append(expression[i])
    # 연산자 우선순위를 결정한다.
    opers_priority = list(permutations(opers, len(opers)))
    # expression을 연산자를 기준으로 나눈다.
    idx = 0
    temp = []
    splited_expression = []
    # expression을 연산자를 기준으로 나누어 저장한다.
    while True:
        # 숫자이면 임시저장소에 저장
        if expression[idx].isdecimal():
            temp.append(expression[idx])
            # 마지막 요소라면 뒤에 연산자가 없으므로 바로 넣어주고 종료한다.
            if idx == len(expression)-1:
                splited_expression.append(''.join(temp))
            idx += 1
        # 연산자이면 기존에 저장되있던 요소와 연산자를 각각 splited_expression에 저장한다.
        else:
            splited_expression.append(''.join(temp))
            splited_expression.append(expression[idx])
            temp = []
            idx += 1
        # 끝까지 도달하면 종료
        if idx == len(expression):
            break
    max_val = -math.inf
    for i in range(len(opers_priority)):
        # 연산자 우선순위가 결정된 리스트
        order = opers_priority[i]
        temp_list = splited_expression[:]
        # 연산자 결정
        for j in range(len(order)):
            idx = 0
            while idx<len(temp_list):
                if temp_list[idx] == order[j]:
                    temp_list = temp_list[:idx-1]+[str(eval(''.join(temp_list[idx-1:idx+2])))]+temp_list[idx+2:]
                else:
                    idx += 1
        if abs(int(temp_list[0])) > max_val:
            max_val = abs(int(temp_list[0]))
    return max_val


