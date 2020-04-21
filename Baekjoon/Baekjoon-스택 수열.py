n = int(input()) # 넣을 숫자 수
stk = [] # 숫자를 넣을 스택
seq = [] # + - 넣는 곳
val = 1 # 스택에 넣을 숫자의 초기값
prob = [] # 문제를 넣을 수열 
for i in range(n):
    temp = int(input()) # 수열에 넣은 수
    prob.append(temp)

for i in range(n):
    while prob[i] >= val :
        seq.append('+')
        stk.append(val)
        val += 1
    if prob[i] == stk[-1] :
        seq.append('-') 
        stk.pop()    
    else :
        print('NO')
        exit(0)
print('\n'.join(seq))

    

    

