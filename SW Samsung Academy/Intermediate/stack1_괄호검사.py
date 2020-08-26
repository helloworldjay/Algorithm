
# testcase 개수
T = int(input())
for idx in range(T):
    # 짝을 확인 할 dictionary
    brackets = {'}':'{', ')':'('}
    # 입출력을 확인할 stack
    check = []
    testcase = list(input())
    is_Check = True
    for i in range(len(testcase)):
        # 괄호가 아니면 넘긴다.
        if testcase[i] not in brackets.keys() and testcase[i] not in brackets.values():
            continue
        # 만약 여는 괄호가 들어온다면 stack에 담는다.
        if testcase[i] in brackets.values():
            check.append(testcase[i])
        # 닫는 괄호가 들어올 때에는 check가 비어있거나 매칭이 안되면 False
        # 매칭이 되면 check에 있는 [-1]값을 pop 해준다.
        else :
            if not check or (brackets[testcase[i]] != check[-1]):
                is_Check = False
                break
            else :
                check.pop()    
    # 모든 연산이 끝나고 check가 비어있으면 True, check에 남은게 있으면 False가 된다.
    if not is_Check or check :
        print(f"#{idx+1} 0")
    else :        
        print(f"#{idx+1} 1")
    

