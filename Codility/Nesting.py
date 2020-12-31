def solution(S: str) -> int:
    stack = []
    for bracket in S:
        if bracket == "(":
            stack.append("(")
            continue
        if not stack:
            return 0
        stack.pop()
    if stack:
        return 0
    return 1
