class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {")": "(", "}": "{", "]": "["}
        for check in s:
            if check in bracket:
                if not stack or bracket[check] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(check)
        return False if stack else True
