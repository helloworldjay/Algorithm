# len(stk) != 0 조건을 생각 못함
# 조건이 닫힌 괄호를 받는 것이므로 key가 닫힌 괄호가 되어야하는데 열린괄호를 key로 해서 key error 발생
def isParenthesisValid(st):
    # 괄호의 쌍을 dict로 표현
    brpair = {"}":"{", ")":"(",">":"<","]":"["}
    # 열린 괄호
    obrkt = {"(","{","<","["}
    # 열린 괄호를 담을 스택
    stk = [] 

    for br in st:
        # 열린 괄호를 받을 때
        if br in obrkt:
            stk.append(br)
        # 닫힌 괄호를 받을 때
        else:
            if len(stk) != 0 and stk[-1] == brpair[br]:
                stk.pop()
            else:
                return False
    if stk :
        return False
    
    return True

def main():
    examples = ["({()})", "[]<>{}", ")(" "<]", "<(>)"]
    for example in examples:
        print(example, isParenthesisValid(example))

    
if __name__ == "__main__":
    main()
