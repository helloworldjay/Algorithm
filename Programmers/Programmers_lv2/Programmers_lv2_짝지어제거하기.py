def solution(s):
    # s를 전체 순회하며 stack에 저장하며 제거
    stack = []
    for i in range(len(s)):
        # 스택에 요소가 존재할 때
        if stack:
            if s[i] == stack[-1]:
                stack.pop()
            else :
                stack.append(s[i])
        else :
            stack.append(s[i])
    return 0 if stack else 1


