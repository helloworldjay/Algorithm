T = int(input())
for idx in range(T):
    s = list(input())
    # 들어오는 문자를 확인할 스택
    stack = []
    # stack에 채울 숫자를 하나하나 확인
    for i in range(len(s)):
        # stack이 비어있지 않고 넣으려는 값이랑 같은 값이 마지막에 존재하면
        # stack의 top 값을 제거한다.
        if stack and stack[-1] == s[i]:
            stack.pop()
        # 위의 상황이 아니면 s[i]를 추가한다.
        else:
            stack.append(s[i])
    print(f"#{idx+1} {len(stack)}")
    
