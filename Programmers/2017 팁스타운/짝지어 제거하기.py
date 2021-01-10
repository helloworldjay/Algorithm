def solution(s: str) -> int:
    stack = []
    for i in range(len(s)):
        if not stack or stack[-1]!=s[i]:
            stack.append(s[i])
            continue
        stack.pop()
    return 0 if stack else 1


print(solution("dladiffaea"))
