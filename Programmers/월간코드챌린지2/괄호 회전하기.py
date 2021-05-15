def is_proper_bracket(candidates):
    stack = []
    pair = {"}":"{", ")":"(", "]":"["}
    for candidate in candidates:
        if candidate in pair.keys():
            if not stack or stack[-1] != pair[candidate]:
                return False
            stack.pop()
        else:
            stack.append(candidate)
    return False if stack else True

def solution(s):
    cnt = 0
    for i in range(len(s)):
        temp = s[i:] + s[:i]
        if is_proper_bracket(temp):
            cnt += 1
    return cnt

print(solution(	"[](){}"))
print(is_proper_bracket("[](){}"))