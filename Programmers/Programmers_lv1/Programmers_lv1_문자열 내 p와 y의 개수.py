def solution(s):
    if (s.lower().count('p') == s.lower().count('y')) or (s.lower().count('p') ==0 and s.lower().count('y') == 0) :
        return True
    else:
        return False

print(solution("pPY"))

