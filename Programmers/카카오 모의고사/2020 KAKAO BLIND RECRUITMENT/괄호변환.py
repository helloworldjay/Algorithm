# 45분
# 균형 잡힌 문자열로 분리
def balenced(p):
    # "(", ")"
    check = [0,0]
    for i in range(len(p)):
        if p[i] == "(": check[0] += 1
        else : check[1] += 1
        if check[0] == check[1]: return p[:i+1], p[i+1:]
    return p, ""
# 올바른 문자열인지 확인하는 함수
def correct(p):
    stack = []
    for i in range(len(p)):
        if p[i] == "(":
            stack.append("(")
        else:
            if not stack: return False
            else : stack.pop()
    # 다 돌았는데 stack이 남았으면 거짓, stack이 없으면 True
    if stack : return False
    return True

# 4-4를 구현
def cutting(u):
    # 만약 길이가 2보다 작으면 앞 뒤를 자를 수 없다.
    if len(u) < 2 :
        return ""
    else:
        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == "(": 
                u = u[:i] + ")" + u[i+1:]
                print(u)
            else: 
                u = u[:i] + "(" + u[i+1:]
                # print(u)
    return u

def solution(p):
    if p == "": return ""
    # 균형잡힌 문자열로 분리
    u, v = balenced(p)
    # 만약 u가 올바른 문자열이면
    if correct(u): return u + solution(v)
    # u가 올바른 문자열이 아니라면
    else:
        return "(" + solution(v) + ")" + cutting(u)

print(solution("()))((()"))
