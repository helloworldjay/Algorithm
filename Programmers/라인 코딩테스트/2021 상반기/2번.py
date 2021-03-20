#2
def solution(inp_str):
    import string
    import collections
    brokenRule = []
    ruleTwoChecks = string.ascii_letters + string.digits + "~!@#$%^&*"
    ruleThreeChecks = [string.ascii_lowercase, string.ascii_uppercase, string.digits, "~!@#$%^&*"]
    def checkRuleTwo(inp_str):
        for oneLetter in inp_str:
            if oneLetter not in ruleTwoChecks:
                return False
        return True
    def checkRuleThree(inp_str):
        checked = [0 for _ in range(4)]
        for oneLetter in inp_str:
            for i in range(len(ruleThreeChecks)):
                if oneLetter in ruleThreeChecks[i]:
                    checked[i] = 1
                    break
        return sum(checked)
    def checkRuleFour(inp_str):
        cnt = 1
        for i in range(1, len(inp_str)):
            if inp_str[i-1] == inp_str[i]:
                cnt += 1
                if cnt >= 4:
                    return False
            else:
                cnt = 1
        return True
    if not (8 <= len(inp_str) <= 15):
        brokenRule.append(1)
    if not checkRuleTwo(inp_str):
        brokenRule.append(2)
    if checkRuleThree(inp_str) < 3:
        brokenRule.append(3)
    if not checkRuleFour(inp_str):
        brokenRule.append(4)
    if collections.Counter(inp_str).most_common(1)[0][1] >= 5:
        brokenRule.append(5)
    return brokenRule if len(brokenRule) != 0 else [0]

print(solution("aaaaZZZZ)"))
print(solution("CaCbCgCdC888834A"))
print(solution("UUUUU"))