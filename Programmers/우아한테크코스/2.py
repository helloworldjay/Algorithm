def solution(s, op):
    decrypted = [] # 암호문 해독 결과
    for i in range(1, len(s)): # index기준 1부터 len(s)-1까지 op를 넣어본다
        decrypted.append(eval(s[:i]+op+str(int(s[i:])))) # 연산 결과를 반영
    return decrypted

print(solution("1234","+"))