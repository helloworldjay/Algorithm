# Laser를 뜻하는 ()를 L 로 바꾸고 빈 스택을 만들어 '(' 일 경우 스택에 추가하고, L이 나오면 스택의 길이만큼 추가하며 ')'의 경우는 스택에서 pop하며 1을 추가한다.

def solution(arrangement):
    arrangement = arrangement.replace("()", 'L') # 주어진 string의 ()를 L로 바꾼다.
    stk = [] # 빈 스택
    num = 0 # 막대의 개수
    for i in arrangement:
        if i == '(':
            stk.append('(')
        elif i == 'L':
            num += len(stk)
        else :
            stk.pop()
            num += 1 
    return num